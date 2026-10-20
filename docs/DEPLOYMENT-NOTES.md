# Deployment notes: what broke, why, and the rule it left behind

A dated log of real deployment problems on the archi-crab testbed, one entry per build day.
Each item says what was observed, the cause once found, the fix, and the rule we keep. Read
the **Rules** section before a build; read the rest when something looks the same.

Companion: `scripts/instance-watch.sh` (shell helpers `st`, `cnt`, `pgact`, `dio` used in
these notes).

## Rules (distilled)

1. **One big Postgres per node.** Two 8 Gi databases on a 14 Gi worker evict each other's page
   cache, and a publish on these volumes then runs at ~44 random reads/s. Check placement
   (`kubectl get pods -A -o wide | grep postgres-0`) before a build; move one with cordon +
   pod delete if two share a node (the Cinder volume follows the pod, the data stays).
2. **Check the Cinder quota before creating claims**, by volume TYPE and by COUNT:
   `PYTHONNOUSERSITE=1 openstack limits show --absolute` (the env var works around a broken
   `openstack` CLI on lxplus). Cinder answers HTTP 413 to a claim over quota; the claim stays
   `Pending` forever and the pod's event only says "unbound immediate PersistentVolumeClaims".
3. **A StatefulSet's volume class cannot be edited in place.** To change it: merge the values
   change, point the Argo app at it, then delete the StatefulSet and the Pending claim; Argo
   recreates both. Never touch the Postgres StatefulSet of a built instance this way.
4. **Don't delete a runtime pod whose bootstrap is running.** Killing a bootstrap mid-drain
   leaves its tail ownership behind; the next bootstrap drains nothing, goes straight to the
   publish gate and fails one `archi_crab_core_floor` invariant check (`code_symbol`
   live_count 0). It self-corrects on the following restart, at the cost of ~5 min and a scare.
5. **`Init:2/5` for hours is normal.** The bootstrap (`okg provision --publish-once`) drains
   every source, then publishes once; the `mcp` container cannot exist before that, so
   "mcp container not up" means "bootstrap still running", not "unreachable". Publisher log
   lines appear only after the last source is drained.
6. **Cilium's `Operation not permitted` on a ClusterIP = no backend yet.** The bootstrap
   crash-loops (5 min back-off) until Postgres has an endpoint, then connects. Wait; do not
   delete (rule 4).
7. **These volumes are slow for everyone**: ~20 MB/s at queue depth 1 and 20-40 ms per request
   on both `cinder-io1` and `cinder-standard`, all nodes. A page-at-a-time scan of a 2.4 GB
   table is ~2 h cold and minutes warm. Cache is the only lever; protect it (rule 1).
8. **Git-history instances need the raised publish cap** (adapter b2:
   `publisher.hard_statement_timeout_seconds: 7200` in deployment.yaml plus the Secret key
   `allow-raised-timeout` wired as `OKG_PUBLISH_LOCK_HEADROOM_ALLOW_RAISED_TIMEOUT` through
   `secrets.extraEnv`). Without the env flag okg silently clamps to its 900 s default.
9. **Measure before acting.** `pg_stat_activity` wait events, per-volume `/proc/diskstats`
   (`dio`), a `dd iflag=direct` read, and `/proc/<pid>/io` of the backend answer "stuck,
   starved or slow?" in a minute. `pg_statio_*` counters do not move inside a long transaction;
   `kubectl top` needs a Metrics API this cluster does not have.

## 2026-10-19: D, F, v2 on corpus v0.2.0-rc1 (first instances with git-history lanes)

Context: wipe-and-rebuild of D (staging, `archi-crab-staging`) and F (prod, `archi-crab`) on
engine v0.2.0-rc2 × corpus v0.2.0-rc1, graph ≈ 539 k nodes / 1.57 M edges (≈ 2× C). Two worker
nodes (node-5, node-6) were added during the day. master-0 (3.5 GiB) was NotReady/OOM all day,
which killed the OpenStack cloud-controller-manager.

### 1. First publish died at okg's 900 s statement cap

- Seen: bootstrap restarts every ~70 min; `--previous` log ends in
  `psycopg.errors.QueryCanceled` from `attributes._materialize_view_kind`; "publish lock held
  2135 s > hard statement_timeout 900000 ms".
- Cause: the publish's view materialization over a 2× graph takes longer than okg's default
  per-statement cap. The knob is read in `okg/substrate/deployments/__init__.py`
  (`publisher.hard_statement_timeout_seconds`) but `publish_lock_headroom.py` clamps a raised
  value back to the default unless `OKG_PUBLISH_LOCK_HEADROOM_ALLOW_RAISED_TIMEOUT=true`.
- Fix: adapter b2 (PR #49): `deployment.yaml` `publisher.hard_statement_timeout_seconds: 7200`;
  chart `secrets.extraEnv` maps Secret key `allow-raised-timeout` ("true") into the bootstrap
  and worker containers. Engine-check green at the adapter commit; D and F re-rendered at it.
- Rule 8. 2 h, not 6: the cap also bounds how long a wedged publish can hold the lock.

### 2. F's runtime claim never provisioned: Cinder quota by volume count

- Seen: `runtime-data-archi-crab-okg-runtime-0` (75 Gi `cinder-standard`) `Pending` for 15+ min,
  provisioner event `Provisioning` ×12 with no `ProvisioningSucceeded`; CSI controller log:
  `CreateVolume failed ... got 413 instead`. Pod event: "0/8 nodes are available: pod has
  unbound immediate PersistentVolumeClaims".
- Cause: the project's `standard` quota was 40/40 **volumes** (gigabytes were fine); io1 had
  31/35. 413 is Cinder's OverLimit.
- Fix: PR #50, F's runtime volume on `cinder-io1-delete` (matrix + rendered envs/prod); Argo app
  pointed at the merge; `kubectl delete sts archi-crab-okg-runtime` + the Pending claim; Argo
  recreated both, claim Bound in 50 s.
- Rules 2, 3. Follow-up: most of the 40 standard volumes are orphans of earlier wipes; list
  `openstack volume list` names (`pvc-…`) against `kubectl get pv` and delete the ones with no
  PV. The matrix budgets 5 standard volumes in total.

### 3. New worker nodes stuck `uninitialized`; pods `Insufficient cpu`

- Seen: v2 rc1 data-manager Pending for 5 h ("0/6 nodes ... Insufficient cpu"); after adding
  node-5/6 they carried `node.cloudprovider.kubernetes.io/uninitialized` and took no pods.
- Cause: the cloud-controller-manager initialises new nodes; it lives on master-0, which was
  NotReady (OOM at 3.5 GiB).
- Fix: taint removed by hand (`kubectl taint node <n> node.cloudprovider.kubernetes.io/uninitialized-`).
  Proper fix: hard-reboot and resize master-0 between builds (`openstack server reboot --hard
  …-master-0`), never while a bootstrap is mid-publish.

### 4. `database_unreachable ... Operation not permitted`, then one `core_floor` failure

- Seen: D's bootstrap `Init:CrashLoopBackOff` (6 restarts) while its Postgres was still
  ContainerCreating on node-5; log `connection to server at "<ClusterIP>", port 5432 failed:
  Operation not permitted`. Endpoints and Cilium on the new node were fine.
- Cause: Cilium's socket load-balancer rejects a connect to a ClusterIP with no backend with
  EPERM. Once Postgres was Running, the 7th attempt connected on its own.
- Mistake: we deleted the pod "to reset the back-off" just as that 7th attempt had started
  draining. The recreated pod's first bootstrap found the tails still owned, drained nothing,
  and the publish gate refused an empty graph (`archi_crab_core_floor`, `code_symbol`
  live_count 0, exit 1). The next restart drained normally.
- Rules 4, 6.

### 5. The edge pass at 44 IOPS: two databases on one node

- Seen: D's publish spent > 1 h in `WITH branch AS (...) SELECT DISTINCT ON (e.edge_id) ...
  ORDER BY e.edge_id, e.live_lo DESC` (the publisher's edge pass; plan = Index Scan on
  `writer_segment_id` + heap fetch per row + external sort on 16 MB work_mem), wait event
  `IO/DataFileRead`, database size flat. F, 20 min behind on the same node, had already written
  its 2.1 M attribute rows and was in short `snapshot_batch` statements, which then slowed from
  30 s to 3 min each.
- Measured: D's volume 0.4 MB/s / 44 IOPS (one 8 KB read per ~22 ms); `dd iflag=direct` 200 MB
  reads: 13-26 MB/s on every volume tested (D, F, C, dev; io1 and standard alike), so the
  volumes are uniformly slow, not node-5's. A `pg_prewarm(..., 'read')` of the 2.4 GB heap took
  6 min and did not help: node-5 hosted both D's and F's Postgres (8 Gi limits each on ~14 Gi),
  so the kernel evicted the cache again.
- Fix: `kubectl cordon node-5; kubectl delete pod <D postgres>` → rescheduled on node-6, volume
  re-attached in 2 min; bootstrap restarted (DB unreachable ×4 during the move, expected) and
  redid the publish from the pre-lock staging; ingest state kept.
- Rules 1, 7, 9. Follow-ups: pod anti-affinity for Postgres in the chart (one per node);
  consider `random_page_cost` and `work_mem` in the Postgres config so the edge pass prefers a
  sequential scan + sort; a post-start `pg_prewarm` of the published tables for serving.

### 6. Timings observed (for the next estimate)

| step | D (node-4 runtime, node-5 → node-6 db) | F (node-6 runtime, node-5 db) |
|---|---|---|
| drain all 29 sources (git-history lanes are the long pole) | 1 h 35 | ~1 h 20 |
| pre-lock staging (`_eff_stage_prelock_*`) | ~13 min | ~12 min |
| counting (`counted 539,121 rows in okg.graph_nodes`, edges 185 s) | ~5 min | ~5 min |
| edge pass (`WITH branch AS …`) | > 1 h cold (abandoned), see §5 | fast (cache still warm) |
| attribute materialization + `snapshot_batch` | — | > 1 h 30 (slow disk) |

A build from an empty database is **3-4 h end to end on these volumes** when nothing goes
wrong; C's 40 min on corpus v0.1.0 (half the graph, no git history) is not the reference.

### 7. What "normal" looks like while watching (`scripts/instance-watch.sh`)

- `st`: pod `Init:2/5`, restart count not climbing, last log timestamp moving (git-history
  lanes go quiet for up to ~15 min), `publisher lines: 0` until the drain ends, then 4 (counting
  started), 6 (counted), more during the publish; `Init:3/5` → `2/2 Running` → `PUBLISHED:`.
- `cnt`: `_chronos_b_interval_okg_graph_{nodes,edges}_*` growing during the drain;
  `_eff_prelock_hash_{node,edge}` appearing at the start of the publish (their counts are the
  graph's final counts); `attribute_versions` / `attribute_effective_view` reaching
  nodes + edges during the materialization. `okg.graph_nodes` (the published view) is 0 until
  the first publish, by design.
- `pgact`: statement age and wait event. `IO/DataFileRead` is recorded on every data-file
  `read()`, cached or not; use `dio` to tell them apart.
- `dio`: per-volume MB/s and IOPS from `/proc/diskstats`. Tens of MB/s during sequential steps;
  near zero with a statement still active means it is served from cache (good); a few hundred
  KB/s at ~44 IOPS with no growth means starved (§5).
- Bad: restart count climbing (`--previous` log says why), `Init:` dropping below 2/5, or
  `cnt` unchanged across two readings 30 min apart during the drain.
