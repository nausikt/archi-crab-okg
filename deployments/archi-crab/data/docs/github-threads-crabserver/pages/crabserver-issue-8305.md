# dmwm/CRABServer issue #8305: #737: Test prod CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2024-03-26T15:19:46Z
Closed: 2024-03-26T19:38:22Z
URL: https://github.com/dmwm/CRABServer/issues/8305

## Opening post (cmsdmwmbot, 2024-03-26T15:19:46Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-03-26 16:19:46
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/737/)

## Comment (cmsdmwmbot, 2024-03-26T15:22:11Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240326_152118:cmsbot_crab_20240326_162117
240326_152120:cmsbot_crab_20240326_162119
240326_152122:cmsbot_crab_20240326_162122
240326_152124:cmsbot_crab_20240326_162124
240326_152126:cmsbot_crab_20240326_162126
240326_152130:cmsbot_crab_20240326_162128
240326_152133:cmsbot_crab_rucio_transfers_20240326_162132
240326_152135:cmsbot_crab_rucio_transfers_group_20240326_162135
240326_152139:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162137
240326_152142:cmsbot_crab_rucio_transfers_nopublication_20240326_162140
240326_152145:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162144
240326_152149:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162147
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240326_152006:cmsbot_crab_transferOutputs
240326_152009:cmsbot_crab_transferLogs
240326_152011:cmsbot_crab_activity
240326_152013:cmsbot_crab_inputFiles
240326_152015:cmsbot_crab_disableAutomaticOutputCollection
240326_152017:cmsbot_crab_outputFiles
240326_152019:cmsbot_crab_allowUndistributedCMSSW
240326_152021:cmsbot_crab_maxMemoryMB
240326_152023:cmsbot_crab_maxJobRuntimeMin
240326_152025:cmsbot_crab_numCores
240326_152028:cmsbot_crab_scriptExe
240326_152030:cmsbot_crab_scriptArgs
240326_152032:cmsbot_crab_sendVenvFolder
240326_152038:cmsbot_crab_sendExternalFolder
240326_152040:cmsbot_crab_inputDBS
240326_152042:cmsbot_crab_useParent
240326_152044:cmsbot_crab_secondaryInputDataset
240326_152046:cmsbot_crab_lumiMaskFile
240326_152049:cmsbot_crab_lumiMaskUrl
240326_152052:cmsbot_crab_outLFNDirBase
240326_152054:cmsbot_crab_runRange
240326_152056:cmsbot_crab_ignoreLocality
240326_152058:cmsbot_crab_userInputFiles
240326_152100:cmsbot_crab_whitelist
240326_152102:cmsbot_crab_blacklist
240326_152104:cmsbot_crab_ignoreGlobalBlacklist
240326_152106:cmsbot_crab_voRole
240326_152109:cmsbot_crab_voGroup
240326_152111:cmsbot_crab_scheddName
240326_152113:cmsbot_crab_collector
240326_152115:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240326_152004:cmsbot_crab_20240326_162004
```

Finished at: 2024-03-26 16:21:49
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/737/console)

## Comment (cmsdmwmbot, 2024-03-26T15:43:22Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-26 16:43:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/840/console

```
{'TN': '240326_152118:cmsbot_crab_20240326_162117', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152120:cmsbot_crab_20240326_162119', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 2, 'finished': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152122:cmsbot_crab_20240326_162122', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152124:cmsbot_crab_20240326_162124', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152126:cmsbot_crab_20240326_162126', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152130:cmsbot_crab_20240326_162128', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152133:cmsbot_crab_rucio_transfers_20240326_162132', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152135:cmsbot_crab_rucio_transfers_group_20240326_162135', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152139:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162137', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152142:cmsbot_crab_rucio_transfers_nopublication_20240326_162140', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152145:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162144', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152149:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T15:47:38Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-03-26 16:47:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/515/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/515//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-03-26T15:48:49Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-26 16:48:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/993/console

```
RETRY TESTS:
numCores-check.sh 240326_152025:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240326_152049:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240326_152052:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240326_152054:cmsbot_crab_runRange - 2
whitelist-check.sh 240326_152100:cmsbot_crab_whitelist - 2
blacklist-check.sh 240326_152102:cmsbot_crab_blacklist - 2
voRole-check.sh 240326_152106:cmsbot_crab_voRole - 2
voGroup-check.sh 240326_152109:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_152006:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_152009:cmsbot_crab_transferLogs - 0
activity-check.sh 240326_152011:cmsbot_crab_activity - 0
inputFiles-check.sh 240326_152013:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_152015:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240326_152017:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240326_152019:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240326_152021:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240326_152023:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240326_152028:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240326_152030:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240326_152032:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_152038:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_152040:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_152042:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_152044:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_152046:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240326_152056:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240326_152058:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240326_152104:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240326_152111:cmsbot_crab_scheddName - 0
collector-check.sh 240326_152113:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_152115:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-26T15:59:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-26 16:59:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/843/console

```
{'TN': '240326_152118:cmsbot_crab_20240326_162117', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152120:cmsbot_crab_20240326_162119', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152122:cmsbot_crab_20240326_162122', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152124:cmsbot_crab_20240326_162124', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152126:cmsbot_crab_20240326_162126', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152130:cmsbot_crab_20240326_162128', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152133:cmsbot_crab_rucio_transfers_20240326_162132', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152135:cmsbot_crab_rucio_transfers_group_20240326_162135', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152139:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162137', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152142:cmsbot_crab_rucio_transfers_nopublication_20240326_162140', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152145:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162144', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152149:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T16:13:06Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-03-26 17:13:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/996/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_152006:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_152009:cmsbot_crab_transferLogs - 0
activity-check.sh 240326_152011:cmsbot_crab_activity - 0
inputFiles-check.sh 240326_152013:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_152015:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240326_152017:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240326_152019:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240326_152021:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240326_152023:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240326_152025:cmsbot_crab_numCores - 0
scriptExe-check.sh 240326_152028:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240326_152030:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240326_152032:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_152038:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_152040:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_152042:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_152044:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_152046:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240326_152049:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240326_152052:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240326_152054:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240326_152056:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240326_152058:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240326_152100:cmsbot_crab_whitelist - 0
blacklist-check.sh 240326_152102:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240326_152104:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240326_152106:cmsbot_crab_voRole - 0
voGroup-check.sh 240326_152109:cmsbot_crab_voGroup - 0
scheddName-check.sh 240326_152111:cmsbot_crab_scheddName - 0
collector-check.sh 240326_152113:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_152115:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-26T16:45:45Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-26 17:45:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/846/console

```
{'TN': '240326_152118:cmsbot_crab_20240326_162117', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240326_152120:cmsbot_crab_20240326_162119', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240326_152122:cmsbot_crab_20240326_162122', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240326_152124:cmsbot_crab_20240326_162124', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240326_152126:cmsbot_crab_20240326_162126', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240326_152130:cmsbot_crab_20240326_162128', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240326_152133:cmsbot_crab_rucio_transfers_20240326_162132', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_152135:cmsbot_crab_rucio_transfers_group_20240326_162135', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_152139:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162137', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152142:cmsbot_crab_rucio_transfers_nopublication_20240326_162140', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152145:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162144', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_152149:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162147', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T18:19:48Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-03-26 19:19:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/849/console

```
{'TN': '240326_152118:cmsbot_crab_20240326_162117', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240326_152120:cmsbot_crab_20240326_162119', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240326_152122:cmsbot_crab_20240326_162122', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240326_152124:cmsbot_crab_20240326_162124', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240326_152126:cmsbot_crab_20240326_162126', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240326_152130:cmsbot_crab_20240326_162128', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240326_152133:cmsbot_crab_rucio_transfers_20240326_162132', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_152135:cmsbot_crab_rucio_transfers_group_20240326_162135', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_152139:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162137', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152142:cmsbot_crab_rucio_transfers_nopublication_20240326_162140', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_152145:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162144', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_152149:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162147', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-03-26T19:38:22Z)

All OK
