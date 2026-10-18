# dmwm/CRABClient pull request #5392: ensure that a valid jobId is passed to run_job.sh. Fix #5390

State: closed
Opened: 2025-05-21T13:46:02Z
Closed: 2025-05-22T08:38:51Z
Merged: 2025-05-22T08:38:51Z
URL: https://github.com/dmwm/CRABClient/pull/5392

## Opening post (belforte, 2025-05-21T13:46:02Z)

thanks for the hint @aspiringmind-code .
I have minimally changed to avoid `sh run_job 0` which also fails.
Please check whether you still like it.

## Comment (cmsdmwmbot, 2025-05-21T13:49:53Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 8 comments to review
 * Pycodestyle check: succeeded
   * 5 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1117/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-22T08:38:45Z)

thanks !
