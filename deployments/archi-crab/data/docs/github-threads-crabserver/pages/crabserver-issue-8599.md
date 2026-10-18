# dmwm/CRABServer issue #8599: #822: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-08T22:15:42Z
Closed: 2024-08-09T07:55:07Z
URL: https://github.com/dmwm/CRABServer/issues/8599

## Opening post (cmsdmwmbot, 2024-08-08T22:15:42Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-08-09 00:15:42
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/822/)

## Comment (cmsdmwmbot, 2024-08-08T22:18:29Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240808_221722:cmsbot_crab_20240809_001721
240808_221723:cmsbot_crab_20240809_001723
240808_221725:cmsbot_crab_20240809_001724
240808_221727:cmsbot_crab_20240809_001726
240808_221728:cmsbot_crab_20240809_001728
240808_221755:cmsbot_crab_20240809_001729
240808_221758:cmsbot_crab_rucio_transfers_20240809_001757
240808_221759:cmsbot_crab_rucio_transfers_group_20240809_001759
240808_221802:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_001800
240808_221804:cmsbot_crab_rucio_transfers_nopublication_20240809_001803
240808_221806:cmsbot_crab_rucio_transfers_withnoneedm_20240809_001805
240808_221808:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_001807
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240808_221633:cmsbot_crab_transferOutputs
240808_221635:cmsbot_crab_transferLogs
240808_221637:cmsbot_crab_activity
240808_221639:cmsbot_crab_inputFiles
240808_221640:cmsbot_crab_disableAutomaticOutputCollection
240808_221642:cmsbot_crab_outputFiles
240808_221643:cmsbot_crab_allowUndistributedCMSSW
240808_221645:cmsbot_crab_maxMemoryMB
240808_221646:cmsbot_crab_maxJobRuntimeMin
240808_221647:cmsbot_crab_numCores
240808_221649:cmsbot_crab_scriptExe
240808_221650:cmsbot_crab_scriptArgs
240808_221652:cmsbot_crab_sendVenvFolder
240808_221653:cmsbot_crab_sendExternalFolder
240808_221655:cmsbot_crab_inputDBS
240808_221656:cmsbot_crab_useParent
240808_221658:cmsbot_crab_secondaryInputDataset
240808_221659:cmsbot_crab_lumiMaskFile
240808_221701:cmsbot_crab_lumiMaskUrl
240808_221703:cmsbot_crab_outLFNDirBase
240808_221705:cmsbot_crab_runRange
240808_221706:cmsbot_crab_ignoreLocality
240808_221708:cmsbot_crab_userInputFiles
240808_221709:cmsbot_crab_whitelist
240808_221711:cmsbot_crab_blacklist
240808_221712:cmsbot_crab_ignoreGlobalBlacklist
240808_221714:cmsbot_crab_voRole
240808_221715:cmsbot_crab_voGroup
240808_221717:cmsbot_crab_scheddName
240808_221718:cmsbot_crab_collector
240808_221720:cmsbot_crab_extraJDL
```

Finished at: 2024-08-09 00:18:08
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/822/console)

## Comment (cmsdmwmbot, 2024-08-08T22:39:27Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-09 00:39:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1055/console

```
{'TN': '240808_221722:cmsbot_crab_20240809_001721', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 992, 'running': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221723:cmsbot_crab_20240809_001723', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221725:cmsbot_crab_20240809_001724', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221727:cmsbot_crab_20240809_001726', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221728:cmsbot_crab_20240809_001728', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 97, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221755:cmsbot_crab_20240809_001729', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 4, 'running': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221758:cmsbot_crab_rucio_transfers_20240809_001757', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221759:cmsbot_crab_rucio_transfers_group_20240809_001759', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221802:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_001800', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221804:cmsbot_crab_rucio_transfers_nopublication_20240809_001803', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221806:cmsbot_crab_rucio_transfers_withnoneedm_20240809_001805', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221808:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_001807', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-08T22:42:08Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-09 00:42:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1148/console

```
RETRY TESTS:
maxMemoryMB-check.sh 240808_221645:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240808_221646:cmsbot_crab_maxJobRuntimeMin - 2
scriptArgs-check.sh 240808_221650:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240808_221656:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240808_221658:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240808_221659:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240808_221701:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240808_221703:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240808_221705:cmsbot_crab_runRange - 2
whitelist-check.sh 240808_221709:cmsbot_crab_whitelist - 2
blacklist-check.sh 240808_221711:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240808_221712:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240808_221714:cmsbot_crab_voRole - 2
voGroup-check.sh 240808_221715:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240808_221633:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240808_221635:cmsbot_crab_transferLogs - 0
activity-check.sh 240808_221637:cmsbot_crab_activity - 0
inputFiles-check.sh 240808_221639:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240808_221640:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240808_221642:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240808_221643:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240808_221647:cmsbot_crab_numCores - 0
scriptExe-check.sh 240808_221649:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240808_221652:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240808_221653:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240808_221655:cmsbot_crab_inputDBS - 0
ignoreLocality-check.sh 240808_221706:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240808_221708:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240808_221717:cmsbot_crab_scheddName - 0
collector-check.sh 240808_221718:cmsbot_crab_collector - 0
extraJDL-check.sh 240808_221720:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-08T22:55:29Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-08-09 00:55:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1056/console

```
{'TN': '240808_221722:cmsbot_crab_20240809_001721', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221723:cmsbot_crab_20240809_001723', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221725:cmsbot_crab_20240809_001724', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221727:cmsbot_crab_20240809_001726', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221728:cmsbot_crab_20240809_001728', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221755:cmsbot_crab_20240809_001729', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221758:cmsbot_crab_rucio_transfers_20240809_001757', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221759:cmsbot_crab_rucio_transfers_group_20240809_001759', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221802:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_001800', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221804:cmsbot_crab_rucio_transfers_nopublication_20240809_001803', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221806:cmsbot_crab_rucio_transfers_withnoneedm_20240809_001805', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221808:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_001807', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-08T23:06:19Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-08-09 01:06:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1149/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240808_221633:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240808_221635:cmsbot_crab_transferLogs - 0
activity-check.sh 240808_221637:cmsbot_crab_activity - 0
inputFiles-check.sh 240808_221639:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240808_221640:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240808_221642:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240808_221643:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240808_221645:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240808_221646:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240808_221647:cmsbot_crab_numCores - 0
scriptExe-check.sh 240808_221649:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240808_221650:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240808_221652:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240808_221653:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240808_221655:cmsbot_crab_inputDBS - 0
useParent-check.sh 240808_221656:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240808_221658:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240808_221659:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240808_221701:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240808_221703:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240808_221705:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240808_221706:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240808_221708:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240808_221709:cmsbot_crab_whitelist - 0
blacklist-check.sh 240808_221711:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240808_221712:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240808_221714:cmsbot_crab_voRole - 0
voGroup-check.sh 240808_221715:cmsbot_crab_voGroup - 0
scheddName-check.sh 240808_221717:cmsbot_crab_scheddName - 0
collector-check.sh 240808_221718:cmsbot_crab_collector - 0
extraJDL-check.sh 240808_221720:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-08T23:42:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-08-09 01:42:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1057/console

```
{'TN': '240808_221722:cmsbot_crab_20240809_001721', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240808_221723:cmsbot_crab_20240809_001723', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221725:cmsbot_crab_20240809_001724', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240808_221727:cmsbot_crab_20240809_001726', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240808_221728:cmsbot_crab_20240809_001728', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240808_221755:cmsbot_crab_20240809_001729', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240808_221758:cmsbot_crab_rucio_transfers_20240809_001757', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221759:cmsbot_crab_rucio_transfers_group_20240809_001759', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221802:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_001800', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221804:cmsbot_crab_rucio_transfers_nopublication_20240809_001803', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221806:cmsbot_crab_rucio_transfers_withnoneedm_20240809_001805', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221808:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_001807', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-09T01:14:32Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-08-09 03:14:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1058/console

```
{'TN': '240808_221722:cmsbot_crab_20240809_001721', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240808_221723:cmsbot_crab_20240809_001723', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240808_221725:cmsbot_crab_20240809_001724', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240808_221727:cmsbot_crab_20240809_001726', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240808_221728:cmsbot_crab_20240809_001728', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240808_221755:cmsbot_crab_20240809_001729', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240808_221758:cmsbot_crab_rucio_transfers_20240809_001757', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 18, 'finished': 22}, 'publication (fail/tdb/DBS)': '0/22/22'}
{'TN': '240808_221759:cmsbot_crab_rucio_transfers_group_20240809_001759', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 17, 'finished': 23}, 'publication (fail/tdb/DBS)': '0/23/23'}
{'TN': '240808_221802:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_001800', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 27, 'finished': 13}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221804:cmsbot_crab_rucio_transfers_nopublication_20240809_001803', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 21, 'transferring': 19}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221806:cmsbot_crab_rucio_transfers_withnoneedm_20240809_001805', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 26, 'finished': 14}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221808:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_001807', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 36, 'finished': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-09T03:16:34Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 4 out of 5. Test is done.
**Finished at:** 2024-08-09 05:16:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1059/console

```
{'TN': '240808_221722:cmsbot_crab_20240809_001721', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240808_221723:cmsbot_crab_20240809_001723', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240808_221725:cmsbot_crab_20240809_001724', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240808_221727:cmsbot_crab_20240809_001726', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240808_221728:cmsbot_crab_20240809_001728', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240808_221755:cmsbot_crab_20240809_001729', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240808_221758:cmsbot_crab_rucio_transfers_20240809_001757', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240808_221759:cmsbot_crab_rucio_transfers_group_20240809_001759', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240808_221802:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_001800', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221804:cmsbot_crab_rucio_transfers_nopublication_20240809_001803', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240808_221806:cmsbot_crab_rucio_transfers_withnoneedm_20240809_001805', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240808_221808:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_001807', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-08-09T07:54:16Z)

all good
