#!/usr/bin/env python3
"""What v2/ borrows from archi, checked against the archi the image was built from.

The MCP layer (v2/mcp/server.py) reimplements nothing: it calls archi's tool factories and
copies the agent's tool descriptions. The chart mounts files archi's data-manager reads. Each
of those is a contract with upstream, and archi `main` moves daily. This check names what
moved, so the engine PR (v2-engine.yaml) carries the finding instead of a broken fixture.

    python3 v2/scripts/contract-check.py [--archi /root/archi] [--markdown out.md]

Sections (any ERROR -> exit 1):
  descriptions   the five tool descriptions in CMSCompOpsAgent._tool_definitions == ours
  factories      the factory signatures/defaults the v2 agent relies on (max_results 3/5,
                 max_documents 4, max_chars 800, fetch 4000; HybridRetriever(k, weights))
  catalog-api    the three /api/catalog routes the grep family calls, still registered
  config         the config keys we set exist in base-config.yaml; weblist `git-` prefix parsed
  runtime        (inside the image only) the imports server.py makes resolve
Standard library + PyYAML. No network, no database.
"""
from __future__ import annotations

import argparse
import ast
import inspect
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
REPO = HERE.parents[2]
# Two layouts: the repository (v2/scripts/ next to v2/mcp/server.py) and the mcp image, where
# the Dockerfile copies server.py and this script side by side into /root/archi/v2mcp/.
IN_IMAGE = (HERE.parent / "server.py").is_file()
SERVER_PY = HERE.parent / "server.py" if IN_IMAGE else REPO / "v2" / "mcp" / "server.py"


class Findings:
    def __init__(self):
        self.rows = []

    def add(self, sev, section, msg):
        self.rows.append((sev, section, msg))
        print("%s [%s] %s" % (sev, section, msg), file=sys.stderr if sev == "ERROR" else sys.stdout)

    def error(self, section, msg):
        self.add("ERROR", section, msg)

    def warn(self, section, msg):
        self.add("WARNING", section, msg)

    def ok(self, section, msg):
        self.add("ok", section, msg)

    @property
    def failed(self):
        return any(r[0] == "ERROR" for r in self.rows)

    def markdown(self, archi_root, commit):
        out = ["## v2 contract check (archi %s)" % (commit or archi_root), "", "| | section | finding |", "|---|---|---|"]
        for sev, sec, msg in self.rows:
            out.append("| %s | %s | %s |" % ({"ERROR": "❌", "WARNING": "⚠️"}.get(sev, "✅"), sec, msg.replace("|", "\\|")))
        return "\n".join(out) + "\n"


def our_descriptions():
    """DESCRIPTIONS from v2/mcp/server.py, without importing it (no mcp package needed)."""
    tree = ast.parse(SERVER_PY.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "DESCRIPTIONS" for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit("%s: no DESCRIPTIONS dict" % SERVER_PY)


def agent_descriptions(agent_py: Path):
    """The description strings in CMSCompOpsAgent._tool_definitions, by tool name."""
    tree = ast.parse(agent_py.read_text(encoding="utf-8"))
    found = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "_tool_definitions":
            for sub in ast.walk(node):
                if isinstance(sub, ast.Dict):
                    for k, v in zip(sub.keys, sub.values):
                        if isinstance(k, ast.Constant) and isinstance(v, ast.Dict):
                            for kk, vv in zip(v.keys, v.values):
                                if isinstance(kk, ast.Constant) and kk.value == "description":
                                    try:
                                        found[k.value] = ast.literal_eval(vv)
                                    except ValueError:
                                        found[k.value] = None
    return found


def check_descriptions(archi, f):
    agent_py = archi / "src" / "archi" / "pipelines" / "agents" / "cms_comp_ops_agent.py"
    if not agent_py.is_file():
        f.error("descriptions", "%s missing: the v2 agent moved or was deleted (ADR 0001 W10?)" % agent_py)
        return
    theirs, ours = agent_descriptions(agent_py), our_descriptions()
    for name, text in ours.items():
        if name not in theirs:
            f.error("descriptions", "%s: no longer defined by CMSCompOpsAgent._tool_definitions" % name)
        elif theirs[name] is None:
            f.warn("descriptions", "%s: description is no longer a literal; compare by hand" % name)
        elif theirs[name] != text:
            f.error("descriptions", "%s: the agent's description changed; copy it into v2/mcp/server.py DESCRIPTIONS" % name)
        else:
            f.ok("descriptions", "%s: identical" % name)


def sig_defaults(fn):
    return {k: p.default for k, p in inspect.signature(fn).parameters.items() if p.default is not inspect._empty}


def check_factories(archi, f):
    sys.path.insert(0, str(archi))
    try:
        from src.archi.pipelines.agents.tools import local_files, retriever  # noqa
    except Exception as exc:  # the image is the only place these imports are guaranteed
        if IN_IMAGE:
            f.error("factories", "archi's tool modules do not import in the image: %s: %s" % (type(exc).__name__, exc))
            return
        f.warn("factories", "cannot import archi's tool modules here (%s: %s); run inside the image" % (type(exc).__name__, exc))
        return
    want = {
        (local_files.create_file_search_tool, "max_results"): 3,
        (local_files.create_metadata_search_tool, "max_results"): 5,
        (local_files.create_document_fetch_tool, "default_max_chars"): 4000,
        (retriever.create_retriever_tool, "max_documents"): 4,
        (retriever.create_retriever_tool, "max_chars"): 800,
    }
    for (fn, param), value in want.items():
        got = sig_defaults(fn).get(param, "<absent>")
        if got != value:
            f.error("factories", "%s(%s=%r): the v2 agent's default was %r; the MCP tools now behave differently" % (fn.__name__, param, got, value))
        else:
            f.ok("factories", "%s(%s=%r)" % (fn.__name__, param, value))
    for fn in (local_files.create_file_search_tool, local_files.create_metadata_search_tool,
               local_files.create_metadata_schema_tool, local_files.create_document_fetch_tool, retriever.create_retriever_tool):
        params = inspect.signature(fn).parameters
        if "description" not in params:
            f.error("factories", "%s: no `description` parameter" % fn.__name__)
    for meth in ("search", "get_document", "schema"):
        if not hasattr(local_files.RemoteCatalogClient, meth):
            f.error("factories", "RemoteCatalogClient.%s is gone" % meth)
    try:
        from src.data_manager.vectorstore.retrievers import HybridRetriever
        params = inspect.signature(HybridRetriever.__init__).parameters
        for p in ("vectorstore", "k", "bm25_weight", "semantic_weight"):
            if p not in params:
                f.error("factories", "HybridRetriever.__init__ lost `%s`" % p)
        from src.archi.utils.vectorstore_connector import VectorstoreConnector  # noqa
        from src.utils.config_access import get_full_config  # noqa
        from src.utils.postgres_service_factory import PostgresServiceFactory
        if not hasattr(PostgresServiceFactory, "from_env"):
            f.error("factories", "PostgresServiceFactory.from_env is gone (server.py builds config from it)")
    except Exception as exc:
        f.error("factories", "vector-side imports: %s: %s" % (type(exc).__name__, exc))


def server_imports():
    """(module, [names]) for every `from X import …` in server.py, at any depth (the archi
    imports are inside functions, so a top-level-only scan would miss them)."""
    tree = ast.parse(SERVER_PY.read_text(encoding="utf-8"))
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module and node.level == 0 and node.module != "__future__":
            out.append((node.module, [a.name for a in node.names]))
        elif isinstance(node, ast.Import):
            out.extend((a.name, []) for a in node.names)
    return out


def check_runtime(archi, f):
    """Inside the image only: every import server.py makes resolves, names included."""
    if not IN_IMAGE:
        f.ok("runtime", "skipped outside the image (v2-smoke runs it in v2-mcp)")
        return
    import importlib
    if str(archi) not in sys.path:
        sys.path.insert(0, str(archi))
    bad = 0
    for mod, names in server_imports():
        try:
            m = importlib.import_module(mod)
            missing = [n for n in names if not hasattr(m, n)]
            if missing:
                bad += 1
                f.error("runtime", "%s no longer provides %s" % (mod, ", ".join(missing)))
        except Exception as exc:
            bad += 1
            f.error("runtime", "import %s: %s: %s" % (mod, type(exc).__name__, exc))
    if not bad:
        f.ok("runtime", "%d imports of server.py resolve" % len(server_imports()))


def check_catalog_api(archi, f):
    app_py = archi / "src" / "interfaces" / "uploader_app" / "app.py"
    text = app_py.read_text(encoding="utf-8") if app_py.is_file() else ""
    for route in ("/api/catalog/search", "/api/catalog/document/<path:resource_hash>", "/api/catalog/schema"):
        if route not in text:
            f.error("catalog-api", "%s not registered in %s" % (route, app_py.relative_to(archi)))
        else:
            f.ok("catalog-api", route)
    if 'read_secret("DM_API_TOKEN")' not in text:
        f.warn("catalog-api", "DM_API_TOKEN no longer read by the uploader app: bearer gating of the catalog API changed")


def check_config(archi, f):
    tmpl = archi / "src" / "cli" / "templates" / "base-config.yaml"
    text = tmpl.read_text(encoding="utf-8") if tmpl.is_file() else ""
    for key in ("collection_name", "data_manager.embedding_name", "data_manager.embedding_class_map",
                "data_manager.chunk_size", "data_manager.retrievers.hybrid_retriever.num_documents_to_retrieve",
                "data_manager.retrievers.hybrid_retriever.bm25_weight", "data_manager.sources.links.base_source_depth",
                "data_manager.sources.links.input_lists", "data_manager.sources.git.enabled", "services.data_manager.port"):
        if key not in text:
            f.error("config", "base-config.yaml no longer reads `%s`" % key)
    if "reset_collection | default(true, true)" in text:
        f.ok("config", "reset_collection still needs the v2_overrides workaround (template default(true, true))")
    elif "reset_collection" in text:
        f.warn("config", "reset_collection template changed: the v2_overrides entry may be unnecessary now")
    sm = archi / "src" / "data_manager" / "collectors" / "scrapers" / "scraper_manager.py"
    smt = sm.read_text(encoding="utf-8") if sm.is_file() else ""
    if 'startswith("git-")' not in smt:
        f.error("config", "weblist `git-` prefix no longer parsed by scraper_manager.py: the generated list breaks")
    else:
        f.ok("config", "weblist `git-` prefix parsed")
    dm = archi / "src" / "bin" / "service_data_manager.py"
    if not dm.is_file():
        f.error("config", "src/bin/service_data_manager.py is gone: the image CMD breaks")
    for rel in ("src/cli/templates/init.sql", "src/cli/tools/config_seed.py"):
        if not (archi / rel).is_file():
            f.error("config", "%s is gone (the chart's config-seed Job / schema depend on it)" % rel)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archi", default=os.environ.get("ARCHI_ROOT", "/root/archi"))
    ap.add_argument("--commit", default=os.environ.get("ARCHI_COMMIT", ""))
    ap.add_argument("--markdown")
    a = ap.parse_args()
    archi = Path(a.archi)
    f = Findings()
    if not (archi / "src").is_dir():
        f.error("runtime", "no archi source tree at %s" % archi)
    else:
        check_descriptions(archi, f)
        check_factories(archi, f)
        check_catalog_api(archi, f)
        check_config(archi, f)
        check_runtime(archi, f)
    if a.markdown:
        Path(a.markdown).write_text(f.markdown(archi, a.commit), encoding="utf-8")
    print("v2 contract: %s" % ("FAIL" if f.failed else "ok"))
    return 1 if f.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
