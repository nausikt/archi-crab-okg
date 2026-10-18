# dmwm/CRABServer pull request #7504: Update task state to FAILED when TaskWorkerException occur

State: closed
Opened: 2023-01-25T12:12:51Z
Closed: 2023-01-25T13:32:57Z
Merged: 2023-01-25T13:32:57Z
URL: https://github.com/dmwm/CRABServer/pull/7504

## Opening post (novicecpp, 2023-01-25T12:12:51Z)

Fix https://github.com/dmwm/CRABServer/issues/5983

Update task state to FAILED when TaskWorkerException using [failTask()](https://github.com/dmwm/CRABServer/blob/9df0542eae377b76b315dcb8292c642ba57578ba/src/python/TaskWorker/Worker.py#L48).

I cannot reproduce the actual task because the user config and sandbox are long gone. So, I force raising exception inside the "try" splitting step [like this](https://github.com/dmwm/CRABServer/commit/20cddde1326012171404252b236fa050d3f68069) and check result in `crab status` command:

https://cmsweb-test12.cern.ch/crabserver/ui/task/230124_135939%3Atseethon_crab_autosplit_hc_test12_20230124_145936

![Screenshot from 2023-01-25 12-18-23](https://user-images.githubusercontent.com/2346664/214557080-8dc20929-074e-4dc9-82e3-5f1e5dff90b2.png)

## Comment (cmsdmwmbot, 2023-01-25T12:17:03Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 3 warnings
   * 26 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1401/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-01-25T12:20:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 3 warnings
   * 26 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1402/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-01-25T12:22:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 3 warnings
   * 26 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1403/artifact/artifacts/PullRequestReport.html
