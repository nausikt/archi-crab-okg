# dmwm/CRABServer pull request #9026: avoid un-pickable objects in multiprocess queue

State: closed
Opened: 2025-04-01T07:31:29Z
Closed: 2025-04-01T13:52:51Z
Merged: 2025-04-01T13:52:51Z
URL: https://github.com/dmwm/CRABServer/pull/9026

## Opening post (belforte, 2025-04-01T07:31:29Z)

fix #9014

see comments in that issue for full description of the problem and rational for this change

also adds exception catching around `multiprocess.Queue.put`, even if in that case the `put` was failing w/o raising an exception

## Comment (cmsdmwmbot, 2025-04-01T07:35:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 23 comments to review
 * Pycodestyle check: succeeded
   * 50 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2418/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-04-01T07:40:54Z)

@aspiringmind-code this change is currently running in canary and I verified that it works with `submit --dryrun`.

Looks very safe anyhow, since the object which was previously pushed to the queue is not used. Maybe it was in some very first implementation 14 years ago ? Fix is amazingly simple, what really bothers me is that there is apparently no way to make the code report the failure.

After lots of googling I found this: https://github.com/python/cpython/issues/84376
sigh

## Comment (belforte, 2025-04-01T13:16:35Z)

thanks Vijay. I will anyhow add some comments in the code.

## Comment (cmsdmwmbot, 2025-04-01T13:41:27Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 23 comments to review
 * Pycodestyle check: succeeded
   * 50 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2419/artifact/artifacts/PullRequestReport.html
