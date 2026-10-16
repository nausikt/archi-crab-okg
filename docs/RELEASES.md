# Releases: engine × corpus shipping (v0.16)

One **instance** per (engine, corpus) pair, built from scratch, frozen, deployed from an immutable
git **tag**, and served at a URL that names the pair. "Latest" URLs are **pointers** (thin
proxies), never a second instance. Prod has its own instance of the best pair (F).

## Where we are, and what is left (2026-10-16 20:45)

**Live on staging** (`archi-crab-okg-staging.cern.ch`, `archi-crab-v2.cern.ch`), all deployed from
tags or merge commits, never `main`:

| Instance | Engine | Corpus | URL | State |
|---|---|---|---|---|
| A | okg `43f459c6` (v4 dev, 3d6cb3e8) | `v0.1.0` | `/releases/43f459c6/v0.1.0/mcp` (+ `/mcp` pointer) | live, frozen (gen `eee6c09f3655`, 326,241 / 419,177) |
| C | okg `v0.2.0-rc1` (06a4771) + archi-okg e1c2886 | `v0.1.0` | `/releases/v0.2.0-rc1/v0.1.0/mcp` | published 2026-10-16 (gen `dbc96e1b4a8d`, 326,419 / 419,367) → freeze (below) |
| v2 | archi `e6609f8f` | `v0.1.0` | `/{grep,vectorstore}/releases/v0.1.0/mcp` (+ pointers) | live |

- run1 is retired.
- A and C share their corpus and adapter (fingerprints `3d37187c…` and `46227d04…`); only the
  engine differs.
- The ToolHive operator is up until C is frozen.
- `okg status` on a FROZEN instance exits 1 with `permission denied for table node_facts`. Only
  the `mcp` container runs, with the read-only role. `publishing` and `database_readiness` still
  report; `stage` and `sources` don't. Capture a full status before freezing.

**Left for corpus v0.1.0: freezing C.** The patches are ready: `archi-crab-okg-6-freeze-c` and
`CMSKubernetes-4-freeze-c`.
1. Wait for C's `bootstrap` to finish its first publish, then save both status files:
   ```bash
   kubectl -n archi-crab-staging exec archi-crab-okg-v0-2-0-rc1-v0-1-0-runtime-0 -c mcp -- okg status --deployment archi-crab --json > C.status.json
   kubectl -n archi-crab-staging exec archi-crab-okg-staging-runtime-0 -c mcp -- okg status --deployment archi-crab --json > A.status.json
   ```
2. Merge `freeze-c` (`[skip ci]` in the merge title is fine; its PR CI checks C's values).
   Then tag the merge commit:
   ```bash
   git fetch origin && M2=$(git rev-parse origin/main)    # AFTER the merge
   git show $M2:releases/matrix.yaml | grep -A2 'engine: v0.2.0-rc1' | grep -q 'status: live' && echo "M2 is the freeze merge"
   git tag -a okg/releases/v0.2.0-rc1/v0.1.0 "$M2" -m "okg C: engine v0.2.0-rc1 x corpus v0.1.0, frozen"
   git push origin okg/releases/v0.2.0-rc1/v0.1.0 && python3 scripts/release.py lint --tags
   ```
3. Merge `CMSKubernetes-4-freeze-c`. It moves C's app to that tag and sets the operator to 0.
   ```bash
   kubectl -n argocd annotate application archi-crab argocd.argoproj.io/refresh=hard --overwrite
   kubectl -n argocd annotate application archi-crab-okg-v0-2-0-rc1-v0-1-0 argocd.argoproj.io/refresh=hard --overwrite
   kubectl -n archi-crab-staging delete pod archi-crab-okg-v0-2-0-rc1-v0-1-0-runtime-0   # StatefulSets don't roll an unready pod
   kubectl -n archi-crab-staging get pod archi-crab-okg-v0-2-0-rc1-v0-1-0-runtime-0 -w   # 1/1, mcp only
   ```
4. Bench: A vs C (and v2). Add each URL with
   `--client-id archi-crab-okg-public-staging --callback-port 8765`, and record runs by okg commit.
5. Optional: put the counts from step 1 and v2's data-manager counts into `releases/corpus.yaml`
   (`materialized`), in any later PR.

**Engine track** (nothing blocks the bench):
- Do **not** merge the `engine/upstream` PR. The tag `engine/v0.2.0-rc1` holds the rc1 build,
  and the daily run moves that branch back to okg `dev`.
- After 2026-10-17 (v0.2.0 is public):
  - patch `archi-crab-okg-2-okg-release-engine` (release tags and wheel installs);
  - then `versions.lock` `track: release`;
  - a new engine is a new id in `engines.yaml` (`v0.2.0`, …), built and tagged like rc1.
- Housekeeping:
  - accept okg's chart PR (deltas 10, 11, 13);
  - drop the okg pull secret and token only once our images are public;
  - add a CI contract check for `deployments/compat/43f459c6` in image `edfe5cad`;
  - retire `main.yaml`'s staging pin and `promote.yaml`;
  - pin `runs-on: ubuntu-24.04` (`ubuntu-latest` becomes Ubuntu 26 on 2026-10-19).

**Corpus v0.2.0-rc1** (the next real step: B, D, F, v2 `v0.2.0-rc1`). It starts when your sources
list and docs exist. Prerequisites:
- de-hardcode the v2 chart's Service names (a second v2 release in the same namespace);
- prod F: certificate, LanDB alias and gateway listener for `archi-crab-okg.cern.ch`; a prod SSO
  app; Secret `okg-archi-crab` in `archi-crab`; StorageClass `cinder-io1`;
- decide on `cmssw-releases`. It needs okg#3317 + archi-okg#32 (archi-okg `e1c2886` has #32;
  check okg#3317 is in the engine). Exclude it for 43f459c6 in
  `deployments/compat/43f459c6/compat.yaml`.

Then phase 2 below:
1. the corpus PR, then the `corpus/v0.2.0-rc1` tag;
2. B (43f459c6, compat adapter);
3. D and F back to back;
4. v2 `v0.2.0-rc1`;
5. flip the pointers (staging `/mcp` → D, v2 → `v0.2.0-rc1`).

**Not ours, still open:**
- The master node has been NotReady since 2026-10-05 (CERN Cloud ticket).
- Prod `crab-mcp-gateway` is OutOfSync / Degraded, and `archi-crab-otel-collector` is Degraded.
  Both predate this work.

The truth is in `releases/` and `scripts/release.py` checks it:

| File | Says |
|---|---|
| `releases/corpus.yaml` | corpus versions: tag, commit, fingerprint of `sources/archi-crab.yaml` + `deployments/archi-crab/data/` |
| `releases/engines.yaml` | engine ids → image digests (okg runtime + postgres; archi v2 images) |
| `releases/matrix.yaml` | every instance and pointer: status, URL, names, ClusterIP, volumes |

```bash
python3 scripts/release.py show            # URL -> instance -> status
python3 scripts/release.py lint [--tags]   # pins, fingerprints, names, pointers (+ git tags)
python3 scripts/release.py budget          # Cinder volumes per type
python3 scripts/release.py fingerprint REV # corpus fingerprint of any commit
python3 scripts/release.py render okg:<engine>/<corpus> --revision REV   # a new instance's values
python3 scripts/release.py iac okg:<engine>/<corpus> [--target SHA]      # its Argo app + proxy entry
```

## The matrix

**okg, staging** (`archi-crab-okg-staging.cern.ch`)

| engine ↓ · corpus → | `v0.1.0` | `v0.2.0-rc1` |
|---|---|---|
| `43f459c6` (okg v4, 2026-10-06) | **A** `/releases/43f459c6/v0.1.0/mcp` (live) | **B** `/releases/43f459c6/v0.2.0-rc1/mcp` (later) |
| `v0.2.0-rc1` (okg release candidate) | **C** `/releases/v0.2.0-rc1/v0.1.0/mcp` (**this weekend**) | **D** `/releases/v0.2.0-rc1/v0.2.0-rc1/mcp` (later) |

- `/mcp` points at A; later it points at D.
- `/run1/mcp` (okg v3, the 2026-10-01 evaluation) is **retired** in phase 0. Its app, proxy,
  volumes and Secret are deleted; the tag `okg-run1` stays as the record.

**okg, prod:** `archi-crab-okg.cern.ch/mcp` serves **F**. F is its own instance of D's pair
(engine `v0.2.0-rc1` × corpus `v0.2.0-rc1`), in namespace `archi-crab`. It comes later.

**archi v2, staging** (`archi-crab-v2.cern.ch`; engine `archi-e6609f8f` for both)

| corpus | grep | vectorstore |
|---|---|---|
| `v0.1.0` (live) | `/grep/releases/v0.1.0/mcp` | `/vectorstore/releases/v0.1.0/mcp` |
| `v0.2.0-rc1` (later) | `/grep/releases/v0.2.0-rc1/mcp` | `/vectorstore/releases/v0.2.0-rc1/mcp` |

`/grep/mcp` and `/vectorstore/mcp` point at `v0.1.0`; later they point at `v0.2.0-rc1`.

**Volumes:**
- A and v2 `v0.1.0` predate the layout and hold 2 io1 each.
- Every new instance (B, C, D, F, v2 `v0.2.0-rc1`) adds 1 io1 (database) + 1 standard
  (build checkout or raw files). That is 5 + 5 new.
- Quota checked on 2026-10-16: 15 volumes left overall, 8 io1 and 7 standard. Retiring run1
  returns 2 io1, which makes 17 overall and 10 io1.

## Rules

1. **Never rename a live instance.** Its release name names its volumes, and both storage
   classes delete a volume with its claim.
2. **A deploy tag is immutable** and names a frozen instance. While an instance is building,
   its Argo app points at a merge sha. Once it is frozen, the app points at the tag.
3. **A corpus tag pins the source list, not the bytes.** Git sources are cloned at branch HEAD
   when an instance is built. Build twins (D and F) back to back. For cross-day comparisons
   (C vs A), record each instance's per-source revisions.
4. **An instance = engine adapter + corpus, at one commit.** Its `repositorySync.revision` must
   carry its corpus's files (fingerprint) and its engine's adapter, native or compat (see
   "Engine adapters"). `release.py lint` checks both. `render` picks the adapter path.
5. **Nothing deploys from `main`.** The engine bot's staging pin (`envs/staging`, `v2/envs/bench`)
   no longer reaches anything once phase 0 is done.

## Engine adapters: old and new engines on one `main`

The corpus contract can change with the engine. A newer okg may need other `kinds.yaml`
renders, other registry keys, other vendored schemas or skills, and `cmssw-releases` needs
okg#3317. So each okg engine in the matrix has an **adapter**:
- `sources/kinds.yaml`;
- `deployments/archi-crab/` apart from `data/` (the corpus), `source_registry.yaml` (rendered)
  and `VENDOR.yaml`.

`releases/engines.yaml` records its fingerprint.

| Where | Holds | Used by |
|---|---|---|
| `deployments/` (native) | the adapter `main` currently speaks: the engine the bot follows | new instances of that engine |
| `deployments/compat/43f459c6/` | **43f459c6's adapter, frozen** (byte copies from 43f459c6): `kinds.yaml`; `archi-crab/` with deployment, extractors, invariants, schemas, skills; `data` → symlink to the live corpus; its own `source_registry.yaml` (the CURRENT source list rendered with ITS kinds, by `sources.py render --write`, checked by CI); `compat.yaml` | B, and any later 43f459c6 × newer-corpus instance |

- An instance selects its adapter with `okg.deploymentsPath` (chart delta 12, default
  `deployments`). The chart then sets `OKG_DEPLOYMENTS_DIR` to that path in the checkout.
- A never needed one: its revision is 43f459c6 itself, where `deployments/` is native.
- **Sources an old engine cannot ingest** go under `exclude:` in its `compat.yaml` (e.g.
  `cmssw-releases: needs okg#3317`). They are left out of that engine's render only, and
  `release.py lint` reports them for every instance that uses the adapter (B = corpus minus
  those).
- **When `main`'s adapter moves on** (an engine PR resyncs vendored files, `kinds.yaml` changes)
  and an older engine is still wanted, freeze it first:
  `release.py freeze-adapter <engine> <its commit>`, then `sources.py render --write`, then
  record `adapter.compat` and `adapter.fingerprint` in `engines.yaml`.
- Retire a compat dir with its last instance.
- Follow-up (a workflow change, not in these PRs): a CI job that runs `contract-check.py` inside
  each compat engine's image (43f459c6 = `edfe5cad`) against its compat deployment. A corpus
  change that the old engine cannot read then fails the PR, instead of failing B's build.

```bash
python3 scripts/release.py adapter 43f459c6 HEAD    # native vs compat fingerprints, and which one matches
```

---

## Phase 0: corpus v0.1.0, with A and v2 on tags (no new volumes)

**0.1 Freeze A.** Merge PR #26 (`freeze-both`), with `[skip ci]` in the merge commit title.
A's app still follows `main`, so it syncs `frozen.enabled: true`. (#26's run1 half no longer
matters: run1 is retired, and its tag is not moved.)

**0.2 Releases PR** (`releases-v0.1.0`). What it changes:
- It adds `releases/`, `envs/releases/`, `v2/envs/releases/`, `deployments/compat/43f459c6/`,
  `scripts/release.py` and this doc.
- It adds chart delta 12 (default render unchanged) and teaches `sources.py` the compat render.
- It removes `envs/run1`.
- **It edits `ci.yaml`**, so pushing it needs a token with the `workflow` scope. CI's run1
  checks move to the release instances, and `release.py lint` joins CI. After #26, CI's old
  "staging keeps bootstrap and worker" check would fail on the now-frozen staging; this PR
  fixes that too.

Nothing deployed reads the new files yet. Merge it with `[skip ci]` in the merge commit title.
A push to `main` that touches `envs/**` or `scripts/**` runs `main.yaml`, and a green e2e
there would re-pin `envs/staging`, which A still follows until 0.4.

**0.3 Cut the tags** (annotated, from a fresh clone of `main`):
```bash
git fetch origin --tags && M=$(git rev-parse origin/main)
git tag -a corpus/v0.1.0 43f459c6bceac6bd26376d8d1db5a89fdd697da1 \
  -m "corpus v0.1.0: sources/archi-crab.yaml + deployments/archi-crab/data (sha256:3d37187c...)"
git tag -a okg/releases/43f459c6/v0.1.0 "$M" -m "okg A: engine 43f459c6 x corpus v0.1.0, frozen"
git tag -a v2/releases/v0.1.0 "$M" -m "archi v2: engine archi-e6609f8f x corpus v0.1.0"
git push origin corpus/v0.1.0 okg/releases/43f459c6/v0.1.0 v2/releases/v0.1.0
python3 scripts/release.py lint --tags        # 0 errors
```

**0.4 IaC PR** (CMSKubernetes `releases-v0.1.0`):
- A's and v2's apps move to their tags and release-path value files.
- Three release-path proxies are added.
- **run1 is removed:** its Application (`47-okg-run1-app.yaml`), its proxy `okg-run1`, and the
  disabled run2 placeholders.
- The ToolHive operator runs (`replicaCount: 1`). Proxy deletions need it too, for their
  finalizers.

When it merges, the root app prunes run1's Application, and the Application's finalizer
deletes run1's StatefulSets, Services and ConfigMap. Then wait:
```bash
kubectl -n argocd get application archi-crab-okg-staging archi-v2 \
  -o custom-columns=NAME:.metadata.name,REV:.status.sync.revision,SYNC:.status.sync.status,HEALTH:.status.health.status
kubectl -n archi-crab-staging get mcpremoteproxy    # okg-43f459c6-v0-1-0-staging, v2-*-v0-1-0-staging Ready; okg-run1 gone
kubectl -n argocd get application archi-crab-okg-run1   # NotFound
```
Then merge the follow-up (`releases-v0.1.0-done`: operator back to 0).

**0.4b Reclaim run1's volumes** (irreversible: the okg v3 evaluation database goes). A
StatefulSet's claims are not Argo's, so they outlive the app. Delete them by hand. The
`cinder-io1-delete` class then deletes the Cinder volumes.
```bash
kubectl -n archi-crab-staging get statefulset,pod,svc | grep -- '-run1-' || echo "run1 workloads gone"
kubectl -n archi-crab-staging get pvc | grep -- '-archi-crab-okg-run1-'      # 2 claims: postgres + runtime
kubectl -n archi-crab-staging get pvc -o name | grep -- '-archi-crab-okg-run1-' \
  | xargs kubectl -n archi-crab-staging delete
kubectl get pv | grep -- '-archi-crab-okg-run1-' || echo "PVs gone"
kubectl -n archi-crab-staging delete secret okg-archi-crab-run1
openstack volume list --long -c Name -c Type -c Status -f value | grep -c io1   # 2 fewer than before
```
`okg-run1` (tag) and `docs/RUN1-FREEZE.md` stay as the record. A rebuild from them is possible,
but it would hold today's sources, not the 2026-10-01 snapshot.

**0.5 Verify.**
```bash
for u in archi-crab-okg-staging.cern.ch/.well-known/oauth-protected-resource/releases/43f459c6/v0.1.0/mcp \
         archi-crab-v2.cern.ch/.well-known/oauth-protected-resource/grep/releases/v0.1.0/mcp \
         archi-crab-v2.cern.ch/.well-known/oauth-protected-resource/vectorstore/releases/v0.1.0/mcp; do
  curl -s "https://$u" | jq -r .resource; done              # each = the URL it describes
# Every release URL takes the PRE-REGISTERED public PKCE client (redirect http://localhost:8765/callback).
# Without --client-id, Claude Code tries dynamic client registration, which CERN SSO refuses
# (403 "Policy 'Allowed Client Scopes' rejected request to client-registration service").
claude mcp add --transport http okg-A https://archi-crab-okg-staging.cern.ch/releases/43f459c6/v0.1.0/mcp \
  --client-id archi-crab-okg-public-staging --callback-port 8765
claude mcp add --transport http v2-grep-v010 https://archi-crab-v2.cern.ch/grep/releases/v0.1.0/mcp \
  --client-id archi-crab-okg-public-staging --callback-port 8765
```
A route answers `ECONNRESET` for its first seconds, until the gateway programs it; retry before
debugging.
- The release path and its pointer must list the same tools (same backend).
- `query` must still be refused.
- Record v2's counts in `corpus.yaml` (`materialized`), using the data-manager queries from
  `docs/V2-BENCH.md`.

---

## Phase 1: engine v0.2.0-rc1 and C, for the weekend bench (A vs C)

okg `v0.2.0-rc1` has **no published image**, so its engine is built **the way 43f459c6's was**:
- okg's dev image for that commit (`ghcr.io/mitdbg/okg:sha-<commit>` + `okg-postgres:sha-<commit>`);
- plus our `docker/runtime/Dockerfile` (`/opt/okg/.git` at the commit, the editable install,
  archi-okg).

This uses the existing `engine` workflow and its `okg_commit` input. No PR is needed, and the
release-tag PR (`okg-release-engine`) waits for v0.2.0's public images (see "Converging").

**1.1 What `v0.2.0-rc1` is, and whether it can be built.**
- It is commit **`06a4771`**, a pre-release that okg calls "the fixed version for benchmarks:
  results on this tag compare with each other".
- No package or image is published, and okg reports version `0.1.0` inside, so runs are
  recorded **by commit**.
- "1964 commits to dev since this release" at about 100 merges a day means it may be **older
  than A's okg `3d6cb3e8`** (2026-10-06). Check before reading the bench as "newer vs older".
```bash
git ls-remote https://x-access-token:$OKG_PAT@github.com/mitdbg/okg 'refs/tags/v0.2.0-rc1*'   # full sha (the ^{} line)
R=<that full sha>
docker buildx imagetools inspect ghcr.io/mitdbg/okg:sha-$R            # MUST exist
docker buildx imagetools inspect ghcr.io/mitdbg/okg-postgres:sha-$R   # MUST exist
# in a clone of mitdbg/okg:
git log -1 --format='%ci %s' $R
git merge-base --is-ancestor $R 3d6cb3e8 && echo "rc1 is OLDER than A's engine" || echo "rc1 is newer (or on a branch)"
```
- If a `sha-` image is missing, there is no base to build on. Use `v0.2.0` (public on 2026-10-17,
  with release images) instead.
- okg reviewed archi-crab-okg against v0.2.0, not rc1. The contract report of the build (1.2) is
  the rc1 check.
- Ask okg which archi-okg commit they pair with rc1. The bot builds with archi-okg `main`
  (`e1c28860` on 2026-10-16).

**1.2 Build the engine.** Build C before any corpus v0.2.0-rc1 change lands on `main`: the
engine branch merges `main` forward, and C needs corpus v0.1.0.
1. Go to Actions → **engine** → Run workflow, with `okg_commit: <R>`, `archi_commit:` (the pair,
   or empty for archi-okg `main`), and `force: true`.
2. The resolver pins the `sha-<R>` pair. The Dockerfile then builds our runtime image, tagged
   `okg-<R:9>-archi-<sha:9>`.
3. The rolling PR `engine/upstream` gets the commit "engine: okg <R> + archi-okg …", plus a
   contract report and e2e. Read the contract report: it is the compatibility check.
```bash
git fetch origin engine/upstream && git log -3 --format='%h %s' origin/engine/upstream
git show origin/engine/upstream:versions.lock | yq '.upstream.commit, .archi.commit, .images, .runtime.digest'
```

**1.3 Tag it right away.** The next daily run (03:17 UTC) moves `engine/upstream` back to okg
`dev`. The tag keeps the rc1 build and its adapter (C's knowledge revision):
```bash
git tag -a engine/v0.2.0-rc1 origin/engine/upstream -m "archi-crab engine okg v0.2.0-rc1 (06a4771) + archi-okg <sha>"
git push origin engine/v0.2.0-rc1
python3 scripts/release.py fingerprint engine/v0.2.0-rc1          # MUST print corpus v0.1.0's sha256:3d37187c...
python3 scripts/release.py adapter v0.2.0-rc1 engine/v0.2.0-rc1   # its native adapter fingerprint (for 1.4)
```
If the corpus fingerprint differs, the build changed `sources/archi-crab.yaml` (a converge
commit), so C would not be corpus v0.1.0. Stop and look.

**1.4 Release PR for C** (on `main`):
- `releases/engines.yaml` `v0.2.0-rc1`:
  - `status: released`;
  - `okg`, `archi_okg`, `runtime.digest` and `postgres.digest` from
    `git show engine/v0.2.0-rc1:versions.lock`;
  - `adapter.native: <engine/v0.2.0-rc1's commit>`, and `adapter.fingerprint` from 1.3.
- `releases/matrix.yaml`: C `status: building`.
- Then:
```bash
python3 scripts/release.py render okg:v0.2.0-rc1/v0.1.0 --revision engine/v0.2.0-rc1
python3 scripts/release.py lint
```
Merge it, and call the merge sha `M1`.

**1.5 Cluster preparation** (namespace `archi-crab-staging`):
```bash
kubectl get svc -A -o jsonpath='{range .items[*]}{.spec.clusterIP}{"\n"}{end}' | grep -qx 10.254.0.203 && echo TAKEN || echo free
scripts/okg-run-secret.sh v0-2-0-rc1-v0-1-0      # -> Secret okg-archi-crab-v0-2-0-rc1-v0-1-0, DSN host = its own Postgres
# okg review item 4: the writer DSN must not be app_rw (fresh v0.2 databases create it without login)
kubectl -n archi-crab-staging get secret okg-archi-crab-v0-2-0-rc1-v0-1-0 -o jsonpath='{.data.okg-dsn}' \
  | base64 -d | grep -oE '^[a-z+]+://[^:@/]+|user=[^ ]+' | sed -E 's#^[a-z+]+://#user=#'   # expect user=postgres
```

**1.6 IaC PR for C.**
```bash
python3 scripts/release.py iac okg:v0.2.0-rc1/v0.1.0 --target "$M1"
```
1. Paste the app as `argocd/archi-crab/staging/48-archi-crab-okg-v0-2-0-rc1-v0-1-0-app.yaml`.
2. Paste the proxy entry under `remoteProxies` (after `okg-43f459c6-v0-1-0`).
3. Set the operator `replicaCount: 1`.
4. Merge.

**1.7 Watch the build.** It's one instance, on worker nodes only:
```bash
kubectl -n archi-crab-staging get pods,pvc | grep v0-2-0-rc1-v0-1-0
P=archi-crab-okg-v0-2-0-rc1-v0-1-0-runtime-0   # init: repository-sync, catalog-claim, bootstrap, runtime-bootstrap, mcp-role
kubectl -n archi-crab-staging logs $P -c bootstrap -f
kubectl -n archi-crab-staging exec $P -c mcp -- okg status --deployment archi-crab --json > C.status.json
kubectl -n archi-crab-staging exec archi-crab-okg-staging-runtime-0 -c mcp -- okg status --deployment archi-crab --json > A.status.json
```
- Done when the first generation is published.
- Then compare the two status files: generation id, node and edge counts, and per-source
  revisions (the git drift between 2026-10-06 and today).

**1.8 Freeze C.**
1. PR: in its values, `frozen.enabled: true`; in the matrix, C `status: live`. Run
   `release.py lint`. Merge, and call the merge sha `M2`.
2. Tag it:
```bash
git tag -a okg/releases/v0.2.0-rc1/v0.1.0 "$M2" -m "okg C: engine v0.2.0-rc1 x corpus v0.1.0, frozen"
git push origin okg/releases/v0.2.0-rc1/v0.1.0 && python3 scripts/release.py lint --tags
```
3. IaC PR: C's app `targetRevision` becomes the tag, and the operator goes back to 0.
4. Record C's counts in `corpus.yaml`.

**Bench endpoints** (each added with `--client-id archi-crab-okg-public-staging --callback-port 8765`):
- A: `.../releases/43f459c6/v0.1.0/mcp`
- C: `.../releases/v0.2.0-rc1/v0.1.0/mcp`
- v2: `archi-crab-v2.cern.ch/{grep,vectorstore}/releases/v0.1.0/mcp`

**Fallback:** if rc1 cannot be built in time, use `okg_track: v0.2.0` (public on 2026-10-17)
and engine id `v0.2.0`.

---

## Phase 2: corpus v0.2.0-rc1 (B, D, F, v2), later

Prerequisites:
- Phase 0 is done (A and v2 on tags).
- The v2 chart has its Service names de-hardcoded, so a second release can share the namespace.
- Prod for F:
  - a host cert and LanDB alias for `archi-crab-okg.cern.ch`, and its gateway listener;
  - a prod SSO app;
  - a Secret in `archi-crab`;
  - a prod Argo app and gateway proxy;
  - StorageClass `cinder-io1`.

1. **Assemble the corpus** on `main`: `sources/archi-crab.yaml` and `deployments/archi-crab/data/`.
   - `cmssw-releases` can come back: it needs okg#3317 and archi-okg#32 in the NEW engine.
   - For engine 43f459c6, add it to `deployments/compat/43f459c6/compat.yaml` under `exclude:`.
     B then ingests the corpus without it, and lint says so.
   - In the same PR: if `main`'s native adapter moved past an engine still in use, freeze that
     engine's adapter (`release.py freeze-adapter`).
   - Run `sources.py render --write`, which writes every registry, native and compat.
2. **Cut `corpus/v0.2.0-rc1`** at the merge. Fill `corpus.yaml` (`release.py fingerprint`).
3. **Revisions:** every new instance can use the corpus commit itself.
   `release.py render <id> --revision corpus/v0.2.0-rc1` picks the adapter:
   - B (43f459c6) → `deploymentsPath: deployments/compat/43f459c6`;
   - D and F → `deployments` if `main`'s native adapter is v0.2.0-rc1's. Otherwise use
     `--revision engine/v0.2.0-rc1` with the corpus files merged in.
4. **Build in this order:**
   - B (validates the corpus on a known engine);
   - D and F back to back (twins);
   - v2 `v0.2.0-rc1`.

   Each follows steps 1.4 to 1.8 (`render`, `iac`, build, freeze, tag).
5. **Flip the pointers** (CMSKubernetes `url:` lines, `matrix.yaml` `target:`):
   - staging `/mcp` goes to D;
   - `/grep/mcp` and `/vectorstore/mcp` go to v2 `v0.2.0-rc1`.

---

## Converging on okg v0.2.0 (okg's review, 2026-10-16)

| # | okg item | Our change | PR | When |
|---|---|---|---|---|
| 1 | Public tagged release images (verified wheel) | `install: wheel`: no `/opt/okg/.git`, no okg token, no editable install. The build fails if archi touches `site-packages/okg`. Not needed for rc1 (no images; built the existing way). | `okg-release-engine` | after 10-17, with v0.2.0's images |
| 1 | …then drop `ghcr-mitdbg-pull`, `OKG_PAT`, private runtime image | Only once **our** images are public too: v2's `nausikt` images use the same pull secret. | later | after 10-17 |
| 2 | Weekly release tags, not `dev` | Resolver `track: release` / `vX.Y.Z[-rcN]`. Set main to `track: release` after the bench. | `okg-release-engine` | after 10-17 |
| 3 | `--profile` becomes `--checks` | Chart `okg.readinessChecks` (helper `okg.readyFlags`). e2e and contract-check already pass no flag. | `okg-ready-checks` | any time: instances deploy from tags |
| 4 | Roles start without login | Writer DSN is `postgres`, not `app_rw` (checked in step 1.5). `okg_mcp` is handled by `mcp-role`. Nothing to change. For prod, consider a non-superuser writer. | — | — |
| 5 | Unknown registry keys refused | Our registry passes. `sources.py lint` keeps it so. | — | — |
| 6 | DSNs on the command line warn | We pass DSNs through env. | — | — |
| 7 | `cmssw-releases` can come back | Needs okg#3317 and archi-okg#32 in the engine. It goes into corpus v0.2.0-rc1; engine 43f459c6's compat adapter excludes it (B ingests the rest). | corpus PR | phase 2 |
| — | Use okg's chart, not a copy (VENDOR-TODO) | Accept okg's offered PR after 10-17. Ask them to carry our deltas: 10 frozen mode, 11 fixed ClusterIP, 13 `readyFlags`. | okg's PR | after 10-17 |

**Order.**
1. Phase 0: #26, then releases, then tags, then IaC (which also retires run1), then the run1
   volumes.
2. Phase 1 needs no PR until C's release PR (1.4).
3. `okg-ready-checks` is based on the releases PR (both touch the chart's `okg:` values) and can
   merge any time after 0.4.
4. `okg-release-engine` waits for v0.2.0's public images (after 2026-10-17). Once A and v2 deploy from
tags, no merge to `main` (the bot's pins included) can move what the bench runs. Before 0.4, a
merge that triggers `main.yaml` could still re-pin A.

`promote.yaml` (copy staging's pins into `envs/prod`) is superseded. Prod F is rendered like
any instance (`release.py render prod:...`), so retire the workflow in phase 2.
