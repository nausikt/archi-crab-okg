#!/usr/bin/env python3
"""release.py — the engine x corpus release matrix (releases/*.yaml, docs/RELEASES.md).

    python3 scripts/release.py show                     # every URL -> instance, status
    python3 scripts/release.py lint [--tags]            # matrix, pins, corpus fingerprints (+ git tags)
    python3 scripts/release.py fingerprint [REV]        # corpus fingerprint of a commit (default HEAD)
    python3 scripts/release.py render okg:<engine>/<corpus> [--revision SHA]   # write a planned instance's values
    python3 scripts/release.py render v2:<corpus>
    python3 scripts/release.py iac okg:<engine>/<corpus> [--target SHA]   # the CMSKubernetes Argo app + proxy entry
    python3 scripts/release.py iac v2:<corpus>
    python3 scripts/release.py budget                   # Cinder volumes per type
    python3 scripts/release.py adapter ENGINE [REV]      # where ENGINE's adapter is at REV (default HEAD)
    python3 scripts/release.py freeze-adapter ENGINE COMMIT   # copy an older engine's adapter to deployments/compat/ENGINE
    python3 scripts/release.py engine-entry ENGINE COMMIT     # the engines.yaml entry of an engine build (versions.lock at COMMIT)

Read-only except `render`, which writes one values file and refuses a live instance.
Needs PyYAML and a git checkout. lint resolves commits locally: `git fetch --tags` first.
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = os.path.join(ROOT, "releases")
STATUSES = ("planned", "building", "live", "retired")
DNS = re.compile(r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$")
MAX_RELEASE = 40  # + "-postgres" + STS revision hash (11) must stay <= 63


# ---------------------------------------------------------------- git + io
def git(*args, check=True):
    p = subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError("git %s: %s" % (" ".join(args), p.stderr.strip()))
    return p.stdout.strip() if p.returncode == 0 else None


def load(name):
    with open(os.path.join(REL, name)) as f:
        return yaml.safe_load(f)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def storage(default, override):
    """{volume: (size, class)}: the product default, overridden per instance."""
    out = {k: tuple(v) for k, v in default.items()}
    out.update({k: tuple(v) for k, v in (override or {}).items()})
    return out


def fingerprint(rev, paths):
    """sha256 over (path, git object id) of every corpus path at rev. None if rev is unknown."""
    if git("cat-file", "-e", "%s^{commit}" % rev, check=False) is None:
        return None, {}
    objs = {}
    for p in paths:
        objs[p] = git("rev-parse", "%s:%s" % (rev, p), check=False) or "MISSING"
    h = hashlib.sha256("".join("%s\0%s\n" % (p, objs[p]) for p in paths).encode())
    return "sha256:" + h.hexdigest(), objs


def tag_commit(tag):
    return git("rev-parse", "-q", "--verify", "refs/tags/%s^{commit}" % tag, check=False)


# ---------------------------------------------------------------- engine adapters
# An engine's ADAPTER is how this repository speaks to it: sources/kinds.yaml plus
# deployments/<dep>/ minus the corpus (data/), the rendered registry and VENDOR.yaml. On main,
# the newest engine's adapter is native (deployments/); an older engine still in the matrix
# keeps a frozen copy in deployments/compat/<engine>/ (freeze-adapter), with its own render of
# the current source list. An instance points the chart at one with okg.deploymentsPath.
DEP = "archi-crab"
ADAPTER_SKIP = ("data", "source_registry.yaml", "VENDOR.yaml")


def adapter_files(rev, path):
    """{relative name: content sha256} of the adapter at `path` ("deployments" or a compat
    dir), at commit `rev`, or in the working tree when rev is None. None if absent."""
    kinds = "sources/kinds.yaml" if path == "deployments" else path + "/kinds.yaml"
    base = "%s/%s/" % (path, DEP)
    out = {}
    if rev is None:
        kp, bp = os.path.join(ROOT, kinds), os.path.join(ROOT, base)
        if not (os.path.isfile(kp) and os.path.isdir(bp)):
            return None
        out["kinds.yaml"] = hashlib.sha256(open(kp, "rb").read()).hexdigest()
        for dirpath, dirs, files in os.walk(bp):
            rel_dir = os.path.relpath(dirpath, bp)
            if rel_dir == ".":
                dirs[:] = [x for x in dirs if x not in ADAPTER_SKIP]
            for fn in files:
                rel = os.path.normpath(os.path.join(rel_dir, fn))
                if rel.split(os.sep)[0] in ADAPTER_SKIP or os.path.islink(os.path.join(dirpath, fn)):
                    continue
                out[rel] = hashlib.sha256(open(os.path.join(dirpath, fn), "rb").read()).hexdigest()
        return out
    if git("cat-file", "-e", "%s:%s" % (rev, kinds), check=False) is None:
        return None
    listing = git("ls-tree", "-r", "--full-tree", rev, "--", base, check=False) or ""
    if not listing:
        return None
    out["kinds.yaml"] = hashlib.sha256(git_bytes("show", "%s:%s" % (rev, kinds))).hexdigest()
    for line in listing.splitlines():
        meta, name = line.split("\t", 1)
        mode, kind = meta.split()[:2]
        rel = name[len(base):]
        if kind != "blob" or mode == "120000" or rel.split("/")[0] in ADAPTER_SKIP:
            continue
        out[rel] = hashlib.sha256(git_bytes("show", "%s:%s" % (rev, name))).hexdigest()
    return out


def adapter_fingerprint(rev, path):
    files = adapter_files(rev, path)
    if files is None:
        return None
    return "sha256:" + hashlib.sha256("".join("%s\0%s\n" % kv for kv in sorted(files.items())).encode()).hexdigest()


def git_bytes(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, check=True).stdout


def adapter_path_for(engine, rev):
    """Which deploymentsPath carries `engine`'s adapter at `rev`: native first, then its compat dir."""
    ad = engine.get("adapter") or {}
    for path in ("deployments", ad.get("compat") or ""):
        if path and adapter_fingerprint(rev, path) == ad.get("fingerprint"):
            return path
    return None


def freeze_adapter(mx, eid, commit):
    e = mx.engines["okg"].get(eid)
    if not e:
        raise SystemExit("no okg engine %s in engines.yaml" % eid)
    full = git("rev-parse", "%s^{commit}" % commit)
    dest = "deployments/compat/%s" % slug(eid)
    if os.path.exists(os.path.join(ROOT, dest)):
        raise SystemExit("%s exists: an adapter is frozen once (delete it first to re-freeze)" % dest)
    os.makedirs(os.path.join(ROOT, dest, DEP))
    with open(os.path.join(ROOT, dest, "kinds.yaml"), "wb") as f:
        f.write(git_bytes("show", "%s:sources/kinds.yaml" % full))
    base = "deployments/%s/" % DEP
    for line in git("ls-tree", "-r", "--full-tree", full, "--", base).splitlines():
        meta, name = line.split("\t", 1)
        rel = name[len(base):]
        if rel.split("/")[0] in ADAPTER_SKIP:
            continue
        out = os.path.join(ROOT, dest, DEP, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "wb") as f:
            f.write(git_bytes("show", "%s:%s" % (full, name)))
        if meta.split()[0] == "100755":
            os.chmod(out, 0o755)
    # the corpus stays single-sourced: OKG_DEPLOYMENTS_DIR/<dep>/data resolves to the live one
    os.symlink("../../../%s/data" % DEP, os.path.join(ROOT, dest, DEP, "data"))
    with open(os.path.join(ROOT, dest, "compat.yaml"), "w") as f:
        f.write(COMPAT_YAML.format(engine=eid, commit=full, dest=dest))
    fp = adapter_fingerprint(None, dest)
    print("froze engine %s's adapter from %s into %s\n  fingerprint %s" % (eid, full[:12], dest, fp))
    print("next: python3 scripts/sources.py render --write   (writes %s/%s/source_registry.yaml)" % (dest, DEP))
    print("      releases/engines.yaml okg.%s.adapter: {compat: %s, fingerprint: \"%s\"}" % (eid, dest, fp))


COMPAT_YAML = """\
# {dest} -- engine {engine}'s adapter, FROZEN from {commit}
# by `scripts/release.py freeze-adapter`. Never edit these files: releases/engines.yaml holds
# their fingerprint and release.py lint refuses a drift. What is here:
#   kinds.yaml               sources/kinds.yaml as this engine reads it
#   archi-crab/              deployment.yaml, extractors, invariants, schemas, skills
#     data -> ../../../archi-crab/data     the corpus (shared; a symlink)
#     source_registry.yaml   GENERATED: the CURRENT source list rendered with kinds.yaml above
#                            (scripts/sources.py render --write; CI checks it)
# An instance of this engine on a newer corpus sets okg.deploymentsPath: {dest}
engine: "{engine}"
frozen_from: {commit}
# Sources of the current list this engine cannot ingest: {{source id: reason}}. They are left
# out of THIS render only; the matrix reports them for every instance that uses this adapter.
exclude: {{}}
"""


def engine_entry(eid, commit):
    """Print the releases/engines.yaml entry of an engine build: versions.lock at COMMIT (the
    engine workflow's build commit, e.g. the tag engine/<eid>) and the adapter it carries."""
    full = git("rev-parse", "%s^{commit}" % commit)
    lock = yaml.safe_load(git("show", "%s:versions.lock" % full)) or {}
    up, ar, rt = lock.get("upstream") or {}, lock.get("archi") or {}, lock.get("runtime") or {}
    pg = str(((lock.get("images") or {}).get("okg-postgres") or {}).get("ref") or "")
    if "@" not in pg or not str(rt.get("digest", "")).startswith("sha256:"):
        raise SystemExit("versions.lock at %s has no built runtime/postgres digest: not an engine build" % full[:12])
    pg_repo, pg_digest = pg.split("@", 1)
    fp = adapter_fingerprint(full, "deployments")
    print('''  "%s":
    status: released
    released: "%s"
    note: >-
      okg %s (track %s) + archi-okg %s, built by the engine workflow; tag engine/%s = %s.
    okg: %s
    archi_okg: %s
    runtime: {repository: %s, digest: "%s"}
    postgres: {repository: %s, digest: "%s"}
    readinessProfile: ""
    adapter:
      native: %s
      compat: ""
      fingerprint: "%s"''' % (eid, git("log", "-1", "--format=%cs", full), str(up.get("commit", ""))[:12],
                              up.get("track", "?"), str(ar.get("commit", ""))[:12], eid, full[:12],
                              up.get("commit"), ar.get("commit"), rt.get("ref"), rt.get("digest"),
                              pg_repo, pg_digest, full, fp))


# ---------------------------------------------------------------- the model
class Matrix:
    def __init__(self):
        self.engines, self.corpus, self.m = load("engines.yaml"), load("corpus.yaml"), load("matrix.yaml")
        self.paths = self.corpus["paths"]

    def okg(self):
        host, ns = self.m["hosts"]["okg"], self.m["okg"]["namespace"]
        out = []
        for i in self.m["okg"]["instances"]:
            e, c = str(i["engine"]), str(i["corpus"])
            # A SLOT (e.g. dev) is ONE fixed instance whose engine AND corpus move: every name
            # below comes from the slot alone, so its volumes, Secret, URL and proxy survive the
            # weekly rebuild. Only the deploy tag names what it currently serves.
            slot = i.get("slot")
            if slot:
                key, pair, path, vals = slug(str(slot)), str(slot), "/releases/%s" % slot, "envs/releases/%s/values.yaml" % slot
            else:
                key, pair = "%s-%s" % (slug(e), slug(c)), "%s/%s" % (e, c)
                path, vals = "/releases/%s/%s" % (e, c), "envs/releases/%s/%s/values.yaml" % (e, c)
            d = dict(i, engine=e, corpus=c, kind="okg", id="okg:" + pair, namespace=ns, host=host,
                     slot=slot, pair=pair)
            d.setdefault("path", path)
            d.setdefault("release", "archi-crab-okg-" + key)
            d.setdefault("secret", "okg-archi-crab-" + key)
            d.setdefault("argoApp", d["release"])
            d.setdefault("values", vals)
            d.setdefault("deployTag", "okg/releases/%s/%s" % (e, c))
            d.setdefault("proxy", "okg-" + key)
            d["storage"] = storage(self.m["okg"]["storage"], i.get("storage"))
            d["url"] = "https://%s%s/mcp" % (host, d["path"])
            d["env"] = "staging"
            out.append(d)
        p = (self.m.get("prod") or {}).get("okg")
        if p:
            e, c = str(p["engine"]), str(p["corpus"])
            d = dict(p, engine=e, corpus=c, kind="okg", id="prod:%s/%s" % (e, c), env="prod", path="",
                     slot=None, pair="%s/%s" % (e, c))
            if p.get("slot"):
                raise SystemExit("matrix.yaml prod.okg: slots live in staging only")
            d.setdefault("deployTag", "okg/prod/%s/%s" % (e, c))
            d["storage"] = storage(self.m["okg"]["storage"], p.get("storage"))
            d["url"] = "https://%s/mcp" % d["host"]
            out.append(d)
        return out

    def v2(self):
        v, host = self.m["v2"], self.m["hosts"]["v2"]
        out = []
        for i in v["instances"]:
            c = str(i["corpus"])
            d = dict(i, corpus=c, kind="v2", id="v2:" + c, engine=v["engine"], host=host, env="staging")
            d.setdefault("namespace", v["namespace"])
            d.setdefault("release", "archi-v2-" + slug(c))
            d.setdefault("argoApp", d["release"])
            d.setdefault("values", "v2/envs/releases/%s/values.yaml" % c)
            d.setdefault("deployTag", "v2/releases/%s" % c)
            d["storage"] = storage(v["storage"], i.get("storage"))
            d["families"] = {}
            for fam, f in v["families"].items():
                path = "/%s/releases/%s" % (fam, c)
                d["families"][fam] = {
                    "path": path, "proxy": "%s-%s" % (f["proxy"], slug(c)),
                    "upstream": "http://%s-%s.%s.svc:%d/mcp" % (d["release"], f["service"], d["namespace"], f["port"]),
                    "url": "https://%s%s/mcp" % (host, path)}
            out.append(d)
        return out

    def find(self, ident):
        for d in self.okg() + self.v2():
            if d["id"] == ident:
                return d
        raise SystemExit("no instance %s (release.py show lists them)" % ident)

    def engine(self, d):
        return self.engines[d["kind"]].get(d["engine"])

    def corp(self, d):
        return self.corpus["corpora"].get(d["corpus"])


# ---------------------------------------------------------------- lint
class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


def get(d, dotted, default=None):
    for k in dotted.split("."):
        if not isinstance(d, dict) or k not in d:
            return default
        d = d[k]
    return d


def lint(mx, tags):
    r = Report()
    # corpora
    for ver, c in mx.corpus["corpora"].items():
        if c["status"] not in ("pending", "released"):
            r.err("corpus %s: status %r" % (ver, c["status"]))
        if c.get("tag") != "corpus/" + ver:
            r.err("corpus %s: tag must be corpus/%s" % (ver, ver))
        if c["status"] != "released":
            continue
        commit = str(c.get("commit") or "")
        fp, _ = fingerprint(commit, mx.paths) if commit else (None, {})
        if fp is None:
            r.err("corpus %s: commit %r not in this checkout (git fetch --tags)" % (ver, commit[:12]))
        elif fp != c["fingerprint"]:
            r.err("corpus %s: fingerprint at %s is %s, corpus.yaml says %s" % (ver, commit[:12], fp, c["fingerprint"]))
        t = tag_commit(c["tag"])
        if t and t != commit:
            r.err("corpus %s: tag %s -> %s, corpus.yaml says %s" % (ver, c["tag"], t[:12], commit[:12]))
        elif not t and tags:
            r.err("corpus %s: tag %s does not exist (docs/RELEASES.md phase 0)" % (ver, c["tag"]))
    # engines
    for kind, es in mx.engines.items():
        if kind == "version":
            continue
        for eid, e in es.items():
            if e["status"] not in ("pending", "released", "retired"):
                r.err("engine %s:%s: status %r" % (kind, eid, e["status"]))
    # instances
    insts = mx.okg() + mx.v2()
    seen = {}

    def unique(what, value, owner):
        if value in (None, ""):
            return
        if (what, value) in seen:
            r.err("%s %s used by %s and %s" % (what, value, seen[(what, value)], owner))
        seen[(what, value)] = owner

    for d in insts:
        if d["status"] not in STATUSES:
            r.err("%s: status %r" % (d["id"], d["status"]))
        e, c = mx.engine(d), mx.corp(d)
        if e is None:
            r.err("%s: engine %s not in engines.yaml" % (d["id"], d["engine"]))
        if c is None:
            r.err("%s: corpus %s not in corpus.yaml" % (d["id"], d["corpus"]))
        if d["status"] in ("building", "live"):
            if e and e["status"] == "pending":
                r.err("%s is %s but engine %s is pending" % (d["id"], d["status"], d["engine"]))
            if c and c["status"] == "pending":
                r.err("%s is %s but corpus %s is pending" % (d["id"], d["status"], d["corpus"]))
        if d.get("slot"):
            sl = str(d["slot"])
            if not d["engine"].startswith(sl + "-"):
                r.err("%s: slot %s serves engine %s; a slot's engines are named %s-<build> (e.g. %s-2026w42)"
                      % (d["id"], sl, d["engine"], sl, sl))
            if sl in mx.engines["okg"]:
                r.err("%s: slot name %s is also an engine id (their URLs would collide)" % (d["id"], sl))
            rel = sorted((str(c_.get("released")), v) for v, c_ in mx.corpus["corpora"].items() if c_["status"] == "released")
            if rel and d["corpus"] != rel[-1][1] and d["status"] != "retired":
                r.warn("%s serves corpus %s; the newest released corpus is %s (move it at the next weekly build)"
                       % (d["id"], d["corpus"], rel[-1][1]))
        if d["status"] == "retired":
            continue
        unique("argo app", d["argoApp"], d["id"])
        unique("values file", d["values"], d["id"])
        if d["kind"] == "okg":
            unique("url", d["url"], d["id"])
            unique("proxy", "%s@%s" % (d["proxy"], d["env"]), d["id"])
            unique("release", "%s@%s" % (d["release"], d["namespace"]), d["id"])
            unique("clusterIP", d.get("clusterIP"), d["id"])
            for what in ("release", "proxy", "secret"):
                if not DNS.match(d[what]):
                    r.err("%s: %s %r is not a DNS label" % (d["id"], what, d[what]))
            if len(d["release"]) > MAX_RELEASE:
                r.err("%s: release %s longer than %d" % (d["id"], d["release"], MAX_RELEASE))
        else:
            unique("release", "%s@%s" % (d["release"], d["namespace"]), d["id"])
            if not DNS.match(d["release"]) or len(d["release"]) > MAX_RELEASE:
                r.err("%s: release %r is not a DNS label of <= %d" % (d["id"], d["release"], MAX_RELEASE))
            for f in d["families"].values():
                unique("url", f["url"], d["id"])
                unique("proxy", "%s@%s" % (f["proxy"], d["env"]), d["id"])
        known = e and c and e["status"] != "pending" and c["status"] != "pending"
        if d["status"] in ("building", "live") or (known and os.path.exists(os.path.join(ROOT, d["values"]))):
            check_values(mx, d, e, c, r)
        if tags and d["status"] == "live":   # a building instance deploys a merge sha, not its tag
            t = tag_commit(d["deployTag"])
            if not t:
                r.err("%s: deploy tag %s does not exist" % (d["id"], d["deployTag"]))
            else:
                at_tag = git("show", "%s:%s" % (t, d["values"]), check=False)
                with open(os.path.join(ROOT, d["values"])) as f:
                    if at_tag is None:
                        r.err("%s: %s is not in tag %s (Argo deploys the tag)" % (d["id"], d["values"], d["deployTag"]))
                    elif at_tag.strip() != f.read().strip():
                        r.warn("%s: %s differs from tag %s -- the tag is what runs" % (d["id"], d["values"], d["deployTag"]))
    # aliases
    okg_live = {d["pair"]: d for d in mx.okg() if d["status"] == "live" and d["env"] == "staging"}
    prod = [d for d in mx.okg() if d["env"] == "prod"]
    for a in mx.m["okg"].get("aliases", []):
        tgt = str(a["target"])
        t = (prod[0] if prod else None) if tgt == "prod" else okg_live.get(tgt) or next(
            (x for x in mx.okg() if x["env"] == "staging" and x["pair"] == tgt), None)
        if t is None:
            r.err("okg alias %r -> %s: no such instance" % (a["path"] or "/mcp", tgt))
        elif a.get("status", "live") == "live" and t["status"] != "live":
            r.err("okg alias %r is live but %s is %s" % (a["path"] or "/mcp", tgt, t["status"]))
        if a["path"]:
            for x in mx.okg():
                if x["env"] == "staging" and x["path"] == a["path"]:
                    r.err("okg alias %s collides with %s" % (a["path"], x["id"]))
        unique("proxy", "%s@staging" % a["proxy"], "alias " + (a["path"] or "/"))
        unique("url", "https://%s%s/mcp" % (mx.m["hosts"]["okg"], a["path"]), "alias")
    v2_live = {d["corpus"]: d for d in mx.v2() if d["status"] == "live"}
    for a in mx.m["v2"].get("aliases", []):
        if str(a["target"]) not in v2_live:
            r.err("v2 alias %s -> %s: no live instance" % (a["family"], a["target"]))
        fam = mx.m["v2"]["families"][a["family"]]
        unique("proxy", "%s@staging" % fam["proxy"], "alias /" + a["family"])
        unique("url", "https://%s/%s/mcp" % (mx.m["hosts"]["v2"], a["family"]), "alias")
    return r


def check_values(mx, d, e, c, r):
    path = os.path.join(ROOT, d["values"])
    if not os.path.exists(path):
        r.err("%s: %s missing (release.py render %s)" % (d["id"], d["values"], d["id"]))
        return
    with open(path) as f:
        v = yaml.safe_load(f) or {}
    me = d["id"]
    if d["kind"] == "okg":
        if v.get("fullnameOverride") != d["release"]:
            r.err("%s: fullnameOverride %r != release %s" % (me, v.get("fullnameOverride"), d["release"]))
        if e and e["status"] != "pending":
            for vk, ek in (("images.okg", "runtime"), ("postgresql.image", "postgres")):
                for field in ("repository", "digest"):
                    if get(v, "%s.%s" % (vk, field)) != e[ek][field]:
                        r.err("%s: %s.%s %r != engine %s %s" % (me, vk, field, get(v, "%s.%s" % (vk, field)), d["engine"], e[ek][field]))
            if get(v, "okg.readinessProfile", "general") != e["readinessProfile"]:
                r.err("%s: okg.readinessProfile %r != engine's %r" % (me, get(v, "okg.readinessProfile", "general"), e["readinessProfile"]))
        rev, appr = get(v, "repositorySync.revision"), get(v, "bootstrap.approvedRevision")
        if rev != appr:
            r.err("%s: repositorySync.revision != bootstrap.approvedRevision" % me)
        if c and c["status"] == "released" and rev:
            fp, _ = fingerprint(rev, mx.paths)
            if fp is None:
                r.warn("%s: revision %s not in this checkout; corpus not verified" % (me, rev[:12]))
            elif fp != c["fingerprint"]:
                r.err("%s: revision %s carries corpus %s, not %s's" % (me, rev[:12], fp, d["corpus"]))
        dp = get(v, "okg.deploymentsPath") or "deployments"
        ad = (e or {}).get("adapter") or {}
        if dp not in ("deployments", ad.get("compat") or "deployments"):
            r.err("%s: okg.deploymentsPath %r is neither native nor engine %s's compat dir" % (me, dp, d["engine"]))
        elif rev and ad.get("fingerprint"):
            afp = adapter_fingerprint(rev, dp)
            if afp is None:
                r.warn("%s: no adapter at %s in revision %s (not in this checkout?)" % (me, dp, rev[:12]))
            elif afp != ad["fingerprint"]:
                r.err("%s: revision %s %s is not engine %s's adapter (%s)" % (me, rev[:12], dp, d["engine"], afp))
        if dp != "deployments":
            meta = yaml.safe_load(git("show", "%s:%s/compat.yaml" % (rev, dp), check=False) or "{}") or {}
            for sid, why in (meta.get("exclude") or {}).items():
                r.warn("%s ingests corpus %s WITHOUT %s (%s: %s)" % (me, d["corpus"], sid, dp, why))
        if get(v, "secrets.existingSecret", "okg-archi-crab") != d["secret"]:
            r.err("%s: secrets.existingSecret != %s" % (me, d["secret"]))
        ip = d.get("clusterIP") or ""
        if (get(v, "mcp.serviceClusterIP") or "") != ip:
            r.err("%s: mcp.serviceClusterIP %r != matrix %r" % (me, get(v, "mcp.serviceClusterIP"), ip))
        hosts = get(v, "mcp.allowedHosts") or []
        need = [d["host"], d["host"] + ":*"] + ([ip + ":*"] if ip else [])
        for h in need:
            if h not in hosts:
                r.err("%s: mcp.allowedHosts lacks %s" % (me, h))
        for vol, key in (("postgres", "postgresql.storage"), ("runtime", "runtime.storage")):
            want = d["storage"][vol]
            have = (get(v, key + ".size"), get(v, key + ".storageClassName"))
            if have != want:
                r.err("%s: %s %s/%s != matrix %s/%s" % (me, key, have[0], have[1], want[0], want[1]))
        frozen = bool(get(v, "frozen.enabled", False))
        if d["status"] == "live" and not frozen:
            r.err("%s: live but frozen.enabled is false" % me)
        if d["status"] in ("planned", "building") and frozen:
            r.err("%s: %s but frozen.enabled is true (it would never ingest)" % (me, d["status"]))
    else:
        if v.get("fullnameOverride", "archi-v2") != d["release"]:
            r.err("%s: fullnameOverride %r != release %s" % (me, v.get("fullnameOverride", "archi-v2"), d["release"]))
        if e:
            for k, img in e["images"].items():
                if get(v, "images.%s.digest" % k) != img["digest"]:
                    r.err("%s: images.%s.digest != engine %s" % (me, k, d["engine"]))
        for vol in ("postgres", "dataManager"):
            want = d["storage"][vol]
            have = (get(v, vol + ".storage.size"), get(v, vol + ".storage.storageClassName"))
            if have != want:
                r.err("%s: %s.storage %s/%s != matrix %s/%s" % (me, vol, have[0], have[1], want[0], want[1]))


# ---------------------------------------------------------------- render
OKG_VALUES = """\
# {values} -- GENERATED by `scripts/release.py render {id}` from releases/*.yaml.
# Edit releases/ and re-render; edit by hand only what the generator does not own (none today).
#
# okg engine {engine} x corpus {corpus}: {url}
#   engine  {eng_note}
#   corpus  {corpus} = tag corpus/{corpus}; this revision carries its fingerprint
# Built FROM SCRATCH on its own two volumes with frozen.enabled false (bootstrap ingests and
# publishes); once the first publish is verified, frozen.enabled true and the matrix says live.
# Deployed from the tag {deploy_tag}, never from main (docs/RELEASES.md).{slot_note}
fullnameOverride: {release}
okg:
  readinessProfile: "{profile}"
  deploymentsPath: {deployments_path}   # this engine's adapter in the checkout (docs/RELEASES.md, adapters)
images:
  okg:
    repository: {rt_repo}
    tag: ""
    digest: "{rt_digest}"
    pullPolicy: IfNotPresent
postgresql:
  image:
    repository: {pg_repo}
    tag: ""
    digest: "{pg_digest}"
    pullPolicy: IfNotPresent
  storage:
    size: {pg_size}
    storageClassName: {pg_class}
runtime:
  storage:
    size: {rt_size}
    storageClassName: {rt_class}   # the build checkout; the queries hit Postgres
secrets:
  existingSecret: {secret}   # scripts/okg-run-secret.sh {secret_suffix}
repositorySync:
  revision: "{revision}"
bootstrap:
  approvedRevision: "{revision}"  # MUST equal repositorySync.revision
frozen:
  enabled: false
mcp:
  serviceClusterIP: "{ip}"   # fixed (chart delta 11): check it is free before the first sync
  allowedHosts:
    - "{host}"
    - "{host}:*"
    - "{ip}:*"
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - {{key: node-role.kubernetes.io/master, operator: DoesNotExist}}
            - {{key: node-role.kubernetes.io/control-plane, operator: DoesNotExist}}
"""

V2_VALUES = """\
# {values} -- GENERATED by `scripts/release.py render {id}` from releases/*.yaml.
# archi v2 engine {engine} x corpus {corpus}: {urls}
# Release {release} in {namespace}. Deployed from the tag {deploy_tag}, never from main (docs/RELEASES.md).
fullnameOverride: {release}
images:
  dataManager: {{repository: {dm_repo}, digest: "{dm_digest}"}}
  mcp: {{repository: {mcp_repo}, digest: "{mcp_digest}"}}
  postgres: {{repository: {pg_repo}, digest: "{pg_digest}"}}
imagePullSecrets: [{{name: ghcr-mitdbg-pull}}]
secrets:
  existingSecret: {release}   # its OWN Secret (PG_PASSWORD, DM_API_TOKEN): v2/helm/archi-v2/values.yaml
postgres:
  storage: {{size: {pg_size}, storageClassName: {pg_class}}}
dataManager:
  storage: {{size: {dm_size}, storageClassName: {dm_class}}}   # raw files grep reads (page-cached once warm)
mcp:
  auth: none   # the ToolHive proxies are the gate (CERN SSO + Cedar)
"""


def render(mx, ident, revision):
    d = mx.find(ident)
    if d["status"] not in ("planned", "building"):
        raise SystemExit("%s is %s: render writes planned/building instances only" % (ident, d["status"]))
    e, c = mx.engine(d), mx.corp(d)
    if e["status"] == "pending":
        raise SystemExit("engine %s is pending: fill releases/engines.yaml first" % d["engine"])
    if c["status"] == "pending":
        raise SystemExit("corpus %s is pending: cut corpus/%s first" % (d["corpus"], d["corpus"]))
    if d["kind"] == "okg":
        rev = revision or c["commit"]
        full = git("rev-parse", "%s^{commit}" % rev)
        fp, _ = fingerprint(full, mx.paths)
        if fp != c["fingerprint"]:
            raise SystemExit("revision %s does not carry corpus %s (fingerprint %s)" % (full[:12], d["corpus"], fp))
        dp = adapter_path_for(e, full)
        if dp is None:
            raise SystemExit("revision %s carries no adapter of engine %s (native or compat): "
                             "freeze-adapter, or pick another revision" % (full[:12], d["engine"]))
        slot_note = ""
        if d.get("slot"):
            slot_note = ("\n# SLOT %s: this release, its volumes, Secret and URL stay; the engine (and, when a new one\n"
                         "# is cut, the corpus) moves every week.\n"
                         "# Each build is wiped and re-ingested from scratch (docs/RELEASES.md, weekly %s)."
                         % (d["slot"], d["slot"]))
        text = OKG_VALUES.format(deployments_path=dp, slot_note=slot_note,
            values=d["values"], id=ident, engine=d["engine"], corpus=d["corpus"], url=d["url"],
            eng_note=" ".join(str(e.get("note", "")).split())[:150], deploy_tag=d["deployTag"],
            release=d["release"], profile=e["readinessProfile"], rt_repo=e["runtime"]["repository"],
            rt_digest=e["runtime"]["digest"], pg_repo=e["postgres"]["repository"],
            pg_digest=e["postgres"]["digest"], secret=d["secret"],
            secret_suffix=d["release"][len("archi-crab-okg-"):], revision=full,
            ip=d.get("clusterIP") or "", host=d["host"],
            pg_size=d["storage"]["postgres"][0], pg_class=d["storage"]["postgres"][1],
            rt_size=d["storage"]["runtime"][0], rt_class=d["storage"]["runtime"][1])
        if not d.get("clusterIP"):
            raise SystemExit("%s: set clusterIP in matrix.yaml (chart delta 11)" % ident)
    else:
        im = e["images"]
        text = V2_VALUES.format(
            values=d["values"], id=ident, engine=d["engine"], corpus=d["corpus"],
            urls=", ".join(f["url"] for f in d["families"].values()), namespace=d["namespace"],
            deploy_tag=d["deployTag"], release=d["release"],
            pg_size=d["storage"]["postgres"][0], pg_class=d["storage"]["postgres"][1],
            dm_size=d["storage"]["dataManager"][0], dm_class=d["storage"]["dataManager"][1],
            dm_repo=im["dataManager"]["repository"],
            dm_digest=im["dataManager"]["digest"], mcp_repo=im["mcp"]["repository"],
            mcp_digest=im["mcp"]["digest"], pg_repo=im["postgres"]["repository"],
            pg_digest=im["postgres"]["digest"])
    out = os.path.join(ROOT, d["values"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(text)
    print("wrote", d["values"])


# ---------------------------------------------------------------- iac
APP = """\
# argocd/archi-crab/{envdir}/48-{app}-app.yaml  ({id})
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: {app}
  namespace: argocd
  annotations: {{argocd.argoproj.io/sync-wave: "4"}}
  finalizers: [resources-finalizer.argocd.argoproj.io]
spec:
  project: archi-crab
  source:
    repoURL: https://github.com/nausikt/archi-crab-okg.git
    targetRevision: {tag}   # building: the merge sha; live: the deploy tag. Never a branch.
    path: {chart}
    helm:
      valueFiles: [{valuefile}]
  destination: {{server: https://kubernetes.default.svc, namespace: {namespace}}}
  syncPolicy:
    automated: {{prune: true, selfHeal: true}}
    retry: {{limit: 3, backoff: {{duration: 30s, factor: 2, maxDuration: 5m}}}}
"""


def iac(mx, ident, target=None):
    d = mx.find(ident)
    chart = "helm/okg" if d["kind"] == "okg" else "v2/helm/archi-v2"
    rel = os.path.relpath(os.path.join(ROOT, d["values"]), os.path.join(ROOT, chart))
    print(APP.format(envdir="prod" if d.get("env") == "prod" else "staging", app=d["argoApp"], id=ident, tag=target or d["deployTag"], chart=chart, valuefile=rel,
                     namespace=d["namespace"]))
    prod = d.get("env") == "prod"
    print("# helm/archi-crab/mcp-gateway/%s, under remoteProxies:" % ("values.yaml" if prod else "values-staging.yaml"))
    if d["kind"] == "okg":
        print("""  - name: {proxy}            # {id}
    enabled: true
    url: http://{release}-mcp.{ns}.svc:8765/mcp
    private: true
    host: {host}{path}
    audience: {aud}
    policies: *okg-policies   # define the anchor in this file if it is not there yet""".format(
            proxy=d["proxy"], id=ident, release=d["release"], ns=d["namespace"], host=d["host"],
            path=("\n    path: " + d["path"]) if d["path"] else "",
            aud="archi-crab-okg-public" if prod else "archi-crab-okg-public-staging"))
    else:
        for fam, f in d["families"].items():
            print("""  - name: {proxy}            # {id} {fam}
    enabled: true
    url: {up}
    private: true
    host: {host}
    path: {path}
    audience: archi-crab-okg-public-staging
    policies: *v2-policies""".format(proxy=f["proxy"], id=ident, fam=fam, up=f["upstream"],
                                     host=d["host"], path=f["path"]))


# ---------------------------------------------------------------- show / budget
def show(mx):
    rows = []
    for d in mx.okg():
        rows.append((d["url"], d["id"], d["status"], "%s @ %s" % (d["release"], d["namespace"])))
    for a in mx.m["okg"].get("aliases", []):
        tgt = "prod (archi-crab-okg @ archi-crab)" if str(a["target"]) == "prod" else "okg:" + str(a["target"])
        rows.append(("https://%s%s/mcp" % (mx.m["hosts"]["okg"], a["path"]), "-> " + tgt,
                     "alias/" + a.get("status", "live"), "proxy " + a["proxy"]))
    for d in mx.v2():
        for f in d["families"].values():
            rows.append((f["url"], d["id"], d["status"], d["release"]))
    for a in mx.m["v2"].get("aliases", []):
        rows.append(("https://%s/%s/mcp" % (mx.m["hosts"]["v2"], a["family"]), "-> v2:" + str(a["target"]),
                     "alias", "proxy " + mx.m["v2"]["families"][a["family"]]["proxy"]))
    w = [max(len(r[i]) for r in rows) for i in range(4)]
    for r in rows:
        print("  ".join(c.ljust(w[i]) for i, c in enumerate(r)).rstrip())


CINDER_TYPE = {"cinder-io1": "io1", "cinder-io1-delete": "io1", "cinder-standard": "standard"}


def budget(mx):
    """Cinder volumes per type: what exists (live/building) and what the planned instances add."""
    def tally(insts):
        t = {}
        for d in insts:
            for size, cls in d["storage"].values():
                k = CINDER_TYPE.get(cls, cls)
                n, g = t.get(k, (0, 0))
                t[k] = (n + 1, g + int(str(size).rstrip("Gi")))
        return t

    def fmt(t):
        return "  ".join("%s %d vol / %d GiB" % (k, n, g) for k, (n, g) in sorted(t.items())) or "-"
    insts = mx.okg() + mx.v2()
    for st in STATUSES:
        ids = [d["id"] for d in insts if d["status"] == st]
        if ids:
            print("%-9s %d  %s" % (st, len(ids), ", ".join(ids)))
    print("%-22s %s" % ("exists (live/building)", fmt(tally([d for d in insts if d["status"] in ("live", "building")]))))
    print("%-22s %s" % ("planned adds", fmt(tally([d for d in insts if d["status"] == "planned"]))))
    print("%-22s %s" % ("matrix total", fmt(tally([d for d in insts if d["status"] != "retired"]))))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("show")
    sub.add_parser("budget")
    p = sub.add_parser("adapter")
    p.add_argument("engine")
    p.add_argument("rev", nargs="?", default="HEAD")
    p = sub.add_parser("freeze-adapter")
    p.add_argument("engine")
    p.add_argument("commit")
    p = sub.add_parser("engine-entry")
    p.add_argument("engine")
    p.add_argument("commit")
    p = sub.add_parser("lint")
    p.add_argument("--tags", action="store_true", help="also require the corpus and deploy tags")
    p = sub.add_parser("fingerprint")
    p.add_argument("rev", nargs="?", default="HEAD")
    p = sub.add_parser("render")
    p.add_argument("id")
    p.add_argument("--revision", help="okg: knowledge revision (default: the corpus tag's commit)")
    p = sub.add_parser("iac")
    p.add_argument("id")
    p.add_argument("--target", help="Argo targetRevision while building (a merge sha); default: the deploy tag")
    a = ap.parse_args()
    mx = Matrix()
    if a.cmd == "show":
        show(mx)
    elif a.cmd == "adapter":
        e = mx.engines["okg"].get(a.engine) or {}
        ad = e.get("adapter") or {}
        for path in ("deployments", ad.get("compat") or ""):
            if path:
                print("%-34s %s" % (path, adapter_fingerprint(a.rev, path)))
        print("%-34s %s" % ("engines.yaml says", ad.get("fingerprint")))
        print("-> %s" % (adapter_path_for(e, a.rev) or "none at %s" % a.rev))
    elif a.cmd == "freeze-adapter":
        freeze_adapter(mx, a.engine, a.commit)
    elif a.cmd == "engine-entry":
        engine_entry(a.engine, a.commit)
    elif a.cmd == "budget":
        budget(mx)
    elif a.cmd == "fingerprint":
        fp, objs = fingerprint(a.rev, mx.paths)
        if fp is None:
            raise SystemExit("unknown revision %s" % a.rev)
        print(fp)
        for p_, o in objs.items():
            print("  %s %s" % (o, p_))
    elif a.cmd == "render":
        render(mx, a.id, a.revision)
    elif a.cmd == "iac":
        iac(mx, a.id, a.target)
    elif a.cmd == "lint":
        r = lint(mx, a.tags)
        for w in r.warnings:
            print("WARN ", w)
        for e in r.errors:
            print("ERROR", e)
        print("release lint: %d error(s), %d warning(s)" % (len(r.errors), len(r.warnings)))
        sys.exit(1 if r.errors else 0)


if __name__ == "__main__":
    main()
