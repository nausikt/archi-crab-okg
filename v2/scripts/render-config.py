#!/usr/bin/env python3
"""Render archi v2's runtime files from OUR short config, with archi's OWN templates.

    v2/deployments/archi-crab/config.yaml   (what we choose: embeddings, chunking, sources)
            |  this script, through archi's base-config.yaml + init.sql Jinja templates
            v
    v2/helm/archi-v2/files/config.yaml      the full config the config-seed Job loads into Postgres
    v2/helm/archi-v2/files/init.sql         the schema (vector dimension follows the embedding)

Same code path as `archi install` (src/cli/managers/templates_manager.py: _render_config_files
and _stage_postgres_init), so a field archi adds or renames arrives on the engine PR as a diff
of these two generated files. Run it inside the pinned image (CI) or with --archi <checkout>.

    python3 v2/scripts/render-config.py --write          # regenerate
    python3 v2/scripts/render-config.py --check          # CI: generated files == render
"""
from __future__ import annotations

import argparse
import copy
import os
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve()
REPO = HERE.parents[2]
FILES = REPO / "v2" / "helm" / "archi-v2" / "files"

# templates_manager._stage_postgres_init: keyed by embedding_name, which is the CLASS name
# (OpenAIEmbeddings / HuggingFaceEmbeddings), so these only ever match when someone names
# an embedding after its model. Set `dimensions:` on the embedding_class_map entry instead.
DEFAULT_DIMENSIONS = {
    "all-MiniLM-L6-v2": 384,
    "text-embedding-ada-002": 1536,
    "text-embedding-3-small": 1536,
    "text-embedding-3-large": 3072,
}
KNOWN_MODEL_DIMENSIONS = {  # our lint, not archi's: catch a schema/embedding mismatch before the e2e
    "sentence-transformers/all-MiniLM-L6-v2": 384,
    "BAAI/bge-small-en-v1.5": 384,
    "BAAI/bge-base-en-v1.5": 768,
    "text-embedding-3-small": 1536,
    "text-embedding-3-large": 3072,
    "text-embedding-ada-002": 1536,
}


def jinja_env(archi_root: Path):
    from jinja2 import ChainableUndefined, Environment, FileSystemLoader, select_autoescape

    templates = archi_root / "src" / "cli" / "templates"
    if not (templates / "base-config.yaml").is_file():
        raise SystemExit("no archi templates at %s (pass --archi <checkout>, or run inside the image)" % templates)
    return Environment(loader=FileSystemLoader(str(templates)), autoescape=select_autoescape(), undefined=ChainableUndefined)


def embedding_dimensions(dm_cfg: dict) -> tuple[int, str | None]:
    """archi's rule, verbatim (templates_manager.py), plus a warning when it is likely wrong."""
    class_map = dm_cfg.get("embedding_class_map", {}) or {}
    name = dm_cfg.get("embedding_name", "all-MiniLM-L6-v2")
    dims = DEFAULT_DIMENSIONS.get(name, 384)
    if name in class_map:
        dims = (class_map[name] or {}).get("dimensions", dims)
    warn = None
    kwargs = ((class_map.get(name) or {}).get("kwargs") or {})
    model = kwargs.get("model") or kwargs.get("model_name")
    known = KNOWN_MODEL_DIMENSIONS.get(str(model))
    if known and known != dims:
        warn = ("embedding %s (%s) has %d dimensions but init.sql will declare vector(%d): set "
                "data_manager.embedding_class_map.%s.dimensions: %d" % (name, model, known, dims, name, known))
    return int(dims), warn


def apply_overrides(config_yaml: str, overrides: dict) -> str:
    """Set dotted keys on the rendered config (fields archi's template cannot express). The
    result is re-dumped by PyYAML, so the file loses archi's comments but keeps every value."""
    data = yaml.safe_load(config_yaml)
    for dotted, value in overrides.items():
        node = data
        parts = str(dotted).split(".")
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = value
    note = "# v2_overrides applied after archi's template: %s\n" % ", ".join("%s=%r" % kv for kv in overrides.items())
    return note + yaml.safe_dump(data, sort_keys=False, width=4096, allow_unicode=True)


def render(user_cfg_path: Path, archi_root: Path, postgres_host: str, verbosity: int) -> dict[str, str]:
    env = jinja_env(archi_root)
    user_cfg = yaml.safe_load(user_cfg_path.read_text(encoding="utf-8")) or {}
    cfg = copy.deepcopy(user_cfg)
    cfg.setdefault("utils", {}).setdefault("postgres", {})["host"] = postgres_host  # as the helm path does
    cfg.setdefault("host_mode", False)
    overrides = cfg.pop("v2_overrides", None) or {}
    config_yaml = env.get_template("base-config.yaml").render(verbosity=verbosity, **cfg)
    if overrides:
        config_yaml = apply_overrides(config_yaml, overrides)
    dm_cfg = user_cfg.get("data_manager", {}) or {}
    dims, warn = embedding_dimensions(dm_cfg)
    if warn:
        print("WARNING: " + warn, file=sys.stderr)
    init_sql = env.get_template("init.sql").render(
        use_grafana=False,
        grafana_pg_password="",
        embedding_dimensions=dims,
        vector_index_type=dm_cfg.get("vector_index_type", "hnsw"),
        vector_index_hnsw_m=dm_cfg.get("vector_index_hnsw_m", 16),
        vector_index_hnsw_ef=dm_cfg.get("vector_index_hnsw_ef", 64),
    )
    head = "# GENERATED by v2/scripts/render-config.py from %s with archi's templates -- do not edit.\n" % (
        user_cfg_path.relative_to(REPO).as_posix())
    yaml.safe_load(config_yaml)  # must stay valid YAML
    return {"config.yaml": head + config_yaml.rstrip("\n") + "\n",
            "init.sql": "-- " + head[2:] + init_sql.rstrip("\n") + "\n"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(REPO / "v2" / "deployments" / "archi-crab" / "config.yaml"))
    ap.add_argument("--archi", default=os.environ.get("ARCHI_ROOT", "/root/archi"), help="archi checkout or install root")
    ap.add_argument("--postgres-host", default="archi-v2-postgres", help="the chart's Postgres Service name")
    ap.add_argument("--verbosity", type=int, default=3)
    ap.add_argument("--out", default=str(FILES))
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    a = ap.parse_args()
    out = Path(a.out)
    rendered = render(Path(a.config), Path(a.archi), a.postgres_host, a.verbosity)
    rc = 0
    for name, text in rendered.items():
        path = out / name
        if a.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            print("wrote %s" % path.relative_to(REPO).as_posix())
        else:
            current = path.read_text(encoding="utf-8") if path.exists() else None
            if current != text:
                print("%s differs from the render -- run: python3 v2/scripts/render-config.py --write" % path.relative_to(REPO).as_posix(), file=sys.stderr)
                rc = 1
    if a.check and rc == 0:
        print("render-config: ok (%s)" % ", ".join(rendered))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
