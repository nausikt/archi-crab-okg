# dmwm/CRABServer issue #8113: #627: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-12-18T20:35:26Z
Closed: 2023-12-19T10:50:43Z
URL: https://github.com/dmwm/CRABServer/issues/8113

## Opening post (cmsdmwmbot, 2023-12-18T20:35:26Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-12-18 21:35:25
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/627/)

## Comment (cmsdmwmbot, 2023-12-18T20:37:52Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231218_203544:cmsbot_crab_transferOutputs
231218_203546:cmsbot_crab_transferLogs
231218_203548:cmsbot_crab_activity
231218_203550:cmsbot_crab_inputFiles
231218_203552:cmsbot_crab_disableAutomaticOutputCollection
231218_203555:cmsbot_crab_outputFiles
231218_203557:cmsbot_crab_allowUndistributedCMSSW
231218_203559:cmsbot_crab_maxMemoryMB
231218_203601:cmsbot_crab_maxJobRuntimeMin
231218_203603:cmsbot_crab_numCores
231218_203605:cmsbot_crab_scriptExe
231218_203607:cmsbot_crab_scriptArgs
231218_203609:cmsbot_crab_sendVenvFolder
231218_203654:cmsbot_crab_sendExternalFolder
231218_203656:cmsbot_crab_inputDBS
231218_203658:cmsbot_crab_useParent
231218_203700:cmsbot_crab_secondaryInputDataset
231218_203702:cmsbot_crab_lumiMaskFile
231218_203704:cmsbot_crab_lumiMaskUrl
231218_203707:cmsbot_crab_outLFNDirBase
231218_203709:cmsbot_crab_runRange
231218_203711:cmsbot_crab_ignoreLocality
231218_203714:cmsbot_crab_userInputFiles
231218_203716:cmsbot_crab_whitelist
231218_203718:cmsbot_crab_blacklist
231218_203720:cmsbot_crab_ignoreGlobalBlacklist
231218_203722:cmsbot_crab_voRole
231218_203724:cmsbot_crab_voGroup
231218_203726:cmsbot_crab_scheddName
231218_203728:cmsbot_crab_collector
231218_203730:cmsbot_crab_extraJDL
```

Finished at: 2023-12-18 21:37:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/627/console)

## Comment (cmsdmwmbot, 2023-12-19T10:37:24Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-12-19 11:37:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/799/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231218_203544:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231218_203546:cmsbot_crab_transferLogs - 0
activity-check.sh 231218_203548:cmsbot_crab_activity - 0
inputFiles-check.sh 231218_203550:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231218_203552:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231218_203555:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231218_203557:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231218_203559:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231218_203601:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231218_203603:cmsbot_crab_numCores - 0
scriptExe-check.sh 231218_203605:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231218_203607:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231218_203609:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231218_203654:cmsbot_crab_sendExternalFolder - 0
lumiMaskFile-check.sh 231218_203702:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231218_203704:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231218_203707:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231218_203709:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231218_203711:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231218_203714:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231218_203716:cmsbot_crab_whitelist - 0
blacklist-check.sh 231218_203718:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231218_203720:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231218_203722:cmsbot_crab_voRole - 0
voGroup-check.sh 231218_203724:cmsbot_crab_voGroup - 0
scheddName-check.sh 231218_203726:cmsbot_crab_scheddName - 0
collector-check.sh 231218_203728:cmsbot_crab_collector - 0
extraJDL-check.sh 231218_203730:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputDBS-check.sh 231218_203656:cmsbot_crab_inputDBS - 1
useParent-check.sh 231218_203658:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231218_203700:cmsbot_crab_secondaryInputDataset - 1
```
