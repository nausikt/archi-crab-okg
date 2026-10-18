# dmwm/CRABServer pull request #9006: Add columns to task db 8973 (#8981)

State: closed
Opened: 2025-03-19T15:15:11Z
Closed: 2025-03-24T11:23:21Z
Merged: 2025-03-24T11:23:21Z
URL: https://github.com/dmwm/CRABServer/pull/9006

## Opening post (belforte, 2025-03-19T15:15:11Z)

* add 3 new columns to task DB for 8973

* add edit-task API

* make numJobs and DA status appear in crabserver UI main page


tested on cmsweb-test2

## Comment (cmsdmwmbot, 2025-03-19T15:18:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 37 comments to review
 * Pycodestyle check: succeeded
   * 219 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2403/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-24T11:23:06Z)

thanks Vijay. At your convenience you can proceed with adding the new columns to DB, so we can deploy the new REST in preprod. Deployment in prod is somehow undefined now until we have come to some conclusion on v3.250310

## Comment (aspiringmind-code, 2025-03-24T12:22:03Z)

@belforte The three new columns have been added to all Oracle DBs. We can deploy REST in preprod now.
