# dmwm/CRABServer pull request #8976: Rucio cleanup for crabint1 account

State: closed
Opened: 2025-03-11T13:15:34Z
Closed: 2025-03-11T14:52:14Z
Merged: 2025-03-11T14:52:14Z
URL: https://github.com/dmwm/CRABServer/pull/8976

## Opening post (aspiringmind-code, 2025-03-11T13:15:34Z)

We add a cleanup stage in the pipeline that deletes rucio rules older than 30 days for crabint1 account. Fix #8887 
The step can be skipped by setting SKIP_CLEANUP variable as true.

## Comment (cmsdmwmbot, 2025-03-11T13:18:44Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2396/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-03-11T13:58:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2397/artifact/artifacts/PullRequestReport.html
