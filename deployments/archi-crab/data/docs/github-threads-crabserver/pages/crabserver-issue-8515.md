# dmwm/CRABServer issue #8515: #810: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-19T13:04:08Z
Closed: 2024-06-19T14:22:15Z
URL: https://github.com/dmwm/CRABServer/issues/8515

## Opening post (cmsdmwmbot, 2024-06-19T13:04:08Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-06-19 15:04:07
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/810/)

## Comment (cmsdmwmbot, 2024-06-19T13:05:56Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240619_130429:cmsbot_crab_transferOutputs
240619_130431:cmsbot_crab_transferLogs
240619_130433:cmsbot_crab_activity
240619_130435:cmsbot_crab_inputFiles
240619_130437:cmsbot_crab_disableAutomaticOutputCollection
240619_130439:cmsbot_crab_outputFiles
240619_130442:cmsbot_crab_allowUndistributedCMSSW
240619_130444:cmsbot_crab_maxMemoryMB
240619_130446:cmsbot_crab_maxJobRuntimeMin
240619_130448:cmsbot_crab_numCores
240619_130450:cmsbot_crab_scriptExe
240619_130452:cmsbot_crab_scriptArgs
240619_130454:cmsbot_crab_sendVenvFolder
240619_130456:cmsbot_crab_sendExternalFolder
240619_130458:cmsbot_crab_inputDBS
240619_130501:cmsbot_crab_useParent
240619_130503:cmsbot_crab_secondaryInputDataset
240619_130505:cmsbot_crab_lumiMaskFile
240619_130507:cmsbot_crab_lumiMaskUrl
240619_130510:cmsbot_crab_outLFNDirBase
240619_130512:cmsbot_crab_runRange
240619_130514:cmsbot_crab_ignoreLocality
240619_130516:cmsbot_crab_userInputFiles
240619_130519:cmsbot_crab_whitelist
240619_130521:cmsbot_crab_blacklist
240619_130523:cmsbot_crab_ignoreGlobalBlacklist
240619_130525:cmsbot_crab_voRole
240619_130528:cmsbot_crab_voGroup
240619_130530:cmsbot_crab_scheddName
240619_130532:cmsbot_crab_collector
240619_130534:cmsbot_crab_extraJDL
```

Finished at: 2024-06-19 15:05:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/810/console)

## Comment (cmsdmwmbot, 2024-06-19T13:29:02Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-19 15:29:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1132/console

```
RETRY TESTS:
transferLogs-check.sh 240619_130431:cmsbot_crab_transferLogs - 2
activity-check.sh 240619_130433:cmsbot_crab_activity - 2
scriptExe-check.sh 240619_130450:cmsbot_crab_scriptExe - 2
secondaryInputDataset-check.sh 240619_130503:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240619_130507:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240619_130512:cmsbot_crab_runRange - 2
whitelist-check.sh 240619_130519:cmsbot_crab_whitelist - 2
blacklist-check.sh 240619_130521:cmsbot_crab_blacklist - 2
voRole-check.sh 240619_130525:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240619_130429:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240619_130435:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240619_130437:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240619_130439:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240619_130442:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240619_130444:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240619_130446:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240619_130448:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240619_130452:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240619_130454:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240619_130456:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240619_130458:cmsbot_crab_inputDBS - 0
useParent-check.sh 240619_130501:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 240619_130505:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240619_130510:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240619_130514:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240619_130516:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240619_130523:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240619_130528:cmsbot_crab_voGroup - 0
scheddName-check.sh 240619_130530:cmsbot_crab_scheddName - 0
collector-check.sh 240619_130532:cmsbot_crab_collector - 0
extraJDL-check.sh 240619_130534:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-19T13:52:52Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-19 15:52:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1135/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240619_130429:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240619_130431:cmsbot_crab_transferLogs - 0
activity-check.sh 240619_130433:cmsbot_crab_activity - 0
inputFiles-check.sh 240619_130435:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240619_130437:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240619_130439:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240619_130442:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240619_130444:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240619_130446:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240619_130448:cmsbot_crab_numCores - 0
scriptExe-check.sh 240619_130450:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240619_130452:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240619_130454:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240619_130456:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240619_130458:cmsbot_crab_inputDBS - 0
useParent-check.sh 240619_130501:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240619_130503:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240619_130505:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240619_130507:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240619_130510:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240619_130512:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240619_130514:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240619_130516:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240619_130519:cmsbot_crab_whitelist - 0
blacklist-check.sh 240619_130521:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240619_130523:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240619_130525:cmsbot_crab_voRole - 0
voGroup-check.sh 240619_130528:cmsbot_crab_voGroup - 0
scheddName-check.sh 240619_130530:cmsbot_crab_scheddName - 0
collector-check.sh 240619_130532:cmsbot_crab_collector - 0
extraJDL-check.sh 240619_130534:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-06-19T14:22:15Z)

OK
