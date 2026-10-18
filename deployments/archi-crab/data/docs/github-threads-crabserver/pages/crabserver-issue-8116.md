# dmwm/CRABServer issue #8116: #629: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-12-19T20:24:27Z
Closed: 2023-12-20T13:08:17Z
URL: https://github.com/dmwm/CRABServer/issues/8116

## Opening post (cmsdmwmbot, 2023-12-19T20:24:27Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-19 21:24:26
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/629/)

## Comment (cmsdmwmbot, 2023-12-19T20:27:00Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_202446:cmsbot_crab_transferOutputs
231219_202457:cmsbot_crab_transferLogs
231219_202459:cmsbot_crab_activity
231219_202501:cmsbot_crab_inputFiles
231219_202503:cmsbot_crab_disableAutomaticOutputCollection
231219_202505:cmsbot_crab_outputFiles
231219_202507:cmsbot_crab_allowUndistributedCMSSW
231219_202509:cmsbot_crab_maxMemoryMB
231219_202511:cmsbot_crab_maxJobRuntimeMin
231219_202513:cmsbot_crab_numCores
231219_202516:cmsbot_crab_scriptExe
231219_202518:cmsbot_crab_scriptArgs
231219_202520:cmsbot_crab_sendVenvFolder
231219_202600:cmsbot_crab_sendExternalFolder
231219_202603:cmsbot_crab_inputDBS
231219_202605:cmsbot_crab_useParent
231219_202607:cmsbot_crab_secondaryInputDataset
231219_202609:cmsbot_crab_lumiMaskFile
231219_202611:cmsbot_crab_lumiMaskUrl
231219_202615:cmsbot_crab_outLFNDirBase
231219_202617:cmsbot_crab_runRange
231219_202619:cmsbot_crab_ignoreLocality
231219_202621:cmsbot_crab_userInputFiles
231219_202623:cmsbot_crab_whitelist
231219_202625:cmsbot_crab_blacklist
231219_202628:cmsbot_crab_ignoreGlobalBlacklist
231219_202630:cmsbot_crab_voRole
231219_202632:cmsbot_crab_voGroup
231219_202634:cmsbot_crab_scheddName
231219_202636:cmsbot_crab_collector
231219_202638:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 21:26:39
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/629/console)

## Comment (cmsdmwmbot, 2023-12-19T20:51:43Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 21:51:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/802/console

```
RETRY TESTS:
transferLogs-check.sh 231219_202457:cmsbot_crab_transferLogs - 2
activity-check.sh 231219_202459:cmsbot_crab_activity - 2
outputFiles-check.sh 231219_202505:cmsbot_crab_outputFiles - 2
lumiMaskUrl-check.sh 231219_202611:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231219_202617:cmsbot_crab_runRange - 2
whitelist-check.sh 231219_202623:cmsbot_crab_whitelist - 2
blacklist-check.sh 231219_202625:cmsbot_crab_blacklist - 2
voRole-check.sh 231219_202630:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_202446:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 231219_202501:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_202503:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 231219_202507:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_202509:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_202511:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_202513:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_202516:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_202518:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_202520:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_202600:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_202603:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_202605:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_202607:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_202609:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_202615:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231219_202619:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_202621:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231219_202628:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 231219_202632:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_202634:cmsbot_crab_scheddName - 0
collector-check.sh 231219_202636:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_202638:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T21:16:02Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-12-19 22:16:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/807/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_202446:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_202457:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_202459:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_202501:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_202503:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_202505:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_202507:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_202509:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_202511:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_202513:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_202516:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_202518:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_202520:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_202600:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_202603:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_202605:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_202607:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_202609:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231219_202611:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231219_202615:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_202617:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_202619:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_202621:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_202623:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_202625:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_202628:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_202630:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_202632:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_202634:cmsbot_crab_scheddName - 0
collector-check.sh 231219_202636:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_202638:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
