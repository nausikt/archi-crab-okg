# dmwm/CRABServer issue #8136: #647: Test dev CRABClient using preprod REST instance and CMSSW_8_0_36 CMSSW release

State: closed
Opened: 2023-12-20T13:33:16Z
Closed: 2023-12-20T17:04:46Z
URL: https://github.com/dmwm/CRABServer/issues/8136

## Opening post (cmsdmwmbot, 2023-12-20T13:33:16Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_8_0_36**
- SCRAM_ARCH: **slc7_amd64_gcc530**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-20 14:33:15
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/647/)

## Comment (cmsdmwmbot, 2023-12-20T13:34:33Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231220_133331:cmsbot_crab_transferOutputs
231220_133332:cmsbot_crab_transferLogs
231220_133333:cmsbot_crab_activity
231220_133335:cmsbot_crab_inputFiles
231220_133336:cmsbot_crab_disableAutomaticOutputCollection
231220_133338:cmsbot_crab_outputFiles
231220_133339:cmsbot_crab_allowUndistributedCMSSW
231220_133340:cmsbot_crab_maxMemoryMB
231220_133341:cmsbot_crab_maxJobRuntimeMin
231220_133343:cmsbot_crab_numCores
231220_133344:cmsbot_crab_scriptExe
231220_133346:cmsbot_crab_scriptArgs
231220_133348:cmsbot_crab_sendVenvFolder
231220_133351:cmsbot_crab_sendExternalFolder
231220_133352:cmsbot_crab_inputDBS
231220_133353:cmsbot_crab_useParent
231220_133355:cmsbot_crab_secondaryInputDataset
231220_133356:cmsbot_crab_lumiMaskFile
231220_133357:cmsbot_crab_lumiMaskUrl
231220_133359:cmsbot_crab_outLFNDirBase
231220_133400:cmsbot_crab_runRange
231220_133401:cmsbot_crab_ignoreLocality
231220_133402:cmsbot_crab_userInputFiles
231220_133403:cmsbot_crab_whitelist
231220_133404:cmsbot_crab_blacklist
231220_133405:cmsbot_crab_ignoreGlobalBlacklist
231220_133406:cmsbot_crab_voRole
231220_133407:cmsbot_crab_voGroup
231220_133408:cmsbot_crab_scheddName
231220_133410:cmsbot_crab_collector
231220_133411:cmsbot_crab_extraJDL
```

Finished at: 2023-12-20 14:34:11
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/647/console)

## Comment (cmsdmwmbot, 2023-12-20T13:55:57Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-20 14:55:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/832/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 231220_133341:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskUrl-check.sh 231220_133357:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 231220_133359:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 231220_133400:cmsbot_crab_runRange - 2
whitelist-check.sh 231220_133403:cmsbot_crab_whitelist - 2
blacklist-check.sh 231220_133404:cmsbot_crab_blacklist - 2
voGroup-check.sh 231220_133407:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_133331:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231220_133332:cmsbot_crab_transferLogs - 0
activity-check.sh 231220_133333:cmsbot_crab_activity - 0
inputFiles-check.sh 231220_133335:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_133336:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_133338:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_133339:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231220_133340:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 231220_133343:cmsbot_crab_numCores - 0
scriptExe-check.sh 231220_133344:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231220_133346:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231220_133348:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_133351:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_133352:cmsbot_crab_inputDBS - 0
useParent-check.sh 231220_133353:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231220_133355:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_133356:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 231220_133401:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_133402:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231220_133405:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231220_133406:cmsbot_crab_voRole - 0
scheddName-check.sh 231220_133408:cmsbot_crab_scheddName - 0
collector-check.sh 231220_133410:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_133411:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-20T14:17:33Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-12-20 15:17:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/835/console

```
RETRY TESTS:
blacklist-check.sh 231220_133404:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_133331:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231220_133332:cmsbot_crab_transferLogs - 0
activity-check.sh 231220_133333:cmsbot_crab_activity - 0
inputFiles-check.sh 231220_133335:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_133336:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_133338:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_133339:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231220_133340:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231220_133341:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231220_133343:cmsbot_crab_numCores - 0
scriptExe-check.sh 231220_133344:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231220_133346:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231220_133348:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_133351:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_133352:cmsbot_crab_inputDBS - 0
useParent-check.sh 231220_133353:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231220_133355:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_133356:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231220_133357:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231220_133359:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231220_133400:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231220_133401:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_133402:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231220_133403:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 231220_133405:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231220_133406:cmsbot_crab_voRole - 0
voGroup-check.sh 231220_133407:cmsbot_crab_voGroup - 0
scheddName-check.sh 231220_133408:cmsbot_crab_scheddName - 0
collector-check.sh 231220_133410:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_133411:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-20T14:39:04Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-12-20 15:38:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/837/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_133331:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231220_133332:cmsbot_crab_transferLogs - 0
activity-check.sh 231220_133333:cmsbot_crab_activity - 0
inputFiles-check.sh 231220_133335:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_133336:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_133338:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_133339:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231220_133340:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231220_133341:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231220_133343:cmsbot_crab_numCores - 0
scriptExe-check.sh 231220_133344:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231220_133346:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231220_133348:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_133351:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_133352:cmsbot_crab_inputDBS - 0
useParent-check.sh 231220_133353:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231220_133355:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_133356:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231220_133357:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231220_133359:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231220_133400:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231220_133401:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_133402:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231220_133403:cmsbot_crab_whitelist - 0
blacklist-check.sh 231220_133404:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231220_133405:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231220_133406:cmsbot_crab_voRole - 0
voGroup-check.sh 231220_133407:cmsbot_crab_voGroup - 0
scheddName-check.sh 231220_133408:cmsbot_crab_scheddName - 0
collector-check.sh 231220_133410:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_133411:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
