# dmwm/CRABServer pull request #9234: remove unused/obsolete files. Fix #9231

State: closed
Opened: 2025-11-19T09:42:08Z
Closed: 2025-11-19T09:53:12Z
Merged: 2025-11-19T09:53:11Z
URL: https://github.com/dmwm/CRABServer/pull/9234

## Opening post (belforte, 2025-11-19T09:42:08Z)

I checked those files and they are not used anywhere anymore.
Creating of a new DB is covered in our MD documentation
https://cmscrab.docs.cern.ch/crab-components/crab-rest/database.html#crab-database-developer
which is pretty similar to old `bin/setupdb.sh`

## Comment (cmsdmwmbot, 2025-11-19T09:44:41Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2672/artifact/artifacts/PullRequestReport.html
