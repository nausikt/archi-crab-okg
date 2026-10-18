# dmwm/CRABServer issue #7696: #405: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-29T20:13:53Z
Closed: 2023-06-29T21:36:08Z
URL: https://github.com/dmwm/CRABServer/issues/7696

## Opening post (cmsdmwmbot, 2023-06-29T20:13:53Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-06-29 22:13:52
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/405/)

## Comment (cmsdmwmbot, 2023-06-29T20:15:52Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_201410:cmsbot_crab_transferOutputs
230629_201412:cmsbot_crab_transferLogs
230629_201413:cmsbot_crab_activity
230629_201414:cmsbot_crab_inputFiles
230629_201416:cmsbot_crab_disableAutomaticOutputCollection
230629_201417:cmsbot_crab_outputFiles
230629_201418:cmsbot_crab_allowUndistributedCMSSW
230629_201420:cmsbot_crab_maxMemoryMB
230629_201421:cmsbot_crab_maxJobRuntimeMin
230629_201422:cmsbot_crab_numCores
230629_201424:cmsbot_crab_scriptExe
230629_201425:cmsbot_crab_scriptArgs
230629_201426:cmsbot_crab_sendPythonFolder
230629_201506:cmsbot_crab_sendExternalFolder
230629_201508:cmsbot_crab_inputDBS
230629_201509:cmsbot_crab_useParent
230629_201510:cmsbot_crab_secondaryInputDataset
230629_201512:cmsbot_crab_lumiMaskFile
230629_201513:cmsbot_crab_lumiMaskUrl
230629_201515:cmsbot_crab_outLFNDirBase
230629_201516:cmsbot_crab_runRange
230629_201518:cmsbot_crab_ignoreLocality
230629_201519:cmsbot_crab_userInputFiles
230629_201520:cmsbot_crab_whitelist
230629_201522:cmsbot_crab_blacklist
230629_201523:cmsbot_crab_ignoreGlobalBlacklist
230629_201524:cmsbot_crab_voRole
230629_201526:cmsbot_crab_voGroup
230629_201527:cmsbot_crab_scheddName
230629_201528:cmsbot_crab_collector
230629_201529:cmsbot_crab_extraJDL
```

Finished at: 2023-06-29 22:15:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/405/console)

## Comment (cmsdmwmbot, 2023-06-29T20:39:08Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 22:39:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/633/console

```
RETRY TESTS:
activity-check.sh 230629_201413:cmsbot_crab_activity - 2
outputFiles-check.sh 230629_201417:cmsbot_crab_outputFiles - 2
lumiMaskUrl-check.sh 230629_201513:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230629_201516:cmsbot_crab_runRange - 2
whitelist-check.sh 230629_201520:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_201522:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_201410:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_201412:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230629_201414:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_201416:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230629_201418:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_201420:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_201421:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_201422:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_201424:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_201425:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_201426:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_201506:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_201508:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_201509:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_201510:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_201512:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230629_201515:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230629_201518:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_201519:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230629_201523:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_201524:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_201526:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_201527:cmsbot_crab_scheddName - 0
collector-check.sh 230629_201528:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_201529:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T21:02:13Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-29 23:02:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/637/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230629_201513:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_201410:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_201412:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_201413:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_201414:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_201416:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_201417:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_201418:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_201420:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_201421:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_201422:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_201424:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_201425:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_201426:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_201506:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_201508:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_201509:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_201510:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_201512:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230629_201515:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_201516:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_201518:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_201519:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_201520:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_201522:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_201523:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_201524:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_201526:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_201527:cmsbot_crab_scheddName - 0
collector-check.sh 230629_201528:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_201529:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T21:28:08Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-06-29 23:28:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/644/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_201410:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_201412:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_201413:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_201414:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_201416:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_201417:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_201418:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_201420:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_201421:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_201422:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_201424:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_201425:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_201426:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_201506:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_201508:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_201509:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_201510:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_201512:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_201513:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_201515:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_201516:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_201518:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_201519:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_201520:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_201522:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_201523:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_201524:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_201526:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_201527:cmsbot_crab_scheddName - 0
collector-check.sh 230629_201528:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_201529:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-06-29T21:36:08Z)

OK
