# dmwm/CRABServer pull request #9019: allow CheckTapeRecall to have empty tasks list.

State: closed
Opened: 2025-03-28T11:38:53Z
Closed: 2025-03-28T13:25:07Z
Merged: 2025-03-28T13:25:06Z
URL: https://github.com/dmwm/CRABServer/pull/9019

## Opening post (nausikt, 2025-03-28T11:38:53Z)

Resolve https://github.com/dmwm/CRABServer/issues/9018

## Comment (cmsdmwmbot, 2025-03-28T11:41:18Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 25 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2409/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-28T12:52:55Z)

of course, a rule with no task pointing to it is not expected and we should evaluate whether to simply silencing this and wait for rule to expire, if ever, or report it so we can delete the rule or investigate more.

## Comment (cmsdmwmbot, 2025-03-28T12:59:17Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 25 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2410/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-28T14:28:10Z)

so you decided not have a warning reported when this happen, @sinonkt  ?
