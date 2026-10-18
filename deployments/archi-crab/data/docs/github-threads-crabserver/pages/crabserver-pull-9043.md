# dmwm/CRABServer pull request #9043: report DAG status, NJob to DB. Fix #7766 Fix #8394

State: closed
Opened: 2025-04-10T17:09:01Z
Closed: 2025-04-11T13:50:19Z
Merged: 2025-04-11T13:50:19Z
URL: https://github.com/dmwm/CRABServer/pull/9043

## Opening post (belforte, 2025-04-10T17:09:01Z)

this PR brings in 3 things

1. reports to DB Number of Jobs in DAG. Works also for automatic splitting.
2. reports to DB status of DAG. More work still needed for automatic splitting, but OK otherwise
3. runs new version of status_cache.py code which was in since years but never enabled. At the moment the new version is run "parassitically", output compared and mail sent to Stefano in case of difference.

I'd like to have this in Canary so I can make sure that 3. is OK (or fix) and to get examples of more complex automatic splitting jobs to finalize code

## Comment (cmsdmwmbot, 2025-04-10T17:13:33Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 27 comments to review
 * Pycodestyle check: succeeded
   * 140 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2430/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-04-11T10:17:10Z)

thanks @aspiringmind-code for fast and thorough review.

## Comment (cmsdmwmbot, 2025-04-11T12:33:42Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 30 comments to review
 * Pycodestyle check: succeeded
   * 177 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2431/artifact/artifacts/PullRequestReport.html
