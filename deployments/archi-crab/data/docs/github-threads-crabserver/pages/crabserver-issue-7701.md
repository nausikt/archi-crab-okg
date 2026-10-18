# dmwm/CRABServer issue #7701: #411: Test prod CRABClient using test2 REST instance and CMSSW_9_4_21 CMSSW release

State: closed
Opened: 2023-06-29T20:39:51Z
Closed: 2023-06-29T22:14:23Z
URL: https://github.com/dmwm/CRABServer/issues/7701

## Opening post (cmsdmwmbot, 2023-06-29T20:39:51Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_9_4_21**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-06-29 22:39:50
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/411/)

## Comment (cmsdmwmbot, 2023-06-29T20:43:18Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_204121:cmsbot_crab_transferOutputs
230629_204124:cmsbot_crab_transferLogs
230629_204127:cmsbot_crab_activity
230629_204130:cmsbot_crab_inputFiles
230629_204133:cmsbot_crab_disableAutomaticOutputCollection
230629_204137:cmsbot_crab_outputFiles
230629_204140:cmsbot_crab_allowUndistributedCMSSW
230629_204143:cmsbot_crab_maxMemoryMB
230629_204146:cmsbot_crab_maxJobRuntimeMin
230629_204150:cmsbot_crab_numCores
230629_204153:cmsbot_crab_scriptExe
230629_204156:cmsbot_crab_scriptArgs
230629_204159:cmsbot_crab_sendPythonFolder
230629_204206:cmsbot_crab_sendExternalFolder
230629_204209:cmsbot_crab_inputDBS
230629_204212:cmsbot_crab_useParent
230629_204215:cmsbot_crab_secondaryInputDataset
230629_204218:cmsbot_crab_lumiMaskFile
230629_204221:cmsbot_crab_lumiMaskUrl
230629_204226:cmsbot_crab_outLFNDirBase
230629_204228:cmsbot_crab_runRange
230629_204231:cmsbot_crab_ignoreLocality
230629_204234:cmsbot_crab_userInputFiles
230629_204237:cmsbot_crab_whitelist
230629_204240:cmsbot_crab_blacklist
230629_204242:cmsbot_crab_ignoreGlobalBlacklist
230629_204245:cmsbot_crab_voRole
230629_204248:cmsbot_crab_voGroup
230629_204251:cmsbot_crab_scheddName
230629_204254:cmsbot_crab_collector
230629_204257:cmsbot_crab_extraJDL
```

Finished at: 2023-06-29 22:42:57
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/411/console)

## Comment (cmsdmwmbot, 2023-06-29T21:10:21Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-29 23:10:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/639/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 230629_204121:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230629_204124:cmsbot_crab_transferLogs - 1
activity-check.sh 230629_204127:cmsbot_crab_activity - 1
inputFiles-check.sh 230629_204130:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 230629_204133:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230629_204137:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 230629_204140:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 230629_204143:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230629_204146:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230629_204150:cmsbot_crab_numCores - 1
scriptExe-check.sh 230629_204153:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230629_204156:cmsbot_crab_scriptArgs - 1
sendPythonFolder-check.sh 230629_204159:cmsbot_crab_sendPythonFolder - 1
sendExternalFolder-check.sh 230629_204206:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 230629_204209:cmsbot_crab_inputDBS - 1
useParent-check.sh 230629_204212:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230629_204215:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230629_204218:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230629_204221:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230629_204226:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230629_204228:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230629_204231:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230629_204234:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230629_204237:cmsbot_crab_whitelist - 1
blacklist-check.sh 230629_204240:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230629_204242:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230629_204245:cmsbot_crab_voRole - 1
voGroup-check.sh 230629_204248:cmsbot_crab_voGroup - 1
scheddName-check.sh 230629_204251:cmsbot_crab_scheddName - 1
collector-check.sh 230629_204254:cmsbot_crab_collector - 1
extraJDL-check.sh 230629_204257:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-06-29T21:46:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 23:46:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/649/console

```
RETRY TESTS:
numCores-check.sh 230629_204150:cmsbot_crab_numCores - 2
lumiMaskFile-check.sh 230629_204218:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230629_204221:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230629_204228:cmsbot_crab_runRange - 2
whitelist-check.sh 230629_204237:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_204240:cmsbot_crab_blacklist - 2
voGroup-check.sh 230629_204248:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_204121:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_204124:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_204127:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_204130:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_204133:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_204137:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_204140:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_204143:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_204146:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230629_204153:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_204156:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_204159:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_204206:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_204209:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_204212:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_204215:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 230629_204226:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230629_204231:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_204234:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230629_204242:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_204245:cmsbot_crab_voRole - 0
scheddName-check.sh 230629_204251:cmsbot_crab_scheddName - 0
collector-check.sh 230629_204254:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_204257:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T22:13:25Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-06-30 00:13:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/654/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_204121:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_204124:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_204127:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_204130:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_204133:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_204137:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_204140:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_204143:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_204146:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_204150:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_204153:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_204156:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_204159:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_204206:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_204209:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_204212:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_204215:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_204218:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_204221:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_204226:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_204228:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_204231:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_204234:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_204237:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_204240:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_204242:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_204245:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_204248:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_204251:cmsbot_crab_scheddName - 0
collector-check.sh 230629_204254:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_204257:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-06-29T22:14:23Z)

all OK
