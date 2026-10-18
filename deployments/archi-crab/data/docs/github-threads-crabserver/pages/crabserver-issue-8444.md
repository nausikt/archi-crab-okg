# dmwm/CRABServer issue #8444: #785: Test GH CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-29T13:19:39Z
Closed: 2024-05-29T20:00:56Z
URL: https://github.com/dmwm/CRABServer/issues/8444

## Opening post (cmsdmwmbot, 2024-05-29T13:19:39Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-05-29 15:19:38
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/785/)

## Comment (cmsdmwmbot, 2024-05-29T13:22:16Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240529_132112:cmsbot_crab_20240529_152112
240529_132114:cmsbot_crab_20240529_152114
240529_132116:cmsbot_crab_20240529_152115
240529_132118:cmsbot_crab_20240529_152117
240529_132120:cmsbot_crab_20240529_152119
240529_132137:cmsbot_crab_20240529_152121
240529_132140:cmsbot_crab_rucio_transfers_20240529_152139
240529_132143:cmsbot_crab_rucio_transfers_group_20240529_152142
240529_132146:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_152144
240529_132149:cmsbot_crab_rucio_transfers_nopublication_20240529_152147
240529_132152:cmsbot_crab_rucio_transfers_withnoneedm_20240529_152150
240529_132155:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_152153
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240529_132002:cmsbot_crab_transferOutputs
240529_132010:cmsbot_crab_transferLogs
240529_132012:cmsbot_crab_activity
240529_132014:cmsbot_crab_inputFiles
240529_132016:cmsbot_crab_disableAutomaticOutputCollection
240529_132018:cmsbot_crab_outputFiles
240529_132020:cmsbot_crab_allowUndistributedCMSSW
240529_132022:cmsbot_crab_maxMemoryMB
240529_132024:cmsbot_crab_maxJobRuntimeMin
240529_132026:cmsbot_crab_numCores
240529_132028:cmsbot_crab_scriptExe
240529_132030:cmsbot_crab_scriptArgs
240529_132032:cmsbot_crab_sendVenvFolder
240529_132035:cmsbot_crab_sendExternalFolder
240529_132036:cmsbot_crab_inputDBS
240529_132038:cmsbot_crab_useParent
240529_132040:cmsbot_crab_secondaryInputDataset
240529_132042:cmsbot_crab_lumiMaskFile
240529_132044:cmsbot_crab_lumiMaskUrl
240529_132048:cmsbot_crab_outLFNDirBase
240529_132050:cmsbot_crab_runRange
240529_132052:cmsbot_crab_ignoreLocality
240529_132054:cmsbot_crab_userInputFiles
240529_132056:cmsbot_crab_whitelist
240529_132058:cmsbot_crab_blacklist
240529_132100:cmsbot_crab_ignoreGlobalBlacklist
240529_132102:cmsbot_crab_voRole
240529_132104:cmsbot_crab_voGroup
240529_132106:cmsbot_crab_scheddName
240529_132108:cmsbot_crab_collector
240529_132110:cmsbot_crab_extraJDL
```

Finished at: 2024-05-29 15:21:55
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/785/console)

## Comment (cmsdmwmbot, 2024-05-29T13:43:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-29 15:43:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/940/console

```
{'TN': '240529_132112:cmsbot_crab_20240529_152112', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 826, 'running': 164, 'idle': 2, 'unsubmitted': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132114:cmsbot_crab_20240529_152114', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 4, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132116:cmsbot_crab_20240529_152115', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132118:cmsbot_crab_20240529_152117', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 8, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132120:cmsbot_crab_20240529_152119', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 7, 'transferring': 93}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132137:cmsbot_crab_20240529_152121', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 8, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132140:cmsbot_crab_rucio_transfers_20240529_152139', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132143:cmsbot_crab_rucio_transfers_group_20240529_152142', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132146:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_152144', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132149:cmsbot_crab_rucio_transfers_nopublication_20240529_152147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132152:cmsbot_crab_rucio_transfers_withnoneedm_20240529_152150', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132155:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_152153', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-29T13:46:17Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-29 15:46:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1074/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240529_132024:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240529_132026:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240529_132044:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240529_132050:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240529_132054:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240529_132056:cmsbot_crab_whitelist - 2
blacklist-check.sh 240529_132058:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240529_132002:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240529_132010:cmsbot_crab_transferLogs - 0
activity-check.sh 240529_132012:cmsbot_crab_activity - 0
inputFiles-check.sh 240529_132014:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240529_132016:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240529_132018:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240529_132020:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240529_132022:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240529_132028:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240529_132030:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240529_132032:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240529_132035:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240529_132036:cmsbot_crab_inputDBS - 0
useParent-check.sh 240529_132038:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240529_132040:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240529_132042:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240529_132048:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240529_132052:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240529_132100:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240529_132102:cmsbot_crab_voRole - 0
voGroup-check.sh 240529_132104:cmsbot_crab_voGroup - 0
scheddName-check.sh 240529_132106:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240529_132110:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240529_132108:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-05-29T13:59:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-05-29 15:59:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/941/console

```
{'TN': '240529_132112:cmsbot_crab_20240529_152112', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 980, 'running': 18, 'idle': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132114:cmsbot_crab_20240529_152114', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132116:cmsbot_crab_20240529_152115', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132118:cmsbot_crab_20240529_152117', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132120:cmsbot_crab_20240529_152119', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132137:cmsbot_crab_20240529_152121', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 1, 'transferring': 9}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132140:cmsbot_crab_rucio_transfers_20240529_152139', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132143:cmsbot_crab_rucio_transfers_group_20240529_152142', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132146:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_152144', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132149:cmsbot_crab_rucio_transfers_nopublication_20240529_152147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132152:cmsbot_crab_rucio_transfers_withnoneedm_20240529_152150', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132155:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_152153', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-29T14:10:31Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-05-29 16:10:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1075/console

```
RETRY TESTS:
runRange-check.sh 240529_132050:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240529_132002:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240529_132010:cmsbot_crab_transferLogs - 0
activity-check.sh 240529_132012:cmsbot_crab_activity - 0
inputFiles-check.sh 240529_132014:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240529_132016:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240529_132018:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240529_132020:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240529_132022:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240529_132024:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240529_132026:cmsbot_crab_numCores - 0
scriptExe-check.sh 240529_132028:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240529_132030:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240529_132032:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240529_132035:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240529_132036:cmsbot_crab_inputDBS - 0
useParent-check.sh 240529_132038:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240529_132040:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240529_132042:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240529_132044:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240529_132048:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240529_132052:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240529_132054:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240529_132056:cmsbot_crab_whitelist - 0
blacklist-check.sh 240529_132058:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240529_132100:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240529_132102:cmsbot_crab_voRole - 0
voGroup-check.sh 240529_132104:cmsbot_crab_voGroup - 0
scheddName-check.sh 240529_132106:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240529_132110:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240529_132108:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-05-29T14:34:49Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-05-29 16:34:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1076/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240529_132002:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240529_132010:cmsbot_crab_transferLogs - 0
activity-check.sh 240529_132012:cmsbot_crab_activity - 0
inputFiles-check.sh 240529_132014:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240529_132016:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240529_132018:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240529_132020:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240529_132022:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240529_132024:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240529_132026:cmsbot_crab_numCores - 0
scriptExe-check.sh 240529_132028:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240529_132030:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240529_132032:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240529_132035:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240529_132036:cmsbot_crab_inputDBS - 0
useParent-check.sh 240529_132038:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240529_132040:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240529_132042:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240529_132044:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240529_132048:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240529_132050:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240529_132052:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240529_132054:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240529_132056:cmsbot_crab_whitelist - 0
blacklist-check.sh 240529_132058:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240529_132100:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240529_132102:cmsbot_crab_voRole - 0
voGroup-check.sh 240529_132104:cmsbot_crab_voGroup - 0
scheddName-check.sh 240529_132106:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240529_132110:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240529_132108:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-05-29T14:45:36Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-05-29 16:45:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/942/console

```
{'TN': '240529_132112:cmsbot_crab_20240529_152112', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 983, 'running': 2, 'failed': 14, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240529_132114:cmsbot_crab_20240529_152114', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132116:cmsbot_crab_20240529_152115', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240529_132118:cmsbot_crab_20240529_152117', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240529_132120:cmsbot_crab_20240529_152119', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240529_132137:cmsbot_crab_20240529_152121', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'failed': 1, 'finished': 9}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240529_132140:cmsbot_crab_rucio_transfers_20240529_152139', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_132143:cmsbot_crab_rucio_transfers_group_20240529_152142', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_132146:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_152144', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132149:cmsbot_crab_rucio_transfers_nopublication_20240529_152147', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132152:cmsbot_crab_rucio_transfers_withnoneedm_20240529_152150', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_132155:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_152153', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-05-29T15:38:06Z)

collector test is the known problem

## Comment (cmsdmwmbot, 2024-05-29T16:20:16Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-05-29 18:20:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/943/console

```
{'TN': '240529_132112:cmsbot_crab_20240529_152112', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 998, 'failed': 2}, 'publication (fail/tdb/DBS)': '0/998/998'}
{'TN': '240529_132114:cmsbot_crab_20240529_152114', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240529_132116:cmsbot_crab_20240529_152115', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240529_132118:cmsbot_crab_20240529_152117', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240529_132120:cmsbot_crab_20240529_152119', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240529_132137:cmsbot_crab_20240529_152121', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240529_132140:cmsbot_crab_rucio_transfers_20240529_152139', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_132143:cmsbot_crab_rucio_transfers_group_20240529_152142', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_132146:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_152144', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132149:cmsbot_crab_rucio_transfers_nopublication_20240529_152147', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132152:cmsbot_crab_rucio_transfers_withnoneedm_20240529_152150', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_132155:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_152153', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-29T18:22:19Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 4 out of 5. Test is done.
**Finished at:** 2024-05-29 20:22:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/944/console

```
{'TN': '240529_132112:cmsbot_crab_20240529_152112', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240529_132114:cmsbot_crab_20240529_152114', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240529_132116:cmsbot_crab_20240529_152115', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240529_132118:cmsbot_crab_20240529_152117', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240529_132120:cmsbot_crab_20240529_152119', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240529_132137:cmsbot_crab_20240529_152121', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240529_132140:cmsbot_crab_rucio_transfers_20240529_152139', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_132143:cmsbot_crab_rucio_transfers_group_20240529_152142', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_132146:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_152144', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132149:cmsbot_crab_rucio_transfers_nopublication_20240529_152147', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_132152:cmsbot_crab_rucio_transfers_withnoneedm_20240529_152150', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_132155:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_152153', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-05-29T20:00:56Z)

All OK.
