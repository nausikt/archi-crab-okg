# Staying on okg `dev` and archi-okg `main`, daily (v0.12)

This replaces the manual engine bump. After it lands, one pull request, `engine/upstream`,
always carries the newest upstream. You read its summary, approve, merge. Staging follows
by itself.

Patches `0001`–`0004` apply on `main` at `5f1efc4`. Read §1–§3 once; §4 is the rollout.

---

## 1. What was established first (2026-09-30)

| Fact | Evidence | Consequence |
|---|---|---|
| okg's working branch is `dev`. Every merge publishes `ghcr.io/mitdbg/okg:dev` and `:sha-<commit>`, and the same two tags for `okg-postgres`. The commit is in the image label `org.opencontainers.image.revision`. | okg `.github/workflows/container-images.yml`, `Dockerfile` | Follow the **image tag** `dev`; read the commit from the image. No okg build here. |
| archi-okg has **no** `dev` branch. Merges land on `main`. `archi_v3_quickstart` (head `6da0d66`, 2026-09-16) is fully contained in archi-okg `main` and has not moved since. | `git ls-remote`, `git merge-base --is-ancestor` | Follow archi-okg `main`. The project instruction naming `archi_v3_quickstart` is out of date. |
| We are 6,237 commits (445 merged changes) behind on okg and 288 commits (49 merged changes) behind on archi-okg. | `scripts/upstream-summary.py` on real clones | One catch-up bump, then small daily ones. |
| The Graph view is the operator console's fifth view. It merged into okg `dev` on 2026-09-28 (PR 2772). | `git log`, `docs/develop/ui/operator-console.md` | Neither our pin (`bed964f`) nor the commit archi-okg tests against (`ac078aabd`) has it. It needs current `dev`. okg's own chart does not serve the console, so showing it in the cluster is a separate chart change. |
| archi-okg `main` works with okg `dev` head at unit level. | archi-okg's suite against okg `2af2fadbe`: 1,264 passed. The snapshot tests were excluded; they need the `zstd` command, which the test machine lacked. | The pairing at head is plausible. Only the e2e on the pull request proves it. |
| Every okg command and flag our workflows, chart and smoke test call still exists at `dev` head. | `scripts/contract-check.py` | No CLI change is needed for the catch-up. |
| Exactly one registry break at head: `cmssw_releases` names the bare reader `CMSSWReleaseSource`; current archi runs `CMSSWReleaseAdapter`. | `scripts/contract-check.py` against okg `2af2fadbe` + archi-okg `1bb7e703` | Fixed mechanically by the workflow, as its own commit. |
| The contract check passes on the engine staging runs today. | same script against okg `bed964f` + archi `728739e6` | The patches' own pull request can be green before any bump. |

## 2. How it works

```
 okg :dev image ──┐                                   engine.yaml  (daily 03:17 UTC, or by hand)
 archi-okg main ──┴─► resolve pins ─► build image ─► resync vendored files ─► contract check
                                                     (+ mechanical fixes) ─► summary
                                                                │
                              pull request  engine/upstream  ◄──┘   one, rolling, never auto-merged
                                                │  ci.yaml: lint · vendor-check · okg-validate
                                                │           (+ contract check) · e2e (ingest + smoke)
                                        you: read summary, approve, merge
                                                │
                              main.yaml: e2e again on main ─► bot commit "staging: pin <sha>"
                                                │             image + knowledge revision TOGETHER
                                        Argo CD rolls staging      Promote copies the same to prod
```

| File | Role |
|---|---|
| `versions.lock` | The only place engine pins live. You edit what is **followed** (`upstream.track`, `archi.repository`, `archi.branch`); the workflow writes the rest. |
| `.github/workflows/engine.yaml` | Replaces `build.yaml`. Resolve, build, propose. |
| `.github/workflows/e2e.yaml` | The ingest, smoke and chart-path jobs, callable. Runs on pull requests and again on `main`. |
| `scripts/upstream-resolve.sh` | Newest okg commit that has **both** a runtime and a postgres image; archi-okg head. |
| `scripts/contract-check.py` | Runs inside the image: registry classes and params, bundle drift, okg CLI, vendored paths. Emits mechanical fixes. |
| `scripts/upstream-summary.py` | The pull-request body: what moved upstream in the parts we use. |
| `scripts/engine-lock.sh` | Fingerprint of what the image was built from. CI fails if a pin moved without a rebuild. |

Four behaviours worth knowing:

- **Staging pins move together.** CI tests the image named in `versions.lock`. `envs/staging`
  is written only by the bot, after `main`'s e2e is green, image and knowledge revision in
  one commit. The Argo pause from the old runbook is no longer needed.
- **Your commits on `engine/upstream` survive.** While the pull request is open, the daily
  run merges `main` into the branch and adds a commit; it never resets it.
- **Pause with the label `hold`.** Closing the pull request is not a pause: the next run
  opens a new one from `main`.
- **Hold one side.** Run the workflow by hand with `okg_commit` or `archi_commit` set to a
  full sha to stay on that commit for that run.

## 3. Submodules: no

| | Submodule | Lock file + workflow (chosen) |
|---|---|---|
| okg (private) | Argo CD fetches a repository's submodules unless that is switched off for the whole Argo CD instance, and it has no credential for `mitdbg/okg`: the staging Application would stop syncing. Every clone of this repo would need an okg token. | The token stays in two CI secrets. |
| okg pin | A second pin next to the image digest, to be kept equal by hand. | The commit is read from the image, so the two cannot disagree. |
| archi-okg (public) | Works, but Dependabot cannot build the image, run the contract check or write the summary, so the workflow is needed anyway. | One mechanism for both upstreams. |

This reverses the submodule proposal in `ONBOARDING-v0.11` §5. That proposal assumed
Dependabot would do the bumping.

## 4. Rollout

### Step 0: prerequisites (10 minutes)

1. **The `dev` tags exist and your token reads them.**

   ```bash
   echo "$GHCR_PAT" | docker login ghcr.io -u nausikt --password-stdin
   git switch -c upstream-sync origin/main && git am /path/to/000*.patch
   scripts/upstream-resolve.sh --dry-run
   ```

   It needs `yq` v4 (mikefarah) and `jq`, and writes nothing.
   Expected: `changed=true`, `okg_to=<40 hex>`, `archi_to=<40 hex>`, and two lines naming
   `ghcr.io/mitdbg/okg@sha256:…` and `ghcr.io/mitdbg/okg-postgres@sha256:…`. This is the one
   part that could not be run against the real registry from here.

2. **Secrets.** The three existing ones are reused. Check their scope while you are here:

   | Secret | Needs | Used by |
   |---|---|---|
   | `GHCR_PAT` | `read:packages` + `write:packages` | engine (pull okg, push ours), ci, e2e (pull) |
   | `OKG_PAT` | read `mitdbg/okg` contents, nothing else | engine (image build, summary) |
   | `STAGING_BUMP_TOKEN` | this repo only: Contents read/write, Pull requests read/write | engine (push branch, open PR), main (pin commit) |

   **Who owns `STAGING_BUMP_TOKEN` matters.** The engine pull request is authored by that
   token's owner, and GitHub does not let an author approve their own pull request. If the
   token is yours and `main` requires an approving review, you cannot merge the bump. Either
   let a bot account (or a GitHub App) own the token, or require the checks but not a review.

3. **Labels and one repo setting.**

   ```bash
   gh label create engine --color 5319e7 --force
   gh label create hold   --color d93f0b --force
   gh repo edit --delete-branch-on-merge
   ```

4. **Close the stale engine pull requests** from the old loop (`engine/archi-crab-okg-10`, `-11`, `-12`):

   ```bash
   gh pr list --label engine
   gh pr close <number> --delete-branch
   ```

### Step 1: the patches' pull request

```bash
git push -u origin upstream-sync      # touches .github/workflows: the pushing token needs `workflow` scope
gh pr create --fill
```

Expected checks, all on the engine staging runs today:

- `lint`: includes `versions.lock: runtime.digest was built from the pinned okg + archi`.
- `okg-validate`: ends with a contract report of 0 errors (it is in the job summary).
- `e2e`: runs, because `scripts/` changed.

### Step 2: merge it

Two workflows start on `main`:

- **`main`** runs the e2e and commits `staging: pin <sha>`. The image lines in
  `envs/staging/values.yaml` are rewritten with the values they already have; only the two
  revision lines change. Check: `git pull && git show --stat HEAD`.
- **`engine`** starts because `docker/` changed. It opens the catch-up pull request,
  titled `engine: okg <sha> + archi-okg <sha>`. Its log must show
  `framework authority: <sha>` and `archi+okg import ok` in the build step.

### Step 3: review the catch-up pull request

`catch-up-preview.md` is what its body looks like, generated from the real upstreams on
2026-09-30. Expect:

- two commits: the pins plus the resynced `extractors.yaml`, then
  `converge: registry classes…` (`CMSSWReleaseSource` → `CMSSWReleaseAdapter`);
- a contract report with 0 errors;
- an upstream chart diff (PR 3040): okg removed the version labels from the StatefulSets'
  storage templates. It is the fix for our frozen `Chart.yaml`. Do not port it in this pull
  request; it needs a one-off `kubectl delete sts --cascade=orphan` and its own change;
- two new migrations (`0034`, `0035`).

Then wait for `e2e`. It is the first real ingest and publish on the new engine.

| If this is red | Do this |
|---|---|
| `okg-validate` → `catalog load` or `deployment lint` | Read the finding. Fix `deployments/archi-crab/` **on the `engine/upstream` branch**; the bot keeps your commits. |
| contract report has an ERROR without a mechanical fix | The message names the class or param. Same: fix on the branch. |
| `vendor-check` | `IMG=<image from versions.lock> scripts/vendor-sync.sh --apply`, commit on the branch. |
| `e2e` → ingest or smoke | Reproduce locally with the image from `versions.lock` (`ONBOARDING-v0.11` A6), or ask Claude to work on the branch with the failing log. |
| image build fails at `test -z "$(git status --porcelain)"` | The new okg image carries a file git does not know. Tell me; the Dockerfile step needs an exclusion. |
| you need time | Label the pull request `hold`. |

### Step 4: merge the catch-up

1. Merge. `main` runs the e2e again.
2. Wait for the bot commit and check that it carries both halves:

   ```bash
   git pull && git show HEAD -- envs/staging/values.yaml   # image digest AND revision lines changed
   ```

3. Argo CD rolls staging. This rollout is the big one: the postgres image changes (the
   database pod restarts) and migrations run on the existing data.

   ```bash
   NS=archi-crab-staging POD=archi-crab-okg-staging-runtime-0
   kubectl -n $NS get pods
   kubectl -n $NS logs $POD -c bootstrap | tail -30
   kubectl -n $NS exec $POD -c worker -- printenv OKG_CODE_REVISION ARCHI_CODE_REVISION
   kubectl -n $NS exec $POD -c worker -- okg status --deployment archi-crab --json | head -40
   ```

   If `bootstrap` refuses the existing database, send me its log before deleting
   anything. Staging's volumes are disposable (`cinder-io1-delete`), so a rebuild from
   empty is an option there, but prod's procedure has to come from what staging showed.
   Settle it before the first Promote.

### Step 5: the daily routine

Each morning there is either nothing, or the `engine/upstream` pull request with a new
summary. Read the table, the contract report and the chart section. Green and nothing
surprising: merge. That is the whole job.

## 5. Security

1. **Two agent-driven upstreams reach a cluster through this path.** Nothing merges by
   itself. The pins are full commit shas and image digests. `CODEOWNERS` now also covers
   `docker/` and `scripts/`, which run with the tokens. Protect `main`: require a pull
   request and the checks. Require a code-owner review too once the bump token belongs to a
   bot account (Step 0.2).
2. **Where upstream code runs, and what it can see.**
   - *Image build.* The step holding `OKG_PAT` now runs first and runs only git. Before,
     archi's install ran earlier as root and `import okg` ran while the token was mounted.
   - *Contract check.* A container with no network, `deployments/` and `scripts/` read-only.
     The fixes it proposes are applied on the runner only if each is a plain rename of one
     class name to another.
   - *e2e.* The containers mount the workspace. Checkouts no longer leave the job token in
     `.git/config` there.
3. **Tokens.**
   - `OKG_PAT` should be fine-grained, read-only, `mitdbg/okg` only. If the organisation does
     not allow fine-grained tokens, the classic `repo` scope is far wider than needed; ask the
     okg owners for a read-only deploy key instead (archi-okg's CI uses one).
   - `STAGING_BUMP_TOKEN` can push to `main`. Scope it to this repository and set an expiry.
   - `GHCR_PAT` is used with write access in jobs that only pull. A second, read-only token
     for `ci` and `e2e` would shrink that.
4. **The summary prints upstream text.** Commit subjects are untrusted. Each is printed
   inside a code span, so it cannot mention a user, link one of our issues or inject
   markdown. If you later add an AI reviewer to these pull requests, give it no write token:
   upstream text is then prompt-injection input.
5. **The image contains okg's private source and its `.git`.** `ghcr.io/nausikt/archi-crab-okg`
   must stay private, and so must this repository's pull requests (the summary quotes okg
   pull-request titles).
6. **Third-party actions are pinned to tags, not shas** (`docker/*`, `step-security/*`,
   `peter-evans/*`), although `dependabot.yml` says otherwise. The engine workflow dropped
   two of them (`docker/login-action`, `peter-evans/create-pull-request`). Pin the rest to
   shas; Dependabot then keeps them current.

## 6. Not verified, and other things to know

- **Nothing here ran on GitHub Actions.** The workflows pass `actionlint`. The `engine`
  job's shell steps were executed locally against a fake registry and a fake `gh`, for:
  first run, no change, human commit plus moved `main`, `hold`, merged with a leftover
  branch, and a conflicting branch. The scripts ran against the real upstream repositories.
  A second reviewer then read the series cold; its findings are fixed in these patches.
- **The registry calls are untested against ghcr.io** (`docker buildx imagetools inspect`).
  They copy what okg's own publish workflow does. Step 0.1 is the check.
- **The image was not built.** The Dockerfile changes are a reorder plus a fetch by sha.
- **Pushing the merged-forward branch may need more scope.** If `main` changed a workflow
  file while the pull request was open, GitHub may refuse the bot's push without the
  `workflow` permission. Then merge `main` into the branch by hand once.
- **Runner minutes.** `e2e` now runs on pull requests as well as on `main`, and the engine
  pull request changes most days. Watch the Actions usage for the first week. If it is too
  much, make the schedule weekly (`cron` in `engine.yaml`), not the checks weaker.
- **The moved e2e jobs still run without `pipefail`.** A failing `okg … | tee` in them does
  not fail the step. That is how they ran before; the new workflows (`engine`, `main`) set
  the strict shell. Tightening the e2e jobs is a separate change, because it can turn a
  check red that is green today.
- **okg merges about 600 commits a day.** A daily bump is a large diff of someone else's
  code. The protection is the contract check and the e2e, not review of the diff.
- **Each merged bump restarts staging's database pod**, because the postgres image is
  pinned to the same okg commit as the runtime.
- **`deployment.yaml`, the schemas and the skills are still hand-owned copies.** The summary
  lists which of them differ from the bundle (today: `schemas/sources.yaml` and four
  skills). Generating them from the bundle is the remaining step from `ONBOARDING-v0.11` §5.
- **The earlier onboarding patches `0001`–`0005` are superseded** for the engine part
  (archi-okg repository, adapter class, Promote fix). Their curated-TWiki and private-repo
  parts are not in this series.

## 8. What the first catch-up needed (2026-10-01, okg `0a8e0cd43`)

The first engine pull request was red on `e2e`. Each cause was reproduced locally (okg at
the pinned commit laid out as in the image, against a Postgres 17 with the same
extensions) and fixed on the branch:

| Check | Cause | Fix |
|---|---|---|
| `e2e-smoke` | okg now refuses to start `mcp-serve` while the read role `okg_mcp` has no login. Migration creates it without one. | The job passes `OKG_MCP_RO_DSN` to `okg runtime bootstrap`, which grants the login and proves it. In the cluster the chart's `mcp-role` init container already does this. |
| `chart-path`, step `deployment apply` | That step is not in the chart. Under `supervisor=container` okg has nothing to reload, and the command it tried does not exist for containers. | Step removed. The worker acknowledges the desired state by itself at boot. |
| `chart-path`, readiness | The job ran the worker from the workspace directory. okg compares where the worker runs with the image's layout (`/opt/okg`), so the acknowledgment never matched. | The worker runs from the image's working directory and the probe runs inside it (`docker exec`), as the kubelet does. |
| `chart-path`, readiness | `nomos.deployment_policy`: the manifest has a `nomos:` block but no posture and no policy for `cmssw_releases`. | `deployment.yaml` declares the posture (below). The contract check now runs the same audit in a second. |

Two things came with it:

- **`chart-path` is a real gate now.** `continue-on-error` is gone: upstream fixed
  readiness for container runtimes, so a red `chart-path` means a worker that would not
  become Ready in the cluster.
- **The chart's bootstrap maps `okg provision` exit 8 to success**, as upstream's chart
  does since 2026-09-30 (published, with a capacity warning).

### The posture is a gate for the sources to come

`deployment.yaml` declares `deployment_class: public_reference_demo`: public material
only, no source secrets. That is what the graph holds today, and it is the only class okg
accepts without Nomos runtime enforcement.

- **Public sources** (more public repositories, public TWiki pages) need one policy per
  new source class under `nomos.source_policy_defaults.by_source_class`. The contract
  check names the missing class.
- **The first non-public source** (CMS-internal TWiki, a private repository, anything read
  with a token or an SSO cookie) fails the audit. The class then has to become
  `org_operational_private`, and okg accepts that class only with runtime enforcement on:
  policies for every source, and lineage. That is a rollout of its own, and the point at
  which the CMS data-governance question has to be answered. Do not widen the public
  posture to get such a source through.
- **The audit only sees `sources:`.** Repositories under `code_repos:` are not checked.
  A private repository cloned with a token would pass the audit while making
  `secret_handling: no_secrets` and `public` untrue. The class has to change with the
  first private repository too, even though nothing will stop you.

## 7. Next

1. Graph view in the cluster: serve the operator console from the chart (after the catch-up).
2. TWiki crawl source, written once against the new engine (`TwikiCrawlAdapter`,
   `base_url: https://twiki.cern.ch/twiki`). The contract check will reject a wrong class or
   param on the pull request.
3. More sources: the contract report lists the bundle's connectors we do not use yet.
