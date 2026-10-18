# dmwm/CRABServer issue #8211: #693: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-31T15:04:17Z
Closed: 2024-01-31T16:36:41Z
URL: https://github.com/dmwm/CRABServer/issues/8211

## Opening post (cmsdmwmbot, 2024-01-31T15:04:17Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-01-31 16:04:16
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/693/)

## Comment (cmsdmwmbot, 2024-01-31T15:06:42Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240131_150445:cmsbot_crab_transferOutputs
240131_150447:cmsbot_crab_transferLogs
240131_150449:cmsbot_crab_activity
240131_150451:cmsbot_crab_inputFiles
240131_150453:cmsbot_crab_disableAutomaticOutputCollection
240131_150455:cmsbot_crab_outputFiles
240131_150457:cmsbot_crab_allowUndistributedCMSSW
240131_150458:cmsbot_crab_maxMemoryMB
240131_150500:cmsbot_crab_maxJobRuntimeMin
240131_150502:cmsbot_crab_numCores
240131_150504:cmsbot_crab_scriptExe
240131_150506:cmsbot_crab_scriptArgs
240131_150508:cmsbot_crab_sendVenvFolder
240131_150547:cmsbot_crab_sendExternalFolder
240131_150548:cmsbot_crab_inputDBS
240131_150550:cmsbot_crab_useParent
240131_150552:cmsbot_crab_secondaryInputDataset
240131_150554:cmsbot_crab_lumiMaskFile
240131_150556:cmsbot_crab_lumiMaskUrl
240131_150559:cmsbot_crab_outLFNDirBase
240131_150601:cmsbot_crab_runRange
240131_150603:cmsbot_crab_ignoreLocality
240131_150605:cmsbot_crab_userInputFiles
240131_150607:cmsbot_crab_whitelist
240131_150609:cmsbot_crab_blacklist
240131_150611:cmsbot_crab_ignoreGlobalBlacklist
240131_150612:cmsbot_crab_voRole
240131_150614:cmsbot_crab_voGroup
240131_150616:cmsbot_crab_scheddName
240131_150618:cmsbot_crab_collector
240131_150620:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240131_150442:cmsbot_crab_20240131_160441
```

Finished at: 2024-01-31 16:06:21
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/693/console)

## Comment (cmsdmwmbot, 2024-01-31T15:30:11Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-31 16:30:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/506/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/506//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-31T15:31:32Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-31 16:31:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/911/console

```
RETRY TESTS:
transferLogs-check.sh 240131_150447:cmsbot_crab_transferLogs - 2
activity-check.sh 240131_150449:cmsbot_crab_activity - 2
blacklist-check.sh 240131_150609:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240131_150445:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240131_150451:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240131_150453:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240131_150455:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240131_150457:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240131_150458:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240131_150500:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240131_150502:cmsbot_crab_numCores - 0
scriptExe-check.sh 240131_150504:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240131_150506:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240131_150508:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240131_150547:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240131_150548:cmsbot_crab_inputDBS - 0
ignoreGlobalBlacklist-check.sh 240131_150611:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240131_150612:cmsbot_crab_voRole - 0
voGroup-check.sh 240131_150614:cmsbot_crab_voGroup - 0
scheddName-check.sh 240131_150616:cmsbot_crab_scheddName - 0
collector-check.sh 240131_150618:cmsbot_crab_collector - 0
extraJDL-check.sh 240131_150620:cmsbot_crab_extraJDL - 0

FAILED TESTS:
useParent-check.sh 240131_150550:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240131_150552:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240131_150554:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240131_150556:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240131_150559:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240131_150601:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240131_150603:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240131_150605:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240131_150607:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2024-01-31T15:55:14Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-01-31 16:55:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/912/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240131_150445:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240131_150447:cmsbot_crab_transferLogs - 0
activity-check.sh 240131_150449:cmsbot_crab_activity - 0
inputFiles-check.sh 240131_150451:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240131_150453:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240131_150455:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240131_150457:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240131_150458:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240131_150500:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240131_150502:cmsbot_crab_numCores - 0
scriptExe-check.sh 240131_150504:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240131_150506:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240131_150508:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240131_150547:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240131_150548:cmsbot_crab_inputDBS - 0
blacklist-check.sh 240131_150609:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240131_150611:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240131_150612:cmsbot_crab_voRole - 0
voGroup-check.sh 240131_150614:cmsbot_crab_voGroup - 0
scheddName-check.sh 240131_150616:cmsbot_crab_scheddName - 0
collector-check.sh 240131_150618:cmsbot_crab_collector - 0
extraJDL-check.sh 240131_150620:cmsbot_crab_extraJDL - 0

FAILED TESTS:
useParent-check.sh 240131_150550:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240131_150552:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240131_150554:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240131_150556:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240131_150559:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240131_150601:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240131_150603:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240131_150605:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240131_150607:cmsbot_crab_whitelist - 1
```

## Comment (belforte, 2024-01-31T16:36:41Z)

still buggy
