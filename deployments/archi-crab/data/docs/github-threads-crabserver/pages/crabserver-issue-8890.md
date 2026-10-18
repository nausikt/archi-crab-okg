# dmwm/CRABServer issue #8890: odd behavior of CCV test

State: closed
Opened: 2025-01-22T17:50:16Z
Closed: 2025-01-30T10:34:15Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/8890

## Opening post (belforte, 2025-01-22T17:50:16Z)

here the test failed because one task was still running. That's OK. The test is supposed to wait and be retried later.
But instead the test exited with SUCCESS and only a partial list of things actually verified.
From https://gitlab.cern.ch/crab3/CRABServer/-/jobs/49700003/raw part of pipeline https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/9943523 for tag v3.250121


```text

Rucio client intialized for account crabint1
CRAB project directory:		/home/gitlab-runner/shell/builds/sedxNxqzs/0/crab3/CRABServer/workdir/CMSSW_13_0_2/src/crab_maxJobRuntimeMin
Task name:			250122_142923:crabint1_crab_maxJobRuntimeMin
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-preprod-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-testbed.cern.ch/crabserver/ui/task/250122_142923%3Acrabint1_crab_maxJobRuntimeMin
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=crabint1&var-task=250122_142923%3Acrabint1_crab_maxJobRuntimeMin&from=1737552563000&to=now
Status on the scheduler:	SUBMITTED

Jobs status:                    transferring 		100.0% (1/1)

No publication information (publication has been disabled in the CRAB configuration file)

Warning: the max jobs runtime is less than 30% of the task requested value (100 min), please consider to request a lower value for failed jobs (allowed through crab resubmit) and/or improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task.

Warning: the average jobs CPU efficiency is less than 50%, please consider to improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task

Summary of run jobs:
 * Memory: 429MB min, 429MB max, 430MB ave
 * Runtime: 0:08:14 min, 0:08:14 max, 0:08:14 ave
 * CPU eff: 2% min, 2% max, 2% ave
 * Waste: 0:00:08 (2% of total)

Log file is /home/gitlab-runner/shell/builds/sedxNxqzs/0/crab3/CRABServer/workdir/CMSSW_13_0_2/src/crab_maxJobRuntimeMin/crab.log
+ '[' 0 -ne 0 ']'
+ local isSub=0
+ local isDone=0
+ local isFailed=0
+ grep -q 'Status on the scheduler:.*SUBMITTED' statusLog.txt
+ isSub=1
+ grep -q 'Status on the scheduler:.*COMPLETED' statusLog.txt
+ grep -q 'Status on the scheduler:.*FAILED' statusLog.txt
+ case $targetStatus in
+ '[' 1 -eq 1 ']'
+ exit 2
+ ERR=true
+ cd /home/gitlab-runner/shell/builds/sedxNxqzs/0/crab3/CRABServer/workdir
+ export RETRY=0
+ RETRY=0
+ export MAX_RETRY=4
+ MAX_RETRY=4
+ TEST_RESULT=FAILED
+ MESSAGE='Test failed. Investigate manually'
```
[....]
```text

+ '[' -s failed_tests ']'
+ echo -e '\nFAILED TESTS:\n none'
+ for result in "${!results[@]}"
+ '[' -s retry_tests ']'
+ echo -e '\nRETRY TESTS:\n none'
++ date '+%Y-%m-%d %H:%M:%S'
+ echo -e '**Test:** Client configuration validation\n**Result:** SUCCEEDED\n**Attempt:** 0 out of 4. Test is done.\n**Finished at:** 2025-01-22 15:55:13\n**Test log:** https://gitlab.cern.ch/crab3/CRABServer/-/jobs/49700003\n'
++ cat message_CCVResult_interim
+ echo -e '```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250122_142857:crabint1_crab_transferOutputs - 0
transferLogs-check.sh 250122_142900:crabint1_crab_transferLogs - 0
activity-check.sh 250122_142904:crabint1_crab_activity - 0
inputFiles-check.sh 250122_142907:crabint1_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250122_142911:crabint1_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250122_142914:crabint1_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250122_142917:crabint1_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250122_142920:crabint1_crab_maxMemoryMB - 0

FAILED TESTS:
 none

RETRY TESTS:
 none\n```'
+ [[ SUCCEEDED == \F\U\L\L\-\S\T\A\T\U\S\-\U\N\K\N\O\W\N ]]
+ [[ SUCCEEDED == \S\U\C\C\E\E\D\E\D ]]
+ exit 0
```

## Comment (belforte, 2025-01-23T11:15:22Z)

also I was expecting the script to test all tasks and make a full tally of failed/success/undefined

## Comment (aspiringmind-code, 2025-01-30T10:34:15Z)

Fixed in https://github.com/dmwm/CRABServer/pull/8899
