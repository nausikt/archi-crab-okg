#!/bin/bash
# scripts/instance-watch.sh -- shell helpers for watching an okg instance build (docs/DEPLOYMENT-NOTES.md §7).
#
#   source scripts/instance-watch.sh                       # watches the instances in $WATCH (below)
#   WATCH="archi-crab-staging/archi-crab-okg-dev" source scripts/instance-watch.sh
#   st      pods, restarts, last bootstrap log line, publisher lines, published generation
#   cnt     database size and the five biggest tables (what is growing)
#   pgact   active statements with age and wait event
#   dio     per-volume disk MB/s and IOPS over 10 s (from /proc/diskstats inside the Postgres pod)
#
# WATCH = space-separated <namespace>/<release>; the pods are <release>-runtime-0 and <release>-postgres-0.
WATCH="${WATCH:-archi-crab-staging/archi-crab-okg-v0-2-0-rc2-v0-2-0-rc1 archi-crab/archi-crab-okg}"

_watch_each() {   # calls "$1 <ns> <release>" for every WATCH entry
  local w; for w in $WATCH; do "$1" "${w%%/*}" "${w#*/}"; done
}

_st1() {
  local ns=$1 r=$2
  echo "== $ns/$r  $(date -u +%H:%M:%SZ)"
  kubectl -n "$ns" get pod "$r-runtime-0" --no-headers 2>/dev/null | awk '{print "   pod:", $3, "restarts:", $4, $5, $6, "age:", $NF}'
  kubectl -n "$ns" logs "$r-runtime-0" -c bootstrap --timestamps --tail=1 2>/dev/null | cut -c1-19 | sed 's/^/   last log: /'
  kubectl -n "$ns" logs "$r-runtime-0" -c bootstrap 2>/dev/null | grep -c "okg publisher archi-crab" | sed 's/^/   publisher lines: /'
  kubectl -n "$ns" exec "$r-runtime-0" -c mcp -- okg status --deployment archi-crab --json 2>/dev/null \
    | grep -o 'okg:archi-crab:branch:default:gen:[0-9TZ]*:[0-9a-f]*' | sort -u | sed 's/^/   PUBLISHED: /' | grep . \
    || echo "   published: not yet (bootstrap still running)"
}
st() { _watch_each _st1; }

_cnt1() {
  local ns=$1 r=$2
  echo "== $ns/$r $(date -u +%H:%M)  db size: $(kubectl -n "$ns" exec "$r-postgres-0" -- psql -d okg -Atc "select pg_size_pretty(pg_database_size('okg'))" 2>&1 | tail -1)"
  kubectl -n "$ns" exec "$r-postgres-0" -- psql -d okg -Atc "select '   '||relname||'  '||n_live_tup from pg_stat_user_tables order by n_live_tup desc limit 5" 2>&1 | tail -5
}
cnt() { _watch_each _cnt1; }

_pgact1() {
  local ns=$1 r=$2
  echo "== $ns/$r $(date -u +%H:%M)"
  kubectl -n "$ns" exec "$r-postgres-0" -- psql -d okg -Atc "select '   '||to_char(now()-query_start,'HH24:MI:SS')||'  wait='||coalesce(wait_event_type,'-')||'/'||coalesce(wait_event,'-')||'  '||left(regexp_replace(query,'\s+',' ','g'),90) from pg_stat_activity where datname='okg' and state<>'idle' and query not ilike '%pg_stat_activity%' order by query_start limit 6" 2>&1
}
pgact() { _watch_each _pgact1; }

_dio1() {
  local ns=$1 r=$2
  kubectl -n "$ns" exec "$r-postgres-0" -- sh -c 'dev=$(df -P "$PGDATA" | awk "NR==2{print \$1}" | sed "s#/dev/##"); a=$(grep " $dev " /proc/diskstats); sleep 10; b=$(grep " $dev " /proc/diskstats); echo "$dev $a"; echo "$dev $b"' 2>/dev/null \
    | awk -v t="$ns/$r" '{d=$1; rio[NR]=$5; rs[NR]=$7; wio[NR]=$9; ws[NR]=$11} END {if (NR<2) {print "== " t "  (could not read diskstats)"; exit} printf "== %s %s  read %.1f MB/s %.0f IOPS   write %.1f MB/s %.0f IOPS\n", t, d, (rs[2]-rs[1])*512/1e7, (rio[2]-rio[1])/10, (ws[2]-ws[1])*512/1e7, (wio[2]-wio[1])/10}'
}
dio() { _watch_each _dio1; }
