#!/usr/bin/env python3
"""contract-check.py — does this deployment still fit the engine it is pinned to?

Run INSIDE the runtime image (it imports the connectors and calls the okg CLI):

    docker run --rm --network none \
      -v "$PWD/deployments:/w/deployments:ro" -v "$PWD/scripts:/w/scripts:ro" -v "$OUT:/out" \
      --entrypoint python "$IMG" /w/scripts/contract-check.py \
      --deployment /w/deployments/archi-crab --markdown /out/contract.md --fixes /out/fixes.json

Exit 1 when an ERROR is found, 0 otherwise. Five checks, each about one thing WE
wrote against something UPSTREAM owns:

  1. sources   every registry `module`/`class` imports, is the class okg can run
               (an adapter, not a bare reader), and accepts exactly the `params` given
  2. bundle    where our registry and the cern-team bundle name a different class for
               the same module; which bundle connectors we do not use yet
  3. cli       every okg command and flag our workflows, chart and smoke test call
  4. vendor    every path VENDOR.yaml copies from the image still exists
  5. policy    okg's own audit of deployment.yaml's Nomos posture and of every source's
               policy: the audit each readiness probe runs, here in one second instead
               of as a worker that never becomes Ready

Applying the mechanical fixes (on the host):

    python3 scripts/contract-check.py --apply-fixes fixes.json --deployment deployments/archi-crab

With sources/kinds.yaml present the registry is generated, so a rename goes into the
kind and the registry is re-rendered (scripts/sources.py: needs PyYAML on the host).
Without it, the old in-place registry edit (standard library only).

Standard library + PyYAML (present in the image).
"""
from __future__ import annotations

import argparse
import importlib
import inspect
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Every okg command + flag this repo calls. Keep in step with:
#   .github/workflows/e2e.yaml, ci.yaml · helm/okg/templates/runtime-statefulset.yaml · scripts/smoke.sh
CLI_CONTRACT: list[tuple[str, list[str]]] = [
    ("migrate", ["--deployment", "--apply"]),
    ("catalog ownership claim", ["--deployment"]),
    ("catalog load", ["--deployment", "--apply"]),
    ("deployment lint", ["--json"]),
    ("ingest", ["--deployment", "--progress", "--inline"]),
    ("provision", ["--deployment", "--publish-once", "--source-workers", "--include", "--json"]),
    ("runtime bootstrap", ["--deployment", "--json"]),
    ("runtime worker", ["--deployment"]),
    ("deployment ready", ["--json"]),   # --profile: gone since okg 3d6cb3e8 (chart: okg.readinessProfile "")
    ("status", ["--deployment", "--json"]),
    ("search", ["--deployment", "--query"]),
    ("mcp-serve", ["--deployment", "--transport", "--host", "--port", "--allowed-host", "--auth-token-env"]),
]

ERROR, WARN, INFO, OK = "ERROR", "WARN", "INFO", "ok"


class Report:
    def __init__(self) -> None:
        self.rows: dict[str, list[tuple[str, str, str]]] = {}
        self.fixes: list[dict[str, str]] = []

    def add(self, section: str, level: str, subject: str, message: str) -> None:
        self.rows.setdefault(section, []).append((level, subject, message))

    def count(self, level: str) -> int:
        return sum(1 for rows in self.rows.values() for lv, _, _ in rows if lv == level)

    def markdown(self, header: str) -> str:
        out = [f"### Contract report: {self.count(ERROR)} error(s), {self.count(WARN)} warning(s)", "", header, ""]
        for section, rows in self.rows.items():
            bad = [r for r in rows if r[0] in (ERROR, WARN)]
            good = len([r for r in rows if r[0] == OK])
            out.append(f"**{section}**: {good} ok" + (f", {len(bad)} to look at" if bad else ""))
            out.append("")
            shown = bad + [r for r in rows if r[0] == INFO]
            if shown:
                out += ["| | what | detail |", "|---|---|---|"]
                out += [f"| {lv} | `{subj}` | {msg} |" for lv, subj, msg in shown]
                out.append("")
        if self.fixes:
            out.append(f"**Mechanical fixes available: {len(self.fixes)}** (applied by the engine workflow as its own commit)")
            out += [f"- `{f['source']}`: `class: {f['old']}` → `class: {f['new']}`" for f in self.fixes]
            out.append("")
        return "\n".join(out)


def _load_yaml(path: Path):
    import yaml  # PyYAML: in the image via archi's dependencies

    return yaml.safe_load(path.read_text())


def _sources(registry) -> dict:
    sources = registry.get("sources") if isinstance(registry, dict) else None
    return sources if isinstance(sources, dict) else {}


def _adapter_for_reader(module, reader_cls):
    """The adapter class in `module` that wraps `reader_cls`, if there is one."""
    for name, obj in vars(module).items():
        if inspect.isclass(obj) and obj.__dict__.get("reader_class") is reader_cls:
            return name
    return None


def check_sources(report: Report, registry: dict) -> None:
    section = "1. sources (registry vs connector code)"
    # Since archi moved onto okg's connector SDK, okg can only run an archi reader through
    # its adapter. Older archi has no adapters at all: there a bare reader IS what runs.
    try:
        from okg.deployment import ConnectorAdapter
        importlib.import_module("archi.sources._sdk_adapter")
        adapters_required = True
    except Exception:
        ConnectorAdapter, adapters_required = None, False
    for name, entry in _sources(registry).items():
        if not isinstance(entry, dict) or not isinstance(entry.get("module"), str) or not isinstance(entry.get("class"), str):
            report.add(section, ERROR, str(name), "entry needs a `module` and a `class` (both strings)")
            continue
        mod_name, cls_name = entry["module"], entry["class"]
        params = entry.get("params") or {}
        if not isinstance(params, dict):
            report.add(section, ERROR, name, "`params` must be a mapping")
            continue
        try:
            module = importlib.import_module(mod_name)
        except Exception as exc:
            report.add(section, ERROR, name, f"cannot import module `{mod_name}`: {type(exc).__name__}: {exc}")
            continue
        cls = getattr(module, cls_name, None)
        if cls is None:
            near = sorted(n for n, o in vars(module).items() if inspect.isclass(o) and o.__module__ == mod_name and not n.startswith("_"))
            report.add(section, ERROR, name, f"`{mod_name}` has no class `{cls_name}`. It defines: {', '.join(near) or 'nothing public'}")
            continue
        problems = []
        if adapters_required and mod_name.startswith("archi.") and not issubclass(cls, ConnectorAdapter):
            adapter = _adapter_for_reader(module, cls)
            if adapter:
                problems.append(f"`{cls_name}` is a bare reader; this engine runs the adapter `{adapter}`")
                report.fixes.append({"source": name, "old": cls_name, "new": adapter})
            else:
                problems.append(f"`{cls_name}` is a bare reader and `{mod_name}` defines no adapter for it; okg cannot run it")
        try:
            inspect.signature(cls).bind(**params)
        except TypeError as exc:
            accepted = ", ".join(p for p in inspect.signature(cls).parameters if p != "self")
            problems.append(f"params do not fit `{cls_name}`: {exc}. It accepts: {accepted}")
        if problems:
            report.add(section, ERROR, name, "; ".join(problems))
        else:
            report.add(section, OK, name, f"{mod_name}.{cls_name}")


def _stem(class_name: str) -> str:
    """CMSSWReleaseSource and CMSSWReleaseAdapter are the same connector."""
    return str(class_name).removesuffix("Adapter").removesuffix("Source")


def check_bundle(report: Report, registry: dict, bundle: Path) -> None:
    section = "2. bundle (cern-team source-defaults vs our registry)"
    defaults = bundle / "source-defaults"
    if not defaults.is_dir():
        report.add(section, WARN, str(defaults), "bundle directory not found in this image")
        return
    ours = {n: (e.get("module"), e.get("class")) for n, e in _sources(registry).items() if isinstance(e, dict)}
    seen: set[tuple[str, str]] = set()
    for path in sorted(defaults.iterdir()):
        if not re.search(r"\.ya?ml(\.example)?$", path.name):
            continue
        try:
            doc = _load_yaml(path) or {}
        except Exception as exc:
            report.add(section, WARN, path.name, f"unreadable: {exc}")
            continue
        if not isinstance(doc, dict):
            report.add(section, WARN, path.name, "not a mapping of source entries; skipped")
            continue
        for bname, entry in doc.items():
            if not isinstance(entry, dict) or "module" not in entry:
                continue
            module, cls = entry.get("module"), entry.get("class")
            same = [n for n, mc in ours.items() if mc == (module, cls)]
            renamed = [n for n, (m, c) in ours.items() if m == module and c != cls and _stem(c) == _stem(cls)]
            if same:
                report.add(section, OK, same[0], f"same class as bundle `{path.name}`")
            elif renamed:
                if (renamed[0], cls) not in seen:
                    report.add(section, WARN, renamed[0], f"bundle `{path.name}` names `{cls}`, our registry names `{ours[renamed[0]][1]}`")
                seen.add((renamed[0], cls))
            else:
                report.add(section, INFO, bname, f"available, not used: `{module}.{cls}` ({path.name})")


def check_cli(report: Report) -> None:
    section = "3. okg CLI (commands and flags this repo calls)"
    for command, flags in CLI_CONTRACT:
        try:
            proc = subprocess.run(["okg", *command.split(), "--help"], capture_output=True, text=True, timeout=120)
        except Exception as exc:
            report.add(section, ERROR, f"okg {command}", f"could not run: {exc}")
            continue
        text = proc.stdout + proc.stderr
        if proc.returncode != 0:
            last = (text.strip().splitlines() or ["no output"])[-1]
            report.add(section, ERROR, f"okg {command}", f"command is gone or renamed: {last}")
            continue
        missing = [f for f in flags if not re.search(rf"(?<![\w-]){re.escape(f)}(?![\w-])", text)]
        if missing:
            report.add(section, ERROR, f"okg {command}", f"flag(s) no longer accepted: {', '.join(missing)}")
        else:
            report.add(section, OK, f"okg {command}", "")


def check_vendor(report: Report, deployment: Path) -> None:
    section = "4. vendored files (VENDOR.yaml sources in the image)"
    manifest = deployment / "VENDOR.yaml"
    if not manifest.is_file():
        return
    for entry in (_load_yaml(manifest) or {}).get("entries") or []:
        src = Path(entry["src"])
        present = src.is_dir() if entry.get("type") == "dir" else src.is_file()
        if present:
            report.add(section, OK, entry["dest"], str(src))
        else:
            report.add(section, ERROR, entry["dest"], f"`{src}` is not in this image: upstream moved or removed it")


def check_policy(report: Report, deployment: Path, registry: dict) -> None:
    section = "5. access policy (the Nomos audit that readiness runs)"
    manifest = _load_yaml(deployment / "deployment.yaml") or {}
    if not isinstance(manifest, dict) or not isinstance(manifest.get("nomos"), dict):
        report.add(section, OK, "nomos", "no nomos block in deployment.yaml: okg skips the audit")
        return
    try:  # okg internals, not its public SDK: when they move, say so instead of crashing
        from okg.substrate.nomos.deployment_audit import audit_deployment_policy

        audit = audit_deployment_policy(manifest, source_registry=registry, deployment=str(manifest.get("name") or ""))
    except Exception as exc:
        report.add(section, WARN, "nomos", f"could not run okg's audit in this engine ({type(exc).__name__}: {exc}); readiness is the only check")
        return
    for finding in audit.get("findings") or []:
        hint = ""
        if finding.get("code") == "nomos.audit.source_policy_missing":
            cls = (finding.get("details") or {}).get("source_class") or "<source_class>"
            hint = f". Declare `nomos.source_policy_defaults.by_source_class.{cls}` in deployment.yaml, or `source_policy` on the source"
        level = ERROR if finding.get("severity") == "error" else WARN
        report.add(section, level, str(finding.get("path") or "nomos"), f"{finding.get('message')}{hint}")
    for warning in audit.get("warnings") or []:
        report.add(section, WARN, str(warning.get("path") or "nomos"), str(warning.get("message")))
    posture = audit.get("deployment_posture") or {}
    try:  # a governed class is accepted by readiness only with runtime enforcement on
        from okg.substrate.nomos.doctor import GOVERNED_DEPLOYMENT_CLASSES
        from okg.substrate.nomos.runtime_enforcement import manifest_nomos_enforcement_mode

        mode = manifest_nomos_enforcement_mode(manifest)
        if posture.get("deployment_class") in GOVERNED_DEPLOYMENT_CLASSES and mode != "enforce":
            report.add(
                section, ERROR, "nomos.deployment_posture.deployment_class",
                f"`{posture.get('deployment_class')}` is a governed class and runtime enforcement is `{mode}`: "
                "readiness will block on `nomos.source_lineage` until Nomos enforcement is rolled out",
            )
    except Exception as exc:
        report.add(section, WARN, "nomos.runtime_enforcement", f"could not check the governed-class rule ({type(exc).__name__})")
    if audit.get("ok"):
        report.add(section, OK, "nomos.deployment_posture", f"class `{posture.get('deployment_class')}`, {audit.get('source_policy_count')} source policies")


def apply_fixes(fixes_path: Path, deployment: Path) -> int:
    """Rewrite `class:` lines in source_registry.yaml. Text edit on purpose: comments stay.

    When the registry is GENERATED (sources/kinds.yaml exists, docs/SOURCES.md), the
    class lives in the kind template: rename it there and re-render, through
    scripts/sources.py rename-class. Editing the generated file alone would make
    sources-lint fail (registry != render) and be undone by the next render."""
    fixes = json.loads(fixes_path.read_text())
    repo = deployment.resolve().parent.parent
    if (repo / "sources" / "kinds.yaml").is_file():
        ident = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
        done: set[tuple[str, str]] = set()
        for fix in fixes if isinstance(fixes, list) else []:
            if not (isinstance(fix, dict) and all(isinstance(fix.get(k), str) for k in ("old", "new"))
                    and ident.fullmatch(fix["old"]) and ident.fullmatch(fix["new"])):
                print(f"refused a malformed fix: {str(fix)[:120]!r}", file=sys.stderr)
                continue
            if (fix["old"], fix["new"]) in done:
                continue
            done.add((fix["old"], fix["new"]))
            proc = subprocess.run([sys.executable, str(repo / "scripts" / "sources.py"), "--repo", str(repo),
                                   "rename-class", fix["old"], fix["new"]])
            if proc.returncode:
                # skip it, as the in-place path does: the engine PR must still open, and its
                # contract report (and sources-lint) say what is left to do
                print(f"skip {fix['old']} -> {fix['new']}: rename-class failed (exit {proc.returncode})", file=sys.stderr)
        return 0
    registry = deployment / "source_registry.yaml"
    lines = registry.read_text().splitlines(keepends=True)
    applied = 0
    # The fixes file was written by code running inside the image: upstream's code. It may
    # rename a class to another Python identifier, and nothing else.
    ident = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
    for fix in fixes if isinstance(fixes, list) else []:
        if not (isinstance(fix, dict) and all(isinstance(fix.get(k), str) for k in ("source", "old", "new"))
                and ident.fullmatch(fix["old"]) and ident.fullmatch(fix["new"]) and re.fullmatch(r"[\w.-]+", fix["source"])):
            print(f"refused a malformed fix: {str(fix)[:120]!r}", file=sys.stderr)
            continue
        # the source's own block: from "  <name>:" to the next key at the same indent
        start = next((i for i, l in enumerate(lines) if re.match(rf"^(\s+){re.escape(fix['source'])}:\s*(#.*)?$", l)), None)
        if start is None:
            print(f"skip {fix['source']}: block not found", file=sys.stderr)
            continue
        indent = len(lines[start]) - len(lines[start].lstrip())
        end = next((i for i in range(start + 1, len(lines)) if lines[i].strip() and not lines[i].lstrip().startswith("#") and len(lines[i]) - len(lines[i].lstrip()) <= indent), len(lines))
        pattern = re.compile(rf"^(\s+class:\s+){re.escape(fix['old'])}(\s*(#.*)?)$")
        hits = [i for i in range(start, end) if pattern.match(lines[i].rstrip("\n"))]
        if len(hits) != 1:
            print(f"skip {fix['source']}: expected one `class: {fix['old']}` line, found {len(hits)}", file=sys.stderr)
            continue
        i = hits[0]
        newline = "\n" if lines[i].endswith("\n") else ""
        found = pattern.match(lines[i].rstrip("\n"))
        lines[i] = found.group(1) + fix["new"] + found.group(2) + newline
        applied += 1
        print(f"fixed {fix['source']}: class {fix['old']} -> {fix['new']}")
    if applied:
        registry.write_text("".join(lines))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--deployment", required=True, type=Path, help="path to deployments/<name>")
    ap.add_argument("--bundle", type=Path, default=Path(os.environ.get("OKG_PROFILES_DIR", "/opt/archi/bundles")) / "cern-team")
    ap.add_argument("--markdown", type=Path, help="write the report here (default: stdout)")
    ap.add_argument("--fixes", type=Path, help="write mechanical fixes (JSON) here")
    ap.add_argument("--apply-fixes", type=Path, metavar="FIXES_JSON", help="apply a fixes file to the registry and exit")
    args = ap.parse_args()

    if args.apply_fixes:
        return apply_fixes(args.apply_fixes, args.deployment)

    registry = _load_yaml(args.deployment / "source_registry.yaml") or {}
    report = Report()
    check_sources(report, registry)
    check_bundle(report, registry, args.bundle)
    check_cli(report)
    check_vendor(report, args.deployment)
    check_policy(report, args.deployment, registry)

    header = (
        f"Engine in this image: okg `{os.environ.get('OKG_CODE_REVISION', 'unknown')[:12]}`, "
        f"archi `{os.environ.get('ARCHI_CODE_REVISION', 'unknown')[:12]}`."
    )
    text = report.markdown(header)
    if args.markdown:
        args.markdown.write_text(text + "\n")
    else:
        print(text)
    if args.fixes:
        args.fixes.write_text(json.dumps(report.fixes, indent=2) + "\n")
    print(f"contract-check: {report.count(ERROR)} error(s), {report.count(WARN)} warning(s)", file=sys.stderr)
    return 1 if report.count(ERROR) else 0


if __name__ == "__main__":
    sys.exit(main())
