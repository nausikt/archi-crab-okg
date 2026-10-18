# dmwm/CRABServer pull request #9164: hotfix argocd sidecar update on pipeline

State: closed
Opened: 2025-08-28T00:00:47Z
Closed: 2025-08-28T00:06:48Z
Merged: 2025-08-28T00:06:48Z
URL: https://github.com/dmwm/CRABServer/pull/9164

## Opening post (nausikt, 2025-08-28T00:00:47Z)

Hotfix for quick merged PR #9163.

I've tested e2e CD via argocd sidecar approach, it's works. Thank you so much for you guys kind understanding on these 2 quick merged testing!

Since our core CI/CD pipeline has support auto-commit for image tag updating via argocd sidecar repo, now we could rebase or cherry pick anytime from master if you guys wish to move to argocd on dev/test transparently anytime!

## Comment (cmsdmwmbot, 2025-08-28T00:03:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2587/artifact/artifacts/PullRequestReport.html
