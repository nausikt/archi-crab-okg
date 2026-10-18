# dmwm/CRABServer issue #8347: #760: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-22T15:43:56Z
Closed: 2024-04-24T14:53:21Z
URL: https://github.com/dmwm/CRABServer/issues/8347

## Opening post (cmsdmwmbot, 2024-04-22T15:43:56Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-04-22 17:43:55
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/760/)

## Comment (cmsdmwmbot, 2024-04-22T15:46:51Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240422_154540:cmsbot_crab_20240422_174539
240422_154542:cmsbot_crab_20240422_174541
240422_154544:cmsbot_crab_20240422_174544
240422_154546:cmsbot_crab_20240422_174546
240422_154549:cmsbot_crab_20240422_174548
240422_154610:cmsbot_crab_20240422_174550
240422_154613:cmsbot_crab_rucio_transfers_20240422_174611
240422_154615:cmsbot_crab_rucio_transfers_group_20240422_174615
240422_154619:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240422_174617
240422_154622:cmsbot_crab_rucio_transfers_nopublication_20240422_174621
240422_154626:cmsbot_crab_rucio_transfers_withnoneedm_20240422_174624
240422_154629:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240422_174628
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240422_154422:cmsbot_crab_transferOutputs
240422_154424:cmsbot_crab_transferLogs
240422_154427:cmsbot_crab_activity
240422_154429:cmsbot_crab_inputFiles
240422_154432:cmsbot_crab_disableAutomaticOutputCollection
240422_154434:cmsbot_crab_outputFiles
240422_154436:cmsbot_crab_allowUndistributedCMSSW
240422_154439:cmsbot_crab_maxMemoryMB
240422_154441:cmsbot_crab_maxJobRuntimeMin
240422_154443:cmsbot_crab_numCores
240422_154446:cmsbot_crab_scriptExe
240422_154448:cmsbot_crab_scriptArgs
240422_154451:cmsbot_crab_sendVenvFolder
240422_154453:cmsbot_crab_sendExternalFolder
240422_154455:cmsbot_crab_inputDBS
240422_154457:cmsbot_crab_useParent
240422_154500:cmsbot_crab_secondaryInputDataset
240422_154502:cmsbot_crab_lumiMaskFile
240422_154507:cmsbot_crab_lumiMaskUrl
240422_154510:cmsbot_crab_outLFNDirBase
240422_154513:cmsbot_crab_runRange
240422_154515:cmsbot_crab_ignoreLocality
240422_154517:cmsbot_crab_userInputFiles
240422_154520:cmsbot_crab_whitelist
240422_154522:cmsbot_crab_blacklist
240422_154524:cmsbot_crab_ignoreGlobalBlacklist
240422_154527:cmsbot_crab_voRole
240422_154529:cmsbot_crab_voGroup
240422_154531:cmsbot_crab_scheddName
240422_154534:cmsbot_crab_collector
240422_154536:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240422_154419:cmsbot_crab_20240422_174418
```

Finished at: 2024-04-22 17:46:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/760/console)

## Comment (novicecpp, 2024-04-22T15:47:37Z)

Validating `crab-prod-tw02`.

## Comment (cmsdmwmbot, 2024-04-22T16:11:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-22 18:11:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/867/console

```
{'TN': '240422_154540:cmsbot_crab_20240422_174539', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 985, 'running': 15}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154542:cmsbot_crab_20240422_174541', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154544:cmsbot_crab_20240422_174544', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154546:cmsbot_crab_20240422_174546', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154549:cmsbot_crab_20240422_174548', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154610:cmsbot_crab_20240422_174550', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154613:cmsbot_crab_rucio_transfers_20240422_174611', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154615:cmsbot_crab_rucio_transfers_group_20240422_174615', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154619:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240422_174617', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154622:cmsbot_crab_rucio_transfers_nopublication_20240422_174621', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 37, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154626:cmsbot_crab_rucio_transfers_withnoneedm_20240422_174624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154629:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240422_174628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-22T16:14:32Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-22 18:14:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/534/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/534//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-22T16:15:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-22 18:15:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1037/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240422_154507:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240422_154513:cmsbot_crab_runRange - 2
whitelist-check.sh 240422_154520:cmsbot_crab_whitelist - 2
blacklist-check.sh 240422_154522:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240422_154422:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240422_154424:cmsbot_crab_transferLogs - 0
activity-check.sh 240422_154427:cmsbot_crab_activity - 0
inputFiles-check.sh 240422_154429:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240422_154432:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240422_154436:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240422_154439:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240422_154441:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240422_154443:cmsbot_crab_numCores - 0
scriptExe-check.sh 240422_154446:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240422_154448:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240422_154451:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240422_154453:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240422_154455:cmsbot_crab_inputDBS - 0
useParent-check.sh 240422_154457:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240422_154500:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240422_154502:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240422_154510:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240422_154515:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240422_154517:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240422_154524:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240422_154527:cmsbot_crab_voRole - 0
voGroup-check.sh 240422_154529:cmsbot_crab_voGroup - 0
scheddName-check.sh 240422_154531:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240422_154536:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240422_154434:cmsbot_crab_outputFiles - 1
collector-check.sh 240422_154534:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-22T16:27:24Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-04-22 18:27:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/868/console

```
{'TN': '240422_154540:cmsbot_crab_20240422_174539', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 946, 'transferring': 38, 'running': 15, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154542:cmsbot_crab_20240422_174541', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154544:cmsbot_crab_20240422_174544', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154546:cmsbot_crab_20240422_174546', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154549:cmsbot_crab_20240422_174548', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 92, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154610:cmsbot_crab_20240422_174550', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 5, 'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154613:cmsbot_crab_rucio_transfers_20240422_174611', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154615:cmsbot_crab_rucio_transfers_group_20240422_174615', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154619:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240422_174617', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154622:cmsbot_crab_rucio_transfers_nopublication_20240422_174621', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 37, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154626:cmsbot_crab_rucio_transfers_withnoneedm_20240422_174624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154629:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240422_174628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-22T16:41:36Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-22 18:41:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1038/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240422_154422:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240422_154424:cmsbot_crab_transferLogs - 0
activity-check.sh 240422_154427:cmsbot_crab_activity - 0
inputFiles-check.sh 240422_154429:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240422_154432:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240422_154436:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240422_154439:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240422_154441:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240422_154443:cmsbot_crab_numCores - 0
scriptExe-check.sh 240422_154446:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240422_154448:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240422_154451:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240422_154453:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240422_154455:cmsbot_crab_inputDBS - 0
useParent-check.sh 240422_154457:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240422_154500:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240422_154502:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240422_154507:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240422_154510:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240422_154513:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240422_154515:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240422_154517:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240422_154520:cmsbot_crab_whitelist - 0
blacklist-check.sh 240422_154522:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240422_154524:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240422_154527:cmsbot_crab_voRole - 0
voGroup-check.sh 240422_154529:cmsbot_crab_voGroup - 0
scheddName-check.sh 240422_154531:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240422_154536:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240422_154434:cmsbot_crab_outputFiles - 1
collector-check.sh 240422_154534:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-22T17:14:34Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-04-22 19:14:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/869/console

```
{'TN': '240422_154540:cmsbot_crab_20240422_174539', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 980, 'transferring': 16, 'running': 3, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/968/968'}
{'TN': '240422_154542:cmsbot_crab_20240422_174541', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154544:cmsbot_crab_20240422_174544', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240422_154546:cmsbot_crab_20240422_174546', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240422_154549:cmsbot_crab_20240422_174548', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240422_154610:cmsbot_crab_20240422_174550', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240422_154613:cmsbot_crab_rucio_transfers_20240422_174611', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154615:cmsbot_crab_rucio_transfers_group_20240422_174615', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154619:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240422_174617', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154622:cmsbot_crab_rucio_transfers_nopublication_20240422_174621', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 37, 'failed': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154626:cmsbot_crab_rucio_transfers_withnoneedm_20240422_174624', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'failed': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154629:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240422_174628', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-22T18:47:24Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-04-22 20:47:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/870/console

```
{'TN': '240422_154540:cmsbot_crab_20240422_174539', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'transferring': 1, 'running': 1}, 'publication (fail/tdb/DBS)': '0/998/998'}
{'TN': '240422_154542:cmsbot_crab_20240422_174541', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240422_154544:cmsbot_crab_20240422_174544', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240422_154546:cmsbot_crab_20240422_174546', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240422_154549:cmsbot_crab_20240422_174548', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240422_154610:cmsbot_crab_20240422_174550', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240422_154613:cmsbot_crab_rucio_transfers_20240422_174611', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154615:cmsbot_crab_rucio_transfers_group_20240422_174615', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154619:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240422_174617', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154622:cmsbot_crab_rucio_transfers_nopublication_20240422_174621', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154626:cmsbot_crab_rucio_transfers_withnoneedm_20240422_174624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154629:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240422_174628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-22T20:49:29Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-04-22 22:49:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/871/console

```
{'TN': '240422_154540:cmsbot_crab_20240422_174539', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 999, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/999/999'}
{'TN': '240422_154542:cmsbot_crab_20240422_174541', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240422_154544:cmsbot_crab_20240422_174544', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240422_154546:cmsbot_crab_20240422_174546', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240422_154549:cmsbot_crab_20240422_174548', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240422_154610:cmsbot_crab_20240422_174550', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240422_154613:cmsbot_crab_rucio_transfers_20240422_174611', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154615:cmsbot_crab_rucio_transfers_group_20240422_174615', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154619:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240422_174617', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154622:cmsbot_crab_rucio_transfers_nopublication_20240422_174621', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154626:cmsbot_crab_rucio_transfers_withnoneedm_20240422_174624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154629:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240422_174628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-22T22:50:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-04-23 00:50:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/872/console

```
{'TN': '240422_154540:cmsbot_crab_20240422_174539', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 999, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/999/999'}
{'TN': '240422_154542:cmsbot_crab_20240422_174541', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240422_154544:cmsbot_crab_20240422_174544', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240422_154546:cmsbot_crab_20240422_174546', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240422_154549:cmsbot_crab_20240422_174548', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240422_154610:cmsbot_crab_20240422_174550', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240422_154613:cmsbot_crab_rucio_transfers_20240422_174611', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154615:cmsbot_crab_rucio_transfers_group_20240422_174615', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154619:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240422_174617', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154622:cmsbot_crab_rucio_transfers_nopublication_20240422_174621', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154626:cmsbot_crab_rucio_transfers_withnoneedm_20240422_174624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240422_154629:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240422_174628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (novicecpp, 2024-04-24T14:53:21Z)

This run against old tag https://github.com/dmwm/CRABServer/releases/tag/v3.240325
Supersede by https://github.com/dmwm/CRABServer/issues/8349
