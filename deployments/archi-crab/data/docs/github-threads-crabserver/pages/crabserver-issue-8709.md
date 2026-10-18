# dmwm/CRABServer issue #8709: #834: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-20T16:13:55Z
Closed: 2024-09-23T21:04:24Z
URL: https://github.com/dmwm/CRABServer/issues/8709

## Opening post (cmsdmwmbot, 2024-09-20T16:13:55Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-09-20 18:13:54
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/834/)

## Comment (cmsdmwmbot, 2024-09-20T16:15:56Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240920_161416:cmsbot_crab_transferOutputs
240920_161418:cmsbot_crab_transferLogs
240920_161421:cmsbot_crab_activity
240920_161423:cmsbot_crab_inputFiles
240920_161426:cmsbot_crab_disableAutomaticOutputCollection
240920_161428:cmsbot_crab_outputFiles
240920_161431:cmsbot_crab_allowUndistributedCMSSW
240920_161433:cmsbot_crab_maxMemoryMB
240920_161435:cmsbot_crab_maxJobRuntimeMin
240920_161438:cmsbot_crab_numCores
240920_161440:cmsbot_crab_scriptExe
240920_161443:cmsbot_crab_scriptArgs
240920_161446:cmsbot_crab_sendVenvFolder
240920_161449:cmsbot_crab_sendExternalFolder
240920_161451:cmsbot_crab_inputDBS
240920_161454:cmsbot_crab_useParent
240920_161457:cmsbot_crab_secondaryInputDataset
240920_161459:cmsbot_crab_lumiMaskFile
240920_161502:cmsbot_crab_lumiMaskUrl
240920_161505:cmsbot_crab_outLFNDirBase
240920_161508:cmsbot_crab_runRange
240920_161511:cmsbot_crab_ignoreLocality
240920_161513:cmsbot_crab_userInputFiles
240920_161516:cmsbot_crab_whitelist
240920_161519:cmsbot_crab_blacklist
240920_161521:cmsbot_crab_ignoreGlobalBlacklist
240920_161524:cmsbot_crab_voRole
240920_161527:cmsbot_crab_voGroup
240920_161529:cmsbot_crab_scheddName
240920_161532:cmsbot_crab_collector
240920_161534:cmsbot_crab_extraJDL
```

Finished at: 2024-09-20 18:15:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/834/console)

## Comment (cmsdmwmbot, 2024-09-20T16:39:17Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-20 18:39:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1173/console

```
RETRY TESTS:
activity-check.sh 240920_161421:cmsbot_crab_activity - 2
outputFiles-check.sh 240920_161428:cmsbot_crab_outputFiles - 2
scriptArgs-check.sh 240920_161443:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240920_161502:cmsbot_crab_lumiMaskUrl - 2
ignoreLocality-check.sh 240920_161511:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 240920_161513:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240920_161516:cmsbot_crab_whitelist - 2
blacklist-check.sh 240920_161519:cmsbot_crab_blacklist - 2
voRole-check.sh 240920_161524:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
allowUndistributedCMSSW-check.sh 240920_161431:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240920_161446:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_161449:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_161451:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_161454:cmsbot_crab_useParent - 0
scheddName-check.sh 240920_161529:cmsbot_crab_scheddName - 0
collector-check.sh 240920_161532:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_161534:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_161416:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240920_161418:cmsbot_crab_transferLogs - 1
inputFiles-check.sh 240920_161423:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_161426:cmsbot_crab_disableAutomaticOutputCollection - 1
maxMemoryMB-check.sh 240920_161433:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_161435:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_161438:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_161440:cmsbot_crab_scriptExe - 1
secondaryInputDataset-check.sh 240920_161457:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_161459:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_161505:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240920_161508:cmsbot_crab_runRange - 1
ignoreGlobalBlacklist-check.sh 240920_161521:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_161527:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2024-09-20T17:03:00Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-09-20 19:02:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1176/console

```
RETRY TESTS:
outputFiles-check.sh 240920_161428:cmsbot_crab_outputFiles - 2
userInputFiles-check.sh 240920_161513:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240920_161516:cmsbot_crab_whitelist - 2
blacklist-check.sh 240920_161519:cmsbot_crab_blacklist - 2
voRole-check.sh 240920_161524:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
activity-check.sh 240920_161421:cmsbot_crab_activity - 0
allowUndistributedCMSSW-check.sh 240920_161431:cmsbot_crab_allowUndistributedCMSSW - 0
scriptArgs-check.sh 240920_161443:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_161446:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_161449:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_161451:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_161454:cmsbot_crab_useParent - 0
lumiMaskUrl-check.sh 240920_161502:cmsbot_crab_lumiMaskUrl - 0
ignoreLocality-check.sh 240920_161511:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 240920_161529:cmsbot_crab_scheddName - 0
collector-check.sh 240920_161532:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_161534:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_161416:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240920_161418:cmsbot_crab_transferLogs - 1
inputFiles-check.sh 240920_161423:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_161426:cmsbot_crab_disableAutomaticOutputCollection - 1
maxMemoryMB-check.sh 240920_161433:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_161435:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_161438:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_161440:cmsbot_crab_scriptExe - 1
secondaryInputDataset-check.sh 240920_161457:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_161459:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_161505:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240920_161508:cmsbot_crab_runRange - 1
ignoreGlobalBlacklist-check.sh 240920_161521:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_161527:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2024-09-20T17:26:42Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-09-20 19:26:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1179/console

```
RETRY TESTS:
outputFiles-check.sh 240920_161428:cmsbot_crab_outputFiles - 2
whitelist-check.sh 240920_161516:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
activity-check.sh 240920_161421:cmsbot_crab_activity - 0
allowUndistributedCMSSW-check.sh 240920_161431:cmsbot_crab_allowUndistributedCMSSW - 0
scriptArgs-check.sh 240920_161443:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_161446:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_161449:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_161451:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_161454:cmsbot_crab_useParent - 0
lumiMaskUrl-check.sh 240920_161502:cmsbot_crab_lumiMaskUrl - 0
ignoreLocality-check.sh 240920_161511:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_161513:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240920_161519:cmsbot_crab_blacklist - 0
voRole-check.sh 240920_161524:cmsbot_crab_voRole - 0
scheddName-check.sh 240920_161529:cmsbot_crab_scheddName - 0
collector-check.sh 240920_161532:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_161534:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_161416:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240920_161418:cmsbot_crab_transferLogs - 1
inputFiles-check.sh 240920_161423:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_161426:cmsbot_crab_disableAutomaticOutputCollection - 1
maxMemoryMB-check.sh 240920_161433:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_161435:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_161438:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_161440:cmsbot_crab_scriptExe - 1
secondaryInputDataset-check.sh 240920_161457:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_161459:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_161505:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240920_161508:cmsbot_crab_runRange - 1
ignoreGlobalBlacklist-check.sh 240920_161521:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_161527:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2024-09-20T17:50:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2024-09-20 19:50:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1182/console

```
RETRY TESTS:
whitelist-check.sh 240920_161516:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
activity-check.sh 240920_161421:cmsbot_crab_activity - 0
outputFiles-check.sh 240920_161428:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_161431:cmsbot_crab_allowUndistributedCMSSW - 0
scriptArgs-check.sh 240920_161443:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_161446:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_161449:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_161451:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_161454:cmsbot_crab_useParent - 0
lumiMaskUrl-check.sh 240920_161502:cmsbot_crab_lumiMaskUrl - 0
ignoreLocality-check.sh 240920_161511:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_161513:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240920_161519:cmsbot_crab_blacklist - 0
voRole-check.sh 240920_161524:cmsbot_crab_voRole - 0
scheddName-check.sh 240920_161529:cmsbot_crab_scheddName - 0
collector-check.sh 240920_161532:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_161534:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_161416:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240920_161418:cmsbot_crab_transferLogs - 1
inputFiles-check.sh 240920_161423:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_161426:cmsbot_crab_disableAutomaticOutputCollection - 1
maxMemoryMB-check.sh 240920_161433:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_161435:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_161438:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_161440:cmsbot_crab_scriptExe - 1
secondaryInputDataset-check.sh 240920_161457:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_161459:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_161505:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240920_161508:cmsbot_crab_runRange - 1
ignoreGlobalBlacklist-check.sh 240920_161521:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_161527:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2024-09-20T18:14:02Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-09-20 20:14:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1187/console

```
RETRY TESTS:
whitelist-check.sh 240920_161516:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
activity-check.sh 240920_161421:cmsbot_crab_activity - 0
outputFiles-check.sh 240920_161428:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_161431:cmsbot_crab_allowUndistributedCMSSW - 0
scriptArgs-check.sh 240920_161443:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_161446:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_161449:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_161451:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_161454:cmsbot_crab_useParent - 0
lumiMaskUrl-check.sh 240920_161502:cmsbot_crab_lumiMaskUrl - 0
ignoreLocality-check.sh 240920_161511:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_161513:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240920_161519:cmsbot_crab_blacklist - 0
voRole-check.sh 240920_161524:cmsbot_crab_voRole - 0
scheddName-check.sh 240920_161529:cmsbot_crab_scheddName - 0
collector-check.sh 240920_161532:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_161534:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_161416:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240920_161418:cmsbot_crab_transferLogs - 1
inputFiles-check.sh 240920_161423:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_161426:cmsbot_crab_disableAutomaticOutputCollection - 1
maxMemoryMB-check.sh 240920_161433:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_161435:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_161438:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_161440:cmsbot_crab_scriptExe - 1
secondaryInputDataset-check.sh 240920_161457:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_161459:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_161505:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240920_161508:cmsbot_crab_runRange - 1
ignoreGlobalBlacklist-check.sh 240920_161521:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_161527:cmsbot_crab_voGroup - 1
```
