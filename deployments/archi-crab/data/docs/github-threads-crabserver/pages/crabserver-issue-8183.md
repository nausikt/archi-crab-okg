# dmwm/CRABServer issue #8183: #679: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-13T12:24:44Z
Closed: 2024-01-15T08:28:55Z
URL: https://github.com/dmwm/CRABServer/issues/8183

## Opening post (cmsdmwmbot, 2024-01-13T12:24:44Z)

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

Started at: 2024-01-13 13:24:43
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/679/)

## Comment (cmsdmwmbot, 2024-01-13T12:28:14Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240113_122702:cmsbot_crab_20240113_132702
240113_122705:cmsbot_crab_20240113_132704
240113_122707:cmsbot_crab_20240113_132706
240113_122709:cmsbot_crab_20240113_132708
240113_122711:cmsbot_crab_20240113_132710
240113_122738:cmsbot_crab_20240113_132712
240113_122741:cmsbot_crab_rucio_transfers_20240113_132739
240113_122744:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240113_132742
240113_122747:cmsbot_crab_rucio_transfers_nopublication_20240113_132745
240113_122750:cmsbot_crab_rucio_transfers_withnoneedm_20240113_132748
240113_122753:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240113_132751
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240113_122509:cmsbot_crab_transferOutputs
240113_122511:cmsbot_crab_transferLogs
240113_122513:cmsbot_crab_activity
240113_122515:cmsbot_crab_inputFiles
240113_122517:cmsbot_crab_disableAutomaticOutputCollection
240113_122520:cmsbot_crab_outputFiles
240113_122522:cmsbot_crab_allowUndistributedCMSSW
240113_122524:cmsbot_crab_maxMemoryMB
240113_122526:cmsbot_crab_maxJobRuntimeMin
240113_122528:cmsbot_crab_numCores
240113_122530:cmsbot_crab_scriptExe
240113_122532:cmsbot_crab_scriptArgs
240113_122534:cmsbot_crab_sendVenvFolder
240113_122622:cmsbot_crab_sendExternalFolder
240113_122624:cmsbot_crab_inputDBS
240113_122626:cmsbot_crab_useParent
240113_122628:cmsbot_crab_secondaryInputDataset
240113_122630:cmsbot_crab_lumiMaskFile
240113_122633:cmsbot_crab_lumiMaskUrl
240113_122636:cmsbot_crab_outLFNDirBase
240113_122638:cmsbot_crab_runRange
240113_122641:cmsbot_crab_ignoreLocality
240113_122643:cmsbot_crab_userInputFiles
240113_122645:cmsbot_crab_whitelist
240113_122647:cmsbot_crab_blacklist
240113_122649:cmsbot_crab_ignoreGlobalBlacklist
240113_122651:cmsbot_crab_voRole
240113_122653:cmsbot_crab_voGroup
240113_122655:cmsbot_crab_scheddName
240113_122657:cmsbot_crab_collector
240113_122659:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240113_122504:cmsbot_crab_20240113_132502
```

Finished at: 2024-01-13 13:27:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/679/console)

## Comment (cmsdmwmbot, 2024-01-13T12:49:30Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-13 13:49:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/720/console

```
{'TN': '240113_122702:cmsbot_crab_20240113_132702', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122705:cmsbot_crab_20240113_132704', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122707:cmsbot_crab_20240113_132706', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122709:cmsbot_crab_20240113_132708', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122711:cmsbot_crab_20240113_132710', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122738:cmsbot_crab_20240113_132712', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122741:cmsbot_crab_rucio_transfers_20240113_132739', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122744:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240113_132742', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'idle': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122747:cmsbot_crab_rucio_transfers_nopublication_20240113_132745', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122750:cmsbot_crab_rucio_transfers_withnoneedm_20240113_132748', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'idle': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122753:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240113_132751', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-13T12:51:27Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-13 13:51:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/497/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/497//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-13T12:53:25Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-13 13:53:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/889/console

```
RETRY TESTS:
activity-check.sh 240113_122513:cmsbot_crab_activity - 2
scriptArgs-check.sh 240113_122532:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240113_122633:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240113_122638:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240113_122643:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240113_122645:cmsbot_crab_whitelist - 2
blacklist-check.sh 240113_122647:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240113_122509:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240113_122511:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240113_122515:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240113_122517:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240113_122520:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240113_122522:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240113_122524:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240113_122526:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240113_122528:cmsbot_crab_numCores - 0
scriptExe-check.sh 240113_122530:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240113_122534:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240113_122622:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240113_122624:cmsbot_crab_inputDBS - 0
useParent-check.sh 240113_122626:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240113_122628:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240113_122630:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240113_122636:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240113_122641:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240113_122649:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240113_122651:cmsbot_crab_voRole - 0
voGroup-check.sh 240113_122653:cmsbot_crab_voGroup - 0
scheddName-check.sh 240113_122655:cmsbot_crab_scheddName - 0
collector-check.sh 240113_122657:cmsbot_crab_collector - 0
extraJDL-check.sh 240113_122659:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-13T13:06:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-01-13 14:06:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/721/console

```
{'TN': '240113_122702:cmsbot_crab_20240113_132702', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 272, 'finished': 728}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122705:cmsbot_crab_20240113_132704', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122707:cmsbot_crab_20240113_132706', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122709:cmsbot_crab_20240113_132708', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122711:cmsbot_crab_20240113_132710', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 94, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122738:cmsbot_crab_20240113_132712', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122741:cmsbot_crab_rucio_transfers_20240113_132739', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122744:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240113_132742', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122747:cmsbot_crab_rucio_transfers_nopublication_20240113_132745', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122750:cmsbot_crab_rucio_transfers_withnoneedm_20240113_132748', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122753:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240113_132751', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-13T13:18:36Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-01-13 14:18:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/890/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240113_122509:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240113_122511:cmsbot_crab_transferLogs - 0
activity-check.sh 240113_122513:cmsbot_crab_activity - 0
inputFiles-check.sh 240113_122515:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240113_122517:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240113_122520:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240113_122522:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240113_122524:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240113_122526:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240113_122528:cmsbot_crab_numCores - 0
scriptExe-check.sh 240113_122530:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240113_122532:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240113_122534:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240113_122622:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240113_122624:cmsbot_crab_inputDBS - 0
useParent-check.sh 240113_122626:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240113_122628:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240113_122630:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240113_122633:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240113_122636:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240113_122638:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240113_122641:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240113_122643:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240113_122645:cmsbot_crab_whitelist - 0
blacklist-check.sh 240113_122647:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240113_122649:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240113_122651:cmsbot_crab_voRole - 0
voGroup-check.sh 240113_122653:cmsbot_crab_voGroup - 0
scheddName-check.sh 240113_122655:cmsbot_crab_scheddName - 0
collector-check.sh 240113_122657:cmsbot_crab_collector - 0
extraJDL-check.sh 240113_122659:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-13T13:52:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-01-13 14:52:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/722/console

```
{'TN': '240113_122702:cmsbot_crab_20240113_132702', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240113_122705:cmsbot_crab_20240113_132704', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122707:cmsbot_crab_20240113_132706', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240113_122709:cmsbot_crab_20240113_132708', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240113_122711:cmsbot_crab_20240113_132710', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240113_122738:cmsbot_crab_20240113_132712', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240113_122741:cmsbot_crab_rucio_transfers_20240113_132739', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240113_122744:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240113_132742', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122747:cmsbot_crab_rucio_transfers_nopublication_20240113_132745', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122750:cmsbot_crab_rucio_transfers_withnoneedm_20240113_132748', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240113_122753:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240113_132751', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-13T15:24:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-01-13 16:24:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/723/console

```
{'TN': '240113_122702:cmsbot_crab_20240113_132702', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240113_122705:cmsbot_crab_20240113_132704', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240113_122707:cmsbot_crab_20240113_132706', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240113_122709:cmsbot_crab_20240113_132708', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240113_122711:cmsbot_crab_20240113_132710', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240113_122738:cmsbot_crab_20240113_132712', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240113_122741:cmsbot_crab_rucio_transfers_20240113_132739', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240113_122744:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240113_132742', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122747:cmsbot_crab_rucio_transfers_nopublication_20240113_132745', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122750:cmsbot_crab_rucio_transfers_withnoneedm_20240113_132748', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240113_122753:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240113_132751', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-13T17:28:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-01-13 18:28:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/724/console

```
{'TN': '240113_122702:cmsbot_crab_20240113_132702', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240113_122705:cmsbot_crab_20240113_132704', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240113_122707:cmsbot_crab_20240113_132706', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240113_122709:cmsbot_crab_20240113_132708', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240113_122711:cmsbot_crab_20240113_132710', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240113_122738:cmsbot_crab_20240113_132712', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240113_122741:cmsbot_crab_rucio_transfers_20240113_132739', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240113_122744:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240113_132742', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122747:cmsbot_crab_rucio_transfers_nopublication_20240113_132745', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122750:cmsbot_crab_rucio_transfers_withnoneedm_20240113_132748', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240113_122753:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240113_132751', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-13T19:29:24Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-01-13 20:29:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/725/console

```
{'TN': '240113_122702:cmsbot_crab_20240113_132702', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240113_122705:cmsbot_crab_20240113_132704', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240113_122707:cmsbot_crab_20240113_132706', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240113_122709:cmsbot_crab_20240113_132708', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240113_122711:cmsbot_crab_20240113_132710', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240113_122738:cmsbot_crab_20240113_132712', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240113_122741:cmsbot_crab_rucio_transfers_20240113_132739', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240113_122744:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240113_132742', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122747:cmsbot_crab_rucio_transfers_nopublication_20240113_132745', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240113_122750:cmsbot_crab_rucio_transfers_withnoneedm_20240113_132748', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240113_122753:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240113_132751', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-01-15T08:28:55Z)

All OK. The `nopublication` Rucio configs are of course failing the publication check.
We should avoid enabling publication check in test submission until a solution is found, when Wa is back.
