# dmwm/CRABServer issue #7749: #435: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2023-07-12T14:30:22Z
Closed: 2023-07-12T15:28:21Z
URL: https://github.com/dmwm/CRABServer/issues/7749

## Opening post (cmsdmwmbot, 2023-07-12T14:30:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-07-12 16:30:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/435/)

## Comment (cmsdmwmbot, 2023-07-12T14:33:47Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230712_143152:cmsbot_crab_transferOutputs
230712_143155:cmsbot_crab_transferLogs
230712_143158:cmsbot_crab_activity
230712_143201:cmsbot_crab_inputFiles
230712_143204:cmsbot_crab_disableAutomaticOutputCollection
230712_143207:cmsbot_crab_outputFiles
230712_143210:cmsbot_crab_allowUndistributedCMSSW
230712_143213:cmsbot_crab_maxMemoryMB
230712_143216:cmsbot_crab_maxJobRuntimeMin
230712_143219:cmsbot_crab_numCores
230712_143222:cmsbot_crab_scriptExe
230712_143225:cmsbot_crab_scriptArgs
230712_143228:cmsbot_crab_sendPythonFolder
230712_143233:cmsbot_crab_sendExternalFolder
230712_143236:cmsbot_crab_inputDBS
230712_143239:cmsbot_crab_useParent
230712_143242:cmsbot_crab_secondaryInputDataset
230712_143245:cmsbot_crab_lumiMaskFile
230712_143248:cmsbot_crab_lumiMaskUrl
230712_143252:cmsbot_crab_outLFNDirBase
230712_143255:cmsbot_crab_runRange
230712_143258:cmsbot_crab_ignoreLocality
230712_143301:cmsbot_crab_userInputFiles
230712_143304:cmsbot_crab_whitelist
230712_143307:cmsbot_crab_blacklist
230712_143309:cmsbot_crab_ignoreGlobalBlacklist
230712_143312:cmsbot_crab_voRole
230712_143315:cmsbot_crab_voGroup
230712_143318:cmsbot_crab_scheddName
230712_143321:cmsbot_crab_collector
230712_143324:cmsbot_crab_extraJDL
```

Finished at: 2023-07-12 16:33:24
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/435/console)

## Comment (cmsdmwmbot, 2023-07-12T15:00:47Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-12 17:00:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/716/console

```
RETRY TESTS:
numCores-check.sh 230712_143219:cmsbot_crab_numCores - 2
secondaryInputDataset-check.sh 230712_143242:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230712_143248:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230712_143255:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230712_143301:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230712_143304:cmsbot_crab_whitelist - 2
blacklist-check.sh 230712_143307:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_143152:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_143155:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_143158:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_143201:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_143204:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_143207:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_143210:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_143213:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_143216:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230712_143222:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_143225:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_143228:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_143233:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_143236:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_143239:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230712_143245:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230712_143252:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230712_143258:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230712_143309:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_143312:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_143315:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_143318:cmsbot_crab_scheddName - 0
collector-check.sh 230712_143321:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_143324:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-12T15:26:03Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-07-12 17:26:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/720/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_143152:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_143155:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_143158:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_143201:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_143204:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_143207:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_143210:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_143213:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_143216:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230712_143219:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_143222:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_143225:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_143228:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_143233:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_143236:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_143239:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_143242:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_143245:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230712_143248:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230712_143252:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230712_143255:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230712_143258:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_143301:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230712_143304:cmsbot_crab_whitelist - 0
blacklist-check.sh 230712_143307:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230712_143309:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_143312:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_143315:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_143318:cmsbot_crab_scheddName - 0
collector-check.sh 230712_143321:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_143324:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
