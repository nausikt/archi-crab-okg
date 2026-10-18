# dmwm/CRABServer issue #8153: #660: Test dev CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2024-01-11T17:43:06Z
Closed: 2024-01-11T19:52:52Z
URL: https://github.com/dmwm/CRABServer/issues/8153

## Opening post (cmsdmwmbot, 2024-01-11T17:43:06Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 18:43:05
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/660/)

## Comment (cmsdmwmbot, 2024-01-11T17:45:14Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_174339:cmsbot_crab_transferOutputs
240111_174341:cmsbot_crab_transferLogs
240111_174343:cmsbot_crab_activity
240111_174346:cmsbot_crab_inputFiles
240111_174348:cmsbot_crab_disableAutomaticOutputCollection
240111_174352:cmsbot_crab_outputFiles
240111_174354:cmsbot_crab_allowUndistributedCMSSW
240111_174356:cmsbot_crab_maxMemoryMB
240111_174358:cmsbot_crab_maxJobRuntimeMin
240111_174401:cmsbot_crab_numCores
240111_174404:cmsbot_crab_scriptExe
240111_174406:cmsbot_crab_scriptArgs
240111_174409:cmsbot_crab_sendVenvFolder
240111_174415:cmsbot_crab_sendExternalFolder
240111_174416:cmsbot_crab_inputDBS
240111_174419:cmsbot_crab_useParent
240111_174421:cmsbot_crab_secondaryInputDataset
240111_174423:cmsbot_crab_lumiMaskFile
240111_174430:cmsbot_crab_outLFNDirBase
240111_174432:cmsbot_crab_runRange
240111_174434:cmsbot_crab_ignoreLocality
240111_174435:cmsbot_crab_userInputFiles
240111_174437:cmsbot_crab_whitelist
240111_174439:cmsbot_crab_blacklist
240111_174441:cmsbot_crab_ignoreGlobalBlacklist
240111_174443:cmsbot_crab_voRole
240111_174445:cmsbot_crab_voGroup
240111_174448:cmsbot_crab_scheddName
240111_174450:cmsbot_crab_collector
240111_174452:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_174336:cmsbot_crab_20240111_184332
```

Finished at: 2024-01-11 18:44:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/660/console)

## Comment (cmsdmwmbot, 2024-01-11T18:08:25Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 19:08:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/477/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/477//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-11T18:13:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 19:13:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/854/console

```
RETRY TESTS:
transferLogs-check.sh 240111_174341:cmsbot_crab_transferLogs - 2
activity-check.sh 240111_174343:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 240111_174348:cmsbot_crab_disableAutomaticOutputCollection - 2
maxMemoryMB-check.sh 240111_174356:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240111_174358:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240111_174401:cmsbot_crab_numCores - 2
scriptExe-check.sh 240111_174404:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240111_174406:cmsbot_crab_scriptArgs - 2
blacklist-check.sh 240111_174439:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240111_174441:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240111_174443:cmsbot_crab_voRole - 2
voGroup-check.sh 240111_174445:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240111_174452:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174339:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240111_174346:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 240111_174352:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174354:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240111_174409:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174415:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174416:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174419:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174421:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174423:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_174430:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174432:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174434:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174435:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174437:cmsbot_crab_whitelist - 0
scheddName-check.sh 240111_174448:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174450:cmsbot_crab_collector - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:37:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-11 19:37:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/863/console

```
RETRY TESTS:
transferLogs-check.sh 240111_174341:cmsbot_crab_transferLogs - 2
activity-check.sh 240111_174343:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 240111_174356:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 240111_174401:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240111_174406:cmsbot_crab_scriptArgs - 2
blacklist-check.sh 240111_174439:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174339:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240111_174346:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174348:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174352:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174354:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240111_174358:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240111_174404:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240111_174409:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174415:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174416:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174419:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174421:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174423:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_174430:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174432:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174434:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174435:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174437:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240111_174441:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174443:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174445:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174448:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174450:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174452:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:03:00Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-01-11 20:02:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/871/console

```
RETRY TESTS:
numCores-check.sh 240111_174401:cmsbot_crab_numCores - 2
blacklist-check.sh 240111_174439:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174339:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_174341:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_174343:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_174346:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174348:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174352:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174354:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174356:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174358:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240111_174404:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174406:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174409:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174415:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174416:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174419:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174421:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174423:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_174430:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174432:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174434:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174435:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174437:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240111_174441:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174443:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174445:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174448:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174450:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174452:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:24:17Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 3 out of 4. Test is done.
**Finished at:** 2024-01-11 20:24:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/877/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174339:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_174341:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_174343:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_174346:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174348:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174352:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174354:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174356:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174358:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_174401:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_174404:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174406:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174409:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174415:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174416:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174419:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174421:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174423:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_174430:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174432:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174434:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174435:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174437:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_174439:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_174441:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174443:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174445:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174448:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174450:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174452:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-11T19:52:35Z)

all OK
