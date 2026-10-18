# dmwm/CRABServer issue #8417: #781: Test GH CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-16T18:33:31Z
Closed: 2024-05-24T13:48:22Z
URL: https://github.com/dmwm/CRABServer/issues/8417

## Opening post (cmsdmwmbot, 2024-05-16T18:33:31Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-05-16 20:33:29
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/781/)

## Comment (cmsdmwmbot, 2024-05-16T18:35:53Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240516_183502:cmsbot_crab_20240516_203501
240516_183504:cmsbot_crab_20240516_203503
240516_183506:cmsbot_crab_20240516_203505
240516_183507:cmsbot_crab_20240516_203507
240516_183509:cmsbot_crab_20240516_203509
240516_183513:cmsbot_crab_20240516_203511
240516_183516:cmsbot_crab_rucio_transfers_20240516_203514
240516_183518:cmsbot_crab_rucio_transfers_group_20240516_203518
240516_183522:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240516_203520
240516_183526:cmsbot_crab_rucio_transfers_nopublication_20240516_203524
240516_183529:cmsbot_crab_rucio_transfers_withnoneedm_20240516_203527
240516_183532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240516_203530
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240516_183356:cmsbot_crab_transferOutputs
240516_183358:cmsbot_crab_transferLogs
240516_183400:cmsbot_crab_activity
240516_183402:cmsbot_crab_inputFiles
240516_183404:cmsbot_crab_disableAutomaticOutputCollection
240516_183406:cmsbot_crab_outputFiles
240516_183408:cmsbot_crab_allowUndistributedCMSSW
240516_183410:cmsbot_crab_maxMemoryMB
240516_183412:cmsbot_crab_maxJobRuntimeMin
240516_183414:cmsbot_crab_numCores
240516_183417:cmsbot_crab_scriptExe
240516_183419:cmsbot_crab_scriptArgs
240516_183421:cmsbot_crab_sendVenvFolder
240516_183424:cmsbot_crab_sendExternalFolder
240516_183425:cmsbot_crab_inputDBS
240516_183428:cmsbot_crab_useParent
240516_183430:cmsbot_crab_secondaryInputDataset
240516_183432:cmsbot_crab_lumiMaskFile
240516_183434:cmsbot_crab_lumiMaskUrl
240516_183437:cmsbot_crab_outLFNDirBase
240516_183439:cmsbot_crab_runRange
240516_183441:cmsbot_crab_ignoreLocality
240516_183443:cmsbot_crab_userInputFiles
240516_183445:cmsbot_crab_whitelist
240516_183447:cmsbot_crab_blacklist
240516_183449:cmsbot_crab_ignoreGlobalBlacklist
240516_183451:cmsbot_crab_voRole
240516_183453:cmsbot_crab_voGroup
240516_183455:cmsbot_crab_scheddName
240516_183457:cmsbot_crab_collector
240516_183459:cmsbot_crab_extraJDL
```

Finished at: 2024-05-16 20:35:32
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/781/console)

## Comment (cmsdmwmbot, 2024-05-16T18:58:22Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-16 20:58:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/924/console

```
{'TN': '240516_183502:cmsbot_crab_20240516_203501', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 467, 'finished': 529, 'running': 2, 'idle': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183504:cmsbot_crab_20240516_203503', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183506:cmsbot_crab_20240516_203505', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183507:cmsbot_crab_20240516_203507', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 3, 'transferring': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183509:cmsbot_crab_20240516_203509', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183513:cmsbot_crab_20240516_203511', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183516:cmsbot_crab_rucio_transfers_20240516_203514', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183518:cmsbot_crab_rucio_transfers_group_20240516_203518', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183522:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240516_203520', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183526:cmsbot_crab_rucio_transfers_nopublication_20240516_203524', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183529:cmsbot_crab_rucio_transfers_withnoneedm_20240516_203527', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240516_203530', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-16T19:02:00Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-16 21:01:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1069/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 240516_183430:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240516_183434:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240516_183437:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240516_183439:cmsbot_crab_runRange - 2
whitelist-check.sh 240516_183445:cmsbot_crab_whitelist - 2
blacklist-check.sh 240516_183447:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240516_183356:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240516_183358:cmsbot_crab_transferLogs - 0
activity-check.sh 240516_183400:cmsbot_crab_activity - 0
inputFiles-check.sh 240516_183402:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240516_183404:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240516_183406:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240516_183408:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240516_183410:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240516_183412:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240516_183414:cmsbot_crab_numCores - 0
scriptExe-check.sh 240516_183417:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240516_183419:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240516_183421:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240516_183424:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240516_183425:cmsbot_crab_inputDBS - 0
useParent-check.sh 240516_183428:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 240516_183432:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240516_183441:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240516_183443:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240516_183449:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240516_183451:cmsbot_crab_voRole - 0
voGroup-check.sh 240516_183453:cmsbot_crab_voGroup - 0
scheddName-check.sh 240516_183455:cmsbot_crab_scheddName - 0
collector-check.sh 240516_183457:cmsbot_crab_collector - 0
extraJDL-check.sh 240516_183459:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-16T19:16:28Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-05-16 21:16:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/925/console

```
{'TN': '240516_183502:cmsbot_crab_20240516_203501', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 991, 'transferring': 7, 'running': 2}, 'publication (fail/tdb/DBS)': '0/500/500'}
{'TN': '240516_183504:cmsbot_crab_20240516_203503', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183506:cmsbot_crab_20240516_203505', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183507:cmsbot_crab_20240516_203507', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/3/3'}
{'TN': '240516_183509:cmsbot_crab_20240516_203509', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 98, 'idle': 1, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183513:cmsbot_crab_20240516_203511', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183516:cmsbot_crab_rucio_transfers_20240516_203514', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1, 'finished': 39}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183518:cmsbot_crab_rucio_transfers_group_20240516_203518', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 2, 'finished': 38}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183522:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240516_203520', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183526:cmsbot_crab_rucio_transfers_nopublication_20240516_203524', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183529:cmsbot_crab_rucio_transfers_withnoneedm_20240516_203527', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 2, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240516_203530', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-16T19:26:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-05-16 21:26:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1070/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240516_183434:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240516_183356:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240516_183358:cmsbot_crab_transferLogs - 0
activity-check.sh 240516_183400:cmsbot_crab_activity - 0
inputFiles-check.sh 240516_183402:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240516_183404:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240516_183406:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240516_183408:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240516_183410:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240516_183412:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240516_183414:cmsbot_crab_numCores - 0
scriptExe-check.sh 240516_183417:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240516_183419:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240516_183421:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240516_183424:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240516_183425:cmsbot_crab_inputDBS - 0
useParent-check.sh 240516_183428:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240516_183430:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240516_183432:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240516_183437:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240516_183439:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240516_183441:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240516_183443:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240516_183445:cmsbot_crab_whitelist - 0
blacklist-check.sh 240516_183447:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240516_183449:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240516_183451:cmsbot_crab_voRole - 0
voGroup-check.sh 240516_183453:cmsbot_crab_voGroup - 0
scheddName-check.sh 240516_183455:cmsbot_crab_scheddName - 0
collector-check.sh 240516_183457:cmsbot_crab_collector - 0
extraJDL-check.sh 240516_183459:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-16T19:52:18Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-05-16 21:52:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1071/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240516_183356:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240516_183358:cmsbot_crab_transferLogs - 0
activity-check.sh 240516_183400:cmsbot_crab_activity - 0
inputFiles-check.sh 240516_183402:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240516_183404:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240516_183406:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240516_183408:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240516_183410:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240516_183412:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240516_183414:cmsbot_crab_numCores - 0
scriptExe-check.sh 240516_183417:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240516_183419:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240516_183421:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240516_183424:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240516_183425:cmsbot_crab_inputDBS - 0
useParent-check.sh 240516_183428:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240516_183430:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240516_183432:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240516_183434:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240516_183437:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240516_183439:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240516_183441:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240516_183443:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240516_183445:cmsbot_crab_whitelist - 0
blacklist-check.sh 240516_183447:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240516_183449:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240516_183451:cmsbot_crab_voRole - 0
voGroup-check.sh 240516_183453:cmsbot_crab_voGroup - 0
scheddName-check.sh 240516_183455:cmsbot_crab_scheddName - 0
collector-check.sh 240516_183457:cmsbot_crab_collector - 0
extraJDL-check.sh 240516_183459:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-16T20:03:22Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-05-16 22:03:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/926/console

```
{'TN': '240516_183502:cmsbot_crab_20240516_203501', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240516_183504:cmsbot_crab_20240516_203503', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183506:cmsbot_crab_20240516_203505', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240516_183507:cmsbot_crab_20240516_203507', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240516_183509:cmsbot_crab_20240516_203509', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/99/99'}
{'TN': '240516_183513:cmsbot_crab_20240516_203511', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240516_183516:cmsbot_crab_rucio_transfers_20240516_203514', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240516_183518:cmsbot_crab_rucio_transfers_group_20240516_203518', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240516_183522:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240516_203520', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183526:cmsbot_crab_rucio_transfers_nopublication_20240516_203524', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183529:cmsbot_crab_rucio_transfers_withnoneedm_20240516_203527', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240516_183532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240516_203530', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-16T21:35:22Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-05-16 23:35:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/927/console

```
{'TN': '240516_183502:cmsbot_crab_20240516_203501', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240516_183504:cmsbot_crab_20240516_203503', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240516_183506:cmsbot_crab_20240516_203505', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240516_183507:cmsbot_crab_20240516_203507', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240516_183509:cmsbot_crab_20240516_203509', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240516_183513:cmsbot_crab_20240516_203511', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240516_183516:cmsbot_crab_rucio_transfers_20240516_203514', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240516_183518:cmsbot_crab_rucio_transfers_group_20240516_203518', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240516_183522:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240516_203520', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183526:cmsbot_crab_rucio_transfers_nopublication_20240516_203524', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183529:cmsbot_crab_rucio_transfers_withnoneedm_20240516_203527', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240516_183532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240516_203530', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-16T23:38:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-05-17 01:38:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/928/console

```
{'TN': '240516_183502:cmsbot_crab_20240516_203501', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240516_183504:cmsbot_crab_20240516_203503', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240516_183506:cmsbot_crab_20240516_203505', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240516_183507:cmsbot_crab_20240516_203507', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240516_183509:cmsbot_crab_20240516_203509', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240516_183513:cmsbot_crab_20240516_203511', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240516_183516:cmsbot_crab_rucio_transfers_20240516_203514', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240516_183518:cmsbot_crab_rucio_transfers_group_20240516_203518', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240516_183522:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240516_203520', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183526:cmsbot_crab_rucio_transfers_nopublication_20240516_203524', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183529:cmsbot_crab_rucio_transfers_withnoneedm_20240516_203527', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240516_183532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240516_203530', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-17T01:40:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-05-17 03:40:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/929/console

```
{'TN': '240516_183502:cmsbot_crab_20240516_203501', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240516_183504:cmsbot_crab_20240516_203503', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240516_183506:cmsbot_crab_20240516_203505', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240516_183507:cmsbot_crab_20240516_203507', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240516_183509:cmsbot_crab_20240516_203509', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240516_183513:cmsbot_crab_20240516_203511', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240516_183516:cmsbot_crab_rucio_transfers_20240516_203514', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240516_183518:cmsbot_crab_rucio_transfers_group_20240516_203518', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240516_183522:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240516_203520', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183526:cmsbot_crab_rucio_transfers_nopublication_20240516_203524', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240516_183529:cmsbot_crab_rucio_transfers_withnoneedm_20240516_203527', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240516_183532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240516_203530', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-05-20T17:59:04Z)

the task `240516_183518:cmsbot_crab_rucio_transfers_group_20240516_203518`
still has one file which Rucio is trying to transfer from GRIF to Legnaro
https://cms-rucio-webui.cern.ch/rule?rule_id=b5ff5f91516142fbb852d3b9c978d741#locks

FTS errors are obscure, e.g.  https://fts-cms-001.cern.ch:8449/var/log/fts3/transfers/2024-05-20/eos.grif.fr__t2-xrdcms.lnl.infn.it/2024-05-20-1623__eos.grif.fr__t2-xrdcms.lnl.infn.it__4231830030__44fc174e-16c5-11ef-b0b4-fa163e9e00e6
```
[....]
INFO    Mon, 20 May 2024 18:23:20 +0200; Davix: > User-Agent: libdavix/0.8.6.1.eddf9a5 libcurl/7.76.1
INFO    Mon, 20 May 2024 18:23:20 +0200; Davix: 
INFO    Mon, 20 May 2024 18:23:20 +0200; Davix: < HTTP/1.1 404 Not Found
INFO    Mon, 20 May 2024 18:23:20 +0200; Davix: < Date: Mon, 20 May 2024 16:23:20 GMT
INFO    Mon, 20 May 2024 18:23:20 +0200; Davix: < Server: dCache/8.2.33
INFO    Mon, 20 May 2024 18:23:20 +0200; Davix: < Content-Type: text/plain;charset=utf-8
INFO    Mon, 20 May 2024 18:23:20 +0200; Davix: < Content-Length: 169
INFO    Mon, 20 May 2024 18:23:20 +0200; Davix: Negative result for operation: HTTP 404 : File not found . After 1 retry
INFO    Mon, 20 May 2024 18:23:20 +0200; [1716222200830] DEST http_plugin	CLEANUP	0
INFO    Mon, 20 May 2024 18:23:20 +0200; Gfal2: Event triggered: DESTINATION http_plugin CLEANUP 0
INFO    Mon, 20 May 2024 18:23:20 +0200; [1716222200830] BOTH http_plugin	TRANSFER:EXIT	ERROR: Copy failed (3rd pull, 3rd push). Last attempt: Transfer failure: Peer certificate cannot be authenticated with given CA certificates
INFO    Mon, 20 May 2024 18:23:20 +0200; Gfal2: Event triggered: BOTH http_plugin TRANSFER:EXIT ERROR: Copy failed (3rd pull, 3rd push). Last attempt: Transfer failure: Peer certificate cannot be authenticated with given CA certificates
ERR     Mon, 20 May 2024 18:23:20 +0200; Recoverable error: [5] TRANSFER ERROR: Copy failed (3rd pull, 3rd push). Last attempt: Transfer failure: Peer certificate cannot be authenticated with given CA certificates
INFO    Mon, 20 May 2024 18:23:20 +0200; Finishing copy process...
```

## Comment (belforte, 2024-05-24T13:48:22Z)

everything cleared and understood
