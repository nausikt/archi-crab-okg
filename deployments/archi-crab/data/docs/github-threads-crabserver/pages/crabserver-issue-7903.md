# dmwm/CRABServer issue #7903: #477: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-10-09T14:10:12Z
Closed: 2023-10-09T19:35:52Z
URL: https://github.com/dmwm/CRABServer/issues/7903

## Opening post (cmsdmwmbot, 2023-10-09T14:10:12Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-10-09 16:10:11
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/477/)

## Comment (cmsdmwmbot, 2023-10-09T14:12:27Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231009_141036:cmsbot_crab_transferOutputs
231009_141038:cmsbot_crab_transferLogs
231009_141039:cmsbot_crab_activity
231009_141041:cmsbot_crab_inputFiles
231009_141042:cmsbot_crab_disableAutomaticOutputCollection
231009_141044:cmsbot_crab_outputFiles
231009_141045:cmsbot_crab_allowUndistributedCMSSW
231009_141046:cmsbot_crab_maxMemoryMB
231009_141048:cmsbot_crab_maxJobRuntimeMin
231009_141049:cmsbot_crab_numCores
231009_141050:cmsbot_crab_scriptExe
231009_141052:cmsbot_crab_scriptArgs
231009_141053:cmsbot_crab_sendPythonFolder
231009_141140:cmsbot_crab_sendExternalFolder
231009_141141:cmsbot_crab_inputDBS
231009_141143:cmsbot_crab_useParent
231009_141144:cmsbot_crab_secondaryInputDataset
231009_141146:cmsbot_crab_lumiMaskFile
231009_141147:cmsbot_crab_lumiMaskUrl
231009_141149:cmsbot_crab_outLFNDirBase
231009_141151:cmsbot_crab_runRange
231009_141152:cmsbot_crab_ignoreLocality
231009_141153:cmsbot_crab_userInputFiles
231009_141155:cmsbot_crab_whitelist
231009_141156:cmsbot_crab_blacklist
231009_141158:cmsbot_crab_ignoreGlobalBlacklist
231009_141159:cmsbot_crab_voRole
231009_141201:cmsbot_crab_voGroup
231009_141202:cmsbot_crab_scheddName
231009_141204:cmsbot_crab_collector
231009_141205:cmsbot_crab_extraJDL
```

Finished at: 2023-10-09 16:12:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/477/console)

## Comment (cmsdmwmbot, 2023-10-09T14:35:17Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-10-09 16:35:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/786/console

```
RETRY TESTS:
activity-check.sh 231009_141039:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 231009_141046:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 231009_141048:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskUrl-check.sh 231009_141147:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231009_141151:cmsbot_crab_runRange - 2
whitelist-check.sh 231009_141155:cmsbot_crab_whitelist - 2
blacklist-check.sh 231009_141156:cmsbot_crab_blacklist - 2
voRole-check.sh 231009_141159:cmsbot_crab_voRole - 2
voGroup-check.sh 231009_141201:cmsbot_crab_voGroup - 2
extraJDL-check.sh 231009_141205:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231009_141036:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231009_141038:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 231009_141041:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231009_141042:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231009_141044:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231009_141045:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 231009_141049:cmsbot_crab_numCores - 0
scriptExe-check.sh 231009_141050:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231009_141052:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 231009_141053:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 231009_141140:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231009_141141:cmsbot_crab_inputDBS - 0
useParent-check.sh 231009_141143:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231009_141144:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231009_141146:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231009_141149:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231009_141152:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231009_141153:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231009_141158:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 231009_141202:cmsbot_crab_scheddName - 0
collector-check.sh 231009_141204:cmsbot_crab_collector - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-10-09T14:57:56Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-10-09 16:57:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/788/console

```
RETRY TESTS:
voRole-check.sh 231009_141159:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231009_141036:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231009_141038:cmsbot_crab_transferLogs - 0
activity-check.sh 231009_141039:cmsbot_crab_activity - 0
inputFiles-check.sh 231009_141041:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231009_141042:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231009_141044:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231009_141045:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231009_141046:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231009_141048:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231009_141049:cmsbot_crab_numCores - 0
scriptExe-check.sh 231009_141050:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231009_141052:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 231009_141053:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 231009_141140:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231009_141141:cmsbot_crab_inputDBS - 0
useParent-check.sh 231009_141143:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231009_141144:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231009_141146:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231009_141147:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231009_141149:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231009_141151:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231009_141152:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231009_141153:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231009_141155:cmsbot_crab_whitelist - 0
blacklist-check.sh 231009_141156:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231009_141158:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 231009_141201:cmsbot_crab_voGroup - 0
scheddName-check.sh 231009_141202:cmsbot_crab_scheddName - 0
collector-check.sh 231009_141204:cmsbot_crab_collector - 0
extraJDL-check.sh 231009_141205:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-10-09T15:20:03Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-10-09 17:20:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/790/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231009_141036:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231009_141038:cmsbot_crab_transferLogs - 0
activity-check.sh 231009_141039:cmsbot_crab_activity - 0
inputFiles-check.sh 231009_141041:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231009_141042:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231009_141044:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231009_141045:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231009_141046:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231009_141048:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231009_141049:cmsbot_crab_numCores - 0
scriptExe-check.sh 231009_141050:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231009_141052:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 231009_141053:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 231009_141140:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231009_141141:cmsbot_crab_inputDBS - 0
useParent-check.sh 231009_141143:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231009_141144:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231009_141146:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231009_141147:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231009_141149:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231009_141151:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231009_141152:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231009_141153:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231009_141155:cmsbot_crab_whitelist - 0
blacklist-check.sh 231009_141156:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231009_141158:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231009_141159:cmsbot_crab_voRole - 0
voGroup-check.sh 231009_141201:cmsbot_crab_voGroup - 0
scheddName-check.sh 231009_141202:cmsbot_crab_scheddName - 0
collector-check.sh 231009_141204:cmsbot_crab_collector - 0
extraJDL-check.sh 231009_141205:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
