# dmwm/CRABServer issue #7698: #407: Test prod CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-06-29T20:30:29Z
Closed: 2023-06-29T21:43:18Z
URL: https://github.com/dmwm/CRABServer/issues/7698

## Opening post (cmsdmwmbot, 2023-06-29T20:30:29Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2023-06-29 22:30:28
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/407/)

## Comment (cmsdmwmbot, 2023-06-29T20:31:55Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_203047:cmsbot_crab_transferOutputs
230629_203048:cmsbot_crab_transferLogs
230629_203049:cmsbot_crab_activity
230629_203051:cmsbot_crab_inputFiles
230629_203052:cmsbot_crab_disableAutomaticOutputCollection
230629_203053:cmsbot_crab_outputFiles
230629_203055:cmsbot_crab_allowUndistributedCMSSW
230629_203056:cmsbot_crab_maxMemoryMB
230629_203058:cmsbot_crab_maxJobRuntimeMin
230629_203059:cmsbot_crab_numCores
230629_203100:cmsbot_crab_scriptExe
230629_203102:cmsbot_crab_scriptArgs
230629_203103:cmsbot_crab_sendPythonFolder
230629_203108:cmsbot_crab_sendExternalFolder
230629_203110:cmsbot_crab_inputDBS
230629_203111:cmsbot_crab_useParent
230629_203113:cmsbot_crab_secondaryInputDataset
230629_203114:cmsbot_crab_lumiMaskFile
230629_203115:cmsbot_crab_lumiMaskUrl
230629_203118:cmsbot_crab_outLFNDirBase
230629_203119:cmsbot_crab_runRange
230629_203121:cmsbot_crab_ignoreLocality
230629_203122:cmsbot_crab_userInputFiles
230629_203123:cmsbot_crab_whitelist
230629_203125:cmsbot_crab_blacklist
230629_203126:cmsbot_crab_ignoreGlobalBlacklist
230629_203127:cmsbot_crab_voRole
230629_203129:cmsbot_crab_voGroup
230629_203130:cmsbot_crab_scheddName
230629_203131:cmsbot_crab_collector
230629_203133:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230629_203045:cmsbot_crab_20230629_223045
```

Finished at: 2023-06-29 22:31:34
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/407/console)

## Comment (cmsdmwmbot, 2023-06-29T20:52:55Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-29 22:52:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/350/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/350//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-29T20:54:56Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 22:54:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/635/console

```
RETRY TESTS:
transferLogs-check.sh 230629_203048:cmsbot_crab_transferLogs - 2
activity-check.sh 230629_203049:cmsbot_crab_activity - 2
numCores-check.sh 230629_203059:cmsbot_crab_numCores - 2
lumiMaskFile-check.sh 230629_203114:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230629_203115:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230629_203119:cmsbot_crab_runRange - 2
whitelist-check.sh 230629_203123:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_203125:cmsbot_crab_blacklist - 2
voRole-check.sh 230629_203127:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_203047:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230629_203051:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_203052:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_203053:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_203055:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_203056:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_203058:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230629_203100:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_203102:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_203103:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_203108:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_203110:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_203111:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_203113:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 230629_203118:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230629_203121:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_203122:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230629_203126:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230629_203129:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_203130:cmsbot_crab_scheddName - 0
collector-check.sh 230629_203131:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_203133:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T21:16:54Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-29 23:16:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/642/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230629_203115:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230629_203119:cmsbot_crab_runRange - 2
whitelist-check.sh 230629_203123:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_203047:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_203048:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_203049:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_203051:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_203052:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_203053:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_203055:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_203056:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_203058:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_203059:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_203100:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_203102:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_203103:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_203108:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_203110:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_203111:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_203113:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_203114:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230629_203118:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230629_203121:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_203122:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230629_203125:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_203126:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_203127:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_203129:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_203130:cmsbot_crab_scheddName - 0
collector-check.sh 230629_203131:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_203133:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T21:38:45Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-06-29 23:38:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/648/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_203047:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_203048:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_203049:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_203051:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_203052:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_203053:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_203055:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_203056:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_203058:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_203059:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_203100:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_203102:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_203103:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_203108:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_203110:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_203111:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_203113:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_203114:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_203115:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_203118:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_203119:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_203121:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_203122:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_203123:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_203125:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_203126:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_203127:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_203129:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_203130:cmsbot_crab_scheddName - 0
collector-check.sh 230629_203131:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_203133:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-06-29T21:43:18Z)

OK
