# dmwm/CRABServer pull request #9279: deprecate (sidecar) crab-k8s-overlays, switching CI to mono-repo approach

State: closed
Opened: 2026-03-09T21:21:55Z
Closed: 2026-04-10T14:37:39Z
Merged: 2026-04-10T14:37:39Z
URL: https://github.com/dmwm/CRABServer/pull/9279

## Opening post (nausikt, 2026-03-09T21:21:55Z)

This PR will fulfill https://github.com/dmwm/CRABServer/issues/9188#issuecomment-4024615388.

CRAB Operator devOps workflow experience should remain the same, with no noticeable effects.

it was tested on the test14 deployment, triggered with gitlab-CI using a new *dedicated deployment key* to update the expected to be upstream `crab` branch, as you can see https://github.com/nausikt/CMSKubernetes/commit/f0e8eb7fb2555683e08c0337a98714d6d88591d4

*P.B. Note that any on-going features branch created **before** this merged may need to run: 
**git fetch upstream** & **git rebase upstream/master** in their branch to pick up this new approach.*

## Comment (cmsdmwmbot, 2026-03-09T21:25:44Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2751/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-17T14:58:18Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2752/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-09T21:22:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2783/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-10T12:34:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2786/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-04-10T12:50:55Z)

The PR have been tested quite thoroughly. 

with this PR merged it will enforced ArgoCD for non-prod envs.

Despite some little longer delay waiting for ArgoCD to converged, there should be no noticeable impact on our DevOps workflow experience.

## Comment (belforte, 2026-04-10T14:29:14Z)

go for it. And if we find problems, you will fix them ! :muscle:
