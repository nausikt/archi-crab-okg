# dmwm/CRABServer issue #8563: #816: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-07-25T13:18:07Z
Closed: 2024-07-26T10:19:07Z
URL: https://github.com/dmwm/CRABServer/issues/8563

## Opening post (cmsdmwmbot, 2024-07-25T13:18:07Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-07-25 15:18:06
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/816/)

## Comment (cmsdmwmbot, 2024-07-25T13:21:14Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240725_132004:cmsbot_crab_20240725_152004
240725_132006:cmsbot_crab_20240725_152006
240725_132008:cmsbot_crab_20240725_152008
240725_132010:cmsbot_crab_20240725_152010
240725_132012:cmsbot_crab_20240725_152012
240725_132038:cmsbot_crab_20240725_152014
240725_132040:cmsbot_crab_rucio_transfers_20240725_152039
240725_132042:cmsbot_crab_rucio_transfers_group_20240725_152042
240725_132045:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240725_152044
240725_132048:cmsbot_crab_rucio_transfers_nopublication_20240725_152046
240725_132050:cmsbot_crab_rucio_transfers_withnoneedm_20240725_152049
240725_132053:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240725_152052
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240725_131859:cmsbot_crab_transferOutputs
240725_131901:cmsbot_crab_transferLogs
240725_131903:cmsbot_crab_activity
240725_131905:cmsbot_crab_inputFiles
240725_131907:cmsbot_crab_disableAutomaticOutputCollection
240725_131910:cmsbot_crab_outputFiles
240725_131912:cmsbot_crab_allowUndistributedCMSSW
240725_131914:cmsbot_crab_maxMemoryMB
240725_131916:cmsbot_crab_maxJobRuntimeMin
240725_131918:cmsbot_crab_numCores
240725_131920:cmsbot_crab_scriptExe
240725_131922:cmsbot_crab_scriptArgs
240725_131924:cmsbot_crab_sendVenvFolder
240725_131926:cmsbot_crab_sendExternalFolder
240725_131928:cmsbot_crab_inputDBS
240725_131930:cmsbot_crab_useParent
240725_131933:cmsbot_crab_secondaryInputDataset
240725_131935:cmsbot_crab_lumiMaskFile
240725_131937:cmsbot_crab_lumiMaskUrl
240725_131940:cmsbot_crab_outLFNDirBase
240725_131942:cmsbot_crab_runRange
240725_131944:cmsbot_crab_ignoreLocality
240725_131946:cmsbot_crab_userInputFiles
240725_131948:cmsbot_crab_whitelist
240725_131950:cmsbot_crab_blacklist
240725_131952:cmsbot_crab_ignoreGlobalBlacklist
240725_131954:cmsbot_crab_voRole
240725_131956:cmsbot_crab_voGroup
240725_131958:cmsbot_crab_scheddName
240725_132000:cmsbot_crab_collector
240725_132001:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240725_131847:cmsbot_crab_20240725_151846
```

Finished at: 2024-07-25 15:20:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/816/console)

## Comment (cmsdmwmbot, 2024-07-25T13:42:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-07-25 15:42:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1032/console

```
{'TN': '240725_132004:cmsbot_crab_20240725_152004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 995, 'idle': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132006:cmsbot_crab_20240725_152006', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132008:cmsbot_crab_20240725_152008', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132010:cmsbot_crab_20240725_152010', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132012:cmsbot_crab_20240725_152012', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132038:cmsbot_crab_20240725_152014', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132040:cmsbot_crab_rucio_transfers_20240725_152039', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132042:cmsbot_crab_rucio_transfers_group_20240725_152042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132045:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240725_152044', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132048:cmsbot_crab_rucio_transfers_nopublication_20240725_152046', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132050:cmsbot_crab_rucio_transfers_withnoneedm_20240725_152049', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132053:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240725_152052', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-07-25T13:44:18Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-07-25 15:44:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/543/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/543//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-07-25T13:45:22Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-07-25 15:45:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1139/console

```
RETRY TESTS:
numCores-check.sh 240725_131918:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240725_131922:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240725_131935:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240725_131937:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240725_131940:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240725_131942:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240725_131946:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240725_131948:cmsbot_crab_whitelist - 2
blacklist-check.sh 240725_131950:cmsbot_crab_blacklist - 2
voGroup-check.sh 240725_131956:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240725_131859:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240725_131901:cmsbot_crab_transferLogs - 0
activity-check.sh 240725_131903:cmsbot_crab_activity - 0
inputFiles-check.sh 240725_131905:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240725_131907:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240725_131910:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240725_131912:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240725_131914:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240725_131916:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240725_131920:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240725_131924:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240725_131926:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240725_131928:cmsbot_crab_inputDBS - 0
useParent-check.sh 240725_131930:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240725_131933:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240725_131944:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240725_131952:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240725_131954:cmsbot_crab_voRole - 0
scheddName-check.sh 240725_131958:cmsbot_crab_scheddName - 0
collector-check.sh 240725_132000:cmsbot_crab_collector - 0
extraJDL-check.sh 240725_132001:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-07-25T13:58:21Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-07-25 15:58:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1033/console

```
{'TN': '240725_132004:cmsbot_crab_20240725_152004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'idle': 1, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/300'}
{'TN': '240725_132006:cmsbot_crab_20240725_152006', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132008:cmsbot_crab_20240725_152008', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/1'}
{'TN': '240725_132010:cmsbot_crab_20240725_152010', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/5'}
{'TN': '240725_132012:cmsbot_crab_20240725_152012', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/76'}
{'TN': '240725_132038:cmsbot_crab_20240725_152014', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132040:cmsbot_crab_rucio_transfers_20240725_152039', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132042:cmsbot_crab_rucio_transfers_group_20240725_152042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132045:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240725_152044', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132048:cmsbot_crab_rucio_transfers_nopublication_20240725_152046', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132050:cmsbot_crab_rucio_transfers_withnoneedm_20240725_152049', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132053:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240725_152052', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-07-25T14:09:52Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-07-25 16:09:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1140/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240725_131859:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240725_131901:cmsbot_crab_transferLogs - 0
activity-check.sh 240725_131903:cmsbot_crab_activity - 0
inputFiles-check.sh 240725_131905:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240725_131907:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240725_131910:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240725_131912:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240725_131914:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240725_131916:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240725_131918:cmsbot_crab_numCores - 0
scriptExe-check.sh 240725_131920:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240725_131922:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240725_131924:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240725_131926:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240725_131928:cmsbot_crab_inputDBS - 0
useParent-check.sh 240725_131930:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240725_131933:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240725_131935:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240725_131937:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240725_131940:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240725_131942:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240725_131944:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240725_131946:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240725_131948:cmsbot_crab_whitelist - 0
blacklist-check.sh 240725_131950:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240725_131952:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240725_131954:cmsbot_crab_voRole - 0
voGroup-check.sh 240725_131956:cmsbot_crab_voGroup - 0
scheddName-check.sh 240725_131958:cmsbot_crab_scheddName - 0
collector-check.sh 240725_132000:cmsbot_crab_collector - 0
extraJDL-check.sh 240725_132001:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-07-25T14:44:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-07-25 16:44:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1034/console

```
{'TN': '240725_132004:cmsbot_crab_20240725_152004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'transferring': 1, 'running': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240725_132006:cmsbot_crab_20240725_152006', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132008:cmsbot_crab_20240725_152008', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240725_132010:cmsbot_crab_20240725_152010', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240725_132012:cmsbot_crab_20240725_152012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240725_132038:cmsbot_crab_20240725_152014', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240725_132040:cmsbot_crab_rucio_transfers_20240725_152039', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132042:cmsbot_crab_rucio_transfers_group_20240725_152042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132045:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240725_152044', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132048:cmsbot_crab_rucio_transfers_nopublication_20240725_152046', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132050:cmsbot_crab_rucio_transfers_withnoneedm_20240725_152049', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132053:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240725_152052', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-07-25T16:17:40Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-07-25 18:17:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1035/console

```
{'TN': '240725_132004:cmsbot_crab_20240725_152004', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 999, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/999/999'}
{'TN': '240725_132006:cmsbot_crab_20240725_152006', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240725_132008:cmsbot_crab_20240725_152008', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240725_132010:cmsbot_crab_20240725_152010', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240725_132012:cmsbot_crab_20240725_152012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240725_132038:cmsbot_crab_20240725_152014', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240725_132040:cmsbot_crab_rucio_transfers_20240725_152039', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132042:cmsbot_crab_rucio_transfers_group_20240725_152042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132045:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240725_152044', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132048:cmsbot_crab_rucio_transfers_nopublication_20240725_152046', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132050:cmsbot_crab_rucio_transfers_withnoneedm_20240725_152049', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132053:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240725_152052', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-07-25T18:19:46Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-07-25 20:19:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1036/console

```
{'TN': '240725_132004:cmsbot_crab_20240725_152004', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240725_132006:cmsbot_crab_20240725_152006', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240725_132008:cmsbot_crab_20240725_152008', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240725_132010:cmsbot_crab_20240725_152010', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240725_132012:cmsbot_crab_20240725_152012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240725_132038:cmsbot_crab_20240725_152014', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240725_132040:cmsbot_crab_rucio_transfers_20240725_152039', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132042:cmsbot_crab_rucio_transfers_group_20240725_152042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132045:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240725_152044', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132048:cmsbot_crab_rucio_transfers_nopublication_20240725_152046', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132050:cmsbot_crab_rucio_transfers_withnoneedm_20240725_152049', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132053:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240725_152052', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-07-25T20:21:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-07-25 22:21:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1037/console

```
{'TN': '240725_132004:cmsbot_crab_20240725_152004', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240725_132006:cmsbot_crab_20240725_152006', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240725_132008:cmsbot_crab_20240725_152008', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240725_132010:cmsbot_crab_20240725_152010', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240725_132012:cmsbot_crab_20240725_152012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240725_132038:cmsbot_crab_20240725_152014', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240725_132040:cmsbot_crab_rucio_transfers_20240725_152039', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132042:cmsbot_crab_rucio_transfers_group_20240725_152042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132045:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240725_152044', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132048:cmsbot_crab_rucio_transfers_nopublication_20240725_152046', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132050:cmsbot_crab_rucio_transfers_withnoneedm_20240725_152049', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240725_132053:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240725_152052', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-07-26T10:19:07Z)

Rucio took longer, but eventually all OK
