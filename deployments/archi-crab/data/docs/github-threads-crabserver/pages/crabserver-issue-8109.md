# dmwm/CRABServer issue #8109: #625: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-12-16T16:12:45Z
Closed: 2023-12-18T18:09:52Z
URL: https://github.com/dmwm/CRABServer/issues/8109

## Opening post (cmsdmwmbot, 2023-12-16T16:12:45Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-12-16 17:12:44
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/625/)

## Comment (cmsdmwmbot, 2023-12-16T16:15:56Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231216_161341:cmsbot_crab_transferOutputs
231216_161343:cmsbot_crab_transferLogs
231216_161345:cmsbot_crab_activity
231216_161347:cmsbot_crab_inputFiles
231216_161349:cmsbot_crab_disableAutomaticOutputCollection
231216_161351:cmsbot_crab_outputFiles
231216_161353:cmsbot_crab_allowUndistributedCMSSW
231216_161355:cmsbot_crab_maxMemoryMB
231216_161357:cmsbot_crab_maxJobRuntimeMin
231216_161359:cmsbot_crab_numCores
231216_161401:cmsbot_crab_scriptExe
231216_161402:cmsbot_crab_scriptArgs
231216_161405:cmsbot_crab_sendVenvFolder
231216_161500:cmsbot_crab_sendExternalFolder
231216_161502:cmsbot_crab_inputDBS
231216_161504:cmsbot_crab_useParent
231216_161506:cmsbot_crab_secondaryInputDataset
231216_161508:cmsbot_crab_lumiMaskFile
231216_161510:cmsbot_crab_lumiMaskUrl
231216_161513:cmsbot_crab_outLFNDirBase
231216_161515:cmsbot_crab_runRange
231216_161517:cmsbot_crab_ignoreLocality
231216_161518:cmsbot_crab_userInputFiles
231216_161520:cmsbot_crab_whitelist
231216_161522:cmsbot_crab_blacklist
231216_161524:cmsbot_crab_ignoreGlobalBlacklist
231216_161526:cmsbot_crab_voRole
231216_161528:cmsbot_crab_voGroup
231216_161530:cmsbot_crab_scheddName
231216_161532:cmsbot_crab_collector
231216_161534:cmsbot_crab_extraJDL
```

Finished at: 2023-12-16 17:15:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/625/console)

## Comment (cmsdmwmbot, 2023-12-16T16:38:53Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-12-16 17:38:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/792/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 231216_161341:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 231216_161343:cmsbot_crab_transferLogs - 1
activity-check.sh 231216_161345:cmsbot_crab_activity - 1
inputFiles-check.sh 231216_161347:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 231216_161349:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 231216_161351:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 231216_161353:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 231216_161355:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 231216_161357:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 231216_161359:cmsbot_crab_numCores - 1
scriptExe-check.sh 231216_161401:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 231216_161402:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 231216_161405:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 231216_161500:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 231216_161502:cmsbot_crab_inputDBS - 1
useParent-check.sh 231216_161504:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231216_161506:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 231216_161508:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 231216_161510:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 231216_161513:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 231216_161515:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 231216_161517:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 231216_161518:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 231216_161520:cmsbot_crab_whitelist - 1
blacklist-check.sh 231216_161522:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 231216_161524:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 231216_161526:cmsbot_crab_voRole - 1
voGroup-check.sh 231216_161528:cmsbot_crab_voGroup - 1
scheddName-check.sh 231216_161530:cmsbot_crab_scheddName - 1
collector-check.sh 231216_161532:cmsbot_crab_collector - 1
extraJDL-check.sh 231216_161534:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-12-16T16:42:34Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-12-16 17:42:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/793/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 231216_161341:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 231216_161343:cmsbot_crab_transferLogs - 1
activity-check.sh 231216_161345:cmsbot_crab_activity - 1
inputFiles-check.sh 231216_161347:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 231216_161349:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 231216_161351:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 231216_161353:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 231216_161355:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 231216_161357:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 231216_161359:cmsbot_crab_numCores - 1
scriptExe-check.sh 231216_161401:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 231216_161402:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 231216_161405:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 231216_161500:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 231216_161502:cmsbot_crab_inputDBS - 1
useParent-check.sh 231216_161504:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231216_161506:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 231216_161508:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 231216_161510:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 231216_161513:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 231216_161515:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 231216_161517:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 231216_161518:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 231216_161520:cmsbot_crab_whitelist - 1
blacklist-check.sh 231216_161522:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 231216_161524:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 231216_161526:cmsbot_crab_voRole - 1
voGroup-check.sh 231216_161528:cmsbot_crab_voGroup - 1
scheddName-check.sh 231216_161530:cmsbot_crab_scheddName - 1
collector-check.sh 231216_161532:cmsbot_crab_collector - 1
extraJDL-check.sh 231216_161534:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-12-16T16:47:49Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-12-16 17:47:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/794/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 231216_161341:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 231216_161343:cmsbot_crab_transferLogs - 1
activity-check.sh 231216_161345:cmsbot_crab_activity - 1
inputFiles-check.sh 231216_161347:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 231216_161349:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 231216_161351:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 231216_161353:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 231216_161355:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 231216_161357:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 231216_161359:cmsbot_crab_numCores - 1
scriptExe-check.sh 231216_161401:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 231216_161402:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 231216_161405:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 231216_161500:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 231216_161502:cmsbot_crab_inputDBS - 1
useParent-check.sh 231216_161504:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231216_161506:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 231216_161508:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 231216_161510:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 231216_161513:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 231216_161515:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 231216_161517:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 231216_161518:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 231216_161520:cmsbot_crab_whitelist - 1
blacklist-check.sh 231216_161522:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 231216_161524:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 231216_161526:cmsbot_crab_voRole - 1
voGroup-check.sh 231216_161528:cmsbot_crab_voGroup - 1
scheddName-check.sh 231216_161530:cmsbot_crab_scheddName - 1
collector-check.sh 231216_161532:cmsbot_crab_collector - 1
extraJDL-check.sh 231216_161534:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-12-18T16:18:27Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-12-18 17:18:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/795/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231216_161341:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231216_161343:cmsbot_crab_transferLogs - 0
activity-check.sh 231216_161345:cmsbot_crab_activity - 0
inputFiles-check.sh 231216_161347:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231216_161349:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231216_161351:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231216_161353:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231216_161355:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231216_161357:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231216_161359:cmsbot_crab_numCores - 0
scriptExe-check.sh 231216_161401:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231216_161402:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231216_161405:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231216_161500:cmsbot_crab_sendExternalFolder - 0
lumiMaskFile-check.sh 231216_161508:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231216_161510:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231216_161513:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231216_161515:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231216_161517:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231216_161518:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231216_161520:cmsbot_crab_whitelist - 0
blacklist-check.sh 231216_161522:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231216_161524:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231216_161526:cmsbot_crab_voRole - 0
voGroup-check.sh 231216_161528:cmsbot_crab_voGroup - 0
scheddName-check.sh 231216_161530:cmsbot_crab_scheddName - 0
collector-check.sh 231216_161532:cmsbot_crab_collector - 0
extraJDL-check.sh 231216_161534:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputDBS-check.sh 231216_161502:cmsbot_crab_inputDBS - 1
useParent-check.sh 231216_161504:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231216_161506:cmsbot_crab_secondaryInputDataset - 1
```
