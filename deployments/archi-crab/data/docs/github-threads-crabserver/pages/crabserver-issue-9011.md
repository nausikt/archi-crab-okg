# dmwm/CRABServer issue #9011: #956: Test dev CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2025-03-20T10:23:49Z
Closed: 2025-03-20T11:24:47Z
URL: https://github.com/dmwm/CRABServer/issues/9011

## Opening post (cmsdmwmbot, 2025-03-20T10:23:49Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2025-03-20 11:23:48
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/956/)

## Comment (cmsdmwmbot, 2025-03-20T10:25:02Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
250320_102403:cmsbot_crab_transferOutputs
250320_102408:cmsbot_crab_transferLogs
250320_102409:cmsbot_crab_activity
250320_102412:cmsbot_crab_inputFiles
250320_102413:cmsbot_crab_disableAutomaticOutputCollection
250320_102416:cmsbot_crab_outputFiles
250320_102416:cmsbot_crab_allowUndistributedCMSSW
250320_102417:cmsbot_crab_maxMemoryMB
250320_102418:cmsbot_crab_maxJobRuntimeMin
250320_102421:cmsbot_crab_numCores
250320_102421:cmsbot_crab_scriptExe
250320_102422:cmsbot_crab_scriptArgs
250320_102425:cmsbot_crab_sendVenvFolder
250320_102428:cmsbot_crab_sendExternalFolder
250320_102429:cmsbot_crab_inputDBS
250320_102429:cmsbot_crab_useParent
250320_102430:cmsbot_crab_secondaryInputDataset
250320_102431:cmsbot_crab_lumiMaskFile
250320_102432:cmsbot_crab_outLFNDirBase
250320_102433:cmsbot_crab_runRange
250320_102434:cmsbot_crab_ignoreLocality
250320_102434:cmsbot_crab_userInputFiles
250320_102435:cmsbot_crab_whitelist
250320_102436:cmsbot_crab_blacklist
250320_102437:cmsbot_crab_ignoreGlobalBlacklist
250320_102437:cmsbot_crab_voRole
250320_102438:cmsbot_crab_voGroup
250320_102439:cmsbot_crab_scheddName
250320_102439:cmsbot_crab_collector
250320_102440:cmsbot_crab_extraJDL
```

Finished at: 2025-03-20 11:24:40
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/956/console)

## Comment (cmsdmwmbot, 2025-03-20T10:46:31Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2025-03-20 11:46:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1289/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250320_102403:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250320_102408:cmsbot_crab_transferLogs - 0
activity-check.sh 250320_102409:cmsbot_crab_activity - 0
inputFiles-check.sh 250320_102412:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250320_102413:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250320_102416:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250320_102416:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250320_102417:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250320_102418:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250320_102421:cmsbot_crab_numCores - 0
scriptExe-check.sh 250320_102421:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250320_102422:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250320_102425:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250320_102428:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250320_102429:cmsbot_crab_inputDBS - 0
useParent-check.sh 250320_102429:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250320_102430:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250320_102431:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 250320_102432:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250320_102433:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250320_102434:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250320_102434:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250320_102435:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 250320_102437:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250320_102437:cmsbot_crab_voRole - 0
voGroup-check.sh 250320_102438:cmsbot_crab_voGroup - 0
scheddName-check.sh 250320_102439:cmsbot_crab_scheddName - 0
collector-check.sh 250320_102439:cmsbot_crab_collector - 0
extraJDL-check.sh 250320_102440:cmsbot_crab_extraJDL - 0

FAILED TESTS:
blacklist-check.sh 250320_102436:cmsbot_crab_blacklist - 1

RETRY TESTS:
 none
```

## Comment (belforte, 2025-03-20T11:24:47Z)

failure understood. It is OK
