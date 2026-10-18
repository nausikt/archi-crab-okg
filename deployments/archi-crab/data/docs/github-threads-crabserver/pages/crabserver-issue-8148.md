# dmwm/CRABServer issue #8148: #655: Test dev CRABClient using preprod REST instance and CMSSW_12_5_0 CMSSW release

State: closed
Opened: 2024-01-11T17:34:29Z
Closed: 2024-01-11T20:00:05Z
URL: https://github.com/dmwm/CRABServer/issues/8148

## Opening post (cmsdmwmbot, 2024-01-11T17:34:29Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_5_0**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 18:34:28
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/655/)

## Comment (cmsdmwmbot, 2024-01-11T17:36:36Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_173503:cmsbot_crab_transferOutputs
240111_173505:cmsbot_crab_transferLogs
240111_173508:cmsbot_crab_activity
240111_173510:cmsbot_crab_inputFiles
240111_173512:cmsbot_crab_disableAutomaticOutputCollection
240111_173514:cmsbot_crab_outputFiles
240111_173516:cmsbot_crab_allowUndistributedCMSSW
240111_173518:cmsbot_crab_maxMemoryMB
240111_173520:cmsbot_crab_maxJobRuntimeMin
240111_173523:cmsbot_crab_numCores
240111_173525:cmsbot_crab_scriptExe
240111_173527:cmsbot_crab_scriptArgs
240111_173530:cmsbot_crab_sendVenvFolder
240111_173537:cmsbot_crab_sendExternalFolder
240111_173539:cmsbot_crab_inputDBS
240111_173542:cmsbot_crab_useParent
240111_173544:cmsbot_crab_secondaryInputDataset
240111_173546:cmsbot_crab_lumiMaskFile
240111_173548:cmsbot_crab_lumiMaskUrl
240111_173551:cmsbot_crab_outLFNDirBase
240111_173553:cmsbot_crab_runRange
240111_173556:cmsbot_crab_ignoreLocality
240111_173558:cmsbot_crab_userInputFiles
240111_173600:cmsbot_crab_whitelist
240111_173602:cmsbot_crab_blacklist
240111_173604:cmsbot_crab_ignoreGlobalBlacklist
240111_173606:cmsbot_crab_voRole
240111_173608:cmsbot_crab_voGroup
240111_173610:cmsbot_crab_scheddName
240111_173612:cmsbot_crab_collector
240111_173614:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_173501:cmsbot_crab_20240111_183500
```

Finished at: 2024-01-11 18:36:15
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/655/console)

## Comment (cmsdmwmbot, 2024-01-11T18:01:10Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 19:01:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/472/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/472//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-11T18:06:02Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 19:06:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/849/console

```
RETRY TESTS:
transferOutputs-check.sh 240111_173503:cmsbot_crab_transferOutputs - 2
maxMemoryMB-check.sh 240111_173518:cmsbot_crab_maxMemoryMB - 2
scriptArgs-check.sh 240111_173527:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240111_173548:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240111_173553:cmsbot_crab_runRange - 2
whitelist-check.sh 240111_173600:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_173602:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferLogs-check.sh 240111_173505:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173508:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173510:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173512:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173514:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173516:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240111_173520:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173523:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173525:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240111_173530:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173537:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173539:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173542:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173544:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173546:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_173551:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240111_173556:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173558:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240111_173604:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173606:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173608:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173610:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173612:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173614:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:30:05Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-11 19:30:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/858/console

```
RETRY TESTS:
whitelist-check.sh 240111_173600:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173503:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173505:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173508:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173510:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173512:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173514:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173516:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173518:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173520:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173523:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173525:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173527:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173530:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173537:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173539:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173542:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173544:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173546:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_173548:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_173551:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173553:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173556:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173558:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240111_173602:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_173604:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173606:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173608:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173610:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173612:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173614:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:54:19Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-01-11 19:54:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/866/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173503:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173505:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173508:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173510:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173512:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173514:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173516:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173518:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173520:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173523:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173525:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173527:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173530:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173537:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173539:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173542:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173544:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173546:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_173548:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_173551:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173553:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173556:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173558:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_173600:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_173602:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_173604:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173606:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173608:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173610:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173612:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173614:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-11T20:00:05Z)

All OK
