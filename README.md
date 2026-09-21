# archi-crab-okg

The **instance** repository for the CRAB knowledge graph (OKG): pure
declaration — connectors, schemas, modules, skills — plus the vendored Helm
chart, per-environment values, and the CI/CD that proves the knowledge
publishes, the invariant holds, and the deployment serves.

Start here: **`docs/RUNBOOK-v0.5.0.md`** (summary, skeleton map, six
verifiable phases, persistence footnotes).

Engine: upstream `mitdbg/okg@bed964f` images, pinned by digest in
`versions.lock` and `envs/*/values.yaml`. This repo builds nothing.

## Layout

    deployments/archi-crab/      the deployment (deployment.yaml, source_registry.yaml, schemas/, skills/)
    helm/okg/            vendored okg chart + archi-crab deltas
    envs/{staging,prod}  overrides: engine digests, storage, knowledge pins
    scripts/smoke.sh     the one judge: CI e2e step == Argo CD PostSync hook
    .github/workflows    ci (PRs) · main (e2e → bump staging) · promote (staging → prod)

## Until the tarball is completed, CI is red on purpose

`ci.yaml` fails while any of these exist: `deployments/archi-crab/extractors.yaml.TODO`,
`deployments/archi-crab/schemas/bridges/README.md`, `helm/okg/VENDOR-TODO.md`,
`REPLACE_ME` in `envs/` or `deployment.yaml`, or an unpinned `@PIN` action.
Runbook Phase 2–3 clears them in order.

## Temporary credentials — delete on publication

`GHCR_PAT` (GitHub secret) · Argo CD repo credential · `git-token` key +
`repositorySync.authSecretKey` · `ghcr-mitdbg-pull` secret + `images.pullSecrets`.

## Timings (fill in at Runbook Phase 2 / 5)

- local e2e ingest wall time: _
- DB size after first publish: _
- PR-merge → staging-smoke-green: _
