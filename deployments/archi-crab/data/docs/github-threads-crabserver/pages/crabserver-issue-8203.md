# dmwm/CRABServer issue #8203: #687: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-30T20:40:19Z
Closed: 2024-01-31T13:58:09Z
URL: https://github.com/dmwm/CRABServer/issues/8203

## Opening post (cmsdmwmbot, 2024-01-30T20:40:19Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-01-30 21:40:18
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/687/)

## Comment (cmsdmwmbot, 2024-01-30T20:43:22Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240130_204119:cmsbot_crab_transferOutputs
240130_204121:cmsbot_crab_transferLogs
240130_204123:cmsbot_crab_activity
240130_204125:cmsbot_crab_inputFiles
240130_204127:cmsbot_crab_disableAutomaticOutputCollection
240130_204129:cmsbot_crab_outputFiles
240130_204131:cmsbot_crab_allowUndistributedCMSSW
240130_204133:cmsbot_crab_maxMemoryMB
240130_204135:cmsbot_crab_maxJobRuntimeMin
240130_204137:cmsbot_crab_numCores
240130_204139:cmsbot_crab_scriptExe
240130_204141:cmsbot_crab_scriptArgs
240130_204143:cmsbot_crab_sendVenvFolder
240130_204225:cmsbot_crab_sendExternalFolder
240130_204227:cmsbot_crab_inputDBS
240130_204229:cmsbot_crab_useParent
240130_204231:cmsbot_crab_secondaryInputDataset
240130_204233:cmsbot_crab_lumiMaskFile
240130_204236:cmsbot_crab_lumiMaskUrl
240130_204239:cmsbot_crab_outLFNDirBase
240130_204240:cmsbot_crab_runRange
240130_204242:cmsbot_crab_ignoreLocality
240130_204244:cmsbot_crab_userInputFiles
240130_204246:cmsbot_crab_whitelist
240130_204248:cmsbot_crab_blacklist
240130_204250:cmsbot_crab_ignoreGlobalBlacklist
240130_204252:cmsbot_crab_voRole
240130_204254:cmsbot_crab_voGroup
240130_204256:cmsbot_crab_scheddName
240130_204258:cmsbot_crab_collector
240130_204300:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240130_204117:cmsbot_crab_20240130_214116
```

Finished at: 2024-01-30 21:43:01
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/687/console)

## Comment (cmsdmwmbot, 2024-01-30T21:07:07Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-30 22:07:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/501/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/501//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-30T21:10:03Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-01-30 22:10:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/897/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_204119:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_204125:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_204127:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240130_204131:cmsbot_crab_allowUndistributedCMSSW - 0

FAILED TESTS:
transferLogs-check.sh 240130_204121:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_204123:cmsbot_crab_activity - 1
outputFiles-check.sh 240130_204129:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240130_204133:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204135:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204137:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_204139:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_204141:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240130_204143:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240130_204225:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240130_204227:cmsbot_crab_inputDBS - 1
useParent-check.sh 240130_204229:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240130_204231:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240130_204233:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_204236:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_204239:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_204240:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_204242:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_204244:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_204246:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_204248:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204250:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204252:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204254:cmsbot_crab_voGroup - 1
scheddName-check.sh 240130_204256:cmsbot_crab_scheddName - 1
collector-check.sh 240130_204258:cmsbot_crab_collector - 1
extraJDL-check.sh 240130_204300:cmsbot_crab_extraJDL - 1
```
