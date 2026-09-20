#!/usr/bin/env bash
# archi-crab smoke — knowledge + deployment testing ONLY.
# Same script in CI (e2e-smoke) and as the Argo CD PostSync hook (--in-cluster).
set -euo pipefail
DEP="${OKG_DEPLOYMENT:-archi-crab}"; MODE="${1:-}"

echo "== 1/3 published (assert STATUS; okg exits 0 even on a failed publish)"
okg status --deployment "$DEP" --json | tee /tmp/okg-status.json
python3 - <<'PY'
import json; s=json.load(open('/tmp/okg-status.json'))
s = s.get('publishing') or s  # okg nests publish fields under `publishing`
assert s.get('latest_published_status')=='published', f"not published: {s}"
assert s.get('latest_published_generation'), "no published generation"
print("generation:", s['latest_published_generation'])
PY

echo "== 2/3 invariant floor answers real queries"
for q in "CRAB task submission" "CRABClient command" "def submit" "CMSSW release"; do
  for attempt in 1 2; do
    out="$(okg search --deployment "$DEP" --query "$q" 2>&1)" || true
    grep -q "results (" <<<"$out" && break
    [ "$attempt" = 2 ] && { echo "EMPTY: $q" >&2; echo "$out" | tail -8; exit 1; }
    sleep 2
  done
done


echo "== 3/3 MCP serves"
if [[ "$MODE" == "--in-cluster" ]]; then
  URL="http://${MCP_HOST:?}:${MCP_PORT:-8765}/mcp"; AUTH=()
else
  export OKG_MCP_AUTH_TOKEN="${OKG_MCP_AUTH_TOKEN:-$(head -c32 /dev/urandom | od -An -tx1 | tr -d " \n")}"
  OKG_PODMAN_EXTRA="${OKG_PODMAN_EXTRA:--p 127.0.0.1:8766:8766}" \
  okg mcp-serve --deployment "$DEP" --transport streamable-http --host 0.0.0.0 --port 8766 \
      --allowed-host 127.0.0.1:8766 --auth-token-env OKG_MCP_AUTH_TOKEN >/tmp/mcp.log 2>&1 &
  MCP_PID=$!; trap 'kill $MCP_PID 2>/dev/null || true' EXIT
  for _ in $(seq 1 20); do curl -fsS -o /dev/null http://127.0.0.1:8766/ 2>/dev/null && break || sleep 1; done
  URL=http://127.0.0.1:8766/mcp; AUTH=(-H "Authorization: Bearer $OKG_MCP_AUTH_TOKEN")
fi
curl -fsS "${AUTH[@]}" -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' "$URL" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"archi-crab-smoke","version":"0.7.0"}}}' \
  | grep -q '"result"' || { echo "MCP initialize failed"; cat /tmp/mcp.log 2>/dev/null; exit 1; }
echo "SMOKE OK"
