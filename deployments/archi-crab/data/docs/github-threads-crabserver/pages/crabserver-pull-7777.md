# dmwm/CRABServer pull request #7777: allow Publisher to retrieve dbs_blockname and block_complete

State: closed
Opened: 2023-07-18T20:36:44Z
Closed: 2023-08-01T19:53:12Z
Merged: 2023-08-01T19:53:12Z
URL: https://github.com/dmwm/CRABServer/pull/7777

## Opening post (belforte, 2023-07-18T20:36:44Z)

from filetransfersdb

## Comment (belforte, 2023-07-18T20:38:15Z)

tested on cmsweb-test2, so syntax and column name spelling are OK. Otherwise it is extremely safe.

## Comment (cmsdmwmbot, 2023-07-18T20:39:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 43 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1616/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-18T21:39:47Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
 * Pycodestyle check: succeeded
   * 6 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1618/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-18T21:51:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1619/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-18T21:59:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1620/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-18T22:05:34Z)

first commit (the actual change) is safe. 2nd one (pylint) is of course dangerous like all code cleanup. Will make sure to test this with Publisher_schedd, besides of course PostJobs and standard ASO

## Comment (cmsdmwmbot, 2023-07-18T22:07:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1621/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-18T22:13:54Z)

deployed on cmsweb-test2 via `start.sh -g`

## Comment (belforte, 2023-07-21T11:21:12Z)

minimal test (CCV) on cmsweb-test2 passed https://github.com/dmwm/CRABServer/issues/7780
Now some tasks where to vaildate publication
https://cmssdt.cern.ch/dmwm-jenkins/view/CRAB/job/CRABServer_ExecuteTests/448/

## Comment (belforte, 2023-08-01T15:18:37Z)

last Jenkins got stuck in xfer, then I left for vacation.
Let's run again.

## Comment (belforte, 2023-08-01T19:53:00Z)

Current publisher_schedd functionality is not affected. Validated
