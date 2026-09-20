# archi-crab — Runbook v0.7.0 (cern-team bundle, derived image)

Supersedes v0.6.0 §3–§4 (the zero-archi pivot is withdrawn). Keeps v0.5.0's
footnotes F1–F5 and its Phases 1, 4, 6 (secrets, staging sync, promote).
Date: 2026-09-20. Repo baseline: `main@468d672` (v0.5.0 + vendored helm +
extractors TODO cleared).

**The decision**: pick up the cern-team bundle. Cost: **one derived image**
(`FROM` upstream okg digest + archi), one build workflow, one archi commit to
track. Gain: `cmssw_releases` today, the HEP vocabulary the skills target,
parity with the proven cms-compops instance, and an open road to TWiki /
docsite / JIRA / Indico.

Shape of the whole thing after v0.7.0:

```
engine change  ──PR──► docker/** or versions.lock ──merge──► build.yaml ──► ENGINE-BUMP PR (bot)
                                                                                │
you, on that branch ──► scripts/gen-cern-team.sh ──► 5 edits ──► lint loop ──► commit
                                                                                │
                                              ci: lint → okg-validate (new engine + new knowledge)
                                                                                │
merge ──► main.yaml: e2e-smoke → bot pins envs/staging → Argo CD staging → PostSync smoke
click Promote ──► prod-env approval → all 5 pins → prod
```

Five pins now, all in `envs/*/values.yaml` (engine: `images.okg.digest`,
`postgresql.image.digest`; knowledge: `repositorySync.revision`,
`bootstrap.approvedRevision`) plus `versions.lock` as the human decoder ring
(upstream commit ⇄ archi commit ⇄ derived digest).

---

## Phase A — The derived image (2 h)

**A.1 Inspect the base once** (the Dockerfile must restore its user):

```bash
BASE=ghcr.io/mitdbg/okg@sha256:5a825f73c8929d2153859d95bfaf4c6f4ae01f02d08477583a7af05131826705
podman inspect "$BASE" | jq -r '.[0].Config | {User, Entrypoint, WorkingDir, Env}'
podman run --rm --entrypoint sh "$BASE" -c 'command -v python; command -v uv; command -v git; python -m pip --version 2>&1 | head -1'
```

Write `runtime.base_user` in `versions.lock` (`"0"` if `User` is empty).
The Dockerfile already handles uv / pip / ensurepip and a missing git.

**A.2 Pin archi**:

```bash
git ls-remote https://github.com/archi-physics/archi refs/heads/archi_v3_quickstart   # → archi.commit
```

Prefer the commit your colleague validated if it is on that branch
(field guide: `728739e6`); otherwise the branch head, and Phase B's lint loop
is the compatibility test.

**A.3 Build locally once** — never let CI be the first place a Dockerfile runs:

```bash
podman build -f docker/runtime/Dockerfile \
  --build-arg BASE_IMAGE="$BASE" --build-arg ARCHI_REF=<archi.commit> --build-arg BASE_USER=<base_user> \
  -t archi-crab-okg:dev .
podman run --rm archi-crab-okg:dev --help
podman run --rm --entrypoint python archi-crab-okg:dev -c "import archi, okg; print('ok')"
podman run --rm --entrypoint sh archi-crab-okg:dev -c 'ls /opt/archi/bundles; ls /opt/archi/python/archi/schemas/bridges'
```

✓ `ok`; `/opt/archi/bundles/cern-team` exists; `schemas/bridges/{operations,sources}.yaml` exist.

**A.4 Secrets & PR1**:
- `GHCR_PAT` must now carry **`write:packages`** (own image) as well as
  `read:packages` (mitdbg base). Same PAT, wider scope; still temporary.
- `STAGING_BUMP_TOKEN` also creates the engine-bump PR (a PAT — PRs opened
  with `GITHUB_TOKEN` never trigger CI).
- Add `packages` visibility: `ghcr.io/nausikt/archi-crab-okg` stays
  **private** (contains upstream's private base). Link the package to this
  repo in GitHub package settings.
- PR1 = this tarball's delta: `docker/`, `.github/workflows/build.yaml`,
  patched `ci.yaml` / `main.yaml` (ARCHI_DATA_ROOT; `versions.lock` moved to
  build.yaml's paths), `versions.lock`, `scripts/*`,
  `okg/archi-crab/invariants.yaml`, `helm/okg/DELTA-5-archi-data-root.md`.
  `envs/*` untouched in PR1 (still the upstream image → lint stays green).
- `pinact run` on the new workflow; CODEOWNERS already covers workflows.

✓ PR1 merges green. `build.yaml` runs on the merge (paths `docker/**`,
`versions.lock`), pushes `ghcr.io/nausikt/archi-crab-okg:<sha>`, and opens
**PR2** `engine: archi-crab-okg @ archi <commit>` editing `envs/staging`
`images.okg.*` and `versions.lock` `runtime.*`. Do not merge PR2 yet — Phase
B happens on its branch.

---

## Phase B — The generator ritual, on PR2's branch (½ day)

```bash
git fetch origin && git switch engine/archi-crab-okg-<run>
IMG=$(yq '.images.okg.repository + "@" + .images.okg.digest' envs/staging/values.yaml)
podman run -d --name pg --shm-size 2g -p 127.0.0.1:5435:5432 -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=okg \
  ghcr.io/mitdbg/okg-postgres@sha256:75845f96d973859c248f0f6741cb0a06445e9d312e563de7a39c5e25f3236616
export OKG_DSN=postgresql://postgres:dev@127.0.0.1:5435/okg
IMG="$IMG" scripts/gen-cern-team.sh
```

The script moves your v0.5.0 `okg/archi-crab` to `okg/archi-crab.prev`
(cherry-pick source), scaffolds with `okg install --profile cern-team
--deployment-name archi-crab --postgres-dsn '${OKG_DSN}' --non-interactive
--no-publish`, copies the archi schema slices + `bridges/sources.yaml`, dumps
the full `bridges/operations.yaml` as `.FULL.yaml` for pruning, and drops in
`extractors.yaml` + `extraction_to_git_files.yaml` from the okg template.

**B.1 Prune the operations bridge**: keep **only**
`cmssw_release_supersedes_release` (edge_archetype `supersedes`,
CMSSWRelease → CMSSWRelease) in `schemas/bridges/operations.yaml`; delete the
`.FULL.yaml`. Everything else references subtypes owned by modules the
bundle does not compose and lacks `optional_when_subtypes_missing` → load
fails `bridge_subtype_unknown`. Also drop any `bridges/sources.yaml`
narrowing that names jira / docsite / twiki / monit connectors.

**B.2 Registry: only what has data on a fresh instance.** Inspect what the
installer registered (`grep -n '^[a-z_]*:' okg/archi-crab/source_registry.yaml`
or the inline `sources:`). Keep `cmssw_releases`. Delete every connector
needing a cache file or an SSO cookie (docsite, twiki_*, jira, indico) and the
bundle's `github_repo` / `gitlab_repo` (file blobs only — the code graph below
supersedes them). Nothing excluded is registered; the k8s bootstrap has no
`--exclude`.

**B.3 Add the code graph** (field guide §5, on top of the bundle, exactly as
cms-compops did). Copy from `okg/archi-crab.prev/`:
- the `code_repos` block (CRABServer + CRABClient, `expand` **without**
  git-history, `base: ${OKG_ENVIRONMENT_DATA_ROOT}/repos`) — placed where
  `.okg-data/codebase-index.deployment.yaml` shows okg's template puts it
  (v0.6.0 §2's Route A/B question, answered by that dump);
- the seven code modules appended to the installer's `modules:` —
  `repo_starter, openspec, agent_sessions, compute_env, code_graph, forge, ci`
  (plus `dataset` if the template lists it) — **all at once**;
- `consistency: {dangling_edges: prune}`.

**B.4 Files already in git**: `invariants.yaml` (the 4-subtype floor —
overwrite the installer's `cern_team_core_pages_floor`), `extractors.yaml`,
`extraction_to_git_files.yaml` (both dropped in by the script). CI's lint
guard asserts the last two exist.

**B.5 The three k8s edits in `deployment.yaml`**: `runtime.enabled: true`;
`chat.enabled: false`; search profile `subtypes: [document_chunk,
source_file, code_symbol, cmssw_release]` (drop `documentation_page`,
`software_repository`). Set `nomos.rollout.owner.contact`. Relative
`data/...` paths stay as the installer wrote them — `ARCHI_DATA_ROOT` anchors
them (CI sets it; chart delta 5 sets it in-cluster).

**B.6 The lint loop** (claim/load idempotent; iterate until `ok: true`):

```bash
export OKG_DEPLOYMENTS_DIR=$PWD/okg OKG_ENVIRONMENT_DATA_ROOT=$PWD/.okg-data ARCHI_DATA_ROOT=$PWD/.okg-data
okg() { podman run --rm --network host -v "$PWD:$PWD" -w "$PWD" \
        -e OKG_DSN -e OKG_DEPLOYMENTS_DIR -e OKG_ENVIRONMENT_DATA_ROOT -e ARCHI_DATA_ROOT "$IMG" "$@"; }
okg migrate --deployment archi-crab --apply && okg migrate --deployment archi-crab --apply
okg catalog ownership claim --deployment "$OKG_DEPLOYMENTS_DIR/archi-crab"
okg catalog load  --deployment "$OKG_DEPLOYMENTS_DIR/archi-crab" --apply
okg deployment lint archi-crab --json | tee lint.json
```

| lint / load says | fix |
|---|---|
| `bridge_subtype_unknown` | B.1 was incomplete — prune harder |
| `profile_invalid` / identity kind on a connector | copy the `source_class`/`record_identity_kind` pairing from the bundle's or template's block verbatim |
| search profile subtype unknown | B.5 lists a subtype no module/schema provides — remove it, or a module is missing (B.3) |
| trigger subtype unknown | prune `skill-triggers.yaml` intents to subtypes the catalog has, or `["*"]` |
| `catalog_ownership_mismatch` | expected mid-loop: re-run claim → load |
| unknown key | diff against `.okg-data/codebase-index.deployment.yaml` and the installer's own output — one of them spells it |

Then ingest and prove:

```bash
mkdir -p .okg-data/repos .okg-data/data/cmssw-releases
okg ingest --deployment archi-crab --progress
bash scripts/smoke.sh
```

Publish blocked on dangling edges → B.3's `consistency` block missing.
Hundreds of thousands of `transform_consistency_violations` → modules landed
incrementally; wipe pg (`podman rm -f pg`, recreate) and rerun from migrate
with the full list.

✓ `SMOKE OK`; four invariant subtypes have live rows; `\dx` shows the six
extensions. `rm -rf okg/archi-crab.prev`; set `validated.local_e2e`; commit
**on PR2's branch**; push. CI: `lint` + `okg-validate` green *on the new
engine with the new knowledge*. Merge PR2.

---

## Phase C — Chart delta 5, staging sync (½ day)

1. Apply `helm/okg/DELTA-5-archi-data-root.md` (`ARCHI_DATA_ROOT` in
   `okg.commonEnv`); delete the note. Confirm `images.pullSecrets` secret
   (`ghcr-mitdbg-pull`, or rename to `ghcr-pull`) is built from the **widened**
   `GHCR_PAT` — one ghcr credential now pulls both `mitdbg/okg-postgres` and
   `nausikt/archi-crab-okg`.
2. Merge → `main.yaml` `e2e-smoke` green on the derived image → bot pins.
3. Argo CD staging Application as v0.5.0 Phase 4; watch `repository-sync →
   bootstrap → mcp-role → worker Ready → PostSync smoke Complete`. Same triage
   map, plus: `ModuleNotFoundError: archi` in bootstrap → `envs/staging`
   still points at the upstream image (PR2 not merged / pins job stale).

✓ App Healthy+Synced; smoke Complete; in-pod
`okg search --deployment archi-crab --query "CMSSW_14"` and `"crab submit"`
both return hits; `echo $ARCHI_DATA_ROOT` in the worker prints
`/var/lib/okg`. Set `validated.staging`.

## Phase D — Promote

v0.5.0 Phase 6 unchanged: prod Application (`prune: false`) → `promote` →
prod-env approval → PR diff = the pin lines only → merge → prod smoke → tag
`v0.7.0`; `validated.prod`.

---

## Standing rules (v0.7.0 additions in bold)

- Knowledge via PR only; identity changes ⇒ rebuild (F4); no in-pod edits.
- git-history: manual second pass only.
- **Engine or archi bump = edit `versions.lock` (+ base digest) in a PR →
  build.yaml → engine-bump PR → Phase B on its branch → merge.** Never edit
  `images.okg.digest` by hand.
- **Archi bumps re-run the generator into a scratch dir and *diff* against
  `okg/archi-crab/` — never overwrite the reviewed instance.** The bundle's
  `source-defaults` and schema slices move with archi; your B.1–B.5 edits are
  the delta you carry.
- **The derived image stays private while the base is.** Publication day
  checklist (v0.5.0) now also covers `ghcr.io/nausikt/archi-crab-okg`
  visibility and `write:packages` on the PAT.
- CI's `username: nausikt` → machine account before this outlives its author.

## Deferred (tracked)

git-history · TWiki export / playbooks as repos (work today via `code_repos`) ·
docsite / JIRA / Indico connectors (need caches → downloader manifest) ·
WMCore + more repos · semantic search · vMCP exposure + SSO clients + DNS ·
prod `prune: true` · retire the derived image if upstream ever ships archi.
