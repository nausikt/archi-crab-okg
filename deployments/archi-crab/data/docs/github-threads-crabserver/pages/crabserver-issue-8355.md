# dmwm/CRABServer issue #8355: #762: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-24T21:53:38Z
Closed: 2024-05-06T22:34:37Z
URL: https://github.com/dmwm/CRABServer/issues/8355

## Opening post (cmsdmwmbot, 2024-04-24T21:53:38Z)

## Using this to investigate failing outputFile test

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-04-24 23:53:37
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/762/)

## Comment (cmsdmwmbot, 2024-04-24T21:55:26Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240424_215358:cmsbot_crab_transferOutputs
240424_215400:cmsbot_crab_transferLogs
240424_215402:cmsbot_crab_activity
240424_215404:cmsbot_crab_inputFiles
240424_215407:cmsbot_crab_disableAutomaticOutputCollection
240424_215409:cmsbot_crab_outputFiles
240424_215411:cmsbot_crab_allowUndistributedCMSSW
240424_215413:cmsbot_crab_maxMemoryMB
240424_215416:cmsbot_crab_maxJobRuntimeMin
240424_215418:cmsbot_crab_numCores
240424_215420:cmsbot_crab_scriptExe
240424_215422:cmsbot_crab_scriptArgs
240424_215424:cmsbot_crab_sendVenvFolder
240424_215426:cmsbot_crab_sendExternalFolder
240424_215428:cmsbot_crab_inputDBS
240424_215431:cmsbot_crab_useParent
240424_215433:cmsbot_crab_secondaryInputDataset
240424_215435:cmsbot_crab_lumiMaskFile
240424_215437:cmsbot_crab_lumiMaskUrl
240424_215440:cmsbot_crab_outLFNDirBase
240424_215442:cmsbot_crab_runRange
240424_215444:cmsbot_crab_ignoreLocality
240424_215446:cmsbot_crab_userInputFiles
240424_215448:cmsbot_crab_whitelist
240424_215450:cmsbot_crab_blacklist
240424_215453:cmsbot_crab_ignoreGlobalBlacklist
240424_215455:cmsbot_crab_voRole
240424_215457:cmsbot_crab_voGroup
240424_215459:cmsbot_crab_scheddName
240424_215501:cmsbot_crab_collector
240424_215504:cmsbot_crab_extraJDL
```

Finished at: 2024-04-24 23:55:05
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/762/console)

## Comment (cmsdmwmbot, 2024-04-24T22:19:50Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-25 00:19:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1041/console

```
RETRY TESTS:
outputFiles-check.sh 240424_215409:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240424_215416:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240424_215418:cmsbot_crab_numCores - 2
scriptExe-check.sh 240424_215420:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240424_215422:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240424_215431:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240424_215433:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240424_215437:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240424_215440:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240424_215442:cmsbot_crab_runRange - 2
whitelist-check.sh 240424_215448:cmsbot_crab_whitelist - 2
blacklist-check.sh 240424_215450:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240424_215358:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240424_215400:cmsbot_crab_transferLogs - 0
activity-check.sh 240424_215402:cmsbot_crab_activity - 0
inputFiles-check.sh 240424_215404:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240424_215407:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240424_215411:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240424_215413:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240424_215424:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240424_215426:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240424_215428:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240424_215435:cmsbot_crab_lumiMaskFile - 0
userInputFiles-check.sh 240424_215446:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240424_215453:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240424_215455:cmsbot_crab_voRole - 0
voGroup-check.sh 240424_215457:cmsbot_crab_voGroup - 0
scheddName-check.sh 240424_215459:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240424_215504:cmsbot_crab_extraJDL - 0

FAILED TESTS:
ignoreLocality-check.sh 240424_215444:cmsbot_crab_ignoreLocality - 1
collector-check.sh 240424_215501:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-24T22:44:57Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-04-25 00:44:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1042/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240424_215437:cmsbot_crab_lumiMaskUrl - 2
whitelist-check.sh 240424_215448:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240424_215358:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240424_215400:cmsbot_crab_transferLogs - 0
activity-check.sh 240424_215402:cmsbot_crab_activity - 0
inputFiles-check.sh 240424_215404:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240424_215407:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240424_215411:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240424_215413:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240424_215416:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240424_215418:cmsbot_crab_numCores - 0
scriptExe-check.sh 240424_215420:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240424_215422:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240424_215424:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240424_215426:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240424_215428:cmsbot_crab_inputDBS - 0
useParent-check.sh 240424_215431:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240424_215433:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240424_215435:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240424_215440:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240424_215446:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240424_215450:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240424_215453:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240424_215455:cmsbot_crab_voRole - 0
voGroup-check.sh 240424_215457:cmsbot_crab_voGroup - 0
scheddName-check.sh 240424_215459:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240424_215504:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240424_215409:cmsbot_crab_outputFiles - 1
runRange-check.sh 240424_215442:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240424_215444:cmsbot_crab_ignoreLocality - 1
collector-check.sh 240424_215501:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-24T23:10:09Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-25 01:10:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1043/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240424_215358:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240424_215400:cmsbot_crab_transferLogs - 0
activity-check.sh 240424_215402:cmsbot_crab_activity - 0
inputFiles-check.sh 240424_215404:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240424_215407:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240424_215411:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240424_215413:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240424_215416:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240424_215418:cmsbot_crab_numCores - 0
scriptExe-check.sh 240424_215420:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240424_215422:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240424_215424:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240424_215426:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240424_215428:cmsbot_crab_inputDBS - 0
useParent-check.sh 240424_215431:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240424_215433:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240424_215435:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240424_215440:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240424_215446:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240424_215448:cmsbot_crab_whitelist - 0
blacklist-check.sh 240424_215450:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240424_215453:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240424_215455:cmsbot_crab_voRole - 0
voGroup-check.sh 240424_215457:cmsbot_crab_voGroup - 0
scheddName-check.sh 240424_215459:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240424_215504:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240424_215409:cmsbot_crab_outputFiles - 1
lumiMaskUrl-check.sh 240424_215437:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 240424_215442:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240424_215444:cmsbot_crab_ignoreLocality - 1
collector-check.sh 240424_215501:cmsbot_crab_collector - 1
```
