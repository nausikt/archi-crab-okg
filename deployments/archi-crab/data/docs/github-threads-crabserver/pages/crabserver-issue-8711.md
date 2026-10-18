# dmwm/CRABServer issue #8711: #836: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-20T16:21:11Z
Closed: 2024-09-23T21:04:24Z
URL: https://github.com/dmwm/CRABServer/issues/8711

## Opening post (cmsdmwmbot, 2024-09-20T16:21:11Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-09-20 18:21:10
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/836/)

## Comment (cmsdmwmbot, 2024-09-20T16:23:08Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240920_162129:cmsbot_crab_transferOutputs
240920_162131:cmsbot_crab_transferLogs
240920_162134:cmsbot_crab_activity
240920_162137:cmsbot_crab_inputFiles
240920_162139:cmsbot_crab_disableAutomaticOutputCollection
240920_162142:cmsbot_crab_outputFiles
240920_162144:cmsbot_crab_allowUndistributedCMSSW
240920_162147:cmsbot_crab_maxMemoryMB
240920_162149:cmsbot_crab_maxJobRuntimeMin
240920_162152:cmsbot_crab_numCores
240920_162155:cmsbot_crab_scriptExe
240920_162157:cmsbot_crab_scriptArgs
240920_162200:cmsbot_crab_sendVenvFolder
240920_162202:cmsbot_crab_sendExternalFolder
240920_162205:cmsbot_crab_inputDBS
240920_162208:cmsbot_crab_useParent
240920_162210:cmsbot_crab_secondaryInputDataset
240920_162213:cmsbot_crab_lumiMaskFile
240920_162215:cmsbot_crab_lumiMaskUrl
240920_162219:cmsbot_crab_outLFNDirBase
240920_162221:cmsbot_crab_runRange
240920_162223:cmsbot_crab_ignoreLocality
240920_162226:cmsbot_crab_userInputFiles
240920_162228:cmsbot_crab_whitelist
240920_162231:cmsbot_crab_blacklist
240920_162233:cmsbot_crab_ignoreGlobalBlacklist
240920_162236:cmsbot_crab_voRole
240920_162238:cmsbot_crab_voGroup
240920_162241:cmsbot_crab_scheddName
240920_162243:cmsbot_crab_collector
240920_162246:cmsbot_crab_extraJDL
```

Finished at: 2024-09-20 18:22:47
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/836/console)

## Comment (cmsdmwmbot, 2024-09-20T16:47:45Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-20 18:47:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1175/console

```
RETRY TESTS:
activity-check.sh 240920_162134:cmsbot_crab_activity - 2
outputFiles-check.sh 240920_162142:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240920_162149:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 240920_162155:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240920_162215:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240920_162219:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240920_162221:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240920_162223:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 240920_162226:cmsbot_crab_userInputFiles - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_162129:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240920_162137:cmsbot_crab_inputFiles - 0
sendVenvFolder-check.sh 240920_162200:cmsbot_crab_sendVenvFolder - 0
scheddName-check.sh 240920_162241:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240920_162246:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferLogs-check.sh 240920_162131:cmsbot_crab_transferLogs - 1
disableAutomaticOutputCollection-check.sh 240920_162139:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240920_162144:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240920_162147:cmsbot_crab_maxMemoryMB - 1
numCores-check.sh 240920_162152:cmsbot_crab_numCores - 1
scriptArgs-check.sh 240920_162157:cmsbot_crab_scriptArgs - 1
sendExternalFolder-check.sh 240920_162202:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240920_162205:cmsbot_crab_inputDBS - 1
useParent-check.sh 240920_162208:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_162210:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_162213:cmsbot_crab_lumiMaskFile - 1
whitelist-check.sh 240920_162228:cmsbot_crab_whitelist - 1
blacklist-check.sh 240920_162231:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_162233:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240920_162236:cmsbot_crab_voRole - 1
voGroup-check.sh 240920_162238:cmsbot_crab_voGroup - 1
collector-check.sh 240920_162243:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-09-20T17:11:53Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-09-20 19:11:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1178/console

```
RETRY TESTS:
outLFNDirBase-check.sh 240920_162219:cmsbot_crab_outLFNDirBase - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_162129:cmsbot_crab_transferOutputs - 0
activity-check.sh 240920_162134:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_162137:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 240920_162142:cmsbot_crab_outputFiles - 0
maxJobRuntimeMin-check.sh 240920_162149:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240920_162155:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240920_162200:cmsbot_crab_sendVenvFolder - 0
lumiMaskUrl-check.sh 240920_162215:cmsbot_crab_lumiMaskUrl - 0
runRange-check.sh 240920_162221:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240920_162223:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_162226:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240920_162241:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240920_162246:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferLogs-check.sh 240920_162131:cmsbot_crab_transferLogs - 1
disableAutomaticOutputCollection-check.sh 240920_162139:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240920_162144:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240920_162147:cmsbot_crab_maxMemoryMB - 1
numCores-check.sh 240920_162152:cmsbot_crab_numCores - 1
scriptArgs-check.sh 240920_162157:cmsbot_crab_scriptArgs - 1
sendExternalFolder-check.sh 240920_162202:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240920_162205:cmsbot_crab_inputDBS - 1
useParent-check.sh 240920_162208:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_162210:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_162213:cmsbot_crab_lumiMaskFile - 1
whitelist-check.sh 240920_162228:cmsbot_crab_whitelist - 1
blacklist-check.sh 240920_162231:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_162233:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240920_162236:cmsbot_crab_voRole - 1
voGroup-check.sh 240920_162238:cmsbot_crab_voGroup - 1
collector-check.sh 240920_162243:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-09-20T17:35:50Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-09-20 19:35:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1181/console

```
RETRY TESTS:
outLFNDirBase-check.sh 240920_162219:cmsbot_crab_outLFNDirBase - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_162129:cmsbot_crab_transferOutputs - 0
activity-check.sh 240920_162134:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_162137:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 240920_162142:cmsbot_crab_outputFiles - 0
maxJobRuntimeMin-check.sh 240920_162149:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240920_162155:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240920_162200:cmsbot_crab_sendVenvFolder - 0
lumiMaskUrl-check.sh 240920_162215:cmsbot_crab_lumiMaskUrl - 0
runRange-check.sh 240920_162221:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240920_162223:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_162226:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240920_162241:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240920_162246:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferLogs-check.sh 240920_162131:cmsbot_crab_transferLogs - 1
disableAutomaticOutputCollection-check.sh 240920_162139:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240920_162144:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240920_162147:cmsbot_crab_maxMemoryMB - 1
numCores-check.sh 240920_162152:cmsbot_crab_numCores - 1
scriptArgs-check.sh 240920_162157:cmsbot_crab_scriptArgs - 1
sendExternalFolder-check.sh 240920_162202:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240920_162205:cmsbot_crab_inputDBS - 1
useParent-check.sh 240920_162208:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_162210:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_162213:cmsbot_crab_lumiMaskFile - 1
whitelist-check.sh 240920_162228:cmsbot_crab_whitelist - 1
blacklist-check.sh 240920_162231:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_162233:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240920_162236:cmsbot_crab_voRole - 1
voGroup-check.sh 240920_162238:cmsbot_crab_voGroup - 1
collector-check.sh 240920_162243:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-09-20T17:59:54Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-09-20 19:59:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1184/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_162129:cmsbot_crab_transferOutputs - 0
activity-check.sh 240920_162134:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_162137:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 240920_162142:cmsbot_crab_outputFiles - 0
maxJobRuntimeMin-check.sh 240920_162149:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240920_162155:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240920_162200:cmsbot_crab_sendVenvFolder - 0
lumiMaskUrl-check.sh 240920_162215:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_162219:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240920_162221:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240920_162223:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_162226:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240920_162241:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240920_162246:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferLogs-check.sh 240920_162131:cmsbot_crab_transferLogs - 1
disableAutomaticOutputCollection-check.sh 240920_162139:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240920_162144:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240920_162147:cmsbot_crab_maxMemoryMB - 1
numCores-check.sh 240920_162152:cmsbot_crab_numCores - 1
scriptArgs-check.sh 240920_162157:cmsbot_crab_scriptArgs - 1
sendExternalFolder-check.sh 240920_162202:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240920_162205:cmsbot_crab_inputDBS - 1
useParent-check.sh 240920_162208:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_162210:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_162213:cmsbot_crab_lumiMaskFile - 1
whitelist-check.sh 240920_162228:cmsbot_crab_whitelist - 1
blacklist-check.sh 240920_162231:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_162233:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240920_162236:cmsbot_crab_voRole - 1
voGroup-check.sh 240920_162238:cmsbot_crab_voGroup - 1
collector-check.sh 240920_162243:cmsbot_crab_collector - 1
```
