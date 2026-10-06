#!/usr/bin/env bash
# okg-run-secret.sh — create a run's own okg Secret from staging's (docs/RUN1-FREEZE.md, step 3).
#
# okg-archi-crab's DSNs NAME STAGING'S POSTGRES. A run that read that Secret would serve, and
# its init containers would write, staging's database. This copies every key (same passwords:
# the restored roles carry them) and rewrites the host in okg-dsn and mcp-dsn to the run's own
# Postgres Service. No value is printed, written to disk, or put in an annotation: the Secret is
# piped to `kubectl create`, never `apply` (apply would store it in last-applied-configuration).
#
#   scripts/okg-run-secret.sh run1        # -> Secret okg-archi-crab-run1
#   NS=archi-crab-staging SRC=okg-archi-crab scripts/okg-run-secret.sh run2
set -euo pipefail
RUN="${1:?usage: $0 <run name, e.g. run1>}"
NS="${NS:-archi-crab-staging}"
SRC="${SRC:-okg-archi-crab}"
FROM_HOST="${FROM_HOST:-archi-crab-okg-staging-postgres}"
TO_HOST="archi-crab-okg-$RUN-postgres"
DST="$SRC-$RUN"

if kubectl -n "$NS" get secret "$DST" > /dev/null 2>&1; then
  echo "Secret $NS/$DST exists; delete it first to recreate it." >&2
  exit 1
fi
kubectl -n "$NS" get secret "$SRC" -o json \
| FROM_HOST="$FROM_HOST" TO_HOST="$TO_HOST" DST="$DST" RUN="$RUN" python3 -c '
import base64, json, os, sys
src = json.load(sys.stdin)
data = dict(src["data"])
old, new = os.environ["FROM_HOST"], os.environ["TO_HOST"]
for key in ("okg-dsn", "mcp-dsn"):
    dsn = base64.b64decode(data[key]).decode()
    if not dsn.startswith(("postgresql://", "postgres://")):
        sys.exit(f"{key}: not a postgresql:// URL; this script handles URL DSNs only; nothing created")
    n = dsn.count(old)
    if n != 1:
        sys.exit(f"{key}: expected the host {old} exactly once, found it {n} time(s); nothing created")
    data[key] = base64.b64encode(dsn.replace(old, new).encode()).decode()
json.dump({
    "apiVersion": "v1", "kind": "Secret", "type": src.get("type", "Opaque"),
    "metadata": {"name": os.environ["DST"], "namespace": src["metadata"]["namespace"],
                 "labels": {"app.kubernetes.io/part-of": "archi-crab-okg", "archi-crab/run": os.environ["RUN"]}},
    "data": data,
}, sys.stdout)
' | kubectl create -f -

# Proof without values: the keys, and only the host:port/db of each DSN.
kubectl -n "$NS" get secret "$DST" -o json | python3 -c '
import base64, json, sys
from urllib.parse import urlsplit
d = json.load(sys.stdin)["data"]
print("keys:", " ".join(sorted(d)))
for key in ("okg-dsn", "mcp-dsn"):
    u = urlsplit(base64.b64decode(d[key]).decode())
    if u.scheme not in ("postgresql", "postgres"):
        print(f"{key}: not a URL (not printed)"); continue
    db = u.path.lstrip("/")
    print(f"{key}: user={u.username} host={u.hostname}:{u.port} db={db}")
'
