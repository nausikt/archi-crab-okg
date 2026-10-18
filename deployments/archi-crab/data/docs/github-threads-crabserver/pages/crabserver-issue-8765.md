# dmwm/CRABServer issue #8765: #868: Test GH CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-04T11:40:13Z
Closed: 2024-11-04T13:58:07Z
URL: https://github.com/dmwm/CRABServer/issues/8765

## Opening post (cmsdmwmbot, 2024-11-04T11:40:13Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **v3.241030**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-11-04 12:40:12
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/868/)

## Comment (cmsdmwmbot, 2024-11-04T11:42:52Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241104_114038:cmsbot_crab_transferOutputs
241104_114043:cmsbot_crab_transferLogs
241104_114047:cmsbot_crab_activity
241104_114052:cmsbot_crab_inputFiles
241104_114056:cmsbot_crab_disableAutomaticOutputCollection
241104_114101:cmsbot_crab_outputFiles
241104_114105:cmsbot_crab_allowUndistributedCMSSW
241104_114109:cmsbot_crab_maxMemoryMB
241104_114113:cmsbot_crab_maxJobRuntimeMin
241104_114117:cmsbot_crab_numCores
241104_114120:cmsbot_crab_scriptExe
241104_114124:cmsbot_crab_scriptArgs
241104_114128:cmsbot_crab_sendVenvFolder
241104_114131:cmsbot_crab_sendExternalFolder
241104_114135:cmsbot_crab_inputDBS
241104_114138:cmsbot_crab_useParent
241104_114142:cmsbot_crab_secondaryInputDataset
241104_114145:cmsbot_crab_lumiMaskFile
241104_114149:cmsbot_crab_lumiMaskUrl
241104_114153:cmsbot_crab_outLFNDirBase
241104_114156:cmsbot_crab_runRange
241104_114200:cmsbot_crab_ignoreLocality
241104_114203:cmsbot_crab_userInputFiles
241104_114207:cmsbot_crab_whitelist
241104_114210:cmsbot_crab_blacklist
241104_114213:cmsbot_crab_ignoreGlobalBlacklist
241104_114217:cmsbot_crab_voRole
241104_114220:cmsbot_crab_voGroup
241104_114223:cmsbot_crab_scheddName
241104_114227:cmsbot_crab_collector
241104_114230:cmsbot_crab_extraJDL
```

Finished at: 2024-11-04 12:42:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/868/console)

## Comment (cmsdmwmbot, 2024-11-04T12:06:58Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-04 13:06:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1219/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 241104_114142:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 241104_114149:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 241104_114156:cmsbot_crab_runRange - 2
whitelist-check.sh 241104_114207:cmsbot_crab_whitelist - 2
blacklist-check.sh 241104_114210:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241104_114213:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241104_114217:cmsbot_crab_voRole - 2
voGroup-check.sh 241104_114220:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241104_114038:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241104_114043:cmsbot_crab_transferLogs - 0
activity-check.sh 241104_114047:cmsbot_crab_activity - 0
inputFiles-check.sh 241104_114052:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241104_114056:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241104_114101:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241104_114105:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241104_114109:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241104_114113:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241104_114117:cmsbot_crab_numCores - 0
scriptExe-check.sh 241104_114120:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241104_114124:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241104_114128:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241104_114131:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241104_114135:cmsbot_crab_inputDBS - 0
useParent-check.sh 241104_114138:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 241104_114145:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 241104_114153:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 241104_114200:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241104_114203:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 241104_114223:cmsbot_crab_scheddName - 0
collector-check.sh 241104_114227:cmsbot_crab_collector - 0
extraJDL-check.sh 241104_114230:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-04T12:31:04Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-04 13:30:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1220/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241104_114038:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241104_114043:cmsbot_crab_transferLogs - 0
activity-check.sh 241104_114047:cmsbot_crab_activity - 0
inputFiles-check.sh 241104_114052:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241104_114056:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241104_114101:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241104_114105:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241104_114109:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241104_114113:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241104_114117:cmsbot_crab_numCores - 0
scriptExe-check.sh 241104_114120:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241104_114124:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241104_114128:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241104_114131:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241104_114135:cmsbot_crab_inputDBS - 0
useParent-check.sh 241104_114138:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241104_114142:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241104_114145:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241104_114149:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241104_114153:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241104_114156:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241104_114200:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241104_114203:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241104_114207:cmsbot_crab_whitelist - 0
blacklist-check.sh 241104_114210:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241104_114213:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241104_114217:cmsbot_crab_voRole - 0
voGroup-check.sh 241104_114220:cmsbot_crab_voGroup - 0
scheddName-check.sh 241104_114223:cmsbot_crab_scheddName - 0
collector-check.sh 241104_114227:cmsbot_crab_collector - 0
extraJDL-check.sh 241104_114230:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-11-04T13:58:08Z)

OK
