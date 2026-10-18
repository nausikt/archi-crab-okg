# dmwm/CRABServer issue #8400: #776: Test GH CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-13T17:53:31Z
Closed: 2024-05-15T09:56:31Z
URL: https://github.com/dmwm/CRABServer/issues/8400

## Opening post (cmsdmwmbot, 2024-05-13T17:53:31Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-05-13 19:53:30
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/776/)

## Comment (cmsdmwmbot, 2024-05-13T17:55:17Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240513_175355:cmsbot_crab_transferOutputs
240513_175357:cmsbot_crab_transferLogs
240513_175359:cmsbot_crab_activity
240513_175401:cmsbot_crab_inputFiles
240513_175403:cmsbot_crab_disableAutomaticOutputCollection
240513_175405:cmsbot_crab_outputFiles
240513_175407:cmsbot_crab_allowUndistributedCMSSW
240513_175409:cmsbot_crab_maxMemoryMB
240513_175411:cmsbot_crab_maxJobRuntimeMin
240513_175413:cmsbot_crab_numCores
240513_175416:cmsbot_crab_scriptExe
240513_175418:cmsbot_crab_scriptArgs
240513_175420:cmsbot_crab_sendVenvFolder
240513_175422:cmsbot_crab_sendExternalFolder
240513_175424:cmsbot_crab_inputDBS
240513_175426:cmsbot_crab_useParent
240513_175428:cmsbot_crab_secondaryInputDataset
240513_175429:cmsbot_crab_lumiMaskFile
240513_175431:cmsbot_crab_lumiMaskUrl
240513_175434:cmsbot_crab_outLFNDirBase
240513_175436:cmsbot_crab_runRange
240513_175438:cmsbot_crab_ignoreLocality
240513_175440:cmsbot_crab_userInputFiles
240513_175442:cmsbot_crab_whitelist
240513_175444:cmsbot_crab_blacklist
240513_175446:cmsbot_crab_ignoreGlobalBlacklist
240513_175448:cmsbot_crab_voRole
240513_175449:cmsbot_crab_voGroup
240513_175451:cmsbot_crab_scheddName
240513_175453:cmsbot_crab_collector
240513_175455:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240513_175353:cmsbot_crab_20240513_195352
```

Finished at: 2024-05-13 19:54:56
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/776/console)

## Comment (cmsdmwmbot, 2024-05-13T18:20:14Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-05-13 20:20:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/537/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/537//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-05-13T18:23:09Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-13 20:23:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1057/console

```
RETRY TESTS:
transferLogs-check.sh 240513_175357:cmsbot_crab_transferLogs - 2
activity-check.sh 240513_175359:cmsbot_crab_activity - 2
lumiMaskUrl-check.sh 240513_175431:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240513_175436:cmsbot_crab_runRange - 2
whitelist-check.sh 240513_175442:cmsbot_crab_whitelist - 2
blacklist-check.sh 240513_175444:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240513_175446:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240513_175448:cmsbot_crab_voRole - 2
voGroup-check.sh 240513_175449:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240513_175355:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240513_175401:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240513_175403:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240513_175405:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240513_175407:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240513_175409:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240513_175411:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240513_175413:cmsbot_crab_numCores - 0
scriptExe-check.sh 240513_175416:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240513_175418:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240513_175420:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240513_175422:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240513_175424:cmsbot_crab_inputDBS - 0
useParent-check.sh 240513_175426:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240513_175428:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240513_175429:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240513_175434:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240513_175438:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240513_175440:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240513_175451:cmsbot_crab_scheddName - 0
collector-check.sh 240513_175453:cmsbot_crab_collector - 0
extraJDL-check.sh 240513_175455:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-13T18:47:17Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-05-13 20:47:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1058/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240513_175355:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240513_175357:cmsbot_crab_transferLogs - 0
activity-check.sh 240513_175359:cmsbot_crab_activity - 0
inputFiles-check.sh 240513_175401:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240513_175403:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240513_175405:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240513_175407:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240513_175409:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240513_175411:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240513_175413:cmsbot_crab_numCores - 0
scriptExe-check.sh 240513_175416:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240513_175418:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240513_175420:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240513_175422:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240513_175424:cmsbot_crab_inputDBS - 0
useParent-check.sh 240513_175426:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240513_175428:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240513_175429:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240513_175431:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240513_175434:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240513_175436:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240513_175438:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240513_175440:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240513_175442:cmsbot_crab_whitelist - 0
blacklist-check.sh 240513_175444:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240513_175446:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240513_175448:cmsbot_crab_voRole - 0
voGroup-check.sh 240513_175449:cmsbot_crab_voGroup - 0
scheddName-check.sh 240513_175451:cmsbot_crab_scheddName - 0
collector-check.sh 240513_175453:cmsbot_crab_collector - 0
extraJDL-check.sh 240513_175455:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
