# dmwm/CRABClient pull request #5423: No dag node parsing in client anymore 5399

State: closed
Opened: 2025-10-30T16:39:20Z
Closed: 2025-10-31T08:41:46Z
Merged: 2025-10-31T08:41:45Z
URL: https://github.com/dmwm/CRABClient/pull/5423

## Opening post (belforte, 2025-10-30T16:39:20Z)

removes a lot of codes which has been moved to the task_process' [cache_status.py](https://github.com/dmwm/CRABServer/blob/master/scripts/dagman/task_process/cache_status.py) in https://github.com/dmwm/CRABServer/commit/7c07eb23a30985a17a26e8399cf95e84b0d7cb40

## Comment (cmsdmwmbot, 2025-10-30T16:42:08Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 188 comments to review
 * Pycodestyle check: succeeded
   * 96 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1147/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-10-31T08:41:07Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 188 comments to review
 * Pycodestyle check: succeeded
   * 94 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1148/artifact/artifacts/PullRequestReport.html
