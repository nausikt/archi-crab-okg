# dmwm/CRABServer issue #8997: #943: Test dev CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2025-03-19T11:40:48Z
Closed: 2025-03-19T14:30:56Z
URL: https://github.com/dmwm/CRABServer/issues/8997

## Opening post (cmsdmwmbot, 2025-03-19T11:40:48Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2025-03-19 12:40:46
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/943/)

## Comment (cmsdmwmbot, 2025-03-19T11:43:27Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_114123:cmsbot_crab_20250319_124121
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_114127:cmsbot_crab_transferOutputs
250319_114130:cmsbot_crab_transferLogs
250319_114133:cmsbot_crab_activity
250319_114136:cmsbot_crab_inputFiles
250319_114139:cmsbot_crab_disableAutomaticOutputCollection
250319_114143:cmsbot_crab_outputFiles
250319_114146:cmsbot_crab_allowUndistributedCMSSW
250319_114149:cmsbot_crab_maxMemoryMB
250319_114153:cmsbot_crab_maxJobRuntimeMin
250319_114156:cmsbot_crab_numCores
250319_114159:cmsbot_crab_scriptExe
250319_114202:cmsbot_crab_scriptArgs
250319_114206:cmsbot_crab_sendVenvFolder
250319_114209:cmsbot_crab_sendExternalFolder
250319_114212:cmsbot_crab_inputDBS
250319_114216:cmsbot_crab_useParent
250319_114219:cmsbot_crab_secondaryInputDataset
250319_114222:cmsbot_crab_lumiMaskFile
250319_114226:cmsbot_crab_lumiMaskUrl
250319_114230:cmsbot_crab_outLFNDirBase
250319_114233:cmsbot_crab_runRange
250319_114236:cmsbot_crab_ignoreLocality
250319_114239:cmsbot_crab_userInputFiles
250319_114242:cmsbot_crab_whitelist
250319_114245:cmsbot_crab_blacklist
250319_114249:cmsbot_crab_ignoreGlobalBlacklist
250319_114252:cmsbot_crab_voRole
250319_114255:cmsbot_crab_voGroup
250319_114258:cmsbot_crab_scheddName
250319_114302:cmsbot_crab_collector
250319_114305:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 12:43:05
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/943/console)

## Comment (cmsdmwmbot, 2025-03-19T12:06:31Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-03-19 13:06:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/609/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/609//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-03-19T12:08:39Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-03-19 13:08:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1278/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250319_114127:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250319_114130:cmsbot_crab_transferLogs - 0
activity-check.sh 250319_114133:cmsbot_crab_activity - 0
inputFiles-check.sh 250319_114136:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250319_114139:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250319_114143:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250319_114146:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250319_114149:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250319_114153:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250319_114156:cmsbot_crab_numCores - 0
scriptExe-check.sh 250319_114159:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250319_114202:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250319_114206:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250319_114209:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250319_114212:cmsbot_crab_inputDBS - 0
useParent-check.sh 250319_114216:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250319_114219:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_114222:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250319_114226:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250319_114230:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_114233:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250319_114236:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250319_114239:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_114242:cmsbot_crab_whitelist - 0
blacklist-check.sh 250319_114245:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250319_114249:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250319_114252:cmsbot_crab_voRole - 0
voGroup-check.sh 250319_114255:cmsbot_crab_voGroup - 0
scheddName-check.sh 250319_114258:cmsbot_crab_scheddName - 0
collector-check.sh 250319_114302:cmsbot_crab_collector - 0
extraJDL-check.sh 250319_114305:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```
