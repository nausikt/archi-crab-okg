# dmwm/CRABServer issue #8142: #652: Test GH CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2024-01-10T14:21:38Z
Closed: 2024-01-10T15:13:28Z
URL: https://github.com/dmwm/CRABServer/issues/8142

## Opening post (cmsdmwmbot, 2024-01-10T14:21:38Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-10 15:21:38
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/652/)

## Comment (cmsdmwmbot, 2024-01-10T14:23:05Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240110_142207:cmsbot_crab_transferOutputs
240110_142207:cmsbot_crab_transferLogs
240110_142208:cmsbot_crab_activity
240110_142210:cmsbot_crab_inputFiles
240110_142211:cmsbot_crab_disableAutomaticOutputCollection
240110_142213:cmsbot_crab_outputFiles
240110_142214:cmsbot_crab_allowUndistributedCMSSW
240110_142215:cmsbot_crab_maxMemoryMB
240110_142216:cmsbot_crab_maxJobRuntimeMin
240110_142218:cmsbot_crab_numCores
240110_142219:cmsbot_crab_scriptExe
240110_142220:cmsbot_crab_scriptArgs
240110_142222:cmsbot_crab_sendVenvFolder
240110_142227:cmsbot_crab_sendExternalFolder
240110_142228:cmsbot_crab_inputDBS
240110_142228:cmsbot_crab_useParent
240110_142229:cmsbot_crab_secondaryInputDataset
240110_142230:cmsbot_crab_lumiMaskFile
240110_142231:cmsbot_crab_lumiMaskUrl
240110_142234:cmsbot_crab_outLFNDirBase
240110_142235:cmsbot_crab_runRange
240110_142235:cmsbot_crab_ignoreLocality
240110_142236:cmsbot_crab_userInputFiles
240110_142237:cmsbot_crab_whitelist
240110_142238:cmsbot_crab_blacklist
240110_142239:cmsbot_crab_ignoreGlobalBlacklist
240110_142239:cmsbot_crab_voRole
240110_142240:cmsbot_crab_voGroup
240110_142241:cmsbot_crab_scheddName
240110_142242:cmsbot_crab_collector
240110_142243:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240110_142206:cmsbot_crab_20240110_152203
```

Finished at: 2024-01-10 15:22:44
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/652/console)

## Comment (cmsdmwmbot, 2024-01-10T14:45:52Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-10 15:45:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/469/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/469//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-10T14:47:04Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-10 15:47:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/844/console

```
RETRY TESTS:
maxMemoryMB-check.sh 240110_142215:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240110_142216:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskUrl-check.sh 240110_142231:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240110_142235:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240110_142236:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240110_142237:cmsbot_crab_whitelist - 2
blacklist-check.sh 240110_142238:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240110_142239:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240110_142239:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240110_142207:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240110_142207:cmsbot_crab_transferLogs - 0
activity-check.sh 240110_142208:cmsbot_crab_activity - 0
inputFiles-check.sh 240110_142210:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240110_142211:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240110_142213:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240110_142214:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240110_142218:cmsbot_crab_numCores - 0
scriptExe-check.sh 240110_142219:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240110_142220:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240110_142222:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240110_142227:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240110_142228:cmsbot_crab_inputDBS - 0
useParent-check.sh 240110_142228:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240110_142229:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240110_142230:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240110_142234:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240110_142235:cmsbot_crab_ignoreLocality - 0
voGroup-check.sh 240110_142240:cmsbot_crab_voGroup - 0
scheddName-check.sh 240110_142241:cmsbot_crab_scheddName - 0
collector-check.sh 240110_142242:cmsbot_crab_collector - 0
extraJDL-check.sh 240110_142243:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-10T15:11:06Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-01-10 16:11:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/846/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240110_142207:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240110_142207:cmsbot_crab_transferLogs - 0
activity-check.sh 240110_142208:cmsbot_crab_activity - 0
inputFiles-check.sh 240110_142210:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240110_142211:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240110_142213:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240110_142214:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240110_142215:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240110_142216:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240110_142218:cmsbot_crab_numCores - 0
scriptExe-check.sh 240110_142219:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240110_142220:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240110_142222:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240110_142227:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240110_142228:cmsbot_crab_inputDBS - 0
useParent-check.sh 240110_142228:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240110_142229:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240110_142230:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240110_142231:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240110_142234:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240110_142235:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240110_142235:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240110_142236:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240110_142237:cmsbot_crab_whitelist - 0
blacklist-check.sh 240110_142238:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240110_142239:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240110_142239:cmsbot_crab_voRole - 0
voGroup-check.sh 240110_142240:cmsbot_crab_voGroup - 0
scheddName-check.sh 240110_142241:cmsbot_crab_scheddName - 0
collector-check.sh 240110_142242:cmsbot_crab_collector - 0
extraJDL-check.sh 240110_142243:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-10T15:13:01Z)

All OK
