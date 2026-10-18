# dmwm/CRABServer pull request #9171: Enable ArgoCD deployment on test2, test12, support normal base ref from kustomization resources

State: closed
Opened: 2025-09-04T09:02:13Z
Closed: 2025-09-04T09:02:42Z
Merged: 2025-09-04T09:02:42Z
URL: https://github.com/dmwm/CRABServer/pull/9171

## Opening post (nausikt, 2025-09-04T09:02:13Z)

Regarding #9170, #9152 

Guys, I've enable test2, test12 to use argocd deployment approach via sidecar in our pipeline.

Also have extended the script, such that CI/CD could easily switch back and forth from workaround branch and on-going migration branch.

As usual, let me merged this changes for further testing in our pipeline, Thanks!.
