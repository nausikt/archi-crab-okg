# dmwm/CRABServer issue #8114: #628: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-12-19T10:55:27Z
Closed: 2023-12-19T20:52:06Z
URL: https://github.com/dmwm/CRABServer/issues/8114

## Opening post (cmsdmwmbot, 2023-12-19T10:55:27Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-12-19 11:55:25
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/628/)

## Comment (cmsdmwmbot, 2023-12-19T10:57:50Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_105546:cmsbot_crab_transferOutputs
231219_105548:cmsbot_crab_transferLogs
231219_105550:cmsbot_crab_activity
231219_105553:cmsbot_crab_inputFiles
231219_105555:cmsbot_crab_disableAutomaticOutputCollection
231219_105557:cmsbot_crab_outputFiles
231219_105559:cmsbot_crab_allowUndistributedCMSSW
231219_105601:cmsbot_crab_maxMemoryMB
231219_105603:cmsbot_crab_maxJobRuntimeMin
231219_105605:cmsbot_crab_numCores
231219_105607:cmsbot_crab_scriptExe
231219_105609:cmsbot_crab_scriptArgs
231219_105611:cmsbot_crab_sendVenvFolder
231219_105652:cmsbot_crab_sendExternalFolder
231219_105654:cmsbot_crab_inputDBS
231219_105656:cmsbot_crab_useParent
231219_105658:cmsbot_crab_secondaryInputDataset
231219_105700:cmsbot_crab_lumiMaskFile
231219_105702:cmsbot_crab_lumiMaskUrl
231219_105705:cmsbot_crab_outLFNDirBase
231219_105707:cmsbot_crab_runRange
231219_105709:cmsbot_crab_ignoreLocality
231219_105711:cmsbot_crab_userInputFiles
231219_105713:cmsbot_crab_whitelist
231219_105715:cmsbot_crab_blacklist
231219_105717:cmsbot_crab_ignoreGlobalBlacklist
231219_105719:cmsbot_crab_voRole
231219_105722:cmsbot_crab_voGroup
231219_105724:cmsbot_crab_scheddName
231219_105726:cmsbot_crab_collector
231219_105728:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 11:57:29
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/628/console)

## Comment (cmsdmwmbot, 2023-12-19T11:21:56Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 12:21:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/800/console

```
RETRY TESTS:
activity-check.sh 231219_105550:cmsbot_crab_activity - 2
outputFiles-check.sh 231219_105557:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 231219_105603:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 231219_105607:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 231219_105609:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 231219_105702:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231219_105707:cmsbot_crab_runRange - 2
whitelist-check.sh 231219_105713:cmsbot_crab_whitelist - 2
blacklist-check.sh 231219_105715:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_105546:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_105548:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 231219_105553:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_105555:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 231219_105559:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_105601:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 231219_105605:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 231219_105611:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_105652:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_105654:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 231219_105700:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_105705:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231219_105709:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_105711:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231219_105717:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_105719:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_105722:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_105724:cmsbot_crab_scheddName - 0
collector-check.sh 231219_105726:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_105728:cmsbot_crab_extraJDL - 0

FAILED TESTS:
useParent-check.sh 231219_105656:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231219_105658:cmsbot_crab_secondaryInputDataset - 1
```

## Comment (cmsdmwmbot, 2023-12-19T11:47:31Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-12-19 12:47:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/801/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_105546:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_105548:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_105550:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_105553:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_105555:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_105557:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_105559:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_105601:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_105603:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_105605:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_105607:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_105609:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_105611:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_105652:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_105654:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 231219_105700:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231219_105702:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231219_105705:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_105707:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_105709:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_105711:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_105713:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_105715:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_105717:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_105719:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_105722:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_105724:cmsbot_crab_scheddName - 0
collector-check.sh 231219_105726:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_105728:cmsbot_crab_extraJDL - 0

FAILED TESTS:
useParent-check.sh 231219_105656:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231219_105658:cmsbot_crab_secondaryInputDataset - 1
```
