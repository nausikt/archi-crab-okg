# dmwm/CRABServer issue #8862: #921: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-12-12T13:51:40Z
Closed: 2024-12-13T17:58:05Z
URL: https://github.com/dmwm/CRABServer/issues/8862

## Opening post (cmsdmwmbot, 2024-12-12T13:51:40Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-12-12 14:51:39
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/921/)

## Comment (cmsdmwmbot, 2024-12-12T13:54:14Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241212_135204:cmsbot_crab_transferOutputs
241212_135208:cmsbot_crab_transferLogs
241212_135211:cmsbot_crab_activity
241212_135215:cmsbot_crab_inputFiles
241212_135218:cmsbot_crab_disableAutomaticOutputCollection
241212_135222:cmsbot_crab_outputFiles
241212_135225:cmsbot_crab_allowUndistributedCMSSW
241212_135229:cmsbot_crab_maxMemoryMB
241212_135232:cmsbot_crab_maxJobRuntimeMin
241212_135236:cmsbot_crab_numCores
241212_135240:cmsbot_crab_scriptExe
241212_135243:cmsbot_crab_scriptArgs
241212_135247:cmsbot_crab_sendVenvFolder
241212_135250:cmsbot_crab_sendExternalFolder
241212_135254:cmsbot_crab_inputDBS
241212_135257:cmsbot_crab_useParent
241212_135301:cmsbot_crab_secondaryInputDataset
241212_135304:cmsbot_crab_lumiMaskFile
241212_135308:cmsbot_crab_lumiMaskUrl
241212_135312:cmsbot_crab_outLFNDirBase
241212_135316:cmsbot_crab_runRange
241212_135319:cmsbot_crab_ignoreLocality
241212_135323:cmsbot_crab_userInputFiles
241212_135327:cmsbot_crab_whitelist
241212_135330:cmsbot_crab_blacklist
241212_135334:cmsbot_crab_ignoreGlobalBlacklist
241212_135337:cmsbot_crab_voRole
241212_135341:cmsbot_crab_voGroup
241212_135344:cmsbot_crab_scheddName
241212_135348:cmsbot_crab_collector
241212_135352:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241212_135200:cmsbot_crab_20241212_145159
```

Finished at: 2024-12-12 14:53:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/921/console)

## Comment (cmsdmwmbot, 2024-12-12T14:17:36Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-12-12 15:17:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/595/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/595//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-12-12T14:18:04Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-12-12 15:18:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1264/console

```
RETRY TESTS:
outputFiles-check.sh 241212_135222:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 241212_135229:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 241212_135232:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241212_135236:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 241212_135308:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241212_135312:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241212_135316:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241212_135323:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241212_135327:cmsbot_crab_whitelist - 2
blacklist-check.sh 241212_135330:cmsbot_crab_blacklist - 2
voRole-check.sh 241212_135337:cmsbot_crab_voRole - 2
voGroup-check.sh 241212_135341:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241212_135204:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241212_135208:cmsbot_crab_transferLogs - 0
activity-check.sh 241212_135211:cmsbot_crab_activity - 0
inputFiles-check.sh 241212_135215:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241212_135218:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241212_135225:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 241212_135240:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241212_135243:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241212_135247:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241212_135250:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241212_135254:cmsbot_crab_inputDBS - 0
useParent-check.sh 241212_135257:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241212_135301:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241212_135304:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 241212_135319:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 241212_135334:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 241212_135344:cmsbot_crab_scheddName - 0
collector-check.sh 241212_135348:cmsbot_crab_collector - 0
extraJDL-check.sh 241212_135352:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-12-12T14:42:40Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-12-12 15:42:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1265/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241212_135204:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241212_135208:cmsbot_crab_transferLogs - 0
activity-check.sh 241212_135211:cmsbot_crab_activity - 0
inputFiles-check.sh 241212_135215:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241212_135218:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241212_135222:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241212_135225:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241212_135229:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241212_135232:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241212_135236:cmsbot_crab_numCores - 0
scriptExe-check.sh 241212_135240:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241212_135243:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241212_135247:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241212_135250:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241212_135254:cmsbot_crab_inputDBS - 0
useParent-check.sh 241212_135257:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241212_135301:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241212_135304:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241212_135308:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241212_135312:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241212_135316:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241212_135319:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241212_135323:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241212_135327:cmsbot_crab_whitelist - 0
blacklist-check.sh 241212_135330:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241212_135334:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241212_135337:cmsbot_crab_voRole - 0
voGroup-check.sh 241212_135341:cmsbot_crab_voGroup - 0
scheddName-check.sh 241212_135344:cmsbot_crab_scheddName - 0
collector-check.sh 241212_135348:cmsbot_crab_collector - 0
extraJDL-check.sh 241212_135352:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
