# dmwm/CRABServer issue #8303: #735: Test prod CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2024-03-25T21:34:23Z
Closed: 2024-03-26T08:21:33Z
URL: https://github.com/dmwm/CRABServer/issues/8303

## Opening post (cmsdmwmbot, 2024-03-25T21:34:23Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-03-25 22:34:22
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/735/)

## Comment (cmsdmwmbot, 2024-03-25T21:37:35Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240325_213626:cmsbot_crab_20240325_223626
240325_213629:cmsbot_crab_20240325_223628
240325_213631:cmsbot_crab_20240325_223630
240325_213633:cmsbot_crab_20240325_223632
240325_213635:cmsbot_crab_20240325_223634
240325_213655:cmsbot_crab_20240325_223637
240325_213658:cmsbot_crab_rucio_transfers_20240325_223657
240325_213701:cmsbot_crab_rucio_transfers_group_20240325_223700
240325_213704:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240325_223702
240325_213707:cmsbot_crab_rucio_transfers_nopublication_20240325_223705
240325_213710:cmsbot_crab_rucio_transfers_withnoneedm_20240325_223709
240325_213713:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240325_223712
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240325_213510:cmsbot_crab_transferOutputs
240325_213512:cmsbot_crab_transferLogs
240325_213514:cmsbot_crab_activity
240325_213516:cmsbot_crab_inputFiles
240325_213518:cmsbot_crab_disableAutomaticOutputCollection
240325_213521:cmsbot_crab_outputFiles
240325_213523:cmsbot_crab_allowUndistributedCMSSW
240325_213525:cmsbot_crab_maxMemoryMB
240325_213527:cmsbot_crab_maxJobRuntimeMin
240325_213529:cmsbot_crab_numCores
240325_213532:cmsbot_crab_scriptExe
240325_213534:cmsbot_crab_scriptArgs
240325_213536:cmsbot_crab_sendVenvFolder
240325_213545:cmsbot_crab_sendExternalFolder
240325_213548:cmsbot_crab_inputDBS
240325_213550:cmsbot_crab_useParent
240325_213552:cmsbot_crab_secondaryInputDataset
240325_213554:cmsbot_crab_lumiMaskFile
240325_213556:cmsbot_crab_lumiMaskUrl
240325_213600:cmsbot_crab_outLFNDirBase
240325_213602:cmsbot_crab_runRange
240325_213604:cmsbot_crab_ignoreLocality
240325_213606:cmsbot_crab_userInputFiles
240325_213608:cmsbot_crab_whitelist
240325_213611:cmsbot_crab_blacklist
240325_213613:cmsbot_crab_ignoreGlobalBlacklist
240325_213615:cmsbot_crab_voRole
240325_213617:cmsbot_crab_voGroup
240325_213620:cmsbot_crab_scheddName
240325_213622:cmsbot_crab_collector
240325_213624:cmsbot_crab_extraJDL
```

Finished at: 2024-03-25 22:37:13
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/735/console)

## Comment (cmsdmwmbot, 2024-03-25T21:59:01Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-25 22:59:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/835/console

```
{'TN': '240325_213626:cmsbot_crab_20240325_223626', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 951, 'idle': 1, 'running': 48}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213629:cmsbot_crab_20240325_223628', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213631:cmsbot_crab_20240325_223630', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213633:cmsbot_crab_20240325_223632', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213635:cmsbot_crab_20240325_223634', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 97, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213655:cmsbot_crab_20240325_223637', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213658:cmsbot_crab_rucio_transfers_20240325_223657', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213701:cmsbot_crab_rucio_transfers_group_20240325_223700', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213704:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240325_223702', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213707:cmsbot_crab_rucio_transfers_nopublication_20240325_223705', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213710:cmsbot_crab_rucio_transfers_withnoneedm_20240325_223709', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213713:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240325_223712', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-25T22:02:02Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-25 23:02:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/989/console

```
RETRY TESTS:
transferOutputs-check.sh 240325_213510:cmsbot_crab_transferOutputs - 2
activity-check.sh 240325_213514:cmsbot_crab_activity - 2
numCores-check.sh 240325_213529:cmsbot_crab_numCores - 2
scriptExe-check.sh 240325_213532:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240325_213534:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240325_213554:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240325_213556:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240325_213602:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240325_213604:cmsbot_crab_ignoreLocality - 2
whitelist-check.sh 240325_213608:cmsbot_crab_whitelist - 2
blacklist-check.sh 240325_213611:cmsbot_crab_blacklist - 2
voRole-check.sh 240325_213615:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferLogs-check.sh 240325_213512:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240325_213516:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240325_213518:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240325_213521:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240325_213523:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240325_213525:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240325_213527:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 240325_213536:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240325_213545:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240325_213548:cmsbot_crab_inputDBS - 0
useParent-check.sh 240325_213550:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240325_213552:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240325_213600:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240325_213606:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240325_213613:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240325_213617:cmsbot_crab_voGroup - 0
scheddName-check.sh 240325_213620:cmsbot_crab_scheddName - 0
collector-check.sh 240325_213622:cmsbot_crab_collector - 0
extraJDL-check.sh 240325_213624:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-25T22:17:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-25 23:17:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/836/console

```
{'TN': '240325_213626:cmsbot_crab_20240325_223626', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 989, 'running': 11}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213629:cmsbot_crab_20240325_223628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213631:cmsbot_crab_20240325_223630', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213633:cmsbot_crab_20240325_223632', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213635:cmsbot_crab_20240325_223634', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 98, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213655:cmsbot_crab_20240325_223637', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213658:cmsbot_crab_rucio_transfers_20240325_223657', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213701:cmsbot_crab_rucio_transfers_group_20240325_223700', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213704:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240325_223702', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213707:cmsbot_crab_rucio_transfers_nopublication_20240325_223705', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213710:cmsbot_crab_rucio_transfers_withnoneedm_20240325_223709', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213713:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240325_223712', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-25T22:27:04Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-03-25 23:27:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/990/console

```
RETRY TESTS:
blacklist-check.sh 240325_213611:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240325_213510:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240325_213512:cmsbot_crab_transferLogs - 0
activity-check.sh 240325_213514:cmsbot_crab_activity - 0
inputFiles-check.sh 240325_213516:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240325_213518:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240325_213521:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240325_213523:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240325_213525:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240325_213527:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240325_213529:cmsbot_crab_numCores - 0
scriptExe-check.sh 240325_213532:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240325_213534:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240325_213536:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240325_213545:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240325_213548:cmsbot_crab_inputDBS - 0
useParent-check.sh 240325_213550:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240325_213552:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240325_213554:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240325_213556:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240325_213600:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240325_213602:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240325_213604:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240325_213606:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240325_213608:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240325_213613:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240325_213615:cmsbot_crab_voRole - 0
voGroup-check.sh 240325_213617:cmsbot_crab_voGroup - 0
scheddName-check.sh 240325_213620:cmsbot_crab_scheddName - 0
collector-check.sh 240325_213622:cmsbot_crab_collector - 0
extraJDL-check.sh 240325_213624:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-25T22:51:08Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-03-25 23:51:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/991/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240325_213510:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240325_213512:cmsbot_crab_transferLogs - 0
activity-check.sh 240325_213514:cmsbot_crab_activity - 0
inputFiles-check.sh 240325_213516:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240325_213518:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240325_213521:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240325_213523:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240325_213525:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240325_213527:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240325_213529:cmsbot_crab_numCores - 0
scriptExe-check.sh 240325_213532:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240325_213534:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240325_213536:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240325_213545:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240325_213548:cmsbot_crab_inputDBS - 0
useParent-check.sh 240325_213550:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240325_213552:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240325_213554:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240325_213556:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240325_213600:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240325_213602:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240325_213604:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240325_213606:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240325_213608:cmsbot_crab_whitelist - 0
blacklist-check.sh 240325_213611:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240325_213613:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240325_213615:cmsbot_crab_voRole - 0
voGroup-check.sh 240325_213617:cmsbot_crab_voGroup - 0
scheddName-check.sh 240325_213620:cmsbot_crab_scheddName - 0
collector-check.sh 240325_213622:cmsbot_crab_collector - 0
extraJDL-check.sh 240325_213624:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-25T23:04:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-26 00:04:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/837/console

```
{'TN': '240325_213626:cmsbot_crab_20240325_223626', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 977, 'transferring': 23}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240325_213629:cmsbot_crab_20240325_223628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213631:cmsbot_crab_20240325_223630', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240325_213633:cmsbot_crab_20240325_223632', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240325_213635:cmsbot_crab_20240325_223634', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 97, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/96/96'}
{'TN': '240325_213655:cmsbot_crab_20240325_223637', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240325_213658:cmsbot_crab_rucio_transfers_20240325_223657', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/37'}
{'TN': '240325_213701:cmsbot_crab_rucio_transfers_group_20240325_223700', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '16/24/24'}
{'TN': '240325_213704:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240325_223702', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213707:cmsbot_crab_rucio_transfers_nopublication_20240325_223705', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213710:cmsbot_crab_rucio_transfers_withnoneedm_20240325_223709', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '19/20/20'}
{'TN': '240325_213713:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240325_223712', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T00:36:04Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-03-26 01:36:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/838/console

```
{'TN': '240325_213626:cmsbot_crab_20240325_223626', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240325_213629:cmsbot_crab_20240325_223628', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240325_213631:cmsbot_crab_20240325_223630', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240325_213633:cmsbot_crab_20240325_223632', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240325_213635:cmsbot_crab_20240325_223634', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240325_213655:cmsbot_crab_20240325_223637', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240325_213658:cmsbot_crab_rucio_transfers_20240325_223657', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/37'}
{'TN': '240325_213701:cmsbot_crab_rucio_transfers_group_20240325_223700', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '16/24/24'}
{'TN': '240325_213704:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240325_223702', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213707:cmsbot_crab_rucio_transfers_nopublication_20240325_223705', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240325_213710:cmsbot_crab_rucio_transfers_withnoneedm_20240325_223709', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '19/21/21'}
{'TN': '240325_213713:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240325_223712', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-03-26T08:21:33Z)

OK
