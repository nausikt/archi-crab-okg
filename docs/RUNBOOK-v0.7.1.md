# archi-crab — Runbook v0.7.1 (vendored vocabulary)

Amends v0.7.0: Phase A unchanged; **Phase B rewritten** around the vendoring
model; new CI job `vendor-check`; `build.yaml` resyncs on every engine bump.
Phases C–D unchanged. Date: 2026-09-20.

## §0 What changed and why (the first-principles answer, kept short)

okg's catalog is a contract pinned by the **ownership claim**: the deployment
directory is the whole vocabulary; okg never reads schema slices from the
installed archi package at runtime; a manifest identity change without a
deployment edit is refused. So schema slices, bridges and `extractors.yaml`
are **vendored data with a pinned version** — the same discipline as the
Helm chart you already vendor. okg's own in-image deployments prove it: the
codebase-index bridge exists in the template *and*, materialized, in
`okg-workspace/schemas/bridges/`.

Two things you established on 2026-09-20 make the vendoring *fully verbatim*:

1. `bundles/cern-team/schemas/{operations,sources}.yaml` and
   `schemas/bridges/{operations,sources}.yaml` exist at the archi pin → the
   profile's `schemas:` slot is real → the installer materializes the
   vocabulary. **The bundle README's manual step 2 is stale; it is deleted
   from this runbook.**
2. The packaged `bridges/operations.yaml` flags cross-module narrowings
   `optional_when_subtypes_missing: 'true'` → composes green without the
   modules it doesn't find. **B.1 (hand-pruning to the cmssw narrowing) is
   deleted.** Zero hand-edited vendored files.

Hence the model:

| | mechanism | when |
|---|---|---|
| **First scaffold** | `scripts/gen-cern-team.sh` (installer + `vendor-sync --apply`) | once per instance lifetime |
| **Archi / okg bump** | `build.yaml` → new image → `vendor-sync --apply` → engine-bump PR carrying the vocabulary diff | automatic, merge = accept |
| **Drift guard** | `vendor-check` CI job: `vendor-sync --check` against the pinned image | every PR |
| **Our deviations** | `ours:` files in `VENDOR.yaml` (deployment.yaml, registry, invariants) | never touched by sync |

Why not a submodule: the chart's `repository-sync` never runs `submodule
update` (empty dir in-cluster); you cannot express "only what we run" inside
a submodule; and bumping it changes the claim identity anyway, so it saves no
ceremony. Why not generate in the image or at bootstrap: two sources of
truth merged at runtime, an unreviewed claim identity, and it fights
repositorySync's git-checkout requirement. **Propose automatically, apply by
merge** is the correct shape, and `build.yaml` now does exactly that.

---

## Phase A — unchanged (v0.7.0): derived image, PR1, `build.yaml` opens PR2

PR1 now also carries `deployments/archi-crab/VENDOR.yaml`, `scripts/vendor-sync.sh`,
the revised `scripts/gen-cern-team.sh`, and the patched `ci.yaml` /
`build.yaml`. `yq` v4 is required locally (`brew install yq` / distro pkg).

✓ PR2 open: `envs/staging` → `ghcr.io/nausikt/archi-crab-okg@<digest>`;
`versions.lock` `runtime.*` filled; on the very first build `vendor-sync
--apply` will have refreshed `skills/` and added `extractors.yaml` +
`extraction_to_git_files.yaml` (the v0.5.0 tree has no bundle `schemas/` yet
— the installer creates them in Phase B).

---

## Phase B — First scaffold, on PR2's branch (½ day, once)

```bash
git fetch origin && git switch engine/archi-crab-okg-<run>
IMG=$(yq -r '.images.okg.repository + "@" + .images.okg.digest' envs/staging/values.yaml)
podman run -d --name pg --shm-size 2g -p 127.0.0.1:5435:5432 -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=okg \
  ghcr.io/mitdbg/okg-postgres@sha256:75845f96d973859c248f0f6741cb0a06445e9d312e563de7a39c5e25f3236616
export OKG_DSN=postgresql://postgres:dev@127.0.0.1:5435/okg
IMG="$IMG" scripts/gen-cern-team.sh
```

The script: moves `deployments/archi-crab` → `deployments/archi-crab.prev`; runs `okg install
--profile cern-team --deployment-name archi-crab --postgres-dsn '${OKG_DSN}'
--non-interactive --no-publish` (`--no-publish` = stop before first load so
our edits land first; harmless if redundant); restores `VENDOR.yaml` and our
`invariants.yaml`; runs `vendor-sync --apply`; prints what the installer wrote.

**B.1 Verify the manifest mirrors reality** (once): compare the installer's
file list against `VENDOR.yaml` — in particular *where* `skill-triggers.yaml`
landed (`skills/` per `deployment-defaults.yaml`) and whether the installer
wrote a separate `source_registry.yaml` or inline `sources:`. Adjust `dest`
/ `ours` so `vendor-sync --check` describes the tree exactly.

**B.2 Registry — only what has data on a fresh instance.** Keep
`cmssw_releases`. Delete every connector needing a cache file or an SSO cookie
(docsite, twiki_*, jira, indico) and the bundle's `github_repo` /
`gitlab_repo` (file blobs; the code graph supersedes them). The k8s bootstrap
has no `--exclude`; unregistered is the only exclusion.

**B.3 Code graph** (field guide §5, cherry-picked from `deployments/archi-crab.prev`):
`code_repos{crabserver, crabclient}` with `expand` **without** git-history and
`base: ${OKG_ENVIRONMENT_DATA_ROOT}/repos`, placed where
`deployments/archi-crab.prev`'s `source_registry.yaml` had it — confirm against the
template dump (`vendor-sync` sources live at
`/opt/okg/src/okg/substrate/library/templates/codebase-index/`; `podman run
--rm --entrypoint sh $IMG -c 'cat …/codebase-index/deployment.yaml*'`); the
seven code modules appended to `modules:` **all at once**; `consistency:
{dangling_edges: prune}`.

**B.4 k8s edits in `deployment.yaml`**: `runtime.enabled: true`;
`chat.enabled: false`; search profile `subtypes: [document_chunk, source_file,
code_symbol, cmssw_release]`; `nomos.rollout.owner.contact`. Relative
`data/...` paths stay as written — `ARCHI_DATA_ROOT` anchors them (CI env;
chart delta 5 in-cluster).

**B.5 Lint loop** (v0.7.0 B.6, table unchanged). `bridge_subtype_unknown`
should now be *impossible* on the bundle bridge — if it appears, it is an
upstream regression: report it with the narrowing name, and do **not**
hand-edit the vendored file; add the narrowing's fix as an `ours` override
only as a last resort.

```bash
export OKG_DEPLOYMENTS_DIR=$PWD/okg OKG_ENVIRONMENT_DATA_ROOT=$PWD/.okg-data ARCHI_DATA_ROOT=$PWD/.okg-data
okg() { podman run --rm --network host -v "$PWD:$PWD" -w "$PWD" \
        -e OKG_DSN -e OKG_DEPLOYMENTS_DIR -e OKG_ENVIRONMENT_DATA_ROOT -e ARCHI_DATA_ROOT "$IMG" "$@"; }
okg migrate --deployment archi-crab --apply && okg migrate --deployment archi-crab --apply
okg catalog ownership claim --deployment "$OKG_DEPLOYMENTS_DIR/archi-crab"
okg catalog load  --deployment "$OKG_DEPLOYMENTS_DIR/archi-crab" --apply
okg deployment lint archi-crab --json | tee lint.json           # loop until ok: true
mkdir -p .okg-data/repos .okg-data/data/cmssw-releases
okg ingest --deployment archi-crab --progress
bash scripts/smoke.sh
IMG="$IMG" scripts/vendor-sync.sh --check                        # must print "vendor in sync"
```

✓ `SMOKE OK`; four invariant subtypes live; `vendor-sync --check` green;
`rm -rf deployments/archi-crab.prev`; set `validated.local_e2e`; commit on PR2's
branch; push. CI: `lint`, `vendor-check`, `okg-validate` green. Merge PR2.

---

## Phases C–D — unchanged (v0.7.0)

Chart delta 5 (`ARCHI_DATA_ROOT`), pull secret from the widened `GHCR_PAT`,
staging sync and verify, promote.

---

## The steady state — what a bump looks like now

**Archi or okg bump**: one PR editing `versions.lock` (`archi.commit` and/or
`images.okg.ref`) → merge → `build.yaml` builds, pushes, runs `vendor-sync
--apply` from the new image, opens the engine-bump PR whose diff *is* the
vocabulary change → `vendor-check` and `okg-validate` run on it → you read
the `schemas/` diff for renames or narrowing changes (rebuild triggers, F4),
compare `ours` files against the bundle's new defaults only if the vocabulary
they reference moved → merge → `main.yaml` e2e → staging → promote.

**Knowledge change**: as before; `vendor-check` runs and is a no-op.

**Someone hand-edits a vendored file**: `vendor-check` goes red on their PR
with the diff. That is the whole point.

## Standing rules (v0.7.1)

- Never hand-edit a `VENDOR.yaml` entry; deviate by moving a file to `ours`
  and owning it, with the reason in a comment.
- The generator runs once per instance lifetime. Re-scaffold into a scratch
  dir only to *diff* the bundle's current defaults against `ours`.
- Everything from v0.5.0/v0.7.0 standing rules still holds (PR-only, rebuild
  on identity change, git-history manual, engine bumps via `versions.lock`,
  private image while the base is, publication-day checklist).
