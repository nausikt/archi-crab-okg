# dmwm/CRABServer issue #7904: #479: Test prod CRABClient using prod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-10-09T14:23:41Z
Closed: 2023-10-09T19:35:52Z
URL: https://github.com/dmwm/CRABServer/issues/7904

## Opening post (cmsdmwmbot, 2023-10-09T14:23:41Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-10-09 16:23:41
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/479/)

## Comment (cmsdmwmbot, 2023-10-09T14:25:21Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231009_142407:cmsbot_crab_transferOutputs
231009_142408:cmsbot_crab_transferLogs
231009_142410:cmsbot_crab_activity
231009_142411:cmsbot_crab_inputFiles
231009_142413:cmsbot_crab_disableAutomaticOutputCollection
231009_142414:cmsbot_crab_outputFiles
231009_142416:cmsbot_crab_allowUndistributedCMSSW
231009_142417:cmsbot_crab_maxMemoryMB
231009_142418:cmsbot_crab_maxJobRuntimeMin
231009_142420:cmsbot_crab_numCores
231009_142422:cmsbot_crab_scriptExe
231009_142423:cmsbot_crab_scriptArgs
231009_142424:cmsbot_crab_sendPythonFolder
231009_142433:cmsbot_crab_sendExternalFolder
231009_142434:cmsbot_crab_inputDBS
231009_142436:cmsbot_crab_useParent
231009_142437:cmsbot_crab_secondaryInputDataset
231009_142439:cmsbot_crab_lumiMaskFile
231009_142441:cmsbot_crab_lumiMaskUrl
231009_142443:cmsbot_crab_outLFNDirBase
231009_142444:cmsbot_crab_runRange
231009_142446:cmsbot_crab_ignoreLocality
231009_142447:cmsbot_crab_userInputFiles
231009_142449:cmsbot_crab_whitelist
231009_142450:cmsbot_crab_blacklist
231009_142452:cmsbot_crab_ignoreGlobalBlacklist
231009_142453:cmsbot_crab_voRole
231009_142454:cmsbot_crab_voGroup
231009_142456:cmsbot_crab_scheddName
231009_142457:cmsbot_crab_collector
231009_142459:cmsbot_crab_extraJDL
```

Finished at: 2023-10-09 16:24:59
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/479/console)

## Comment (cmsdmwmbot, 2023-10-09T14:47:52Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-10-09 16:47:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/787/console

```
RETRY TESTS:
transferLogs-check.sh 231009_142408:cmsbot_crab_transferLogs - 2
maxMemoryMB-check.sh 231009_142417:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 231009_142420:cmsbot_crab_numCores - 2
useParent-check.sh 231009_142436:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 231009_142441:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231009_142444:cmsbot_crab_runRange - 2
whitelist-check.sh 231009_142449:cmsbot_crab_whitelist - 2
blacklist-check.sh 231009_142450:cmsbot_crab_blacklist - 2
voGroup-check.sh 231009_142454:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231009_142407:cmsbot_crab_transferOutputs - 0
activity-check.sh 231009_142410:cmsbot_crab_activity - 0
inputFiles-check.sh 231009_142411:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231009_142413:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231009_142414:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231009_142416:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 231009_142418:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 231009_142422:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231009_142423:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 231009_142424:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 231009_142433:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231009_142434:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 231009_142437:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231009_142439:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231009_142443:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231009_142446:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231009_142447:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231009_142452:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231009_142453:cmsbot_crab_voRole - 0
scheddName-check.sh 231009_142456:cmsbot_crab_scheddName - 0
collector-check.sh 231009_142457:cmsbot_crab_collector - 0
extraJDL-check.sh 231009_142459:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-10-09T15:10:06Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-10-09 17:10:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/789/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231009_142407:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231009_142408:cmsbot_crab_transferLogs - 0
activity-check.sh 231009_142410:cmsbot_crab_activity - 0
inputFiles-check.sh 231009_142411:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231009_142413:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231009_142414:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231009_142416:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231009_142417:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231009_142418:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231009_142420:cmsbot_crab_numCores - 0
scriptExe-check.sh 231009_142422:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231009_142423:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 231009_142424:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 231009_142433:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231009_142434:cmsbot_crab_inputDBS - 0
useParent-check.sh 231009_142436:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231009_142437:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231009_142439:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231009_142441:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231009_142443:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231009_142444:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231009_142446:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231009_142447:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231009_142449:cmsbot_crab_whitelist - 0
blacklist-check.sh 231009_142450:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231009_142452:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231009_142453:cmsbot_crab_voRole - 0
voGroup-check.sh 231009_142454:cmsbot_crab_voGroup - 0
scheddName-check.sh 231009_142456:cmsbot_crab_scheddName - 0
collector-check.sh 231009_142457:cmsbot_crab_collector - 0
extraJDL-check.sh 231009_142459:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
