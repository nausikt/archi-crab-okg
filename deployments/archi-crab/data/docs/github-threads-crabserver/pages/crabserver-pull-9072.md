# dmwm/CRABServer pull request #9072: Fix #8928

State: closed
Opened: 2025-05-12T18:52:35Z
Closed: 2025-05-22T10:49:08Z
Merged: 2025-05-22T10:49:08Z
URL: https://github.com/dmwm/CRABServer/pull/9072

## Opening post (aspiringmind-code, 2025-05-12T18:52:35Z)

Populate tm_uploaded in both dryrun and without dryrun cases. See Issue #8928 
Dry run test
```
DEBUG 2025-05-12 18:41:17.896 UTC: 	 Result: {'desc': {'columns': ['tm_taskname', 'tm_task_status', 'tm_task_command', 'tm_user_role', 'tm_user_group', 'tm_task_failure', 'tm_split_algo', 'tm_split_args', 'tm_save_logs', 'tm_username', 'tm_user_dn', 'tm_arguments', 'tm_input_dataset', 'tm_dbs_url', 'tm_task_warnings', 'tm_publication', 'tm_user_webdir', 'tm_output_dataset', 'tm_collector', 'tm_schedd', 'tm_dry_run', 'clusterid', 'tm_start_time', 'tw_name', 'tm_dagman_status', 'tm_num_jobs', 'tm_uploaded']}, 'result': [{'result': 'ok'}]}
INFO 2025-05-12 18:41:17.897 UTC: 	 To check task progress, use 'crab status'
INFO 2025-05-12 18:41:17.897 UTC: 	 Task continuation request successfully sent to the CRAB3 server
INFO 2025-05-12 18:41:17.898 UTC: 	 Log file is /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250512_203737/crab.log
```

For Without dryrun test
See [task](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=vchakrav&var-task=250512_183609%3Avchakrav_crab_20250512_203606&from=1747071369000&to=now)

## Comment (cmsdmwmbot, 2025-05-12T18:56:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 41 comments to review
 * Pycodestyle check: succeeded
   * 382 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2450/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-13T08:43:39Z)

at first sight it looks like you implemented this twice. Via `edit` API and via ad-hoc SQL. What am I missing ?

## Comment (belforte, 2025-05-13T09:14:31Z)

Did you try to simply add the call to edit API inside Uploader.py ?

## Comment (cmsdmwmbot, 2025-05-20T07:54:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 41 comments to review
 * Pycodestyle check: succeeded
   * 382 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2457/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-20T08:27:04Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 42 comments to review
 * Pycodestyle check: succeeded
   * 381 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2458/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-20T10:09:07Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 42 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2460/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-05-20T10:27:55Z)

> Did you try to simply add the call to edit API inside Uploader.py ?

I tried. I am not sure how it will work for we don't have self.crabserver. Adding the SQL follows the pattern used in the script. To make edit work inside the DataWorkFlow.py would require deeper changes. This is more straightforward imho.

## Comment (cmsdmwmbot, 2025-05-20T12:43:04Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 42 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2461/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-20T13:44:05Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 42 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2462/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-20T13:52:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 300 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2463/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-20T14:40:32Z)

I think that you do not need to touch DataWorkflow either

## Comment (aspiringmind-code, 2025-05-22T10:48:55Z)

Thanks for the review. Unnecessary changes removed. Merging.

## Comment (cmsdmwmbot, 2025-05-22T10:49:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 300 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2468/artifact/artifacts/PullRequestReport.html
