#!/usr/bin/env python3
"""harvest-gh-threads -- GitHub issues, pull requests and commits as docs-build.py pages.

okg has no connector for GitHub issue or PR threads (only the `github_issue_ref` URL-mention
extractor), and its git-history lane carries commits, not discussions. Until a native
connector exists, a `docs-files` source holds the threads: one page per issue or PR (title,
state, dates, labels, body, every comment), one page per named commit (message + --stat), and
one page per per-file history, each keyed by its canonical public GitHub URL, which is also
what a `github_issue_ref` mention carries (DocumentationPage.okg_alias_fields: url).

Needs the `gh` CLI, authenticated (`gh auth status`), for issues/PRs; a local clone for
commits and histories. Writes <out>/<slug>-{issue,pull,commit,history}-<n>.md and urls.tsv
(docs-build.py --urls), plus manifest.json (fetched_at, counts, the highest issue number seen:
a later refresh is a diff).

  # the class: every issue and PR of a repo (all states), comments included
  scripts/harvest-gh-threads.py --repo dmwm/CRABServer --repo dmwm/CRABClient --out .../pages
  # named threads in other repos
  scripts/harvest-gh-threads.py --repo cms-sw/cmssw --numbers 38017,38622,38678 --out .../pages
  # commits and per-file histories, from a clone
  scripts/harvest-gh-threads.py --repo dmwm/CRABServer --clone ~/src/CRABServer \\
      --commits 052d399,e7c14e3 --history src/python/ServerUtilities.py --out .../pages
  python3 scripts/docs-build.py --src .../pages --out .../github-threads-crabserver \\
      --urls .../pages/urls.tsv --site-name github.com --strict --report /tmp/r.csv

Bots (logins ending in [bot]) are dropped. Nothing is rewritten: the text is the public
thread. Keep one source per repository (one records.json each) so a large tracker does not
become one huge file.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path


def gh(args, paginate=False):
    cmd = ["gh", "api"] + (["--paginate"] if paginate else []) + args
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        sys.exit("gh api %s failed: %s" % (" ".join(args), p.stderr.strip()[:300]))
    text = p.stdout.strip()
    if paginate and text.startswith("["):
        # --paginate concatenates JSON arrays; join them
        parts = text.replace("]\n[", ",").replace("][", ",")
        return json.loads(parts)
    return json.loads(text) if text else None


def is_bot(user):
    return not user or str(user.get("login", "")).endswith("[bot]")


def render_thread(repo, item, comments, kind):
    n = item["number"]
    lines = ["# %s %s #%d: %s" % (repo, "pull request" if kind == "pull" else "issue", n, item.get("title") or ""), ""]
    meta = ["State: %s" % item.get("state"), "Opened: %s" % item.get("created_at")]
    if item.get("closed_at"):
        meta.append("Closed: %s" % item["closed_at"])
    if kind == "pull" and item.get("pull_request", {}).get("merged_at"):
        meta.append("Merged: %s" % item["pull_request"]["merged_at"])
    labels = [lb.get("name") for lb in item.get("labels") or []]
    if labels:
        meta.append("Labels: %s" % ", ".join(labels))
    if item.get("milestone"):
        meta.append("Milestone: %s" % item["milestone"].get("title"))
    meta.append("URL: %s" % item.get("html_url"))
    lines += meta + ["", "## Opening post (%s, %s)" % ((item.get("user") or {}).get("login", "?"), item.get("created_at")), "",
                     (item.get("body") or "").strip() or "(no text)", ""]
    for c in comments:
        if is_bot(c.get("user")):
            continue
        lines += ["## Comment (%s, %s)" % ((c.get("user") or {}).get("login", "?"), c.get("created_at")), "",
                  (c.get("body") or "").strip() or "(no text)", ""]
    return "\n".join(lines)


def git(clone, *args):
    p = subprocess.run(["git", "-C", clone] + list(args), capture_output=True, text=True)
    if p.returncode:
        sys.exit("git %s failed: %s" % (" ".join(args), p.stderr.strip()[:300]))
    return p.stdout


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("--repo", action="append", required=True, help="org/name (repeatable)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--state", default="all", choices=["all", "open", "closed"])
    ap.add_argument("--since", help="only issues/PRs created on or after YYYY-MM-DD")
    ap.add_argument("--numbers", help="comma-separated issue/PR numbers (default: every one)")
    ap.add_argument("--no-threads", action="store_true", help="skip issues/PRs (commits/histories only)")
    ap.add_argument("--clone", help="local clone of the (single) --repo, for --commits and --history")
    ap.add_argument("--commits", help="comma-separated commit shas (needs --clone)")
    ap.add_argument("--history", action="append", default=[], help="path whose commit history to dump (needs --clone; repeatable)")
    ap.add_argument("--branch", default="master", help="branch name for the history URLs")
    a = ap.parse_args(argv)

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    urls = []
    manifest = {"tool": "scripts/harvest-gh-threads.py", "repos": {}, "fetched_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    numbers = {int(x) for x in a.numbers.split(",")} if a.numbers else None

    for repo in a.repo:
        slug = repo.split("/", 1)[1].lower().replace(".", "-")
        info = {"threads": 0, "commits": 0, "histories": 0, "highest_number": 0, "skipped_bots": 0}
        if not a.no_threads:
            items = gh(["repos/%s/issues?state=%s&per_page=100&sort=created&direction=asc" % (repo, a.state)], paginate=True) or []
            for item in items:
                n = item["number"]
                if numbers is not None and n not in numbers:
                    continue
                if a.since and str(item.get("created_at", ""))[:10] < a.since:
                    continue
                kind = "pull" if item.get("pull_request") else "issue"
                comments = gh(["repos/%s/issues/%d/comments?per_page=100" % (repo, n)], paginate=True) or [] if item.get("comments") else []
                name = "%s-%s-%d.md" % (slug, kind, n)
                (out / name).write_text(render_thread(repo, item, comments, kind), encoding="utf-8")
                urls.append((name, item["html_url"], "%s %s #%d: %s" % (repo, "PR" if kind == "pull" else "issue", n, item.get("title") or "")))
                info["threads"] += 1
                info["highest_number"] = max(info["highest_number"], n)
                print("ok %s" % name)
        if a.clone and (a.commits or a.history):
            for sha in (a.commits.split(",") if a.commits else []):
                full = git(a.clone, "rev-parse", sha).strip()
                show = git(a.clone, "show", "--stat", "--format=# %s%n%nCommit %H%nAuthor: %an%nDate: %ci%n%n%b", full)
                name = "%s-commit-%s.md" % (slug, full[:12])
                (out / name).write_text(show, encoding="utf-8")
                subject = git(a.clone, "log", "-1", "--format=%s", full).strip()
                urls.append((name, "https://github.com/%s/commit/%s" % (repo, full), "%s commit %s: %s" % (repo, full[:7], subject)))
                info["commits"] += 1
                print("ok %s" % name)
            for path in a.history:
                log = git(a.clone, "log", "--date=iso", "--format=%h %ad %an: %s%n%b", "--", path)
                head = git(a.clone, "rev-parse", "HEAD").strip()
                name = "%s-history-%s.md" % (slug, path.replace("/", "_"))
                text = "# %s: commit history of %s (at %s)\n\nURL: https://github.com/%s/commits/%s/%s\n\n%s" % (repo, path, head[:12], repo, a.branch, path, log)
                (out / name).write_text(text, encoding="utf-8")
                urls.append((name, "https://github.com/%s/commits/%s/%s" % (repo, a.branch, path), "%s: commit history of %s" % (repo, path)))
                info["histories"] += 1
                print("ok %s" % name)
        manifest["repos"][repo] = info
    with open(out / "urls.tsv", "a", encoding="utf-8") as f:
        if f.tell() == 0:
            f.write("# <file name><TAB><url><TAB><title>  -- written by scripts/harvest-gh-threads.py; docs-build.py --urls input\n")
        for name, url, title in urls:
            f.write("%s\t%s\t%s\n" % (name, url, title.replace("\t", " ")))
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("wrote %d pages -> %s" % (len(urls), out))


if __name__ == "__main__":
    main()
