#!/usr/bin/env bash
# archi-crab smoke — knowledge + deployment testing ONLY (not okg code testing).
# Runs identically as the CI e2e step and as the Argo CD PostSync hook
# (`--in-cluster`), so "smoke passed" means the same thing everywhere.
#
#   1. Published   — assert on STATUS, never on exit code
#                    (`okg install` exits 0 even when the publish fails).
#   2. Invariant   — one search per required subtype returns something.
#   3. Serves      — MCP initialize handshake succeeds.
set -euo pipefail
DEP="${OKG_DEPLOYMENT:-archi-crab}"
MODE="${1:-}"

echo "== 1/3 published status"
okg status --deployment "$DEP" --json | tee /tmp/okg-status.json
python3 - <<'PY'
import json
s = json.load(open('/tmp/okg-status.json'))
assert s.get('latest_published_status') == 'published', f"not published: {s}"
assert s.get('latest_published_generation'), "no published generation"
print("generation:", s['latest_published_generation'])
PY

echo "== 2/3 invariant floor answers real queries"
for q in "CRAB task submission" "CRABClient command" "def submit" "CMSSW release"; do
  if ! okg search --deployment "$DEP" --query "$q" | grep -q .; then
    echo "EMPTY search result for: $q" >&2; exit 1
  fi
done

echo "== 3/3 MCP serves"
if [[ "$MODE" == "--in-cluster" ]]; then
  URL="http://${MCP_HOST:?}:${MCP_PORT:-8765}/mcp"; AUTH=()
else
  export OKG_MCP_AUTH_TOKEN=ci-smoke
  okg mcp-serve --deployment "$DEP" --transport streamable-http \
      --host 127.0.0.1 --port 8766 --allowed-host 127.0.0.1:8766 \
      --auth-token-env OKG_MCP_AUTH_TOKEN >/tmp/mcp.log 2>&1 &
  MCP_PID=$!; trap 'kill $MCP_PID 2>/dev/null || true' EXIT
  for _ in $(seq 1 20); do curl -fsS -o /dev/null "http://127.0.0.1:8766/" 2>/dev/null && break || sleep 1; done
  URL="http://127.0.0.1:8766/mcp"; AUTH=(-H "Authorization: Bearer ci-smoke")
fi
curl -fsS "${AUTH[@]}" -H 'Content-Type: application/json' \
     -H 'Accept: application/json, text/event-stream' "$URL" \
     -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"archi-crab-smoke","version":"0.5.0"}}}' \
  | grep -q '"result"' || { echo "MCP initialize failed"; cat /tmp/mcp.log 2>/dev/null; exit 1; }

echo "SMOKE OK"
