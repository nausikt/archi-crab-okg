# dmwm/CRABServer pull request #8558: put all calls to fts3.get_job_status in try/except Fix #8556

State: closed
Opened: 2024-07-24T12:58:33Z
Closed: 2024-07-24T14:16:17Z
Merged: 2024-07-24T14:16:17Z
URL: https://github.com/dmwm/CRABServer/pull/8558

## Opening post (belforte, 2024-07-24T12:58:33Z)

(no text)

## Comment (belforte, 2024-07-24T12:59:58Z)

I decided to simply move the second call to fts3.get_job_status inside the existing try/except. Less lines overall !

## Comment (cmsdmwmbot, 2024-07-24T13:01:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 16 comments to review
 * Pycodestyle check: succeeded
   * 14 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2061/artifact/artifacts/PullRequestReport.html
