#!/usr/bin/env python3
"""archi v2 retrieval tools over MCP -- the thin layer (docs/V2-BENCH.md, ADR-V2-3/4).

One process = one tool family, chosen by V2_MCP_FAMILY:

  grep    search_local_files, search_metadata_index, list_metadata_schema
          (+ fetch_catalog_document unless V2_MCP_FETCH=0)
          HTTP to the data-manager's catalog API. Needs DM_BASE_URL + DM_API_TOKEN only.
  vector  search_vectorstore_hybrid (+ fetch_catalog_document unless V2_MCP_FETCH=0)
          archi's HybridRetriever in-process: the embedding model + a pgvector/pg_textsearch
          query, exactly as the v2 agent runs it. Needs the Postgres env the data-manager
          has (PGHOST/PGPORT/PGDATABASE/PGUSER + PG_PASSWORD) and the embedding provider's
          secret, because archi keeps its config in Postgres and embeds the query locally.

Nothing here reimplements a tool. Each tool is the LangChain StructuredTool archi's own
factories build (src/archi/pipelines/agents/tools/*) -- same name, same argument schema,
same defaults, same output string the v2 agent sees -- exposed as an MCP tool by
introspection. The descriptions are the ones CMSCompOpsAgent._tool_definitions() gives
them; v2/scripts/contract-check.py fails the engine PR when archi changes either.

Transport: MCP streamable-http at /mcp (stateless, JSON responses), /healthz for probes.
Auth: a static bearer token (V2_MCP_AUTH_TOKEN), the same posture as okg's MCP server.
"""
from __future__ import annotations

import logging
import os
import sys
from typing import Any

import anyio
import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Mount, Route

log = logging.getLogger("v2mcp")

# The descriptions the v2 agent gives these tools (CMSCompOpsAgent._tool_definitions,
# src/archi/pipelines/agents/cms_comp_ops_agent.py). Copied verbatim so the model reads
# the same text over MCP as it did in LangChain; contract-check.py asserts they still match.
DESCRIPTIONS = {
    "search_local_files": (
        "Grep-like search over file contents. Provide a distinctive phrase or regex; optionally use "
        "regex=true, case_sensitive=true, and context (before/after). Returns matching lines with hashes; "
        "use fetch_catalog_document for full text."
    ),
    "search_metadata_index": (
        "Query the files' metadata catalog (ticket IDs, source URLs, resource types, etc.). "
        "Supports key:value filters and OR (e.g., source_type:git OR url:https://... ticket_id:CMS-123). "
        "Returns matching files with metadata; use fetch_catalog_document to pull full text."
    ),
    "list_metadata_schema": (
        "List metadata schema hints: supported keys, distinct source_type values, and suffixes. "
        "Use this to learn which key:value filters are available before searching."
    ),
    "fetch_catalog_document": (
        "Fetch full document text by resource hash after a search hit. "
        "Use this sparingly to pull only the most relevant files."
    ),
    "search_vectorstore_hybrid": (
        "Hybrid search over the knowledge base that combines lexical (BM25) and semantic (vector) matching.\n"
        "Input must be a plain text query string.\n"
        "Query writing guidance:\n"
        "- Use one short, specific question or request (not a long keyword dump).\n"
        "- Keep only the most informative terms (about 3-8 keywords or a short sentence).\n"
        "- Do not repeat terms unless repetition is intentional for emphasis.\n"
        "- Avoid partial/trailing fragments (e.g., ending with a single character).\n"
        "- Include exact identifiers when known (component names, APIs, error strings), using quotes for multi-word phrases.\n"
        "- If results are weak, run a second query that is narrower (add identifiers) or broader (remove overly specific terms)."
    ),
}

FAMILIES = {
    "grep": ["search_local_files", "search_metadata_index", "list_metadata_schema"],
    "vector": ["search_vectorstore_hybrid"],
}


def env_flag(name: str, default: bool) -> bool:
    v = os.environ.get(name)
    if v is None or v == "":
        return default
    return v.strip().lower() in {"1", "true", "yes", "on"}


# --------------------------------------------------------------------------- tools ----
def build_catalog_client():
    from src.archi.pipelines.agents.tools.local_files import RemoteCatalogClient
    from src.utils.env import read_secret

    base_url = os.environ.get("DM_BASE_URL") or "http://127.0.0.1:7871"
    token = read_secret("DM_API_TOKEN") or None
    if not token:
        log.warning("DM_API_TOKEN is empty: the data-manager will answer 401 unless its API is unprotected")
    return RemoteCatalogClient(base_url=base_url, api_token=token)


def build_grep_tools(catalog) -> list:
    """The three catalog tools, with the SAME defaults the v2 agent uses (it passes only
    a description, so max_results=3 for grep and 5 for metadata come from the factories)."""
    from src.archi.pipelines.agents.tools.local_files import (
        create_file_search_tool,
        create_metadata_schema_tool,
        create_metadata_search_tool,
    )

    return [
        create_file_search_tool(catalog, description=DESCRIPTIONS["search_local_files"]),
        create_metadata_search_tool(catalog, description=DESCRIPTIONS["search_metadata_index"]),
        create_metadata_schema_tool(catalog, description=DESCRIPTIONS["list_metadata_schema"]),
    ]


def build_fetch_tool(catalog):
    from src.archi.pipelines.agents.tools.local_files import create_document_fetch_tool

    return create_document_fetch_tool(catalog, description=DESCRIPTIONS["fetch_catalog_document"])


def build_vector_tool():
    """archi's hybrid retriever as the v2 agent builds it (CMSCompOpsAgent._update_vector_retrievers):
    k and the weights from data_manager.retrievers.hybrid_retriever, max_documents=4 /
    max_chars=800 from create_retriever_tool's defaults. Config comes from Postgres, where
    archi keeps it (config-seed), so this needs the data-manager's PG env."""
    from src.archi.pipelines.agents.tools.retriever import create_retriever_tool
    from src.archi.utils.vectorstore_connector import VectorstoreConnector
    from src.data_manager.vectorstore.retrievers import HybridRetriever
    from src.utils.config_access import get_full_config
    from src.utils.env import read_secret
    from src.utils.postgres_service_factory import PostgresServiceFactory

    for key in ("OPENAI_API_KEY", "HUGGING_FACE_HUB_TOKEN"):  # how service_data_manager exposes them
        val = read_secret(key)
        if val:
            os.environ[key] = val
    factory = PostgresServiceFactory.from_env(password_override=read_secret("PG_PASSWORD"))
    PostgresServiceFactory.set_instance(factory)
    config = get_full_config()
    hybrid_cfg = (config.get("data_manager", {}).get("retrievers", {}) or {}).get("hybrid_retriever", {}) or {}
    vectorstore = VectorstoreConnector(config).get_vectorstore()  # instantiates the embedding model
    retriever = HybridRetriever(
        vectorstore=vectorstore,
        k=hybrid_cfg.get("num_documents_to_retrieve", 5),
        bm25_weight=hybrid_cfg.get("bm25_weight", 0.6),
        semantic_weight=hybrid_cfg.get("semantic_weight", 0.4),
    )
    log.info(
        "vector tool: collection=%s k=%s bm25=%s semantic=%s",
        getattr(vectorstore, "collection_name", "?"), retriever.k, retriever.bm25_weight, retriever.semantic_weight,
    )
    return create_retriever_tool(
        retriever, name="search_vectorstore_hybrid", description=DESCRIPTIONS["search_vectorstore_hybrid"]
    )


def build_tools() -> list:
    family = (os.environ.get("V2_MCP_FAMILY") or "grep").strip().lower()
    if family not in FAMILIES:
        raise SystemExit("V2_MCP_FAMILY must be one of %s (got %r)" % (sorted(FAMILIES), family))
    wanted = [t.strip() for t in (os.environ.get("V2_MCP_TOOLS") or "").split(",") if t.strip()] or FAMILIES[family]
    with_fetch = env_flag("V2_MCP_FETCH", True)  # fetch is the second half of BOTH workflows
    tools = []
    catalog = None
    if any(t in FAMILIES["grep"] for t in wanted) or with_fetch:
        catalog = build_catalog_client()
    if any(t in FAMILIES["grep"] for t in wanted):
        tools += [t for t in build_grep_tools(catalog) if t.name in wanted]
    if "search_vectorstore_hybrid" in wanted:
        tools.append(build_vector_tool())
    if with_fetch:
        tools.append(build_fetch_tool(catalog))
    unknown = set(wanted) - set(DESCRIPTIONS)
    if unknown:
        raise SystemExit("V2_MCP_TOOLS names unknown tools: %s" % sorted(unknown))
    return tools


# ------------------------------------------------------------------- the bridge ----
def input_schema(tool) -> dict:
    schema = tool.args_schema.model_json_schema() if getattr(tool, "args_schema", None) else {}
    schema = {k: v for k, v in schema.items() if k not in ("title",)}
    schema.setdefault("type", "object")
    schema.setdefault("properties", {})
    for prop in schema["properties"].values():
        prop.pop("title", None)
    return schema


def make_server(tools: list) -> Server:
    by_name = {t.name: t for t in tools}
    # version = the archi commit the image was built from (v2/versions.lock), so a client sees which v2 it talks to
    server = Server("archi-v2-" + (os.environ.get("V2_MCP_FAMILY") or "grep"), version=os.environ.get("ARCHI_COMMIT") or None)

    @server.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [types.Tool(name=t.name, description=t.description, inputSchema=input_schema(t)) for t in tools]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any] | None):
        tool = by_name.get(name)
        if tool is None:
            raise ValueError("unknown tool %r" % name)
        # archi's tools are synchronous (requests / psycopg2): keep the event loop free
        text = await anyio.to_thread.run_sync(lambda: tool.invoke(arguments or {}))
        return [types.TextContent(type="text", text=str(text))]

    return server


class BearerAuth(BaseHTTPMiddleware):
    def __init__(self, app, token: str | None):
        super().__init__(app)
        self.token = token

    async def dispatch(self, request: Request, call_next):
        if request.url.path == "/healthz" or not self.token:
            return await call_next(request)
        auth = request.headers.get("authorization", "")
        if auth != "Bearer " + self.token:
            return JSONResponse({"error": "unauthorized"}, status_code=401, headers={"WWW-Authenticate": "Bearer"})
        return await call_next(request)


def make_app(tools: list) -> Starlette:
    from src.utils.env import read_secret

    token = read_secret("V2_MCP_AUTH_TOKEN") or None
    if not token and not env_flag("V2_MCP_ALLOW_ANONYMOUS", False):
        raise SystemExit("V2_MCP_AUTH_TOKEN is empty; set it, or V2_MCP_ALLOW_ANONYMOUS=1 for a local test")
    server = make_server(tools)
    try:  # mcp >= 1.10: DNS-rebinding protection is host-based; the bearer token is our gate
        from mcp.server.transport_security import TransportSecuritySettings

        security = TransportSecuritySettings(enable_dns_rebinding_protection=False)
    except ImportError:  # older SDKs have no such setting
        security = None
    kwargs = {"json_response": True, "stateless": True}
    if security is not None:
        kwargs["security_settings"] = security
    manager = StreamableHTTPSessionManager(app=server, **kwargs)

    async def handle_mcp(scope, receive, send):
        await manager.handle_request(scope, receive, send)

    async def healthz(_: Request):
        return PlainTextResponse("ok")

    async def lifespan(_: Starlette):
        async with manager.run():
            log.info("archi v2 MCP (%s) serving %s", os.environ.get("V2_MCP_FAMILY", "grep"), [t.name for t in tools])
            yield

    return Starlette(
        routes=[Route("/healthz", healthz), Mount("/mcp", app=handle_mcp)],
        middleware=[Middleware(BearerAuth, token=token)],
        lifespan=lifespan,
    )


def main() -> int:
    logging.basicConfig(level=os.environ.get("V2_MCP_LOG_LEVEL", "INFO"), format="%(asctime)s %(name)s %(levelname)s %(message)s")
    sys.path.insert(0, os.environ.get("ARCHI_ROOT", "/root/archi"))  # `src.` imports, as archi's own services do
    tools = build_tools()
    app = make_app(tools)
    import uvicorn

    uvicorn.run(app, host=os.environ.get("V2_MCP_HOST", "0.0.0.0"), port=int(os.environ.get("V2_MCP_PORT", "8081")), log_level="info")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
