# dmwm/CRABServer issue #9001: #947: Test dev CRABClient using preprod REST instance and CMSSW_12_5_0 CMSSW release

State: closed
Opened: 2025-03-19T14:27:54Z
Closed: 2025-03-19T15:20:04Z
URL: https://github.com/dmwm/CRABServer/issues/9001

## Opening post (cmsdmwmbot, 2025-03-19T14:27:54Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_5_0**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2025-03-19 15:27:53
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/947/)

## Comment (cmsdmwmbot, 2025-03-19T14:30:35Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_142828:cmsbot_crab_20250319_152825
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_142832:cmsbot_crab_transferOutputs
250319_142835:cmsbot_crab_transferLogs
250319_142838:cmsbot_crab_activity
250319_142842:cmsbot_crab_inputFiles
250319_142845:cmsbot_crab_disableAutomaticOutputCollection
250319_142850:cmsbot_crab_outputFiles
250319_142853:cmsbot_crab_allowUndistributedCMSSW
250319_142856:cmsbot_crab_maxMemoryMB
250319_142859:cmsbot_crab_maxJobRuntimeMin
250319_142903:cmsbot_crab_numCores
250319_142906:cmsbot_crab_scriptExe
250319_142910:cmsbot_crab_scriptArgs
250319_142914:cmsbot_crab_sendVenvFolder
250319_142918:cmsbot_crab_sendExternalFolder
250319_142921:cmsbot_crab_inputDBS
250319_142925:cmsbot_crab_useParent
250319_142928:cmsbot_crab_secondaryInputDataset
250319_142931:cmsbot_crab_lumiMaskFile
250319_142934:cmsbot_crab_lumiMaskUrl
250319_142938:cmsbot_crab_outLFNDirBase
250319_142941:cmsbot_crab_runRange
250319_142945:cmsbot_crab_ignoreLocality
250319_142948:cmsbot_crab_userInputFiles
250319_142951:cmsbot_crab_whitelist
250319_142954:cmsbot_crab_blacklist
250319_142957:cmsbot_crab_ignoreGlobalBlacklist
250319_143000:cmsbot_crab_voRole
250319_143003:cmsbot_crab_voGroup
250319_143007:cmsbot_crab_scheddName
250319_143010:cmsbot_crab_collector
250319_143013:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 15:30:13
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/947/console)

## Comment (cmsdmwmbot, 2025-03-19T14:53:45Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-03-19 15:53:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/613/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/613//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-03-19T14:55:23Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-03-19 15:55:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1281/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250319_142832:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250319_142835:cmsbot_crab_transferLogs - 0
activity-check.sh 250319_142838:cmsbot_crab_activity - 0
inputFiles-check.sh 250319_142842:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250319_142845:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250319_142850:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250319_142853:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250319_142856:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250319_142859:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250319_142903:cmsbot_crab_numCores - 0
scriptExe-check.sh 250319_142906:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250319_142910:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250319_142914:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250319_142918:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250319_142921:cmsbot_crab_inputDBS - 0
useParent-check.sh 250319_142925:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250319_142928:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_142931:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250319_142934:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250319_142938:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_142941:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250319_142945:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250319_142948:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_142951:cmsbot_crab_whitelist - 0
blacklist-check.sh 250319_142954:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250319_142957:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250319_143000:cmsbot_crab_voRole - 0
voGroup-check.sh 250319_143003:cmsbot_crab_voGroup - 0
scheddName-check.sh 250319_143007:cmsbot_crab_scheddName - 0
collector-check.sh 250319_143010:cmsbot_crab_collector - 0
extraJDL-check.sh 250319_143013:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```
