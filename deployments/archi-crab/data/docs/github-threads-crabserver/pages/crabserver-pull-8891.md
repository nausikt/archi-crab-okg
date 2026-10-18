# dmwm/CRABServer pull request #8891: add bumping WMCore version script.

State: closed
Opened: 2025-01-23T13:55:07Z
Closed: 2025-01-27T13:42:40Z
Merged: 2025-01-27T13:42:40Z
URL: https://github.com/dmwm/CRABServer/pull/8891

## Opening post (nausikt, 2025-01-23T13:55:07Z)

Note that this is just the draft script that bumping wmcore version on both CRABServer and TaskWorker.
Once reviewed the bumping will be made before merged pull request. #8880

## Comment (cmsdmwmbot, 2025-01-23T13:58:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2335/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-23T15:51:29Z)

Let's put this in the `cicd` directory. For some historical reasons `CRABServer/scripts` contains scripts to be executed by remote jobs and some odd things in `scripts/Monitor` and `scripts/Utils` which need to be removed as obsolete or moved elsewhere.

## Comment (cmsdmwmbot, 2025-01-23T17:06:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2339/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-27T13:41:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2340/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-01-27T13:44:17Z)

Resolve #8880
