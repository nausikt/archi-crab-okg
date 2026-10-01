# Adding sources and vocabulary, by example

Written against the engine on `main`: okg `0a8e0cd4` + archi-okg `1bb7e703`. Six worked
examples, each a real patch you can apply, read and throw away. Together they cover
everything that decides what the graph ingests. [SOURCES.md](SOURCES.md) is the reference
behind it; this page is the walkthrough.

| # | You want to | You edit | Patch |
|---|---|---|---|
| 1 | turn on repos already in the list | 1 line in the list | `ex1` |
| 2 | add a public repo the list does not have | the list (and decide its size) | `ex2`, on top of `ex1` |
| 3 | ingest a folder of documents (the sanitized TWiki) | the list, the data, `deployment.yaml` (policy, search), `invariants.yaml` | `ex3` (2 commits; the second is sample data, never merge it) |
| 4 | ingest a private GitLab repo | the list, both `envs/*/values.yaml`, three workflows; **then a governance decision** | `ex4`, on top of `ex1`, **do not merge** |
| 5 | update the vocabulary (subtypes) | `VENDOR.yaml`, `schemas/sources.yaml` | `ex5` |
| 6 | use an archi connector nobody uses here yet | `sources/kinds.yaml`, the list, `deployment.yaml` | `ex6`, on top of `ex5` |

To try one, on a branch that has the sources series (`archi-crab-okg-v0.13-sources`
patches on `main`): `git switch -c try && git am <path>/ex1/*.patch`, then run the commands
in its section. Examples 2 and 4 go on top of example 1; example 6 on top of example 5. A
suggested real order is at the end (§8).

---

## 0. What okg needs before it ingests anything

Every fact that reaches the graph has passed four questions. Each one has its own file.

```
                     ┌─────────────────────────────────────────────────────────────┐
  1. WHO READS IT?   │ a reader (connector) + its parameters                       │  sources/archi-crab.yaml  (what)
                     │   archi.sources.* classes, or okg's code_repos lanes         │  sources/kinds.yaml        (how)
                     │                                                             │  → source_registry.yaml   (generated)
                     ├─────────────────────────────────────────────────────────────┤
  2. WHAT ARE THE    │ subtypes and edges the facts use, declared before ingest:    │  deployment.yaml  modules:      (okg half)
     WORDS?          │   okg modules (document_chunk, source_file, code_symbol...)  │  schemas/*.yaml + bridges/      (archi half)
                     │   archi schema slices (documentation_page, cds_record...)    │
                     ├─────────────────────────────────────────────────────────────┤
  3. MAY WE HOLD IT? │ the Nomos posture + one policy per source class             │  deployment.yaml  nomos:
                     │   readiness fails without them                              │
                     ├─────────────────────────────────────────────────────────────┤
  4. WHAT IS AN      │ which subtypes search returns; which must exist after a     │  deployment.yaml  search:
     ANSWER?         │ publish (floors)                                            │  invariants.yaml
                     └─────────────────────────────────────────────────────────────┘
```

What goes wrong when one is missing:

1. **The reader is wrong.** The class does not import, it is a bare reader instead of
   its adapter, or a parameter is misspelled. The run crashes (`sources-contract`,
   `contract-check` catch this).
2. **A word is missing.** Admission refuses the facts, or `okg catalog load` fails
   (`okg deployment lint`, the e2e).
3. **No policy.** The worker never becomes Ready (`nomos.deployment_policy`). Content
   the posture does not allow is a governance breach (`sources-lint`).
4. **Not in search, no floor.** It ingests and nobody finds it, or it silently drops to
   zero (`sources-lint` warns).

**Each file and who writes it:**

| File | Says | Edited by |
|---|---|---|
| `sources/archi-crab.yaml` | which sources, which tier, sensitivity | you, for every source |
| `sources/kinds.yaml` | how a kind becomes registry YAML for this engine | you, rarely (new connector, engine change); engine PR's mechanical renames |
| `deployments/archi-crab/source_registry.yaml` | what okg reads | **nobody**: `python3 scripts/sources.py render --write` |
| `deployments/archi-crab/deployment.yaml` | modules, Nomos posture + policies, search profiles | you |
| `deployments/archi-crab/schemas/*` | archi's vocabulary slice | vendor-sync (after example 5) |
| `deployments/archi-crab/invariants.yaml` | floors that must hold after a publish | you |
| `deployments/archi-crab/data/docs/<id>/` | records for a document source | `scripts/docs-build.py` |

## 1. The loop, for any change

```bash
$EDITOR sources/archi-crab.yaml                 # (and the other files the example names)
python3 scripts/sources.py render --write       # regenerate the registry
python3 scripts/sources.py lint --base published  # offline gates, seconds
python3 scripts/sources.py probe --tier 20      # network: reachable? right branch? how big?
git add -A && git commit && git push            # open the PR
```

The pull request then runs, without you:

- **`sources-lint`, `sources-probe`, `sources-contract`.** The last one runs inside the
  pinned image. Its job summary also carries `sources.py inventory`: the engine's modules,
  templates and Nomos vocabulary.
- **ci's `okg-validate`.** `contract-check.py` runs okg's own Nomos audit, then
  `okg catalog load` and `okg deployment lint`.
- **The e2e.** A real ingest and publish on an empty database.

After the merge, main runs the e2e again and pins staging; Argo CD rolls it out. The
`catalog-claim` init container (chart delta 9) re-claims the database for the new
manifest, since every one of these edits changes it.

Two habits:

- **Never edit `source_registry.yaml`.** If a merge conflicts there, take either side and
  run `render --write`; the file is generated.
- **Read the lint output as a to-do list.** Example 3 shows it walking you through a
  change.

---

## Example 1: turn on repos that are already in the list

**Goal.** Ingest the four public tier-20 repos (das2go, dasgoclient, DBSClient, rucio).
The five MCP repos in the same tier stay off; they still say `enabled: false`.

**The whole change is one line.** The rest of the diff is generated.

```diff
--- a/sources/archi-crab.yaml
 rollout:
-  enabled_tiers: [10]
+  enabled_tiers: [10, 20]
```
```diff
--- a/deployments/archi-crab/source_registry.yaml      (generated by render)
     - {slug: crabclient, url: 'https://github.com/dmwm/CRABClient.git', dir: CRABClient}
+    # das2go -- tier 20 -- DAS server (Go)
+    - {slug: das2go, url: 'https://github.com/dmwm/das2go.git', dir: das2go}
+    # dasgoclient -- tier 20 -- dasgoclient, the DAS command-line client
+    - {slug: dasgoclient, url: 'https://github.com/dmwm/dasgoclient.git', dir: dasgoclient}
+    # dbsclient -- tier 20 -- DBS3 Python client
+    - {slug: dbsclient, url: 'https://github.com/dmwm/DBSClient.git', dir: DBSClient}
+    # rucio -- tier 20 -- Rucio (server, client, daemons); 952 files unscoped
+    - {slug: rucio, url: 'https://github.com/rucio/rucio.git', dir: rucio}
```

**Check it:**

```
$ python3 scripts/sources.py lint --base published
sources lint: ok -- 7 rendered, 13 pending
$ python3 scripts/sources.py probe
das2go       20  ok  master@2301a754c6  100 files  ~4k nodes  .go=34, .tmpl=17, .yml=13, .txt=9
dasgoclient  20  ok  master@d781756487  14 files   ~0k nodes  .md=4, <none>=3, .go=3, .yml=2
dbsclient    20  ok  main@1e6acbd55c    110 files  ~4k nodes  .py=69, .json=19, .sh=9, <none>=3
rucio        20  ok  master@5a4c2e188c  952 files  ~38k nodes .py=582, .js=52, .json=51, <none>=46
```

**Why nothing else changes:**

- **Vocabulary.** A `git` source makes `source_file`, `code_symbol`, `document_chunk` and
  the like. The code modules in `deployment.yaml` already declare them all.
- **Policy.** okg's Nomos audit only covers entries under `sources:`. These go under
  `code_repos:`, and lint confirms each is `public` (a GitHub host without a token).
- **Search and floors.** Both already include code.

**Watch out for:** the e2e time. These four add about 1,180 files to the 512 ingested
today. If the first PR's `e2e-smoke` comes close to 45 minutes, raise `timeout-minutes`
in `e2e.yaml`.

## Example 2: add a public repo the list does not have

**Goal.** Add `dmwm/WMCore`: CRAB runs on its libraries, and `WMExceptions.py` holds the
WM exit codes that the coverage report finds missing.

**Step 1: add the entry.** Lint is happy; the probe is not.

```diff
--- a/sources/archi-crab.yaml
+  wmcore:
+    tier: 20
+    group: extras/data
+    kind: git
+    git: https://github.com/dmwm/WMCore.git
+    branch: master
+    dir: WMCore
+    about: WMCore libraries CRAB runs on; WMExceptions.py holds the WM exit codes
```
```
$ python3 scripts/sources.py probe --id wmcore
wmcore  20  FAIL  master@16a70a1e17  3081 files  ~123k nodes  .py=2003, .js=412, .pkl=150, .json=106;
              3081 files in scope > budget 1500 (raise max_files deliberately, or scope it)
```

**Step 2: make a decision and write it down.** There are two ways out:

- **Raise its budget, deliberately.** That is what the patch does, with the reason next
  to it.
- **Scope it** (`scope: {include: [src/python/**]}`). This waits for scope support (§5 of
  SOURCES.md).

```diff
+    # 3,081 files at 16a70a1e17 (2026-10-01): ~123k nodes, about 2x everything
+    # rendered so far. Accepted on purpose; revisit with a scope (src/python/**)
+    # once scope_fields is verified. Watch the e2e time on this PR.
+    max_files: 3200
```
```
$ python3 scripts/sources.py probe --id wmcore
wmcore  20  ok  master@16a70a1e17  3081 files  ~123k nodes  ...
```

**What you learn here:**

- **The id becomes the identity.** `wmcore` keys every node (`file:wmcore:...`). Pick it
  once; renaming it later is a rebuild, and `lint --base published` refuses a rename.
- **The budget is a size decision, not a formality.** The probe makes it visible before
  CI or the cluster pays for it.

## Example 3: a folder of documents (the sanitized TWiki)

**Goal.** Ingest your converted TWiki pages: public webs only, cited by their TWiki URL.

**Step 1: build the records** where the files are:

```
$ python3 scripts/docs-build.py --src ~/sources/10_sanitized_twikis \
      --out deployments/archi-crab/data/docs/twiki-sanitized --webs CMSPublic --report /tmp/r.csv
files: 9  kept=3 shadowed=1 too_short=1 unsupported=1 web_filtered=3
kept by web: CMSPublic=3  -- every web here must be public for a `sensitivity: public` source
  too_short    CMSPublic_Tiny.md
  unsupported  notes.xlsx
wrote 3 page(s) to deployments/archi-crab/data/docs/twiki-sanitized/records.json
```

That run used 9 test files. With your folder you get about 316 lines in the CSV, one per
file, each with its reason. `--webs CMSPublic` leaves out pages from other webs (the CMS
web is CMS-internal however sanitized). They can become a second, internal source once
the posture allows one (example 4).

**Step 2: switch the source on, and let lint tell you what is missing:**

```diff
--- a/sources/archi-crab.yaml
   twiki-sanitized:
     kind: docs-files
     data: data/docs/twiki-sanitized   # records.json, built by scripts/docs-build.py
-    enabled: false           # until records.json is built and committed (docs/SOURCES.md §3)
```
```
$ python3 scripts/sources.py lint
WARNING: a rendered source produces documentation_page but no invariant floors it -- paste archi_crab_docs_floor back ...
WARNING: a rendered source produces documentation_page but no search profile names it -- add it to deployment.yaml ...
ERROR: source twiki_sanitized has source_class discovery_crawl, and deployment.yaml has no
       nomos.source_policy_defaults.by_source_class.discovery_crawl: okg's audit fails and the worker never becomes Ready
ERROR: twiki-sanitized: say what its content is -- `sensitivity: public` (every page is world-readable) or `internal` ...
```

That is four questions from §0. Each answer goes in its own file.

**Step 3, question 3 (may we hold it?).** Declare what it is, and give its source class
a policy:

```diff
--- a/sources/archi-crab.yaml
     kind: docs-files
+    # Built with `docs-build.py --webs CMSPublic`: every page is from a public web.
+    # CMS-web pages go into a separate, internal source once the posture allows it.
+    sensitivity: public
```
```diff
--- a/deployments/archi-crab/deployment.yaml
   source_policy_defaults:
     by_source_class:
+      discovery_crawl:
+        sensitivity: public
+        data_classification: public
+        credential_ref_policy: none
+        live_call_allowed: false
+        exportability: public
+        retention: normal
+        provenance: remote_api  # CONFIRM against `sources.py inventory` (Nomos vocabulary)
+        privacy_obligations: [audit]
       reference_catalog:
```

The policy is per **source class**, not per source. `discovery_crawl` comes from the
kind (`sources/kinds.yaml`), and every later `discovery_crawl` source with the same
sensitivity reuses this block. Every value copies the `reference_catalog` policy that
main already passes with. `provenance: remote_api` is the one whose meaning may not fit
pages committed to the repo: check the vocabulary in the `sources-contract` job summary,
which lists okg's allowed values. okg's own audit then
judges the block on the PR (ci's okg-validate, contract-check section 5).

**Step 3, question 4 (what is an answer?).** Make whole pages searchable, and give the
source a floor:

```diff
--- a/deployments/archi-crab/deployment.yaml
     content:
       subtypes:
+        - documentation_page
         - document_chunk
```
```diff
--- a/deployments/archi-crab/invariants.yaml      (the parked block, un-commented)
+  - name: archi_crab_docs_floor
+    severity: error
+    ...
+    sql: |
+      WITH required(subtype) AS (VALUES ('documentation_page')),
```
```
$ python3 scripts/sources.py lint --base published
sources lint: ok -- 4 rendered, 16 pending
```

**Step 3, question 2 (the words).** Nothing to do: `documentation_page` is in
`schemas/sources.yaml` (archi's slice) and `document_chunk` is in the `extraction`
module. Apply example 5 first anyway. It makes a page's title searchable by its
component words (separators today; CamelCase like `CRAB3FAQ` once okg#2925 is in the
engine) and rolls chunk hits up to their page, which TWiki pages need.

**In the registry** (generated), a new entry appears under `sources:`. It uses archi's
`DocumentationAdapter`, `records_path:
${OKG_DEPLOYMENTS_DIR}/archi-crab/data/docs/twiki-sanitized/records.json`, and
`source_class: discovery_crawl`. The pod reads the file from the repository checkout
that repositorySync keeps, so there is no volume to mount and no network at ingest.

## Example 4: a private GitLab repo, and where you must stop

**Goal.** Ingest `crab-mcp` from gitlab.cern.ch with a token. The patch wires
**everything**, so you can see every file a private source touches, and lint still stops
it. That is intended.

**The files:**

```diff
--- a/sources/archi-crab.yaml
-    git: https://gitlab.cern.ch/FILL-ME/crab-mcp.git
-    enabled: false
+    git: https://gitlab.cern.ch/cmscrab/crab-mcp.git   # YOUR real path: this group is a guess
```
```diff
--- a/envs/staging/values.yaml   (and envs/prod/values.yaml)
+gitCredentials:
+  hosts:
+    - {host: gitlab.cern.ch, username: oauth2, secretKey: gitlab-token}
```
```diff
--- a/.github/workflows/e2e.yaml
   workflow_call:
     secrets:
       GHCR_PAT: {required: true}
+      GITLAB_TOKEN: {required: false}
 ...  (in BOTH ingesting jobs, e2e-smoke and chart-path)
       OKG_REPO_ROOT: ${{ github.workspace }}
+      GIT_TERMINAL_PROMPT: "0"
+      GIT_CONFIG_COUNT: "1"
+      GIT_CONFIG_KEY_0: credential.https://gitlab.cern.ch.helper
+      GIT_CONFIG_VALUE_0: '!f() { test "$1" = get || exit 0; echo username=oauth2; echo "password=$GIT_CRED_TOKEN_0"; }; f'
+      GIT_CRED_TOKEN_0: ${{ secrets.GITLAB_TOKEN }}
 ...  (on EVERY docker run of $OKG_IMG: two okg wrappers and the background worker)
             -e OKG_DSN ... -e ARCHI_DATA_ROOT \
+            -e GIT_TERMINAL_PROMPT -e GIT_CONFIG_COUNT -e GIT_CONFIG_KEY_0 -e GIT_CONFIG_VALUE_0 -e GIT_CRED_TOKEN_0 \
```
```diff
--- a/.github/workflows/ci.yaml   (and main.yaml: both call e2e.yaml)
     secrets:
       GHCR_PAT: ${{ secrets.GHCR_PAT }}
+      GITLAB_TOKEN: ${{ secrets.GITLAB_TOKEN }}
```

**Outside the repo** (docs/ONBOARDING.md §4 B1–B2):

- a GitLab token with `read_repository`, stored in the `okg-archi-crab` Secret under
  `gitlab-token`;
- a `GITLAB_TOKEN` repository secret.

**Lint follows each piece.** Here is the run with the e2e only half-wired:

```
ERROR: .github/workflows/ci.yaml job e2e calls e2e.yaml without passing secrets.GITLAB_TOKEN -- the e2e clone gets no token
ERROR: .github/workflows/main.yaml job e2e calls e2e.yaml without passing secrets.GITLAB_TOKEN -- ...
ERROR: .github/workflows/e2e.yaml job e2e-smoke: a `docker run` of the okg image does not pass -e GIT_CONFIG_COUNT / -e GIT_CRED_TOKEN_ ...
ERROR: .github/workflows/e2e.yaml job chart-path: a `docker run` of the okg image does not pass ... (x2)
```

**With everything wired, two errors remain**, and they are the point:

```
ERROR: crab-mcp is internal, but the posture (public_reference_demo) allows only ['public'] sources.
       This is the data-governance gate, on purpose: the class must become org_operational_private
       with Nomos runtime enforcement first. Do not widen the public lists
ERROR: sources read gitlab.cern.ch with a token, but the posture says secret_handling: no_secrets
```

okg's own audit would **not** have stopped this: it does not look at `code_repos:`. lint
does, because a private repo makes the public posture untrue (docs/UPSTREAM-SYNC.md "The
posture is a gate"). The way forward is a decision, not a patch:

1. Settle with CMS data governance which non-public content the graph may hold (MCP
   code, CMS-web TWiki, internal docs), and who may read it.
2. Roll out Nomos runtime enforcement. It is its own change: policies for every source,
   lineage, then `deployment_class: org_operational_private` with the matching
   `allowed_source_sensitivities` and `secret_handling`.
3. Rebase this example on top. It then passes lint, and the in-pod probe
   (SOURCES.md §4) proves the pod's token.

A GitLab project whose visibility is **Public** needs none of this: give it `auth: none`
in the list. It is then cloned without a token, and its sensitivity defaults to public.

## Example 5: vocabulary (subtypes): the archi half, and how the okg half works

### 5a. Vendor archi's schema slices (a real, recommended change)

**What.** `schemas/sources.yaml` was hand-copied from archi 6da0d66 and is now behind
the bundle in the image (archi-okg `1bb7e703`). The bundle adds three things:

- **`okg_searchable_text_path_fields: title` on `documentation_page`.** A title's
  component words become searchable (CamelCase such as `CRAB3FAQ` once okg#2925 is in
  the engine).
- **`okg_passage_rollup` on `documentation_page` and `jira_issue`.** A matching chunk
  ranks its page.
- **A new subtype, `cds_record`** (example 6 uses it).

The other three schema files are byte-identical. The note in `VENDOR.yaml` said to
re-vendor "when one archi commit has both". This patch does that.

```diff
--- a/deployments/archi-crab/VENDOR.yaml
   # ---- cern-team bundle: the HEP vocabulary + narrowings (profile `schemas:` slot) ----
+  - {dest: schemas/sources.yaml,            type: file, src: /opt/archi/bundles/cern-team/schemas/sources.yaml}
+  - {dest: schemas/operations.yaml,         type: file, src: /opt/archi/bundles/cern-team/schemas/operations.yaml}
+  - {dest: schemas/bridges/sources.yaml,    type: file, src: /opt/archi/bundles/cern-team/schemas/bridges/sources.yaml}
+  - {dest: schemas/bridges/operations.yaml, type: file, src: /opt/archi/bundles/cern-team/schemas/bridges/operations.yaml}
 ours:
-  - schemas/operations.yaml
-  - schemas/sources.yaml
-  - schemas/bridges/operations.yaml
-  - schemas/bridges/sources.yaml
```
```diff
--- a/deployments/archi-crab/schemas/sources.yaml   (+74 lines, all additions; written by vendor-sync --apply)
   DocumentationPage:
     annotations:
+      okg_searchable_text_path_fields: title
+      okg_passage_rollup:
+        edge_type: contains
+        child_subtype: DocumentChunk
+  CDSRecord:
+    class_uri: archi:CDSRecord
+    attributes: {recid: ..., title: ..., abstract: ..., report_number: ..., ...}
```

From now on, every engine PR keeps these four files current (vendor-check fails if
they drift). Nothing is ingested differently until a source emits these subtypes, but
the catalog changes: delta 9's `catalog-claim` re-claims the database on rollout.

### 5b. okg's modules: how to add one (none of your 20 sources needs one)

okg's subtypes come in **modules**, composed in `deployment.yaml`. This deployment
already composes twelve: the base five (`document_starter`, `person`, `extraction`,
`dataset`, `repo_starter`) and the seven code modules (`git_graph`, `openspec`,
`agent_sessions`, `compute_env`, `code_graph`, `forge`, `ci`). Every planned source
(code, documents, CDS) only uses subtypes these modules or archi's slice declare. You
add a module only when a source emits a subtype that nothing declares yet.

1. **Find it.** The `sources-contract` job summary carries `sources.py inventory`:
   every module in the pinned okg and the subtypes it declares. Locally:
   ```bash
   IMG=$(yq -r '.runtime.ref + "@" + .runtime.digest' versions.lock)
   docker run --rm -v "$PWD:/w:ro" --entrypoint python "$IMG" /w/scripts/sources.py --repo /w inventory
   ```
2. **Add it**, all at once if it comes in a family. Adding the seven code modules one at
   a time cascaded into ~618k `transform_consistency_violations` at publish (the
   comment above `modules:` says so).
   ```diff
   --- a/deployments/archi-crab/deployment.yaml
    modules:
      ...
      - ci
   +  - <module from the inventory>
   ```
3. **Expect bridges to wake up.** `schemas/bridges/*.yaml` hold narrowings marked
   `optional_when_subtypes_missing`. They are skipped while one end's subtype is absent,
   and become strict once a module declares it. `okg catalog load` (ci okg-validate)
   says which.
4. **Search and floors.** Add the new subtypes to `search.profiles.content.subtypes`
   only once a rendered source produces them. lint warns about a searched subtype
   nobody produces, and refuses a floor nobody can satisfy.
5. **Verify.** ci's okg-validate (catalog load + deployment lint) and the e2e prove it.
   Rollout re-claims the database (delta 9).

## Example 6: an archi connector nobody uses here yet (a new kind)

**Goal.** Harvest the CMS Notes OAI set from the CERN Document Server with archi's
`CDSAdapter`. It is public and needs no credential.

This example teaches the mechanics. Whether CMS Notes belong in a CRAB graph is your
call; the computing notes are in that set too.

**Step 1: a new kind,** copied from
`vendor/reference/archi-cern-team-source-defaults/cds.yaml.example` (or the bundle in
archi-okg). Three rules:
- `${deployment_name}` becomes `{{deployment}}`;
- the name becomes `{{id}}`/`{{name}}`;
- the per-source choice moves out to each source's `params:`.

```diff
--- a/sources/kinds.yaml
+  cds-oai:
+    about: CERN Document Server records harvested over OAI-PMH (public endpoint, no credential)
+    render: source
+    requires: []
+    entry:
+      module: archi.sources.cds
+      class: CDSAdapter
+      ownership_id: '{{deployment}}.{{id}}'
+      admission_policy: {... output_signature: {nodes: [{subtype: cds_record}], edges: []} ...}
+      source_class: discovery_crawl
+      record_identity_kind: scoped_locator
+      record_identity_fields: [oai_id]
+      ...
+      params:
+        required: false
+    produces: [cds_record]
```

**Step 2: a source of that kind**, with its own parameters:

```diff
--- a/sources/archi-crab.yaml
+  cms-notes:
+    tier: 20
+    group: cds
+    kind: cds-oai
+    sensitivity: public          # the cerncds OAI endpoint is public
+    about: CMS Notes on the CERN Document Server (computing notes included)
+    params:
+      sets: [cerncds:cms-notes]
```

**Step 3: the vocabulary** comes from example 5 (`cds_record`). **The policy** is the
same `discovery_crawl` block as example 3 (keep one). **Search** gets `cds_record`.

```
$ python3 scripts/sources.py lint --base published
sources lint: ok -- 8 rendered, 13 pending
$ python3 scripts/sources.py contract        # in the image; here with archi 1bb7e703
  note: cms_notes: archi.sources.cds.CDSAdapter binds
  note: ~kind cds-oai: archi.sources.cds.CDSAdapter binds
$ python3 scripts/sources.py probe --id cms-notes
cms-notes  20  skip  no network probe for kind cds-oai (contract binds it; the e2e ingests it)
```

No code change: lint, probe and contract read `requires:` and the rest from the kind.
The e2e is the first real harvest. archi's note says it takes a few minutes; leave
`max_records` unset in production, because a bounded run never claims a complete scope.

---

## 7. Cheat sheet

| I want to... | Change | Run | Gate that would catch a mistake |
|---|---|---|---|
| ingest a tier that is already listed | `rollout.enabled_tiers` | render, lint, probe `--tier N` | probe (size, access), e2e |
| add a public repo | a `kind: git` entry | render, lint, probe `--id` | probe budget; `lint --base` on later renames |
| add documents from files | docs-build; entry + `sensitivity`; Nomos class policy; search; floor | docs-build, render, lint | lint (data, policy, sensitivity, floor), okg audit, e2e |
| add a private repo | entry; `envs/*` gitCredentials; e2e.yaml + callers; Secret; **posture** | render, lint, in-pod probe | lint (wiring, posture gate) |
| use a new archi connector | a kind in `kinds.yaml`; a source with `params:`; vocabulary; policy; search | render, lint, contract | contract (import, adapter, params), okg audit, e2e |
| add vocabulary | vendor (5a) or `modules:` (5b) | vendor-sync, `inventory` | vendor-check, catalog load, deployment lint |
| remove a published source | delete it **and** list it under `retired:` | render, lint `--base published` | lint (identity); the facts stay until a rebuild |
| a class was renamed upstream | nothing: the engine PR runs `contract-check --apply-fixes` → `sources.py rename-class` | (by hand: `sources.py rename-class OLD NEW`) | sources-lint (registry == render) |

## 8. A sensible order for real

1. **Example 5 (vocabulary).** No source changes, and it improves documents later.
2. **Example 1 (tier 20, public).** Watch the e2e time.
3. **Example 3 (sanitized TWiki, CMSPublic only),** with your real `records.json`.
   Confirm `provenance` against the inventory.
4. **Example 2 (WMCore),** if the e2e time from step 2 allows.
5. **Example 6 (CDS),** if you want it.
6. **Example 4 and everything internal** (GitLab docs and MCP repos, CMS-web TWiki,
   curated raw topics) after the governance decision and the Nomos enforcement rollout.
7. **Tier 30**, after the scope keys are known (SOURCES.md §5).

## What was checked, and what was not

- **Checked here:**
  - every example lints clean (example 4 stops at exactly its two intended errors);
  - the render of each is what the diffs show;
  - the docs-files, twiki-raw and CDS kinds bind against archi-okg `1bb7e703`, and the
    data kinds ingest a fixture through archi's real readers;
  - example 4's chart values render the credential into `bootstrap` and `worker` only;
  - the probe numbers are from the real repositories on 2026-10-01.
- **Not checked here** (needs the private image or the cluster):
  - okg's acceptance of the `discovery_crawl` policy values (`provenance` in particular);
  - the module list;
  - a real CDS harvest;
  - the e2e duration with tier 20.

  The PR's `sources-contract` summary (inventory) and ci's okg-validate answer the first
  two. The e2e answers the last two.
