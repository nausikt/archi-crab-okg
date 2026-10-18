# dmwm/CRABServer issue #8619: #830: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-14T11:06:13Z
Closed: 2024-08-14T18:59:00Z
URL: https://github.com/dmwm/CRABServer/issues/8619

## Opening post (cmsdmwmbot, 2024-08-14T11:06:13Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-08-14 13:06:12
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/830/)

## Comment (cmsdmwmbot, 2024-08-14T11:08:56Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240814_110745:cmsbot_crab_20240814_130745
240814_110747:cmsbot_crab_20240814_130747
240814_110750:cmsbot_crab_20240814_130749
240814_110752:cmsbot_crab_20240814_130751
240814_110754:cmsbot_crab_20240814_130754
240814_110818:cmsbot_crab_20240814_130756
240814_110821:cmsbot_crab_rucio_transfers_20240814_130820
240814_110823:cmsbot_crab_rucio_transfers_group_20240814_130823
240814_110826:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240814_130825
240814_110829:cmsbot_crab_rucio_transfers_nopublication_20240814_130828
240814_110832:cmsbot_crab_rucio_transfers_withnoneedm_20240814_130830
240814_110834:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240814_130833
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240814_110635:cmsbot_crab_transferOutputs
240814_110637:cmsbot_crab_transferLogs
240814_110639:cmsbot_crab_activity
240814_110641:cmsbot_crab_inputFiles
240814_110644:cmsbot_crab_disableAutomaticOutputCollection
240814_110646:cmsbot_crab_outputFiles
240814_110648:cmsbot_crab_allowUndistributedCMSSW
240814_110650:cmsbot_crab_maxMemoryMB
240814_110653:cmsbot_crab_maxJobRuntimeMin
240814_110655:cmsbot_crab_numCores
240814_110657:cmsbot_crab_scriptExe
240814_110659:cmsbot_crab_scriptArgs
240814_110702:cmsbot_crab_sendVenvFolder
240814_110704:cmsbot_crab_sendExternalFolder
240814_110706:cmsbot_crab_inputDBS
240814_110708:cmsbot_crab_useParent
240814_110710:cmsbot_crab_secondaryInputDataset
240814_110713:cmsbot_crab_lumiMaskFile
240814_110715:cmsbot_crab_lumiMaskUrl
240814_110718:cmsbot_crab_outLFNDirBase
240814_110720:cmsbot_crab_runRange
240814_110723:cmsbot_crab_ignoreLocality
240814_110725:cmsbot_crab_userInputFiles
240814_110727:cmsbot_crab_whitelist
240814_110729:cmsbot_crab_blacklist
240814_110731:cmsbot_crab_ignoreGlobalBlacklist
240814_110734:cmsbot_crab_voRole
240814_110736:cmsbot_crab_voGroup
240814_110738:cmsbot_crab_scheddName
240814_110740:cmsbot_crab_collector
240814_110742:cmsbot_crab_extraJDL
```

Finished at: 2024-08-14 13:08:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/830/console)

## Comment (cmsdmwmbot, 2024-08-14T11:32:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-14 13:32:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1083/console

```
{'TN': '240814_110745:cmsbot_crab_20240814_130745', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 992, 'running': 2, 'failed': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110747:cmsbot_crab_20240814_130747', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110750:cmsbot_crab_20240814_130749', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110752:cmsbot_crab_20240814_130751', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110754:cmsbot_crab_20240814_130754', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110818:cmsbot_crab_20240814_130756', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110821:cmsbot_crab_rucio_transfers_20240814_130820', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110823:cmsbot_crab_rucio_transfers_group_20240814_130823', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110826:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240814_130825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110829:cmsbot_crab_rucio_transfers_nopublication_20240814_130828', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110832:cmsbot_crab_rucio_transfers_withnoneedm_20240814_130830', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110834:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240814_130833', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-14T11:35:52Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-14 13:35:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1163/console

```
RETRY TESTS:
transferLogs-check.sh 240814_110637:cmsbot_crab_transferLogs - 2
activity-check.sh 240814_110639:cmsbot_crab_activity - 2
outputFiles-check.sh 240814_110646:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240814_110650:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240814_110653:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240814_110655:cmsbot_crab_numCores - 2
scriptExe-check.sh 240814_110657:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240814_110659:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240814_110713:cmsbot_crab_lumiMaskFile - 2
outLFNDirBase-check.sh 240814_110718:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240814_110720:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240814_110725:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240814_110727:cmsbot_crab_whitelist - 2
blacklist-check.sh 240814_110729:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240814_110731:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240814_110734:cmsbot_crab_voRole - 2
voGroup-check.sh 240814_110736:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240814_110635:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240814_110641:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240814_110644:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240814_110648:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240814_110702:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240814_110704:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240814_110706:cmsbot_crab_inputDBS - 0
useParent-check.sh 240814_110708:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240814_110710:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240814_110723:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 240814_110738:cmsbot_crab_scheddName - 0
collector-check.sh 240814_110740:cmsbot_crab_collector - 0
extraJDL-check.sh 240814_110742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240814_110715:cmsbot_crab_lumiMaskUrl - 1
```

## Comment (cmsdmwmbot, 2024-08-14T11:49:04Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-08-14 13:49:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1084/console

```
{'TN': '240814_110745:cmsbot_crab_20240814_130745', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 849, 'transferring': 151}, 'publication (fail/tdb/DBS)': '0/800/800'}
{'TN': '240814_110747:cmsbot_crab_20240814_130747', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110750:cmsbot_crab_20240814_130749', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110752:cmsbot_crab_20240814_130751', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240814_110754:cmsbot_crab_20240814_130754', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110818:cmsbot_crab_20240814_130756', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110821:cmsbot_crab_rucio_transfers_20240814_130820', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110823:cmsbot_crab_rucio_transfers_group_20240814_130823', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110826:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240814_130825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110829:cmsbot_crab_rucio_transfers_nopublication_20240814_130828', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110832:cmsbot_crab_rucio_transfers_withnoneedm_20240814_130830', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110834:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240814_130833', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-14T11:59:47Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-08-14 13:59:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1164/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240814_110635:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240814_110637:cmsbot_crab_transferLogs - 0
activity-check.sh 240814_110639:cmsbot_crab_activity - 0
inputFiles-check.sh 240814_110641:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240814_110644:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240814_110646:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240814_110648:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240814_110650:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240814_110653:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240814_110655:cmsbot_crab_numCores - 0
scriptExe-check.sh 240814_110657:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240814_110659:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240814_110702:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240814_110704:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240814_110706:cmsbot_crab_inputDBS - 0
useParent-check.sh 240814_110708:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240814_110710:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240814_110713:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240814_110718:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240814_110720:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240814_110723:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240814_110725:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240814_110727:cmsbot_crab_whitelist - 0
blacklist-check.sh 240814_110729:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240814_110731:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240814_110734:cmsbot_crab_voRole - 0
voGroup-check.sh 240814_110736:cmsbot_crab_voGroup - 0
scheddName-check.sh 240814_110738:cmsbot_crab_scheddName - 0
collector-check.sh 240814_110740:cmsbot_crab_collector - 0
extraJDL-check.sh 240814_110742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240814_110715:cmsbot_crab_lumiMaskUrl - 1
```

## Comment (cmsdmwmbot, 2024-08-14T12:35:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-08-14 14:35:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1085/console

```
{'TN': '240814_110745:cmsbot_crab_20240814_130745', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240814_110747:cmsbot_crab_20240814_130747', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110750:cmsbot_crab_20240814_130749', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240814_110752:cmsbot_crab_20240814_130751', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240814_110754:cmsbot_crab_20240814_130754', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/98/98'}
{'TN': '240814_110818:cmsbot_crab_20240814_130756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/7/7'}
{'TN': '240814_110821:cmsbot_crab_rucio_transfers_20240814_130820', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110823:cmsbot_crab_rucio_transfers_group_20240814_130823', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 27, 'transferring': 13}, 'publication (fail/tdb/DBS)': '0/18/18'}
{'TN': '240814_110826:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240814_130825', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110829:cmsbot_crab_rucio_transfers_nopublication_20240814_130828', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110832:cmsbot_crab_rucio_transfers_withnoneedm_20240814_130830', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110834:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240814_130833', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-14T12:39:01Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-14 14:38:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1165/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240814_110715:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240814_110635:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240814_110637:cmsbot_crab_transferLogs - 0
activity-check.sh 240814_110639:cmsbot_crab_activity - 0
inputFiles-check.sh 240814_110641:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240814_110644:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240814_110646:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240814_110648:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240814_110650:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240814_110653:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240814_110655:cmsbot_crab_numCores - 0
scriptExe-check.sh 240814_110657:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240814_110659:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240814_110702:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240814_110704:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240814_110706:cmsbot_crab_inputDBS - 0
useParent-check.sh 240814_110708:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240814_110710:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240814_110713:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240814_110718:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240814_110720:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240814_110723:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240814_110725:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240814_110727:cmsbot_crab_whitelist - 0
blacklist-check.sh 240814_110729:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240814_110731:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240814_110734:cmsbot_crab_voRole - 0
voGroup-check.sh 240814_110736:cmsbot_crab_voGroup - 0
scheddName-check.sh 240814_110738:cmsbot_crab_scheddName - 0
collector-check.sh 240814_110740:cmsbot_crab_collector - 0
extraJDL-check.sh 240814_110742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-14T13:03:12Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-08-14 15:03:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1166/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240814_110635:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240814_110637:cmsbot_crab_transferLogs - 0
activity-check.sh 240814_110639:cmsbot_crab_activity - 0
inputFiles-check.sh 240814_110641:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240814_110644:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240814_110646:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240814_110648:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240814_110650:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240814_110653:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240814_110655:cmsbot_crab_numCores - 0
scriptExe-check.sh 240814_110657:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240814_110659:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240814_110702:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240814_110704:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240814_110706:cmsbot_crab_inputDBS - 0
useParent-check.sh 240814_110708:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240814_110710:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240814_110713:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240814_110715:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240814_110718:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240814_110720:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240814_110723:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240814_110725:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240814_110727:cmsbot_crab_whitelist - 0
blacklist-check.sh 240814_110729:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240814_110731:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240814_110734:cmsbot_crab_voRole - 0
voGroup-check.sh 240814_110736:cmsbot_crab_voGroup - 0
scheddName-check.sh 240814_110738:cmsbot_crab_scheddName - 0
collector-check.sh 240814_110740:cmsbot_crab_collector - 0
extraJDL-check.sh 240814_110742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-14T14:07:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-08-14 16:07:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1086/console

```
{'TN': '240814_110745:cmsbot_crab_20240814_130745', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240814_110747:cmsbot_crab_20240814_130747', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240814_110750:cmsbot_crab_20240814_130749', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240814_110752:cmsbot_crab_20240814_130751', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240814_110754:cmsbot_crab_20240814_130754', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240814_110818:cmsbot_crab_20240814_130756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240814_110821:cmsbot_crab_rucio_transfers_20240814_130820', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110823:cmsbot_crab_rucio_transfers_group_20240814_130823', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/32/32'}
{'TN': '240814_110826:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240814_130825', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110829:cmsbot_crab_rucio_transfers_nopublication_20240814_130828', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110832:cmsbot_crab_rucio_transfers_withnoneedm_20240814_130830', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110834:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240814_130833', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-14T16:12:01Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-08-14 18:12:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1087/console

```
{'TN': '240814_110745:cmsbot_crab_20240814_130745', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240814_110747:cmsbot_crab_20240814_130747', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240814_110750:cmsbot_crab_20240814_130749', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240814_110752:cmsbot_crab_20240814_130751', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240814_110754:cmsbot_crab_20240814_130754', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240814_110818:cmsbot_crab_20240814_130756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240814_110821:cmsbot_crab_rucio_transfers_20240814_130820', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110823:cmsbot_crab_rucio_transfers_group_20240814_130823', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240814_110826:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240814_130825', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110829:cmsbot_crab_rucio_transfers_nopublication_20240814_130828', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110832:cmsbot_crab_rucio_transfers_withnoneedm_20240814_130830', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110834:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240814_130833', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-14T18:14:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-08-14 20:14:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1088/console

```
{'TN': '240814_110745:cmsbot_crab_20240814_130745', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240814_110747:cmsbot_crab_20240814_130747', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240814_110750:cmsbot_crab_20240814_130749', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240814_110752:cmsbot_crab_20240814_130751', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240814_110754:cmsbot_crab_20240814_130754', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240814_110818:cmsbot_crab_20240814_130756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240814_110821:cmsbot_crab_rucio_transfers_20240814_130820', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110823:cmsbot_crab_rucio_transfers_group_20240814_130823', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240814_110826:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240814_130825', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110829:cmsbot_crab_rucio_transfers_nopublication_20240814_130828', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110832:cmsbot_crab_rucio_transfers_withnoneedm_20240814_130830', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110834:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240814_130833', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-14T18:57:56Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 5 out of 0. Test is done.
**Finished at:** 2024-08-14 20:57:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1089/console

```
{'TN': '240814_110745:cmsbot_crab_20240814_130745', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240814_110747:cmsbot_crab_20240814_130747', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240814_110750:cmsbot_crab_20240814_130749', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240814_110752:cmsbot_crab_20240814_130751', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240814_110754:cmsbot_crab_20240814_130754', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240814_110818:cmsbot_crab_20240814_130756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240814_110821:cmsbot_crab_rucio_transfers_20240814_130820', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110823:cmsbot_crab_rucio_transfers_group_20240814_130823', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110826:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240814_130825', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110829:cmsbot_crab_rucio_transfers_nopublication_20240814_130828', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240814_110832:cmsbot_crab_rucio_transfers_withnoneedm_20240814_130830', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240814_110834:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240814_130833', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-08-14T18:59:00Z)

took a couple of kicks, but in the end everything worked
