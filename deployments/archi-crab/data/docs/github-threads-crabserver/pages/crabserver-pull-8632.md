# dmwm/CRABServer pull request #8632: Fix small bugs

State: closed
Opened: 2024-08-17T14:31:05Z
Closed: 2024-08-19T17:14:44Z
Merged: 2024-08-19T17:14:44Z
URL: https://github.com/dmwm/CRABServer/pull/8632

## Opening post (belforte, 2024-08-17T14:31:05Z)

fix #8628

## Comment (belforte, 2024-08-17T14:31:48Z)

after this is merged we need to build and deploy a new monit container to fix CheckTapeRecall

## Comment (cmsdmwmbot, 2024-08-17T14:35:39Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 24 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2110/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-19T16:46:23Z)

Since Dario is traveling, and this is quite minor. I will merge and create a new monitoring container so we get TapeRecall monitoring back

## Comment (cmsdmwmbot, 2024-08-19T16:54:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 24 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2111/artifact/artifacts/PullRequestReport.html
