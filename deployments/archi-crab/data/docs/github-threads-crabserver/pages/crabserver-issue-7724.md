# dmwm/CRABServer issue #7724: #425: Test prod CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-07-07T16:29:32Z
Closed: 2023-07-07T19:38:12Z
URL: https://github.com/dmwm/CRABServer/issues/7724

## Opening post (cmsdmwmbot, 2023-07-07T16:29:32Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-07-07 18:29:31
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/425/)

## Comment (cmsdmwmbot, 2023-07-07T16:33:29Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230707_163231:cmsbot_crab_20230707_183228
230707_163233:cmsbot_crab_20230707_183231
230707_163236:cmsbot_crab_20230707_183234
230707_163239:cmsbot_crab_20230707_183236
230707_163241:cmsbot_crab_20230707_183239
230707_163307:cmsbot_crab_20230707_183242
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230707_163058:cmsbot_crab_transferOutputs
230707_163101:cmsbot_crab_transferLogs
230707_163104:cmsbot_crab_activity
230707_163106:cmsbot_crab_inputFiles
230707_163109:cmsbot_crab_disableAutomaticOutputCollection
230707_163112:cmsbot_crab_outputFiles
230707_163115:cmsbot_crab_allowUndistributedCMSSW
230707_163117:cmsbot_crab_maxMemoryMB
230707_163120:cmsbot_crab_maxJobRuntimeMin
230707_163123:cmsbot_crab_numCores
230707_163126:cmsbot_crab_scriptExe
230707_163129:cmsbot_crab_scriptArgs
230707_163131:cmsbot_crab_sendPythonFolder
230707_163139:cmsbot_crab_sendExternalFolder
230707_163142:cmsbot_crab_inputDBS
230707_163144:cmsbot_crab_useParent
230707_163147:cmsbot_crab_secondaryInputDataset
230707_163150:cmsbot_crab_lumiMaskFile
230707_163153:cmsbot_crab_lumiMaskUrl
230707_163157:cmsbot_crab_outLFNDirBase
230707_163200:cmsbot_crab_runRange
230707_163202:cmsbot_crab_ignoreLocality
230707_163205:cmsbot_crab_userInputFiles
230707_163208:cmsbot_crab_whitelist
230707_163211:cmsbot_crab_blacklist
230707_163214:cmsbot_crab_ignoreGlobalBlacklist
230707_163216:cmsbot_crab_voRole
230707_163219:cmsbot_crab_voGroup
230707_163222:cmsbot_crab_scheddName
230707_163225:cmsbot_crab_collector
230707_163228:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230707_163055:cmsbot_crab_20230707_183051
```

Finished at: 2023-07-07 18:33:08
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/425/console)

## Comment (cmsdmwmbot, 2023-07-07T16:56:34Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-07 18:56:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/360/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/360//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-07T16:58:02Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 18:58:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/679/console

```
RETRY TESTS:
disableAutomaticOutputCollection-check.sh 230707_163109:cmsbot_crab_disableAutomaticOutputCollection - 2
maxMemoryMB-check.sh 230707_163117:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230707_163120:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230707_163123:cmsbot_crab_numCores - 2
scriptExe-check.sh 230707_163126:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230707_163129:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 230707_163153:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230707_163157:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230707_163200:cmsbot_crab_runRange - 2
whitelist-check.sh 230707_163208:cmsbot_crab_whitelist - 2
blacklist-check.sh 230707_163211:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163058:cmsbot_crab_transferOutputs - 0
activity-check.sh 230707_163104:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163106:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 230707_163112:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163115:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230707_163131:cmsbot_crab_sendPythonFolder - 0
inputDBS-check.sh 230707_163142:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163144:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163147:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 230707_163202:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230707_163214:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163216:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163219:cmsbot_crab_voGroup - 0
collector-check.sh 230707_163225:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163228:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferLogs-check.sh 230707_163101:cmsbot_crab_transferLogs - 1
sendExternalFolder-check.sh 230707_163139:cmsbot_crab_sendExternalFolder - 1
lumiMaskFile-check.sh 230707_163150:cmsbot_crab_lumiMaskFile - 1
userInputFiles-check.sh 230707_163205:cmsbot_crab_userInputFiles - 1
scheddName-check.sh 230707_163222:cmsbot_crab_scheddName - 1
```

## Comment (cmsdmwmbot, 2023-07-07T17:23:12Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-07 19:23:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/683/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 230707_163120:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230707_163123:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230707_163153:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230707_163200:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163058:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163101:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163104:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163106:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163109:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163112:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163115:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163117:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 230707_163126:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163129:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163131:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163139:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163142:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163144:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163147:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163150:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_163157:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_163202:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163205:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163208:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163211:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163214:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163216:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163219:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163222:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163225:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163228:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T17:35:36Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 19:35:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/470/console

```
{'TN': '230707_163231:cmsbot_crab_20230707_183228', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 998, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163233:cmsbot_crab_20230707_183231', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163236:cmsbot_crab_20230707_183234', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163239:cmsbot_crab_20230707_183236', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163241:cmsbot_crab_20230707_183239', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163307:cmsbot_crab_20230707_183242', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-07T17:48:27Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-07 19:48:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/688/console

```
RETRY TESTS:
runRange-check.sh 230707_163200:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163058:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163101:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163104:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163106:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163109:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163112:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163115:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163117:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163120:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163123:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163126:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163129:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163131:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163139:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163142:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163144:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163147:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163150:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_163153:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_163157:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_163202:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163205:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163208:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163211:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163214:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163216:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163219:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163222:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163225:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163228:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T18:13:36Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-07 20:13:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/693/console

```
RETRY TESTS:
runRange-check.sh 230707_163200:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163058:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163101:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163104:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163106:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163109:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163112:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163115:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163117:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163120:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163123:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163126:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163129:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163131:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163139:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163142:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163144:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163147:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163150:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_163153:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_163157:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_163202:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163205:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163208:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163211:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163214:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163216:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163219:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163222:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163225:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163228:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T18:38:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-07 20:38:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/697/console

```
RETRY TESTS:
runRange-check.sh 230707_163200:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163058:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163101:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163104:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163106:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163109:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163112:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163115:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163117:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163120:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163123:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163126:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163129:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163131:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163139:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163142:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163144:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163147:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163150:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_163153:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_163157:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_163202:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163205:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163208:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163211:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163214:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163216:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163219:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163222:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163225:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163228:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T18:39:28Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-07-07 20:39:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/475/console

```
{'TN': '230707_163231:cmsbot_crab_20230707_183228', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163233:cmsbot_crab_20230707_183231', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163236:cmsbot_crab_20230707_183234', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163239:cmsbot_crab_20230707_183236', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163241:cmsbot_crab_20230707_183239', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163307:cmsbot_crab_20230707_183242', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-07-07T19:37:32Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 0. Test is done.
**Finished at:** 2023-07-07 21:37:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/699/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163058:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163101:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163104:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163106:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163109:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163112:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163115:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163117:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163120:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163123:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163126:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163129:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163131:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163139:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163142:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163144:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163147:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163150:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_163153:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_163157:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_163200:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_163202:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163205:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163208:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163211:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163214:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163216:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163219:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163222:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163225:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163228:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-07-07T19:38:12Z)

all OK
