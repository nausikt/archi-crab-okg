# dmwm/CRABServer issue #8318: #747: Test GH CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-04T09:09:24Z
Closed: 2024-04-04T11:24:29Z
URL: https://github.com/dmwm/CRABServer/issues/8318

## Opening post (cmsdmwmbot, 2024-04-04T09:09:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-04-04 11:09:24
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/747/)

## Comment (cmsdmwmbot, 2024-04-04T09:11:10Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240404_090946:cmsbot_crab_transferOutputs
240404_090948:cmsbot_crab_transferLogs
240404_090950:cmsbot_crab_activity
240404_090952:cmsbot_crab_inputFiles
240404_090954:cmsbot_crab_disableAutomaticOutputCollection
240404_090956:cmsbot_crab_outputFiles
240404_090958:cmsbot_crab_allowUndistributedCMSSW
240404_091000:cmsbot_crab_maxMemoryMB
240404_091002:cmsbot_crab_maxJobRuntimeMin
240404_091004:cmsbot_crab_numCores
240404_091006:cmsbot_crab_scriptExe
240404_091008:cmsbot_crab_scriptArgs
240404_091010:cmsbot_crab_sendVenvFolder
240404_091013:cmsbot_crab_sendExternalFolder
240404_091015:cmsbot_crab_inputDBS
240404_091017:cmsbot_crab_useParent
240404_091019:cmsbot_crab_secondaryInputDataset
240404_091021:cmsbot_crab_lumiMaskFile
240404_091023:cmsbot_crab_lumiMaskUrl
240404_091026:cmsbot_crab_outLFNDirBase
240404_091028:cmsbot_crab_runRange
240404_091030:cmsbot_crab_ignoreLocality
240404_091032:cmsbot_crab_userInputFiles
240404_091034:cmsbot_crab_whitelist
240404_091036:cmsbot_crab_blacklist
240404_091038:cmsbot_crab_ignoreGlobalBlacklist
240404_091040:cmsbot_crab_voRole
240404_091042:cmsbot_crab_voGroup
240404_091044:cmsbot_crab_scheddName
240404_091046:cmsbot_crab_collector
240404_091048:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240404_090944:cmsbot_crab_20240404_110944
```

Finished at: 2024-04-04 11:10:49
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/747/console)

## Comment (cmsdmwmbot, 2024-04-04T09:35:45Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-04 11:35:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/522/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/522//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-04T09:39:06Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-04 11:39:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1017/console

```
RETRY TESTS:
transferLogs-check.sh 240404_090948:cmsbot_crab_transferLogs - 2
activity-check.sh 240404_090950:cmsbot_crab_activity - 2
outputFiles-check.sh 240404_090956:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240404_091000:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240404_091002:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 240404_091006:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240404_091008:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240404_091021:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240404_091023:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240404_091026:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240404_091028:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240404_091032:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240404_091034:cmsbot_crab_whitelist - 2
blacklist-check.sh 240404_091036:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240404_091038:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240404_091040:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240404_090946:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240404_090952:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240404_090954:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240404_090958:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240404_091004:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240404_091010:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240404_091013:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240404_091015:cmsbot_crab_inputDBS - 0
useParent-check.sh 240404_091017:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240404_091019:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240404_091030:cmsbot_crab_ignoreLocality - 0
voGroup-check.sh 240404_091042:cmsbot_crab_voGroup - 0
scheddName-check.sh 240404_091044:cmsbot_crab_scheddName - 0
collector-check.sh 240404_091046:cmsbot_crab_collector - 0
extraJDL-check.sh 240404_091048:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-04-04T10:04:53Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-04-04 12:04:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1019/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240404_090946:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240404_090948:cmsbot_crab_transferLogs - 0
activity-check.sh 240404_090950:cmsbot_crab_activity - 0
inputFiles-check.sh 240404_090952:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240404_090954:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240404_090956:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240404_090958:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240404_091000:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240404_091002:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240404_091004:cmsbot_crab_numCores - 0
scriptExe-check.sh 240404_091006:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240404_091008:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240404_091010:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240404_091013:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240404_091015:cmsbot_crab_inputDBS - 0
useParent-check.sh 240404_091017:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240404_091019:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240404_091021:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240404_091023:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240404_091026:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240404_091028:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240404_091030:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240404_091032:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240404_091034:cmsbot_crab_whitelist - 0
blacklist-check.sh 240404_091036:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240404_091038:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240404_091040:cmsbot_crab_voRole - 0
voGroup-check.sh 240404_091042:cmsbot_crab_voGroup - 0
scheddName-check.sh 240404_091044:cmsbot_crab_scheddName - 0
collector-check.sh 240404_091046:cmsbot_crab_collector - 0
extraJDL-check.sh 240404_091048:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-04-04T11:24:29Z)

OK
