# dmwm/CRABServer issue #7695: #404: Test dev CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-29T19:35:32Z
Closed: 2023-06-29T20:16:19Z
URL: https://github.com/dmwm/CRABServer/issues/7695

## Opening post (cmsdmwmbot, 2023-06-29T19:35:32Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-06-29 21:35:31
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/404/)

## Comment (cmsdmwmbot, 2023-06-29T19:37:49Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_193559:cmsbot_crab_transferOutputs
230629_193601:cmsbot_crab_transferLogs
230629_193602:cmsbot_crab_activity
230629_193604:cmsbot_crab_inputFiles
230629_193606:cmsbot_crab_disableAutomaticOutputCollection
230629_193607:cmsbot_crab_outputFiles
230629_193608:cmsbot_crab_allowUndistributedCMSSW
230629_193610:cmsbot_crab_maxMemoryMB
230629_193611:cmsbot_crab_maxJobRuntimeMin
230629_193613:cmsbot_crab_numCores
230629_193614:cmsbot_crab_scriptExe
230629_193615:cmsbot_crab_scriptArgs
230629_193617:cmsbot_crab_sendPythonFolder
230629_193701:cmsbot_crab_sendExternalFolder
230629_193703:cmsbot_crab_inputDBS
230629_193704:cmsbot_crab_useParent
230629_193706:cmsbot_crab_secondaryInputDataset
230629_193707:cmsbot_crab_lumiMaskFile
230629_193708:cmsbot_crab_lumiMaskUrl
230629_193711:cmsbot_crab_outLFNDirBase
230629_193712:cmsbot_crab_runRange
230629_193714:cmsbot_crab_ignoreLocality
230629_193715:cmsbot_crab_userInputFiles
230629_193716:cmsbot_crab_whitelist
230629_193718:cmsbot_crab_blacklist
230629_193719:cmsbot_crab_ignoreGlobalBlacklist
230629_193721:cmsbot_crab_voRole
230629_193722:cmsbot_crab_voGroup
230629_193723:cmsbot_crab_scheddName
230629_193725:cmsbot_crab_collector
230629_193726:cmsbot_crab_extraJDL
```

Finished at: 2023-06-29 21:37:27
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/404/console)

## Comment (cmsdmwmbot, 2023-06-29T20:01:16Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 22:01:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/631/console

```
RETRY TESTS:
scriptArgs-check.sh 230629_193615:cmsbot_crab_scriptArgs - 2
useParent-check.sh 230629_193704:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230629_193706:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230629_193708:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230629_193711:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230629_193712:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230629_193715:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230629_193716:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_193718:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230629_193719:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230629_193721:cmsbot_crab_voRole - 2
voGroup-check.sh 230629_193722:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_193559:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_193601:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_193602:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_193604:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_193606:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_193607:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_193608:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_193610:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_193611:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_193613:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_193614:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230629_193617:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_193701:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_193703:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 230629_193707:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230629_193714:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 230629_193723:cmsbot_crab_scheddName - 0
collector-check.sh 230629_193725:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_193726:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T20:25:33Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-06-29 22:25:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/632/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_193559:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_193601:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_193602:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_193604:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_193606:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_193607:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_193608:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_193610:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_193611:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_193613:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_193614:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_193615:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_193617:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_193701:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_193703:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_193704:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_193706:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_193707:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_193708:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_193711:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_193712:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_193714:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_193715:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_193716:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_193718:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_193719:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_193721:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_193722:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_193723:cmsbot_crab_scheddName - 0
collector-check.sh 230629_193725:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_193726:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
