# archi v2 over MCP: the benchmark fixture — decisions and runbook

Written against `archi-physics/archi` **main @ e6609f8f** (2026-10-04) and this repository's
`main` (okg 0a8e0cd4, archi-okg 1bb7e703). Everything under `v2/` comes from it. §6 tracks
where we are; it is updated as the runbook is walked.

## 0. The end game, in one picture

```
                    knowledge: ONE list, sources/archi-crab.yaml (tiers, enabled, sensitivity)
                                  │ scripts/sources.py render
                ┌─────────────────┴─────────────────────┐
                ▼                                       ▼
 deployments/archi-crab/source_registry.yaml   v2/helm/archi-v2/files/weblists/archi-crab.list
                │                                       │
   namespace archi-crab-staging (ALL of it: one namespace, one release per instance)
   ┌────────────┼─────────────┐                         ▼
   ▼            ▼             ▼              archi-v2 (release): Postgres + data-manager
 okg staging  okg run1      okg run2           pod: data-manager | mcp-grep | mcp-vector
 (best of     (frozen)      (frozen)                               :8081      :8082
  knowledge)                                                         │          │
   │ -mcp:8765  │ -mcp        │ -mcp                                 │          │
   ▼            ▼             ▼                                      ▼          ▼
 ── ToolHive MCPRemoteProxy per endpoint (CMSKubernetes mcp-gateway: CERN SSO + Cedar) ──
   │            │             │                                      │          │
 archi-crab-okg-staging.cern.ch                          archi-crab-v2.cern.ch
   /mcp       /run1/mcp     /run2/mcp                    /grep/mcp   /vectorstore/mcp
   /akmon     /run1/akmon   /run2/akmon   <- console, okg chart (oauth2-proxy per release)
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
choices), `envs/bench/values.yaml` (what runs: the fixture has ONE environment), `versions.lock`
(the pin), `scripts/`,
`vendor/reference/` (upstream's Dockerfiles, base requirements and chart, copied verbatim for
diffing). Workflows are prefixed `v2-`.

*Why here:* the knowledge list is here (ADR-V2-6), the engine-pinning pattern is here, and the
IaC repository only needs one Argo CD Application pointing at `v2/helm/archi-v2`
(`v2/argocd/application.example.yaml`). *Not* archi's own chart: rendered per deployment
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

### ADR-V2-3 — The MCP layer is one image, run as two sidecars; exposure is the gateway chart's job

`archi-v2-mcp` = the data-manager image + `v2/mcp/server.py`. One process serves one tool
family (`V2_MCP_FAMILY=grep|vector`); the `fetch` toggle and the tool list are **environment**
(`V2_MCP_FETCH`, `V2_MCP_TOOLS`), so `tools/list` is the gate — a client never sees a tool the
condition does not include. Both run as **sidecars of the data-manager pod**, one Service each
(`archi-v2-mcp-grep:8081`, `archi-v2-mcp-vector:8082`): the grep server reaches the catalog API
on localhost; the vector server holds the embedding model and a Postgres connection, as the v2
agent did. This chart creates **no** public surface (ADR-V2-5).

*Simplified (2026-10-04):* an earlier draft ran each family as a ToolHive `MCPServer` in its own
`MCPGroup` behind its own `VirtualMCPServer`. That is three CRDs per family to front one
endpoint each; the okg MCP is already fronted the simpler way (one `MCPRemoteProxy` per Service),
and that pattern is verified on this cluster. The v2 chart is now plain Kubernetes, the same in
CI and in the cluster. *Why not one server with all five tools:* conditions 1, 2, 5 and 6 need
them apart. *Why `fetch` rides with both:* it is the second half of both workflows.

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

### ADR-V2-5 — One hostname per surface, a path per endpoint, CERN SSO through MCPRemoteProxy

Every public MCP endpoint of this project goes through the CMSKubernetes `mcp-gateway` chart's
`remoteProxies`: a ToolHive `MCPRemoteProxy` per endpoint (CERN SSO with the public PKCE client,
Cedar policy, audit) in front of an in-cluster Service. MCP is never exposed any other way.
Entries now take a **`path`**, so endpoints share hostnames instead of costing a LanDB alias,
certificate and Gateway listener each:

| URL | proxy (`remoteProxies`) | upstream Service |
|---|---|---|
| `archi-crab-okg-staging.cern.ch/mcp` | `okg` (no path: catch-all `/`, as today) | `archi-crab-okg-staging-mcp:8765` |
| `archi-crab-okg-staging.cern.ch/run1/mcp` | `okg-run1`, `path: /run1` | `archi-crab-okg-run1-mcp:8765` |
| `archi-crab-okg-staging.cern.ch/run2/mcp` | `okg-run2`, `path: /run2` | `archi-crab-okg-run2-mcp:8765` |
| `archi-crab-v2.cern.ch/grep/mcp` | `v2-grep`, `path: /grep` | `archi-v2-mcp-grep:8081` |
| `archi-crab-v2.cern.ch/vectorstore/mcp` | `v2-vector`, `path: /vectorstore` | `archi-v2-mcp-vector:8082` |

A path entry renders two HTTPRoute rules: `PathPrefix <path>` rewritten to `/` (the proxy serves
`/mcp`), and an `Exact` rule mapping the RFC 9728 path-aware discovery document
(`/.well-known/oauth-protected-resource<path>/mcp`, what MCP clients try first for a resource
that has a path) to the proxy's `/.well-known/oauth-protected-resource`; `resourceUrl` is the
full public URL, so the document's `resource` matches what the client connected to. The
authorization server is CERN's (clients talk to auth.cern.ch directly), so nothing else needs a
path. Gateway API's longest-prefix match keeps everything apart on one hostname:
`/run1/akmon` (console) > `/run1` (run1 MCP) > `/` (staging MCP catch-all).

**Audience:** the okg proxy's public client `archi-crab-okg-public-staging` for all five, with
the okg Cedar policy (`cms-members` may call tools; `query` is forbidden on okg). One login then
covers v2 and v3 for the benchmark harness, and no new CERN application is registered.

**The v2 sidecars run without an app-level token** once fronted (`mcp.auth: none`): the proxy is
the gate, and the chart's NetworkPolicy admits only ToolHive's proxy pods (`toolhive: "true"`)
to the MCP ports. Before that (phase 2), `mcp.auth: bearer` and port-forward.

*Risk, checked in phase 4:* ToolHive's 401 must name the path-aware discovery URL, or Claude
Code must fall back to it. If neither, the fallback is a hostname per endpoint (aliases) for the
v2 pair; the okg runs could instead stay on their own hostnames. One `curl -sI` settles it.

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
files == render, helm lint/template with `mcp.auth` bearer and none, static contract, vendored references match)
and `v2-smoke.yaml` (pull the lock's images, run everything on the runner, MCP handshake and
calls). `v2-main.yaml` after the merge: smoke again, then pin the digests into
`v2/envs/bench/values.yaml` in one bot commit. The chart and its generated files follow
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
(while `mcp.auth: bearer`), optionally `DM_ADMIN_PASSWD`, `OPENAI_API_KEY`, `HUGGING_FACE_HUB_TOKEN`.
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
3. **Path-aware OAuth discovery through MCPRemoteProxy** (ADR-V2-5 risk): one `curl -sI` in
   phase 4. Test it first on the cheapest endpoint (`/run1/mcp` or `/grep/mcp`).

## 4. Runbook

Each phase ends in a pull request on `nausikt/archi-crab-okg` (or the IaC repository) and a
check that proves it. §6 is the checklist.

### Phase 1 — scaffold (this PR, branch `v2-bench`)

Adds `v2/` (above), the `scripts/sources.py` v2 target, `v2-ci.yaml`, `v2-smoke.yaml`,
`v2-engine.yaml`, `v2-main.yaml`, this document. CI on the PR proves: generated files equal
their render; the chart lints and templates with `mcp.auth` bearer and none; the static contract with archi
e6609f8f holds; the vendored references match; the smoke builds the base + three images on the
runner (the lock has no digests yet) and talks MCP to both servers over a two-entry corpus.

```bash
git switch -c v2-bench origin/main && git am archi-crab-okg-v2-bench/*.patch   # folder in the delivered tarball
git push -u origin v2-bench            # open the PR; read v2-ci's two jobs; merge
```

`git am` warns about trailing whitespace in `v2/vendor/reference/**` and
`v2/helm/archi-v2/files/init.sql`. Expected: the first is upstream's files verbatim, the second
is rendered from upstream's template, and CI diffs both byte for byte against archi
(`vendor-sync.sh`, `render-config.py --check`). Do **not** use `--whitespace=fix`; it would make
those checks fail. `.gitattributes` marks both paths so later patches and `git diff --check`
stay quiet.

Before or right after merging, answer §3 item 1 (the live v2 config) in
`v2/deployments/archi-crab/config.yaml`, then `python3 v2/scripts/render-config.py --write --archi <checkout>`
and `python3 scripts/sources.py lint --base published` — the smoke proves the new embedding.

### Phase 2 — first images, first deploy (`mcp.auth: bearer`, namespace archi-crab-staging)

1. **Images.** Actions → `v2-engine` → Run workflow (leave inputs empty). It builds and pushes
   the base + three images, writes `v2/versions.lock`, and opens PR `v2/upstream`. Its `v2-ci`
   smoke pulls exactly those images. Merge it. `v2-main` then re-runs the smoke on main and pins
   the digests into `v2/envs/bench/values.yaml` (`v2 bench: pin …`).
2. **The Secret**, in the cluster only:
   ```bash
   kubectl -n archi-crab-staging create secret generic archi-v2 \
     --from-literal=PG_PASSWORD="$(openssl rand -hex 24)" \
     --from-literal=DM_API_TOKEN="$(openssl rand -hex 24)" \
     --from-literal=V2_MCP_AUTH_TOKEN="$(openssl rand -hex 24)"
   # + OPENAI_API_KEY=… if the embedding is OpenAI; + DM_ADMIN_PASSWD=… only if you want the upload UI
   ```
3. `v2/envs/bench/values.yaml` already says `mcp.auth: bearer` for this phase (no
   hostname yet; phase 4 flips that one line to `none` once the remote proxies are the gate).
4. **The Argo CD Application** in CMSKubernetes (`archi-crab-testbed`), from
   `v2/argocd/application.example.yaml` (namespace `archi-crab-staging`: the ToolHive operator, the
   mcp-gateway remote proxies and the Gateway's listener selector are there; every run shares it); sync. Watch the first ingest (19 sources: 285
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

### Phase 4 — `archi-crab-v2.cern.ch` and CERN SSO (gateway chart)

Two pull requests and three outside-Git items. The CMSKubernetes changes are in the
`archi-crab-paths` patch (path support in `remoteProxies`, the v2 and run entries as
`enabled: false`, the `archi-crab-v2.cern.ch` listener, the `archi-v2` Application as `.disabled`).

1. **Outside Git:** LanDB alias `archi-crab-v2` on the Gateway's VIP (the Octavia LB's
   `landb-alias` tag, same VIP as every other hostname); host certificate as Secret
   `archi-crab-v2-tls` in `archi-crab-gw`; nothing in the Application Portal (the okg public client
   is reused).
2. **CMSKubernetes PR:** apply `archi-crab-paths`; rename `46-archi-v2-app.yaml.disabled` →
   `.yaml` (if phase 2 did not already); set `v2-grep` / `v2-vector` `enabled: true`.
3. **This repository, same day:** `v2/envs/bench/values.yaml` `mcp.auth: bearer` → `none`.
   (Order does not matter much: until both land, either the proxy cannot reach the MCP port, or
   the sidecar still wants a bearer the proxy does not send — closed, not open.)

Check, in this order — the third command is the ADR-V2-5 risk:

```bash
kubectl -n archi-crab-gw get gateway archi-crab -o json | jq '.status.listeners[] | select(.hostname=="archi-crab-v2.cern.ch") | .conditions[] | {type,status}'
kubectl -n archi-crab-staging get mcpremoteproxy,httproute | grep v2-
curl -sI https://archi-crab-v2.cern.ch/grep/mcp | grep -i www-authenticate
#   want: resource_metadata="https://archi-crab-v2.cern.ch/.well-known/oauth-protected-resource/grep/mcp"
curl -s https://archi-crab-v2.cern.ch/.well-known/oauth-protected-resource/grep/mcp
#   want: {"resource": "https://archi-crab-v2.cern.ch/grep/mcp", "authorization_servers": ["https://auth.cern.ch/auth/realms/cern"], …}
claude mcp add --transport http v2-grep   https://archi-crab-v2.cern.ch/grep/mcp        --client-id archi-crab-okg-public-staging --callback-port 8765
claude mcp add --transport http v2-vector https://archi-crab-v2.cern.ch/vectorstore/mcp --client-id archi-crab-okg-public-staging --callback-port 8765
```

If the 401 names the root `/.well-known/oauth-protected-resource` and Claude Code does not fall
back to the path-aware URL: say so, and the two v2 entries move to their own aliases
(`host:` per entry, no `path:`) — a values change, no template change.

### Phase 5 — run1/run2 (same namespace), their console paths, the harness

**All runs share `archi-crab-staging`** — this is the simple option, not a complication. Each run
is one more Helm release of the same `helm/okg` chart with its own `fullnameOverride`
(`archi-crab-okg-run1`), so every object it creates is already name-scoped (Services, StatefulSets,
PVCs, NetworkPolicies select on the release instance label). What staying in one namespace saves:
no ReferenceGrant, no namespace label for the Gateway's listener selector, no second Vault/VSO
path (the runs read the same `okg-archi-crab` Secret; each run has its own Postgres, so sharing
the role passwords crosses no data), and the proxies of the gateway chart reach every run's
Service in-namespace. The cost is only quota: each run is a full okg (runtime + Postgres + two
PVCs), so check the namespace quota before adding run2.

1. **Values:** `envs/run1/values.yaml` from `envs/run1/values.yaml.example` (in this repo): `fullnameOverride: archi-crab-okg-run1`, `repositorySync.revision` and
   `bootstrap.approvedRevision` = the knowledge commit the run studies, `images.*` = the engine of
   that day, storage, `mcp.allowedHosts: [archi-crab-okg-staging.cern.ch]`. Pinned by hand,
   never by the bot (`main.yaml` writes only `envs/staging`). `sources.py lint --base published`
   reads only staging and prod, and `ci.yaml` lints only those two, so a run's file gates
   nothing; add `helm lint … -f envs/run1/values.yaml` to `ci.yaml` once it exists.
   If the proxy reaches the run but the MCP answers 421/403 "invalid Host", add the Service's
   ClusterIP to `mcp.allowedHosts` as staging does (`10.254.109.91:*`) — and note that pin is
   debt: a recreated Service gets a new IP. The better fix is the Service DNS name, which the
   example already lists.
   A per-run source list is fine (`sources/archi-crab-run1.yaml`, `--deployment archi-crab-run1`);
   the best-of-knowledge list stays `sources/archi-crab.yaml`, and v2 follows that one.
2. **Argo:** rename `47-okg-run1-app.yaml.disabled` → `.yaml` in CMSKubernetes.
3. **MCP:** `okg-run1` `enabled: true` in the gateway chart → `archi-crab-okg-staging.cern.ch/run1/mcp`.
   No listener, alias or certificate: the hostname exists.
4. **Console (`/akmon`, `/runN/akmon`):** the console series (`CONSOLE-v0.13`, not on `main`
   yet) already supports a shared hostname with `console.basePath`. On this hostname each
   release sets `basePath` (`/akmon` for staging, `/run1/akmon` for run1) and
   `route.hostname: archi-crab-okg-staging.cern.ch`; its route (`PathPrefix <basePath>`) wins
   over the MCP catch-all and over `/run1`. Three changes to that series, agreed:
   - **Cookies:** oauth2-proxy cookie name **per release** (`_okg_console_<release>`, e.g.
     `_okg_console_archi-crab-okg-run1`) with **path = basePath** and `--proxy-prefix=<basePath>/oauth2`.
     Path alone already keeps `/akmon` and `/run1/akmon` apart (neither path prefixes the other);
     the per-release name keeps them apart even if one release is ever mounted at `/`.
   - **One Application Portal client for all consoles** on this hostname, with one redirect
     URI per release: `https://archi-crab-okg-staging.cern.ch/akmon/oauth2/callback`,
     `…/run1/akmon/oauth2/callback`, `…/run2/akmon/oauth2/callback`. One client secret in Vault.
   - **One bundle per base:** the console image is built per engine run for the base its release
     declares; a run keeps the console image of its own engine (the bundle must match the viz API
     it reads), pinned in `envs/runN` like its runtime image.
   To apply them I need the console series on a branch here (push it as `console`, or attach
   its tarball): it was built in another session and is not in this repository.
5. **The harness.** A condition is a set of MCP servers; the harness connects them exactly as
   above (`claude mcp add` per server, or the SDK), runs the question set, and records per query:
   the answer, every tool call (server, tool, arguments, result hash) for attribution, the okg
   generation id, the v2 corpus fingerprint, and the images' digests. A run whose fingerprints
   moved is discarded. Defaults are v2's (`max_documents=4`, `max_chars=800`, fetch 4000).
   Lives under `bench/` in this repository when it exists.

## 5. What was checked here, and what was not

- **Checked:** the MCP server against archi's real tool factories (e6609f8f) and a stand-in
  data-manager: initialize, `tools/list` (names, schemas, descriptions), the four grep-family
  calls, 401 without the bearer; `render-config.py` through archi's real templates; the v2
  weblist render and its lint gate (18 repositories + 285 pages); the contract check (green
  against e6609f8f); `vendor-sync.sh` is a no-op at the pinned commit; the lock helper's
  fingerprints and stale checks.
- **Not checked here** (no Docker Hub, no helm, no cluster in this sandbox): the image builds
  (base, data-manager, mcp, postgres), the vector server against a real pgvector +
  pg_textsearch, `helm lint`/`template` of both charts, path-aware discovery through
  MCPRemoteProxy. The first three run in `v2-ci` on the phase 1 PR; the last is phase 4's curl.

## 6. Where we are (updated as the runbook is walked)

| step | state | evidence |
|---|---|---|
| Phase 1 PR (`v2-bench`) | **to open** — patches delivered, nothing on `main` yet | `main` = 3430a78 (`staging: pin ffbe61dae`) |
| §3.1 live v2 config | open | placeholder in `v2/deployments/archi-crab/config.yaml` |
| Phase 2.1 first images (`v2-engine` by hand) | not started | |
| Phase 2.2–2.5 Secret, sidecar deploy, smoke | not started | |
| Phase 3 daily loop | not started | |
| CMSKubernetes `archi-crab-paths` (path support, disabled entries) | **to open** — patch delivered; inert until entries are enabled | `archi-crab-testbed` = 2b87114 |
| Phase 4 `archi-crab-v2.cern.ch` + SSO (path prefixes) | not started | ADR-V2-5 risk to check first: `curl -sI …/grep/mcp` |
| Phase 5 run1/run2 (same namespace), console paths, harness | not started | console series needed on a branch for the cookie/base changes |
