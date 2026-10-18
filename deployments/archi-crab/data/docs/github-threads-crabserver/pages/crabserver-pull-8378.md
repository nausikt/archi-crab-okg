# dmwm/CRABServer pull request #8378: Deal with failed migrations 8244

State: closed
Opened: 2024-05-03T12:52:43Z
Closed: 2024-05-06T22:28:28Z
Merged: 2024-05-06T22:28:28Z
URL: https://github.com/dmwm/CRABServer/pull/8378

## Opening post (belforte, 2024-05-03T12:52:43Z)

this combines
1. refactoring so that almost all code common to TaskPublish and TaskPublishRucio is in common Publish(Dbs)Utils
2. catch "migration already exists" and make sure that it is retried

## Comment (cmsdmwmbot, 2024-05-03T15:13:10Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1968/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-05-03T15:36:10Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1969/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-06T21:13:41Z)

there's a bug in the new code
```
2024-05-06 23:12:05,108:INFO: Found 1 files not already present in DBS which will be published.
2024-05-06 23:12:05,108:INFO: List of parent blocks that need to be migrated from https://cmsweb-prod.cern.ch:8443/dbs/prod/global/DBSReader:
{'/DisplacedJet/Run2022E-10Dec2022-v2/MINIAOD#018fd373-22d0-4f06-b90b-ace3d5cd37ff'}
2024-05-06 23:12:05,108:ERROR: Exception raised inside migrateByBlockDBS3
migrateByBlockDBS3() got multiple values for argument 'logger'
Traceback (most recent call last):
  File "/data/repos/CRABServer/src/python/Publisher/TaskPublish.py", line 197, in publishInDBS3
    statusCode, failureMsg = migrateByBlockDBS3(taskname, migrateApi, destReadApi, sourceApi,
TypeError: migrateByBlockDBS3() got multiple values for argument 'logger'
2024-05-06 23:12:05,109:INFO: Exception raised inside migrateByBlockDBS3 Not publishing any files.

```

## Comment (cmsdmwmbot, 2024-05-06T21:42:10Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1970/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-06T22:19:07Z)

OK. Problem https://github.com/dmwm/CRABServer/pull/8378#issuecomment-2096929246 is fixex by previous commit.
