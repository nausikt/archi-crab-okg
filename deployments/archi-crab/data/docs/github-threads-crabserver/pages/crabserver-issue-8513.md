# dmwm/CRABServer issue #8513: #809: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-18T22:04:42Z
Closed: 2024-06-19T09:55:14Z
URL: https://github.com/dmwm/CRABServer/issues/8513

## Opening post (cmsdmwmbot, 2024-06-18T22:04:42Z)

**Test master TW after PR #8512**

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-06-19 00:04:41
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/809/)

## Comment (cmsdmwmbot, 2024-06-18T22:06:53Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240618_220605:cmsbot_crab_20240619_000604
240618_220607:cmsbot_crab_20240619_000606
240618_220609:cmsbot_crab_20240619_000608
240618_220611:cmsbot_crab_20240619_000610
240618_220613:cmsbot_crab_20240619_000612
240618_220616:cmsbot_crab_20240619_000614
240618_220619:cmsbot_crab_rucio_transfers_20240619_000618
240618_220621:cmsbot_crab_rucio_transfers_group_20240619_000621
240618_220624:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_000623
240618_220626:cmsbot_crab_rucio_transfers_nopublication_20240619_000625
240618_220629:cmsbot_crab_rucio_transfers_withnoneedm_20240619_000628
240618_220632:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_000631
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240618_220500:cmsbot_crab_transferOutputs
240618_220503:cmsbot_crab_transferLogs
240618_220505:cmsbot_crab_activity
240618_220507:cmsbot_crab_inputFiles
240618_220509:cmsbot_crab_disableAutomaticOutputCollection
240618_220511:cmsbot_crab_outputFiles
240618_220513:cmsbot_crab_allowUndistributedCMSSW
240618_220515:cmsbot_crab_maxMemoryMB
240618_220517:cmsbot_crab_maxJobRuntimeMin
240618_220519:cmsbot_crab_numCores
240618_220521:cmsbot_crab_scriptExe
240618_220523:cmsbot_crab_scriptArgs
240618_220525:cmsbot_crab_sendVenvFolder
240618_220527:cmsbot_crab_sendExternalFolder
240618_220529:cmsbot_crab_inputDBS
240618_220531:cmsbot_crab_useParent
240618_220533:cmsbot_crab_secondaryInputDataset
240618_220535:cmsbot_crab_lumiMaskFile
240618_220538:cmsbot_crab_lumiMaskUrl
240618_220540:cmsbot_crab_outLFNDirBase
240618_220542:cmsbot_crab_runRange
240618_220544:cmsbot_crab_ignoreLocality
240618_220546:cmsbot_crab_userInputFiles
240618_220548:cmsbot_crab_whitelist
240618_220550:cmsbot_crab_blacklist
240618_220552:cmsbot_crab_ignoreGlobalBlacklist
240618_220554:cmsbot_crab_voRole
240618_220556:cmsbot_crab_voGroup
240618_220558:cmsbot_crab_scheddName
240618_220600:cmsbot_crab_collector
240618_220602:cmsbot_crab_extraJDL
```

Finished at: 2024-06-19 00:06:32
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/809/console)

## Comment (cmsdmwmbot, 2024-06-18T22:27:55Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-19 00:27:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1012/console

```
{'TN': '240618_220605:cmsbot_crab_20240619_000604', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 997, 'unsubmitted': 2, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220607:cmsbot_crab_20240619_000606', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220609:cmsbot_crab_20240619_000608', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220611:cmsbot_crab_20240619_000610', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220613:cmsbot_crab_20240619_000612', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220616:cmsbot_crab_20240619_000614', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220619:cmsbot_crab_rucio_transfers_20240619_000618', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220621:cmsbot_crab_rucio_transfers_group_20240619_000621', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220624:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_000623', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220626:cmsbot_crab_rucio_transfers_nopublication_20240619_000625', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220629:cmsbot_crab_rucio_transfers_withnoneedm_20240619_000628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220632:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_000631', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-18T22:30:36Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-19 00:30:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1129/console

```
RETRY TESTS:
useParent-check.sh 240618_220531:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 240618_220538:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240618_220542:cmsbot_crab_runRange - 2
whitelist-check.sh 240618_220548:cmsbot_crab_whitelist - 2
blacklist-check.sh 240618_220550:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240618_220500:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240618_220503:cmsbot_crab_transferLogs - 0
activity-check.sh 240618_220505:cmsbot_crab_activity - 0
inputFiles-check.sh 240618_220507:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240618_220509:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240618_220511:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240618_220513:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240618_220515:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240618_220517:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240618_220519:cmsbot_crab_numCores - 0
scriptExe-check.sh 240618_220521:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240618_220523:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240618_220525:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240618_220527:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240618_220529:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240618_220533:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240618_220535:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240618_220540:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240618_220544:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240618_220546:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240618_220552:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240618_220554:cmsbot_crab_voRole - 0
voGroup-check.sh 240618_220556:cmsbot_crab_voGroup - 0
scheddName-check.sh 240618_220558:cmsbot_crab_scheddName - 0
collector-check.sh 240618_220600:cmsbot_crab_collector - 0
extraJDL-check.sh 240618_220602:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-18T22:43:51Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-19 00:43:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1013/console

```
{'TN': '240618_220605:cmsbot_crab_20240619_000604', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 997, 'idle': 2, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220607:cmsbot_crab_20240619_000606', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220609:cmsbot_crab_20240619_000608', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220611:cmsbot_crab_20240619_000610', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220613:cmsbot_crab_20240619_000612', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220616:cmsbot_crab_20240619_000614', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220619:cmsbot_crab_rucio_transfers_20240619_000618', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220621:cmsbot_crab_rucio_transfers_group_20240619_000621', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220624:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_000623', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220626:cmsbot_crab_rucio_transfers_nopublication_20240619_000625', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220629:cmsbot_crab_rucio_transfers_withnoneedm_20240619_000628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220632:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_000631', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-18T22:54:17Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-06-19 00:54:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1130/console

```
RETRY TESTS:
runRange-check.sh 240618_220542:cmsbot_crab_runRange - 2
whitelist-check.sh 240618_220548:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240618_220500:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240618_220503:cmsbot_crab_transferLogs - 0
activity-check.sh 240618_220505:cmsbot_crab_activity - 0
inputFiles-check.sh 240618_220507:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240618_220509:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240618_220511:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240618_220513:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240618_220515:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240618_220517:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240618_220519:cmsbot_crab_numCores - 0
scriptExe-check.sh 240618_220521:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240618_220523:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240618_220525:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240618_220527:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240618_220529:cmsbot_crab_inputDBS - 0
useParent-check.sh 240618_220531:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240618_220533:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240618_220535:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240618_220538:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240618_220540:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240618_220544:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240618_220546:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240618_220550:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240618_220552:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240618_220554:cmsbot_crab_voRole - 0
voGroup-check.sh 240618_220556:cmsbot_crab_voGroup - 0
scheddName-check.sh 240618_220558:cmsbot_crab_scheddName - 0
collector-check.sh 240618_220600:cmsbot_crab_collector - 0
extraJDL-check.sh 240618_220602:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-18T23:18:04Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-06-19 01:18:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1131/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240618_220500:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240618_220503:cmsbot_crab_transferLogs - 0
activity-check.sh 240618_220505:cmsbot_crab_activity - 0
inputFiles-check.sh 240618_220507:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240618_220509:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240618_220511:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240618_220513:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240618_220515:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240618_220517:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240618_220519:cmsbot_crab_numCores - 0
scriptExe-check.sh 240618_220521:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240618_220523:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240618_220525:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240618_220527:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240618_220529:cmsbot_crab_inputDBS - 0
useParent-check.sh 240618_220531:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240618_220533:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240618_220535:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240618_220538:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240618_220540:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240618_220542:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240618_220544:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240618_220546:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240618_220548:cmsbot_crab_whitelist - 0
blacklist-check.sh 240618_220550:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240618_220552:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240618_220554:cmsbot_crab_voRole - 0
voGroup-check.sh 240618_220556:cmsbot_crab_voGroup - 0
scheddName-check.sh 240618_220558:cmsbot_crab_scheddName - 0
collector-check.sh 240618_220600:cmsbot_crab_collector - 0
extraJDL-check.sh 240618_220602:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-18T23:29:48Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-19 01:29:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1014/console

```
{'TN': '240618_220605:cmsbot_crab_20240619_000604', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240618_220607:cmsbot_crab_20240619_000606', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220609:cmsbot_crab_20240619_000608', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240618_220611:cmsbot_crab_20240619_000610', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_220613:cmsbot_crab_20240619_000612', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240618_220616:cmsbot_crab_20240619_000614', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_220619:cmsbot_crab_rucio_transfers_20240619_000618', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_220621:cmsbot_crab_rucio_transfers_group_20240619_000621', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_220624:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_000623', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220626:cmsbot_crab_rucio_transfers_nopublication_20240619_000625', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220629:cmsbot_crab_rucio_transfers_withnoneedm_20240619_000628', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_220632:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_000631', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-19T01:01:23Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-06-19 03:01:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1015/console

```
{'TN': '240618_220605:cmsbot_crab_20240619_000604', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240618_220607:cmsbot_crab_20240619_000606', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240618_220609:cmsbot_crab_20240619_000608', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240618_220611:cmsbot_crab_20240619_000610', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_220613:cmsbot_crab_20240619_000612', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240618_220616:cmsbot_crab_20240619_000614', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_220619:cmsbot_crab_rucio_transfers_20240619_000618', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_220621:cmsbot_crab_rucio_transfers_group_20240619_000621', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_220624:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_000623', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220626:cmsbot_crab_rucio_transfers_nopublication_20240619_000625', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_220629:cmsbot_crab_rucio_transfers_withnoneedm_20240619_000628', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_220632:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_000631', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-19T09:55:14Z)

all OK
