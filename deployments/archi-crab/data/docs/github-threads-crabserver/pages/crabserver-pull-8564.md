# dmwm/CRABServer pull request #8564: Add submitrefused 7989

State: closed
Opened: 2024-07-25T14:12:52Z
Closed: 2024-07-30T09:11:40Z
Merged: 2024-07-30T09:11:40Z
URL: https://github.com/dmwm/CRABServer/pull/8564

## Opening post (belforte, 2024-07-25T14:12:52Z)

Fix #7989 

I have reviewed all cases where TaskWorkerException is raised and replaced with SubmissionRefusedException where appropriate. But this is very difficult/annoying to test since it requires to reproduce all possible user mistakes :-(

I had tested the most common cases (dataset not in DBS, stageout error)

## Comment (cmsdmwmbot, 2024-07-25T14:15:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 3 warnings
   * 183 comments to review
 * Pycodestyle check: succeeded
   * 348 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2066/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-07-25T19:51:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 warnings
   * 135 comments to review
 * Pycodestyle check: succeeded
   * 347 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2069/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-29T10:49:59Z)

@mapellidario ping

## Comment (belforte, 2024-07-29T13:39:18Z)

nice finding Dario. I am adding it there as well.

## Comment (cmsdmwmbot, 2024-07-29T15:02:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 warnings
   * 135 comments to review
 * Pycodestyle check: succeeded
   * 347 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2072/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-29T16:31:59Z)

@mapellidario if that was your only comment, it should be addressed now.
