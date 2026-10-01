# Sources: the list, the gates, the rollout

This page covers everything that decides **what the archi-crab graph ingests**. The
engine (okg, archi-okg, the image, the chart) is out of scope here; this is written so
that once the engine is current, the sources go in with no surprises.

## 0. The picture: two inputs, one generated file

```
sources/archi-crab.yaml   WHAT we ingest: ids, tiers, git URLs, branches, scopes, data dirs.
                          Names no okg/archi class. Survives engine bumps unchanged.
sources/kinds.yaml        HOW each kind becomes okg registry YAML for the PINNED engine.
                          All engine-specific data lives here (module, class, params,
                          signatures). Reviewed against archi 1bb7e703 / okg 0a8e0cd4.
        │  python3 scripts/sources.py render --write
        ▼
deployments/archi-crab/source_registry.yaml    GENERATED. What okg reads. Never hand-edited;
                                               CI fails when it differs from the render.
vendor/reference/                              upstream templates the kinds mirror (vendor-sync
                                               copies them from the image; an engine bump shows
                                               their diff next to the kind to adjust)
```

`scripts/sources.py` has eight commands: `render`, `lint`, `status` and `probe` (run
them anywhere), `contract` and `inventory` (inside the pinned image), `verify` (against
an ingested database) and `rename-class` (the mechanical fix for an upstream rename).
`scripts/docs-build.py` turns a folder of pages into the data one kind reads.

The first render is a **no-op** for what is live: with the curated TWiki switched on,
it reproduces the onboarding registry exactly. Without it, it reproduces main's
`code_repos` and `cmssw_releases`, apart from the adapter class fix.

Outside kinds.yaml, `sources.py` still relies on a few engine facts, each checked where
it is used:
- the two render modes a kind can name (`render: code_repos` or `render: source`) and
  the two data checks (`data_check: records-json` or `twiki-tree`); everything else
  about a kind is data in kinds.yaml (§2.1);
- `okg.deployment.ConnectorAdapter` and the readers' `run()` result (`contract`);
- node ids `file:<slug>:<path>` in `okg.v_nodes` (`verify`);
- the `versions.lock` keys (`contract`'s review warning);
- archi's TWiki pattern modules (the twiki-curate comparison).

If one of them moves, the command that uses it fails loudly rather than passing.

## 0.1 How this plugs into the engine track (okg 0a8e0cd4, archi-okg 1bb7e703)

The engine catch-up is merged (`main` 58c6412, staging pinned at `bff281ef6`). This
series sits on top of it:

- **No-op for what is live.** On `main` the render is byte-for-byte the same registry,
  YAML-equal to the hand-written one (crabserver, crabclient, cmssw_releases with
  `CMSSWReleaseAdapter`).
- **Mechanical fixes land in kinds.** `scripts/contract-check.py --apply-fixes` (run by
  `engine.yaml` on the engine PR) now renames a class in `sources/kinds.yaml` through
  `sources.py rename-class` and re-renders, instead of editing the generated registry.
  The engine workflow commits `deployments/` and `sources/` together.
- **One image.** `sources-contract` tests `versions.lock`'s `runtime.ref@digest`, the
  same image `ci.yaml` and `e2e.yaml` test. `contract-check.py` (in ci's okg-validate)
  covers the rendered registry, okg's CLI, vendored paths and okg's own Nomos audit.
  `sources.py contract` adds the kinds nothing renders yet, the fixture ingests and the
  code_repos scope keys. `sources.py inventory` lists what it can find in the image
  (modules, templates, Nomos vocabulary). It is a reading aid: okg's own audit, `okg
  catalog load` and `okg deployment lint` stay the authority on what is accepted.
- **The e2e is reusable.** `e2e.yaml` runs on PRs (from ci.yaml) and on main (from
  main.yaml), and only gets the secrets its callers pass. lint follows that chain for
  the GitLab token (§4).
- **The Nomos posture is the gate for anything non-public.** `deployment.yaml` declares
  `public_reference_demo`. lint checks every source against it offline, including
  `code_repos`, which okg's own audit does not see (§6, docs/ADDING-SOURCES.md 4).

## 1. The list today

`python3 scripts/sources.py status` prints this. The sizes are from `probe --all` on
2026-09-30 (files after scope; nodes estimated at 40 per file, measured on staging:
crabserver 414 files → 15,572 code nodes).

| id | tier | kind | state | size | next step |
|---|---|---|---|---|---|
| crabserver | 10 | git | **rendered** | 413 files, ~16k nodes | live |
| crabclient | 10 | git | **rendered** | 99 files, ~3k | live |
| cmssw-releases | 10 | cmssw-releases | **rendered** | 5,032 releases | live |
| cms-analysis-docs | 10 | git (GitLab) | pending | ? | GitLab path; governed posture if private (§4) |
| cms-crab-docs | 10 | git (GitLab) | pending | ? | GitLab path; governed posture if private (§4) |
| cmscrab-userguide | 10 | git (GitLab) | pending | ? | GitLab path; governed posture if private (§4) |
| twiki-sanitized | 10 | docs-files | pending | your 316 files | build records with `--webs CMSPublic`, declare `sensitivity` (§3) |
| twiki | 10 | twiki-raw | pending | curated EOS topics | `internal`: needs the governed posture |
| crab-mcp, dbs-mcp, htcondor-mcp, rucio-mcp, site-status-mcp | 20 | git (GitLab) | pending | ? | governed posture, then GitLab paths (§4) |
| das2go | 20 | git | tier off | 100 files, ~4k | enable tier 20 |
| dasgoclient | 20 | git | tier off | 14 files | enable tier 20 |
| dbsclient | 20 | git | tier off | 110 files, ~4k | enable tier 20 |
| rucio | 20 | git | tier off | 952 files, ~38k | enable tier 20 |
| cmssw | 30 | git + scope | blocked | 623 of 62,655 files | scope support (§5) |
| cms-sw-github-io | 30 | git + scope | blocked | 46 of 81,204 files | scope support (§5) |
| htcondor | 30 | git + scope | blocked | 352 of 4,954 files | scope support (§5) |

**Tiers are rollout waves**, taken from the 10_/20_/30_ prefixes of your tree. okg
publishes all sources or none: *one* source that cannot read its input fails the
completeness gate and blocks the publish for every other source (archi-okg
`bundles/cern-team/profile.yaml`). So a tier goes in only after its probe is green, and
tiers are widened one per PR (`rollout.enabled_tiers`).

A source is rendered when its tier is enabled **and** it does not say `enabled: false`.
`enabled: false` means the input is not ready yet (unknown path, data not built). It is
**not** a way to remove something already published (§7).

## 2. The kinds: what each one does in the graph

| kind | engine path (sources/kinds.yaml) | emits | proven |
|---|---|---|---|
| `git` | okg `code_repos` codebase-index: each repo becomes `<id>.git-files`, `.code-structure`, `.interfaces` and `.doc-corpus`. git-history stays out (concurrency bug) | source_file, code_symbol, code_import, code_reference, interface_endpoint, document_chunk, entity_mention | staging, public GitHub |
| `docs-files` | archi `DocumentationAdapter` over one `records.json` | documentation_page, document_chunk | archi, ingest-proven 2026-08-11. Also run here with archi 1bb7e703 on docs-build output: complete scope, pages + chunks + `contains` only |
| `twiki-raw` | archi `TwikiEOSAdapter` over `<Web>/<Topic>.txt` | documentation_page, document_chunk (+ topic references) | archi parity corpus |
| `cmssw-releases` | archi `CMSSWReleaseAdapter`, public releases.map | cmssw_release | staging |

Why the GitLab **documentation** repos use `git` and not archi's GitLab docs downloader:
`git` keeps itself current (the clone fast-forwards on every reconcile), goes through the
same credential path as the MCP repos, and the doc-corpus lane chunks Markdown by
heading. The downloader would mean a manual rebuild and a committed cache for every
change.

### 2.1 The fields of a kind (what you write in kinds.yaml)

A kind is data. `sources.py` reads these fields; nothing about a specific kind is
hard-coded (docs/ADDING-SOURCES.md example 6 adds one).

| field | meaning | checked by |
|---|---|---|
| `render` | `code_repos` (the entry joins okg's `code_repos.repos`, through `repo_entry`) or `source` (a full entry under `sources:`, from `entry`) | render |
| `entry` / `repo_entry` | the registry YAML, with `{{id}}`, `{{name}}`, `{{deployment}}`, `{{data}}`, `{{git}}`, `{{dir}}` filled in; `${VAR}` passes through to okg | render; `contract` imports `entry.module`/`class` |
| `requires` | per-source fields a source of this kind must set (`git`, `data`, ...) | lint |
| `data_check` | `records-json` or `twiki-tree`: lint validates the committed data, `contract` ingests a fixture through the real reader | lint, contract |
| `params_required` | `{key: list\|str\|int\|bool\|mapping}`: params each source must give, non-empty | lint |
| `params_overridable` | keys of `entry.params` a source may override. Every other key in `entry.params` is fixed by the kind (data paths, safety switches) and lint refuses a source that sets it | lint |
| `produces` | the subtypes it emits: lint uses it for floors and search profiles | lint |
| `scope_fields` | (git only) the repo-entry keys for `scope`; `null` = not verified, scoped sources are refused | lint, render, probe, contract |
| `about`, `proven`, `comment` | for humans; `proven` says where it last ran for real | — |

Per source, the list may then set `params:` (merged over `entry.params`), `sensitivity:`
and `auth: none` (§4).

## 3. The sanitized TWiki folder → `twiki-sanitized`

Your 316 Markdown/HTML/PDF files become one `records.json` that archi's documentation
reader ingests. Build it where the files are:

```bash
python3 scripts/docs-build.py \
    --src ~/sources/10_sanitized_twikis \
    --out deployments/archi-crab/data/docs/twiki-sanitized \
    --report /tmp/twiki-sanitized.csv --dry-run          # read the summary + CSV first
```

- **Identity = URL.** `CMSPublic_CRAB3FAQ.md` becomes
  `https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ`: the node is keyed by it,
  and every answer cites it. Names that are not `<Web>_<Topic>` go in `--urls map.tsv`
  (`<file name><TAB><url>`). Otherwise they are refused and listed.
- **One page per URL.** If a page exists as md + html + pdf, md wins, then html, then pdf
  (the others show as `shadowed` in the report).
- **Refused, with the reason in the CSV:** no URL, empty or under 200 characters, or a
  CERN login page captured instead of the page (`login_page`). Subfolders are listed as
  `subdir_skipped` (not recursive).
- **Emails** are replaced by `<email>` (`--keep-emails` to opt out). Command look-alikes
  are left alone: `git@github.com:…`, `user@host:path` and `user@lxplus.cern.ch`.
- **HTML:** on a rendered TWiki page, only the `patternTopic` div is kept. That drops the
  breadcrumb, the edit bar, the revision line and "uploaded by". Only `<div>` nesting is
  counted, so unclosed `<p>` or stray `</span>` tags do not cut the page short. If no
  topic body is found, the whole page is kept and the CSV says so.
- **PDF** needs `pip install pypdf` (or poppler's `pdftotext`). `build.json` records
  which one was used, since switching changes every PDF's text.
- **Public webs only, for a public source.** `--webs CMSPublic` keeps only those webs
  (the others show as `web_filtered`), and the summary counts kept pages per web. The
  source's `sensitivity: public` is a claim about every page in it.
- **Overlap:** if a page is also in `data/twiki/` (curated raw topics), it is reported.
  The same page would otherwise be ingested twice under two ids, so keep it in one source.

Then, in **one PR**: drop `--dry-run`, commit `data/docs/twiki-sanitized/`, delete
`enabled: false` from `twiki-sanitized`, paste `archi_crab_docs_floor` back into
`invariants.yaml` (it is parked there as a comment; lint warns until you do), and run
`python3 scripts/sources.py render --write`. `lint` checks that the file is
well-formed, has no duplicate, empty or login-page records, and that no two docs sources
claim the same URL.

Rebuilding later works the same way. The output is sorted with one record per line, so
the PR diff shows exactly which pages changed. Pages that disappear keep their old facts
live (§7); lint warns about them against what is published.

## 4. A GitLab source (docs repos, MCP servers)

The GitLab paths are not known here (the MCP images live in Harbor project `cmscrab`,
which says nothing about the GitLab group).

**First, the governance gate.** A repository read with a token is not public. Today's
posture (`public_reference_demo`, `secret_handling: no_secrets`) cannot hold it, and lint
says so even though okg's audit would not notice a private repo under `code_repos`. The
posture must become `org_operational_private` with Nomos runtime enforcement on. That is
a CMS data-governance decision and a rollout of its own (docs/UPSTREAM-SYNC.md "The
posture is a gate"). docs/ADDING-SOURCES.md example 4 shows every other file and where
lint stops. Once the posture allows it, for each repo:

1. Put the real URL in `git:` (`https://gitlab.cern.ch/<group>/<repo>.git`, **no token
   in it**; lint, render and probe refuse credentials in a URL, and never print one).
2. **Once per host**, wire the token. These are docs/ONBOARDING.md §4 B1–B5; lint
   checks (a) and (b):
   (a) `gitCredentials.hosts: [{host: gitlab.cern.ch, username: oauth2, secretKey: gitlab-token}]`
   in `envs/staging/values.yaml` **and** `envs/prod/values.yaml`,
   (b) `e2e.yaml` (the reusable e2e both ci.yaml and main.yaml call) declares
   `GITLAB_TOKEN` under `on.workflow_call.secrets`, and both callers pass it. Each
   ingesting job (`e2e-smoke`, `chart-path`) sets `GIT_CONFIG_COUNT`,
   `GIT_CONFIG_KEY_0: credential.https://gitlab.cern.ch.helper`, `GIT_CONFIG_VALUE_0` and
   `GIT_CRED_TOKEN_0: ${{ secrets.GITLAB_TOKEN }}`. Every `docker run` of `$OKG_IMG`
   passes `-e GIT_CONFIG_COUNT -e GIT_CONFIG_KEY_0 -e GIT_CONFIG_VALUE_0 -e GIT_CRED_TOKEN_0`.
   lint checks each of these per job; a comment does not count,
   (c) the token itself, in the `okg-archi-crab` Secret and the `GITLAB_TOKEN` repo secret.
3. Probe it **from the pod**. This is the authoritative check, with the pod's own
   credential and network. From stdin, the script finds the synced checkout through
   `$OKG_REPO_ROOT`:
   ```bash
   kubectl -n archi-crab-staging exec -i archi-crab-okg-staging-runtime-0 -c worker -- \
     python - probe --manifest-b64 "$(base64 -w0 sources/archi-crab.yaml)" --id crab-mcp \
     < scripts/sources.py
   ```
   It reports ok with the branch, head, file count and extensions; FAIL with the reason
   ("not found" on GitLab also means "no access"; an empty repo fails too); or skip when
   the pod has no credential for the host. The `sources` workflow runs the same probe with
   `GITLAB_TOKEN`, if that secret exists, on every PR and weekly in strict mode.
4. Remove `enabled: false`, `render --write`, and open the PR.

The token needs `read_repository` on every listed project: a group access token on
the group, or one project token per repo. It expires (GitLab caps tokens at one year).
The weekly strict probe is what tells you before a reconcile does.

**A GitLab project whose visibility is Public** needs none of the above: give the source
`auth: none`. Its sensitivity then defaults to `public`, and two rules keep that claim
honest:

- **probe clones it anonymously** (no credential helper, no global or system git config),
  so a project that is really private fails the probe instead of passing on a token
  you happen to have;
- **a held credential overrides `auth:`.** git applies a credential helper per host,
  so if the deployment holds a token for the host (`gitCredentials` in `envs/*`, or a
  helper in an ingesting CI job), the pod and the e2e clone with it whatever the source
  says. Under `secret_handling: no_secrets` lint refuses any held credential, even when
  every source on that host says `auth: none`.

## 5. Tier 30: scoped repositories

cmssw (62,655 files), cms-sw.github.io (81,204, almost all dashboard data) and htcondor
(4,954) are only worth ingesting in part. Their `scope.include` picks the parts CRAB
questions need: the cmsRun exit codes, file open/read, the storage adaptors, the
site-local config, edmFileUtil and edmDumpEventContent; the cms-sw pages; the HTCondor
manual.

The blocker is that **we do not know how the pinned okg restricts a `code_repos` repo to
globs**. The extractor config says the doc-corpus lane takes include/exclude globs "from
the source_registry entry", but the code_repos key that feeds them is not visible
without okg's source. If okg silently ignored a key we guessed, it would ingest the
whole repo (cmssw: ~2.5M nodes). So `kinds.yaml` has `git.scope_fields: null`, and lint,
render and probe all refuse to enable a scoped source until that is resolved. To resolve
it:

1. After the next `vendor-sync --apply` (the `engine/upstream` PR does it), read
   `vendor/reference/okg-codebase-index/`: its registry template shows the per-repo keys
   and their glob dialect (in `probe`, `*` stays within a directory and `**` crosses
   directories).
2. Set `git.scope_fields: {include: <key>, exclude: <key>}` in `kinds.yaml`.
3. `contract` fails if the pinned okg never reads those keys near its `code_repos`
   handling, and prints every file that handles `code_repos` as evidence. Passing it is
   necessary, **not sufficient**: a common key name can appear there for another reason.
4. **The proof is `verify` after the ingest.** It counts `source_file` nodes per repo
   and fails when a repo exceeds its budget, or its probed in-scope count. Add it to
   `e2e.yaml`'s `e2e-smoke` job, after the ingest step, in the PR that enables tier 30:
   ```yaml
   - run: python3 scripts/sources.py probe --json probe.json   # sizes to compare against
   - run: |
       docker run --rm --network host -v "$GITHUB_WORKSPACE:/w:ro" -e OKG_DSN \
         --entrypoint python "$OKG_IMG" /w/scripts/sources.py --repo /w verify --probe /w/probe.json
   ```
   A red `verify` blocks the staging pin, so a scope okg ignored never reaches the cluster.
5. Run `probe --tier 30` (Actions → sources → Run workflow, `tier: 30`), then enable the tier.

If okg has no per-repo scoping, the fallback is an explicit per-lane source block. The
same reference template shows that shape too, and it becomes a second kind in
`kinds.yaml` with no change to the list.

## 6. The gates, and the failure each one prevents

Make `sources-lint` and `sources-contract` **required checks** on main, next to ci's
`lint` and `okg-validate`. The job names are distinct from ci's, so each requirement is
unambiguous.

| gate | where | catches |
|---|---|---|
| duplicate or unknown keys; empty scope; bad types | `lint`, every PR | a pasted second `enabled:`, a typo like `enable: false`, or `scope: {}` silently changing what is ingested |
| registry == render | `lint` | hand edits; forgetting `render --write` |
| URL, host, placeholder and duplicate-repo checks | `lint`, `render`, `probe` | FILL-ME paths going live; tokens in clone URLs (any case, never echoed); the same repo under two ids |
| token host wired in both envs + every CI job that ingests (job env with helper, value, count and a token from a secret; `-e` flags on each `docker run` of the okg image; the secret declared by `e2e.yaml` and passed by its callers) | `lint` | the pod or the post-merge e2e cannot clone, so staging never gets its pin |
| data present and sane | `lint` | empty or garbled `records.json` (archi reports `cache_missing` and blocks the publish); login pages ingested as content; two sources owning one URL |
| every rendered source has a Nomos policy for its source_class, and that policy's sensitivity matches the source's; every source's `sensitivity` is allowed by the posture; under `secret_handling: no_secrets`, no token host and no held credential (envs `gitCredentials`, CI helpers) | `lint` (and okg's own audit in contract-check §5) | a worker that never becomes Ready (`nomos.deployment_policy`); a private repo or CMS-internal pages slipping into a public posture, which okg cannot see for `code_repos`; an `auth: none` source cloned with a token after all |
| a kind's `requires`, `params_required` and fixed params | `lint` | a source missing what its reader needs, or overriding a data path or safety switch the kind owns |
| every invariant floor has a producer (and search profiles, as a warning) | `lint` | a permanent error-severity failure after every publish. It caught the old twiki floor on this branch, with no twiki source rendered |
| nothing **published** vanished, was renamed or re-pointed; docs pages or topics removed | `lint --base published` | stale facts okg never retracts (§7). A planned removal goes under `retired:` (durable, so later PRs are not blocked); the label `rebuild-planned` waives the gate for one PR |
| reachable, right branch, non-empty, within budget; `auth: none` sources cloned anonymously | `probe` (PRs, weekly strict, pod) | wrong path or no access; expired token; default-branch drift; a repo far bigger than planned; a "public" project that is not |
| every kind imports, is an adapter, binds its params; data kinds ingest a fixture within their signature | `contract`, inside the pinned image | engine bumps that rename a class or parameter, or change what a reader emits; bare readers (`'ConnectorRun' has no 'next_cursor'`); **before** the PR that enables a kind |
| scope keys appear in okg's code_repos code | `contract` | a guessed scope key (necessary, not sufficient) |
| kinds reviewed against this engine | `contract` (warning) | an engine bump nobody re-read the templates for |
| per-repo file counts after the real ingest | `verify` (e2e, pod) | a scope that was ignored; a lane that emitted nothing |
| `okg deployment lint` | ci.yaml (unchanged) | okg's own registry rules (profile combinations, strict admission) |
| the real ingest | the e2e (`e2e.yaml`: on PRs from this repository, and again on main) | anything left: staging is only pinned after it passes |

## 7. Things that bite

- **okg does not retract what disappears** (archi-okg `bundles/cern-team/README.md`: facts
  that leave a completed scope stay live, even with `missing_from_completed_scope` and a
  reconcile). This affects:
  - **Sources.** Removing, renaming or disabling a published one leaves its nodes live
    and stale. A git source's id is its slug and keys every node (`file:<id>:<path>`),
    so renaming it re-keys everything.
  - **Records.** A file deleted upstream in a git repo, or a page dropped from a
    `records.json` rebuild, stays in the graph.

  lint refuses the first against what is published: a vanished id, and also a slug
  re-pointed at another repository. Record a planned removal under `retired:` with its
  date and reason. lint warns on dropped pages and topics. For the rest, the remedy is
  the same: a periodic **rebuild** (fresh database) once stale content matters. Check
  whether a newer okg fixed retraction when you catch up.
- **Things change between PRs.** Git sources follow upstream: a token expiry, a moved or
  archived project, a default-branch rename, or a repo outgrowing its budget fails at the
  next reconcile and blocks every source's publish. The weekly strict probe is the early
  warning; act on a red one.
- **Cross-source references are off on purpose.** archi's documentation reader can link
  chunks to `cmssw_release` nodes (`releases_map_path`), but a configured reference file
  that is missing at run time raises. cmssw-releases writes that map during the same
  bootstrap, so the first run could race it. Turn it on only after a first green publish,
  as a kind change.
- **CI time grows with each tier.** The e2e ingests the whole registry in two jobs with
  45-minute limits. Tier 20 adds about 1,180 code files to today's 512, roughly 3.3×.
  Watch the first tier-20 run of `e2e-smoke` and raise `timeout-minutes` if needed, or
  give CI a smaller render. That second option is not built.
- **Two TWiki paths.** `twiki-sanitized` (your converted pages) and `twiki` (raw curated
  topics) can hold the same page under two ids. docs-build reports the overlap; pick one
  source per page.

## 8. The order from here

1. **Merge this series.** It changes nothing that is live (§0.1). The next engine PR
   runs `vendor-sync --apply`, and `vendor/reference/` appears with okg's codebase-index
   template and archi's connector templates. The sources-contract job summary carries
   `sources.py inventory`: the modules, templates and Nomos vocabulary it finds in the
   pinned image (okg's audit stays the authority).
2. **Public repos, now.** `enabled_tiers: [10, 20]` renders das2go, dasgoclient,
   dbsclient and rucio; the five MCP repos stay off until their paths are known
   (docs/ADDING-SOURCES.md example 1). A new public repo is the same, plus a probe and a
   budget decision (example 2).
3. **The sanitized TWiki, public webs only.** Build it with `--webs CMSPublic`, declare
   `sensitivity: public`, and add the `discovery_crawl` policy, the docs floor and
   `documentation_page` in search (example 3).
4. **Anything non-public: a decision first.** The GitLab docs and MCP repos, CMS-web
   TWiki pages and the curated raw topics all need the posture to become
   `org_operational_private` with Nomos runtime enforcement. Settle that with CMS data
   governance and roll it out on its own; then the wiring in example 4 goes in.
5. **Tier 30**, once §5 is resolved: `probe --tier 30`, add `verify` to the e2e, then
   enable the tier.

Each merge is proven by the e2e before staging is pinned. Prod follows through
Promote as before. Use one PR per source family, so a red e2e names its cause.
