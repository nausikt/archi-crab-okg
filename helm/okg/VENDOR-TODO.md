# helm/okg — complete the vendor copy before first lint (Runbook Phase 2, step 2)

This directory ships the okg chart files that were available for vendoring
VERBATIM (templates/*.yaml, values.schema.json). Copy the rest from the
original working chart in CMSKubernetes@archi-crab-testbed:

    templates/_helpers.tpl        # REQUIRED: okg.fullname, okg.labels, okg.selectorLabels,
                                  #   okg.commonEnv, okg.runtimeImage, okg.postgresImage,
                                  #   okg.writerDsnEnv, okg.readerDsnEnv, okg.runtimeSubjectEnv,
                                  #   okg.mcpSubjectEnv, okg.extraSecretEnvFor,
                                  #   okg.containerSecurityContext, okg.serviceAccountName
    templates/networkpolicy.yaml  # the okg chart's own (the platform one is NOT it)
    templates/tests/*             # readiness + mcp test pods (converted below)
    values.yaml                   # DIFF against the reconstructed one here; keep upstream
                                  #   defaults except the deliberate deltas listed below

Check in `_helpers.tpl` how `okg.commonEnv` derives OKG_DEPLOYMENTS_DIR from
`okg.repoRoot`. This repo puts the deployment at `okg/archi-crab/`; if the
helper expects `<repoRoot>/<deployment>` directly, either set repoRoot to
`/var/lib/okg/repo/okg` in values or move the directory. Resolve once, then
`okg deployment lint` in CI keeps it honest.

## Deliberate deltas (apply as separate commits, each diffable against upstream)

1. `images.pullSecrets` -> podSpec `imagePullSecrets` on BOTH StatefulSets and
   the hook Job (ghcr.io/mitdbg/* is private until upstream publishes).
2. `podDisruptionBudget.enabled: false` default (see values.yaml comment).
3. helm-test pods -> Argo CD PostSync hook Job running
   `scripts/smoke.sh --in-cluster` from the repositorySync checkout
   (annotations: argocd.argoproj.io/hook: PostSync, hook-delete-policy:
   BeforeHookCreation). Argo never runs `helm test`; without this the only
   automated read-back proof is lost.
4. ONLY IF bootstrap fails with an authentication error: extend the mcp-role
   init pattern (`ALTER ROLE ... PASSWORD ... LOGIN`) to app_rw / app_ro.

Delete this file when the copy is complete; CI's lint job fails while it exists.
