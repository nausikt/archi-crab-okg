# dmwm/CRABClient pull request #5207: skip .git directories when creating sandbox. Fix #5202

State: closed
Opened: 2023-09-01T21:37:55Z
Closed: 2023-09-22T09:43:28Z
Merged: 2023-09-22T09:43:28Z
URL: https://github.com/dmwm/CRABClient/pull/5207

## Opening post (belforte, 2023-09-01T21:37:55Z)

includes a few small pylint fixes

## Comment (cmsdmwmbot, 2023-09-01T21:45:42Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 warnings
   * 34 comments to review
 * Pycodestyle check: succeeded
   * 24 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/935/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-01T22:01:51Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/936/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-01T22:10:42Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/937/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-09-01T23:17:35Z)

fixing remaining pylint messages would likely break py2 compatibility
