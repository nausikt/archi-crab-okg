# dmwm/CRABServer issue #8120: #633: Test dev CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2023-12-19T20:33:59Z
Closed: 2023-12-20T11:25:24Z
URL: https://github.com/dmwm/CRABServer/issues/8120

## Opening post (cmsdmwmbot, 2023-12-19T20:33:59Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-19 21:33:59
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/633/)

## Comment (cmsdmwmbot, 2023-12-19T20:36:15Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_203417:cmsbot_crab_transferOutputs
231219_203420:cmsbot_crab_transferLogs
231219_203423:cmsbot_crab_activity
231219_203427:cmsbot_crab_inputFiles
231219_203430:cmsbot_crab_disableAutomaticOutputCollection
231219_203433:cmsbot_crab_outputFiles
231219_203436:cmsbot_crab_allowUndistributedCMSSW
231219_203439:cmsbot_crab_maxMemoryMB
231219_203442:cmsbot_crab_maxJobRuntimeMin
231219_203446:cmsbot_crab_numCores
231219_203449:cmsbot_crab_scriptExe
231219_203452:cmsbot_crab_scriptArgs
231219_203456:cmsbot_crab_sendVenvFolder
231219_203503:cmsbot_crab_sendExternalFolder
231219_203506:cmsbot_crab_inputDBS
231219_203509:cmsbot_crab_useParent
231219_203512:cmsbot_crab_secondaryInputDataset
231219_203515:cmsbot_crab_lumiMaskFile
231219_203518:cmsbot_crab_lumiMaskUrl
231219_203522:cmsbot_crab_outLFNDirBase
231219_203525:cmsbot_crab_runRange
231219_203527:cmsbot_crab_ignoreLocality
231219_203530:cmsbot_crab_userInputFiles
231219_203533:cmsbot_crab_whitelist
231219_203536:cmsbot_crab_blacklist
231219_203539:cmsbot_crab_ignoreGlobalBlacklist
231219_203542:cmsbot_crab_voRole
231219_203545:cmsbot_crab_voGroup
231219_203548:cmsbot_crab_scheddName
231219_203551:cmsbot_crab_collector
231219_203553:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 21:35:54
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/633/console)

## Comment (cmsdmwmbot, 2023-12-19T21:06:54Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 22:06:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/806/console

```
RETRY TESTS:
activity-check.sh 231219_203423:cmsbot_crab_activity - 2
numCores-check.sh 231219_203446:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 231219_203518:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231219_203525:cmsbot_crab_runRange - 2
userInputFiles-check.sh 231219_203530:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 231219_203533:cmsbot_crab_whitelist - 2
blacklist-check.sh 231219_203536:cmsbot_crab_blacklist - 2
voGroup-check.sh 231219_203545:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_203417:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_203420:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 231219_203427:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_203430:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_203433:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_203436:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_203439:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_203442:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 231219_203449:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_203452:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_203456:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_203503:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_203506:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_203509:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_203512:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_203515:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_203522:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231219_203527:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 231219_203539:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_203542:cmsbot_crab_voRole - 0
scheddName-check.sh 231219_203548:cmsbot_crab_scheddName - 0
collector-check.sh 231219_203551:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_203553:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T21:31:17Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-12-19 22:31:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/811/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_203417:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_203420:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_203423:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_203427:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_203430:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_203433:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_203436:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_203439:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_203442:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_203446:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_203449:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_203452:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_203456:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_203503:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_203506:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_203509:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_203512:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_203515:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231219_203518:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231219_203522:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_203525:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_203527:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_203530:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_203533:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_203536:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_203539:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_203542:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_203545:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_203548:cmsbot_crab_scheddName - 0
collector-check.sh 231219_203551:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_203553:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (mapellidario, 2023-12-20T11:25:24Z)

looks good to me
