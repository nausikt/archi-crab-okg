# dmwm/CRABServer issue #8748: #854: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-10-24T10:14:01Z
Closed: 2024-10-29T20:20:39Z
URL: https://github.com/dmwm/CRABServer/issues/8748

## Opening post (cmsdmwmbot, 2024-10-24T10:14:01Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-10-24 11:45:50
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/854/)

## Comment (cmsdmwmbot, 2024-10-24T10:17:28Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
241024_101613:cmsbot_crab_20241024_121612
241024_101616:cmsbot_crab_20241024_121615
241024_101619:cmsbot_crab_20241024_121618
241024_101630:cmsbot_crab_20241024_121621
241024_101633:cmsbot_crab_20241024_121633
241024_101646:cmsbot_crab_20241024_121635
241024_101650:cmsbot_crab_rucio_transfers_20241024_121648
241024_101652:cmsbot_crab_rucio_transfers_group_20241024_121652
241024_101656:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_121655
241024_101659:cmsbot_crab_rucio_transfers_nopublication_20241024_121658
241024_101703:cmsbot_crab_rucio_transfers_withnoneedm_20241024_121702
241024_101707:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_121705
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
241024_101446:cmsbot_crab_transferOutputs
241024_101448:cmsbot_crab_transferLogs
241024_101451:cmsbot_crab_activity
241024_101453:cmsbot_crab_inputFiles
241024_101456:cmsbot_crab_disableAutomaticOutputCollection
241024_101459:cmsbot_crab_outputFiles
241024_101502:cmsbot_crab_allowUndistributedCMSSW
241024_101504:cmsbot_crab_maxMemoryMB
241024_101507:cmsbot_crab_maxJobRuntimeMin
241024_101510:cmsbot_crab_numCores
241024_101513:cmsbot_crab_scriptExe
241024_101515:cmsbot_crab_scriptArgs
241024_101518:cmsbot_crab_sendVenvFolder
241024_101521:cmsbot_crab_sendExternalFolder
241024_101524:cmsbot_crab_inputDBS
241024_101527:cmsbot_crab_useParent
241024_101530:cmsbot_crab_secondaryInputDataset
241024_101532:cmsbot_crab_lumiMaskFile
241024_101535:cmsbot_crab_lumiMaskUrl
241024_101539:cmsbot_crab_outLFNDirBase
241024_101542:cmsbot_crab_runRange
241024_101545:cmsbot_crab_ignoreLocality
241024_101547:cmsbot_crab_userInputFiles
241024_101550:cmsbot_crab_whitelist
241024_101553:cmsbot_crab_blacklist
241024_101556:cmsbot_crab_ignoreGlobalBlacklist
241024_101558:cmsbot_crab_voRole
241024_101601:cmsbot_crab_voGroup
241024_101604:cmsbot_crab_scheddName
241024_101607:cmsbot_crab_collector
241024_101609:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241024_101443:cmsbot_crab_20241024_121442
```

Finished at: 2024-10-24 12:17:07
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/854/console)

## Comment (cmsdmwmbot, 2024-10-24T11:14:09Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-10-24 12:38:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1100/console

```
{'TN': '241024_101613:cmsbot_crab_20241024_121612', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 997, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101616:cmsbot_crab_20241024_121615', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 2, 'failed': 0, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101619:cmsbot_crab_20241024_121618', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101630:cmsbot_crab_20241024_121621', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101633:cmsbot_crab_20241024_121633', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101646:cmsbot_crab_20241024_121635', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101650:cmsbot_crab_rucio_transfers_20241024_121648', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101652:cmsbot_crab_rucio_transfers_group_20241024_121652', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101656:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_121655', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101659:cmsbot_crab_rucio_transfers_nopublication_20241024_121658', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101703:cmsbot_crab_rucio_transfers_withnoneedm_20241024_121702', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101707:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_121705', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-10-24T11:14:10Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-10-24 12:41:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/550/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/550//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241024_121442  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Command recover failed


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241024_101443:cmsbot_crab_20241024_121442  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241024_121442/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
step kill - task already killed
Command recover failed
```

## Comment (cmsdmwmbot, 2024-10-24T11:14:11Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-10-24 12:42:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1206/console

```
RETRY TESTS:
numCores-check.sh 241024_101510:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 241024_101535:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 241024_101542:cmsbot_crab_runRange - 2
whitelist-check.sh 241024_101550:cmsbot_crab_whitelist - 2
blacklist-check.sh 241024_101553:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241024_101446:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241024_101448:cmsbot_crab_transferLogs - 0
activity-check.sh 241024_101451:cmsbot_crab_activity - 0
inputFiles-check.sh 241024_101453:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241024_101456:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241024_101459:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241024_101502:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241024_101504:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241024_101507:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 241024_101513:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241024_101515:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241024_101518:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241024_101521:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241024_101524:cmsbot_crab_inputDBS - 0
useParent-check.sh 241024_101527:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241024_101530:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241024_101532:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 241024_101539:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 241024_101545:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241024_101547:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 241024_101556:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241024_101558:cmsbot_crab_voRole - 0
voGroup-check.sh 241024_101601:cmsbot_crab_voGroup - 0
scheddName-check.sh 241024_101604:cmsbot_crab_scheddName - 0
collector-check.sh 241024_101607:cmsbot_crab_collector - 0
extraJDL-check.sh 241024_101609:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-10-24T11:30:11Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-10-24 13:30:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1101/console

```
{'TN': '241024_101613:cmsbot_crab_20241024_121612', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 970, 'transferring': 29, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '241024_101616:cmsbot_crab_20241024_121615', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'failed': 0, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101619:cmsbot_crab_20241024_121618', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_101630:cmsbot_crab_20241024_121621', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_101633:cmsbot_crab_20241024_121633', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241024_101646:cmsbot_crab_20241024_121635', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_101650:cmsbot_crab_rucio_transfers_20241024_121648', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_101652:cmsbot_crab_rucio_transfers_group_20241024_121652', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '241024_101656:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_121655', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101659:cmsbot_crab_rucio_transfers_nopublication_20241024_121658', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101703:cmsbot_crab_rucio_transfers_withnoneedm_20241024_121702', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '241024_101707:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_121705', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-10-24T12:14:16Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-10-24 13:38:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1207/console

```
RETRY TESTS:
numCores-check.sh 241024_101510:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241024_101446:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241024_101448:cmsbot_crab_transferLogs - 0
activity-check.sh 241024_101451:cmsbot_crab_activity - 0
inputFiles-check.sh 241024_101453:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241024_101456:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241024_101459:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241024_101502:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241024_101504:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241024_101507:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 241024_101513:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241024_101515:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241024_101518:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241024_101521:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241024_101524:cmsbot_crab_inputDBS - 0
useParent-check.sh 241024_101527:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241024_101530:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241024_101532:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241024_101535:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241024_101539:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241024_101542:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241024_101545:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241024_101547:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241024_101550:cmsbot_crab_whitelist - 0
blacklist-check.sh 241024_101553:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241024_101556:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241024_101558:cmsbot_crab_voRole - 0
voGroup-check.sh 241024_101601:cmsbot_crab_voGroup - 0
scheddName-check.sh 241024_101604:cmsbot_crab_scheddName - 0
collector-check.sh 241024_101607:cmsbot_crab_collector - 0
extraJDL-check.sh 241024_101609:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-10-24T12:15:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-10-24 14:15:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1104/console

```
{'TN': '241024_101613:cmsbot_crab_20241024_121612', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/970/0'}
{'TN': '241024_101616:cmsbot_crab_20241024_121615', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 5, 'failed': 0}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101619:cmsbot_crab_20241024_121618', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/0'}
{'TN': '241024_101630:cmsbot_crab_20241024_121621', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/0'}
{'TN': '241024_101633:cmsbot_crab_20241024_121633', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/0'}
{'TN': '241024_101646:cmsbot_crab_20241024_121635', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/0'}
{'TN': '241024_101650:cmsbot_crab_rucio_transfers_20241024_121648', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/0'}
{'TN': '241024_101652:cmsbot_crab_rucio_transfers_group_20241024_121652', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/0'}
{'TN': '241024_101656:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_121655', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101659:cmsbot_crab_rucio_transfers_nopublication_20241024_121658', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101703:cmsbot_crab_rucio_transfers_withnoneedm_20241024_121702', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/0'}
{'TN': '241024_101707:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_121705', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-10-24T13:14:23Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-10-24 14:38:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1210/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241024_101446:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241024_101448:cmsbot_crab_transferLogs - 0
activity-check.sh 241024_101451:cmsbot_crab_activity - 0
inputFiles-check.sh 241024_101453:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241024_101456:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241024_101459:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241024_101502:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241024_101504:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241024_101507:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241024_101510:cmsbot_crab_numCores - 0
scriptExe-check.sh 241024_101513:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241024_101515:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241024_101518:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241024_101521:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241024_101524:cmsbot_crab_inputDBS - 0
useParent-check.sh 241024_101527:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241024_101530:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241024_101532:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241024_101535:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241024_101539:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241024_101542:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241024_101545:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241024_101547:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241024_101550:cmsbot_crab_whitelist - 0
blacklist-check.sh 241024_101553:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241024_101556:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241024_101558:cmsbot_crab_voRole - 0
voGroup-check.sh 241024_101601:cmsbot_crab_voGroup - 0
scheddName-check.sh 241024_101604:cmsbot_crab_scheddName - 0
collector-check.sh 241024_101607:cmsbot_crab_collector - 0
extraJDL-check.sh 241024_101609:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-10-24T14:14:30Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-10-24 15:47:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1108/console

```
{'TN': '241024_101613:cmsbot_crab_20241024_121612', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241024_101616:cmsbot_crab_20241024_121615', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 5, 'failed': 0}, 'publication (fail/tdb/DBS)': '0/0/1'}
{'TN': '241024_101619:cmsbot_crab_20241024_121618', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_101630:cmsbot_crab_20241024_121621', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_101633:cmsbot_crab_20241024_121633', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241024_101646:cmsbot_crab_20241024_121635', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_101650:cmsbot_crab_rucio_transfers_20241024_121648', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_101652:cmsbot_crab_rucio_transfers_group_20241024_121652', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_101656:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_121655', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101659:cmsbot_crab_rucio_transfers_nopublication_20241024_121658', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_101703:cmsbot_crab_rucio_transfers_withnoneedm_20241024_121702', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_101707:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_121705', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
