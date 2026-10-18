# dmwm/CRABServer issue #8827: #893: Test GH CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-11-25T21:53:23Z
Closed: 2024-11-26T08:42:16Z
URL: https://github.com/dmwm/CRABServer/issues/8827

## Opening post (cmsdmwmbot, 2024-11-25T21:53:23Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**
- CRABServer_tag: **v3.241125**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-11-25 22:53:22
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/893/)

## Comment (cmsdmwmbot, 2024-11-25T21:55:28Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241125_215342:cmsbot_crab_transferOutputs
241125_215343:cmsbot_crab_transferLogs
241125_215344:cmsbot_crab_activity
241125_215345:cmsbot_crab_inputFiles
241125_215345:cmsbot_crab_disableAutomaticOutputCollection
241125_215348:cmsbot_crab_outputFiles
241125_215351:cmsbot_crab_allowUndistributedCMSSW
241125_215354:cmsbot_crab_maxMemoryMB
241125_215357:cmsbot_crab_maxJobRuntimeMin
241125_215402:cmsbot_crab_numCores
241125_215404:cmsbot_crab_scriptExe
241125_215407:cmsbot_crab_scriptArgs
241125_215412:cmsbot_crab_sendVenvFolder
241125_215417:cmsbot_crab_sendExternalFolder
241125_215420:cmsbot_crab_inputDBS
241125_215423:cmsbot_crab_useParent
241125_215426:cmsbot_crab_secondaryInputDataset
241125_215429:cmsbot_crab_lumiMaskFile
241125_215431:cmsbot_crab_lumiMaskUrl
241125_215435:cmsbot_crab_outLFNDirBase
241125_215438:cmsbot_crab_runRange
241125_215441:cmsbot_crab_ignoreLocality
241125_215443:cmsbot_crab_userInputFiles
241125_215446:cmsbot_crab_whitelist
241125_215449:cmsbot_crab_blacklist
241125_215452:cmsbot_crab_ignoreGlobalBlacklist
241125_215455:cmsbot_crab_voRole
241125_215458:cmsbot_crab_voGroup
241125_215500:cmsbot_crab_scheddName
241125_215503:cmsbot_crab_collector
241125_215506:cmsbot_crab_extraJDL
```

Finished at: 2024-11-25 22:55:07
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/893/console)

## Comment (cmsdmwmbot, 2024-11-25T22:18:36Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-25 23:18:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1239/console

```
RETRY TESTS:
transferLogs-check.sh 241125_215343:cmsbot_crab_transferLogs - 2
activity-check.sh 241125_215344:cmsbot_crab_activity - 2
outputFiles-check.sh 241125_215348:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 241125_215354:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 241125_215357:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241125_215402:cmsbot_crab_numCores - 2
scriptExe-check.sh 241125_215404:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 241125_215407:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 241125_215431:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 241125_215438:cmsbot_crab_runRange - 2
whitelist-check.sh 241125_215446:cmsbot_crab_whitelist - 2
blacklist-check.sh 241125_215449:cmsbot_crab_blacklist - 2
voRole-check.sh 241125_215455:cmsbot_crab_voRole - 2
voGroup-check.sh 241125_215458:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_215342:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241125_215345:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_215345:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241125_215351:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 241125_215412:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_215417:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_215420:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_215423:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_215426:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_215429:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 241125_215435:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 241125_215441:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241125_215443:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 241125_215452:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 241125_215500:cmsbot_crab_scheddName - 0
collector-check.sh 241125_215503:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_215506:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-25T22:42:57Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-25 23:42:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1242/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_215342:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_215343:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_215344:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_215345:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_215345:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241125_215348:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241125_215351:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_215354:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241125_215357:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241125_215402:cmsbot_crab_numCores - 0
scriptExe-check.sh 241125_215404:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_215407:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_215412:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_215417:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_215420:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_215423:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_215426:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_215429:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241125_215431:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241125_215435:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241125_215438:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241125_215441:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241125_215443:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241125_215446:cmsbot_crab_whitelist - 0
blacklist-check.sh 241125_215449:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241125_215452:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241125_215455:cmsbot_crab_voRole - 0
voGroup-check.sh 241125_215458:cmsbot_crab_voGroup - 0
scheddName-check.sh 241125_215500:cmsbot_crab_scheddName - 0
collector-check.sh 241125_215503:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_215506:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
