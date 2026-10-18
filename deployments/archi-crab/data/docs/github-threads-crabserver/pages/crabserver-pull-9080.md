# dmwm/CRABServer pull request #9080: give StatusTracking more time to complete

State: closed
Opened: 2025-05-16T20:08:45Z
Closed: 2025-05-19T08:54:40Z
Merged: 2025-05-19T08:54:40Z
URL: https://github.com/dmwm/CRABServer/pull/9080

## Opening post (belforte, 2025-05-16T20:08:45Z)

currently tests are retried every 15min up to 10 times. But StatusTracking has large tasks which often requires resubmission, and it can easily take a few hours.
I am increasing to 30min the sleep time at each iteration.

## Comment (belforte, 2025-05-16T20:09:24Z)

Note that I have not tested yet.

## Comment (cmsdmwmbot, 2025-05-16T20:12:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2451/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-17T16:30:46Z)

testing in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12012532
* test OK
