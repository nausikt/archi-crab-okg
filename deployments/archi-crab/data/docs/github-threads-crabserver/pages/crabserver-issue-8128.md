# dmwm/CRABServer issue #8128: #639: Test prod CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2023-12-19T22:20:28Z
Closed: 2023-12-20T11:25:40Z
URL: https://github.com/dmwm/CRABServer/issues/8128

## Opening post (cmsdmwmbot, 2023-12-19T22:20:28Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-19 23:20:27
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/639/)

## Comment (cmsdmwmbot, 2023-12-19T22:22:23Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_222048:cmsbot_crab_transferOutputs
231219_222050:cmsbot_crab_transferLogs
231219_222052:cmsbot_crab_activity
231219_222055:cmsbot_crab_inputFiles
231219_222057:cmsbot_crab_disableAutomaticOutputCollection
231219_222101:cmsbot_crab_outputFiles
231219_222103:cmsbot_crab_allowUndistributedCMSSW
231219_222105:cmsbot_crab_maxMemoryMB
231219_222107:cmsbot_crab_maxJobRuntimeMin
231219_222110:cmsbot_crab_numCores
231219_222113:cmsbot_crab_scriptExe
231219_222115:cmsbot_crab_scriptArgs
231219_222118:cmsbot_crab_sendVenvFolder
231219_222124:cmsbot_crab_sendExternalFolder
231219_222126:cmsbot_crab_inputDBS
231219_222128:cmsbot_crab_useParent
231219_222130:cmsbot_crab_secondaryInputDataset
231219_222133:cmsbot_crab_lumiMaskFile
231219_222135:cmsbot_crab_lumiMaskUrl
231219_222138:cmsbot_crab_outLFNDirBase
231219_222140:cmsbot_crab_runRange
231219_222142:cmsbot_crab_ignoreLocality
231219_222144:cmsbot_crab_userInputFiles
231219_222146:cmsbot_crab_whitelist
231219_222148:cmsbot_crab_blacklist
231219_222150:cmsbot_crab_ignoreGlobalBlacklist
231219_222152:cmsbot_crab_voRole
231219_222154:cmsbot_crab_voGroup
231219_222156:cmsbot_crab_scheddName
231219_222158:cmsbot_crab_collector
231219_222201:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 23:22:01
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/639/console)

## Comment (cmsdmwmbot, 2023-12-19T22:44:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 23:44:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/812/console

```
RETRY TESTS:
lumiMaskFile-check.sh 231219_222133:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 231219_222135:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231219_222140:cmsbot_crab_runRange - 2
userInputFiles-check.sh 231219_222144:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 231219_222146:cmsbot_crab_whitelist - 2
blacklist-check.sh 231219_222148:cmsbot_crab_blacklist - 2
voGroup-check.sh 231219_222154:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222048:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222050:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222052:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222055:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222057:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222101:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222103:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222105:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222107:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_222110:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_222113:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222115:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222118:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222124:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222126:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222128:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222130:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 231219_222138:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231219_222142:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 231219_222150:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222152:cmsbot_crab_voRole - 0
scheddName-check.sh 231219_222156:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222158:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222201:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:06:44Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-12-20 00:06:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/817/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222048:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222050:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222052:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222055:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222057:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222101:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222103:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222105:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222107:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_222110:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_222113:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222115:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222118:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222124:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222126:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222128:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222130:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222133:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231219_222135:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231219_222138:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222140:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222142:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222144:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222146:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_222148:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_222150:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222152:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222154:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222156:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222158:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222201:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (mapellidario, 2023-12-20T11:25:40Z)

looks good to me
