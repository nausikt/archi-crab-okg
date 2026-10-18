# dmwm/CRABServer issue #8177: #677: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-12T14:38:07Z
Closed: 2024-01-13T09:41:38Z
URL: https://github.com/dmwm/CRABServer/issues/8177

## Opening post (cmsdmwmbot, 2024-01-12T14:38:07Z)

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

Started at: 2024-01-12 15:38:06
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/677/)

## Comment (cmsdmwmbot, 2024-01-12T14:41:51Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240112_144056:cmsbot_crab_20240112_154055
240112_144058:cmsbot_crab_20240112_154057
240112_144100:cmsbot_crab_20240112_154100
240112_144102:cmsbot_crab_20240112_154102
240112_144105:cmsbot_crab_20240112_154104
240112_144111:cmsbot_crab_20240112_154106
240112_144114:cmsbot_crab_rucio_transfers_20240112_154112
240112_144116:cmsbot_crab_rucio_transfers_group_20240112_154116
240112_144120:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_154118
240112_144123:cmsbot_crab_rucio_transfers_nopublication_20240112_154121
240112_144126:cmsbot_crab_rucio_transfers_withnoneedm_20240112_154125
240112_144130:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_154128
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240112_143842:cmsbot_crab_transferOutputs
240112_143844:cmsbot_crab_transferLogs
240112_143847:cmsbot_crab_activity
240112_143850:cmsbot_crab_inputFiles
240112_143852:cmsbot_crab_disableAutomaticOutputCollection
240112_143854:cmsbot_crab_outputFiles
240112_143856:cmsbot_crab_allowUndistributedCMSSW
240112_143858:cmsbot_crab_maxMemoryMB
240112_143901:cmsbot_crab_maxJobRuntimeMin
240112_143903:cmsbot_crab_numCores
240112_143905:cmsbot_crab_scriptExe
240112_143907:cmsbot_crab_scriptArgs
240112_143910:cmsbot_crab_sendVenvFolder
240112_143953:cmsbot_crab_sendExternalFolder
240112_143955:cmsbot_crab_inputDBS
240112_143957:cmsbot_crab_useParent
240112_143959:cmsbot_crab_secondaryInputDataset
240112_144002:cmsbot_crab_lumiMaskFile
240112_144004:cmsbot_crab_lumiMaskUrl
240112_144028:cmsbot_crab_outLFNDirBase
240112_144030:cmsbot_crab_runRange
240112_144033:cmsbot_crab_ignoreLocality
240112_144035:cmsbot_crab_userInputFiles
240112_144037:cmsbot_crab_whitelist
240112_144039:cmsbot_crab_blacklist
240112_144041:cmsbot_crab_ignoreGlobalBlacklist
240112_144043:cmsbot_crab_voRole
240112_144046:cmsbot_crab_voGroup
240112_144048:cmsbot_crab_scheddName
240112_144050:cmsbot_crab_collector
240112_144052:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240112_143840:cmsbot_crab_20240112_153839
```

Finished at: 2024-01-12 15:41:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/677/console)

## Comment (cmsdmwmbot, 2024-01-12T15:02:43Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-12 16:02:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/705/console

```
{'TN': '240112_144056:cmsbot_crab_20240112_154055', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 982, 'running': 18}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144058:cmsbot_crab_20240112_154057', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144100:cmsbot_crab_20240112_154100', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144102:cmsbot_crab_20240112_154102', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144105:cmsbot_crab_20240112_154104', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144111:cmsbot_crab_20240112_154106', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144114:cmsbot_crab_rucio_transfers_20240112_154112', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144116:cmsbot_crab_rucio_transfers_group_20240112_154116', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144120:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_154118', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144123:cmsbot_crab_rucio_transfers_nopublication_20240112_154121', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144126:cmsbot_crab_rucio_transfers_withnoneedm_20240112_154125', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144130:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_154128', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T15:05:35Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-12 16:05:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/495/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/495//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-12T15:06:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-12 16:06:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/885/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 240112_143959:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240112_144004:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240112_144028:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240112_144030:cmsbot_crab_runRange - 2
whitelist-check.sh 240112_144037:cmsbot_crab_whitelist - 2
blacklist-check.sh 240112_144039:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240112_144041:cmsbot_crab_ignoreGlobalBlacklist - 2
voGroup-check.sh 240112_144046:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240112_143842:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240112_143844:cmsbot_crab_transferLogs - 0
activity-check.sh 240112_143847:cmsbot_crab_activity - 0
inputFiles-check.sh 240112_143850:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240112_143852:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240112_143854:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240112_143856:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240112_143858:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240112_143901:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240112_143903:cmsbot_crab_numCores - 0
scriptExe-check.sh 240112_143905:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240112_143907:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240112_143910:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240112_143953:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240112_143955:cmsbot_crab_inputDBS - 0
useParent-check.sh 240112_143957:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 240112_144002:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240112_144033:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240112_144035:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240112_144043:cmsbot_crab_voRole - 0
scheddName-check.sh 240112_144048:cmsbot_crab_scheddName - 0
collector-check.sh 240112_144050:cmsbot_crab_collector - 0
extraJDL-check.sh 240112_144052:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-12T15:18:39Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-01-12 16:18:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/706/console

```
{'TN': '240112_144056:cmsbot_crab_20240112_154055', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 182, 'finished': 811, 'running': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144058:cmsbot_crab_20240112_154057', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144100:cmsbot_crab_20240112_154100', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144102:cmsbot_crab_20240112_154102', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 2, 'finished': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144105:cmsbot_crab_20240112_154104', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144111:cmsbot_crab_20240112_154106', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144114:cmsbot_crab_rucio_transfers_20240112_154112', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144116:cmsbot_crab_rucio_transfers_group_20240112_154116', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144120:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_154118', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144123:cmsbot_crab_rucio_transfers_nopublication_20240112_154121', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144126:cmsbot_crab_rucio_transfers_withnoneedm_20240112_154125', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144130:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_154128', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 28, 'transferring': 12}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T15:30:51Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-01-12 16:30:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/886/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240112_143842:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240112_143844:cmsbot_crab_transferLogs - 0
activity-check.sh 240112_143847:cmsbot_crab_activity - 0
inputFiles-check.sh 240112_143850:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240112_143852:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240112_143854:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240112_143856:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240112_143858:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240112_143901:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240112_143903:cmsbot_crab_numCores - 0
scriptExe-check.sh 240112_143905:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240112_143907:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240112_143910:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240112_143953:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240112_143955:cmsbot_crab_inputDBS - 0
useParent-check.sh 240112_143957:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240112_143959:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240112_144002:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240112_144004:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240112_144028:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240112_144030:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240112_144033:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240112_144035:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240112_144037:cmsbot_crab_whitelist - 0
blacklist-check.sh 240112_144039:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240112_144041:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240112_144043:cmsbot_crab_voRole - 0
voGroup-check.sh 240112_144046:cmsbot_crab_voGroup - 0
scheddName-check.sh 240112_144048:cmsbot_crab_scheddName - 0
collector-check.sh 240112_144050:cmsbot_crab_collector - 0
extraJDL-check.sh 240112_144052:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-12T16:04:45Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-01-12 17:04:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/709/console

```
{'TN': '240112_144056:cmsbot_crab_20240112_154055', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 996, 'transferring': 4}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240112_144058:cmsbot_crab_20240112_154057', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_144100:cmsbot_crab_20240112_154100', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_144102:cmsbot_crab_20240112_154102', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_144105:cmsbot_crab_20240112_154104', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240112_144111:cmsbot_crab_20240112_154106', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_144114:cmsbot_crab_rucio_transfers_20240112_154112', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '240112_144116:cmsbot_crab_rucio_transfers_group_20240112_154116', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144120:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_154118', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144123:cmsbot_crab_rucio_transfers_nopublication_20240112_154121', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144126:cmsbot_crab_rucio_transfers_withnoneedm_20240112_154125', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240112_144130:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_154128', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T17:38:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-01-12 18:38:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/712/console

```
{'TN': '240112_144056:cmsbot_crab_20240112_154055', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240112_144058:cmsbot_crab_20240112_154057', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_144100:cmsbot_crab_20240112_154100', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_144102:cmsbot_crab_20240112_154102', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_144105:cmsbot_crab_20240112_154104', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240112_144111:cmsbot_crab_20240112_154106', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_144114:cmsbot_crab_rucio_transfers_20240112_154112', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240112_144116:cmsbot_crab_rucio_transfers_group_20240112_154116', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144120:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_154118', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144123:cmsbot_crab_rucio_transfers_nopublication_20240112_154121', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144126:cmsbot_crab_rucio_transfers_withnoneedm_20240112_154125', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240112_144130:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_154128', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T19:41:24Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-01-12 20:41:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/715/console

```
{'TN': '240112_144056:cmsbot_crab_20240112_154055', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240112_144058:cmsbot_crab_20240112_154057', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_144100:cmsbot_crab_20240112_154100', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_144102:cmsbot_crab_20240112_154102', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_144105:cmsbot_crab_20240112_154104', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240112_144111:cmsbot_crab_20240112_154106', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_144114:cmsbot_crab_rucio_transfers_20240112_154112', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240112_144116:cmsbot_crab_rucio_transfers_group_20240112_154116', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144120:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_154118', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144123:cmsbot_crab_rucio_transfers_nopublication_20240112_154121', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144126:cmsbot_crab_rucio_transfers_withnoneedm_20240112_154125', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240112_144130:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_154128', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T21:43:21Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-01-12 22:43:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/718/console

```
{'TN': '240112_144056:cmsbot_crab_20240112_154055', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240112_144058:cmsbot_crab_20240112_154057', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_144100:cmsbot_crab_20240112_154100', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_144102:cmsbot_crab_20240112_154102', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_144105:cmsbot_crab_20240112_154104', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240112_144111:cmsbot_crab_20240112_154106', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_144114:cmsbot_crab_rucio_transfers_20240112_154112', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240112_144116:cmsbot_crab_rucio_transfers_group_20240112_154116', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144120:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_154118', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144123:cmsbot_crab_rucio_transfers_nopublication_20240112_154121', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_144126:cmsbot_crab_rucio_transfers_withnoneedm_20240112_154125', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240112_144130:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_154128', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-01-13T09:40:30Z)

OK. the last task fails to transfer becasuse cmsbot can not authenticate for crab_test Rucio group account
```
rucio.common.exception.CannotAuthenticate: Cannot authenticate.
Details: Cannot authenticate to account crab_test_group with given credentials

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "task_process/RUCIO_Transfers.py", line 10, in <module>
    main()
  File "/data/srv/glidecondor/condor_local/spool/1655/0/cluster9481655.proc0.subproc0/CRAB3.zip/ASO/Rucio/Main.py", line 111, in main
```

Either was not confiured properly or the config. was lost somehow.
We'll follow up with Rahul
