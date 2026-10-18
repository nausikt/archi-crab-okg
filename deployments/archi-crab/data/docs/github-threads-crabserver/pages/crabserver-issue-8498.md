# dmwm/CRABServer issue #8498: #805: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-14T20:24:43Z
Closed: 2024-06-17T06:24:47Z
URL: https://github.com/dmwm/CRABServer/issues/8498

## Opening post (cmsdmwmbot, 2024-06-14T20:24:43Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-06-14 22:24:43
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/805/)

## Comment (cmsdmwmbot, 2024-06-14T20:26:27Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240614_202503:cmsbot_crab_transferOutputs
240614_202505:cmsbot_crab_transferLogs
240614_202507:cmsbot_crab_activity
240614_202509:cmsbot_crab_inputFiles
240614_202511:cmsbot_crab_disableAutomaticOutputCollection
240614_202513:cmsbot_crab_outputFiles
240614_202515:cmsbot_crab_allowUndistributedCMSSW
240614_202517:cmsbot_crab_maxMemoryMB
240614_202519:cmsbot_crab_maxJobRuntimeMin
240614_202521:cmsbot_crab_numCores
240614_202523:cmsbot_crab_scriptExe
240614_202525:cmsbot_crab_scriptArgs
240614_202527:cmsbot_crab_sendVenvFolder
240614_202529:cmsbot_crab_sendExternalFolder
240614_202532:cmsbot_crab_inputDBS
240614_202534:cmsbot_crab_useParent
240614_202536:cmsbot_crab_secondaryInputDataset
240614_202538:cmsbot_crab_lumiMaskFile
240614_202540:cmsbot_crab_lumiMaskUrl
240614_202543:cmsbot_crab_outLFNDirBase
240614_202545:cmsbot_crab_runRange
240614_202547:cmsbot_crab_ignoreLocality
240614_202549:cmsbot_crab_userInputFiles
240614_202551:cmsbot_crab_whitelist
240614_202553:cmsbot_crab_blacklist
240614_202555:cmsbot_crab_ignoreGlobalBlacklist
240614_202557:cmsbot_crab_voRole
240614_202559:cmsbot_crab_voGroup
240614_202601:cmsbot_crab_scheddName
240614_202603:cmsbot_crab_collector
240614_202605:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240614_202501:cmsbot_crab_20240614_222500
```

Finished at: 2024-06-14 22:26:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/805/console)

## Comment (cmsdmwmbot, 2024-06-14T20:51:05Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-06-14 22:51:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/541/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/541//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-06-14T20:51:50Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-14 22:51:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1120/console

```
RETRY TESTS:
maxMemoryMB-check.sh 240614_202517:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240614_202519:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskFile-check.sh 240614_202538:cmsbot_crab_lumiMaskFile - 2
outLFNDirBase-check.sh 240614_202543:cmsbot_crab_outLFNDirBase - 2
whitelist-check.sh 240614_202551:cmsbot_crab_whitelist - 2
blacklist-check.sh 240614_202553:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240614_202503:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240614_202505:cmsbot_crab_transferLogs - 0
activity-check.sh 240614_202507:cmsbot_crab_activity - 0
inputFiles-check.sh 240614_202509:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240614_202511:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240614_202513:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240614_202515:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240614_202521:cmsbot_crab_numCores - 0
scriptExe-check.sh 240614_202523:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240614_202525:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240614_202527:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240614_202529:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240614_202532:cmsbot_crab_inputDBS - 0
useParent-check.sh 240614_202534:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240614_202536:cmsbot_crab_secondaryInputDataset - 0
userInputFiles-check.sh 240614_202549:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240614_202555:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240614_202557:cmsbot_crab_voRole - 0
voGroup-check.sh 240614_202559:cmsbot_crab_voGroup - 0
scheddName-check.sh 240614_202601:cmsbot_crab_scheddName - 0
collector-check.sh 240614_202603:cmsbot_crab_collector - 0
extraJDL-check.sh 240614_202605:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240614_202540:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 240614_202545:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240614_202547:cmsbot_crab_ignoreLocality - 1
```

## Comment (belforte, 2024-06-14T21:10:15Z)

DESY dcache keep causing those 3 tests to fail :-(

## Comment (cmsdmwmbot, 2024-06-14T21:16:00Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-06-14 23:15:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1121/console

```
RETRY TESTS:
blacklist-check.sh 240614_202553:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240614_202503:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240614_202505:cmsbot_crab_transferLogs - 0
activity-check.sh 240614_202507:cmsbot_crab_activity - 0
inputFiles-check.sh 240614_202509:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240614_202511:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240614_202513:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240614_202515:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240614_202517:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240614_202519:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240614_202521:cmsbot_crab_numCores - 0
scriptExe-check.sh 240614_202523:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240614_202525:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240614_202527:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240614_202529:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240614_202532:cmsbot_crab_inputDBS - 0
useParent-check.sh 240614_202534:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240614_202536:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240614_202538:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240614_202543:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240614_202549:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240614_202551:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240614_202555:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240614_202557:cmsbot_crab_voRole - 0
voGroup-check.sh 240614_202559:cmsbot_crab_voGroup - 0
scheddName-check.sh 240614_202601:cmsbot_crab_scheddName - 0
collector-check.sh 240614_202603:cmsbot_crab_collector - 0
extraJDL-check.sh 240614_202605:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240614_202540:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 240614_202545:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240614_202547:cmsbot_crab_ignoreLocality - 1
```

## Comment (cmsdmwmbot, 2024-06-14T21:41:04Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-14 23:41:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1122/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240614_202503:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240614_202505:cmsbot_crab_transferLogs - 0
activity-check.sh 240614_202507:cmsbot_crab_activity - 0
inputFiles-check.sh 240614_202509:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240614_202511:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240614_202513:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240614_202515:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240614_202517:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240614_202519:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240614_202521:cmsbot_crab_numCores - 0
scriptExe-check.sh 240614_202523:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240614_202525:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240614_202527:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240614_202529:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240614_202532:cmsbot_crab_inputDBS - 0
useParent-check.sh 240614_202534:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240614_202536:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240614_202538:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240614_202543:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240614_202549:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240614_202551:cmsbot_crab_whitelist - 0
blacklist-check.sh 240614_202553:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240614_202555:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240614_202557:cmsbot_crab_voRole - 0
voGroup-check.sh 240614_202559:cmsbot_crab_voGroup - 0
scheddName-check.sh 240614_202601:cmsbot_crab_scheddName - 0
collector-check.sh 240614_202603:cmsbot_crab_collector - 0
extraJDL-check.sh 240614_202605:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240614_202540:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 240614_202545:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240614_202547:cmsbot_crab_ignoreLocality - 1
```

## Comment (belforte, 2024-06-17T06:24:47Z)

usual dcache problems at DESY
