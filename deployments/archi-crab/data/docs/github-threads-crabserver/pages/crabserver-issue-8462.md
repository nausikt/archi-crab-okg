# dmwm/CRABServer issue #8462: #792: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-03T10:53:10Z
Closed: 2024-06-12T10:19:28Z
URL: https://github.com/dmwm/CRABServer/issues/8462

## Opening post (cmsdmwmbot, 2024-06-03T10:53:10Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-06-03 12:53:09
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/792/)

## Comment (cmsdmwmbot, 2024-06-03T10:55:28Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240603_105434:cmsbot_crab_20240603_125433
240603_105436:cmsbot_crab_20240603_125435
240603_105438:cmsbot_crab_20240603_125438
240603_105441:cmsbot_crab_20240603_125440
240603_105443:cmsbot_crab_20240603_125442
240603_105447:cmsbot_crab_20240603_125444
240603_105450:cmsbot_crab_rucio_transfers_20240603_125448
240603_105452:cmsbot_crab_rucio_transfers_group_20240603_125451
240603_105456:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240603_125454
240603_105459:cmsbot_crab_rucio_transfers_nopublication_20240603_125457
240603_105502:cmsbot_crab_rucio_transfers_withnoneedm_20240603_125501
240603_105506:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240603_125504
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240603_105329:cmsbot_crab_transferOutputs
240603_105331:cmsbot_crab_transferLogs
240603_105333:cmsbot_crab_activity
240603_105335:cmsbot_crab_inputFiles
240603_105337:cmsbot_crab_disableAutomaticOutputCollection
240603_105339:cmsbot_crab_outputFiles
240603_105341:cmsbot_crab_allowUndistributedCMSSW
240603_105343:cmsbot_crab_maxMemoryMB
240603_105345:cmsbot_crab_maxJobRuntimeMin
240603_105347:cmsbot_crab_numCores
240603_105349:cmsbot_crab_scriptExe
240603_105351:cmsbot_crab_scriptArgs
240603_105353:cmsbot_crab_sendVenvFolder
240603_105356:cmsbot_crab_sendExternalFolder
240603_105358:cmsbot_crab_inputDBS
240603_105400:cmsbot_crab_useParent
240603_105402:cmsbot_crab_secondaryInputDataset
240603_105404:cmsbot_crab_lumiMaskFile
240603_105406:cmsbot_crab_lumiMaskUrl
240603_105409:cmsbot_crab_outLFNDirBase
240603_105411:cmsbot_crab_runRange
240603_105413:cmsbot_crab_ignoreLocality
240603_105415:cmsbot_crab_userInputFiles
240603_105417:cmsbot_crab_whitelist
240603_105419:cmsbot_crab_blacklist
240603_105421:cmsbot_crab_ignoreGlobalBlacklist
240603_105423:cmsbot_crab_voRole
240603_105425:cmsbot_crab_voGroup
240603_105427:cmsbot_crab_scheddName
240603_105429:cmsbot_crab_collector
240603_105431:cmsbot_crab_extraJDL
```

Finished at: 2024-06-03 12:55:07
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/792/console)

## Comment (cmsdmwmbot, 2024-06-03T11:17:50Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-03 13:17:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/952/console

```
{'TN': '240603_105434:cmsbot_crab_20240603_125433', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105436:cmsbot_crab_20240603_125435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105438:cmsbot_crab_20240603_125438', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105441:cmsbot_crab_20240603_125440', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105443:cmsbot_crab_20240603_125442', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105447:cmsbot_crab_20240603_125444', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 8, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105450:cmsbot_crab_rucio_transfers_20240603_125448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105452:cmsbot_crab_rucio_transfers_group_20240603_125451', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105456:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240603_125454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105459:cmsbot_crab_rucio_transfers_nopublication_20240603_125457', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105502:cmsbot_crab_rucio_transfers_withnoneedm_20240603_125501', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105506:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240603_125504', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T11:20:22Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-03 13:20:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1089/console

```
RETRY TESTS:
transferLogs-check.sh 240603_105331:cmsbot_crab_transferLogs - 2
activity-check.sh 240603_105333:cmsbot_crab_activity - 2
outputFiles-check.sh 240603_105339:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240603_105343:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240603_105345:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240603_105347:cmsbot_crab_numCores - 2
scriptExe-check.sh 240603_105349:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240603_105351:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240603_105400:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240603_105402:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240603_105404:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240603_105406:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240603_105409:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240603_105411:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240603_105415:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240603_105417:cmsbot_crab_whitelist - 2
blacklist-check.sh 240603_105419:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240603_105421:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240603_105423:cmsbot_crab_voRole - 2
voGroup-check.sh 240603_105425:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_105329:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240603_105335:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_105337:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240603_105341:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240603_105353:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_105356:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_105358:cmsbot_crab_inputDBS - 0
ignoreLocality-check.sh 240603_105413:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 240603_105427:cmsbot_crab_scheddName - 0
collector-check.sh 240603_105429:cmsbot_crab_collector - 0
extraJDL-check.sh 240603_105431:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-03T11:34:49Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-03 13:34:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/953/console

```
{'TN': '240603_105434:cmsbot_crab_20240603_125433', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105436:cmsbot_crab_20240603_125435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105438:cmsbot_crab_20240603_125438', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105441:cmsbot_crab_20240603_125440', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105443:cmsbot_crab_20240603_125442', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105447:cmsbot_crab_20240603_125444', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105450:cmsbot_crab_rucio_transfers_20240603_125448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 33, 'finished': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105452:cmsbot_crab_rucio_transfers_group_20240603_125451', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 34, 'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105456:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240603_125454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105459:cmsbot_crab_rucio_transfers_nopublication_20240603_125457', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105502:cmsbot_crab_rucio_transfers_withnoneedm_20240603_125501', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 18, 'transferring': 22}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105506:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240603_125504', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T11:45:11Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-06-03 13:45:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1090/console

```
RETRY TESTS:
blacklist-check.sh 240603_105419:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_105329:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_105331:cmsbot_crab_transferLogs - 0
activity-check.sh 240603_105333:cmsbot_crab_activity - 0
inputFiles-check.sh 240603_105335:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_105337:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240603_105339:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240603_105341:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240603_105343:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240603_105345:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240603_105349:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240603_105351:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240603_105353:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_105356:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_105358:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_105400:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_105402:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240603_105404:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240603_105406:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240603_105409:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240603_105411:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240603_105413:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_105415:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240603_105417:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240603_105421:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_105423:cmsbot_crab_voRole - 0
voGroup-check.sh 240603_105425:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_105427:cmsbot_crab_scheddName - 0
collector-check.sh 240603_105429:cmsbot_crab_collector - 0
extraJDL-check.sh 240603_105431:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 240603_105347:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-06-03T12:10:07Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-03 14:10:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1091/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_105329:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_105331:cmsbot_crab_transferLogs - 0
activity-check.sh 240603_105333:cmsbot_crab_activity - 0
inputFiles-check.sh 240603_105335:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_105337:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240603_105339:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240603_105341:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240603_105343:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240603_105345:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240603_105349:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240603_105351:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240603_105353:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_105356:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_105358:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_105400:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_105402:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240603_105404:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240603_105406:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240603_105409:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240603_105411:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240603_105413:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_105415:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240603_105417:cmsbot_crab_whitelist - 0
blacklist-check.sh 240603_105419:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240603_105421:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_105423:cmsbot_crab_voRole - 0
voGroup-check.sh 240603_105425:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_105427:cmsbot_crab_scheddName - 0
collector-check.sh 240603_105429:cmsbot_crab_collector - 0
extraJDL-check.sh 240603_105431:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 240603_105347:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-06-03T12:22:52Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-03 14:22:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/954/console

```
{'TN': '240603_105434:cmsbot_crab_20240603_125433', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240603_105436:cmsbot_crab_20240603_125435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105438:cmsbot_crab_20240603_125438', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_105441:cmsbot_crab_20240603_125440', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_105443:cmsbot_crab_20240603_125442', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_105447:cmsbot_crab_20240603_125444', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_105450:cmsbot_crab_rucio_transfers_20240603_125448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240603_105452:cmsbot_crab_rucio_transfers_group_20240603_125451', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105456:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240603_125454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105459:cmsbot_crab_rucio_transfers_nopublication_20240603_125457', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105502:cmsbot_crab_rucio_transfers_withnoneedm_20240603_125501', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '240603_105506:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240603_125504', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T13:53:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-06-03 15:53:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/955/console

```
{'TN': '240603_105434:cmsbot_crab_20240603_125433', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240603_105436:cmsbot_crab_20240603_125435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105438:cmsbot_crab_20240603_125438', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_105441:cmsbot_crab_20240603_125440', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_105443:cmsbot_crab_20240603_125442', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_105447:cmsbot_crab_20240603_125444', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_105450:cmsbot_crab_rucio_transfers_20240603_125448', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105452:cmsbot_crab_rucio_transfers_group_20240603_125451', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105456:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240603_125454', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105459:cmsbot_crab_rucio_transfers_nopublication_20240603_125457', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105502:cmsbot_crab_rucio_transfers_withnoneedm_20240603_125501', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105506:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240603_125504', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T15:55:51Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-06-03 17:55:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/956/console

```
{'TN': '240603_105434:cmsbot_crab_20240603_125433', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240603_105436:cmsbot_crab_20240603_125435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105438:cmsbot_crab_20240603_125438', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_105441:cmsbot_crab_20240603_125440', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_105443:cmsbot_crab_20240603_125442', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_105447:cmsbot_crab_20240603_125444', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_105450:cmsbot_crab_rucio_transfers_20240603_125448', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105452:cmsbot_crab_rucio_transfers_group_20240603_125451', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105456:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240603_125454', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105459:cmsbot_crab_rucio_transfers_nopublication_20240603_125457', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105502:cmsbot_crab_rucio_transfers_withnoneedm_20240603_125501', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105506:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240603_125504', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T17:59:52Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-03 19:59:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/957/console

```
{'TN': '240603_105434:cmsbot_crab_20240603_125433', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240603_105436:cmsbot_crab_20240603_125435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105438:cmsbot_crab_20240603_125438', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_105441:cmsbot_crab_20240603_125440', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_105443:cmsbot_crab_20240603_125442', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_105447:cmsbot_crab_20240603_125444', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_105450:cmsbot_crab_rucio_transfers_20240603_125448', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105452:cmsbot_crab_rucio_transfers_group_20240603_125451', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105456:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240603_125454', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105459:cmsbot_crab_rucio_transfers_nopublication_20240603_125457', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_105502:cmsbot_crab_rucio_transfers_withnoneedm_20240603_125501', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_105506:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240603_125504', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-12T10:19:28Z)

now fixed
