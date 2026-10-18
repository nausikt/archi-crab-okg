# dmwm/CRABServer pull request #8018: Add 'type' back to transfers dict for retry job

State: closed
Opened: 2023-11-21T13:52:35Z
Closed: 2023-11-22T15:26:44Z
Merged: 2023-11-22T15:26:44Z
URL: https://github.com/dmwm/CRABServer/pull/8018

## Opening post (novicecpp, 2023-11-21T13:52:35Z)

Fix https://github.com/dmwm/CRABServer/issues/8005

Add `type` back for transfer dicts of second retry. Also pop out some unnecessary key.

## Comment (cmsdmwmbot, 2023-11-21T13:58:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 2 warnings
   * 160 comments to review
 * Pycodestyle check: succeeded
   * 618 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1761/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-11-22T15:05:53Z)

Ahhhh, we have already done this for other keys in line 973-983,  before we dump it into `transfers.txt`.
 https://github.com/dmwm/CRABServer/blob/372e3856e4431a8e54c16469d7c7060cf403fdb5/src/python/TaskWorker/Actions/PostJob.py#L973-L986

I will add `type` below the line 983 instead.

## Comment (cmsdmwmbot, 2023-11-22T15:15:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 2 warnings
   * 160 comments to review
 * Pycodestyle check: succeeded
   * 618 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1766/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-22T15:23:55Z)

very good ! yeah... it is not clear at all what `toTransfer` argument mean here :-(

## Comment (novicecpp, 2023-11-22T15:26:40Z)

Thanks. Merging...
