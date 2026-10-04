# archi v2 over MCP: the benchmark fixture — decisions and runbook

Written against `archi-physics/archi` **main @ e6609f8f** (2026-10-04) and this repository's
`main` (okg 0a8e0cd4, archi-okg 1bb7e703). Everything under `v2/` comes from it. §6 tracks
where we are; it is updated as the runbook is walked.

## 0. The end game, in one picture

```
                         knowledge: ONE list, sources/archi-crab.yaml (tiers, enabled, sensitivity)
                                   │ scripts/sources.py render
                 ┌─────────────────┴──────────────────────┐
                 ▼                                        ▼
  deployments/archi-crab/source_registry.yaml     v2/helm/archi-v2/files/weblists/archi-crab.list
  (okg: what the v3 instances ingest)             (archi v2: what the data-manager ingests)
                 │                                        │
   ┌─────────────┼──────────────┐                 ┌───────┴──────────────────────────┐
   ▼             ▼              ▼                 ▼                                  │
 run1          run2          prod        archi-v2 data-manager + Postgres            │ catalog API / SQL
 (frozen for   (best of      (promoted)  (pgvector + pg_textsearch)                  │
  study)        knowledge)                                              ┌────────────┴────────────┐
                                                                        ▼                         ▼
   okg mcp-serve per instance                                    MCPServer archi-v2-grep   MCPServer archi-v2-vector
   …/run1/mcp  …/run2/mcp  …/mcp                                 (ToolHive, group grep)    (ToolHive, group vector)
                                                                        ▼                         ▼
                                                                 vMCP + CERN SSO           vMCP + CERN SSO
                                                      archi-crab-v2-grep-<env>.cern.ch   archi-crab-v2-vector-<env>.cern.ch
                                                      search_local_files                 search_vectorstore_hybrid
                                                      search_metadata_index              (+ fetch_catalog_document)
                                                      list_metadata_schema
                                                      (+ fetch_catalog_document)
```

Ablations are composed by **which MCP servers the harness connects** — the same mechanism a
Claude Code user has (`claude mcp add` per server) — so the merged-toolset conditions are faithful:

| # | condition | what it answers |
|---|---|---|
| 1 | grep only | the lexical floor: how far exact match alone gets you |
| 2 | v2-vector only | embedding retrieval in isolation |
| 3 | okg (v3) only | the v3 claim, standalone |
| 4 | grep + v2-vector | **the v2 production baseline — the reference bar** |
| 5 | grep + okg | does cheap lexical search patch okg's gaps? (→ "add a lexical tool to v3", not "keep v2") |
| 6 | v2-vector + okg | — |
| 7 | all | — |

## 1. What archi `main` is today (verified, e6609f8f)

- **The data-manager is already headless.** `src/bin/service_data_manager.py`: a Flask
  service (port 7871) that at boot collects every configured source (`DataManager.run_ingestion`),
  persists files into a catalog in Postgres, chunks and embeds them (pgvector), then serves the
  catalog API: `GET /api/catalog/search` (modes: metadata, `grep`), `/api/catalog/document/<hash>`,
  `/api/catalog/schema`. Sources come from **weblists**: one URL per line, `git-<url>` for a
  repository (GitScraper: default branch, mkdocs `docs/` + code files by suffix), a bare URL for
  a page (html scraper, crawl depth `base_source_depth`). Cron re-sync per source is optional.
- **Config lives in Postgres**, not in files. `src/cli/tools/config_seed.py` loads the rendered
  `config.yaml` into a `static_config` table; services read it from there. The rendered config
  is archi's Jinja template `src/cli/templates/base-config.yaml` filled with your values;
  `init.sql` is its schema, and the vector column's dimension comes from the embedding you chose.
- **The grep family is HTTP; the vectorstore is in-process.** `search_local_files`,
  `search_metadata_index`, `list_metadata_schema`, `fetch_catalog_document` are LangChain tools
  around `RemoteCatalogClient` → the catalog API (bearer `DM_API_TOKEN`).
  `search_vectorstore_hybrid` is `HybridRetriever` over `VectorstoreConnector(config).get_vectorstore()`:
  a psycopg2 connection and the **embedding model instantiated in the caller**; BM25 runs inside
  Postgres (pg_textsearch, else `ts_rank`). There is no HTTP endpoint for vector search on `main`.
- **archi serves no MCP.** It is an MCP *client* (`langchain-mcp-adapters`). The v3 ADR keeps it
  so: no retrieval, vectorstore, embeddings or MCP servers in Archi.
- **Images.** Upstream CI publishes only base images (`a2rchi/archi-python-base:<version>`, and
  `a2rchi/a2rchi-python-base:latest` from the PR-preview workflow); the service images are built
  by `archi install` on the user's machine from `src/cli/templates/dockerfiles/`. The base image
  itself is `python:3.10` + one `requirements.txt` (91 pins). Its helm chart is rendered per
  deployment by the CLI and **bakes the secrets into `secrets.yaml`**.
- **Tool text and defaults the v2 agent used** (`cms_comp_ops_agent.py`, `tools/local_files.py`,
  `tools/retriever.py`): descriptions in `_tool_definitions()`; grep `max_results=3`, metadata
  `max_results=5`, fetch `max_chars=4000`; retriever `max_documents=4`, `max_chars=800`; hybrid
  `k`, `bm25_weight`, `semantic_weight` from `data_manager.retrievers.hybrid_retriever`
  (config default 0.6/0.4; the code default is 0.5/0.5).

Three upstream quirks that matter here (each reported in phase 3):

1. `base-config.yaml` renders `reset_collection: {{ … | default(true, true) }}` — a `false` is
   treated as unset, so the template can only say `true`, and `true` truncates `document_chunks`
   and re-embeds the whole corpus on **every** data-manager start.
2. `init.sql`'s vector dimension is looked up by `embedding_name`, which is the class name
   (`OpenAIEmbeddings`), never a model name, so it is 384 unless `dimensions:` is set on the
   embedding entry. With OpenAI's 1536-dimensional model and no `dimensions:`, ingestion fails.
3. The catalog API checks `DM_API_TOKEN` only when `services.data_manager.auth.enabled` is true;
   with auth off it answers anyone who can reach the pod.

## 2. Decisions (ADR-V2-1 … 10)

Each: what, why, what else was considered, what it costs.

### ADR-V2-1 — It lives in this repository, under `v2/`, as its own chart and images

`v2/` holds everything: `docker/` (base, data-manager+mcp, postgres), `mcp/` (the server),
`helm/archi-v2/` (a chart written for Argo CD), `deployments/archi-crab/config.yaml` (our
choices), `envs/<env>/values.yaml` (what runs), `versions.lock` (the pin), `scripts/`,
`vendor/reference/` (upstream's Dockerfiles, base requirements and chart, copied verbatim for
diffing). Workflows are prefixed `v2-`.

*Why here:* the knowledge list is here (ADR-V2-6), the engine-pinning pattern is here, and the
IaC repository only needs one Argo CD Application pointing at `v2/helm/archi-v2`
(`v2/argocd/application-staging.example.yaml`). *Not* archi's own chart: rendered per deployment
by the CLI, secrets baked in, chat UI included — vendored for reference only. *Not* a new
repository: zero new repos is the v3 rule.

### ADR-V2-2 — Headless: Postgres + data-manager + the config seed. Nothing else

No chat, no grader, no grafana, no selenium. Ingestion is archi's own, unchanged: the
data-manager stage is upstream's `Dockerfile-data-manager-universal` (vendored) with two
differences — the source is `ADD`ed from git at the pinned commit, and the HuggingFace embedding
model is baked into the image (`HF_HOME`, `HF_HUB_OFFLINE=1` at run time), so the image is a pure
function of (base image, archi commit, model) and nothing downloads at start. The config is seeded
by an **initContainer** before every data-manager start (upstream uses a post-install hook Job;
an init container has no Argo CD hook-ordering problem and makes "what runs is what git says"
true on every restart).

*Cost:* Firefox and geckodriver ride along (~300 MB) because upstream's image has them; keeping
the Dockerfile verbatim beats a slimmer image we would then be benchmarking.

### ADR-V2-3 — The MCP layer is one image; staging runs it as ToolHive servers, CI as sidecars

`archi-v2-mcp` = the data-manager image + `v2/mcp/server.py`. One process serves one tool
family (`V2_MCP_FAMILY=grep|vector`); the `fetch` toggle and the tool list are **environment**
(`V2_MCP_FETCH`, `V2_MCP_TOOLS`), so `tools/list` is the gate — a client never sees a tool the
condition does not include. The chart runs it in one of two modes (`mcp.mode`):

- **`toolhive`** (staging, prod): one ToolHive `MCPServer` per family, each in its **own
  `MCPGroup`** (the trust boundary: one audience, one group), fronted by its own
  `VirtualMCPServer` with CERN SSO and one hostname per family (ADR-V2-5). The grep server
  reaches the data-manager over its Service; the vector server holds the embedding model and a
  Postgres connection, as the v2 agent did.
- **`sidecar`** (CI, a laptop): two containers in the data-manager pod behind a static bearer,
  ClusterIP only. What `v2-smoke` exercises, since a runner has neither ToolHive nor a Gateway.

*Why not one server with all five tools:* conditions 1, 2, 5 and 6 need them apart, and mixed
conditions must not become a tool-description wording contest. *Why `fetch` rides with both:*
it is the second half of both workflows (the vector tool's own description says so).
*Why not a member of the crab gateway's group:* a benchmark fixture is not part of that trust
boundary (the group comment in that chart is right); separate groups cost nothing but hostnames.

### ADR-V2-4 — The thin layer reimplements nothing: archi's tools, exposed by introspection

`v2/mcp/server.py` calls archi's own factories (`create_file_search_tool`,
`create_metadata_search_tool`, `create_metadata_schema_tool`, `create_document_fetch_tool`,
`create_retriever_tool` over `HybridRetriever` over `VectorstoreConnector`) and exposes each
LangChain `StructuredTool` as an MCP tool: name, argument schema (from `args_schema`), defaults,
and the exact output string the v2 agent saw. The five descriptions are the agent's own, copied
verbatim; `v2/scripts/contract-check.py` fails the engine PR when archi changes a description, a
factory default, a route or a config key. Tool names stay **native** (`search_local_files`, …):
MCP clients already namespace by server (`mcp__v2-grep__search_local_files`).

*Measured consequence (design notes §3):* per call, query embedding 50–300 ms, SQL 5–30 ms, the
MCP hop 1–5 ms, the LLM turn seconds — the MCP layer is noise. One warm embedding model per
family is operationally better than v2's per-agent-replica in-process model.

### ADR-V2-5 — CERN SSO now, through ToolHive vMCPs, on the existing public CERN client

Each family's `VirtualMCPServer` has `incomingAuth: oidc` against the CERN realm with the
**public client the crab gateway already uses** (`crab-mcp-gateway-public[-staging]`) as
audience: PKCE with a localhost redirect, so Claude Code and mcp-inspector log in at CERN SSO
and no new CERN application is registered. Each family gets one hostname on the shared Gateway
(`archi-crab-v2-grep-<env>.cern.ch`, `archi-crab-v2-vector-<env>.cern.ch`), exactly as the
gateway chart adds a hostname per client family. The MCP container itself runs anonymous
(`V2_MCP_ALLOW_ANONYMOUS=1`): the vMCP is the only gate — the gateway chart's `backendAuth:
false` for the same reason (a vMCP cannot authenticate its own health checks to a backend that
enforces OIDC) — and the chart's NetworkPolicy keeps everything but in-namespace pods from the
backends. **MCP is never exposed except through a vMCP**: the bearer-token HTTPRoute of the
first draft is gone.

*Accepted:* a token minted for the crab gateway is valid for the v2 vMCPs and vice versa (same
audience). Same users, public corpus (the sources governance gate feeds both targets, so the v2
corpus cannot hold anything the okg instances may not). Isolation later = one Application Portal
entry (`archi-crab-v2-public`) + one values line. *Cost:* two hostnames per environment: LanDB
alias, certificate, Gateway listener (phase 4, in the IaC repository).

### ADR-V2-6 — One source of truth, propagated: the okg list renders the v2 weblist

`scripts/sources.py render --write` writes two generated files from `sources/archi-crab.yaml`:
the okg registry and `v2/helm/archi-v2/files/weblists/archi-crab.list`; `lint` fails when either
differs from its render. The mapping (`render_v2`):

| okg kind | v2 line | parity notes |
|---|---|---|
| `git` (code_repos) | `git-<url>` | archi clones the default branch and indexes mkdocs `docs/` + code by suffix; `scope`/`max_files` have no v2 equivalent (tier 30 stays off in both) |
| `docs-files` (records.json) | one bare `<url>` per record | archi fetches the **live** TWiki page (`base_source_depth: 1` = listed pages only); the okg instance holds the sanitized export. Same 285 page identities, different text processing — a structural asymmetry, stated in the methodology. Local-file ingestion of the sanitized text was rejected: archi's local files carry no URL, so citations would break |
| `twiki-raw` | `https://twiki.cern.ch/twiki/bin/view/<Web>/<Topic>` per topic | same as above |
| `cmssw-releases` | — (no v2 collector) | listed in the file header as "not in v2" |

Tiers, `enabled`, `retired` and the governance gate apply unchanged. v2 has no generation
pinning: the corpus moves only when the data-manager pod restarts (ingestion runs at boot; all
cron schedules are empty), and the chart rolls the pod when the list or config changes (checksum
annotations). Pinning for a benchmark run = note the pod's start time and fingerprint
`resources` / `document_chunks` before and after (§4, phase 2 step 6).

### ADR-V2-7 — Pinned and tracked like the engine: `v2/versions.lock`, a daily PR, bot-written env pins

`v2/versions.lock` carries archi's commit (and pyproject version), our base image digest, and the
digests of our three images, each with a fingerprint of what it was built from
(`v2/scripts/lock.sh`). `v2-engine.yaml` (daily, or by hand): resolve archi `main` → re-vendor
the references → rebuild the base when its inputs moved → build and push the three images when
theirs moved → contract check inside the image → re-render config/init.sql → write the lock →
one rolling PR on `v2/upstream` (label `hold` pauses it). `v2-ci.yaml` on the PR: lint (generated
files == render, helm lint/template in both modes, static contract, vendored references match)
and `v2-smoke.yaml` (pull the lock's images, run everything on the runner, MCP handshake and
calls). `v2-main.yaml` after the merge: smoke again, then pin the digests into
`v2/envs/staging/values.yaml` in one bot commit. The chart and its generated files follow
`main` directly (Argo CD points at the path); the bot gates the **image**.

### ADR-V2-8 — Config: our short file, rendered by archi's own templates, generated files checked in

`v2/deployments/archi-crab/config.yaml` holds only what we choose. `v2/scripts/render-config.py`
renders it through archi's `base-config.yaml` and `init.sql` (the CLI's code path) into
`v2/helm/archi-v2/files/`, and `--check` fails CI on drift. A `v2_overrides:` block applies the
few values the template cannot express (today: `reset_collection: false`, quirk 1), each an
upstream report. Embedding dimensions are checked against the model (quirk 2). Auth is on, so the
bearer gates the catalog API (quirk 3).

### ADR-V2-9 — Secrets by reference; a read-only DB role for the vector server is phase 2b

One Secret (`archi-v2`) created out of band: `PG_PASSWORD`, `DM_API_TOKEN`, `V2_MCP_AUTH_TOKEN`
(sidecar mode only), optionally `DM_ADMIN_PASSWD`, `OPENAI_API_KEY`, `HUGGING_FACE_HUB_TOKEN`.
The grep server holds only `DM_API_TOKEN`. The vector server holds the Postgres password today;
a `SELECT`-only role (okg's `mcp-role` pattern) waits until the config read path is confirmed
read-only (`ConfigService.get_static_config` may upsert) — phase 2b.

### ADR-V2-10 — Our own base image, from upstream's recipe, rebuilt only when the recipe moves

`v2/docker/Dockerfile.base` is upstream's base recipe (`python:3.10` + `requirements.txt`, both
vendored under `v2/vendor/reference/dockerfiles/` and re-vendored on every engine PR) plus one
file of our own, `v2/docker/base-requirements.extra.txt`, empty unless a pin must be patched.
`v2-engine` rebuilds and pushes `ghcr.io/nausikt/archi-v2-python-base` only when the fingerprint
of those inputs changes (`lock.sh base-stale`), and records digest + fingerprint in the lock; the
data-manager and mcp images build `FROM` it by digest. Nothing in `v2/` depends on `a2rchi/*`
images on Docker Hub any more, and a base-level change (a CVE in a pin, a yanked wheel) is a
one-line commit here instead of a wait for upstream.

*Cost:* one more image (~2 GB, torch CPU) and ~10 minutes when the base rebuilds (rare: upstream
changes `requirements.txt` a few times a year).

## 3. Open questions — answers change files, not the design

1. **The live v2 deployment's config.** The benchmark's reference bar (condition 4) is only
   meaningful with the SAME `embedding_name` (+ model, `dimensions`), `chunk_size`,
   `chunk_overlap`, `collection_name`, `distance_metric`, `retrievers.hybrid_retriever.*`, and
   the `dynamic_config` row if the UI ever changed `num_documents_to_retrieve`/weights. Until
   pasted in, `config.yaml` carries a marked placeholder (HuggingFace all-MiniLM-L6-v2, CPU,
   baked into the image). If it is `OpenAIEmbeddings` through the CERN LiteLLM gateway: the
   `OPENAI_API_KEY` secret, the gateway `base_url` under `embedding_class_map.OpenAIEmbeddings.kwargs`,
   `dimensions: 1536`, and `HF_PREFETCH_MODEL=""` (nothing to bake).
2. **TWiki in v2: live pages (default) or the sanitized text as local files?** Live is the
   native v2 path with real citations (ADR-V2-6); local files would be the identical text with no URL.
3. **ToolHive CRD versions on the testbed.** The chart assumes `toolhive.stacklok.dev/v1beta1`
   and operator 0.47.0 behaviour, as the gateway chart does; `kubectl api-resources --api-group=toolhive.stacklok.dev`
   confirms it before phase 4.

## 4. Runbook

Each phase ends in a pull request on `nausikt/archi-crab-okg` (or the IaC repository) and a
check that proves it. §6 is the checklist.

### Phase 1 — scaffold (this PR, branch `v2-bench`)

Adds `v2/` (above), the `scripts/sources.py` v2 target, `v2-ci.yaml`, `v2-smoke.yaml`,
`v2-engine.yaml`, `v2-main.yaml`, this document. CI on the PR proves: generated files equal
their render; the chart lints and templates in both modes; the static contract with archi
e6609f8f holds; the vendored references match; the smoke builds the base + three images on the
runner (the lock has no digests yet) and talks MCP to both servers over a two-entry corpus.

```bash
git switch -c v2-bench origin/main && git am archi-crab-okg-v2-bench-phase1/*.patch
git push -u origin v2-bench            # open the PR; read v2-ci's two jobs; merge
```

Before or right after merging, answer §3 item 1 (the live v2 config) in
`v2/deployments/archi-crab/config.yaml`, then `python3 v2/scripts/render-config.py --write --archi <checkout>`
and `python3 scripts/sources.py lint --base published` — the smoke proves the new embedding.

### Phase 2 — first images, first deploy (sidecar mode on the staging testbed)

1. **Images.** Actions → `v2-engine` → Run workflow (leave inputs empty). It builds and pushes
   the base + three images, writes `v2/versions.lock`, and opens PR `v2/upstream`. Its `v2-ci`
   smoke pulls exactly those images. Merge it. `v2-main` then re-runs the smoke on main and pins
   the digests into `v2/envs/staging/values.yaml` (`v2 staging: pin …`).
2. **The Secret**, in the cluster only:
   ```bash
   kubectl -n archi-crab-staging create secret generic archi-v2 \
     --from-literal=PG_PASSWORD="$(openssl rand -hex 24)" \
     --from-literal=DM_API_TOKEN="$(openssl rand -hex 24)" \
     --from-literal=V2_MCP_AUTH_TOKEN="$(openssl rand -hex 24)"
   # + OPENAI_API_KEY=… if the embedding is OpenAI; + DM_ADMIN_PASSWD=… only if you want the upload UI
   ```
3. `v2/envs/staging/values.yaml` already says `mcp.mode: sidecar` for this phase (no
   hostnames yet; phase 4 flips that one line to `toolhive`).
4. **The Argo CD Application** in CMSKubernetes (`archi-crab-testbed`), from
   `v2/argocd/application-staging.example.yaml`; sync. Watch the first ingest (19 sources: 285
   pages + 18 repositories; tens of minutes):
   ```bash
   NS=archi-crab-staging
   kubectl -n $NS get pod -l app.kubernetes.io/component=data-manager
   kubectl -n $NS logs deploy/archi-v2-data-manager -c config-seed
   kubectl -n $NS logs deploy/archi-v2-data-manager -c data-manager -f | grep -iE 'ingest|indexing|error'
   kubectl -n $NS exec deploy/archi-v2-data-manager -c data-manager -- curl -s localhost:7871/api/ingestion/status
   ```
5. **Smoke from your machine** (the chart's NOTES print the same):
   ```bash
   T=$(kubectl -n $NS get secret archi-v2 -o jsonpath='{.data.V2_MCP_AUTH_TOKEN}' | base64 -d)
   kubectl -n $NS port-forward svc/archi-v2-mcp-grep 8081 & kubectl -n $NS port-forward svc/archi-v2-mcp-vector 8082 &
   python3 v2/scripts/smoke.py http://127.0.0.1:8081/mcp --token "$T" --expect fetch_catalog_document,list_metadata_schema,search_local_files,search_metadata_index --call search_local_files '{"query": "crab submit"}'
   python3 v2/scripts/smoke.py http://127.0.0.1:8082/mcp --token "$T" --expect fetch_catalog_document,search_vectorstore_hybrid --call search_vectorstore_hybrid '{"query": "stageout failure exit code 8028"}'
   ```
6. **Corpus fingerprint**, kept with every benchmark run (`psql` in the postgres pod):
   `select count(*), md5(string_agg(hash, ',' order by hash)) from resources;` and the same over
   `document_chunks` (by `id`).

Phase 2b (any time after 2): the read-only role for the vector server (ADR-V2-9), once
`ConfigService.get_static_config` is confirmed SELECT-only in the pinned archi.

### Phase 3 — the daily loop, and the upstream reports

Nothing to deploy: `v2-engine` runs daily from phase 1 on. What to do once:

1. Create the `v2` label (`gh label create v2`) and check `STAGING_BUMP_TOKEN` + `GHCR_PAT` are
   the repository secrets the okg engine already uses (they are; same names).
2. Watch the first scheduled PR: its diff of `v2/vendor/reference/` is the upstream change; the
   contract report in the PR body says whether archi moved anything we borrow.
3. File the three quirks (§1) against archi-physics/archi, each with the one-line fix:
   `default(true, true)` → `default(true)` on `reset_collection`; look dimensions up by the
   embedding's model name; check `DM_API_TOKEN` regardless of `auth.enabled`.

### Phase 4 — hostnames and CERN SSO (toolhive mode)

In the IaC repository (`CMSKubernetes`, `archi-crab-testbed`), the same three things the crab
gateway's hostnames needed:

1. **LanDB aliases** `archi-crab-v2-grep-staging` and `archi-crab-v2-vector-staging` on the
   Gateway's VIP (the one `kubectl -n archi-crab-gw get svc cilium-gateway-archi-crab` shows).
2. **Certificates** for both names in `archi-crab-gw` (however the existing listeners got
   theirs: cert-manager or the CERN CA), and **two listeners** in the gateway chart's values
   (`listeners: - {host: …, tlsSecret: …, env: staging}`), so routes from a namespace labelled
   `archi-crab.cern.ch/env: staging` may claim them.
3. Confirm the ToolHive CRD version: `kubectl api-resources --api-group=toolhive.stacklok.dev -o wide`
   (`v1beta1` is what the chart assumes).

Then in this repository: `v2/envs/staging/values.yaml` `mcp.mode: sidecar` → `toolhive` (the
hosts and `cern.audience` are already there). PR, merge; Argo CD syncs the groups, OIDC configs,
MCPServers, vMCPs and HTTPRoutes. Check:

```bash
kubectl -n archi-crab-staging get mcpgroup,mcpserver,virtualmcpserver,httproute -l app.kubernetes.io/part-of=archi-crab-bench
kubectl -n archi-crab-staging get svc | grep vmcp-archi-v2      # vmcp-archi-v2-grep / -vector on 4483
curl -sI https://archi-crab-v2-grep-staging.cern.ch/mcp | head -3   # 401 + WWW-Authenticate from the vMCP
claude mcp add --transport http v2-grep   https://archi-crab-v2-grep-staging.cern.ch/mcp   --client-id crab-mcp-gateway-public-staging
claude mcp add --transport http v2-vector https://archi-crab-v2-vector-staging.cern.ch/mcp --client-id crab-mcp-gateway-public-staging
```

Prod is the same with `v2/envs/prod/values.yaml` (`-staging` dropped from the hosts, audience
`crab-mcp-gateway-public`), promoted the way the okg chart is.

### Phase 5 — run1/run2, the harness

**run1 / run2 as preserved okg instances.** One okg release per run in its own namespace
(`archi-crab-run1`, `archi-crab-run2`), from `envs/run1/values.yaml` etc.: `fullnameOverride`,
`repositorySync.revision` and `bootstrap.approvedRevision` pinned by hand to the knowledge
commit the run studies, images pinned to the engine of that day, and **no bot pin** (the
`main.yaml` bump writes only `envs/staging`). A per-run source list is fine
(`sources/archi-crab-run1.yaml` → `deployments/archi-crab-run1/`: `scripts/sources.py --deployment`
already takes the name); the best-of-knowledge list stays `sources/archi-crab.yaml`, and it is the
one the v2 fixture follows. Their MCP paths (`archi-crab-okg-staging.cern.ch/run1/mcp`, …) are
one HTTPRoute with path prefixes in the okg chart (`PathPrefix /run1` → that release's `-mcp`
Service, `URLRewrite` to `/mcp`); bearer-gated as okg's MCP is today, or behind a vMCP per run
if they are to be used by people — the same two choices as ADR-V2-5.

**The harness.** A condition is a set of MCP servers; the harness connects them exactly as
above (`claude mcp add` per server, or the SDK), runs the question set, and records per query:
the answer, every tool call (server, tool, arguments, result hash) for attribution, the okg
generation id, the v2 corpus fingerprint, and the images' digests. A run whose fingerprints
moved is discarded. Defaults are v2's (`max_documents=4`, `max_chars=800`, fetch 4000); `k`
and `max_chars` sweeps are the tool parameters, not server changes. Lives under `bench/` in
this repository when it exists — nothing in `v2/` constrains it.

## 5. What was checked here, and what was not

- **Checked:** the MCP server against archi's real tool factories (e6609f8f) and a stand-in
  data-manager: initialize, `tools/list` (names, schemas, descriptions), the four grep-family
  calls, 401 without the bearer; `render-config.py` through archi's real templates; the v2
  weblist render and its lint gate (18 repositories + 285 pages); the contract check (green
  against e6609f8f); `vendor-sync.sh` is a no-op at the pinned commit; the lock helper's
  fingerprints and stale checks.
- **Not checked here** (no Docker Hub, no helm, no cluster in this sandbox): the image builds
  (base, data-manager, mcp, postgres), the vector server against a real pgvector +
  pg_textsearch, `helm lint`/`template`, the ToolHive CRs against the operator. The first two
  run in `v2-ci` on the phase 1 PR; the CRs are proven by phase 4's sync.

## 6. Where we are (updated as the runbook is walked)

| step | state | evidence |
|---|---|---|
| Phase 1 PR (`v2-bench`) | **to open** — patches delivered, nothing on `main` yet | `main` = 3430a78 (`staging: pin ffbe61dae`) |
| §3.1 live v2 config | open | placeholder in `v2/deployments/archi-crab/config.yaml` |
| Phase 2.1 first images (`v2-engine` by hand) | not started | |
| Phase 2.2–2.5 Secret, sidecar deploy, smoke | not started | |
| Phase 3 daily loop | not started | |
| Phase 4 hostnames + SSO | not started | |
| Phase 5 run1/run2, harness | not started | |
