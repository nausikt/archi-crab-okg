# dmwm/CRABServer issue #9002: #948: Test dev CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2025-03-19T14:30:45Z
Closed: 2025-03-19T15:02:29Z
URL: https://github.com/dmwm/CRABServer/issues/9002

## Opening post (cmsdmwmbot, 2025-03-19T14:30:45Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2025-03-19 15:30:43
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/948/)

## Comment (cmsdmwmbot, 2025-03-19T14:32:38Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_143111:cmsbot_crab_20250319_153111
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_143113:cmsbot_crab_transferOutputs
250319_143115:cmsbot_crab_transferLogs
250319_143117:cmsbot_crab_activity
250319_143120:cmsbot_crab_inputFiles
250319_143122:cmsbot_crab_disableAutomaticOutputCollection
250319_143125:cmsbot_crab_outputFiles
250319_143127:cmsbot_crab_allowUndistributedCMSSW
250319_143129:cmsbot_crab_maxMemoryMB
250319_143131:cmsbot_crab_maxJobRuntimeMin
250319_143134:cmsbot_crab_numCores
250319_143135:cmsbot_crab_scriptExe
250319_143137:cmsbot_crab_scriptArgs
250319_143140:cmsbot_crab_sendVenvFolder
250319_143144:cmsbot_crab_sendExternalFolder
250319_143145:cmsbot_crab_inputDBS
250319_143147:cmsbot_crab_useParent
250319_143149:cmsbot_crab_secondaryInputDataset
250319_143151:cmsbot_crab_lumiMaskFile
250319_143153:cmsbot_crab_lumiMaskUrl
250319_143155:cmsbot_crab_outLFNDirBase
250319_143157:cmsbot_crab_runRange
250319_143159:cmsbot_crab_ignoreLocality
250319_143201:cmsbot_crab_userInputFiles
250319_143203:cmsbot_crab_whitelist
250319_143204:cmsbot_crab_blacklist
250319_143206:cmsbot_crab_ignoreGlobalBlacklist
250319_143208:cmsbot_crab_voRole
250319_143210:cmsbot_crab_voGroup
250319_143212:cmsbot_crab_scheddName
250319_143214:cmsbot_crab_collector
250319_143216:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 15:32:16
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/948/console)

## Comment (cmsdmwmbot, 2025-03-19T14:56:33Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-03-19 15:56:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/614/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/614//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-03-19T14:58:57Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-03-19 15:58:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1282/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250319_143113:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250319_143115:cmsbot_crab_transferLogs - 0
activity-check.sh 250319_143117:cmsbot_crab_activity - 0
inputFiles-check.sh 250319_143120:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250319_143122:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250319_143125:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250319_143127:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250319_143129:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250319_143131:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250319_143134:cmsbot_crab_numCores - 0
scriptExe-check.sh 250319_143135:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250319_143137:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250319_143140:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250319_143144:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250319_143145:cmsbot_crab_inputDBS - 0
useParent-check.sh 250319_143147:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250319_143149:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_143151:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250319_143153:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250319_143155:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_143157:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250319_143159:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250319_143201:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_143203:cmsbot_crab_whitelist - 0
blacklist-check.sh 250319_143204:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250319_143206:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250319_143208:cmsbot_crab_voRole - 0
voGroup-check.sh 250319_143210:cmsbot_crab_voGroup - 0
scheddName-check.sh 250319_143212:cmsbot_crab_scheddName - 0
collector-check.sh 250319_143214:cmsbot_crab_collector - 0
extraJDL-check.sh 250319_143216:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```
