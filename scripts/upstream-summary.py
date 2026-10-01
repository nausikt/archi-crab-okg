#!/usr/bin/env python3
"""upstream-summary.py — the body of the engine pull request.

Answers, for a reviewer who has five minutes: what moved upstream, which of it touches
something THIS repo uses, and what has to be checked before approving.

    scripts/upstream-summary.py \
      --okg-git DIR   --okg-from SHA   --okg-to SHA \
      --archi-git DIR --archi-from SHA --archi-to SHA \
      [--contract contract.md] [--deployment deployments/archi-crab] > body.md

DIR is a clone that contains both commits (a blobless clone is enough:
`git clone --filter=blob:none --no-checkout`). Omit --okg-git to skip the okg section.

Upstream commit subjects are UNTRUSTED TEXT. Every one is printed inside a code span,
so it cannot mention a user, link an issue of this repository, or inject markdown.
Standard library only.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

MAX_BODY = 60000  # GitHub refuses a pull-request body above 65536 characters

# okg paths this repo depends on, and why a change there matters to us.
OKG_WATCH = [
    ("Dockerfile", "runtime image build (our image is built on top of it)"),
    (".dockerignore", "what the runtime image leaves out"),
    ("ops/kubernetes/okg", "Helm chart: `helm/okg` here is a copy with our deltas, port changes by hand"),
    ("src/okg/substrate/library/templates/codebase-index", "code-graph template: `extractors.yaml` and one bridge are copied from it (VENDOR.yaml)"),
    ("src/okg/deployment", "connector SDK that archi's adapters are built on"),
    ("src/okg/substrate/ingest/adapter_factory.py", "how a registry entry is turned into a running source"),
    ("src/okg/substrate/db/migrations", "database migrations: they run against the staging database at rollout"),
]
ARCHI_WATCH = [
    ("python/archi/sources", "connectors"),
    ("python/archi/auth", "cookie and cache helpers the connectors use"),
    ("bundles/cern-team/source-defaults", "registry templates: copy new entries from here"),
    ("bundles/cern-team/schemas", "schema slices and bridges (we own copies in `schemas/`)"),
    ("bundles/cern-team", "bundle defaults (modules, invariants, deployment defaults)"),
    ("skills", "playbooks (we own copies in `skills/`)"),
]


def git(repo: str, *args: str, check: bool = True) -> str:
    proc = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {proc.stderr.strip()}")
    return proc.stdout


def code(text: str, limit: int = 140) -> str:
    """Untrusted text as an inert code span."""
    text = re.sub(r"\s+", " ", text).replace("`", "'").replace("|", "/").strip()
    if len(text) > limit:
        text = text[: limit - 1] + "…"
    return f"`{text}`" if text else ""


def has_commit(repo: str, sha: str) -> bool:
    return subprocess.run(["git", "-C", repo, "cat-file", "-e", f"{sha}^{{commit}}"], capture_output=True).returncode == 0


def commit_date(repo: str, sha: str) -> str:
    return git(repo, "log", "-1", "--format=%cs", sha).strip()


def count(repo: str, rng: str, *paths: str, first_parent: bool = False) -> int:
    args = ["rev-list", "--count"] + (["--first-parent"] if first_parent else []) + [rng]
    if paths:
        args += ["--", *paths]
    return int(git(repo, *args).strip() or 0)


def landed(repo: str, rng: str, *paths: str, limit: int = 30, url: str = "") -> tuple[list[str], int]:
    """What landed on the followed branch, newest first: one line per merge or direct commit."""
    args = ["log", "--first-parent", "--format=%h%x1f%s%x1f%b%x1e", rng]
    if paths:
        args += ["--", *paths]
    rows = []
    for record in git(repo, *args).split("\x1e"):
        if not record.strip():
            continue
        short, subject, body = (record.strip("\n").split("\x1f") + ["", ""])[:3]
        merge = re.match(r"Merge pull request #(\d+) from \S+", subject)
        if merge:
            title = next((line for line in body.splitlines() if line.strip()), subject)
            number = merge.group(1)
            ref = f"[PR {number}]({url.rstrip('/')}/pull/{number})" if url else f"PR {number}"
            rows.append(f"- {ref} {code(title)} ({short})")
        else:
            rows.append(f"- {code(subject)} ({short})")
    return rows[:limit], len(rows)


def changed_files(repo: str, a: str, b: str, *paths: str) -> list[tuple[str, str]]:
    out = git(repo, "diff", "--name-status", "--no-renames", a, b, "--", *paths)
    return [tuple(line.split("\t", 1)) for line in out.splitlines() if "\t" in line]  # type: ignore[misc]


def range_header(repo: str, name: str, track: str, a: str, b: str) -> tuple[str, str | None]:
    """One table row, and the usable range (None when there is nothing to list)."""
    if a == b:
        return f"| {name} (`{track}`) | `{a[:9]}` | unchanged | 0 | 0 |", None
    if not has_commit(repo, a) or not has_commit(repo, b):
        return f"| {name} (`{track}`) | `{a[:9]}` | `{b[:9]}` | ? | ? |", None
    rng = f"{a}..{b}"
    row = (
        f"| {name} (`{track}`) | `{a[:9]}` ({commit_date(repo, a)}) | `{b[:9]}` ({commit_date(repo, b)}) "
        f"| {count(repo, rng)} | {count(repo, rng, first_parent=True)} |"
    )
    return row, rng


def watch_table(repo: str, a: str, b: str, rng: str, watch: list[tuple[str, str]]) -> list[str]:
    lines = ["| path | commits | files changed | why it matters here |", "|---|---|---|---|"]
    quiet = []
    for path, why in watch:
        files = changed_files(repo, a, b, path)
        if not files:
            quiet.append(f"`{path}`")
            continue
        lines.append(f"| `{path}` | {count(repo, rng, path)} | {len(files)} | {why} |")
    if len(lines) == 2:
        return ["Nothing this repo depends on changed."]
    if quiet:
        lines += ["", "Unchanged: " + ", ".join(quiet) + "."]
    return lines


def fenced_diff(repo: str, a: str, b: str, path: str, limit: int = 120) -> list[str]:
    diff = git(repo, "diff", "--no-color", a, b, "--", path, check=False).replace("```", "'''").splitlines()
    if not diff:
        return []
    more = [f"… {len(diff) - limit} more lines: git diff {a[:9]} {b[:9]} -- {path}"] if len(diff) > limit else []
    return ["```diff", *diff[:limit], *more, "```"]


def registry_modules(deployment: Path) -> list[str]:
    text = (deployment / "source_registry.yaml").read_text()
    return sorted(set(re.findall(r"^\s+module:\s+(archi\.[\w.]+)\s*(?:#.*)?$", text, re.M)))


def show(repo: str, sha: str, path: str) -> str | None:
    """File content at a commit, following one level of symlink (the bundle links its skills)."""
    tree = git(repo, "ls-tree", sha, "--", path, check=False).split()
    if len(tree) < 3:
        return None
    text = git(repo, "show", f"{sha}:{path}", check=False)
    if tree[0] == "120000":
        parts: list[str] = []
        for part in (Path(path).parent / text.strip()).parts:
            if part == "..":
                parts.pop() if parts else None
            elif part != ".":
                parts.append(part)
        return show(repo, sha, "/".join(parts))
    return text


def owned_copies(repo: str, sha: str, deployment: Path) -> list[str]:
    """Files we own that started as copies of the bundle's: which now differ from upstream."""
    differ, same = [], 0
    for sub in ("schemas", "schemas/bridges", "skills"):
        local_dir = deployment / sub
        if not local_dir.is_dir():
            continue
        for local in sorted(p for p in local_dir.iterdir() if p.is_file() and p.suffix in (".yaml", ".md")):
            upstream = show(repo, sha, f"bundles/cern-team/{sub}/{local.name}")
            if upstream is None:
                continue  # ours only (for example the vendored okg bridge)
            if upstream == local.read_text():
                same += 1
            else:
                differ.append(f"`{sub}/{local.name}`")
    if not differ:
        return [f"All {same} owned copies of bundle schemas and skills equal the bundle at the new commit."]
    return [
        f"{len(differ)} owned file(s) differ from the bundle at the new commit ({same} are equal). "
        "They are ours on purpose; adopt upstream changes when `catalog load` accepts them:",
        ", ".join(differ),
    ]


def okg_tested_by_archi(repo: str, sha: str) -> str | None:
    ci = git(repo, "show", f"{sha}:.github/workflows/ci.yml", check=False)
    found = re.search(r"mitdbg/okg(?:\.git)?@([0-9a-f]{40})", ci)
    return found.group(1) if found else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--okg-git"), ap.add_argument("--okg-from"), ap.add_argument("--okg-to")
    ap.add_argument("--okg-track", default="dev"), ap.add_argument("--okg-url", default="")
    ap.add_argument("--archi-url", default="")
    ap.add_argument("--archi-git", required=True), ap.add_argument("--archi-from", required=True)
    ap.add_argument("--archi-to", required=True), ap.add_argument("--archi-track", default="main")
    ap.add_argument("--contract", type=Path)
    ap.add_argument("--deployment", type=Path, default=Path("deployments/archi-crab"))
    args = ap.parse_args()

    out: list[str] = []
    table = ["| upstream | from | to | commits | landed on the branch |", "|---|---|---|---|---|"]
    okg_rng = None
    if args.okg_git:
        row, okg_rng = range_header(args.okg_git, "okg", args.okg_track, args.okg_from, args.okg_to)
        table.append(row)
    else:
        table.append(f"| okg (`{args.okg_track}`) | `{(args.okg_from or '?')[:9]}` | `{(args.okg_to or '?')[:9]}` | not read | not read |")
    row, archi_rng = range_header(args.archi_git, "archi-okg", args.archi_track, args.archi_from, args.archi_to)
    table.append(row)

    out += ["## Engine bump", "", *table, ""]
    out += [
        "### Before you approve",
        "",
        "- [ ] Every check on this pull request is green. `e2e` ran a full ingest and the smoke test on the image pinned here.",
        "- [ ] The contract report below has no ERROR left.",
        "- [ ] If the chart section lists changes, decide whether `helm/okg` needs them.",
        "- [ ] If migrations are listed, staging's database is migrated by the rollout; prod only on Promote.",
        "",
        "Merging pins nothing by itself: after `main`'s e2e is green the bot writes the image and the "
        "knowledge revision into `envs/staging` in one commit, and Argo CD rolls staging.",
        "Label this pull request `hold` to stop the daily run from moving it.",
        "",
    ]
    if args.contract and args.contract.is_file():
        out += [args.contract.read_text().strip(), ""]

    # ---- archi-okg --------------------------------------------------------------------------
    out += ["### archi-okg: what changed in what we use", ""]
    if archi_rng is None:
        out += ["No change, or the two commits are not both in the clone.", ""]
    else:
        a, b, repo = args.archi_from, args.archi_to, args.archi_git
        if subprocess.run(["git", "-C", repo, "merge-base", "--is-ancestor", a, b]).returncode != 0:
            out += ["**The old pin is not an ancestor of the new one** (upstream rewrote history or the branch changed).", ""]
        modules = registry_modules(args.deployment)
        if modules:
            out += ["Connectors our registry names:", ""]
            for module in modules:
                path = "python/" + module.replace(".", "/") + ".py"
                rows, total = landed(repo, archi_rng, path, limit=6, url=args.archi_url)
                out.append(f"- `{module}`: " + (f"{count(repo, archi_rng, path)} commit(s)" if total else "unchanged"))
                out += ["  " + r for r in rows]
            out.append("")
        out += watch_table(repo, a, b, archi_rng, ARCHI_WATCH) + [""]
        new_defaults = [p for status, p in changed_files(repo, a, b, "bundles/cern-team/source-defaults") if status == "A"]
        if new_defaults:
            out += ["New registry templates (connectors you could add): " + ", ".join(f"`{Path(p).name}`" for p in new_defaults), ""]
        out += owned_copies(repo, b, args.deployment) + [""]
        rows, total = landed(repo, archi_rng, limit=25, url=args.archi_url)
        out += [f"<details><summary>Landed on {args.archi_track}: {total}" + (f" (newest {len(rows)} shown)" if total > len(rows) else "") + "</summary>", "", *rows, "", "</details>", ""]

    # ---- okg --------------------------------------------------------------------------------
    out += ["### okg: what changed in what we use", ""]
    if not args.okg_git:
        out += ["Not read: no okg clone was available to this run (OKG_PAT missing or without access).", ""]
    elif okg_rng is None:
        out += ["No change, or the two commits are not both in the clone.", ""]
    else:
        a, b, repo = args.okg_from, args.okg_to, args.okg_git
        if subprocess.run(["git", "-C", repo, "merge-base", "--is-ancestor", a, b]).returncode != 0:
            out += ["**The old pin is not an ancestor of the new one.**", ""]
        out += watch_table(repo, a, b, okg_rng, OKG_WATCH) + [""]
        chart = fenced_diff(repo, a, b, "ops/kubernetes/okg")
        if chart:
            out += ["<details><summary>Upstream chart diff (port by hand into <code>helm/okg</code>)</summary>", "", *chart, "", "</details>", ""]
        migrations = [p for status, p in changed_files(repo, a, b, "src/okg/substrate/db/migrations") if status == "A"]
        if migrations:
            out += [f"New migrations ({len(migrations)}): " + ", ".join(f"`{Path(p).name}`" for p in migrations[:20]) + (" …" if len(migrations) > 20 else ""), ""]
        rows, total = landed(repo, okg_rng, *[p for p, _ in OKG_WATCH], limit=25, url=args.okg_url)
        if total:
            out += [f"<details><summary>Landed on {args.okg_track} and touching the paths above: {total}" + (f" (newest {len(rows)} shown)" if total > len(rows) else "") + "</summary>", "", *rows, "", "</details>", ""]

    # ---- pairing ----------------------------------------------------------------------------
    tested = okg_tested_by_archi(args.archi_git, args.archi_to)
    out += ["### Pairing", ""]
    if not tested:
        out += ["archi-okg's CI no longer names the okg commit it tests against (`.github/workflows/ci.yml`).", ""]
    elif args.okg_to and tested == args.okg_to:
        out += [f"archi-okg's own CI tests against exactly this okg commit (`{tested[:9]}`).", ""]
    else:
        ahead = ""
        if args.okg_git and args.okg_to and has_commit(args.okg_git, tested) and has_commit(args.okg_git, args.okg_to):
            ahead = f", {count(args.okg_git, f'{tested}..{args.okg_to}')} commits behind the okg pinned here"
        out += [
            f"archi-okg's own CI tests against okg `{tested[:9]}`{ahead}. "
            "This pairing is therefore proven only by the checks on this pull request.",
            "",
        ]

    body = "\n".join(out)
    if len(body) > MAX_BODY:
        body = body[:MAX_BODY] + "\n\n… truncated: the full report is in the workflow run's summary.\n"
    sys.stdout.write(body + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
