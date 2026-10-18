# dmwm/CRABServer issue #8469: #795: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-03T22:15:20Z
Closed: 2024-06-04T12:43:29Z
URL: https://github.com/dmwm/CRABServer/issues/8469

## Opening post (cmsdmwmbot, 2024-06-03T22:15:20Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-06-04 00:15:19
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/795/)

## Comment (cmsdmwmbot, 2024-06-03T22:18:10Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240603_221653:cmsbot_crab_20240604_001652
240603_221655:cmsbot_crab_20240604_001654
240603_221657:cmsbot_crab_20240604_001656
240603_221659:cmsbot_crab_20240604_001659
240603_221701:cmsbot_crab_20240604_001701
240603_221730:cmsbot_crab_20240604_001703
240603_221734:cmsbot_crab_rucio_transfers_20240604_001732
240603_221736:cmsbot_crab_rucio_transfers_group_20240604_001735
240603_221739:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001737
240603_221742:cmsbot_crab_rucio_transfers_nopublication_20240604_001740
240603_221745:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001744
240603_221749:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001747
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240603_221543:cmsbot_crab_transferOutputs
240603_221546:cmsbot_crab_transferLogs
240603_221548:cmsbot_crab_activity
240603_221550:cmsbot_crab_inputFiles
240603_221552:cmsbot_crab_disableAutomaticOutputCollection
240603_221554:cmsbot_crab_outputFiles
240603_221556:cmsbot_crab_allowUndistributedCMSSW
240603_221559:cmsbot_crab_maxMemoryMB
240603_221601:cmsbot_crab_maxJobRuntimeMin
240603_221603:cmsbot_crab_numCores
240603_221605:cmsbot_crab_scriptExe
240603_221607:cmsbot_crab_scriptArgs
240603_221609:cmsbot_crab_sendVenvFolder
240603_221612:cmsbot_crab_sendExternalFolder
240603_221614:cmsbot_crab_inputDBS
240603_221616:cmsbot_crab_useParent
240603_221618:cmsbot_crab_secondaryInputDataset
240603_221621:cmsbot_crab_lumiMaskFile
240603_221623:cmsbot_crab_lumiMaskUrl
240603_221626:cmsbot_crab_outLFNDirBase
240603_221628:cmsbot_crab_runRange
240603_221631:cmsbot_crab_ignoreLocality
240603_221633:cmsbot_crab_userInputFiles
240603_221635:cmsbot_crab_whitelist
240603_221637:cmsbot_crab_blacklist
240603_221639:cmsbot_crab_ignoreGlobalBlacklist
240603_221641:cmsbot_crab_voRole
240603_221643:cmsbot_crab_voGroup
240603_221646:cmsbot_crab_scheddName
240603_221648:cmsbot_crab_collector
240603_221650:cmsbot_crab_extraJDL
```

Finished at: 2024-06-04 00:17:49
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/795/console)

## Comment (cmsdmwmbot, 2024-06-03T22:39:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-04 00:39:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/959/console

```
{'TN': '240603_221653:cmsbot_crab_20240604_001652', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221655:cmsbot_crab_20240604_001654', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221657:cmsbot_crab_20240604_001656', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221659:cmsbot_crab_20240604_001659', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221701:cmsbot_crab_20240604_001701', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221730:cmsbot_crab_20240604_001703', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221734:cmsbot_crab_rucio_transfers_20240604_001732', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221736:cmsbot_crab_rucio_transfers_group_20240604_001735', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221739:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001737', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221742:cmsbot_crab_rucio_transfers_nopublication_20240604_001740', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221745:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001744', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221749:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001747', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T22:42:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-04 00:42:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1095/console

```
RETRY TESTS:
outputFiles-check.sh 240603_221554:cmsbot_crab_outputFiles - 2
numCores-check.sh 240603_221603:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240603_221607:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240603_221623:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240603_221628:cmsbot_crab_runRange - 2
whitelist-check.sh 240603_221635:cmsbot_crab_whitelist - 2
blacklist-check.sh 240603_221637:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_221543:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_221546:cmsbot_crab_transferLogs - 0
activity-check.sh 240603_221548:cmsbot_crab_activity - 0
inputFiles-check.sh 240603_221550:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_221552:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240603_221556:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240603_221559:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240603_221601:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240603_221605:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240603_221609:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_221612:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_221614:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_221616:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_221618:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240603_221621:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240603_221626:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240603_221631:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_221633:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240603_221639:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_221641:cmsbot_crab_voRole - 0
voGroup-check.sh 240603_221643:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_221646:cmsbot_crab_scheddName - 0
collector-check.sh 240603_221648:cmsbot_crab_collector - 0
extraJDL-check.sh 240603_221650:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-03T22:54:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-04 00:54:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/961/console

```
{'TN': '240603_221653:cmsbot_crab_20240604_001652', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221655:cmsbot_crab_20240604_001654', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221657:cmsbot_crab_20240604_001656', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221659:cmsbot_crab_20240604_001659', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221701:cmsbot_crab_20240604_001701', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221730:cmsbot_crab_20240604_001703', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221734:cmsbot_crab_rucio_transfers_20240604_001732', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221736:cmsbot_crab_rucio_transfers_group_20240604_001735', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221739:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001737', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221742:cmsbot_crab_rucio_transfers_nopublication_20240604_001740', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221745:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001744', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221749:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001747', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T23:06:40Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-04 01:06:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1097/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_221543:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_221546:cmsbot_crab_transferLogs - 0
activity-check.sh 240603_221548:cmsbot_crab_activity - 0
inputFiles-check.sh 240603_221550:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_221552:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240603_221554:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240603_221556:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240603_221559:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240603_221601:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240603_221603:cmsbot_crab_numCores - 0
scriptExe-check.sh 240603_221605:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240603_221607:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240603_221609:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_221612:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_221614:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_221616:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_221618:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240603_221621:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240603_221623:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240603_221626:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240603_221628:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240603_221631:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_221633:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240603_221635:cmsbot_crab_whitelist - 0
blacklist-check.sh 240603_221637:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240603_221639:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_221641:cmsbot_crab_voRole - 0
voGroup-check.sh 240603_221643:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_221646:cmsbot_crab_scheddName - 0
collector-check.sh 240603_221648:cmsbot_crab_collector - 0
extraJDL-check.sh 240603_221650:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-03T23:40:47Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-04 01:40:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/965/console

```
{'TN': '240603_221653:cmsbot_crab_20240604_001652', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 999, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240603_221655:cmsbot_crab_20240604_001654', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221657:cmsbot_crab_20240604_001656', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221659:cmsbot_crab_20240604_001659', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221701:cmsbot_crab_20240604_001701', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_221730:cmsbot_crab_20240604_001703', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221734:cmsbot_crab_rucio_transfers_20240604_001732', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221736:cmsbot_crab_rucio_transfers_group_20240604_001735', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221739:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001737', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221742:cmsbot_crab_rucio_transfers_nopublication_20240604_001740', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221745:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001744', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221749:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001747', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-04T01:11:44Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-06-04 03:11:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/968/console

```
{'TN': '240603_221653:cmsbot_crab_20240604_001652', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 999, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240603_221655:cmsbot_crab_20240604_001654', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221657:cmsbot_crab_20240604_001656', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221659:cmsbot_crab_20240604_001659', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221701:cmsbot_crab_20240604_001701', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_221730:cmsbot_crab_20240604_001703', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221734:cmsbot_crab_rucio_transfers_20240604_001732', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221736:cmsbot_crab_rucio_transfers_group_20240604_001735', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221739:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001737', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221742:cmsbot_crab_rucio_transfers_nopublication_20240604_001740', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221745:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001744', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221749:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001747', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-04T03:12:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-06-04 05:12:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/971/console

```
{'TN': '240603_221653:cmsbot_crab_20240604_001652', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 999, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240603_221655:cmsbot_crab_20240604_001654', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221657:cmsbot_crab_20240604_001656', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221659:cmsbot_crab_20240604_001659', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221701:cmsbot_crab_20240604_001701', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_221730:cmsbot_crab_20240604_001703', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221734:cmsbot_crab_rucio_transfers_20240604_001732', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221736:cmsbot_crab_rucio_transfers_group_20240604_001735', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221739:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001737', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221742:cmsbot_crab_rucio_transfers_nopublication_20240604_001740', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221745:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001744', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221749:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001747', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-04T05:14:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-04 07:14:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/973/console

```
{'TN': '240603_221653:cmsbot_crab_20240604_001652', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 999, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240603_221655:cmsbot_crab_20240604_001654', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221657:cmsbot_crab_20240604_001656', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221659:cmsbot_crab_20240604_001659', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221701:cmsbot_crab_20240604_001701', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_221730:cmsbot_crab_20240604_001703', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221734:cmsbot_crab_rucio_transfers_20240604_001732', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221736:cmsbot_crab_rucio_transfers_group_20240604_001735', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221739:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001737', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221742:cmsbot_crab_rucio_transfers_nopublication_20240604_001740', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221745:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001744', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221749:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001747', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-04T07:26:32Z)

resubmission failed :sob: investigating
```
belforte@lxplus807/bot> crab status crab_20240604_001652/
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_20240604_001652
Task name:			240603_221653:cmsbot_crab_20240604_001652
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-preprod-tw01
Status on the CRAB server:	RESUBMITFAILED
Task URL to use for HELP:	https://cmsweb-testbed.cern.ch/crabserver/ui/task/240603_221653%3Acmsbot_crab_20240604_001652
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240603_221653%3Acmsbot_crab_20240604_001652&from=1717449413000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_SGrid_Bristol']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Failure message from server:	The CRAB server backend was not able to resubmit the task, because the Grid scheduler answered with an error. This is probably a temporary glitch. Please try again later. If the error persists send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch. Error reason: Unable to edit jobs matching constraint
Status on the 
```

## Comment (belforte, 2024-06-04T07:28:11Z)

error is
```
  File "/data/srv/TaskManager/v3.240603-c9fbdc0538bd0008e8fe4e772eece824/slc7_amd64_gcc630/cms/crabtaskworker/v3.240603-c9fbdc0538bd0008e8fe4e772eece824/lib/python3.8/site-packages/TaskWorker/Actions/DagmanResubmitter.py", line 95, in executeInternal
    schedd.edit(rootConst, "HoldKillSig", 'SIGKILL')
  File "/data/srv/TaskManager/v3.240603-c9fbdc0538bd0008e8fe4e772eece824/slc7_amd64_gcc630/external/py3-htcondor/10.2.3/lib/python3.8/site-packages/htcondor/_lock.py", line 70, in wrapper
    rv = func(*args, **kwargs)
htcondor.HTCondorIOError: Unable to edit jobs matching constraint

```
