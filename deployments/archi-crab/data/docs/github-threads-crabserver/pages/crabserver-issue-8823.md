# dmwm/CRABServer issue #8823: #890: Test GH CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-25T20:54:41Z
Closed: 2024-11-25T22:03:39Z
URL: https://github.com/dmwm/CRABServer/issues/8823

## Opening post (cmsdmwmbot, 2024-11-25T20:54:41Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **v3.241125**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-11-25 21:54:40
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/890/)

## Comment (cmsdmwmbot, 2024-11-25T20:57:18Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241125_205506:cmsbot_crab_transferOutputs
241125_205510:cmsbot_crab_transferLogs
241125_205513:cmsbot_crab_activity
241125_205516:cmsbot_crab_inputFiles
241125_205519:cmsbot_crab_disableAutomaticOutputCollection
241125_205523:cmsbot_crab_outputFiles
241125_205526:cmsbot_crab_allowUndistributedCMSSW
241125_205529:cmsbot_crab_maxMemoryMB
241125_205533:cmsbot_crab_maxJobRuntimeMin
241125_205537:cmsbot_crab_numCores
241125_205540:cmsbot_crab_scriptExe
241125_205543:cmsbot_crab_scriptArgs
241125_205547:cmsbot_crab_sendVenvFolder
241125_205550:cmsbot_crab_sendExternalFolder
241125_205553:cmsbot_crab_inputDBS
241125_205557:cmsbot_crab_useParent
241125_205600:cmsbot_crab_secondaryInputDataset
241125_205603:cmsbot_crab_lumiMaskFile
241125_205606:cmsbot_crab_lumiMaskUrl
241125_205610:cmsbot_crab_outLFNDirBase
241125_205613:cmsbot_crab_runRange
241125_205617:cmsbot_crab_ignoreLocality
241125_205620:cmsbot_crab_userInputFiles
241125_205623:cmsbot_crab_whitelist
241125_205627:cmsbot_crab_blacklist
241125_205630:cmsbot_crab_ignoreGlobalBlacklist
241125_205633:cmsbot_crab_voRole
241125_205646:cmsbot_crab_voGroup
241125_205649:cmsbot_crab_scheddName
241125_205653:cmsbot_crab_collector
241125_205656:cmsbot_crab_extraJDL
```

Finished at: 2024-11-25 21:56:56
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/890/console)

## Comment (cmsdmwmbot, 2024-11-25T21:22:19Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-25 22:22:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1237/console

```
RETRY TESTS:
transferLogs-check.sh 241125_205510:cmsbot_crab_transferLogs - 2
activity-check.sh 241125_205513:cmsbot_crab_activity - 2
outputFiles-check.sh 241125_205523:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 241125_205529:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 241125_205533:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241125_205537:cmsbot_crab_numCores - 2
lumiMaskFile-check.sh 241125_205603:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241125_205606:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241125_205610:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241125_205613:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241125_205620:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241125_205623:cmsbot_crab_whitelist - 2
blacklist-check.sh 241125_205627:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241125_205630:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241125_205633:cmsbot_crab_voRole - 2
voGroup-check.sh 241125_205646:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_205506:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241125_205516:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_205519:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241125_205526:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 241125_205540:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_205543:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_205547:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_205550:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_205553:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_205557:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_205600:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 241125_205617:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 241125_205649:cmsbot_crab_scheddName - 0
collector-check.sh 241125_205653:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_205656:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-25T21:46:25Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-25 22:46:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1238/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_205506:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_205510:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_205513:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_205516:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_205519:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241125_205523:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241125_205526:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_205529:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241125_205533:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241125_205537:cmsbot_crab_numCores - 0
scriptExe-check.sh 241125_205540:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_205543:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_205547:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_205550:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_205553:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_205557:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_205600:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_205603:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241125_205606:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241125_205610:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241125_205613:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241125_205617:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241125_205620:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241125_205623:cmsbot_crab_whitelist - 0
blacklist-check.sh 241125_205627:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241125_205630:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241125_205633:cmsbot_crab_voRole - 0
voGroup-check.sh 241125_205646:cmsbot_crab_voGroup - 0
scheddName-check.sh 241125_205649:cmsbot_crab_scheddName - 0
collector-check.sh 241125_205653:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_205656:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-11-25T22:03:40Z)

OK.
