# dmwm/CRABServer pull request #7774: RUCIO_Transfers.py: skip logfiles transfer

State: closed
Opened: 2023-07-18T17:15:49Z
Closed: 2023-07-20T08:26:57Z
Merged: 2023-07-20T08:26:57Z
URL: https://github.com/dmwm/CRABServer/pull/7774

## Opening post (novicecpp, 2023-07-18T17:15:49Z)

We need to skip logfile entries in `transfers.txt` but we need to update transfers state to `DONE` in order to make PostJob.py work properly. This is a bit hack but it easier than change code in PostJob.py.

## Comment (cmsdmwmbot, 2023-07-18T17:19:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1612/artifact/artifacts/PullRequestReport.html
