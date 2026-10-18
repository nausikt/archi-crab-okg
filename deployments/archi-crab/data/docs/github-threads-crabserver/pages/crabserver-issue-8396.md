# dmwm/CRABServer issue #8396: #774: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-12T21:55:30Z
Closed: 2024-05-13T17:32:21Z
URL: https://github.com/dmwm/CRABServer/issues/8396

## Opening post (cmsdmwmbot, 2024-05-12T21:55:30Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-05-12 23:55:29
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/774/)

## Comment (cmsdmwmbot, 2024-05-12T21:57:14Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240512_215549:cmsbot_crab_transferOutputs
240512_215551:cmsbot_crab_transferLogs
240512_215554:cmsbot_crab_activity
240512_215556:cmsbot_crab_inputFiles
240512_215558:cmsbot_crab_disableAutomaticOutputCollection
240512_215600:cmsbot_crab_outputFiles
240512_215602:cmsbot_crab_allowUndistributedCMSSW
240512_215604:cmsbot_crab_maxMemoryMB
240512_215606:cmsbot_crab_maxJobRuntimeMin
240512_215608:cmsbot_crab_numCores
240512_215611:cmsbot_crab_scriptExe
240512_215613:cmsbot_crab_scriptArgs
240512_215615:cmsbot_crab_sendVenvFolder
240512_215617:cmsbot_crab_sendExternalFolder
240512_215619:cmsbot_crab_inputDBS
240512_215621:cmsbot_crab_useParent
240512_215623:cmsbot_crab_secondaryInputDataset
240512_215625:cmsbot_crab_lumiMaskFile
240512_215627:cmsbot_crab_lumiMaskUrl
240512_215630:cmsbot_crab_outLFNDirBase
240512_215632:cmsbot_crab_runRange
240512_215634:cmsbot_crab_ignoreLocality
240512_215636:cmsbot_crab_userInputFiles
240512_215638:cmsbot_crab_whitelist
240512_215640:cmsbot_crab_blacklist
240512_215642:cmsbot_crab_ignoreGlobalBlacklist
240512_215645:cmsbot_crab_voRole
240512_215647:cmsbot_crab_voGroup
240512_215649:cmsbot_crab_scheddName
240512_215651:cmsbot_crab_collector
240512_215652:cmsbot_crab_extraJDL
```

Finished at: 2024-05-12 23:56:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/774/console)

## Comment (cmsdmwmbot, 2024-05-12T22:24:23Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-13 00:24:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1052/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240512_215606:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240512_215608:cmsbot_crab_numCores - 2
scriptExe-check.sh 240512_215611:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240512_215613:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240512_215621:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240512_215623:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240512_215627:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240512_215632:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240512_215636:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240512_215638:cmsbot_crab_whitelist - 2
blacklist-check.sh 240512_215640:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240512_215642:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240512_215645:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240512_215549:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240512_215551:cmsbot_crab_transferLogs - 0
activity-check.sh 240512_215554:cmsbot_crab_activity - 0
inputFiles-check.sh 240512_215556:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240512_215558:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240512_215602:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240512_215604:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240512_215615:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240512_215617:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240512_215619:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240512_215625:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240512_215630:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240512_215634:cmsbot_crab_ignoreLocality - 0
voGroup-check.sh 240512_215647:cmsbot_crab_voGroup - 0
scheddName-check.sh 240512_215649:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240512_215652:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240512_215600:cmsbot_crab_outputFiles - 1
collector-check.sh 240512_215651:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-05-12T22:50:15Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-05-13 00:50:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1053/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240512_215549:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240512_215551:cmsbot_crab_transferLogs - 0
activity-check.sh 240512_215554:cmsbot_crab_activity - 0
inputFiles-check.sh 240512_215556:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240512_215558:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240512_215602:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240512_215604:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240512_215606:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240512_215608:cmsbot_crab_numCores - 0
scriptExe-check.sh 240512_215611:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240512_215613:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240512_215615:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240512_215617:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240512_215619:cmsbot_crab_inputDBS - 0
useParent-check.sh 240512_215621:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240512_215623:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240512_215625:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240512_215627:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240512_215630:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240512_215632:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240512_215634:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240512_215636:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240512_215638:cmsbot_crab_whitelist - 0
blacklist-check.sh 240512_215640:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240512_215642:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240512_215645:cmsbot_crab_voRole - 0
voGroup-check.sh 240512_215647:cmsbot_crab_voGroup - 0
scheddName-check.sh 240512_215649:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240512_215652:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240512_215600:cmsbot_crab_outputFiles - 1
collector-check.sh 240512_215651:cmsbot_crab_collector - 1
```
