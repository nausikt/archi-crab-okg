# dmwm/CRABServer issue #8455: #788: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-31T21:45:10Z
Closed: 2024-06-03T10:11:25Z
URL: https://github.com/dmwm/CRABServer/issues/8455

## Opening post (cmsdmwmbot, 2024-05-31T21:45:10Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-05-31 23:45:09
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/788/)

## Comment (cmsdmwmbot, 2024-05-31T21:47:08Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240531_214528:cmsbot_crab_transferOutputs
240531_214542:cmsbot_crab_transferLogs
240531_214544:cmsbot_crab_activity
240531_214547:cmsbot_crab_inputFiles
240531_214549:cmsbot_crab_disableAutomaticOutputCollection
240531_214551:cmsbot_crab_outputFiles
240531_214554:cmsbot_crab_allowUndistributedCMSSW
240531_214556:cmsbot_crab_maxMemoryMB
240531_214558:cmsbot_crab_maxJobRuntimeMin
240531_214600:cmsbot_crab_numCores
240531_214602:cmsbot_crab_scriptExe
240531_214604:cmsbot_crab_scriptArgs
240531_214606:cmsbot_crab_sendVenvFolder
240531_214609:cmsbot_crab_sendExternalFolder
240531_214611:cmsbot_crab_inputDBS
240531_214613:cmsbot_crab_useParent
240531_214615:cmsbot_crab_secondaryInputDataset
240531_214617:cmsbot_crab_lumiMaskFile
240531_214620:cmsbot_crab_lumiMaskUrl
240531_214623:cmsbot_crab_outLFNDirBase
240531_214625:cmsbot_crab_runRange
240531_214627:cmsbot_crab_ignoreLocality
240531_214629:cmsbot_crab_userInputFiles
240531_214632:cmsbot_crab_whitelist
240531_214634:cmsbot_crab_blacklist
240531_214636:cmsbot_crab_ignoreGlobalBlacklist
240531_214638:cmsbot_crab_voRole
240531_214640:cmsbot_crab_voGroup
240531_214642:cmsbot_crab_scheddName
240531_214644:cmsbot_crab_collector
240531_214646:cmsbot_crab_extraJDL
```

Finished at: 2024-05-31 23:46:47
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/788/console)

## Comment (cmsdmwmbot, 2024-05-31T22:12:57Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-01 00:12:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1080/console

```
RETRY TESTS:
outputFiles-check.sh 240531_214551:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240531_214556:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 240531_214600:cmsbot_crab_numCores - 2
scriptExe-check.sh 240531_214602:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240531_214604:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240531_214613:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240531_214615:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240531_214620:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240531_214623:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240531_214625:cmsbot_crab_runRange - 2
whitelist-check.sh 240531_214632:cmsbot_crab_whitelist - 2
blacklist-check.sh 240531_214634:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240531_214636:cmsbot_crab_ignoreGlobalBlacklist - 2
voGroup-check.sh 240531_214640:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240531_214528:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240531_214542:cmsbot_crab_transferLogs - 0
activity-check.sh 240531_214544:cmsbot_crab_activity - 0
inputFiles-check.sh 240531_214547:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240531_214549:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240531_214554:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240531_214558:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 240531_214606:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240531_214609:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240531_214611:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240531_214617:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240531_214627:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240531_214629:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240531_214638:cmsbot_crab_voRole - 0
scheddName-check.sh 240531_214642:cmsbot_crab_scheddName - 0
collector-check.sh 240531_214644:cmsbot_crab_collector - 0
extraJDL-check.sh 240531_214646:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-31T22:39:01Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-01 00:39:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1082/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240531_214528:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240531_214542:cmsbot_crab_transferLogs - 0
activity-check.sh 240531_214544:cmsbot_crab_activity - 0
inputFiles-check.sh 240531_214547:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240531_214549:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240531_214554:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240531_214556:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240531_214558:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240531_214600:cmsbot_crab_numCores - 0
scriptExe-check.sh 240531_214602:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240531_214604:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240531_214606:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240531_214609:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240531_214611:cmsbot_crab_inputDBS - 0
useParent-check.sh 240531_214613:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240531_214615:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240531_214617:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240531_214620:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240531_214623:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240531_214625:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240531_214627:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240531_214629:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240531_214632:cmsbot_crab_whitelist - 0
blacklist-check.sh 240531_214634:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240531_214636:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240531_214638:cmsbot_crab_voRole - 0
voGroup-check.sh 240531_214640:cmsbot_crab_voGroup - 0
scheddName-check.sh 240531_214642:cmsbot_crab_scheddName - 0
collector-check.sh 240531_214644:cmsbot_crab_collector - 0
extraJDL-check.sh 240531_214646:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240531_214551:cmsbot_crab_outputFiles - 1
```
