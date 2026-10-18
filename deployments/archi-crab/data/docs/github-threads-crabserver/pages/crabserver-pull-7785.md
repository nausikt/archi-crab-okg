# dmwm/CRABServer pull request #7785: RUCIO_Transfers.py: Fix bookkeeping block complete

State: closed
Opened: 2023-07-21T11:25:20Z
Closed: 2023-07-27T06:33:40Z
Merged: 2023-07-27T06:33:40Z
URL: https://github.com/dmwm/CRABServer/pull/7785

## Opening post (novicecpp, 2023-07-21T11:25:20Z)

Untangle MonitorLockStatus actions and break into 2 steps:
- Monitoring transfer status and update status "DONE" to the REST.
- Add new successful transfer replica to publish container.

Bookkeeping and readability is much more cleaner now.

## Comment (cmsdmwmbot, 2023-07-21T11:30:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1629/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-25T08:04:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1630/artifact/artifacts/PullRequestReport.html
