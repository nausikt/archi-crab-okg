# dmwm/CRABServer issue #9000: #946: Test dev CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2025-03-19T12:13:40Z
Closed: 2025-03-19T14:43:35Z
URL: https://github.com/dmwm/CRABServer/issues/9000

## Opening post (cmsdmwmbot, 2025-03-19T12:13:40Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2025-03-19 13:13:39
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/946/)

## Comment (cmsdmwmbot, 2025-03-19T12:16:46Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_121437:cmsbot_crab_20250319_131435
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_121441:cmsbot_crab_transferOutputs
250319_121444:cmsbot_crab_transferLogs
250319_121447:cmsbot_crab_activity
250319_121452:cmsbot_crab_inputFiles
250319_121455:cmsbot_crab_disableAutomaticOutputCollection
250319_121459:cmsbot_crab_outputFiles
250319_121502:cmsbot_crab_allowUndistributedCMSSW
250319_121506:cmsbot_crab_maxMemoryMB
250319_121509:cmsbot_crab_maxJobRuntimeMin
250319_121513:cmsbot_crab_numCores
250319_121516:cmsbot_crab_scriptExe
250319_121520:cmsbot_crab_scriptArgs
250319_121524:cmsbot_crab_sendVenvFolder
250319_121528:cmsbot_crab_sendExternalFolder
250319_121532:cmsbot_crab_inputDBS
250319_121535:cmsbot_crab_useParent
250319_121538:cmsbot_crab_secondaryInputDataset
250319_121541:cmsbot_crab_lumiMaskFile
250319_121545:cmsbot_crab_lumiMaskUrl
250319_121549:cmsbot_crab_outLFNDirBase
250319_121552:cmsbot_crab_runRange
250319_121555:cmsbot_crab_ignoreLocality
250319_121558:cmsbot_crab_userInputFiles
250319_121602:cmsbot_crab_whitelist
250319_121605:cmsbot_crab_blacklist
250319_121608:cmsbot_crab_ignoreGlobalBlacklist
250319_121611:cmsbot_crab_voRole
250319_121614:cmsbot_crab_voGroup
250319_121617:cmsbot_crab_scheddName
250319_121621:cmsbot_crab_collector
250319_121624:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 13:16:24
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/946/console)

## Comment (cmsdmwmbot, 2025-03-19T12:40:17Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-03-19 13:40:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/612/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/612//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-03-19T12:41:48Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-03-19 13:41:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1280/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250319_121441:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250319_121444:cmsbot_crab_transferLogs - 0
activity-check.sh 250319_121447:cmsbot_crab_activity - 0
inputFiles-check.sh 250319_121452:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250319_121455:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250319_121459:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250319_121502:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250319_121506:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250319_121509:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250319_121513:cmsbot_crab_numCores - 0
scriptExe-check.sh 250319_121516:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250319_121520:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250319_121524:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250319_121528:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250319_121532:cmsbot_crab_inputDBS - 0
useParent-check.sh 250319_121535:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250319_121538:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_121541:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250319_121545:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250319_121549:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_121552:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250319_121555:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250319_121558:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_121602:cmsbot_crab_whitelist - 0
blacklist-check.sh 250319_121605:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250319_121608:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250319_121611:cmsbot_crab_voRole - 0
voGroup-check.sh 250319_121614:cmsbot_crab_voGroup - 0
scheddName-check.sh 250319_121617:cmsbot_crab_scheddName - 0
collector-check.sh 250319_121621:cmsbot_crab_collector - 0
extraJDL-check.sh 250319_121624:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```
