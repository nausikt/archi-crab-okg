# dmwm/CRABServer pull request #9186: Switching to argocd helm on testX

State: closed
Opened: 2025-09-17T08:38:57Z
Closed: 2025-09-17T08:43:27Z
Merged: 2025-09-17T08:43:27Z
URL: https://github.com/dmwm/CRABServer/pull/9186

## Opening post (nausikt, 2025-09-17T08:38:57Z)

I've refactored everything to argocd+helm, we will living with this fallback (vendir sync approach) solution such that its not block your routine development workflow.  

Let me quick merged this one for further testing in pipeline as usual.

## Comment (nausikt, 2025-09-17T08:41:04Z)

#9152

## Comment (cmsdmwmbot, 2025-09-17T08:42:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2631/artifact/artifacts/PullRequestReport.html
