#!/usr/bin/env python3
"""mcp-tools.py — list an MCP server's tools over streamable HTTP (stdlib only).

For the okg MCP behind a port-forward, i.e. BEFORE the ToolHive proxy (no token needed):

    kubectl -n archi-crab-staging port-forward svc/archi-crab-okg-run1-mcp 18765:8765 &
    scripts/mcp-tools.py http://127.0.0.1:18765/mcp            # names + first line
    scripts/mcp-tools.py http://127.0.0.1:18765/mcp --names    # names only (diff two servers)

Used by docs/RUN1-FREEZE.md to compare v3 (run1) with v4 (staging) and to check that the
raw-SQL tool is still named `query` (the name the gateway's Cedar policy forbids).
"""
import json
import sys
import urllib.request

HEADERS = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}


def rpc(url, body, session=None):
    headers = dict(HEADERS)
    if session:
        headers["Mcp-Session-Id"] = session
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        sid = resp.headers.get("Mcp-Session-Id") or session
        raw = resp.read().decode()
    if "id" not in body:  # a notification: 202, no body
        return None, sid
    if resp.headers.get_content_type() == "text/event-stream":
        for line in raw.splitlines():
            if line.startswith("data:"):
                msg = json.loads(line[5:].strip())
                if msg.get("id") == body["id"]:
                    return msg, sid
        raise SystemExit(f"no response to {body['method']} in the event stream")
    return json.loads(raw), sid


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    url, names_only = sys.argv[1], "--names" in sys.argv[2:]
    init, sid = rpc(url, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2025-03-26", "capabilities": {},
        "clientInfo": {"name": "archi-crab-mcp-tools", "version": "1"}}})
    if "error" in init:
        raise SystemExit(f"initialize: {init['error']}")
    rpc(url, {"jsonrpc": "2.0", "method": "notifications/initialized"}, sid)
    tools, _ = rpc(url, {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}, sid)
    if "error" in tools:
        raise SystemExit(f"tools/list: {tools['error']}")
    info = init["result"].get("serverInfo", {})
    if not names_only:
        print(f"# {info.get('name', '?')} {info.get('version', '')} ({init['result'].get('protocolVersion')})")
    for tool in sorted(tools["result"]["tools"], key=lambda t: t["name"]):
        first = (tool.get("description") or "").strip().splitlines()
        print(tool["name"] if names_only else f"{tool['name']:28} {first[0][:100] if first else ''}")


if __name__ == "__main__":
    main()
