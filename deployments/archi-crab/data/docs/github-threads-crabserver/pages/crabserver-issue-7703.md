# dmwm/CRABServer issue #7703: #415: Test prod CRABClient using test2 REST instance and CMSSW_12_5_0 CMSSW release

State: closed
Opened: 2023-06-29T21:32:37Z
Closed: 2023-06-30T09:06:33Z
URL: https://github.com/dmwm/CRABServer/issues/7703

## Opening post (cmsdmwmbot, 2023-06-29T21:32:37Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_5_0**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2023-06-29 23:32:36
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/415/)

## Comment (cmsdmwmbot, 2023-06-29T21:34:09Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_213259:cmsbot_crab_transferOutputs
230629_213301:cmsbot_crab_transferLogs
230629_213302:cmsbot_crab_activity
230629_213303:cmsbot_crab_inputFiles
230629_213305:cmsbot_crab_disableAutomaticOutputCollection
230629_213306:cmsbot_crab_outputFiles
230629_213307:cmsbot_crab_allowUndistributedCMSSW
230629_213309:cmsbot_crab_maxMemoryMB
230629_213310:cmsbot_crab_maxJobRuntimeMin
230629_213311:cmsbot_crab_numCores
230629_213312:cmsbot_crab_scriptExe
230629_213314:cmsbot_crab_scriptArgs
230629_213315:cmsbot_crab_sendPythonFolder
230629_213323:cmsbot_crab_sendExternalFolder
230629_213324:cmsbot_crab_inputDBS
230629_213326:cmsbot_crab_useParent
230629_213327:cmsbot_crab_secondaryInputDataset
230629_213328:cmsbot_crab_lumiMaskFile
230629_213330:cmsbot_crab_lumiMaskUrl
230629_213332:cmsbot_crab_outLFNDirBase
230629_213333:cmsbot_crab_runRange
230629_213335:cmsbot_crab_ignoreLocality
230629_213336:cmsbot_crab_userInputFiles
230629_213337:cmsbot_crab_whitelist
230629_213339:cmsbot_crab_blacklist
230629_213340:cmsbot_crab_ignoreGlobalBlacklist
230629_213341:cmsbot_crab_voRole
230629_213343:cmsbot_crab_voGroup
230629_213344:cmsbot_crab_scheddName
230629_213345:cmsbot_crab_collector
230629_213347:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230629_213258:cmsbot_crab_20230629_233257
```

Finished at: 2023-06-29 23:33:48
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/415/console)

## Comment (cmsdmwmbot, 2023-06-29T21:56:24Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-29 23:56:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/355/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/355//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-29T21:59:27Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 23:59:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/653/console

```
RETRY TESTS:
outputFiles-check.sh 230629_213306:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230629_213309:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230629_213310:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230629_213311:cmsbot_crab_numCores - 2
scriptExe-check.sh 230629_213312:cmsbot_crab_scriptExe - 2
useParent-check.sh 230629_213326:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230629_213327:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230629_213330:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230629_213333:cmsbot_crab_runRange - 2
whitelist-check.sh 230629_213337:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_213339:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230629_213340:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_213259:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_213301:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_213302:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_213303:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_213305:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230629_213307:cmsbot_crab_allowUndistributedCMSSW - 0
scriptArgs-check.sh 230629_213314:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_213315:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_213323:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_213324:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 230629_213328:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230629_213332:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230629_213335:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_213336:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230629_213341:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_213343:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_213344:cmsbot_crab_scheddName - 0
collector-check.sh 230629_213345:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_213347:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T22:24:23Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-30 00:24:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/656/console

```
RETRY TESTS:
outputFiles-check.sh 230629_213306:cmsbot_crab_outputFiles - 2
numCores-check.sh 230629_213311:cmsbot_crab_numCores - 2
secondaryInputDataset-check.sh 230629_213327:cmsbot_crab_secondaryInputDataset - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_213259:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_213301:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_213302:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_213303:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_213305:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230629_213307:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_213309:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_213310:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230629_213312:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_213314:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_213315:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_213323:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_213324:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_213326:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230629_213328:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_213330:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_213332:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_213333:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_213335:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_213336:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_213337:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_213339:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_213340:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_213341:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_213343:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_213344:cmsbot_crab_scheddName - 0
collector-check.sh 230629_213345:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_213347:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T22:46:43Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-06-30 00:46:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/657/console

```
RETRY TESTS:
numCores-check.sh 230629_213311:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_213259:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_213301:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_213302:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_213303:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_213305:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_213306:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_213307:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_213309:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_213310:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230629_213312:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_213314:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_213315:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_213323:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_213324:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_213326:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_213327:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_213328:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_213330:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_213332:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_213333:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_213335:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_213336:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_213337:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_213339:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_213340:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_213341:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_213343:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_213344:cmsbot_crab_scheddName - 0
collector-check.sh 230629_213345:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_213347:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T23:08:39Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-06-30 01:08:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/658/console

```
RETRY TESTS:
numCores-check.sh 230629_213311:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_213259:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_213301:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_213302:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_213303:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_213305:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_213306:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_213307:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_213309:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_213310:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230629_213312:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_213314:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_213315:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_213323:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_213324:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_213326:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_213327:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_213328:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_213330:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_213332:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_213333:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_213335:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_213336:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_213337:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_213339:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_213340:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_213341:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_213343:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_213344:cmsbot_crab_scheddName - 0
collector-check.sh 230629_213345:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_213347:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T23:30:32Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 4. Test is done.
**Finished at:** 2023-06-30 01:30:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/659/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_213259:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_213301:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_213302:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_213303:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_213305:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_213306:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_213307:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_213309:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_213310:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_213311:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_213312:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_213314:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_213315:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_213323:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_213324:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_213326:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_213327:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_213328:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_213330:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_213332:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_213333:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_213335:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_213336:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_213337:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_213339:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_213340:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_213341:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_213343:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_213344:cmsbot_crab_scheddName - 0
collector-check.sh 230629_213345:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_213347:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
