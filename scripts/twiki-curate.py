#!/usr/bin/env python3
"""twiki-curate — build a small, CRAB-scoped TWiki snapshot from the big one.

Runs where the full snapshot is readable (lxplus reads /eos with your own
Kerberos ticket). Needs only python3 >= 3.9: no archi, no okg, no network.
Copies the selected raw topic files UNCHANGED (%META lines included) into one
directory per web, which is exactly what archi's TWiki reader ingests:

  deployments/archi-crab/data/twiki/<Web>/<Topic>.txt     (docs/ONBOARDING.md §3)

  python3 scripts/twiki-curate.py \\
      --src /eos/cms/store/group/internal_comm/twiki/CMS/topics \\
      --out deployments/archi-crab/data/twiki/CMS \\
      --report /tmp/curate-CMS.csv --dry-run          # review, then drop --dry-run

One decision per topic, in this order (the CSV has the reason for each):
  exclude   name matches --exclude                        -> dropped
  name      name matches --include                        -> kept   (a seed)
  physics   name is a physics page (PAG code, POG, workbook roots)  -> dropped
  content   body has >= --min-hits matches of --content   -> kept   (a seed)
  parent    %META:TOPICPARENT chain reaches a kept seed   -> kept
  unmatched everything else                               -> dropped

--include/--exclude/--content ADD to the defaults below (--no-defaults to
replace them). The physics patterns and the skipped-file patterns are archi's
own (checked in CI so they cannot drift). Refresh: re-run, then
`git add -A deployments/archi-crab/data/twiki && git diff --cached --stat`
shows which pages appeared, changed or went away (new files are untracked
until added, so plain `git diff` would hide them).
"""
import argparse
import csv
import os
import re
import shutil
import sys
from collections import Counter

INCLUDE = [
    r"(?i)crab", r"(?i)asyncstageout", r"(?i)taskworker", r"^Site(Status|Readiness)",
    r"(?:^|(?<=[a-z0-9])|(?<=CMS))DBS(?!CAN)", r"(?i)rucio", r"(?i)condor", r"(?i)glidein",
    r"^SubmissionInfrastructure", r"(?i)globalpool", r"(?:^|(?<=[a-z0-9])|(?<=CMS))FTS",
    r"(?i)xrootd", r"(?i)xrdcp", r"(?:^|(?<=[a-z0-9])|(?<=CMS))AAA(?![a-z])", r"(?i)webdav",
    r"(?:^|(?<=[a-z0-9])|(?<=CMS))CRIC", r"(?i)siteconf", r"^CMSSW", r"(?i)scram",
    r"[Cc]msRun", r"^WMCore",
]
EXCLUDE = [r"(?i)crab2(?![0-9])", r"(?i)^(?!.*crab).*sandbox"]
CONTENT = [
    r"\bCRAB3?\b",
    r"\bcrab (?:submit|status|resubmit|getoutput|getlog|report|kill|checkwrite)\b",
    r"\bAsyncStageOut\b|\bASO\b",
    r"\bTaskWorker\b",
]
# Copied from archi-okg python/archi/sources/_twiki_physics.py (stage 1 allow-list);
# ci.yaml okg-validate asserts these equal the pinned archi's, so they cannot drift.
PAG_CODE_RE = re.compile(
    r"^(HIG|TOP|SUS|SMP|B2G|BPH|BTV|EXO|FTR|HIN|JME|MUO|TAU|TRK|EGM|PPS|FSQ)"
    r"[-_]?[0-9]"
)
POG_NAME_RE = re.compile(r"^(Muon|Egamma|JetMET|BTag|Tau|Tracking|Trigger|AlCa)")
PHYSICS_ROOT_RE = re.compile(
    r"^(Higgs|SUSY|Exotica|WorkBook|PhysicsResults|StandardModel|HeavyIons"
    r"|HeavyFlavor|SWGuidePhysics|Top[A-Z0-9])"
)
# Copied from archi-okg python/archi/sources/_twiki_parse.py DEFAULT_SKIP_PATTERNS
# (matched against the FILE name): files the reader never ingests are not
# copied either, so "kept" here == pages ingested. CI checks this too.
DEFAULT_SKIP_PATTERNS = (
    r"^[0-9]+\.txt$",
    r"^[0-9]{6,8}[A-Za-z]",
    r"^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}",
    r"-replies\.txt$",
    r"^[a-z]",
    r"^Web(Atom|Changes|CreateNewTopic|Index|LeftBar|Notify|Preferences|"
    r"Rss|Search|SearchAdvanced|Statistics|TopicCreator|TopicEditTemplate|"
    r"TopicList|TopMenu|BottomBar)\.txt$",
    r"^(LastViewedTopics|TWeederSummaryViews|SearchResults)\.txt$",
)
SKIP = re.compile("|".join("(?:%s)" % p for p in DEFAULT_SKIP_PATTERNS))
PARENT_RE = re.compile(r'%META:TOPICPARENT\{[^}]*name="([^"]+)"', re.I)
META_RE = re.compile(r"%META:[^%]*%")
MARKER = ".curated"
KEPT = ("name", "content", "parent")


def is_physics(topic):
    return bool(PAG_CODE_RE.match(topic) or POG_NAME_RE.match(topic) or PHYSICS_ROOT_RE.match(topic))


def family(topic):
    m = re.match(r"^[A-Z0-9]+(?![a-z])|^[A-Z]?[a-z0-9]+|^.", topic)
    return m.group(0) if m else topic


def bare(parent):
    """CMS.CRAB or .../view/CMS/CRAB -> CRAB (same web assumed)."""
    return re.split(r"[./]", parent)[-1] if parent else ""


def select(src, inc, exc, con, min_hits, follow_parents):
    names = sorted(f[:-4] for f in os.listdir(src) if f.endswith(".txt") and not f.startswith("."))
    names = [n for n in names if not SKIP.search(n + ".txt")]
    reason, hits, parent = {}, {}, {}
    for n in names:
        if any(r.search(n) for r in exc):
            reason[n] = "exclude"
            continue
        try:
            with open(os.path.join(src, n + ".txt"), "rb") as fh:
                raw = fh.read().decode("utf-8", "replace")
        except OSError as err:
            reason[n] = "unreadable"
            print("unreadable: %s (%s)" % (n, err), file=sys.stderr)
            continue
        m = PARENT_RE.search(raw)
        parent[n] = bare(m.group(1)) if m else ""
        if any(r.search(n) for r in inc):
            reason[n] = "name"
        elif is_physics(n):
            reason[n] = "physics"
        else:
            hits[n] = sum(len(r.findall(META_RE.sub(" ", raw))) for r in con)
            if hits[n] >= min_hits:
                reason[n] = "content"
    if follow_parents:
        seeds = {n for n, r in reason.items() if r in ("name", "content")}
        memo = {}

        def reaches(n, seen):
            if n in seeds:
                return True
            if n in memo:
                return memo[n]
            p = parent.get(n, "")
            ok = bool(p) and p not in seen and reason.get(p) not in ("exclude", "physics") and p in parent and reaches(p, seen | {n})
            memo[n] = ok
            return ok

        for n in names:
            if n not in reason and reaches(n, frozenset()):
                reason[n] = "parent"
    return names, reason, hits, parent


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--src", required=True, help="<Web>/topics directory of the full snapshot")
    ap.add_argument("--out", required=True, help="curated directory for THIS web, e.g. deployments/archi-crab/data/twiki/CMS")
    ap.add_argument("--include", action="append", default=[], help="extra name regex, repeatable (adds to the defaults)")
    ap.add_argument("--exclude", action="append", default=[], help="extra name regex, repeatable (adds to the defaults)")
    ap.add_argument("--content", action="append", default=[], help="extra body regex, repeatable (adds to the defaults)")
    ap.add_argument("--no-defaults", action="store_true", help="use ONLY the --include/--exclude/--content given")
    ap.add_argument("--min-hits", type=int, default=3, help="content matches needed to keep a page (default 3)")
    ap.add_argument("--no-parents", action="store_true", help="do not keep children of kept pages")
    ap.add_argument("--report", help="CSV: topic,reason,content_hits,parent,family")
    ap.add_argument("--dry-run", action="store_true", help="select and report; write nothing")
    ap.add_argument("--force", action="store_true", help="allow pruning an --out this tool did not create")
    a = ap.parse_args()
    src, out = os.path.abspath(a.src), os.path.abspath(a.out)
    if out == src or out.startswith(src + os.sep):
        sys.exit("--out must not be (inside) --src")

    names, reason, hits, parent = select(
        src,
        [re.compile(p) for p in ([] if a.no_defaults else INCLUDE) + a.include],
        [re.compile(p) for p in ([] if a.no_defaults else EXCLUDE) + a.exclude],
        [re.compile(p) for p in ([] if a.no_defaults else CONTENT) + a.content],
        a.min_hits,
        not a.no_parents,
    )
    kept = [n for n in names if reason.get(n) in KEPT]
    print("topics: %d  kept: %d  %s" % (len(names), len(kept), dict(Counter(reason.get(n, "unmatched") for n in names))))
    for label, sel in (("kept", kept), ("unmatched", [n for n in names if n not in reason])):
        fam = Counter(family(n) for n in sel)
        print("%s by name family: %s" % (label, ", ".join("%s=%d" % kv for kv in fam.most_common(30))))
    near = sorted(((h, n) for n, h in hits.items() if n not in reason and h > 0), reverse=True)[:30]
    print("near misses (content hits < %d): %s" % (a.min_hits, ", ".join("%s(%d)" % (n, h) for h, n in near)))

    if a.report:
        with open(a.report, "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["topic", "reason", "content_hits", "parent", "family"])
            for n in names:
                w.writerow([n, reason.get(n, "unmatched"), hits.get(n, ""), parent.get(n, ""), family(n)])
        print("report: %s" % a.report)
    if a.dry_run:
        return 0

    existing = [f for f in os.listdir(out) if f.endswith(".txt")] if os.path.isdir(out) else []
    if existing and not os.path.exists(os.path.join(out, MARKER)) and not a.force:
        sys.exit("%s holds %d .txt files and no %s marker: not created by this tool; refusing to prune (use --force)" % (out, len(existing), MARKER))
    os.makedirs(out, exist_ok=True)
    keep = {n + ".txt" for n in kept}
    removed = [f for f in existing if f not in keep]
    for f in removed:
        os.remove(os.path.join(out, f))
    for n in kept:
        shutil.copyfile(os.path.join(src, n + ".txt"), os.path.join(out, n + ".txt"))
    with open(os.path.join(out, MARKER), "w") as fh:
        fh.write("source=%s\ntopics=%d\n" % (src, len(kept)))
    print("wrote %d topics to %s (%d removed since last run)" % (len(kept), out, len(removed)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
