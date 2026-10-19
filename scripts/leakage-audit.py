#!/usr/bin/env python3
"""leakage-audit -- no gold-dataset identifier may appear in the corpus.

The gold evaluation dataset (archi-crab-gold-dataset) must never leak into the knowledge the
agent is evaluated against: not a ticket's thread text, not its usernames, task names or DDM
ids, not a cms-talk thread id. This script builds the needles from a gold checkout and scans
corpus data (every records.json under deployments/archi-crab/data/docs, or any files given)
for them. Exit 1 on any hit. Run it on every corpus PR and on the cms-crab-docs merge request
that publishes doc proposals.

  scripts/leakage-audit.py --gold ~/src/archi-crab-gold-dataset            # scans data/docs/*/records.json
  scripts/leakage-audit.py --gold ~/src/archi-crab-gold-dataset path/to/pages/*.md

Needles (all from the gold checkout, never written anywhere): every string value in a ticket's
metadata.external_ids (task names like 260925_212625:user_crab_..., usernames, DDM request ids,
cms_site values are skipped: site names are public vocabulary), every provenance_id
(cms-talk:<id>:qa-N), the thread id forms `cms-talk:<id>` and `cms-talk.web.cern.ch/t/.../<id>`,
and the literal `thread_excerpts` sentences (first 80 characters of each). Short or generic
values (< 6 characters) are ignored.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

# public vocabulary the corpus legitimately contains: never a needle
GENERIC_KINDS = {"cms_site", "site", "dataset", "block_name", "exit_code", "error_code", "cmssw_release", "scram_arch",
                 "github_issue", "github_pull_request"}
THREAD_RE = re.compile(r"cms-talk\.web\.cern\.ch/t/[^/\s]+/(\d+)")


def needles_from_gold(gold):
    needles = {}  # needle -> provenance
    thread_ids = {}  # cms-talk thread number -> ticket id
    tickets = glob.glob(os.path.join(gold, "tier-*", "**", "*.json"), recursive=True)
    if not tickets:
        sys.exit("no tickets under %s/tier-*: is this the gold checkout?" % gold)
    for f in tickets:
        try:
            t = json.load(open(f, encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            print("skip %s: %s" % (f, exc), file=sys.stderr)
            continue
        tid = t.get("id") or os.path.basename(f)
        m = t.get("metadata") or {}
        pid = str(m.get("provenance_id") or "")
        if pid:
            needles[pid] = tid
            num = re.search(r"cms-talk:(\d+)", pid)
            if num:
                needles["cms-talk:%s" % num.group(1)] = tid
                thread_ids[num.group(1)] = tid
        ext = m.get("external_ids") or []
        pairs = ext.items() if isinstance(ext, dict) else [(e.get("kind"), e.get("ids")) for e in ext if isinstance(e, dict)]
        for kind, vals in pairs:
            if kind in GENERIC_KINDS:
                continue
            for v in (vals if isinstance(vals, list) else [vals]):
                if isinstance(v, str) and len(v.strip()) >= 6:
                    needles[v.strip()] = "%s external_ids.%s" % (tid, kind)
        for ex in (m.get("thread_excerpts") or []):
            text = ex.get("text") if isinstance(ex, dict) else ex
            if isinstance(text, str):
                s = " ".join(text.split())[:80]
                if len(s) >= 40:
                    needles[s] = "%s thread_excerpts" % tid
    return needles, thread_ids


def scan_text(text, needles, thread_ids, where, hits):
    for n, prov in needles.items():
        if n in text:
            hits.append((where, n[:60], prov))
    for m in THREAD_RE.finditer(text):   # a link to the forum is fine; a link to a gold thread is not
        if m.group(1) in thread_ids:
            hits.append((where, m.group(0)[:60], "%s thread URL" % thread_ids[m.group(1)]))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("--gold", required=True, help="checkout of archi-crab-gold-dataset (read only)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("paths", nargs="*", help="files to scan (default: every data/docs/*/records.json)")
    a = ap.parse_args(argv)
    needles, thread_ids = needles_from_gold(a.gold)
    paths = a.paths or sorted(glob.glob(os.path.join(a.repo, "deployments", "archi-crab", "data", "docs", "*", "records.json")))
    hits, scanned = [], 0
    for p in paths:
        if p.endswith("records.json"):
            for r in json.load(open(p, encoding="utf-8")):
                scanned += 1
                scan_text("%s\n%s\n%s" % (r.get("title", ""), r.get("url", ""), r.get("body", "")), needles, thread_ids, "%s %s" % (os.path.relpath(p, a.repo), r.get("url")), hits)
        else:
            scanned += 1
            scan_text(open(p, encoding="utf-8", errors="replace").read(), needles, thread_ids, p, hits)
    for where, n, prov in hits:
        print("HIT  %s\n     needle %r  (from %s)" % (where, n, prov))
    print("leakage audit: %d needle(s) + %d gold thread ids from %s, %d record(s)/file(s) scanned, %d hit(s)" % (len(needles), len(thread_ids), a.gold, scanned, len(hits)))
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
