# dmwm/CRABClient pull request #5418: py2 compatible HTTPStatus imported.

State: closed
Opened: 2025-09-26T13:15:41Z
Closed: 2025-09-26T14:08:35Z
Merged: 2025-09-26T14:08:35Z
URL: https://github.com/dmwm/CRABClient/pull/5418

## Opening post (nausikt, 2025-09-26T13:15:41Z)

Resolve #5416 

I've tested on all slc6 env (e.g. `CMSSW_10_1_0`, `CMSSW_9_4_21`, `CMSSW_8_0_36`). Status responses are fine for every status codes, also in case of unknown one.

## Comment (cmsdmwmbot, 2025-09-26T13:17:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 warnings
   * 16 comments to review
 * Pycodestyle check: succeeded
   * 12 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1140/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-26T13:41:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 warnings
   * 16 comments to review
 * Pycodestyle check: succeeded
   * 13 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1141/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-09-26T13:57:30Z)

WOW

please add a comment line of the sort "add an HTTPS method so that it can be used like http which is only available in python3" ... just something to explain what's going on with this new class.

## Comment (cmsdmwmbot, 2025-09-26T14:05:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 warnings
   * 16 comments to review
 * Pycodestyle check: succeeded
   * 12 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1142/artifact/artifacts/PullRequestReport.html
