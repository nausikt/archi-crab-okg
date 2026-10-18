# dmwm/CRABServer issue #8130: #641: Test prod CRABClient using preprod REST instance and CMSSW_8_0_36 CMSSW release

State: closed
Opened: 2023-12-19T22:23:57Z
Closed: 2023-12-20T11:26:16Z
URL: https://github.com/dmwm/CRABServer/issues/8130

## Opening post (cmsdmwmbot, 2023-12-19T22:23:57Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_8_0_36**
- SCRAM_ARCH: **slc7_amd64_gcc530**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-19 23:23:57
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/641/)

## Comment (cmsdmwmbot, 2023-12-19T22:25:44Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_222416:cmsbot_crab_transferOutputs
231219_222418:cmsbot_crab_transferLogs
231219_222420:cmsbot_crab_activity
231219_222423:cmsbot_crab_inputFiles
231219_222425:cmsbot_crab_disableAutomaticOutputCollection
231219_222428:cmsbot_crab_outputFiles
231219_222430:cmsbot_crab_allowUndistributedCMSSW
231219_222432:cmsbot_crab_maxMemoryMB
231219_222435:cmsbot_crab_maxJobRuntimeMin
231219_222438:cmsbot_crab_numCores
231219_222440:cmsbot_crab_scriptExe
231219_222442:cmsbot_crab_scriptArgs
231219_222445:cmsbot_crab_sendVenvFolder
231219_222451:cmsbot_crab_sendExternalFolder
231219_222452:cmsbot_crab_inputDBS
231219_222454:cmsbot_crab_useParent
231219_222456:cmsbot_crab_secondaryInputDataset
231219_222458:cmsbot_crab_lumiMaskFile
231219_222459:cmsbot_crab_lumiMaskUrl
231219_222502:cmsbot_crab_outLFNDirBase
231219_222503:cmsbot_crab_runRange
231219_222504:cmsbot_crab_ignoreLocality
231219_222505:cmsbot_crab_userInputFiles
231219_222507:cmsbot_crab_whitelist
231219_222509:cmsbot_crab_blacklist
231219_222511:cmsbot_crab_ignoreGlobalBlacklist
231219_222513:cmsbot_crab_voRole
231219_222516:cmsbot_crab_voGroup
231219_222518:cmsbot_crab_scheddName
231219_222520:cmsbot_crab_collector
231219_222522:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 23:25:23
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/641/console)

## Comment (cmsdmwmbot, 2023-12-19T22:47:09Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 23:47:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/814/console

```
RETRY TESTS:
transferLogs-check.sh 231219_222418:cmsbot_crab_transferLogs - 2
activity-check.sh 231219_222420:cmsbot_crab_activity - 2
lumiMaskUrl-check.sh 231219_222459:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231219_222503:cmsbot_crab_runRange - 2
whitelist-check.sh 231219_222507:cmsbot_crab_whitelist - 2
blacklist-check.sh 231219_222509:cmsbot_crab_blacklist - 2
voGroup-check.sh 231219_222516:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222416:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 231219_222423:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222425:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222428:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222430:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222432:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222435:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_222438:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_222440:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222442:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222445:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222451:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222452:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222454:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222456:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222458:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222502:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231219_222504:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222505:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231219_222511:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222513:cmsbot_crab_voRole - 0
scheddName-check.sh 231219_222518:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222520:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222522:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:09:28Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-12-20 00:09:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/819/console

```
RETRY TESTS:
runRange-check.sh 231219_222503:cmsbot_crab_runRange - 2
whitelist-check.sh 231219_222507:cmsbot_crab_whitelist - 2
blacklist-check.sh 231219_222509:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222416:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222418:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222420:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222423:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222425:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222428:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222430:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222432:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222435:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_222438:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_222440:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222442:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222445:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222451:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222452:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222454:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222456:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222458:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231219_222459:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231219_222502:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231219_222504:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222505:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231219_222511:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222513:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222516:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222518:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222520:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222522:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:30:50Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-12-20 00:30:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/822/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222416:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222418:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222420:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222423:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222425:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222428:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222430:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222432:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222435:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_222438:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_222440:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222442:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222445:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222451:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222452:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222454:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222456:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222458:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231219_222459:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231219_222502:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222503:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222504:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222505:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222507:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_222509:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_222511:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222513:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222516:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222518:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222520:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222522:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (mapellidario, 2023-12-20T11:26:16Z)

looks good to me
