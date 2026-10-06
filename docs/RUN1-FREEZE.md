# run1 = okg v3, built fresh then frozen · staging → okg v4, rebuilt fresh — decisions and runbook

Written 2026-10-06 against this repository's `main` @ ed24df2 (staging pinned at 6d5edef) and
CMSKubernetes `archi-crab-testbed` @ aa9fcf3c. Goal:

```
 BEFORE                                       AFTER
 archi-crab-okg-staging.cern.ch/mcp  okg v3    archi-crab-okg-staging.cern.ch/mcp       okg v4 (latest dev), new volumes
                                               archi-crab-okg-staging.cern.ch/run1/mcp  okg v3, new volumes, FROZEN
```

| | engine (`ghcr.io/nausikt/archi-crab-okg`) | okg | archi-okg | okg-postgres | knowledge |
|---|---|---|---|---|---|
| **v3** = run1 = staging during the **2026-10-01 evaluation** (pin bb79172, Thu 1 Oct 07:55 UTC → Sat 3 Oct 21:51 UTC) | `sha256:f7ffb358…` | `0a8e0cd4` | `1bb7e703` | `sha256:b5b6eb8c…` | `11ede756` |
| *(staging today, not used: `9e05c239…`, okg `f4041547`, knowledge `6d5edef0`)* | | | | | |
| **v4** = engine PR (`engine/upstream` 1bb39a3 as of writing; refreshed in step 7.1) | `sha256:2b50b4aa…` | `c85d4381` | `faa731ff` | `sha256:2345f981…` | the merge sha |

## 1. Decisions

**F1 — both instances start from empty volumes, at the same time.** run1 is a new release pinned to
what staging ran for the 2026-10-01 evaluation (engine, images, knowledge revision); staging is
rebuilt on new volumes once pinned to v4. Consequences, accepted:
- run1 is that evaluation's *engine and configuration*, not that evaluation's *data*: the code
  repositories are cloned at today's HEAD (the same as v4's, F6). The data staging served on
  1 Oct no longer exists anywhere (staging has re-ingested since).
- run1 is *okg v3 on today's sources*, not a copy of what staging accumulated. A revision pin
  does not freeze okg (the worker re-crawls pages and fast-forwards code repositories), so a
  fresh build ingests the upstreams of the day it runs.
- That is what the bench wants: v3 and v4 built within hours of each other, from (nearly) the
  same upstream state, each by its own engine. Neither build can be repeated identically later:
  **their volumes are the record.**
- Staging's current volumes, and everything v3 accumulated there, are deleted (reclaim policy
  Delete). `ops/staging-backup/` takes one read-only dump first (step 4).
- No in-place engine upgrade on old data: the okg-postgres image change in the v4 bump
  (39d60d88 → 2345f981) meets an empty volume, the case CI proves. run1's okg-postgres
  (b5b6eb8c, 1 Oct) also starts empty.

**F2 — frozen = one values line (chart delta 10).** run1 is built as an ordinary okg
(`frozen.enabled: false`: bootstrap ingests and publishes, the worker syncs). Once its first
publish is verified, `frozen.enabled: true` removes catalog-claim, bootstrap, runtime-bootstrap
and the worker: the pod runs repository-sync, mcp-role, then only `mcp`, over the generation
already published. Step 7 also pauses TimescaleDB's scheduled jobs, which run inside Postgres
and would otherwise keep running. CI checks that frozen renders the MCP only and that staging
keeps its bootstrap and worker.

**F3 — run1 has its OWN Secret, `okg-archi-crab-run1`.** ⚠ Corrects V2-BENCH phase 5, which said
runs read staging's `okg-archi-crab`: its `okg-dsn`/`mcp-dsn` *name staging's Postgres*. A run
building with it would claim, migrate and publish INTO staging's database.
`scripts/okg-run-secret.sh run1` copies every key and rewrites only the DSN host, printing no
value. CI refuses any `envs/run*/` using `okg-archi-crab`; the chart refuses frozen with it.

**F4 — fixed ClusterIP for run1's MCP Service (chart delta 11, `mcp.serviceClusterIP`).**
ToolHive's remote proxy sends the address it dialled as `Host`, which is why staging lists
`10.254.109.91:*`. run1 gets `10.254.0.201`, inside 10.254.0.0/24 (the static band Kubernetes
keeps at the bottom of the 10.254.0.0/16 Service range), listed in its allowedHosts: right on the
first sync, and it survives a recreated Service.

**F5 — run1 deploys from the tag `okg-run1`, never `main`.** Later chart changes on main never
re-render it. The tag moves twice, on purpose: PR A's merge (build), A2's merge (frozen).

**F6 — same inputs underneath: same registry, same knowledge tree, same upstream commits.**
- *Registry and knowledge tree:* identical today, checked by git tree hash — `sources/` 08b6a47
  and `deployments/` b5d0ac5 at run1's pin 11ede756 (1 Oct), at staging's 6d5edef, on main ed24df2,
  and in the engine PR 1bb39a3 (it changes `versions.lock` only). `helm/okg` is also unchanged
  since 1 Oct (tree 08a9644) apart from this PR's deltas, which are off by default: run1 renders
  as staging did on 1 Oct. Step 3.2 re-checks after the engine PR is refreshed; vendored
  *engine* files (`deployments/archi-crab/schemas`, `extractors.yaml`, `skills`) may differ — they
  are each engine's own vocabulary — but `sources/`, `source_registry.yaml` and `data/` may not.
  No merge touching `sources/` or `deployments/` until both are frozen.
- *The one moving input:* the 18 `code_repos` are cloned at their branch HEAD when a build runs
  (no per-repo commit pin in this okg). The only knob is time: **both builds start within
  minutes of each other** (step 5), and step 6 compares the commit every clone sits on, repo by
  repo. The TWiki source is a committed file: identical by construction.
- *After the first publish* each worker would fast-forward again. run1 is frozen (step 7); for the
  bench window staging is frozen the same way (one line, step 7), and unfrozen afterwards.
- Same inputs is not same graph: v3 and v4 extract differently, which is what the bench measures.

**F6b — order and safety.** Because both builds start together, staging is wiped before run1 is
proven on today's sources. The safety net is the staging backup (step 4, no longer optional) and
the fact that the engine PR's CI has built v4 from empty. Staging is wiped AFTER its v4 pin is
live, so v3 never re-bootstraps on the new volumes. Every merge to main from step 5 to the end of
the bench carries `[skip ci]` in its merge commit message: otherwise `main.yaml` re-pins staging,
the pod restarts, and a restarted bootstrap ingests newer upstream commits.

**F7 — ToolHive operator: short windows.** It is paused (master out of memory) and turning it
on applies every ToolHive change made in git since the pause, staging and prod. On with B for
run1's proxy, off with C as soon as that proxy is Ready (run1 may still be building). On again
only if v4 needs a Cedar change (step 6).

## 2. What changes

| # | where | what | when |
|---|---|---|---|
| A | archi-crab-okg PR `run1-freeze` | chart deltas 10 + 11; `envs/run1/values.yaml` (v3 pins, own Secret, fixed IP, `frozen: false`); `ops/staging-backup/`; `scripts/okg-run-secret.sh`, `mcp-tools.py`; CI; this doc | step 1, then tag `okg-run1` |
| — | archi-crab-okg engine PR | v4; the bot pins staging; then the wipe | step 5 |
| B | CMSKubernetes `okg-run1-on` | enable `47-okg-run1-app` (`targetRevision: okg-run1`); `okg-run1` proxy `enabled: true`; ToolHive operator 1 | step 5, right after the wipe |
| C | CMSKubernetes `okg-run1-done` | ToolHive operator 0 | step 5, once the proxy is Ready |
| A2 | archi-crab-okg, `[skip ci]` | `envs/run1/values.yaml` and `envs/staging/values.yaml`: `frozen.enabled: true`; run1's tag moved | step 7 |
| A3 | archi-crab-okg, `[skip ci]` | `envs/staging/values.yaml`: `frozen.enabled: false` | after the bench |

## 3. Runbook

```bash
NS=archi-crab-staging
k() { kubectl -n "$NS" "$@"; }
```

### Step 0 — preflight (read-only; stop on any surprise)

```bash
# 0.1 The control plane can take it (master m2.medium; AUDIT-DEPLOY E.2): readyz < 2 s, master < ~85 % memory.
time kubectl get --raw='/readyz' ; kubectl top node

# 0.2 run1's 1 Oct images still exist (GHCR keeps digests unless a package version was deleted).
#     Both must reach Running/Completed (exit 0), not ErrImagePull:
for img in ghcr.io/nausikt/archi-crab-okg@sha256:f7ffb358b07f191ce2cf91df3d2d43322a0a9d7124a60dd7ca4d336a2db130b3 \
           ghcr.io/mitdbg/okg-postgres@sha256:b5b6eb8ca70a960d643e9117ac73d05d75899aa42018065b666d8f4bdae8fe36; do
  k run "pull-$(echo "$img" | cut -d@ -f2 | cut -c8-15)" --restart=Never --image="$img" --command \
    --overrides='{"spec":{"imagePullSecrets":[{"name":"ghcr-mitdbg-pull"}]}}' -- true
done; sleep 60; k get pods | grep pull-      # want Completed, not ErrImagePull
k get pods -o name | grep pull- | xargs -r kubectl -n "$NS" delete
#     Staging's live pins (recorded by the backup Job's SOURCE_* env; edit them there if they differ):
k get sts archi-crab-okg-staging-runtime -o jsonpath='{.spec.template.spec.containers[?(@.name=="mcp")].image}{"\n"}'
#   want …archi-crab-okg@sha256:9e05c239…

# 0.3 Volumes. run1: +2 cinder-io1-delete (150Gi Postgres, 75Gi runtime; the runtime may go to
#     cinder-standard if io1 is short). Backup: +1 cinder-standard. The staging wipe
#     deletes 2 io1 and creates 2: transiently +2 until Cinder has deleted the old ones.
kubectl get pvc -A -o custom-columns=NS:.metadata.namespace,NAME:.metadata.name,CLASS:.spec.storageClassName,SIZE:.spec.resources.requests.storage | sort -k3
openstack quota show -c volumes -c gigabytes

# 0.4 Room for a second full okg on the workers (run1 requests: Postgres 1 CPU/4Gi, runtime 1 CPU/2Gi; limits 8Gi + 6Gi).
kubectl describe nodes | grep -A6 'Allocated resources'

# 0.5 The fixed ClusterIP is free (no output = free; else pick another 10.254.0.x in envs/run1).
kubectl get svc -A -o jsonpath='{range .items[*]}{.spec.clusterIP}{"\n"}{end}' | grep -x 10.254.0.201

# 0.6 Prerequisite Secrets.
k get secret ghcr-mitdbg-pull okg-archi-crab -o name

# 0.7 What the ToolHive operator will apply when it comes back (F7).
git -C ../CMSKubernetes fetch origin && git -C ../CMSKubernetes log --oneline aa9fcf3c..origin/archi-crab-testbed -- helm/archi-crab argocd/archi-crab
kubectl get mcpserver,mcpremoteproxy,virtualmcpserver -A
```

### Step 1 — PR A: merge, tag

Open the PR from `run1-freeze`; CI must be green (lint incl. the run checks, kubeconform incl.
run1 building and frozen, okg-validate, e2e). Merge. `main.yaml` then re-pins staging to the merge
sha: staging restarts on the same v3 engine (deployments/ unchanged) — harmless.
```bash
git fetch origin && A=<PR A merge sha>
git tag -a okg-run1 -m "okg v3 run1: build (docs/RUN1-FREEZE.md)" "$A" && git push origin okg-run1
```

### Step 2 — run1's Secret (before B)

```bash
scripts/okg-run-secret.sh run1
#   keys: git-token mcp-dsn mcp-password okg-dsn postgres-password
#   okg-dsn: user=postgres host=archi-crab-okg-run1-postgres:5432 db=okg
#   mcp-dsn: user=okg_mcp  host=archi-crab-okg-run1-postgres…:5432 db=okg
```

### Step 3 — v4 ready, inputs identical (nothing is wiped yet)

**3.1 Refresh the engine PR to the newest `dev`.** GitHub → Actions → `engine` → *Run workflow*
(defaults). It merges main (with PR A) forward into `engine/upstream` and updates the PR. Its CI
must be green (lint, vendor-check, okg-validate, e2e incl. `chart-path`: v4 built from an empty
database, staging's case after the wipe). Do NOT merge yet.

**3.2 Same knowledge for both (F6).** Must print nothing:
```bash
git fetch origin
R1=11ede756bb057d7ae782b3da68f0563e20736593   # run1's knowledge revision (1 Oct)
git diff --stat "$R1" origin/engine/upstream -- sources deployments/archi-crab/source_registry.yaml \
  deployments/archi-crab/data deployments/archi-crab/deployment.yaml deployments/archi-crab/invariants.yaml
git diff --stat "$R1" origin/engine/upstream -- deployments    # informational: vendored engine files only
```
If the first diff is not empty, stop: the two instances would not read the same sources.

### Step 4 — back up staging (insurance: staging is wiped before run1 is proven, F6b)

```bash
k exec archi-crab-okg-staging-postgres-0 -c postgres -- psql -XAt -U postgres -d postgres -c \
  "SELECT datname, pg_size_pretty(pg_database_size(datname)) FROM pg_database WHERE NOT datistemplate"   # size the PVC (50Gi ~ 80 GB)
kubectl apply -f ops/staging-backup/pvc.yaml -f ops/staging-backup/dump-job.yaml
k logs -f job/archi-crab-okg-staging-backup
k wait --for=condition=complete --timeout=6h job/archi-crab-okg-staging-backup
```
Read-only on staging, one snapshot (ops/staging-backup/README.md). While it runs, staging DDL that
needs an exclusive lock (a publish swap) waits, and queries queue behind it; start it right after
a publish, and `k delete job archi-crab-okg-staging-backup` releases every lock if `/mcp` stalls.

### Step 5 — start both builds together

Announce first: `/mcp` (Claude Code, OpenWebUI's okg tool server) is down from the wipe until v4's
first publish (hours); `/run1/mcp` appears when run1 has published. From here to the end of the
bench, no merge touching `sources/` or `deployments/`, and every other merge to main with
`[skip ci]` in its commit message (F6b).

```bash
# 5.1 Merge the engine PR. main.yaml: e2e, then the bot's "staging: pin <sha>". Wait until it is live:
k get sts archi-crab-okg-staging-runtime -o jsonpath='{.spec.template.spec.containers[?(@.name=="mcp")].image}{"\n"}'   # = v4's digest
# 5.2 Wipe staging at once. Volumes first (they wait in Terminating while the pods use them), then
#     the StatefulSets; Argo (selfHeal) recreates them on new volumes. Services untouched
#     (staging keeps 10.254.109.91).
k delete pvc runtime-data-archi-crab-okg-staging-runtime-0 postgres-data-archi-crab-okg-staging-postgres-0 --wait=false
k delete sts archi-crab-okg-staging-runtime archi-crab-okg-staging-postgres
# 5.3 In the same minutes: merge CMSKubernetes B (re-check 0.1 first). run1 starts building.
# 5.4 Watch both bootstraps; merge C (operator 0) as soon as the okg-run1 proxy is Ready.
k get pvc | grep -E 'archi-crab-okg-(staging|run1)'
k get pods -l 'app.kubernetes.io/instance in (archi-crab-okg-staging,archi-crab-okg-run1)' -w
k logs -f archi-crab-okg-staging-runtime-0 -c bootstrap      # and archi-crab-okg-run1-runtime-0
k get mcpremoteproxy | grep run1; k get svc archi-crab-okg-run1-mcp   # Ready; ClusterIP 10.254.0.201
```
A pod stuck Pending on a volume that is gone: delete the pod. PVC Pending on quota: Cinder is
still deleting staging's old volumes; it clears by itself. If the operator crash-loops (lease
timeouts) or the master passes ~90 %, merge C anyway and redo B's window later.

If v3 cannot build on today's sources (a source fails admission, a connector breaks): v4 keeps
building; decide with the backup in hand (fix on a run1 branch, or a narrower run1).

### Step 6 — verify both, and that their inputs are the same

```bash
# 6.1 The commit every clone sits on, per instance (F6). Run right after each first publish.
heads() { k exec "$1-runtime-0" -c mcp -- sh -c \
  'for d in "$OKG_ENVIRONMENT_DATA_ROOT"/repos/*/; do printf "%s %s\n" "$(basename "$d")" "$(git -C "$d" rev-parse HEAD)"; done'; }
heads archi-crab-okg-run1 > run1-heads.txt; heads archi-crab-okg-staging > v4-heads.txt
diff run1-heads.txt v4-heads.txt && echo "same 18 commits"
# 6.2 Published, and the tool surfaces (port-forwards: no token before the proxy)
for r in run1 staging; do k exec archi-crab-okg-$r-runtime-0 -c mcp -- okg status --deployment archi-crab --json | head -20; done
k port-forward svc/archi-crab-okg-run1-mcp 18765:8765 & k port-forward svc/archi-crab-okg-staging-mcp 18766:8765 &
scripts/mcp-tools.py http://127.0.0.1:18765/mcp | tee run1-tools.txt
scripts/mcp-tools.py http://127.0.0.1:18766/mcp | tee v4-tools.txt
diff <(cut -d' ' -f1 run1-tools.txt) <(cut -d' ' -f1 v4-tools.txt)       # v3 -> v4 tool surface
# 6.3 Through the gateway
curl -si https://archi-crab-okg-staging.cern.ch/run1/mcp | grep -i www-authenticate
#   want: resource_metadata="https://archi-crab-okg-staging.cern.ch/.well-known/oauth-protected-resource/run1/mcp"
curl -s https://archi-crab-okg-staging.cern.ch/.well-known/oauth-protected-resource/run1/mcp
#   want: "resource": "https://archi-crab-okg-staging.cern.ch/run1/mcp"
claude mcp add --transport http okg-run1 https://archi-crab-okg-staging.cern.ch/run1/mcp \
  --client-id archi-crab-okg-public-staging --callback-port 8765
#   /mcp -> authenticate on both okg-run1 and the existing staging entry; call every tool; `query` denied on both
```
- A repo whose commit differs in 6.1: it moved between the two clones. Decide: accept and note it
  in §5, or delete that repo's clone on the instance that is behind, restart its pod, and let the
  worker re-clone (it fast-forwards to the same HEAD if the repo has not moved again).
- `421`/`403` *Invalid Host* on run1: the Service must have ClusterIP `10.254.0.201` and the `mcp`
  args `10.254.0.201:*`; any other address the proxy sends goes into `mcp.allowedHosts` (A2 carries it).
- v4 renamed or added a raw-SQL tool (anything in `v4-tools.txt` that takes SQL and is not named
  `query`): Cedar's forbid does not cover it. Add it to the `okg` entry's policies (and
  `*okg-policies`) in CMSKubernetes `mcp-gateway/values-staging.yaml`, with the operator at 1 for
  that change and back to 0 after:
  ```yaml
      - |
        forbid(principal, action == Action::"call_tool", resource == Tool::"<new name>");
  ```
- v4 cannot build: `/run1/mcp` serves v3; fix forward with a newer engine PR (inputs move: re-run
  step 3.2 and accept the time gap, or rebuild run1 alongside).

### Step 7 — freeze both (A2, `[skip ci]`)

One PR: `frozen.enabled: true` in `envs/run1/values.yaml` AND in `envs/staging/values.yaml`
(staging's for the bench window only; the bot never writes that line). Merge with `[skip ci]` in
the merge commit message. Argo re-renders staging at once; move run1's tag:
```bash
git fetch origin && A2=<A2 merge sha>
git tag -f -a okg-run1 -m "okg v3 run1: frozen (docs/RUN1-FREEZE.md)" "$A2" && git push -f origin okg-run1
argocd app get archi-crab-okg-run1 --hard-refresh            # or Refresh (hard) in the UI
for r in run1 staging; do
  k get pod archi-crab-okg-$r-runtime-0 -o jsonpath='{.spec.initContainers[*].name} | {.spec.containers[*].name}{"\n"}'   # repository-sync mcp-role | mcp
  # TimescaleDB runs scheduled jobs inside Postgres, worker or not: list, then pause user jobs (id >= 1000)
  k exec archi-crab-okg-$r-postgres-0 -c postgres -- psql -XAt -U postgres -d okg \
    -c "SELECT job_id, proc_schema || '.' || proc_name, scheduled FROM timescaledb_information.jobs WHERE job_id >= 1000" \
    -c "SELECT count(*) FROM (SELECT alter_job(job_id, scheduled => false) FROM timescaledb_information.jobs WHERE job_id >= 1000) j"
  k exec archi-crab-okg-$r-runtime-0 -c mcp -- okg status --deployment archi-crab --json | head -20    # the frozen generation: record it
  k exec archi-crab-okg-$r-postgres-0 -c postgres -- psql -XAt -U postgres -d okg \
    -c "SELECT 'node ' || subtype || ' ' || count(*) FROM okg.v_nodes GROUP BY subtype ORDER BY 1" \
    -c "SELECT 'edges ' || count(*) FROM okg.v_edges" | tee $r-fingerprint.txt
done
heads archi-crab-okg-run1 | diff - run1-heads.txt && heads archi-crab-okg-staging | diff - v4-heads.txt && echo "no clone moved before the freeze"
```
If a clone moved between step 6 and the freeze (the worker fast-forwarded it), the generation may
have too: re-run 6.1 and decide as there.

**After the bench (A3, `[skip ci]`):** `frozen.enabled: false` in `envs/staging/values.yaml`, and
resume staging's TimescaleDB jobs: `SELECT alter_job(job_id, scheduled => true) FROM
timescaledb_information.jobs WHERE job_id >= 1000`. Staging then catches up with its upstreams.
run1 stays frozen.

### Step 8 — record

Fill §5 and V2-BENCH §6: both frozen generations and fingerprints, `run1-heads.txt` /
`v4-heads.txt`, the tool diff. Neither build can be repeated identically (F1): a dump of each
(the backup Job with that release's names and labels) is cheap insurance once frozen.

## 4. Debt and discordances found on the way

1. **V2-BENCH phase 5 said runs share `okg-archi-crab`** — wrong and dangerous (F3); corrected.
2. **Staging's allowedHosts pins a dynamic ClusterIP** (`10.254.109.91:*`); the wipe keeps the
   Service, but a recreated Service breaks the proxy. `mcp.serviceClusterIP: 10.254.109.91` in
   envs/staging would pin the address it already has.
3. **CMSKubernetes `mcp-gateway/values-staging.yaml` defines `authz:` twice** (AUDIT B7); Helm keeps
   the last (`enabled: true`). Delete the first.
4. **The run1/run2 Argo apps promised a console at `/runN/akmon`** that is not on main; run1's
   comment now says so.
5. **Engine bumps that change okg-postgres are proven on empty databases only.** Moot for staging
   now (it is rebuilt), not for prod, which will be upgraded in place: check PG major and
   extension libraries before that promotion (a check script is in the first run1 patch set).
6. **The master is still m2.medium**: every ToolHive change costs an operator window (F7).

## 5. Where we are

| step | state | evidence |
|---|---|---|
| 0 preflight | | |
| 1 PR A merged, tag okg-run1 | | merge sha |
| 2 Secret | | hosts printed by the script |
| 3 engine PR refreshed, green; knowledge diff empty | | engine PR #, okg/archi-okg commits |
| 4 staging backup | | MANIFEST |
| 5 v4 pin live, staging wiped, B merged, C merged | | pin sha; times both bootstraps started |
| 6 both verified, same clone commits | | generations; run1-heads.txt = v4-heads.txt; tool diff |
| 7 both frozen (A2), run1 tag moved | | frozen generations; fingerprints; TimescaleDB jobs paused |
| A3 staging unfrozen (after the bench) | | |
