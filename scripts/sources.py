#!/usr/bin/env python3
"""sources — the archi-crab source list: render it, lint it, probe it, check it
against the pinned engine, and verify what an ingest actually produced.

  sources/archi-crab.yaml   WHAT we ingest (version-agnostic; edit this)
  sources/kinds.yaml        HOW each kind becomes okg registry YAML (engine-specific data)
  deployments/archi-crab/source_registry.yaml   GENERATED from the two

Commands (python3 >= 3.9 and PyYAML; nothing else):

  render [--write]        print (or write) the registry rendered from the list
  lint [--base REF|published ...] [--allow-identity-change]
                          offline gates: list shape, credentials wired, data
                          present and sane, registry == render, invariants and
                          search profile covered, and (with --base) nothing
                          published has vanished or been renamed. `published`
                          means the revisions staging and prod ingest from
                          (repositorySync.revision in envs/*/values.yaml).
  status                  what is rendered, what is pending, and why
  probe [--tier N|--id X|--all] [--cache DIR [--refresh]] [--json F] [--strict]
                          network: can the repo be reached with THIS
                          environment's git credentials, is the branch right,
                          how many files after scope, data checks. In the
                          worker pod it tests the pod's own credentials:
                            kubectl exec -i <pod> -c worker -- python - probe \\
                              --manifest-b64 "$(base64 -w0 sources/archi-crab.yaml)" \\
                              < scripts/sources.py
                          (from stdin the repo root is $OKG_REPO_ROOT, which the
                          chart sets to the synced checkout)
  contract                INSIDE the pinned image: every kind's class imports, is
                          an adapter and binds its params; the data kinds run
                          on a one-page fixture and emit only what their
                          output_signature declares; the code_repos keys we
                          write appear in okg's code_repos handling
  inventory               INSIDE the pinned image, read-only: which ontology
                          modules the engine ships (and their subtypes), the
                          codebase-index template, archi's connector templates
                          and the Nomos vocabulary -- what you may write
  rename-class OLD NEW    a class moved upstream: change it in sources/kinds.yaml
                          and re-render (what an engine PR's mechanical fix
                          must do once the registry is generated)
  verify [--probe F]      AFTER an ingest (needs OKG_DSN): every rendered git
                          source produced source_file nodes, and no more than
                          its budget (or its probed in-scope count) -- the
                          proof that a scope was honoured

Exit status: 0 clean, 1 findings, 2 usage/input error. docs/SOURCES.md is the
walkthrough.
"""
from __future__ import annotations

import argparse
import ast
import base64
import collections
import copy
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

import yaml

_HERE = Path(__file__) if not __file__.startswith("<") else None
REPO = _HERE.resolve().parent.parent if _HERE else Path(os.environ.get("OKG_REPO_ROOT") or os.getcwd())
ID_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
PLACEHOLDER_RE = re.compile(r"FILL-ME|REPLACE_ME|TODO|<[^>]*>")
SOURCE_KEYS = {"tier", "group", "kind", "git", "branch", "dir", "about", "enabled", "scope", "data", "max_files",
               "sensitivity", "auth", "params"}
# The kind NAMES are the contract between the list and kinds.yaml; what each kind
# renders to lives in kinds.yaml. A new kind = a new name here + its template there.
KIND_REQUIRED = {"git": ("git",), "docs-files": ("data",), "twiki-raw": ("data",), "cmssw-releases": ()}


def kind_names(ctx):
    """Kinds are whatever sources/kinds.yaml defines (a new connector = a new kind
    there, no code change); the built-in four when kinds.yaml is not at hand."""
    return list(((ctx.kinds or {}).get("kinds") or {}) or KIND_REQUIRED)


def kind_requires(ctx, name):
    k = ((ctx.kinds or {}).get("kinds") or {}).get(name) or {}
    return tuple(k.get("requires") or KIND_REQUIRED.get(name, ()))
NODES_PER_FILE = 40  # staging: crabserver 414 files -> 15,572 code-structure nodes
LOGIN_RE = re.compile(r"auth\.cern\.ch/auth/realms|Sign in with your CERN|CERN Single Sign-On|login\.cern\.ch", re.I)
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
USERINFO_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*://[^/]*@")


class InputError(Exception):
    """A file this tool needs is missing or malformed (exit 2)."""


# ---------------------------------------------------------------- loading ----

class _UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate keys. Plain YAML keeps the LAST one
    silently, so a pasted `enabled: false` twice, or a source id repeated,
    would change what is ingested without a word."""


def _mapping(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise yaml.constructor.ConstructorError(
                None, None, "duplicate key %r" % (key,), key_node.start_mark)
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep)


_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def load_yaml(path, text=None):
    try:
        if text is None:
            text = Path(path).read_text(encoding="utf-8")
        return yaml.load(text, Loader=_UniqueKeyLoader)
    except FileNotFoundError:
        raise InputError("%s: not found" % path)
    except yaml.YAMLError as exc:
        raise InputError("%s: %s" % (path, exc))


class Ctx:
    """Paths and parsed inputs for one deployment."""

    def __init__(self, args):
        self.deployment = args.deployment
        self.repo = Path(args.repo).resolve()
        self.manifest_path = self.repo / "sources" / ("%s.yaml" % self.deployment)
        self.kinds_path = self.repo / "sources" / "kinds.yaml"
        self.dep_dir = self.repo / "deployments" / self.deployment
        self.registry_path = self.dep_dir / "source_registry.yaml"
        b64 = getattr(args, "manifest_b64", None)
        text = base64.b64decode(b64).decode("utf-8") if b64 else None
        self.manifest = load_yaml(self.manifest_path, text)
        self.kinds = load_yaml(self.kinds_path) if (self.kinds_path.exists() or not b64) else None
        if not isinstance(self.manifest, dict) or not isinstance(self.manifest.get("sources"), dict):
            raise InputError("%s: expected a mapping with `sources:`" % self.manifest_path)
        bad = [k for k in self.manifest["sources"] if not isinstance(k, str)]
        if bad:
            raise InputError("source ids must be strings; YAML read %s (quote them)" % bad)

    @property
    def sources(self):
        return self.manifest["sources"]

    def tiers(self):
        return list((self.manifest.get("rollout") or {}).get("enabled_tiers") or [])

    def selected(self, sid):
        s = self.sources[sid]
        return isinstance(s, dict) and s.get("tier") in self.tiers() and s.get("enabled", True) is not False

    def why_not(self, sid):
        s = self.sources[sid]
        if s.get("tier") not in self.tiers():
            return "tier %s not enabled" % s.get("tier")
        if s.get("enabled", True) is False:
            return "enabled: false"
        return ""

    def kind(self, sid):
        if self.kinds is None:
            raise InputError("sources/kinds.yaml is needed for this command")
        name = self.sources[sid].get("kind")
        kinds = self.kinds.get("kinds") or {}
        if name not in kinds:
            raise InputError("%s: unknown kind %r (known: %s)" % (sid, name, ", ".join(sorted(kinds))))
        return kinds[name]

    def max_files(self, sid):
        v = self.sources[sid].get("max_files") or (self.manifest.get("defaults") or {}).get("max_files") or 1500
        return v if isinstance(v, int) and v > 0 else 1500


def git_host(url):
    m = re.match(r"^https://([^/@:]+)(?::\d+)?/", url or "")
    return m.group(1).lower() if m else ""


def has_userinfo(url):
    """A credential in a clone URL would be rendered into a committed file."""
    return bool(USERINFO_RE.match(url or ""))


_MASK_RE = re.compile(r"([A-Za-z][A-Za-z0-9+.-]*://)[^/@\s]*@")


def mask_url(text):
    """Mask credentials in every URL inside `text` (a URL or a whole message)."""
    return _MASK_RE.sub(r"\1***@", text or "")


def norm_url(url):
    return re.sub(r"(\.git)?/*$", "", (url or "").strip().lower())


def default_dir(url):
    return re.sub(r"\.git$", "", (url or "").rstrip("/").rsplit("/", 1)[-1])


# --------------------------------------------------------------- rendering ---

def _subst(obj, env):
    if isinstance(obj, str):
        return re.sub(r"\{\{(\w+)\}\}", lambda m: str(env[m.group(1)]), obj)
    if isinstance(obj, list):
        return [_subst(x, env) for x in obj]
    if isinstance(obj, dict):
        return {_subst(k, env): _subst(v, env) for k, v in obj.items()}
    return obj


def _env(ctx, sid, s=None):
    s = s if s is not None else ctx.sources[sid]
    return {"id": sid, "name": sid.replace("-", "_"), "deployment": ctx.deployment,
            "data": str(s.get("data") or "").strip("/"), "git": s.get("git") or "",
            "dir": s.get("dir") or default_dir(s.get("git"))}


class RenderError(Exception):
    pass


def render(ctx):
    """(registry dict, per-source metadata for comments)."""
    repos, sources, meta = [], {}, []
    git_kind = None
    for sid in ctx.sources:
        if not ctx.selected(sid):
            continue
        s, k = ctx.sources[sid], ctx.kind(sid)
        env = _env(ctx, sid)
        if has_userinfo(env["git"]) or "@" in env["git"].split("://", 1)[-1].split("/", 1)[0]:
            raise RenderError("%s: credentials in the git URL; tokens go through gitCredentials, never the URL" % sid)
        if k.get("render") == "code_repos":
            git_kind = k
            entry = _subst(k["repo_entry"], env)
            scope = s.get("scope") or {}
            if scope:
                fields = k.get("scope_fields")
                if not fields:
                    raise RenderError(
                        "%s: has `scope`, but sources/kinds.yaml git.scope_fields is null: scoping is not "
                        "verified for the pinned okg, and an ignored key would ingest the WHOLE repo. "
                        "Keep it disabled, or verify (docs/SOURCES.md §5) and fill scope_fields." % sid)
                for part in ("include", "exclude"):
                    if scope.get(part):
                        if not fields.get(part):
                            raise RenderError("%s: scope.%s given but kinds git.scope_fields has no %r key" % (sid, part, part))
                        entry[fields[part]] = list(scope[part])
            repos.append(entry)
            meta.append(("repo", sid))
        elif k.get("render") == "source":
            name = env["name"]
            if name in sources:
                raise RenderError("%s: registry key %r collides with another source" % (sid, name))
            entry = _subst(copy.deepcopy(k["entry"]), env)
            if s.get("params"):
                # per-source parameters the kind leaves open (e.g. which OAI sets, which
                # categories); `contract` binds them to the connector's signature
                entry["params"] = dict(entry.get("params") or {}, **s["params"])
            sources[name] = entry
            meta.append(("source", sid))
        else:
            raise RenderError("%s: kind %r has unknown render %r" % (sid, s.get("kind"), k.get("render")))
    reg = {}
    if repos:
        reg["code_repos"] = dict(_subst(git_kind["code_repos"], {}), repos=repos)
    if sources:
        reg["sources"] = sources
    return reg, meta


class _Dumper(yaml.SafeDumper):
    """Block style, indented sequences (yamllint's default), and short all-scalar
    mappings/lists on one line -- the way the hand-written registry looked."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def _short(items):
    return all(not isinstance(x, (dict, list)) for x in items) and len(str(items)) < 72


_Dumper.add_representer(dict, lambda d, data: d.represent_mapping(
    "tag:yaml.org,2002:map", data.items(), flow_style=_short(list(data.values()))))
_Dumper.add_representer(list, lambda d, data: d.represent_sequence(
    "tag:yaml.org,2002:seq", data, flow_style=_short(data)))


def _block(obj, indent):
    text = yaml.dump(obj, Dumper=_Dumper, sort_keys=False, width=4096, allow_unicode=True)
    return "\n".join((" " * indent + line) if line else line for line in text.rstrip("\n").split("\n"))


def _comment(text, indent):
    pad = " " * indent
    return "\n".join((pad + "# " + line).rstrip() for line in str(text).rstrip("\n").split("\n"))


def render_text(ctx):
    reg, meta = render(ctx)
    rel = lambda p: p.relative_to(ctx.repo).as_posix()  # noqa: E731
    ra = (ctx.kinds or {}).get("reviewed_against") or {}
    pending = ["%s (%s)" % (sid, ctx.why_not(sid)) for sid in ctx.sources if not ctx.selected(sid)]
    out = [
        "# GENERATED by scripts/sources.py render -- do not edit.",
        "# Inputs: %s (what) + %s (how)." % (rel(ctx.manifest_path), rel(ctx.kinds_path)),
        "# Change a source there, then: python3 scripts/sources.py render --write",
        "# CI (workflow `sources`) fails when this file differs from the render.",
        "#",
        "# Enabled tiers: %s. Kinds reviewed against archi %s, okg %s." % (
            ctx.tiers(), ra.get("archi", "?"), ra.get("okg", "?")),
    ]
    if pending:
        out.append("# Not rendered (`python3 scripts/sources.py status` says why):")
        line = "#  "
        for item in pending:
            if len(line) + len(item) > 100:
                out.append(line.rstrip(","))
                line = "#  "
            line += " " + item + ","
        out.append(line.rstrip(",") + ".")
    out.append("")
    if "code_repos" in reg:
        gk = ctx.kinds["kinds"]["git"]
        out.append(_comment("kind git: %s.\nProven: %s." % (gk.get("about", ""), gk.get("proven", "")), 0))
        cr = reg["code_repos"]
        out.append(_block({"code_repos": {k: v for k, v in cr.items() if k != "repos"}}, 0))
        out.append("  repos:")
        repo_ids = [sid for what, sid in meta if what == "repo"]
        for sid, entry in zip(repo_ids, cr["repos"]):
            s = ctx.sources[sid]
            out.append(_comment("%s -- tier %s -- %s" % (sid, s.get("tier"), s.get("about", "")), 4))
            out.append("    - " + yaml.safe_dump(entry, default_flow_style=True, width=4096, sort_keys=False).strip())
        out.append("")
    if "sources" in reg:
        out.append("sources:")
        for what, sid in meta:
            if what != "source":
                continue
            s, k = ctx.sources[sid], ctx.kind(sid)
            name = sid.replace("-", "_")
            out.append(_comment("---- %s -- tier %s -- kind %s -- %s" % (sid, s.get("tier"), s.get("kind"), s.get("about", "")), 2))
            if k.get("comment"):
                out.append(_comment(k["comment"], 2))
            out.append(_block({name: reg["sources"][name]}, 2))
            out.append("")
    return "\n".join(out).rstrip("\n") + "\n", reg


# ------------------------------------------------------------------- lint ----

class Findings:
    def __init__(self):
        self.errors, self.warnings, self.notes = [], [], []

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def note(self, msg):
        self.notes.append(msg)

    def report(self, ok_msg):
        gh = bool(os.environ.get("GITHUB_ACTIONS"))
        for n in self.notes:
            print("  note: " + n)
        for w in self.warnings:
            print(("::warning::" if gh else "WARNING: ") + w)
        for e in self.errors:
            print(("::error::" if gh else "ERROR: ") + e)
        if not self.errors:
            print(ok_msg + (" (%d warning(s))" % len(self.warnings) if self.warnings else ""))
        return 1 if self.errors else 0


def read_records(path):
    """records.json -> list, or raise ValueError with the reason."""
    items = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(items, list):
        raise ValueError("not a JSON list")
    return items


def _command_lookalike(m):
    """git@github.com:org/repo, user@host:path, user@lxplus.cern.ch -- commands in a
    page, not contact addresses (docs-build.py keeps them for the same reason)."""
    local, dom = m.group(0).split("@", 1)
    return (m.string[m.end():m.end() + 1] == ":" or local == "git"
            or bool(re.match(r"(lxplus|lxtunnel|aiadm|cmslpc|lxbatch|lxslc)[\w-]*\.", dom, re.I)))


def check_records_json(path, f, label):
    """Data gate for a docs-files source. Returns the URLs (for cross-source checks)."""
    if not path.is_file():
        f.error("%s: %s missing -- build it with scripts/docs-build.py (docs/SOURCES.md §3)" % (label, path))
        return set()
    try:
        items = read_records(path)
    except (ValueError, UnicodeDecodeError) as exc:
        f.error("%s: %s is not a valid records file: %s" % (label, path, exc))
        return set()
    if not items:
        f.error("%s: %s is empty (archi reports cache_missing and the publish is blocked)" % (label, path))
        return set()
    urls, nourl, empty, dup, short, emails, login = set(), 0, 0, 0, 0, 0, []
    for it in items:
        if not isinstance(it, dict) or not re.match(r"^https?://", str(it.get("url") or "")):
            nourl += 1
            continue
        u, body = it["url"], str(it.get("body") or "")
        if u in urls:
            dup += 1
        urls.add(u)
        if not body.strip():
            empty += 1
            continue
        short += len(body) < 200
        emails += sum(1 for m in EMAIL_RE.finditer(body) if not _command_lookalike(m))
        if len(body) < 3000 and LOGIN_RE.search(body):
            login.append(u)
    if nourl:
        f.error("%s: %d record(s) without an http(s) url -- archi skips them and then never claims a complete scope" % (label, nourl))
    if empty:
        f.error("%s: %d record(s) with an empty body -- a page with nothing to search" % (label, empty))
    if dup:
        f.error("%s: %d duplicate url(s) -- one page per url" % (label, dup))
    if login:
        f.error("%s: %d record(s) look like a CERN login page, e.g. %s" % (label, len(login), login[0]))
    if emails:
        f.warn("%s: %d e-mail address(es) in page bodies (docs-build.py redacts them by default)" % (label, emails))
    if short:
        f.note("%s: %d page(s) under 200 characters" % (label, short))
    f.note("%s: %d pages" % (label, len(urls)))
    return urls


def check_twiki_tree(path, f, label):
    if not path.is_dir():
        f.error("%s: %s missing -- scripts/twiki-curate.py (docs/ONBOARDING.md §3)" % (label, path))
        return
    top = sorted(p.name for p in path.glob("*.txt"))
    webs = {d.name: len(list(d.glob("*.txt"))) for d in path.iterdir() if d.is_dir() and not d.name.startswith(".")}
    if top:
        f.error("%s: topic files at the top of %s (web unknown): %s" % (label, path, top[:5]))
    if not any(webs.values()):
        f.error("%s: no topics under %s/<Web>/" % (label, path))
    f.note("%s: webs %s" % (label, webs))


def invariant_subtypes(dep_dir):
    """{invariant name: [subtypes it requires]} for the floor pattern we use."""
    inv = load_yaml(dep_dir / "invariants.yaml") if (dep_dir / "invariants.yaml").exists() else {}
    out = {}
    for item in (inv or {}).get("invariants") or []:
        m = re.search(r"required\s*\(\s*subtype\s*\)\s+AS\s+\(\s*VALUES\s+((?:\(\s*'[^']+'\s*\)\s*,?\s*)+)\)",
                      item.get("sql") or "", re.I)
        if m:
            out[item.get("name")] = re.findall(r"'([^']+)'", m.group(1))
    return out


def _git_show(ctx, ref, rel):
    try:
        return subprocess.run(["git", "-C", str(ctx.repo), "show", "%s:%s" % (ref, rel)],
                              check=True, capture_output=True, text=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def resolve_bases(ctx, bases):
    """--base values -> [(label, git ref)]. `published` = what staging and prod
    ingest from (repositorySync.revision); an unset revision is skipped."""
    out = []
    for b in bases or []:
        if b != "published":
            if b and not re.fullmatch(r"0+", b):
                out.append((b, b, False))
            continue
        for env in ("staging", "prod"):
            p = ctx.repo / "envs" / env / "values.yaml"
            rev = str((((load_yaml(p) if p.exists() else {}) or {}).get("repositorySync") or {}).get("revision") or "")
            if rev:
                out.append(("%s (%s)" % (env, rev[:10]), rev, True))
    return out


def _has_value(obj, want):
    if isinstance(obj, dict):
        return any(_has_value(v, want) for v in obj.values())
    if isinstance(obj, list):
        return any(_has_value(v, want) for v in obj)
    return obj == want


_INGEST_RE = re.compile(r"(?:\bokg|\$\{?OKG\}?)[\"']?\s+(?:ingest|provision)\b")


def _job_runs(job):
    return "\n".join(str(st.get("run") or "") for st in (job.get("steps") or []) if isinstance(st, dict))


def check_ci_credentials(ctx, hosts_needed, f):
    """Every CI job that ingests must carry the same git credential helper the
    chart renders (docs/ONBOARDING.md §4 B5): job/workflow env with the helper,
    its value, the count and a token from a secret, and every `docker run` of
    the okg image in that job must pass them into the container."""
    wf_dir = ctx.repo / ".github" / "workflows"
    docs = {}
    for p in sorted(wf_dir.glob("*.y*ml")) if wf_dir.is_dir() else []:
        try:
            docs[p.name] = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            f.error(".github/workflows/%s does not parse: %s" % (p.name, exc))
    ingesting = []
    for name, doc in docs.items():
        for jname, job in (doc.get("jobs") or {}).items():
            if isinstance(job, dict) and _INGEST_RE.search(_job_runs(job)):
                ingesting.append((name, jname, doc, job))
    actions_dir = ctx.repo / ".github" / "actions"
    for p in sorted(actions_dir.rglob("action.y*ml")) if actions_dir.is_dir() else []:
        if _INGEST_RE.search(p.read_text(encoding="utf-8")):
            f.warn("%s runs an ingest inside a composite action: check its git credentials by hand"
                   % p.relative_to(ctx.repo))
    if not ingesting:
        f.error("sources on %s need a git credential in CI, but no workflow job runs `okg ingest`/`okg provision`; "
                "the credential gate cannot tell where the e2e clones -- teach check_ci_credentials the new shape"
                % ", ".join(hosts_needed))
        return
    # A reusable e2e (workflow_call) only sees the secrets its callers hand it: the
    # token's secret must be declared by the callee and passed by every caller.
    needed = {}  # callee file -> secret names its ingesting jobs read for git tokens
    for name, jname, doc, job in ingesting:
        env = dict(doc.get("env") or {})
        env.update(job.get("env") or {})
        for k, v in env.items():
            if str(k).startswith("GIT_CRED_TOKEN_"):
                needed.setdefault(name, set()).update(re.findall(r"secrets\.([A-Za-z0-9_]+)", str(v)))
    for callee, names in needed.items():
        trig = docs[callee].get("on", docs[callee].get(True)) or {}
        call = trig.get("workflow_call") if isinstance(trig, dict) else None
        if call is None:
            continue
        declared = set(((call or {}).get("secrets") or {}).keys())
        for n in sorted(names - declared):
            f.error(".github/workflows/%s reads secrets.%s but does not declare it under on.workflow_call.secrets -- "
                    "callers cannot pass it, the token is empty" % (callee, n))
        for name, doc in docs.items():
            for jname, job in (doc.get("jobs") or {}).items():
                uses = str((job or {}).get("uses") or "") if isinstance(job, dict) else ""
                if not (uses.startswith("./.github/workflows/") and uses.rsplit("/", 1)[-1] == callee):
                    continue
                passed = job.get("secrets")
                if passed == "inherit":
                    continue
                for n in sorted(names - set((passed or {}).keys())):
                    f.error(".github/workflows/%s job %s calls %s without passing secrets.%s -- the e2e clone gets no "
                            "token" % (name, jname, callee, n))
    for name, jname, doc, job in ingesting:
        env = dict(doc.get("env") or {})
        env.update(job.get("env") or {})
        where = ".github/workflows/%s job %s" % (name, jname)
        for host in hosts_needed:
            keys = [k for k, v in env.items() if str(k).startswith("GIT_CONFIG_KEY_") and v == "credential.https://%s.helper" % host]
            if not keys:
                f.error("%s ingests but its env sets no GIT_CONFIG_KEY_i = credential.https://%s.helper -- the e2e would "
                        "fail to clone and staging would never get the pin (docs/ONBOARDING.md §4 B5)" % (where, host))
                continue
            i = keys[0].rsplit("_", 1)[-1]
            missing = [k for k in ("GIT_CONFIG_COUNT", "GIT_CONFIG_VALUE_%s" % i) if k not in env]
            if not any(str(k).startswith("GIT_CRED_TOKEN_") and "secrets." in str(v) for k, v in env.items()):
                missing.append("GIT_CRED_TOKEN_i from a secret")
            if missing:
                f.error("%s: credential helper for %s is incomplete, missing %s" % (where, host, ", ".join(missing)))
        runs = _job_runs(job).replace("\\\n", " ")
        for line in runs.split("\n"):
            if "docker run" in line and "OKG_IMG" in line:
                lacking = [flag for flag in ("-e GIT_CONFIG_COUNT", "-e GIT_CRED_TOKEN_") if flag not in line]
                if lacking:
                    f.error("%s: a `docker run` of the okg image does not pass %s into the container: %s"
                            % (where, " / ".join(lacking), line.strip()[:120]))


def source_auth(ctx, sid):
    """none|token: the source's own `auth:` (a public project on a token host), else its host's."""
    s = ctx.sources[sid]
    return s.get("auth") or ((ctx.manifest.get("hosts") or {}).get(git_host(s.get("git"))) or {}).get("auth")


def sensitivity(ctx, sid):
    """What a source's content is, in the posture's vocabulary. Explicit wins;
    a git repo defaults by its host (public without a token, internal with
    one); the release catalog is public; documents must say."""
    s = ctx.sources[sid]
    if s.get("sensitivity"):
        return str(s["sensitivity"])
    if s.get("kind") == "git":
        return "public" if source_auth(ctx, sid) == "none" else "internal"
    if s.get("kind") == "cmssw-releases":
        return "public"
    return ""


def check_nomos(ctx, reg, token_hosts, f):
    """The access-policy gate okg runs on every readiness probe (and that
    scripts/contract-check.py runs in the image), checked offline -- plus the
    part okg cannot see: repositories under code_repos are not audited, so a
    private repo would make a public posture silently untrue."""
    dep = load_yaml(ctx.dep_dir / "deployment.yaml") if (ctx.dep_dir / "deployment.yaml").exists() else {}
    nomos = (dep or {}).get("nomos")
    if not isinstance(nomos, dict):
        return
    posture = nomos.get("deployment_posture") or {}
    klass = posture.get("deployment_class") or "?"
    by_class = ((nomos.get("source_policy_defaults") or {}).get("by_source_class") or {})
    allowed = posture.get("allowed_source_sensitivities")
    for name, entry in ((reg or {}).get("sources") or {}).items():
        sc = (entry or {}).get("source_class")
        if sc and sc not in by_class and not (entry or {}).get("source_policy"):
            f.error("source %s has source_class %s, and deployment.yaml has no nomos.source_policy_defaults."
                    "by_source_class.%s: okg's audit fails and the worker never becomes Ready "
                    "(docs/ADDING-SOURCES.md, example 3)" % (name, sc, sc))
        elif sc in by_class:
            sid = name.replace("_", "-")
            pol = by_class[sc] or {}
            if sid in ctx.sources and pol.get("sensitivity") and sensitivity(ctx, sid) and pol["sensitivity"] != sensitivity(ctx, sid):
                f.warn("source %s is %s, but the %s policy it falls under says %s" % (sid, sensitivity(ctx, sid), sc, pol["sensitivity"]))
    for sid in ctx.sources:
        if not ctx.selected(sid):
            continue
        sens = sensitivity(ctx, sid)
        if not sens:
            f.error("%s: say what its content is -- `sensitivity: public` (every page is world-readable) or "
                    "`internal` -- it decides which posture may hold it" % sid)
        elif isinstance(allowed, list) and sens not in allowed:
            f.error("%s is %s, but the posture (%s) allows only %s sources. This is the data-governance gate, on purpose: "
                    "the class must become org_operational_private with Nomos runtime enforcement first. Do not "
                    "widen the public lists (docs/UPSTREAM-SYNC.md 'The posture is a gate')" % (sid, sens, klass, allowed))
    if token_hosts and posture.get("secret_handling") == "no_secrets":
        f.error("sources read %s with a token, but the posture says secret_handling: no_secrets -- untrue the moment "
                "the first private repository is enabled (same gate as above)" % ", ".join(sorted(token_hosts)))


def cmd_lint(ctx, args):
    f = Findings()
    m = ctx.manifest
    stray = set(m) - {"version", "rollout", "hosts", "defaults", "sources", "retired"}
    if stray:
        f.error("sources/%s.yaml: unknown top-level key(s) %s" % (ctx.deployment, sorted(stray)))
    if m.get("version") != 1:
        f.error("sources/%s.yaml: version must be 1" % ctx.deployment)
    tiers = ctx.tiers()
    if not tiers or not all(isinstance(t, int) for t in tiers):
        f.error("rollout.enabled_tiers must be a non-empty list of integers")
    hosts = m.get("hosts") or {}
    for h, spec in hosts.items():
        if (spec or {}).get("auth") not in ("none", "token"):
            f.error("hosts.%s.auth must be none or token" % h)
        if (spec or {}).get("auth") == "token" and not ((spec or {}).get("username") and (spec or {}).get("secret_key")):
            f.error("hosts.%s: a token host needs username and secret_key" % h)
    retired = m.get("retired") or {}
    if not isinstance(retired, dict) or not all(isinstance(k, str) and isinstance(v, str) and v.strip() for k, v in retired.items()):
        f.error("retired: must map a source id to the reason and date it was removed (a rebuild is planned)")
        retired = {}
    for rid in retired:
        if rid in ctx.sources:
            f.error("%s is both a source and retired" % rid)
    dmf = (m.get("defaults") or {}).get("max_files")
    if dmf is not None and not (isinstance(dmf, int) and dmf > 0):
        f.error("defaults.max_files must be a positive integer")

    dirs, urls_seen, token_hosts, produced, doc_urls = {}, {}, set(), set(), {}
    for sid, s in ctx.sources.items():
        if not ID_RE.match(sid):
            f.error("%s: id must be lowercase letters, digits and dashes (it keys every node)" % sid)
        if not isinstance(s, dict):
            f.error("%s: must be a mapping" % sid)
            continue
        unknown = set(s) - SOURCE_KEYS
        if unknown:
            f.error("%s: unknown key(s) %s (allowed: %s)" % (sid, sorted(unknown), ", ".join(sorted(SOURCE_KEYS))))
        if not isinstance(s.get("tier"), int):
            f.error("%s: tier must be an integer" % sid)
        if s.get("enabled", True) not in (True, False):
            f.error("%s: enabled must be true or false" % sid)
        if s.get("auth") is not None and s["auth"] not in ("none", "token"):
            f.error("%s: auth must be none or token (overrides its host's)" % sid)
        if s.get("sensitivity") is not None and not (isinstance(s["sensitivity"], str) and re.fullmatch(r"[a-z_]+", s["sensitivity"])):
            f.error("%s: sensitivity must be a word such as public or internal" % sid)
        if s.get("max_files") is not None and not (isinstance(s["max_files"], int) and s["max_files"] > 0):
            f.error("%s: max_files must be a positive integer" % sid)
        kind = s.get("kind")
        if kind not in kind_names(ctx):
            f.error("%s: kind must be one of %s (sources/kinds.yaml)" % (sid, ", ".join(kind_names(ctx))))
            continue
        if s.get("params") is not None and (not isinstance(s["params"], dict) or kind == "git"):
            f.error("%s: params must be a mapping, on a kind rendered as a source (not git)" % sid)
        for req in kind_requires(ctx, kind):
            if not s.get(req):
                f.error("%s: kind %s needs `%s`" % (sid, kind, req))
        if "scope" in s:
            sc = s["scope"]
            ok = (kind == "git" and isinstance(sc, dict) and sc and not (set(sc) - {"include", "exclude"})
                  and all(isinstance(v, list) and v and all(isinstance(g, str) and g for g in v) for v in sc.values()))
            if not ok:
                f.error("%s: scope must be {include: [globs], exclude: [globs]} with at least one glob, on a git "
                        "source (an empty scope would silently mean the whole repo)" % sid)
        if s.get("data") and (Path(str(s["data"])).is_absolute() or ".." in Path(str(s["data"])).parts):
            f.error("%s: data must be a path inside deployments/%s/ (the pod only has that)" % (sid, ctx.deployment))
        url = str(s.get("git") or "")
        if url and not PLACEHOLDER_RE.search(url):
            key = norm_url(url)
            if key in urls_seen:
                f.error("%s: same repository as %s (%s) -- two slugs, every file twice" % (sid, urls_seen[key], mask_url(url)))
            urls_seen[key] = sid
        if url and (has_userinfo(url) or "?" in url or "@" in url.split("://", 1)[-1].split("/", 1)[0]):
            f.error("%s: no credentials or query in the git URL -- tokens go through gitCredentials" % sid)
            continue
        if not ctx.selected(sid):
            if kind == "git" and PLACEHOLDER_RE.search(url):
                f.note("%s: pending -- fill the repository path, then `probe --id %s`" % (sid, sid))
            continue

        # ---- selected sources only below ----
        if ctx.kinds:
            produced.update(ctx.kind(sid).get("produces") or [])
        if kind == "git":
            if PLACEHOLDER_RE.search(url):
                f.error("%s: git URL still has a placeholder: %s" % (sid, url))
            host = git_host(url)
            if not host or not url.endswith(".git"):
                f.error("%s: git must be https://<host>/<path>.git (got %s)" % (sid, url))
            elif host not in hosts:
                f.error("%s: host %s is not declared under hosts:" % (sid, host))
            elif source_auth(ctx, sid) == "token":
                token_hosts.add(host)
            d = s.get("dir") or default_dir(url)
            if d in dirs:
                f.error("%s: clone dir %r already used by %s" % (sid, d, dirs[d]))
            dirs[d] = sid
            if s.get("scope") and ctx.kinds and not (ctx.kinds["kinds"]["git"].get("scope_fields")):
                f.error("%s: has `scope` but scoping is not verified for the pinned okg "
                        "(sources/kinds.yaml git.scope_fields is null) -- keep it disabled (docs/SOURCES.md §5)" % sid)
        elif (ctx.kinds and (ctx.kind(sid).get("data_check") == "records-json")) or kind == "docs-files":
            urls = check_records_json(ctx.dep_dir / s["data"] / "records.json", f, sid)
            for other, ou in doc_urls.items():
                both = urls & ou
                if both:
                    f.error("%s and %s share %d url(s), e.g. %s: same node id, two owners" % (sid, other, len(both), sorted(both)[0]))
            doc_urls[sid] = urls
        elif (ctx.kinds and (ctx.kind(sid).get("data_check") == "twiki-tree")) or kind == "twiki-raw":
            check_twiki_tree(ctx.dep_dir / s["data"], f, sid)

    # ---- credentials wired where the clones happen ----
    if token_hosts:
        check_ci_credentials(ctx, sorted(token_hosts), f)
    for host in sorted(token_hosts):
        spec = hosts[host]
        want = {"host": host, "username": spec["username"], "secretKey": spec["secret_key"]}
        for env in ("staging", "prod"):
            p = ctx.repo / "envs" / env / "values.yaml"
            vals = load_yaml(p) if p.exists() else {}
            got = ((vals or {}).get("gitCredentials") or {}).get("hosts") or []
            if not any(all(h.get(k) == v for k, v in want.items()) for h in got if isinstance(h, dict)):
                f.error("%s needs gitCredentials.hosts entry %s in envs/%s/values.yaml, or the pod cannot clone "
                        "(docs/ONBOARDING.md §4 B3)" % (host, want, env))

    # ---- the render, and the file okg actually reads ----
    reg = None
    if ctx.kinds:
        try:
            text, reg = render_text(ctx)
        except (RenderError, KeyError) as exc:
            f.error("render: %s" % exc)
        if reg is not None:
            owners = collections.Counter(e.get("ownership_id") for e in (reg.get("sources") or {}).values())
            for o, n in owners.items():
                if n > 1:
                    f.error("ownership_id %s used by %d sources" % (o, n))
            current = load_yaml(ctx.registry_path) if ctx.registry_path.exists() else None
            if current != reg:
                f.error("%s differs from the render -- run: python3 scripts/sources.py render --write. If a tool "
                        "edited the registry (e.g. a mechanical class rename on the engine PR), make the same edit in "
                        "sources/kinds.yaml instead, then render" % ctx.registry_path.relative_to(ctx.repo))

    # ---- access policy (Nomos): the readiness gate, offline ----
    check_nomos(ctx, reg, token_hosts, f)

    # ---- kinds: `produces` (which the floor check trusts) covers each signature ----
    for kname, kind in ((ctx.kinds or {}).get("kinds") or {}).items():
        sig = ((kind.get("entry") or {}).get("admission_policy") or {}).get("output_signature") or {}
        nodes = {n.get("subtype") for n in sig.get("nodes") or []}
        if nodes - set(kind.get("produces") or []):
            f.error("sources/kinds.yaml %s: output_signature nodes %s missing from `produces`"
                    % (kname, sorted(nodes - set(kind.get("produces") or []))))

    # ---- invariants and search: nothing may name a subtype nobody produces ----
    floors = invariant_subtypes(ctx.dep_dir)
    for name, subtypes in floors.items():
        missing = [st for st in subtypes if st not in produced]
        if missing:
            f.error("invariant %s requires %s, which no rendered source produces -- a permanent error-severity "
                    "failure after every publish; enable a source that does, or drop the floor" % (name, missing))
    if "documentation_page" in produced and not any("documentation_page" in v for v in floors.values()):
        f.warn("a rendered source produces documentation_page but no invariant floors it -- paste archi_crab_docs_floor "
               "back into invariants.yaml (a silent zero would go unnoticed)")
    dep = load_yaml(ctx.dep_dir / "deployment.yaml") if (ctx.dep_dir / "deployment.yaml").exists() else {}
    for pname, prof in (((dep or {}).get("search") or {}).get("profiles") or {}).items():
        idle = [st for st in (prof or {}).get("subtypes") or [] if st not in produced]
        if idle:
            f.warn("search profile %s names %s, which no rendered source produces (empty until one does)" % (pname, idle))
    searched = {st for prof in (((dep or {}).get("search") or {}).get("profiles") or {}).values() for st in (prof or {}).get("subtypes") or []}
    if "documentation_page" in produced and searched and "documentation_page" not in searched:
        f.warn("a rendered source produces documentation_page but no search profile names it -- add it to "
               "deployment.yaml search.profiles.content.subtypes so whole pages can be answers, not only their chunks")

    # ---- identity: nothing published may vanish or be renamed ----
    if reg is not None:
        rel_reg = ctx.registry_path.relative_to(ctx.repo).as_posix()
        retired_names = set(retired) | {r.replace("-", "_") for r in retired}
        for label, ref, published in resolve_bases(ctx, args.base):
            text = _git_show(ctx, ref, rel_reg)
            if text is None:
                (f.error if published else f.note)(
                    "base %s: its registry cannot be read (revision not in this clone's history?) -- identity not "
                    "checked%s" % (label, "; fetch full history (fetch-depth: 0)" if published else ""))
                continue
            base = yaml.safe_load(text) or {}
            hard = f.warn if args.allow_identity_change else f.error
            now_slugs = {r.get("slug"): r for r in ((reg.get("code_repos") or {}).get("repos") or [])}
            for r in (base.get("code_repos") or {}).get("repos") or []:
                slug = r.get("slug")
                if slug not in now_slugs:
                    if slug in retired_names:
                        f.note("repo %s is retired (%s) and still live in %s until the rebuild" % (slug, retired.get(slug, ""), label))
                    else:
                        hard("repo slug %r is in %s and gone from the render: okg does not retract a vanished source's "
                             "facts, so its nodes stay live and stale -- a REBUILD. If that is the plan, list it under "
                             "`retired:` with the reason (docs/SOURCES.md §7)" % (slug, label))
                    continue
                if norm_url(r.get("url")) != norm_url(now_slugs[slug].get("url")):
                    hard("repo %s now points at %s, but %s ingested %s under the same slug: the old repo's files stay "
                         "live next to the new one's -- a REBUILD, or give the new repo a new id"
                         % (slug, mask_url(now_slugs[slug].get("url")), label, mask_url(r.get("url"))))
                if r.get("dir") != now_slugs[slug].get("dir"):
                    f.warn("repo %s: clone dir %r -> %r (a fresh clone; identity unchanged)"
                           % (slug, r.get("dir"), now_slugs[slug].get("dir")))
            for name, entry in (base.get("sources") or {}).items():
                if name not in (reg.get("sources") or {}):
                    if name in retired_names:
                        f.note("source %s is retired and still live in %s until the rebuild" % (name, label))
                    else:
                        hard("source %r is in %s and gone from the render: same as above, a REBUILD (or `retired:`)" % (name, label))
                    continue
                root = ((entry or {}).get("params") or {}).get("eos_root") or ""
                if "/%s/" % ctx.deployment in root:
                    rel_dir = "deployments/%s/%s" % (ctx.deployment, root.split("/%s/" % ctx.deployment, 1)[1].strip("/"))
                    r_ls = subprocess.run(["git", "-C", str(ctx.repo), "ls-tree", "-r", "--name-only", ref, "--", rel_dir],
                                          capture_output=True, text=True)
                    old_topics = {x for x in r_ls.stdout.split("\n") if x.endswith(".txt")}
                    now_topics = {p.relative_to(ctx.repo).as_posix() for p in (ctx.repo / rel_dir).glob("*/*.txt")}
                    gone = old_topics - now_topics
                    if gone:
                        f.warn("%s: %d topic(s) in %s are gone from %s (e.g. %s) -- okg keeps their old facts live; plan a "
                               "rebuild if they matter" % (name, len(gone), label, rel_dir, sorted(gone)[0]))
                rp = ((entry or {}).get("params") or {}).get("records_path") or ""
                if rp.endswith("/records.json") and "/%s/" % ctx.deployment in rp:
                    rel_rec = "deployments/%s/%s" % (ctx.deployment, rp.split("/%s/" % ctx.deployment, 1)[1])
                    old, new = _git_show(ctx, ref, rel_rec), ctx.repo / rel_rec
                    try:
                        gone = ({i.get("url") for i in json.loads(old)} - {i.get("url") for i in read_records(new)}) if old and new.exists() else set()
                    except (ValueError, AttributeError):
                        gone = set()
                    if gone:
                        f.warn("%s: %d page url(s) in %s are gone from records.json (e.g. %s) -- okg keeps their old "
                               "facts live; plan a rebuild if they matter" % (name, len(gone), label, sorted(gone)[0]))
    return f.report("sources lint: ok -- %d rendered, %d pending" % (
        sum(ctx.selected(s) for s in ctx.sources), sum(not ctx.selected(s) for s in ctx.sources)))


# ----------------------------------------------------------------- render ----

def cmd_render(ctx, args):
    try:
        text, _ = render_text(ctx)
    except RenderError as exc:
        print("render: %s" % exc, file=sys.stderr)
        return 1
    if args.write:
        ctx.registry_path.write_text(text, encoding="utf-8")
        print("wrote %s" % ctx.registry_path.relative_to(ctx.repo))
    else:
        sys.stdout.write(text)
    return 0


def cmd_rename_class(ctx, args):
    """A class moved upstream (e.g. the engine PR's contract-check wants X -> Y):
    change it where it lives now, in sources/kinds.yaml, then re-render. Text
    edit, so the comments in kinds.yaml survive."""
    text = ctx.kinds_path.read_text(encoding="utf-8")
    pat = re.compile(r"^(\s*class:\s*)%s(\s*(?:#.*)?)$" % re.escape(args.old), re.M)
    new, n = pat.subn(lambda m: m.group(1) + args.new + m.group(2), text)
    if not n:
        print("rename-class: no `class: %s` in %s" % (args.old, ctx.kinds_path.relative_to(ctx.repo)), file=sys.stderr)
        return 1
    ctx.kinds_path.write_text(new, encoding="utf-8")
    ctx.kinds = load_yaml(ctx.kinds_path)
    print("renamed %s -> %s in %d kind(s)" % (args.old, args.new, n))
    args.write = True
    return cmd_render(ctx, args)


def cmd_status(ctx, args):
    rows = []
    for sid, s in ctx.sources.items():
        why = ctx.why_not(sid)
        extra = []
        if s.get("kind") == "git" and PLACEHOLDER_RE.search(str(s.get("git") or "")):
            extra.append("path unknown")
        if s.get("scope"):
            extra.append("needs scope")
        rows.append((sid, str(s.get("tier")), s.get("kind", "?"), "rendered" if not why else "pending",
                     "; ".join([w for w in [why] + extra if w])))
    w = [max(len(r[i]) for r in rows + [("id", "tier", "kind", "state", "")]) for i in range(4)]
    print("%-*s  %-*s  %-*s  %-*s  %s" % (w[0], "id", w[1], "tier", w[2], "kind", w[3], "state", "why"))
    for r in rows:
        print("%-*s  %-*s  %-*s  %-*s  %s" % (w[0], r[0], w[1], r[1], w[2], r[2], w[3], r[3], r[4]))
    return 0


# ------------------------------------------------------------------ probe ----

def glob_re(pattern):
    """git-style glob: ** crosses directories, * and ? do not."""
    out, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out, i = out + "(?:.*/)?", i + 3
        elif pattern.startswith("**", i):
            out, i = out + ".*", i + 2
        elif pattern[i] == "*":
            out, i = out + "[^/]*", i + 1
        elif pattern[i] == "?":
            out, i = out + "[^/]", i + 1
        else:
            out, i = out + re.escape(pattern[i]), i + 1
    return re.compile(out + r"\Z")


def in_scope(paths, scope):
    inc = [glob_re(g) for g in (scope or {}).get("include") or []]
    exc = [glob_re(g) for g in (scope or {}).get("exclude") or []]
    return [p for p in paths if (not inc or any(r.match(p) for r in inc)) and not any(r.match(p) for r in exc)]


def _git(args, timeout, cwd=None):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="true")
    return subprocess.run(["git"] + args, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout)


def _last_line(text):
    return mask_url((text.strip().splitlines() or ["?"])[-1])


def has_credential(host):
    r = _git(["config", "--get-urlmatch", "credential.helper", "https://%s/" % host], 20)
    return r.returncode == 0 and bool(r.stdout.strip())


def probe_git(ctx, sid, cache, refresh, strict):
    s = ctx.sources[sid]
    url = s.get("git") or ""
    if PLACEHOLDER_RE.search(url):
        return "skip", "repository path not filled in", {}
    if has_userinfo(url) or "@" in url.split("://", 1)[-1].split("/", 1)[0]:
        return "FAIL", "credentials in the git URL (never; use gitCredentials)", {}
    host = git_host(url)
    auth = source_auth(ctx, sid)
    if auth == "token" and not has_credential(host):
        return ("FAIL" if strict else "skip"), (
            "no git credential for %s in this environment; run the probe in the worker pod "
            "(see `sources.py --help`) or export the CI helper env" % host), {}
    try:
        r = _git(["ls-remote", "--symref", url, "HEAD"], 90)
    except subprocess.TimeoutExpired:
        return "FAIL", "ls-remote timed out (network/egress?)", {}
    if r.returncode != 0:
        return "FAIL", "cannot reach: %s (on GitLab, 'not found' also means 'no access')" % _last_line(r.stderr), {}
    m = re.search(r"^ref: refs/heads/(\S+)\s+HEAD", r.stdout, re.M)
    if not m:
        return "FAIL", "no default branch advertised (empty repository?)", {}
    default = m.group(1)
    info = {"default_branch": default}
    problems = []
    if s.get("branch") and s["branch"] != default:
        problems.append("declared branch %s but the default branch is %s (the clone follows the default)" % (s["branch"], default))
    tmp = None
    base = Path(cache) if cache else Path(tempfile.mkdtemp(prefix="sources-probe-"))
    if not cache:
        tmp = base
    dest = base / ("%s.git" % sid)
    try:
        if dest.exists() and refresh:
            shutil.rmtree(dest, ignore_errors=True)
        if not dest.exists():
            base.mkdir(parents=True, exist_ok=True)
            c = _git(["clone", "--quiet", "--bare", "--depth", "1", "--filter=blob:none", "--no-tags", url, str(dest)], 900)
            if c.returncode != 0:
                return "FAIL", "clone failed: %s" % _last_line(c.stderr), info
        t = _git(["ls-tree", "-r", "--name-only", "HEAD"], 300, cwd=str(dest))
        head = _git(["rev-parse", "--short=10", "HEAD"], 30, cwd=str(dest)).stdout.strip()
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
    if t.returncode != 0:
        return "FAIL", "cannot list files: %s" % _last_line(t.stderr), info
    paths = [p for p in t.stdout.split("\n") if p]
    if not paths:
        return "FAIL", "the repository has no files on %s" % default, info
    scoped = in_scope(paths, s.get("scope"))
    budget = ctx.max_files(sid)
    ext = collections.Counter(os.path.splitext(p)[1].lower() or "<none>" for p in scoped)
    info.update(head=head, files_total=len(paths), files_in_scope=len(scoped), max_files=budget,
                est_nodes=len(scoped) * NODES_PER_FILE, top_ext=dict(ext.most_common(6)))
    scope_ok = bool(ctx.kinds and ctx.kinds["kinds"]["git"].get("scope_fields"))
    if s.get("scope") and not scope_ok:
        problems.append("scope not supported by the pinned engine yet: enabled today it would ingest all %d files" % len(paths))
    if len(scoped) > budget:
        problems.append("%d files in scope > budget %d (raise max_files deliberately, or scope it)" % (len(scoped), budget))
    if s.get("scope") and not scoped:
        problems.append("scope matches no file")
    detail = "%s@%s  %d files%s  ~%dk nodes  %s" % (
        default, head, len(scoped), (" of %d" % len(paths)) if s.get("scope") else "",
        info["est_nodes"] // 1000, ", ".join("%s=%d" % kv for kv in ext.most_common(4)))
    return ("FAIL" if problems else "ok"), "; ".join([detail] + problems), info


def probe_catalog(ctx, sid):
    entry = _subst(ctx.kind(sid)["entry"], _env(ctx, sid))
    url = (entry.get("params") or {}).get("releases_map_url")
    if not url:
        return "skip", "no releases_map_url in the kind", {}
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            body = resp.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001 -- report any network failure
        return "FAIL", "cannot fetch %s: %s" % (url, exc), {}
    n = sum("label=CMSSW_" in line for line in body.splitlines())
    return ("ok" if n else "FAIL"), "%d releases in %s" % (n, url), {"releases": n}


def cmd_probe(ctx, args):
    if args.all:
        ids = list(ctx.sources)
    elif args.id:
        ids = args.id
    elif args.tier is not None:
        ids = [sid for sid, s in ctx.sources.items() if s.get("tier") == args.tier]
    else:
        ids = [sid for sid in ctx.sources if ctx.selected(sid)]
    unknown = [i for i in ids if i not in ctx.sources]
    if unknown:
        raise InputError("unknown source id(s): %s" % unknown)
    rows, report = [], {}
    for sid in ids:
        kind = ctx.sources[sid].get("kind")
        try:
            if kind == "git":
                res = probe_git(ctx, sid, args.cache, args.refresh, args.strict)
            elif kind == "cmssw-releases":
                res = probe_catalog(ctx, sid) if ctx.kinds else ("skip", "needs sources/kinds.yaml (pass --repo)", {})
            else:
                check = ((ctx.kinds or {}).get("kinds", {}).get(kind) or {}).get("data_check") or (
                    "records-json" if kind == "docs-files" else "twiki-tree" if kind == "twiki-raw" else None)
                if check and ctx.sources[sid].get("data"):
                    f = Findings()
                    data = ctx.dep_dir / ctx.sources[sid]["data"]
                    if check == "records-json":
                        check_records_json(data / "records.json", f, sid)
                    else:
                        check_twiki_tree(data, f, sid)
                    res = ("FAIL" if f.errors else "ok"), "; ".join(f.errors + f.warnings + f.notes), {}
                else:
                    res = "skip", "no network probe for kind %s (contract binds it; the e2e ingests it)" % kind, {}
        except subprocess.TimeoutExpired as exc:
            res = "FAIL", "timed out: %s" % exc, {}
        rows.append((sid, str(ctx.sources[sid].get("tier")), res[0], res[1]))
        report[sid] = {"result": res[0], "detail": res[1], **res[2]}
        print("%-18s %-4s %-4s %s" % rows[-1], flush=True)
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("| source | tier | result | detail |\n|---|---|---|---|\n")
            for r in rows:
                fh.write("| %s | %s | %s | %s |\n" % tuple(x.replace("|", "\\|") for x in r))
    return 1 if any(r[2] == "FAIL" for r in rows) else 0


# --------------------------------------------------------------- contract ----

# One page for each data kind, run through the pinned reader: it must accept the
# shape our tools write and emit only what the kind's output_signature declares.
_FIXTURE_TOPIC = ('%META:TOPICINFO{author="x" date="1" format="1.1" version="1"}%\n'
                  '%META:TOPICPARENT{name="WebHome"}%\n---+ Contract Probe\n\n'
                  "The crab submit command sends a task. See CRAB3FAQ for more.\n")


def _fixture(kind, root):
    if kind.get("data_check") == "records-json":
        p = root / "data" / "records.json"
        p.parent.mkdir(parents=True)
        p.write_text(json.dumps([{"url": "https://twiki.cern.ch/twiki/bin/view/CMSPublic/ContractProbe",
                                  "title": "Contract Probe", "path": "CMSPublic/ContractProbe", "site_name": "twiki.cern.ch",
                                  "body": "# Contract Probe\n\n" + "The crab submit command sends a task. " * 12}]))
        return {"records_path": str(p)}
    if kind.get("data_check") == "twiki-tree":
        p = root / "data" / "CMSPublic" / "ContractProbe.txt"
        p.parent.mkdir(parents=True)
        p.write_text(_FIXTURE_TOPIC)
        return {"eos_root": str(root / "data")}
    return None


def _run_fixture(name, cls, params, signature, f):
    """Drive the reader behind the adapter over the fixture; compare its facts to the signature."""
    reader_cls = getattr(cls, "reader_class", None) or cls
    try:
        reader = reader_cls(**params)
        run = reader.run("sources-contract", mode="scope_complete")
        facts = list(run.facts)
    except Exception as exc:  # noqa: BLE001 -- any failure is the finding
        f.error("%s: the pinned reader fails on a one-page fixture: %s: %s" % (name, type(exc).__name__, exc))
        return
    nodes = {getattr(x, "subtype", None) for x in facts if getattr(x, "subtype", None)}
    edges = {getattr(x, "edge_type", None) for x in facts if getattr(x, "edge_type", None)}
    sig_nodes = {n.get("subtype") for n in signature.get("nodes") or []}
    sig_edges = {e.get("edge_type") for e in signature.get("edges") or []}
    status = getattr(getattr(run, "health", None), "status", "?")
    if not nodes:
        f.error("%s: the pinned reader emitted nothing for a valid one-page fixture (health %s)" % (name, status))
    if nodes - sig_nodes or edges - sig_edges:
        f.error("%s: the pinned reader emits %s outside output_signature (%s) -- strict admission would refuse the run"
                % (name, sorted((nodes - sig_nodes) | (edges - sig_edges)), sorted(sig_nodes | sig_edges)))
    if not getattr(run, "completed_scope", False):
        f.warn("%s: fixture run did not claim a complete scope (health %s)" % (name, status))
    f.note("%s: fixture -> %s + %s, health %s" % (name, sorted(nodes), sorted(edges), status))


def _okg_keys_near_code_repos():
    """Evidence of what the pinned okg reads for `code_repos`: files that mention
    it, and every mapping key / field / keyword name used in those files. A key
    found here is NECESSARY, not sufficient: `verify` after an ingest is the proof."""
    import okg  # noqa: F401 -- only inside the image
    root = Path(okg.__file__).resolve().parent
    hits, keys = [], set()
    for p in sorted(root.rglob("*")):
        if p.suffix not in (".py", ".yaml", ".yml") or not p.is_file():
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if "code_repos" not in src:
            continue
        lines = [i + 1 for i, line in enumerate(src.splitlines()) if "code_repos" in line]
        hits.append("%s:%s" % (p.relative_to(root.parent), ",".join(map(str, lines[:8]))))
        if p.suffix != ".py":
            continue
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in (
                    "get", "pop", "setdefault") and node.args and isinstance(node.args[0], ast.Constant):
                keys.add(node.args[0].value)
            elif isinstance(node, ast.Subscript):
                sl = node.slice.value if isinstance(node.slice, getattr(ast, "Index", ())) else node.slice  # py<3.9 shape
                if isinstance(sl, ast.Constant):
                    keys.add(sl.value)
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                keys.add(node.target.id)
            elif isinstance(node, ast.keyword) and node.arg:
                keys.add(node.arg)
    return root, hits, {k for k in keys if isinstance(k, str)}


def _string_collections(path):
    """NAME = {...}/[...]/(...)/frozenset(...)/Literal[...] of >= 2 strings, from one file."""
    out = []
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (SyntaxError, OSError, UnicodeDecodeError):
        return out
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        names = [t.id for t in targets if isinstance(t, ast.Name)]
        val = node.value
        if val is None or not names:
            continue
        if isinstance(val, ast.Call) and val.args:
            val = val.args[0]
        if isinstance(val, ast.Subscript):
            val = val.slice.value if isinstance(val.slice, getattr(ast, "Index", ())) else val.slice
        elts = getattr(val, "elts", None) if isinstance(val, (ast.Set, ast.List, ast.Tuple)) else None
        strs = [e.value for e in elts or [] if isinstance(e, ast.Constant) and isinstance(e.value, str)]
        if len(strs) >= 2 and len(strs) == len(elts or []):
            out.append((names[0], strs, node.lineno))
    return out


def cmd_inventory(ctx, args):
    """Read-only map of what the pinned engine offers, for writing modules,
    kinds and Nomos policies without guessing. Markdown on stdout."""
    try:
        import okg
    except ImportError as exc:
        print("inventory must run inside the pinned image (okg not importable: %s)" % exc, file=sys.stderr)
        return 2
    root = Path(okg.__file__).resolve().parent
    out = ["## Engine inventory", "",
           "okg `%s`, archi `%s` (from the image environment)" % (
               os.environ.get("OKG_CODE_REVISION", "?")[:12], os.environ.get("ARCHI_CODE_REVISION", "?")[:12]), ""]
    # 1. ontology modules: any directory named `modules` in okg, its children, and the
    #    LinkML classes (= node subtypes) their YAML declares
    out += ["### Ontology modules (what `deployment.yaml` `modules:` may name)", ""]
    mod_dirs = [d for d in root.rglob("modules") if d.is_dir() and "__pycache__" not in d.parts and len(d.relative_to(root).parts) <= 5]
    for md in sorted(mod_dirs):
        children = sorted(c for c in md.iterdir() if not c.name.startswith(("_", ".")))
        if not children:
            continue
        out += ["`%s`" % md.relative_to(root.parent), "", "| module | subtypes it declares |", "|---|---|"]
        for c in children:
            classes = set()
            for y in ([c] if c.is_file() else sorted(c.rglob("*.y*ml"))):
                if y.suffix not in (".yaml", ".yml"):
                    continue
                try:
                    doc = yaml.safe_load(y.read_text(encoding="utf-8"))
                except (yaml.YAMLError, OSError, UnicodeDecodeError):
                    continue
                if isinstance(doc, dict) and isinstance(doc.get("classes"), dict):
                    classes.update(doc["classes"])
            name = c.stem if c.is_file() else c.name
            shown = ", ".join(sorted(classes)[:14]) + (" ..." if len(classes) > 14 else "")
            out.append("| `%s` | %s |" % (name, shown or "(no LinkML classes found)"))
        out.append("")
    if not mod_dirs:
        out += ["No `modules` directory found under %s; look for the module loader in okg." % root, ""]
    # 2. the code-graph template the `git` kind mirrors
    tpl = root / "substrate" / "library" / "templates" / "codebase-index"
    out += ["### codebase-index template (the `git` kind: `code_repos`, lanes, scope keys)", ""]
    if tpl.is_dir():
        for y in sorted(tpl.rglob("*")):
            if y.is_file() and y.suffix in (".yaml", ".yml", ".example", ".md") and "schemas" not in y.parts:
                text = y.read_text(encoding="utf-8", errors="replace").splitlines()
                out += ["<details><summary>%s (%d lines)</summary>" % (y.relative_to(tpl), len(text)), "", "```yaml",
                        *text[:220], "```", "</details>", ""]
    else:
        out += ["not found at %s" % tpl, ""]
    # 3. the Nomos vocabulary
    nomos = root / "substrate" / "nomos"
    out += ["### Nomos vocabulary (values a posture or source policy may use)", ""]
    for py in sorted(nomos.glob("*.py")) if nomos.is_dir() else []:
        for name, values, line in _string_collections(py):
            if any(v in values for v in ("public", "public_reference_demo", "remote_api", "deny", "normal", "audit")) \
                    or re.search(r"CLASS|SENSITIV|PROVENANCE|EXPORT|RETENTION|CLASSIFICATION|PRINCIPAL|POLICY|OBLIGATION", name):
                out.append("- `%s` (%s:%d): %s" % (name, py.name, line, ", ".join("`%s`" % v for v in values)))
    out.append("")
    # 4. archi's connector templates
    bundle = Path(os.environ.get("OKG_PROFILES_DIR", "/opt/archi/bundles")) / "cern-team" / "source-defaults"
    out += ["### archi cern-team source templates (candidates for new kinds)", ""]
    for y in sorted(bundle.glob("*.y*ml*")) if bundle.is_dir() else []:
        try:
            doc = yaml.safe_load(y.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            continue
        for bname, entry in (doc.items() if isinstance(doc, dict) else []):
            if isinstance(entry, dict) and "module" in entry:
                out.append("- `%s` (%s): `%s.%s`, source_class `%s`" % (
                    bname, y.name, entry.get("module"), entry.get("class"), entry.get("source_class")))
    text = "\n".join(out) + "\n"
    sys.stdout.write(text)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("<details><summary>Engine inventory (modules, templates, Nomos vocabulary)</summary>\n\n" + text + "\n</details>\n")
    return 0


def cmd_contract(ctx, args):
    import importlib
    import inspect
    f = Findings()
    try:
        import importlib.util as _u
        if _u.find_spec("okg") is None:
            raise ImportError("no module named okg")
    except ImportError as exc:
        print("contract must run inside the pinned image (okg not importable: %s)" % exc, file=sys.stderr)
        return 2
    try:
        from okg.deployment import ConnectorAdapter
    except ImportError as exc:
        f.error("okg.deployment.ConnectorAdapter is gone from the pinned okg (%s): the adapter check in this tool and "
                "archi's ReaderAdapter both need re-reading" % exc)
        ConnectorAdapter = None
    reg = load_yaml(ctx.registry_path)
    rendered = reg.get("sources") or {}
    # Every `source` kind, rendered or not: a kind must work on the new engine
    # BEFORE the PR that enables it, not in it.
    entries = dict(rendered)
    fixtures = {}
    for kname, kind in ((ctx.kinds or {}).get("kinds") or {}).items():
        if kind.get("render") != "source":
            continue
        probe_id = "contract-%s" % kname
        env = _env(ctx, probe_id, {"data": "data/contract", "git": ""})
        entries.setdefault("~kind " + kname, _subst(copy.deepcopy(kind["entry"]), env))
        fixtures["~kind " + kname] = kind
    for name, src in entries.items():
        try:
            cls = getattr(importlib.import_module(src["module"]), src["class"])
        except (ImportError, AttributeError) as exc:
            f.error("%s: %s.%s does not import: %s" % (name, src.get("module"), src.get("class"), exc))
            continue
        if ConnectorAdapter is not None and src["module"].startswith("archi.") and not (
                isinstance(cls, type) and issubclass(cls, ConnectorAdapter)):
            f.error("%s: %s is a bare reader; the registry needs its *Adapter (a bare reader crashes the runner)" % (name, src["class"]))
        params = dict(src.get("params") or {})
        try:
            inspect.signature(cls).bind(**params)
        except TypeError as exc:
            f.error("%s: params do not bind to %s.%s: %s" % (name, src["module"], src["class"], exc))
            continue
        f.note("%s: %s.%s binds" % (name, src["module"], src["class"]))
        kind = fixtures.get(name)
        if kind is not None:
            with tempfile.TemporaryDirectory(prefix="sources-contract-") as tmp:
                override = _fixture(kind, Path(tmp))
                if override is not None:
                    params.update(override)
                    _run_fixture(name, cls, params, (src.get("admission_policy") or {}).get("output_signature") or {}, f)
    repos = (reg.get("code_repos") or {}).get("repos") or []
    root, hits, keys = _okg_keys_near_code_repos()
    f.note("okg package: %s" % root)
    f.note("files mentioning code_repos: %s" % ("; ".join(hits) or "NONE"))
    if repos and not hits:
        f.error("the registry has code_repos but the pinned okg never mentions it -- the block would be ignored")
    for key in sorted({k for r in repos for k in r}):
        if key not in keys:
            f.warn("code_repos repo key %r not found near okg's code_repos handling (static scan) -- confirm it is read" % key)
    scope_fields = (ctx.kinds or {}).get("kinds", {}).get("git", {}).get("scope_fields") or {}
    for part, key in scope_fields.items():
        if key not in keys:
            f.error("kinds git.scope_fields.%s = %r, but the pinned okg never reads that key near code_repos: an "
                    "unread scope key means the WHOLE repo is ingested" % (part, key))
    lock = load_yaml(ctx.repo / "versions.lock") if (ctx.repo / "versions.lock").exists() else {}
    ra = (ctx.kinds or {}).get("reviewed_against") or {}
    lock = lock or {}
    pinned = {"archi": str((lock.get("archi") or {}).get("commit") or ""),
              "okg": str((lock.get("upstream") or {}).get("commit") or (lock.get("okg") or {}).get("commit") or "")}
    if not any(pinned.values()):
        f.note("versions.lock names no archi/okg commit this tool recognises; reviewed_against not compared")
    for k, v in pinned.items():
        if v and ra.get(k) and not v.startswith(str(ra[k])):
            f.warn("sources/kinds.yaml was reviewed against %s %s; versions.lock pins %s -- read vendor/reference/ "
                   "diffs, adjust kinds, then bump reviewed_against" % (k, ra[k], v[:10]))
    curate = ctx.repo / "scripts" / "twiki-curate.py"
    if curate.exists():
        import importlib.util
        try:
            spec = importlib.util.spec_from_file_location("twiki_curate", str(curate))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            from archi.sources import _twiki_physics as phys, _twiki_parse as parse
            for rx in ("PAG_CODE_RE", "POG_NAME_RE", "PHYSICS_ROOT_RE"):
                if getattr(mod, rx).pattern != getattr(phys, rx).pattern:
                    f.error("scripts/twiki-curate.py %s differs from the pinned archi's; copy it over" % rx)
            if tuple(mod.DEFAULT_SKIP_PATTERNS) != tuple(parse.DEFAULT_SKIP_PATTERNS):
                f.error("scripts/twiki-curate.py DEFAULT_SKIP_PATTERNS differ from the pinned archi's; copy them over")
        except (ImportError, AttributeError) as exc:
            f.warn("could not compare scripts/twiki-curate.py with the pinned archi: %s" % exc)
    return f.report("sources contract: ok against the pinned image")


# ----------------------------------------------------------------- verify ----

_VERIFY_SQL = ("SELECT split_part(node_id, ':', 2) AS slug, count(*) FROM okg.v_nodes "
               "WHERE subtype = 'source_file' AND node_id LIKE 'file:%' GROUP BY 1")


def _query(dsn, sql):
    try:
        import psycopg
        with psycopg.connect(dsn) as conn:
            return conn.execute(sql).fetchall()
    except ImportError:
        pass
    try:
        import psycopg2
        conn = psycopg2.connect(dsn)
        try:
            cur = conn.cursor()
            cur.execute(sql)
            return cur.fetchall()
        finally:
            conn.close()
    except ImportError:
        pass
    r = subprocess.run(["psql", dsn, "-At", "-F", "\t", "-c", sql], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError("psql: %s" % r.stderr.strip()[:300])
    return [tuple(line.split("\t")) for line in r.stdout.splitlines() if line]


def cmd_verify(ctx, args):
    f = Findings()
    dsn = os.environ.get("OKG_DSN")
    if not dsn:
        print("verify needs OKG_DSN (run it where the ingest ran: CI e2e or the worker pod)", file=sys.stderr)
        return 2
    try:
        counts = {str(slug): int(n) for slug, n in _query(dsn, _VERIFY_SQL)}
    except Exception as exc:  # noqa: BLE001
        print("verify: query failed: %s" % mask_url(str(exc)), file=sys.stderr)
        return 2
    probed = json.loads(Path(args.probe).read_text()) if args.probe else {}
    for sid, s in ctx.sources.items():
        if not ctx.selected(sid) or s.get("kind") != "git":
            continue
        n = counts.get(sid, 0)
        cap = ctx.max_files(sid)
        in_scope = (probed.get(sid) or {}).get("files_in_scope")
        if n == 0:
            f.error("%s: no source_file nodes -- the git lanes did not run for it" % sid)
        elif n > cap:
            f.error("%s: %d source_file nodes > budget %d -- %s" % (
                sid, n, cap, "the scope was NOT honoured" if s.get("scope") else "the repo is bigger than planned"))
        elif in_scope is not None and n > in_scope * 1.05 + 5:
            f.error("%s: %d source_file nodes, but the probe found %d files in scope -- %s" % (
                sid, n, in_scope, "the scope was NOT honoured" if s.get("scope") else "the repo grew since the probe; re-probe"))
        else:
            f.note("%s: %d source_file nodes (budget %d%s)" % (sid, n, cap, ", probed %d" % in_scope if in_scope is not None else ""))
    return f.report("sources verify: every rendered git source ingested within its budget")


# ------------------------------------------------------------------- main ----

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("--deployment", default="archi-crab")
    ap.add_argument("--repo", default=str(REPO), help="repository root (default: this script's repo, or $OKG_REPO_ROOT from stdin)")
    ap.add_argument("--manifest-b64", help="the source list as base64 (for running from stdin in a pod)")
    # The same three also after the subcommand (`python - probe --manifest-b64 ...`).
    common = argparse.ArgumentParser(add_help=False)
    for flag in ("--deployment", "--repo", "--manifest-b64"):
        common.add_argument(flag, default=argparse.SUPPRESS)
    sub = ap.add_subparsers(dest="cmd", required=True)
    _add = sub.add_parser
    sub.add_parser = lambda name, **kw: _add(name, parents=[common], **kw)
    r = sub.add_parser("render")
    r.add_argument("--write", action="store_true")
    li = sub.add_parser("lint")
    li.add_argument("--base", action="append", help="git ref, or `published` (staging + prod revisions); repeatable")
    li.add_argument("--allow-identity-change", action="store_true",
                    help="downgrade vanished/renamed sources to warnings (you plan a rebuild)")
    sub.add_parser("status")
    p = sub.add_parser("probe")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--tier", type=int)
    g.add_argument("--id", action="append")
    g.add_argument("--all", action="store_true")
    p.add_argument("--cache", help="keep treeless clones here and reuse them")
    p.add_argument("--refresh", action="store_true", help="re-clone cached repos")
    p.add_argument("--json", help="write the results as JSON (verify --probe reads it)")
    p.add_argument("--strict", action="store_true", help="a source that cannot be checked here fails instead of skipping")
    sub.add_parser("contract")
    sub.add_parser("inventory")
    rc = sub.add_parser("rename-class")
    rc.add_argument("old")
    rc.add_argument("new")
    v = sub.add_parser("verify")
    v.add_argument("--probe", help="probe --json output: also require source_file count <= probed in-scope files")
    args = ap.parse_args(argv)
    try:
        ctx = Ctx(args)
        return {"render": cmd_render, "lint": cmd_lint, "status": cmd_status, "probe": cmd_probe,
                "contract": cmd_contract, "verify": cmd_verify, "rename-class": cmd_rename_class,
                "inventory": cmd_inventory}[args.cmd](ctx, args)
    except InputError as exc:
        print("sources: %s" % exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
