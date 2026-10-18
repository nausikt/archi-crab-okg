# dmwm/CRABServer pull request #8851: removing sleep in pendingwork if else

State: closed
Opened: 2024-11-29T08:38:24Z
Closed: 2024-12-03T08:35:14Z
Merged: 2024-12-03T08:35:14Z
URL: https://github.com/dmwm/CRABServer/pull/8851

## Opening post (aspiringmind-code, 2024-11-29T08:38:24Z)

Polling in [here](https://github.com/aspiringmind-code/CRABServer/blob/ddd6ce1ded4d1b49cf92406b39d9a47321bd6776/src/python/TaskWorker/MasterWorker.py#L618) works for both canary and master. No need for pending-else polling.

## Comment (cmsdmwmbot, 2024-11-29T08:42:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 58 comments to review
 * Pycodestyle check: succeeded
   * 65 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2307/artifact/artifacts/PullRequestReport.html
