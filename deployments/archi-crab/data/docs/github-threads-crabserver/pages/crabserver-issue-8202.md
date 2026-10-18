# dmwm/CRABServer issue #8202: #686: Test GH CRABClient using test2 REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-01-30T20:19:51Z
Closed: 2024-01-31T13:58:08Z
URL: https://github.com/dmwm/CRABServer/issues/8202

## Opening post (cmsdmwmbot, 2024-01-30T20:19:51Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**
- CRABServer_tag: **HEAD**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-01-30 21:19:51
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/686/)

## Comment (cmsdmwmbot, 2024-01-30T20:21:41Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240130_202017:cmsbot_crab_transferOutputs
240130_202019:cmsbot_crab_transferLogs
240130_202020:cmsbot_crab_activity
240130_202023:cmsbot_crab_inputFiles
240130_202025:cmsbot_crab_disableAutomaticOutputCollection
240130_202028:cmsbot_crab_outputFiles
240130_202030:cmsbot_crab_allowUndistributedCMSSW
240130_202032:cmsbot_crab_maxMemoryMB
240130_202033:cmsbot_crab_maxJobRuntimeMin
240130_202036:cmsbot_crab_numCores
240130_202038:cmsbot_crab_scriptExe
240130_202040:cmsbot_crab_scriptArgs
240130_202043:cmsbot_crab_sendVenvFolder
240130_202048:cmsbot_crab_sendExternalFolder
240130_202050:cmsbot_crab_inputDBS
240130_202052:cmsbot_crab_useParent
240130_202054:cmsbot_crab_secondaryInputDataset
240130_202055:cmsbot_crab_lumiMaskFile
240130_202057:cmsbot_crab_lumiMaskUrl
240130_202100:cmsbot_crab_outLFNDirBase
240130_202102:cmsbot_crab_runRange
240130_202103:cmsbot_crab_ignoreLocality
240130_202105:cmsbot_crab_userInputFiles
240130_202107:cmsbot_crab_whitelist
240130_202109:cmsbot_crab_blacklist
240130_202110:cmsbot_crab_ignoreGlobalBlacklist
240130_202112:cmsbot_crab_voRole
240130_202114:cmsbot_crab_voGroup
240130_202116:cmsbot_crab_scheddName
240130_202118:cmsbot_crab_collector
240130_202119:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240130_202015:cmsbot_crab_20240130_212012
```

Finished at: 2024-01-30 21:21:20
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/686/console)

## Comment (cmsdmwmbot, 2024-01-30T20:45:26Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-30 21:45:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/500/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/500//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-30T20:45:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-30 21:45:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/895/console

```
RETRY TESTS:
blacklist-check.sh 240130_202109:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_202017:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_202023:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_202025:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240130_202030:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_202043:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240130_202048:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240130_202050:cmsbot_crab_inputDBS - 0
useParent-check.sh 240130_202052:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240130_202054:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 240130_202116:cmsbot_crab_scheddName - 0
collector-check.sh 240130_202118:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240130_202019:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_202020:cmsbot_crab_activity - 1
outputFiles-check.sh 240130_202028:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240130_202032:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_202033:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_202036:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_202038:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_202040:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 240130_202055:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_202057:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_202100:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_202102:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_202103:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_202105:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_202107:cmsbot_crab_whitelist - 1
ignoreGlobalBlacklist-check.sh 240130_202110:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_202112:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_202114:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_202119:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-01-30T21:15:42Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-01-30 22:15:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/899/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_202017:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_202023:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_202025:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240130_202030:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_202043:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240130_202048:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240130_202050:cmsbot_crab_inputDBS - 0
useParent-check.sh 240130_202052:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240130_202054:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 240130_202116:cmsbot_crab_scheddName - 0
collector-check.sh 240130_202118:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240130_202019:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_202020:cmsbot_crab_activity - 1
outputFiles-check.sh 240130_202028:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240130_202032:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_202033:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_202036:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_202038:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_202040:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 240130_202055:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_202057:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_202100:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_202102:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_202103:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_202105:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_202107:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_202109:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_202110:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_202112:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_202114:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_202119:cmsbot_crab_extraJDL - 1
```
