# archi-crab — Runbook v0.5.0 (MVP)

Everything in one document: what OKG is (§1), what this repo contains (§2),
the six phases to a working prod (§3), the standing rules (§4), and the
persistence footnotes F1–F5 you must understand before the first sync (§5).
Every phase ends with a **Verify**; red means stop.

Pinned engine: upstream `mitdbg/okg@bed964f` — both images cut from that one
commit (`versions.lock`). Date of this revision: 2026-09-20.

---

## §1 Summary — what you are deploying

**OKG is three things on Postgres.** A **graph inside a database** (nodes:
files, symbols, doc chunks, releases; edges: contains, member_of,
supersedes) read through `okg.v_nodes` / `okg.v_edges`, written only in
**generations** — immutable published snapshots, so readers never see a
half-ingested state. **Connectors** that fill it deterministically (clone,
parse, chunk, hash, diff, publish) under a **catalog** contract (LinkML
schemas + registry) — no LLM anywhere in ingestion; "knowledge distillation"
is connectors + schemas + the completeness gate. An **MCP server**
(`okg mcp-serve`, streamable-http) exposing six read operators — search,
inspect, expand, filter, map, aggregate — over the published generation via
a read-only role. Any MCP client (Claude Code, Open WebUI through your vMCP)
consumes it; the LLM is a *client*, chosen at chat time, never a dependency.

**The Helm chart** runs it as one runtime StatefulSet — init containers in
order `repository-sync → bootstrap (okg provision --publish-once) →
runtime-bootstrap → mcp-role`, then two long-running containers `worker` and
`mcp` — plus an internal Postgres StatefulSet (TimescaleDB + pg_textsearch +
pgvector). Argo CD syncs it from **this repo**, per environment, from
`envs/<env>/values.yaml`.

**This repo is the instance**: pure declaration (which connectors, which
schemas, which modules, which skills). Zero code. Zero builds. CI proves the
knowledge publishes, the invariant holds, and the deployment serves — never
okg's own code.

**Decisions on record** (each argued earlier; here for the reader who wasn't):
single branch `main`, environments by path; upstream images only, pinned by
digest; two secrets in GitHub (`GHCR_PAT` temporary, `STAGING_BUMP_TOKEN`);
GitHub-hosted runners only, no mirror, no self-hosted runner; minimal sources
(CRABServer, CRABClient, cmssw_releases) — *public*, so the full e2e runs in
CI with no CERN credential; git-history excluded (upstream race); chat via
the platform's Open WebUI + vMCP, not okg's chat machinery; MCP exposed only
through the vMCP (`query` denied to chat/public audiences).

**Known upstream defects you are designing around** (field guide, 2026-09):
retraction does not work (`missing_from_completed_scope` never retracts) →
identity changes mean rebuild, not reconcile; git-files/git-history race →
git-history is manual-only; `okg install` exits 0 on failed publish → assert
status, never exit codes; the seven code modules must land together or
publish drowns in ~618k consistency violations; app_rw/app_ro may be created
NOLOGIN → chart delta 4 if bootstrap hits an auth error.

---

## §2 Skeleton — what is in the tarball and what each file is for

```
archi-crab-okg/
├── VERSION  versions.lock  README.md  CODEOWNERS  .yamllint.yaml  .gitignore
├── .github/
│   ├── dependabot.yml                 # bumps SHA-pinned actions weekly
│   └── workflows/
│       ├── ci.yaml                    # PR+main: guards → lint → kubeconform → okg-validate
│       ├── main.yaml                  # main: e2e-smoke → bot bumps envs/staging pins
│       └── promote.yaml               # manual, prod-env gated, pins-only PR
├── deployments/archi-crab/                    # THE INSTANCE
│   ├── deployment.yaml                # 12 modules · dangling prune · runtime on · chat off
│   ├── source_registry.yaml           # code_repos{crabserver,crabclient} + cmssw_releases
│   ├── invariants.yaml                # floor: source_file, code_symbol, document_chunk, cmssw_release
│   ├── extractors.yaml.TODO           # ← copy real file from image (Phase 2.3); CI fails until done
│   ├── schemas/operations.yaml        # archi HEP vocabulary (verbatim)
│   ├── schemas/sources.yaml           # archi source subtypes (verbatim)
│   ├── schemas/bridges/README.md      # ← copy + prune bridges (Phase 2.4); CI fails until done
│   ├── skills/*.md + skill-triggers.yaml   # 20 playbooks, materialized
│   └── data/.gitkeep                  # connector caches live on the PVC, not in git (F1)
├── helm/okg/
│   ├── Chart.yaml  values.schema.json # schema verbatim from the working chart
│   ├── values.yaml                    # RECONSTRUCTED from schema — diff vs original (Phase 2.2)
│   ├── VENDOR-TODO.md                 # ← missing files + 4 deltas; CI fails until deleted
│   └── templates/*.yaml               # the six okg templates available verbatim
├── envs/staging/values.yaml           # overrides: digests, storage, pins (CI-bumped)
├── envs/prod/values.yaml              # same shape; Promote-PR-only
├── scripts/smoke.sh                   # CI e2e step == Argo PostSync hook body
└── docs/RUNBOOK-v0.5.0.md             # this file
```

**Four guard files** make CI red until the tarball is *completed* rather
than merely pushed: `extractors.yaml.TODO`, `schemas/bridges/README.md`,
`helm/okg/VENDOR-TODO.md`, and any `REPLACE_ME` in `envs/` or
`deployment.yaml`. They are forcing functions, not decoration.

**Pin taxonomy** (all four live in `envs/*/values.yaml`, nowhere else):

| Pin | Path | Moves how |
|---|---|---|
| engine | `images.okg.digest` | engine-bump PR (with `versions.lock`) |
| engine | `postgresql.image.digest` | engine-bump PR |
| knowledge | `repositorySync.revision` | bot, on green `main.yaml` |
| knowledge | `bootstrap.approvedRevision` | bot (chart enforces == revision) |

Prod receives all four only via the Promote PR.

---

## §3 Phases

### Phase 0 — Access & pins (½ day; start SSO/DNS requests in parallel)

1. `echo $GHCR_PAT | docker login ghcr.io -u nausikt --password-stdin`
2. Pull both pinned images and confirm the digests in `versions.lock`:
   ```bash
   docker pull ghcr.io/mitdbg/okg@sha256:5a825f73c8929d2153859d95bfaf4c6f4ae01f02d08477583a7af05131826705
   docker pull ghcr.io/mitdbg/okg-postgres@sha256:75845f96d973859c248f0f6741cb0a06445e9d312e563de7a39c5e25f3236616
   ```
3. Sanity the engine — the whole no-build design rests on archi being inside:
   ```bash
   IMG=ghcr.io/mitdbg/okg@sha256:5a825f73c8929d2153859d95bfaf4c6f4ae01f02d08477583a7af05131826705
   docker run --rm $IMG --help
   docker run --rm --entrypoint python $IMG -c "import archi, okg; print('ok')"
   ```
4. `tar xzf archi-crab-okg-skeleton-v0.5.0.tar.gz && cd archi-crab-okg && git init -b main`

**Verify 0** — both pulls succeed; `okg --help` prints; archi import prints
`ok`. (Import failure = talk to upstream before anything else.)

### Phase 1 — In-cluster secrets (Vault → VSO, both namespaces)

For `archi-crab-staging` and `archi-crab`:
- `okg-archi-crab` with keys `postgres-password, okg-dsn, mcp-dsn,
  mcp-password, git-token` (DSNs point at `<release>-postgres:5432/okg`;
  `git-token` = read-only fine-grained PAT on this repo — temporary).
- `ghcr-mitdbg-pull` (`kubernetes.io/dockerconfigjson` from `GHCR_PAT`) — temporary.
- Register this repo's read credential in Argo CD repo-creds (private-repo period).

**Verify 1** — `kubectl -n <ns> get secret okg-archi-crab -o jsonpath='{.data}' | jq keys`
shows five keys in both namespaces; Argo UI browses the repo.

### Phase 2 — Complete the tarball, then ONE local end-to-end (1 day)

Do these in order; each clears a CI guard.

1. **Placeholders**: `deployment.yaml` nomos contact; `envs/*` storageClassName
   (`kubectl get storageclass` on the target cluster).
2. **Vendor copy** (`helm/okg/VENDOR-TODO.md`): copy `_helpers.tpl`,
   `networkpolicy.yaml`, `tests/`, and diff the reconstructed `values.yaml`
   against the original working chart's — keep upstream defaults except the
   four deliberate deltas. Resolve how `okg.commonEnv` derives
   `OKG_DEPLOYMENTS_DIR` from `repoRoot` (this repo uses `deployments/archi-crab/`).
   Apply deltas as separate commits. Delete `VENDOR-TODO.md`.
3. **extractors.yaml**: run the command in `extractors.yaml.TODO`; delete the `.TODO`.
4. **Bridges**: follow `schemas/bridges/README.md`; keep only
   `cmssw_release_supersedes_release`; delete the README.
5. `helm lint helm/okg -f envs/staging/values.yaml --set repositorySync.revision=x --set bootstrap.approvedRevision=x`
6. **Local e2e** — identical commands to CI; pass here ⇒ pass there:
   ```bash
   docker run -d --name pg --shm-size 2g -p 127.0.0.1:5435:5432 \
     -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=okg \
     ghcr.io/mitdbg/okg-postgres@sha256:75845f96d973859c248f0f6741cb0a06445e9d312e563de7a39c5e25f3236616
   export OKG_DSN=postgresql://postgres:dev@127.0.0.1:5435/okg
   export OKG_DEPLOYMENTS_DIR=$PWD/okg OKG_ENVIRONMENT_DATA_ROOT=$PWD/.okg-data
   mkdir -p .okg-data/repos .okg-data/cmssw-releases
   alias okg='docker run --rm --network host -v "$PWD:$PWD" -w "$PWD" \
     -e OKG_DSN -e OKG_DEPLOYMENTS_DIR -e OKG_ENVIRONMENT_DATA_ROOT \
     ghcr.io/mitdbg/okg@sha256:5a825f73c8929d2153859d95bfaf4c6f4ae01f02d08477583a7af05131826705'

   okg migrate --deployment archi-crab --apply      # twice → idempotent
   okg catalog ownership claim --deployment "$OKG_DEPLOYMENTS_DIR/archi-crab"
   okg catalog load  --deployment "$OKG_DEPLOYMENTS_DIR/archi-crab" --apply
   okg deployment lint archi-crab                   # ok=true or STOP: reconcile keys lint flags
   okg ingest --deployment archi-crab --progress
   bash scripts/smoke.sh
   ```
   `okg deployment lint` is the arbiter for every hand-authored key in
   `deployment.yaml` / `source_registry.yaml` — fix what it names, re-run
   claim → load → lint, never ingest on red. **Claim ownership only after
   registry + schemas + bridges are final** (steps 3–4).

**Verify 2** — `SMOKE OK`; `\dx` in the DB lists btree_gist, fuzzystrmatch,
pg_textsearch, pg_trgm, timescaledb, vector. Record in `README.md`: ingest
wall time, DB size (calibrate `timeout-minutes`, PVC sizes). Set
`validated.local_e2e` in `versions.lock`. If bed964f fails unexplainably →
`fallback` pins, note it, report upstream.

### Phase 3 — Push, protect, prove CI (½ day)

1. Push `main`. Immediately: branch protection (required `lint` +
   `okg-validate`, linear history, no force-push), CODEOWNERS review, secret
   scanning + push protection, Actions allowed-list = pinned actions,
   approval for outside collaborators.
2. Secrets: `GHCR_PAT`, `STAGING_BUMP_TOKEN` (fine-grained, this repo,
   contents:write). Environments: `staging` (no reviewers), `prod` (named
   reviewer, `main` only).
3. `pinact run` replaces every `@PIN`; commit.
4. Trivial PR → `lint` ≈ 90 s fail-fast; `okg-validate` green; the lint job
   references **no** secrets.
5. Merge → `main.yaml`: `e2e-smoke` green → bot commit lands the merge sha in
   both knowledge pins.

**Verify 3** — `envs/staging/values.yaml`: `revision == approvedRevision ==
merge sha`; engine digests untouched; Actions log shows digest-pinned images.

### Phase 4 — First staging deployment (Argo CD only; never `helm install`)

1. In CMSKubernetes@archi-crab-testbed add the staging Application:
   `repoURL: https://github.com/nausikt/archi-crab-okg.git`, `targetRevision:
   main`, `path: helm/okg`, `helm.valueFiles: [../../envs/staging/values.yaml]`,
   `destination.namespace: archi-crab-staging`, automated sync + prune. Root
   app-of-apps picks it up.
2. Watch: `repository-sync` (F2) → `bootstrap` (clones 2 repos to the PVC,
   ingests, publishes once) → `mcp-role` → `worker` Ready (its startup probe
   *is* `okg deployment ready`) → PostSync smoke Job `Complete`.
3. Triage map — each symptom is a known trap:
   `ImagePullBackOff` → Phase 1 pull secret / chart delta 1 ·
   PVC `Pending` → storageClassName (F1) ·
   bootstrap auth error → app_rw/app_ro NOLOGIN → chart delta 4 ·
   `release authority unavailable` → checkout lacks `.git` (F2) or `release.pin` wrong ·
   `record_set coverage check failed` → git-history crept into `expand` ·
   publish blocked on dangling edges → `consistency` block missing ·
   `catalog_ownership_foreign_writer` → manifests edited outside a PR ·
   `ProducerPolicyViolation` at ingest → a narrowing outside `schemas/bridges/`.

**Verify 4** — app Healthy+Synced; smoke Job Complete;
`kubectl -n archi-crab-staging exec sts/<rel>-runtime -c worker -- okg search --deployment archi-crab --query "crab submit"`
returns hits. Set `validated.staging` (via PR).

### Phase 5 — Prove both change types (the loop you will live in)

**Knowledge**: add a skill file by PR → merge → `main.yaml` → staging rolls →
smoke green. Time it; README the number (budget ≈ 30–40 min).

**Engine bump** (dry-run once): one PR edits `envs/staging` digests **and**
`versions.lock` → `pins` job picks the new engine → validate + e2e run *on
it* (compatibility gate; catalog drift and migration breakage surface here,
not in staging) → merge → staging soaks (a Postgres digest bump is a
data-compat event — watch bootstrap migrate; rebuild if anything smells off,
F4) → prod only via Promote.

**Verify 5** — both change types produced green staging smokes; you can name
the file each pin lives in from memory (`envs/*/values.yaml` — all four).

### Phase 6 — Promote (prod)

Add the prod Application (`prune: false` until two clean promotions). Actions
→ `promote` → prod-environment approval → PR diff **must be the four pin
lines only** (drift guard fails otherwise — reconcile hand-edits first) →
merge → prod syncs → prod smoke Complete → tag `v0.5.0`; set `validated.prod`.

**Verify 6** — prod Healthy; smoke Complete; tag pushed.

---

## §4 Standing rules

- Every knowledge change is a PR; no `kubectl exec` edits, ever.
- Identity-changing source edits ⇒ **fresh-database rebuild** (F4), routine.
- Never mix fixture and live data in one database.
- git-history: manual second pass only, until the upstream race is fixed.
- New sources: repo-based knowledge → a `code_repos` entry (works today; also
  the trick for TWiki exports and playbooks — make them repos) · curated files
  → needs a connector path (revisit when real) · live systems → MCPServer
  behind the vMCP, never ingestion.
- Engine bumps: digests only, Phase-5 checklist, staging-soaked first.
- **Publication day** (repo + upstream images public): delete `GHCR_PAT`, the
  Argo repo credential, `git-token` + `repositorySync.authSecretKey`,
  `ghcr-mitdbg-pull` + `images.pullSecrets`. The fork-PR lint-only limit
  self-deletes with the PAT.
- CI's `credentials.username: nausikt` ties CI to a personal account; swap to
  a machine account before this outlives its author.

Deferred, tracked: git-history · downloader init container + curated JSON
(Discord / cms-threads) · WMCore and more repos · TWiki/playbook export repos ·
semantic search (embedder) · MCP exposure (vMCP, 6 SSO clients, 6 LanDB
aliases) — follows a working staging graph · prod `prune: true`.

---

## §5 Footnotes — persistence, volumes, idempotence

Read these before the first sync. They are what the chart's volume layout
means for *your* data.

**F1 — The runtime-data PVC is where all knowledge state lives.** The
runtime StatefulSet's `volumeClaimTemplates` creates one PVC
(`runtime.storage`, sized per env) mounted at `okg.environmentDataRoot`
(`/var/lib/okg`) in **every** init and main container. On it: the
repositorySync checkout (`okg.repoRoot`, which must sit *under* the data
root or bootstrap cannot see it), the two repo clones (registry `base:
${OKG_ENVIRONMENT_DATA_ROOT}/repos`), the cmssw `releases.map` cache, and
any future connector caches (downloader targets). Persisting it is what makes
restarts cheap: on a warm restart the connectors fast-forward clones instead
of re-cloning, and `publishOnce` makes the bootstrap no-op. Sizing: clones +
caches + headroom — 20 Gi staging, 30 Gi prod is generous for two repos.
`storageClassName` **must** be a real class or the PVC pends forever and the
first init container never starts.

**F2 — The checkout is rebuilt deterministically every start.** The
`repository-sync` init container does `fetch --force --prune <revision>`,
`checkout --force --detach FETCH_HEAD`, `clean -ffdx` into `repoRoot`. Any
local drift in the checkout is erased on each pod start — the PVC persists
the `.git` objects (fast fetch), never edits. This also satisfies okg's
release-authority requirement that the deployment dir be a git repo. If
`repoRoot` already exists but is not a git repo, sync refuses — never
pre-populate that path by hand.

**F3 — Postgres has its own PVC and a memory-backed `/dev/shm`.** The
Postgres StatefulSet claims `postgresql.storage` at `/home/postgres/pgdata`
(the graph itself; the field guide's 15-repo instance was 26 GB — two repos
will be far smaller, but leave 30–50 Gi), and mounts `/dev/shm` as an
`emptyDir` with `medium: Memory`, `sizeLimit: postgresql.shmSizeLimit`
(2 Gi) — the k8s equivalent of `--shm-size 2g`, needed for parallel workers.
`max_locks_per_transaction=1024` is already in the container args.
`/tmp` is a shared emptyDir across the pod's containers — scratch only.

**F4 — Rebuild path (the intentional cold start).** Because retraction is
broken upstream, identity-changing source edits and Postgres image bumps that
smell wrong are handled by rebuilding, not reconciling:
`argocd app set <app> --sync-policy none` → scale both StatefulSets to 0 →
delete the two PVCs (`runtime-data-*`, the postgres data claim) → re-enable
sync. Bootstrap then re-clones, re-ingests and publishes from scratch
(minutes for two repos). StatefulSet PVCs are **not** deleted with the pod
or the StatefulSet by default — that is the safety you rely on; the rebuild
is the one time you delete them on purpose.

**F5 — What is idempotent, and why the pipeline is safe to re-run.**
`okg migrate --apply` is idempotent (CI runs it twice to prove it); catalog
claim + load are idempotent when content is unchanged (a *changed* manifest
outside a PR is what trips `catalog_ownership_foreign_writer`); bootstrap
re-runs on every pod restart but `publishOnce: true` guards the publish;
`repository-sync` converges to the pinned revision regardless of prior
state (F2); connectors fast-forward existing clones. Not idempotent:
retraction (F4) and anything you do by hand inside a pod — which is why the
standing rules forbid it.
