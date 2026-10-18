# dmwm/CRABServer issue #8501: #806: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-16T21:04:43Z
Closed: 2024-08-01T15:06:05Z
URL: https://github.com/dmwm/CRABServer/issues/8501

## Opening post (cmsdmwmbot, 2024-06-16T21:04:43Z)

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

Started at: 2024-06-16 23:04:42
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/806/)

## Comment (cmsdmwmbot, 2024-06-16T21:07:10Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240616_210622:cmsbot_crab_20240616_230622
240616_210624:cmsbot_crab_20240616_230624
240616_210626:cmsbot_crab_20240616_230626
240616_210628:cmsbot_crab_20240616_230628
240616_210630:cmsbot_crab_20240616_230630
240616_210634:cmsbot_crab_20240616_230632
240616_210636:cmsbot_crab_rucio_transfers_20240616_230635
240616_210638:cmsbot_crab_rucio_transfers_group_20240616_230638
240616_210641:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240616_230640
240616_210643:cmsbot_crab_rucio_transfers_nopublication_20240616_230642
240616_210646:cmsbot_crab_rucio_transfers_withnoneedm_20240616_230645
240616_210649:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240616_230647
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240616_210518:cmsbot_crab_transferOutputs
240616_210520:cmsbot_crab_transferLogs
240616_210522:cmsbot_crab_activity
240616_210524:cmsbot_crab_inputFiles
240616_210526:cmsbot_crab_disableAutomaticOutputCollection
240616_210528:cmsbot_crab_outputFiles
240616_210530:cmsbot_crab_allowUndistributedCMSSW
240616_210532:cmsbot_crab_maxMemoryMB
240616_210534:cmsbot_crab_maxJobRuntimeMin
240616_210536:cmsbot_crab_numCores
240616_210538:cmsbot_crab_scriptExe
240616_210540:cmsbot_crab_scriptArgs
240616_210542:cmsbot_crab_sendVenvFolder
240616_210544:cmsbot_crab_sendExternalFolder
240616_210546:cmsbot_crab_inputDBS
240616_210548:cmsbot_crab_useParent
240616_210550:cmsbot_crab_secondaryInputDataset
240616_210552:cmsbot_crab_lumiMaskFile
240616_210554:cmsbot_crab_lumiMaskUrl
240616_210557:cmsbot_crab_outLFNDirBase
240616_210559:cmsbot_crab_runRange
240616_210601:cmsbot_crab_ignoreLocality
240616_210603:cmsbot_crab_userInputFiles
240616_210605:cmsbot_crab_whitelist
240616_210607:cmsbot_crab_blacklist
240616_210609:cmsbot_crab_ignoreGlobalBlacklist
240616_210612:cmsbot_crab_voRole
240616_210614:cmsbot_crab_voGroup
240616_210616:cmsbot_crab_scheddName
240616_210618:cmsbot_crab_collector
240616_210620:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240616_210503:cmsbot_crab_20240616_230502
```

Finished at: 2024-06-16 23:06:49
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/806/console)

## Comment (cmsdmwmbot, 2024-06-16T21:28:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-16 23:28:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/996/console

```
{'TN': '240616_210622:cmsbot_crab_20240616_230622', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210624:cmsbot_crab_20240616_230624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210626:cmsbot_crab_20240616_230626', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210628:cmsbot_crab_20240616_230628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210630:cmsbot_crab_20240616_230630', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210634:cmsbot_crab_20240616_230632', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210636:cmsbot_crab_rucio_transfers_20240616_230635', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210638:cmsbot_crab_rucio_transfers_group_20240616_230638', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210641:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240616_230640', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210643:cmsbot_crab_rucio_transfers_nopublication_20240616_230642', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210646:cmsbot_crab_rucio_transfers_withnoneedm_20240616_230645', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210649:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240616_230647', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-16T21:30:41Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-06-16 23:30:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/542/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/542//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-06-16T21:32:35Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-16 23:32:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1123/console

```
RETRY TESTS:
transferLogs-check.sh 240616_210520:cmsbot_crab_transferLogs - 2
activity-check.sh 240616_210522:cmsbot_crab_activity - 2
outputFiles-check.sh 240616_210528:cmsbot_crab_outputFiles - 2
lumiMaskFile-check.sh 240616_210552:cmsbot_crab_lumiMaskFile - 2
outLFNDirBase-check.sh 240616_210557:cmsbot_crab_outLFNDirBase - 2
userInputFiles-check.sh 240616_210603:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240616_210605:cmsbot_crab_whitelist - 2
blacklist-check.sh 240616_210607:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240616_210609:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240616_210518:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240616_210524:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240616_210526:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240616_210530:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240616_210532:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240616_210534:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240616_210536:cmsbot_crab_numCores - 0
scriptExe-check.sh 240616_210538:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240616_210540:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240616_210542:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240616_210544:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240616_210546:cmsbot_crab_inputDBS - 0
useParent-check.sh 240616_210548:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240616_210550:cmsbot_crab_secondaryInputDataset - 0
voRole-check.sh 240616_210612:cmsbot_crab_voRole - 0
voGroup-check.sh 240616_210614:cmsbot_crab_voGroup - 0
scheddName-check.sh 240616_210616:cmsbot_crab_scheddName - 0
collector-check.sh 240616_210618:cmsbot_crab_collector - 0
extraJDL-check.sh 240616_210620:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240616_210554:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 240616_210559:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240616_210601:cmsbot_crab_ignoreLocality - 1
```

## Comment (cmsdmwmbot, 2024-06-16T21:46:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-16 23:46:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/997/console

```
{'TN': '240616_210622:cmsbot_crab_20240616_230622', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210624:cmsbot_crab_20240616_230624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210626:cmsbot_crab_20240616_230626', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210628:cmsbot_crab_20240616_230628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210630:cmsbot_crab_20240616_230630', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 95, 'transferring': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210634:cmsbot_crab_20240616_230632', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210636:cmsbot_crab_rucio_transfers_20240616_230635', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210638:cmsbot_crab_rucio_transfers_group_20240616_230638', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210641:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240616_230640', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210643:cmsbot_crab_rucio_transfers_nopublication_20240616_230642', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210646:cmsbot_crab_rucio_transfers_withnoneedm_20240616_230645', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210649:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240616_230647', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-16T21:57:00Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-16 23:56:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1124/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240616_210518:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240616_210520:cmsbot_crab_transferLogs - 0
activity-check.sh 240616_210522:cmsbot_crab_activity - 0
inputFiles-check.sh 240616_210524:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240616_210526:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240616_210528:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240616_210530:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240616_210532:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240616_210534:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240616_210536:cmsbot_crab_numCores - 0
scriptExe-check.sh 240616_210538:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240616_210540:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240616_210542:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240616_210544:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240616_210546:cmsbot_crab_inputDBS - 0
useParent-check.sh 240616_210548:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240616_210550:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240616_210552:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240616_210557:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240616_210603:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240616_210605:cmsbot_crab_whitelist - 0
blacklist-check.sh 240616_210607:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240616_210609:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240616_210612:cmsbot_crab_voRole - 0
voGroup-check.sh 240616_210614:cmsbot_crab_voGroup - 0
scheddName-check.sh 240616_210616:cmsbot_crab_scheddName - 0
collector-check.sh 240616_210618:cmsbot_crab_collector - 0
extraJDL-check.sh 240616_210620:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240616_210554:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 240616_210559:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240616_210601:cmsbot_crab_ignoreLocality - 1
```

## Comment (cmsdmwmbot, 2024-06-16T22:32:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-17 00:32:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/998/console

```
{'TN': '240616_210622:cmsbot_crab_20240616_230622', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240616_210624:cmsbot_crab_20240616_230624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210626:cmsbot_crab_20240616_230626', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240616_210628:cmsbot_crab_20240616_230628', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240616_210630:cmsbot_crab_20240616_230630', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240616_210634:cmsbot_crab_20240616_230632', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240616_210636:cmsbot_crab_rucio_transfers_20240616_230635', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240616_210638:cmsbot_crab_rucio_transfers_group_20240616_230638', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '2/38/38'}
{'TN': '240616_210641:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240616_230640', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210643:cmsbot_crab_rucio_transfers_nopublication_20240616_230642', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210646:cmsbot_crab_rucio_transfers_withnoneedm_20240616_230645', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '2/38/38'}
{'TN': '240616_210649:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240616_230647', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-17T00:05:33Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 3 out of 5. Test failed. Investigate manually
**Finished at:** 2024-06-17 02:05:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/999/console

```
{'TN': '240616_210622:cmsbot_crab_20240616_230622', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240616_210624:cmsbot_crab_20240616_230624', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240616_210626:cmsbot_crab_20240616_230626', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240616_210628:cmsbot_crab_20240616_230628', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240616_210630:cmsbot_crab_20240616_230630', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240616_210634:cmsbot_crab_20240616_230632', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240616_210636:cmsbot_crab_rucio_transfers_20240616_230635', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240616_210638:cmsbot_crab_rucio_transfers_group_20240616_230638', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '2/38/38'}
{'TN': '240616_210641:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240616_230640', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210643:cmsbot_crab_rucio_transfers_nopublication_20240616_230642', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240616_210646:cmsbot_crab_rucio_transfers_withnoneedm_20240616_230645', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '2/38/38'}
{'TN': '240616_210649:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240616_230647', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-17T06:37:05Z)

CCV failures are the "new normal" of dCache at DESY

## Comment (belforte, 2024-06-17T09:45:18Z)

the publication failures in ST are due to known https://github.com/dmwm/CRABServer/issues/8376

conclusion: all OK
