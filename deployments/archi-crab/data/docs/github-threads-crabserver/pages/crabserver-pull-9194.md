# dmwm/CRABServer pull request #9194: switch back to pre-argocd deploying method until convergence to monorepo at CMSKubernetes.

State: closed
Opened: 2025-09-30T14:05:34Z
Closed: 2025-09-30T14:06:31Z
Merged: 2025-09-30T14:06:31Z
URL: https://github.com/dmwm/CRABServer/pull/9194

## Opening post (nausikt, 2025-09-30T14:05:34Z)

We will pause deploying in CI/CD pipeline via ArgoCD for a while. I've pause argocd both automatic and manual syncing from `crab-k8s-overlays` now. There should be no noticeable changes on our CI/CD dev/test workflow.

You guys are also free to use `kubectl edit deployment ...` for manual bumping image tag. Since ArgoCD no longer take control over our live manifests anymore.
