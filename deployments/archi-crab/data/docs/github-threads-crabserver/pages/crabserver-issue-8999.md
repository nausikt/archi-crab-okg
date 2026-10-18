# dmwm/CRABServer issue #8999: #945: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2025-03-19T12:11:13Z
Closed: 2025-03-19T14:42:11Z
URL: https://github.com/dmwm/CRABServer/issues/8999

## Opening post (cmsdmwmbot, 2025-03-19T12:11:13Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2025-03-19 13:11:12
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/945/)

## Comment (cmsdmwmbot, 2025-03-19T12:13:32Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_121129:cmsbot_crab_20250319_131127
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_121132:cmsbot_crab_transferOutputs
250319_121136:cmsbot_crab_transferLogs
250319_121139:cmsbot_crab_activity
250319_121142:cmsbot_crab_inputFiles
250319_121145:cmsbot_crab_disableAutomaticOutputCollection
250319_121149:cmsbot_crab_outputFiles
250319_121152:cmsbot_crab_allowUndistributedCMSSW
250319_121155:cmsbot_crab_maxMemoryMB
250319_121158:cmsbot_crab_maxJobRuntimeMin
250319_121202:cmsbot_crab_numCores
250319_121205:cmsbot_crab_scriptExe
250319_121208:cmsbot_crab_scriptArgs
250319_121211:cmsbot_crab_sendVenvFolder
250319_121215:cmsbot_crab_sendExternalFolder
250319_121218:cmsbot_crab_inputDBS
250319_121221:cmsbot_crab_useParent
250319_121224:cmsbot_crab_secondaryInputDataset
250319_121228:cmsbot_crab_lumiMaskFile
250319_121231:cmsbot_crab_lumiMaskUrl
250319_121235:cmsbot_crab_outLFNDirBase
250319_121238:cmsbot_crab_runRange
250319_121241:cmsbot_crab_ignoreLocality
250319_121244:cmsbot_crab_userInputFiles
250319_121248:cmsbot_crab_whitelist
250319_121251:cmsbot_crab_blacklist
250319_121254:cmsbot_crab_ignoreGlobalBlacklist
250319_121257:cmsbot_crab_voRole
250319_121301:cmsbot_crab_voGroup
250319_121304:cmsbot_crab_scheddName
250319_121307:cmsbot_crab_collector
250319_121310:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 13:13:11
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/945/console)

## Comment (cmsdmwmbot, 2025-03-19T12:37:21Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-03-19 13:37:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/611/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/611//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-03-19T12:38:12Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-03-19 13:38:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1279/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250319_121132:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250319_121136:cmsbot_crab_transferLogs - 0
activity-check.sh 250319_121139:cmsbot_crab_activity - 0
inputFiles-check.sh 250319_121142:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250319_121145:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250319_121149:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250319_121152:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250319_121155:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250319_121158:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250319_121202:cmsbot_crab_numCores - 0
scriptExe-check.sh 250319_121205:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250319_121208:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250319_121211:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250319_121215:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250319_121218:cmsbot_crab_inputDBS - 0
useParent-check.sh 250319_121221:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250319_121224:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_121228:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250319_121231:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250319_121235:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_121238:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250319_121241:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250319_121244:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_121248:cmsbot_crab_whitelist - 0
blacklist-check.sh 250319_121251:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250319_121254:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250319_121257:cmsbot_crab_voRole - 0
voGroup-check.sh 250319_121301:cmsbot_crab_voGroup - 0
scheddName-check.sh 250319_121304:cmsbot_crab_scheddName - 0
collector-check.sh 250319_121307:cmsbot_crab_collector - 0
extraJDL-check.sh 250319_121310:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```
