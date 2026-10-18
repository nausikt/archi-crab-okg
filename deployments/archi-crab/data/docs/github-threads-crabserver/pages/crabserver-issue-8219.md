# dmwm/CRABServer issue #8219: #700: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-02-02T11:37:00Z
Closed: 2024-02-02T14:46:21Z
URL: https://github.com/dmwm/CRABServer/issues/8219

## Opening post (cmsdmwmbot, 2024-02-02T11:37:00Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-02-02 12:36:59
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/700/)

## Comment (cmsdmwmbot, 2024-02-02T11:40:58Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240202_113912:cmsbot_crab_20240202_123911
240202_113914:cmsbot_crab_20240202_123914
240202_113916:cmsbot_crab_20240202_123916
240202_113919:cmsbot_crab_20240202_123918
240202_113921:cmsbot_crab_20240202_123920
240202_114003:cmsbot_crab_20240202_123922
240202_114021:cmsbot_crab_rucio_transfers_20240202_124004
240202_114024:cmsbot_crab_rucio_transfers_group_20240202_124023
240202_114027:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124025
240202_114030:cmsbot_crab_rucio_transfers_nopublication_20240202_124028
240202_114033:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124031
240202_114036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124035
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_113722:cmsbot_crab_transferOutputs
240202_113724:cmsbot_crab_transferLogs
240202_113726:cmsbot_crab_activity
240202_113729:cmsbot_crab_inputFiles
240202_113731:cmsbot_crab_disableAutomaticOutputCollection
240202_113733:cmsbot_crab_outputFiles
240202_113735:cmsbot_crab_allowUndistributedCMSSW
240202_113738:cmsbot_crab_maxMemoryMB
240202_113740:cmsbot_crab_maxJobRuntimeMin
240202_113742:cmsbot_crab_numCores
240202_113744:cmsbot_crab_scriptExe
240202_113747:cmsbot_crab_scriptArgs
240202_113749:cmsbot_crab_sendVenvFolder
240202_113830:cmsbot_crab_sendExternalFolder
240202_113833:cmsbot_crab_inputDBS
240202_113835:cmsbot_crab_useParent
240202_113837:cmsbot_crab_secondaryInputDataset
240202_113839:cmsbot_crab_lumiMaskFile
240202_113841:cmsbot_crab_lumiMaskUrl
240202_113844:cmsbot_crab_outLFNDirBase
240202_113846:cmsbot_crab_runRange
240202_113849:cmsbot_crab_ignoreLocality
240202_113851:cmsbot_crab_userInputFiles
240202_113853:cmsbot_crab_whitelist
240202_113856:cmsbot_crab_blacklist
240202_113858:cmsbot_crab_ignoreGlobalBlacklist
240202_113900:cmsbot_crab_voRole
240202_113902:cmsbot_crab_voGroup
240202_113904:cmsbot_crab_scheddName
240202_113907:cmsbot_crab_collector
240202_113909:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240202_113719:cmsbot_crab_20240202_123718
```

Finished at: 2024-02-02 12:40:36
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/700/console)

## Comment (cmsdmwmbot, 2024-02-02T12:02:50Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 13:02:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/740/console

```
{'TN': '240202_113912:cmsbot_crab_20240202_123911', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 989, 'failed': 9, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_113914:cmsbot_crab_20240202_123914', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_113916:cmsbot_crab_20240202_123916', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_113919:cmsbot_crab_20240202_123918', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_113921:cmsbot_crab_20240202_123920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114003:cmsbot_crab_20240202_123922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 6, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114021:cmsbot_crab_rucio_transfers_20240202_124004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114024:cmsbot_crab_rucio_transfers_group_20240202_124023', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114027:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124025', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114030:cmsbot_crab_rucio_transfers_nopublication_20240202_124028', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114033:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124031', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 34, 'running': 5, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124035', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 31, 'failed': 3, 'running': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T12:04:55Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-02-02 13:04:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/508/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/508//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-02-02T12:05:46Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 13:05:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/927/console

```
RETRY TESTS:
scriptArgs-check.sh 240202_113747:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240202_113841:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240202_113844:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240202_113846:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240202_113851:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240202_113853:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_113856:cmsbot_crab_blacklist - 2
voGroup-check.sh 240202_113902:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_113722:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_113724:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_113726:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_113729:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_113731:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_113733:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_113735:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_113738:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_113740:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_113742:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_113744:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240202_113749:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_113830:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_113833:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_113835:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_113837:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_113839:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240202_113849:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240202_113858:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_113900:cmsbot_crab_voRole - 0
scheddName-check.sh 240202_113904:cmsbot_crab_scheddName - 0
collector-check.sh 240202_113907:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_113909:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T12:19:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-02-02 13:19:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/742/console

```
{'TN': '240202_113912:cmsbot_crab_20240202_123911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 602, 'finished': 398}, 'publication (fail/tdb/DBS)': '0/300/300'}
{'TN': '240202_113914:cmsbot_crab_20240202_123914', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_113916:cmsbot_crab_20240202_123916', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_113919:cmsbot_crab_20240202_123918', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_113921:cmsbot_crab_20240202_123920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114003:cmsbot_crab_20240202_123922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114021:cmsbot_crab_rucio_transfers_20240202_124004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114024:cmsbot_crab_rucio_transfers_group_20240202_124023', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114027:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124025', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114030:cmsbot_crab_rucio_transfers_nopublication_20240202_124028', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114033:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 31, 'transferring': 9}, 'publication (fail/tdb/DBS)': '0/31/31'}
{'TN': '240202_114036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124035', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 26, 'transferring': 14}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T12:29:59Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-02-02 13:29:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/932/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_113722:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_113724:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_113726:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_113729:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_113731:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_113733:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_113735:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_113738:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_113740:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_113742:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_113744:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_113747:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_113749:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_113830:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_113833:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_113835:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_113837:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_113839:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_113841:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_113844:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_113846:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_113849:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_113851:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_113853:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_113856:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_113858:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_113900:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_113902:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_113904:cmsbot_crab_scheddName - 0
collector-check.sh 240202_113907:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_113909:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T13:06:44Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-02-02 14:06:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/744/console

```
{'TN': '240202_113912:cmsbot_crab_20240202_123911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 925, 'transferring': 75}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240202_113914:cmsbot_crab_20240202_123914', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_113916:cmsbot_crab_20240202_123916', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240202_113919:cmsbot_crab_20240202_123918', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/4/4'}
{'TN': '240202_113921:cmsbot_crab_20240202_123920', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/35/35'}
{'TN': '240202_114003:cmsbot_crab_20240202_123922', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114021:cmsbot_crab_rucio_transfers_20240202_124004', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240202_114024:cmsbot_crab_rucio_transfers_group_20240202_124023', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240202_114027:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124025', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 24, 'finished': 16}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114030:cmsbot_crab_rucio_transfers_nopublication_20240202_124028', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114033:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240202_114036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124035', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T14:37:42Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-02-02 15:37:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/746/console

```
{'TN': '240202_113912:cmsbot_crab_20240202_123911', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240202_113914:cmsbot_crab_20240202_123914', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240202_113916:cmsbot_crab_20240202_123916', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240202_113919:cmsbot_crab_20240202_123918', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240202_113921:cmsbot_crab_20240202_123920', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240202_114003:cmsbot_crab_20240202_123922', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240202_114021:cmsbot_crab_rucio_transfers_20240202_124004', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240202_114024:cmsbot_crab_rucio_transfers_group_20240202_124023', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240202_114027:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124025', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114030:cmsbot_crab_rucio_transfers_nopublication_20240202_124028', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_114033:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124031', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240202_114036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124035', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-02-02T14:46:13Z)

all OK
