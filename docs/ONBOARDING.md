# archi-crab-okg onboarding: the whole picture, then TWiki and private repos step by step

This guide is for the person who runs this repo. Read §0–§2 once, to get the map.
Then §3 (curated TWiki) and §4 (private GitHub/GitLab) are recipes you can follow
with your finger on the page. §5 covers staying close to upstream, and §6 is the
order to do things in.

Every diff quoted here comes from five commits on top of `main` 5f1efc4, delivered as
patch files `0001`–`0005` (they are not pushed anywhere yet). Quoted diffs are abridged
to the lines that matter, so the patches are the full truth:

| Patch | Commit | What |
|---|---|---|
| 0001 | `engine` | archi from `archi-physics/archi-okg` main `1bb7e703`; the build fails on a bad okg pairing |
| 0002 | `helm/okg delta 8` | git credentials for private code repositories (off by default) |
| 0003 | `promote` | copy the image repository with the digest; fix the drift guard |
| 0004 | `tools + docs` | this guide, `scripts/twiki-curate.py`, `data/twiki/README.md` |
| 0005 | `knowledge` | curated TWiki source, CMSSW adapter class, invariant, CI checks. Goes on the engine-bump branch. |

---

## 0. The map: four repositories, one pod

```
 mitdbg/okg (PRIVATE)            archi-physics/archi-okg (PUBLIC)
 the ENGINE: Postgres graph,     the HEP DISTRIBUTION: connectors (python/archi/sources),
 ingest/publish, MCP server,     schema slices (LinkML), bundles/cern-team, skills
 generic modules + sources       (plays the role of "cern-team common modules")
        │ ghcr.io/mitdbg/okg@digest          │ git commit (versions.lock archi.commit)
        └───────────────┬────────────────────┘
                        ▼  build.yaml (docker/runtime/Dockerfile)
            ghcr.io/nausikt/archi-crab-okg@digest    ← ONE image = okg + archi
                        │ pinned in envs/staging/values.yaml
 nausikt/archi-crab-okg (THIS repo, private)       nausikt/CMSKubernetes@archi-crab-testbed
 deployments/archi-crab/  ← WHAT to ingest         argocd/archi-crab/…  ← Argo apps
 helm/okg/                ← HOW it runs            helm/archi-crab/mcp-gateway ← who may ask
 envs/{staging,prod}/     ← pins per env           (MCPRemoteProxy + Cedar, vMCP, OpenWebUI)
                        │ Argo CD syncs helm/okg with envs/<env>/values.yaml
                        ▼
 pod $REL-runtime-0:  repository-sync → bootstrap → runtime-bootstrap → mcp-role   (init)
                      worker + mcp                                                  (main)
   repository-sync: git checkout of THIS repo at repositorySync.revision → /var/lib/okg/repository
   bootstrap:       okg provision --publish-once = migrate + catalog load + ingest ALL sources + publish
   worker:          keeps sources in sync afterwards;  mcp: serves the published graph on :8765
                        ▼
 archi-crab-okg-staging.cern.ch (cms-members only, `query` denied) → Claude Code / OpenWebUI
```

Two pins decide *what code* runs: the okg image digest and the archi commit, both in
`versions.lock` and baked into one image. One pin decides *what knowledge* is loaded:
`repositorySync.revision`, a commit of this repo. That separation is what the CI is
built around:

- `build.yaml` moves the code pins. It builds the image and opens an engine-bump PR.
- `main.yaml` moves the knowledge pin. It runs the e2e, then the bot commits
  `staging: pin <sha>`.
- `promote.yaml` copies both to prod.

## 1. Vocabulary, in one table

| Word | What it is | Where it lives |
|---|---|---|
| **deployment** | one knowledge-graph instance: its modules, schemas, sources, invariants | `deployments/archi-crab/deployment.yaml` |
| **module** | an okg ontology building block that brings subtypes (`extraction` → `document_chunk`, `git_graph` → `source_file`, …) | `deployment.yaml: modules:` |
| **schema slice** | LinkML classes archi adds (`documentation_page`, `cmssw_release`, `site`, …) | `schemas/*.yaml` |
| **bridge / narrowing** | which edge may connect which subtypes (`documentation_page contains document_chunk`). An edge without one is rejected at ingest. | `schemas/bridges/*.yaml` |
| **connector (reader)** | Python class that reads a source and emits facts (nodes and edges) | archi-okg `python/archi/sources/*.py`, or okg's own library |
| **adapter** | the registry-facing wrapper around a reader (`TwikiEOSAdapter` wraps `TwikiEOSSource`). With current archi the registry must name the adapter; a bare reader crashes okg's runner. | same files |
| **source (registry entry)** | one configured connector: class + params + what it promises to emit | `source_registry.yaml: sources:` |
| **params** | the connector's constructor arguments, bound by name. A typo fails before any data moves. | registry entry `params:` |
| **code_repos** | okg's codebase-index expansion: one repo becomes git-files, code-structure, interfaces and doc-corpus sources | `source_registry.yaml: code_repos:` |
| **generation / publish** | ingest writes facts; publish makes a consistent generation the one MCP serves | `okg status` |
| **invariant** | SQL that must return no rows, or the publish is refused | `invariants.yaml` |
| **search profile** | which subtypes `search` ranks | `deployment.yaml: search:` |
| **bundle / profile** | archi's installer recipe (`bundles/cern-team`): answers + modules + source-defaults + schemas → a scaffolded deployment | archi-okg `bundles/` |

## 2. How the cern-team bundle maps onto this repo

Your colleague's cms-kb generates its deployment from a bundle, via
`okg install --profile …`. This repo hand-wrote the same pieces, because the bundle
could not yet produce the code-graph half. Read the bundle and this repo side by side
with this table:

| cern-team bundle (archi-okg `bundles/cern-team/`) | here (`deployments/archi-crab/`) | Owner |
|---|---|---|
| `profile.yaml` `init_questions` (deployment_name, postgres_dsn, archi_data_root, repo URLs, …) | answered by hand: `name: archi-crab`, `dsn: ${OKG_DSN}`, paths via `${OKG_ENVIRONMENT_DATA_ROOT}` / `${OKG_DEPLOYMENTS_DIR}` | ours |
| `modules.yaml`: document_starter, person, extraction, git_graph | `deployment.yaml modules:` same base **plus** dataset, repo_starter, openspec, agent_sessions, compute_env, code_graph, forge, ci (the codebase-index set) | ours |
| `source-defaults/cmssw_releases.yaml` | `source_registry.yaml sources.cmssw_releases` (same entry, variables filled in) | ours, copied from the bundle |
| `source-defaults/twiki_eos.yaml.example` | `sources.twiki`: same reader, pointed at the curated directory (§3) | ours |
| `source-defaults/github_repo.yaml.example` / `gitlab_repo.yaml.example` (okg `GitFilesSource`: files only) | `code_repos:` (okg codebase-index: files **and** symbols, interfaces, docs) | ours |
| `schemas/` (+ `bridges/`) | `schemas/` (+ `bridges/`), copied from the bundle | ours (`VENDOR.yaml` says why) |
| `deployment-defaults.yaml` (release, runtime, nomos, search, chat) | the rest of `deployment.yaml` (runtime on, chat off, the search profile) | ours |
| `invariants.yaml` (`cern_team_core_pages_floor`) | `invariants.yaml` (`archi_crab_core_floor`, `archi_crab_twiki_floor`) | ours |
| `skills/` | `skills/` | ours (copied) |
| — (okg `library/templates/codebase-index/`) | `extractors.yaml`, `schemas/bridges/extraction_to_git_files.yaml` | **vendored** by `scripts/vendor-sync.sh` |

**The cost of hand-writing: upstream fixes don't arrive by themselves.** Example: the
bundle switched `cmssw_releases` from `CMSSWReleaseSource` to `CMSSWReleaseAdapter`
when archi moved to okg's connector SDK. This repo only learns that when the new image
crash-loops. §5 is about closing that gap.

### Anatomy of one registry entry (the TWiki one, annotated)

```yaml
twiki:                                  # the source's name in this deployment
  module: archi.sources.twiki           # Python module inside the image (/opt/archi)
  class: TwikiEOSAdapter                # ADAPTER class (wraps the TwikiEOSSource reader)
  ownership_id: archi-crab.twiki        # who owns the facts this source writes
  admission_policy:
    ...
    output_signature:                   # PROMISE: only these node/edge types. Each must exist
      nodes: [documentation_page, document_chunk]      # in a module or schema slice, and
      edges: [page references page, page contains chunk]  # each edge needs a bridge.
  source_class: discovery_crawl         # these four decide how change and deletion work.
  record_identity_kind: scoped_locator  # Copy the combination the bundle/docstring uses:
  source_revision_kind: content_hash    # okg refuses combinations it does not admit.
  deletion_semantics: missing_from_completed_scope   # a page missing from a COMPLETE run is retracted
  params:                               # = TwikiEOSSource(**params): names must match the
    eos_root: ${OKG_DEPLOYMENTS_DIR}/archi-crab/data/twiki   # constructor exactly (CI binds them)
    web_root: ""
  sync: {triggers: [manual, reconcile], default_event_mode: scope_complete, reconcile_mode: scope_complete}
```

**Where params come from.** The reader's constructor. To list them for any connector,
from the image:

```bash
podman login ghcr.io                                   # the image is private
IMG="ghcr.io/nausikt/archi-crab-okg@$(yq '.images.okg.digest' envs/staging/values.yaml)"
podman run --rm --platform linux/amd64 --entrypoint python "$IMG" -c \
  "import inspect; from archi.sources.twiki import TwikiEOSAdapter as C; print(inspect.signature(C))"
```

`--platform linux/amd64` is needed on Apple Silicon, because the image is amd64 only.

**Where to copy a new entry from:**

1. **First choice:** the bundle's `bundles/cern-team/source-defaults/*.yaml(.example)`
   in archi-okg. They name the **adapter** classes.
2. **Otherwise:** a connector's module docstring (the top of `twiki.py`, `cmssw.py`, …)
   has a registry template, but those templates still name the *bare reader*
   (`TwikiEOSSource`). Swap in the `…Adapter` class defined at the bottom of the same
   module. CI now fails a bare archi reader, with a message saying which adapter to
   use.

---

## 3. Recipe A: add curated CMS TWiki pages (one directory, no EOS in the cluster)

**Idea.** Curate on lxplus, where EOS and your Kerberos ticket already work. Commit the
selected raw topic files into this repo. Argo's `repository-sync` delivers them into the
pod with the rest of the deployment. The reader is archi's ordinary TWiki reader, for
which a curated directory is just a smaller snapshot. No keytab, no EOS mount.

### A1. Why raw topics and not markdown

A snapshot file is the page's TWiki *source*, with metadata lines the reader turns into
graph structure:

```
%META:TOPICINFO{author="meloam" date="1401468455" version="1.10"}%   → author, last_updated, version
%META:TOPICPARENT{name="CRAB"}%                                     → parent_topic + edge to CRAB
---+ CRAB3 Cheat Sheet                                              → "# CRAB3 Cheat Sheet" (markdown style)
[[https://…/CMSPublic/WorkBookCRAB3Tutorial][CRAB3 workbook]]       → text kept; [[Topic]] links → edges
```

Converted markdown loses the parent chain, the dates and the links, so pages become
unconnected text. If your ~300 crawled pages are markdown:

- **Best:** re-fetch them raw (`…/bin/view/<Web>/<Topic>?raw=all`). That needs a CERN
  SSO cookie even for public pages.
- **Fallback:** keep them as markdown and feed them through archi's `docsite` source. It
  reads a `records.json` list of `{title, url, body}`. The pages arrive, but without
  structure.

### A2. Curate (lxplus)

The repo is private, so cloning it on lxplus needs a credential: an SSH key registered
on GitHub, or a fine-grained PAT with Contents read/write on this one repo. The curated
data touches no workflow files, so a PAT without `workflow` scope is enough to push it.

```bash
git clone <this repo> && cd archi-crab-okg && git checkout -b twiki-curated
SNAP=/eos/cms/store/group/internal_comm/twiki
ls $SNAP                                           # which webs exist? (CMS, CMSPublic?)

# 1) dry run: nothing written, a CSV with one reason per topic
python3 scripts/twiki-curate.py --src $SNAP/CMS/topics --out deployments/archi-crab/data/twiki/CMS \
        --report /tmp/curate-CMS.csv --dry-run
```

It prints:

- **Totals per reason:** `name`, `content`, `parent`, `physics`, `exclude`, `unmatched`.
- **Kept pages by name family:** is anything there that shouldn't be?
- **Unmatched pages by name family:** is anything missing from the vocabulary?
- **Near misses:** pages that mention CRAB just under `--min-hits`.

Tune with `--include/--exclude/--content/--min-hits`. They **add** to the built-in
defaults; `--no-defaults` replaces them. Keep the same flags on every run: a real run
**removes** pages from `--out` that the current selection no longer keeps. Then run it
without `--dry-run`:

```bash
python3 scripts/twiki-curate.py --src $SNAP/CMS/topics --out deployments/archi-crab/data/twiki/CMS --report /tmp/c.csv
# only if a CMSPublic snapshot exists:
python3 scripts/twiki-curate.py --src $SNAP/CMSPublic/topics --out deployments/archi-crab/data/twiki/CMSPublic
git add -A deployments/archi-crab/data/twiki && git diff --cached --stat | tail -3   # -A: new files count too
git commit -m "twiki: curated CRAB topics from the EOS snapshot" && git push -u origin twiki-curated
```

Once your tuning flags settle, put them into the script's `INCLUDE`/`EXCLUDE` lists and
commit that, so the next refresh reproduces the same selection.

The selection order, one reason per topic:

| # | Rule | Decision |
|---|---|---|
| 1 | name matches an exclude (`(?i)crab2(?![0-9])`, sandbox) | dropped |
| 2 | name matches the CRAB vocabulary (CRAB, ASO, TaskWorker, SiteStatus, DBS, Rucio, HTCondor, glidein, SubmissionInfrastructure, FTS, XRootD, AAA, WebDAV, CRIC, SITECONF, CMSSW, scram, cmsRun, WMCore) | kept |
| 3 | name is a physics page (archi's physics patterns, which CI keeps identical) | dropped |
| 4 | body has ≥ 3 CRAB mentions (`CRAB3`, `crab submit`, `ASO`, `TaskWorker`) | kept |
| 5 | TOPICPARENT chain reaches a kept page | kept |

**Layout rule:** `data/twiki/<Web>/<Topic>.txt`, never a `.txt` at the top of
`data/twiki/`. The reader, with `web_root: ""`, uses the folder name as the web:

```
data/twiki/CMS/CRAB3CheatSheet.txt      → node twiki:CMS:CRAB3CheatSheet,      https://twiki.cern.ch/twiki/bin/view/CMS/CRAB3CheatSheet
data/twiki/CMSPublic/SWGuideCrab.txt    → node twiki:CMSPublic:SWGuideCrab,    …/view/CMSPublic/SWGuideCrab
[[CMSPublic.SWGuideCrab]] inside a CMS page → edge CMS/CRAB3CheatSheet → CMSPublic/SWGuideCrab (cross-web works)
```

That behaviour was tested against archi-okg main with CMS and CMSPublic pages in one
directory.

**Privacy:** CMS-web pages are CMS-internal.

- **The repo must stay private.** Its README and `helm/okg/values.yaml` still talk about
  "once public"; that plan ends the day these files land.
- **Raw files keep e-mail addresses.** archi redacts them at ingest, so the graph has
  none, but the `.txt` files in git and in git history do.
- **The MCP serves them to `cms-members` only** (§6, debt 1).
- **Think twice about a personal GitHub account** hosting CMS-internal pages.

### A3. The registry entry (actual diff)

```diff
   cmssw_releases:
     module: archi.sources.cmssw
-    class: CMSSWReleaseSource
+    # The ADAPTER, not the bare reader: since archi's connector-SDK migration a
+    # bare reader crashes okg's runner ('ConnectorRun' has no 'next_cursor').
+    class: CMSSWReleaseAdapter
 ...
+  twiki:
+    module: archi.sources.twiki
+    class: TwikiEOSAdapter
+    ownership_id: archi-crab.twiki
+    admission_policy:            # (as annotated in §2)
+      ...
+    params:
+      eos_root: ${OKG_DEPLOYMENTS_DIR}/archi-crab/data/twiki
+      web_root: ""                # one subdirectory per web under eos_root
+      required: true
+      heading_style: markdown     # keep "## headings" and line breaks: <pre> config
+      whitespace: preserve        # blocks stay readable in chunks
```

`${OKG_DEPLOYMENTS_DIR}` is set by the chart (`/var/lib/okg/repository/deployments`) and
by CI (`$GITHUB_WORKSPACE/deployments`). For local runs, export it from the repo root:
`export OKG_DEPLOYMENTS_DIR=$PWD/deployments`. The older `RUNBOOK-v0.7.1.md` still says
`$PWD/okg`, from before the directory was renamed; with that value the TWiki source finds
nothing and fails.

### A4. The rest of the deployment (actual diff)

```diff
 # deployment.yaml
       subtypes:
+        - documentation_page     # TWiki pages become search answers, not only their chunks
         - document_chunk
 # invariants.yaml
+  - name: archi_crab_twiki_floor     # publish refused if there is no documentation_page:
+    severity: error                  # an empty/mis-laid data/twiki fails loudly and names itself
```

No schema change is needed. `documentation_page` and its two bridges
(`documentation_page_contains_chunk`, `documentation_page_references_documentation_page`)
are already in `schemas/`.

### A5. The engine it needs (actual diff, merge FIRST)

```diff
 # versions.lock
-  repository: https://github.com/archi-physics/archi
-  commit: "728739e6"
+  repository: https://github.com/archi-physics/archi-okg
+  commit: "1bb7e703"           # archi-okg main, 2026-09-29
+  tested_with_okg: ac078aabd   # the okg commit archi-okg's own CI uses (we run bed964f)
 # Dockerfile: clone "$ARCHI_REPO"; then fail the BUILD if the pairing is wrong:
+  python -c "from okg.deployment import ConnectorAdapter; from archi.sources.twiki import TwikiEOSAdapter; from archi.sources.cmssw import CMSSWReleaseAdapter"
```

The adapters exist only in the new archi, and the old `CMSSWReleaseSource` crashes with
it. So engine and knowledge must land together, as below.

### A6. Merge order (the only tricky part)

**Why there is an order.** The registry now names adapters that exist only in the new
image, and the old `CMSSWReleaseSource` crashes with the new archi. So the image and the
registry must switch together. The engine-bump PR that `build.yaml` opens is where they
meet: its branch carries the new image digest, and you add the knowledge there.

**Step 1: PR 1 = patches `0001`–`0004`** (engine inputs, chart delta 8, promote fix,
this guide + curate script). All four are inert for the running instance. From your
laptop:

```bash
git fetch origin && git switch -c onboarding-pr1 origin/main
git am /path/to/0001-*.patch /path/to/0002-*.patch /path/to/0003-*.patch /path/to/0004-*.patch
git push -u origin onboarding-pr1        # touches .github/workflows: your token needs `workflow` scope
gh pr create --fill
gh pr list --label engine                # close the stale engine PRs from the old loop (#…-10/11/12, archi 728739e6):
gh pr close <number> --delete-branch     # one per stale PR
```

CI on PR 1 is lint + the old image, so it's green. Merge it. Two things run on `main`:

- `main.yaml` pins staging to the merge (expected: nothing in it changes what runs).
- `build.yaml` builds the new image. Its log must show `engine pairing ok`. If the
  pairing check fails (`ConnectorAdapter` missing), okg `bed964f` is too old for this
  archi: bump `images.okg.ref` to a newer upstream okg image, and never touch `Chart.yaml`
  (debt 3).

**Step 2: on the bot's engine branch**, add the knowledge and the curated data:

```bash
git fetch origin && git switch engine/archi-crab-okg-<n>                        # the PR titled "… @ archi 1bb7e703"
git am /path/to/0005-*.patch
git checkout origin/twiki-curated -- deployments/archi-crab/data/twiki          # the data you pushed from lxplus
git commit -m "twiki: curated CRAB topics" && git push
```

PR CI then checks:

- `lint`: the curated layout. A clear error if `data/twiki` is empty or has top-level
  files.
- `okg-validate`, **inside the new image**:
  - every archi class in the registry is an adapter;
  - every param binds (a typo like `web-root` fails here);
  - the curate script's patterns equal archi's.

  It then loads the catalog and lints the deployment.

**PR CI never runs an ingest with the new engine.** The first ingest happens after the
merge. Before merging, run one locally with the image from this branch; it takes ten
minutes and catches everything CI can't:

```bash
export OKG_IMG="ghcr.io/nausikt/archi-crab-okg@$(yq '.images.okg.digest' envs/staging/values.yaml)"
export OKG_DEPLOYMENTS_DIR=$PWD/deployments            # plus your usual local Postgres/wrapper env
okg migrate --deployment archi-crab --apply && okg catalog load --deployment "$OKG_DEPLOYMENTS_DIR/archi-crab" --apply
okg ingest --deployment archi-crab --inline --progress && okg runtime bootstrap --deployment archi-crab --json
bash scripts/smoke.sh
```

Optional, same place: compare our owned `schemas/` and `skills/` with the new archi's
bundle, and decide whether to adopt changes (debt 6):

```bash
podman run --rm --platform linux/amd64 --entrypoint cat "$OKG_IMG" \
  /opt/archi/bundles/cern-team/schemas/sources.yaml | diff - deployments/archi-crab/schemas/sources.yaml
```

**Step 3: pause Argo, right before merging.**

- **Why pause at all:** merging moves the staging image at once, but the knowledge pin
  only moves after `main.yaml`'s e2e passes. In between, the new image would run the old
  registry.
- **Why the root first:** the staging app is managed by the `archi-crab` app-of-apps with
  `selfHeal`, so the root would restore the child's policy.
- **Why just before merging:** pausing the root freezes every archi-crab app.

```bash
argocd app set archi-crab --sync-policy none
argocd app set archi-crab-okg-staging --sync-policy none
```

**Step 4: merge the engine PR.** Squash keeps history linear. Any method is safe:
`build.yaml` no longer rebuilds when only the runtime pins changed.

**Step 5: wait for the pin, then re-enable.** `main.yaml` ingests the real curated pages
and runs `smoke.sh` and the TWiki invariant. Only when it's green does the bot commit
`staging: pin <sha>`. Check it, then re-enable the root:

```bash
git pull && git log -1 --format=%s && yq '.repositorySync.revision' envs/staging/values.yaml   # == the merge sha
argocd app set archi-crab --sync-policy automated --self-heal --auto-prune
argocd app get archi-crab-okg-staging -o json | jq .spec.syncPolicy                          # automated again (root restored it)
```

**If `main.yaml` is red: stay paused.** Staging is still running the old pair, untouched.
Then choose one:

- **Fix forward:** a new PR with the fix. Its merge re-runs `main.yaml`.
- **Revert the engine PR:** `git revert <squash-sha>`, or `git revert -m1 <merge-sha>`
  for a merge commit. The revert restores the old digest and registry together, and
  `build.yaml` stays quiet because only runtime pins change.

Re-enable Argo only once `repositorySync.revision` equals a green merge.

### A7. Verify

```bash
NS=archi-crab-staging POD=archi-crab-okg-staging-runtime-0
kubectl -n $NS get pod $POD                                     # Running; see the note below on READY
kubectl -n $NS logs $POD -c bootstrap | tail -20                # the publish, including source "twiki"
kubectl -n $NS exec $POD -c worker -- okg status --deployment archi-crab --json | python3 -c \
  "import json,sys; print([x for x in json.load(sys.stdin)['live_subtypes'] if x['subtype'] in ('documentation_page','document_chunk')])"
kubectl -n $NS exec $POD -c worker -- okg search --deployment archi-crab --query "crab submit stageout error"
```

Then ask Claude Code, through `archi-crab-okg-staging.cern.ch`, something only a TWiki
page answers.

- **READY.** The `worker` container stays NotReady, a known upstream issue: readiness
  can't pass under the container supervisor. The MCP Service publishes not-ready
  addresses, so serving is unaffected, but Argo may show the app as
  Progressing/Degraded. Judge by the checks above.
- **No PostSync smoke.** The chart has no PostSync hook yet (`VENDOR-TODO.md` delta 3),
  so nothing runs `smoke.sh` in-cluster automatically.
- **`okg status` shape.** The `live_subtypes` key is the one `okg status --json` printed
  in the 2026-09-20 smoke run.

**Refresh loop:**

1. Re-run the curate script on lxplus with the same flags.
2. `git add -A deployments/archi-crab/data/twiki && git diff --cached --stat`.
3. Commit and open a PR. CI checks it, the merge pins it, Argo rolls it out. No pause is
   needed: data-only changes don't touch the image.
4. Removed pages are retracted automatically, because a complete run without them
   retracts them.

---

## 4. Recipe B: add a private GitHub or GitLab repository

You have two ways to ingest a repository:

| | `code_repos:` (what CRABServer/CRABClient use) | `github_repo` / `gitlab_repo` source (bundle example) |
|---|---|---|
| Engine | okg codebase-index expansion | okg `GitFilesSource` |
| Emits | files, **symbols, interfaces, doc chunks** | files + branch only |
| Use for | code you want to ask questions *about* | a docs-only repo, a quick add |

Both clone the repo themselves (never `git clone` by hand) and fast-forward it on later
runs. For a **private** repo the clone needs a credential. The bundle's note "uses your
own git credentials" assumes a laptop. In the pod, only `repository-sync` has one (the
`git-token` for this repo); `bootstrap` and `worker`, which clone the code sources, have
none. That's what chart delta 8 adds.

### B1. Make a read-only token

- **GitLab (gitlab.cern.ch):** a project (or group) access token, scope
  `read_repository`, role Reporter. For HTTPS git the username can be anything
  non-empty; we use `oauth2`.
- **GitHub:** a fine-grained PAT restricted to the repos you list, **Contents: read**.
  Username `x-access-token`.
- **Rotation:** both expire (GitLab caps tokens at one year). Note the date, and on
  renewal re-run B2 and update the CI secret (B5).

### B2. Put it in the existing Secret (from a file, never on the command line)

First check that nobody else owns the Secret. If a controller (Vault Secrets Operator)
owns it, it will overwrite your key within the hour, and the key belongs in Vault
instead. The chart comment still mentions VSO, but the VSO app is disabled today, so
expect empty output:

```bash
kubectl -n archi-crab-staging get secret okg-archi-crab -o jsonpath='{.metadata.ownerReferences}{"\n"}'
```

Then, portable between macOS and Linux shells:

```bash
W=$(mktemp -d) && chmod 700 "$W"
printf 'token: '; read -rs TOKEN; echo; printf '%s' "$TOKEN" > "$W/t"; unset TOKEN
printf '{"data":{"gitlab-token":"%s"}}' "$(base64 < "$W/t" | tr -d '\n')" > "$W/patch.json"
kubectl -n archi-crab-staging patch secret okg-archi-crab --type merge --patch-file "$W/patch.json"
rm -rf "$W"
kubectl -n archi-crab-staging get secret okg-archi-crab -o jsonpath='{.data}' \
  | python3 -c "import json,sys; print(sorted(json.load(sys.stdin)))"    # key NAMES only; expect gitlab-token
```

### B3. Turn on the credential helper for that host (your values change; the chart side is delta 8)

```diff
 # envs/staging/values.yaml (and prod)
+gitCredentials:
+  hosts:
+    - {host: gitlab.cern.ch, username: oauth2, secretKey: gitlab-token}
```

This renders into `bootstrap` and `worker` only:

```yaml
- {name: GIT_TERMINAL_PROMPT, value: "0"}                     # missing credential = fast failure, no hang
- {name: GIT_CONFIG_COUNT, value: "1"}
- {name: GIT_CONFIG_KEY_0, value: credential.https://gitlab.cern.ch.helper}
- {name: GIT_CONFIG_VALUE_0, value: '!f() { test "$1" = get || exit 0; echo username=oauth2; echo "password=$GIT_CRED_TOKEN_0"; }; f'}
- name: GIT_CRED_TOKEN_0
  valueFrom: {secretKeyRef: {name: okg-archi-crab, key: gitlab-token}}
```

The token is never in the registry, a clone URL, this repo, a file or a command line. It
was tested with real git: the rendered env answers `git credential fill` for
`gitlab.cern.ch` and refuses any other host.

### B4. Declare the repo

```diff
 code_repos:
   base: ${OKG_ENVIRONMENT_DATA_ROOT}/repos
   expand: [git-files, code-structure, interfaces, doc-corpus]
   repos:
     - { slug: crabserver, url: https://github.com/dmwm/CRABServer.git, dir: CRABServer }
     - { slug: crabclient, url: https://github.com/dmwm/CRABClient.git, dir: CRABClient }
+    - { slug: crab-ops,   url: https://gitlab.cern.ch/<group>/<repo>.git, dir: crab-ops }
```

Plain HTTPS URL, no token in it. Keep `git-history` out (the registry header explains
why).

### B5. CI needs the same credential (do this with the first private repo)

Only `main.yaml` ingests (`e2e-smoke` and `chart-path`); `ci.yaml` on PRs never clones
code sources. So a bad or missing token shows up **after** the merge, as a red
`main.yaml` and no staging pin. Set it up in the same PR that adds the repo.

1. Add a repository secret `GITLAB_TOKEN` (Settings → Secrets → Actions).
2. In `main.yaml`, give **both** jobs the same helper the chart renders, at **job**
   level, so every step and every `docker run` can pass it:

   ```yaml
   env:                                    # add to e2e-smoke: env: and chart-path: env:
     GIT_TERMINAL_PROMPT: "0"
     GIT_CONFIG_COUNT: "1"
     GIT_CONFIG_KEY_0: credential.https://gitlab.cern.ch.helper
     GIT_CONFIG_VALUE_0: '!f() { test "$1" = get || exit 0; echo username=oauth2; echo "password=$GIT_CRED_TOKEN_0"; }; f'
     GIT_CRED_TOKEN_0: ${{ secrets.GITLAB_TOKEN }}
   ```

3. Pass them into the containers: add
   `-e GIT_TERMINAL_PROMPT -e GIT_CONFIG_COUNT -e GIT_CONFIG_KEY_0 -e GIT_CONFIG_VALUE_0 -e GIT_CRED_TOKEN_0`
   to **three** `docker run` lines: the wrapper in `e2e-smoke`, the wrapper in
   `chart-path`, and chart-path's background `worker` container, which doesn't use the
   wrapper.

This mirrors the chart exactly (same variable names, same helper), so a clone that works
in CI works in the pod. GitHub masks the secret in logs.

### B6. Verify before trusting an ingest

```bash
kubectl -n archi-crab-staging exec archi-crab-okg-staging-runtime-0 -c worker -- \
  git ls-remote https://gitlab.cern.ch/<group>/<repo>.git HEAD     # prints a sha = credential works
```

This proves the pod's git can clone. The first ingest proves the rest: okg's
clone goes through git, so it uses the same helper. If `ls-remote` works and the
ingest does not, send me the bootstrap log.

---

## 5. Keeping up with upstream okg and archi-okg

### How cms-kb does it (from the colleague's "TWiki extractor" guide)

- **Submodules for both upstreams.** `okg` and `archi-okg` are git submodules, so a bump
  is one commit that moves a submodule SHA. A test (`tests/pytest/test_submodules_clean.py`)
  fails the build on a dirty submodule, and `scripts/sync-archi-schemas.sh` refreshes
  schemas after a bump that touched them.
- **A thin profile on top of cern-team.** `bundles/cms-kb/` holds a `profile.yaml` (its
  own install answers, e.g. `cms_kb_twiki_root`) and `source-defaults/` overrides (e.g.
  `twiki_eos.yaml` with `physics_filter: true`). `okg install --profile cms-kb`
  *generates* the deployment.
- **Upstream first.** "Never add to cms-kb what archi-okg could own". A variant of an
  archi source becomes an *option on the archi source, off by default*, turned on from
  the profile, never a forked connector. Anything CMS-specific that archi cannot own goes
  in `src/cms_kb/`, with a high bar.
- **They run okg from source** (a venv), so a private okg submodule costs them nothing
  extra. We run okg as a **container image** in Kubernetes. That difference matters in
  the table below.

### What we do today, and the proposal

| Concern | Today | Proposal |
|---|---|---|
| archi-okg pin | `versions.lock archi.commit`; the Dockerfile `git clone`s it | **git submodule `vendor/archi-okg`**. The pin is visible in git; Dependabot (`gitsubmodule` ecosystem) opens bump PRs; the Dockerfile `COPY`s it; you can read and grep the exact source and bundle you run. |
| okg pin | upstream **image digest** + `upstream.commit` | **keep the image digest.** okg's image is its release unit, and we don't build okg. A submodule would be a second pin to keep equal to the image's `OKG_CODE_REVISION`. CI already holds `OKG_PAT`, so credentials aren't the obstacle; the duplication is. |
| okg ↔ archi pairing | the build's import check (new) | plus a CI **pairing report**: read the okg commit archi-okg's CI tests against (`vendor/archi-okg/.github/workflows/ci.yml`, today `ac078aabd`) and compare it with the image's `OKG_CODE_REVISION` (`bed964f`). Warn on mismatch; bump the okg image to that commit's tag when one exists. |
| engine vs knowledge rollout | image PR and knowledge pin land separately, so staging needs a paused auto-sync | **build the image on the PR itself** (tag = PR head SHA) and validate the PR's knowledge against *that* image. On merge, one bot commit pins **digest + revision together**. No broken window, no separate engine PR. |
| bundle updates (e.g. the adapter class switch) | invisible until something crashes | **our own thin bundle `bundles/archi-crab/`**, cms-kb style. CI runs `okg install --profile archi-crab --non-interactive --no-publish` into a scratch dir and **diffs it against `deployments/archi-crab/`**. An upstream bundle change becomes a readable diff on the Dependabot PR. `scripts/gen-cern-team.sh` already runs that installer against cern-team, so it's the starting point. *Unverified:* whether `OKG_PROFILES_DIR` accepts two directories (ours + archi's); if not, copy cern-team into `bundles/`. |
| vendored files | `vendor-sync.sh` `docker cp`s from the image | read straight from `vendor/archi-okg` (archi files). okg's two codebase-index files still come from the image. |
| reusable changes | — | **upstream first**, like the topic-scope PR: CRAB vocabulary stays here, mechanisms go to archi-okg |

What the submodule step looks like (proposal, not in the `onboarding` branch):

```bash
git submodule add -b main https://github.com/archi-physics/archi-okg vendor/archi-okg
git -C vendor/archi-okg checkout 1bb7e703 && git add vendor/archi-okg      # the pin IS the submodule sha
```

```yaml
# .github/dependabot.yml already exists (github-actions); APPEND this entry under `updates:`
  - {package-ecosystem: gitsubmodule, directory: "/", schedule: {interval: weekly}, labels: [engine]}
```

Dependabot PRs only see **Dependabot secrets**. Add `GHCR_PAT` (and `OKG_PAT`, if the PR
builds an image) under Settings → Secrets → Dependabot, or `vendor-check` and
`okg-validate` fail on every bump PR.

```dockerfile
# Dockerfile: COPY instead of clone (build.yaml/ci checkout with `submodules: true`)
COPY vendor/archi-okg /opt/archi
RUN uv pip install --python "$(command -v python)" --no-cache /opt/archi/python && python -c "…pairing check…"
```

Order to adopt it, each step useful on its own:

1. Submodule + Dependabot + Dockerfile `COPY`: small, and removes `archi.commit` from
   `versions.lock`.
2. Pairing report in CI.
3. Build on PR + one atomic pin commit. This changes `build.yaml` and `main.yaml` and
   deletes the engine-bump PR dance.
4. Thin bundle + generate-and-diff. First check `okg install --help` in the image for
   a scaffold-only mode, and whether `OKG_PROFILES_DIR` accepts a path list. If it
   doesn't, copy `cern-team` into `bundles/` and diff that copy on each bump instead.

---

## 6. Do it in this order

| # | Step | Where | Done when |
|---|---|---|---|
| 1 | Merge PR 1 (patches `0001`–`0004`) (A6 step 1) | GitHub | `build` log shows `engine pairing ok`; engine-bump PR opened; a `staging: pin` for PR 1 (expected) |
| 2 | Curate the TWiki (A2) | lxplus | `twiki-curate.py` report reviewed, files in `data/twiki/<Web>/` |
| 3 | Engine branch: apply `0005` (knowledge), add curated data, push (A6 step 2) | laptop | CI green: layout, adapters + bind check, catalog load, lint |
| 4 | Local e2e with the engine branch's image (A6 step 2) | laptop | `smoke.sh` prints `SMOKE OK` |
| 5 | Pause root + staging, merge, wait for `staging: pin <sha>`, re-enable (A6 steps 3–5) | argocd / GitHub | revision == merge sha; pod Running (worker NotReady is known) |
| 6 | Verify (A7) | kubectl, Claude Code | `documentation_page` > 0; a TWiki-only question answered |
| 7 | First private repo (B1–B6) | GitLab/GitHub, kubectl | `git ls-remote` from the worker; code subtypes grow |
| 8 | Upstream convergence (§5 steps 1–4) | this repo | Dependabot PRs arrive; bumps are routine |

### Debt and discordances to keep in view

1. **One access path is correct only by accident.**
   - `archi-crab-okg-staging.cern.ch` is protected regardless: its Cedar policy
     (`cms-members`, `query` denied) is rendered from `remoteProxies[].policies` whatever
     `authz.enabled` says.
   - The **OpenWebUI path** (`okg-webui` vMCP) and its `query` deny are Cedar-protected
     only because `CMSKubernetes/helm/archi-crab/mcp-gateway/values-staging.yaml` has
     **two** `authz:` keys and helm keeps the last one (`enabled: true`). Delete the first.
2. **CMS-internal content now sits on github.com under a personal account,** in this
   repo's files and git history. The images don't contain it. Moving the instance repo to
   a CMS organisation (GitHub org or CERN GitLab) is the durable fix. Chunks also reach
   whichever LLM provider OpenWebUI or Claude Code uses, which is a data-governance
   question for CMS.
3. **The chart's `Chart.yaml` is frozen.** `helm.sh/chart` (name + `version`) and
   `app.kubernetes.io/version` (`appVersion`) are both in the immutable volumeClaimTemplates
   labels of both StatefulSets, so changing either fails every sync. Bump the okg engine
   through `images.okg` and `versions.lock` only.
4. **The EOS-mount design is parked,** in the `twiki-eos` series from the previous session
   (mirror sidecar, `eos-probe.yaml`, topic-scope upstream PR), not pushed anywhere.
   Curating on lxplus replaces it. The archi-okg topic-scope PR is still worth offering
   upstream, but nothing here depends on it.
5. **Prod has no Argo CD Application yet.** Promote now copies image repository and digest
   together. Before creating the app, the prod Secret needs the same keys as staging.
6. **Owned schemas and skills lag the pinned archi.**
   - At `1bb7e703` the bundle's `schemas/sources.yaml` adds
     `okg_searchable_text_path_fields: title` and `okg_passage_rollup` to
     `DocumentationPage`. With them, a WikiWord title like `CRAB3CheatSheet` is also
     searched by its parts; without them it's one token.
   - Four skills differ.
   - Diff them on the engine branch (A6 step 2) and adopt what the pinned okg accepts:
     `catalog load` in CI tells you.
7. **The curate script copies archi's patterns.** The physics and skip patterns are
   duplicated, but CI (`okg-validate`) fails the moment they drift from the pinned archi,
   so they can't silently diverge.
