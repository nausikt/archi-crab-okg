# dmwm/CRABServer issue #9004: #951: Test dev CRABClient using preprod REST instance and CMSSW_8_0_36 CMSSW release

State: closed
Opened: 2025-03-19T14:51:47Z
Closed: 2025-03-19T15:22:32Z
URL: https://github.com/dmwm/CRABServer/issues/9004

## Opening post (cmsdmwmbot, 2025-03-19T14:51:47Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_8_0_36**
- SCRAM_ARCH: **slc7_amd64_gcc530**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2025-03-19 15:51:46
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/951/)

## Comment (cmsdmwmbot, 2025-03-19T14:54:07Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_145214:cmsbot_crab_20250319_155209
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_145217:cmsbot_crab_transferOutputs
250319_145220:cmsbot_crab_transferLogs
250319_145223:cmsbot_crab_activity
250319_145228:cmsbot_crab_inputFiles
250319_145231:cmsbot_crab_disableAutomaticOutputCollection
250319_145236:cmsbot_crab_outputFiles
250319_145239:cmsbot_crab_allowUndistributedCMSSW
250319_145241:cmsbot_crab_maxMemoryMB
250319_145244:cmsbot_crab_maxJobRuntimeMin
250319_145249:cmsbot_crab_numCores
250319_145252:cmsbot_crab_scriptExe
250319_145255:cmsbot_crab_scriptArgs
250319_145300:cmsbot_crab_sendVenvFolder
250319_145305:cmsbot_crab_sendExternalFolder
250319_145306:cmsbot_crab_inputDBS
250319_145309:cmsbot_crab_useParent
250319_145313:cmsbot_crab_secondaryInputDataset
250319_145315:cmsbot_crab_lumiMaskFile
250319_145316:cmsbot_crab_lumiMaskUrl
250319_145320:cmsbot_crab_outLFNDirBase
250319_145321:cmsbot_crab_runRange
250319_145321:cmsbot_crab_ignoreLocality
250319_145322:cmsbot_crab_userInputFiles
250319_145325:cmsbot_crab_whitelist
250319_145328:cmsbot_crab_blacklist
250319_145330:cmsbot_crab_ignoreGlobalBlacklist
250319_145333:cmsbot_crab_voRole
250319_145336:cmsbot_crab_voGroup
250319_145339:cmsbot_crab_scheddName
250319_145342:cmsbot_crab_collector
250319_145345:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 15:53:45
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/951/console)

## Comment (cmsdmwmbot, 2025-03-19T15:15:16Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-03-19 16:15:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1284/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250319_145217:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250319_145220:cmsbot_crab_transferLogs - 0
activity-check.sh 250319_145223:cmsbot_crab_activity - 0
inputFiles-check.sh 250319_145228:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250319_145231:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250319_145236:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250319_145239:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250319_145241:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250319_145244:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250319_145249:cmsbot_crab_numCores - 0
scriptExe-check.sh 250319_145252:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250319_145255:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250319_145300:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250319_145305:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250319_145306:cmsbot_crab_inputDBS - 0
useParent-check.sh 250319_145309:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250319_145313:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_145315:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250319_145316:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250319_145320:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_145321:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250319_145321:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250319_145322:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_145325:cmsbot_crab_whitelist - 0
blacklist-check.sh 250319_145328:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250319_145330:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250319_145333:cmsbot_crab_voRole - 0
voGroup-check.sh 250319_145336:cmsbot_crab_voGroup - 0
scheddName-check.sh 250319_145339:cmsbot_crab_scheddName - 0
collector-check.sh 250319_145342:cmsbot_crab_collector - 0
extraJDL-check.sh 250319_145345:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```

## Comment (cmsdmwmbot, 2025-03-19T15:15:16Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-03-19 16:15:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/616/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/616//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.
