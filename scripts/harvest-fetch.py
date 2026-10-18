#!/usr/bin/env python3
"""harvest-fetch -- fetch a list of PUBLIC URLs into a folder that docs-build.py reads.

One record of a `docs-files` source = one public URL (its identity) + the bytes behind it.
This script fetches those bytes once, anonymously, and writes next to them everything a
rebuild needs: `urls.tsv` (<file name><TAB><url>[<TAB><title>], the --urls input of
docs-build.py) and `manifest.json` (fetched_at, sha256, status per file). It refuses a
CERN login page captured instead of the page (same test as docs-build) and any URL that
needs a cookie or token: a record v2 cannot fetch anonymously does not belong in the
public corpus (docs/RELEASES.md; the action plan's sensitivity ledger).

  scripts/harvest-fetch.py --list snapshots.tsv --out deployments/archi-crab/data/docs/code-snapshots/pages
  python3 scripts/docs-build.py --src .../code-snapshots/pages --out .../code-snapshots \\
      --urls .../code-snapshots/pages/urls.tsv --site-name raw.githubusercontent.com --strict --report /tmp/r.csv

The list is a TSV: <file name><TAB><url>[<TAB><title>]. File names end in .html, .md or
.txt (docs-build's formats): a code file or a plain-text page is saved as .txt. A raw
GitHub URL pinned to a commit (raw.githubusercontent.com/<org>/<repo>/<sha>/<path>) gives
every engine the same bytes; a live page gives same-day-identical bytes.

Needs python3 >= 3.9 and network; no credentials, ever.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

LOGIN_RE = re.compile(r"auth\.cern\.ch/auth/realms|Sign in with your CERN|CERN Single Sign-On|login\.cern\.ch", re.I)
UA = "archi-crab-okg harvest-fetch/1 (+https://github.com/nausikt/archi-crab-okg)"


def read_list(path):
    rows = []
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("\t")]
        if len(parts) < 2 or not parts[1].startswith(("http://", "https://")):
            sys.exit("%s:%d: expected <file name><TAB><url>[<TAB><title>]" % (path, n))
        if not parts[0].lower().endswith((".html", ".htm", ".md", ".txt")):
            sys.exit("%s:%d: %s must end in .html, .md or .txt (docs-build's formats)" % (path, n, parts[0]))
        rows.append((parts[0], parts[1], parts[2] if len(parts) > 2 else ""))
    names = [r[0] for r in rows]
    dup = sorted({n for n in names if names.count(n) > 1})
    if dup:
        sys.exit("duplicate file names in the list: %s" % ", ".join(dup))
    return rows


def fetch(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status, resp.geturl(), resp.headers.get("Content-Type", ""), resp.read()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("--list", required=True, help="TSV: <file name><TAB><url>[<TAB><title>]")
    ap.add_argument("--out", required=True, help="folder to write the files, urls.tsv and manifest.json into")
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--min-bytes", type=int, default=200)
    ap.add_argument("--refetch", action="store_true", help="fetch again even when the file exists with the same sha256 in manifest.json")
    a = ap.parse_args(argv)

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    rows = read_list(a.list)
    manifest_path = out / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {"files": {}}
    bad = 0
    for name, url, title in rows:
        dest = out / name
        entry = {"url": url, "title": title}
        try:
            status, final_url, ctype, data = fetch(url, a.timeout)
            entry.update(status=status, final_url=final_url, content_type=ctype, bytes=len(data))
            text = data.decode("utf-8", errors="replace")
            if final_url != url and ("auth.cern.ch" in final_url or "login" in final_url.lower()):
                entry["result"] = "redirected_to_login"
            elif len(data) < 20000 and LOGIN_RE.search(text):
                entry["result"] = "login_page"
            elif len(data) < a.min_bytes:
                entry["result"] = "too_short"
            else:
                entry["result"] = "ok"
        except urllib.error.HTTPError as exc:
            entry.update(status=exc.code, result="http_error")
        except Exception as exc:  # noqa: BLE001 -- report and go on
            entry.update(result="error", error=str(exc)[:200])
        if entry["result"] != "ok":
            bad += 1
            print("REFUSED %-50s %s (%s)" % (name, entry["result"], entry.get("status", "")), file=sys.stderr)
            if dest.exists():
                dest.unlink()
            manifest["files"][name] = entry
            continue
        dest.write_bytes(data)
        entry["sha256"] = hashlib.sha256(data).hexdigest()
        entry["fetched_at"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        manifest["files"][name] = entry
        print("ok      %-50s %7d bytes  %s" % (name, len(data), url))
    # the two files docs-build needs: urls.tsv (its --urls) and a dated manifest
    with open(out / "urls.tsv", "w", encoding="utf-8") as f:
        f.write("# <file name><TAB><url>[<TAB><title>]  -- written by scripts/harvest-fetch.py; docs-build.py --urls input\n")
        for name, url, title in rows:
            if manifest["files"].get(name, {}).get("result") == "ok":
                f.write("%s\t%s%s\n" % (name, url, ("\t" + title) if title else ""))
    manifest["tool"] = "scripts/harvest-fetch.py"
    manifest["list"] = str(a.list)
    manifest["written_at"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest_path.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    ok = sum(1 for e in manifest["files"].values() if e.get("result") == "ok")
    print("%d fetched, %d refused -> %s (urls.tsv, manifest.json)" % (ok, bad, out))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
