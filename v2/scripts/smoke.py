#!/usr/bin/env python3
"""Smoke an archi v2 MCP endpoint the way a client does: initialize, tools/list, one call.

    python3 v2/scripts/smoke.py http://127.0.0.1:8081/mcp --token "$V2_MCP_AUTH_TOKEN" \
        --expect search_local_files,search_metadata_index,list_metadata_schema,fetch_catalog_document \
        --call list_metadata_schema '{}' --call search_local_files '{"query": "crab"}'

Exit 1 when the handshake fails, a tool from --expect is missing (or an unexpected one is
served: server-side gating is what the benchmark relies on), or a --call errors.
Needs only the `mcp` package (pip install "mcp>=1.12,<2").
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def run(args) -> int:
    headers = {"Authorization": "Bearer " + args.token} if args.token else {}
    rc = 0
    async with streamablehttp_client(args.url, headers=headers) as (read, write, _):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            print("server: %s %s" % (init.serverInfo.name, init.serverInfo.version))
            listed = await session.list_tools()
            names = sorted(t.name for t in listed.tools)
            print("tools: %s" % ", ".join(names))
            if args.expect:
                want = sorted(x.strip() for x in args.expect.split(",") if x.strip())
                if names != want:
                    print("FAIL: tools/list %s != expected %s" % (names, want), file=sys.stderr)
                    rc = 1
            for name, raw in args.call or []:
                result = await session.call_tool(name, json.loads(raw))
                text = "\n".join(c.text for c in result.content if getattr(c, "type", "") == "text")
                print("--- %s(%s)%s\n%s" % (name, raw, " [isError]" if result.isError else "", text[: args.max_chars]))
                if result.isError:
                    rc = 1
    return rc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--token", default="")
    ap.add_argument("--expect", help="comma-separated tool names tools/list must equal")
    ap.add_argument("--call", nargs=2, action="append", metavar=("TOOL", "JSON"))
    ap.add_argument("--max-chars", type=int, default=1200)
    return asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    raise SystemExit(main())
