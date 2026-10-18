# dmwm/CRABServer issue #7584: #380: Test dev CRABClient using prod REST instance and CMSSW_12_6_0_pre4 CMSSW release

State: closed
Opened: 2023-04-06T08:44:54Z
Closed: 2023-04-06T12:22:10Z
URL: https://github.com/dmwm/CRABServer/issues/7584

## Opening post (cmsdmwmbot, 2023-04-06T08:44:54Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_12_6_0_pre4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2023-04-06 10:44:53
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/380/)

## Comment (cmsdmwmbot, 2023-04-06T08:47:20Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230406_084604:cmsbot_crab_transferOutputs
230406_084605:cmsbot_crab_transferLogs
230406_084607:cmsbot_crab_activity
230406_084609:cmsbot_crab_inputFiles
230406_084610:cmsbot_crab_disableAutomaticOutputCollection
230406_084612:cmsbot_crab_outputFiles
230406_084613:cmsbot_crab_allowUndistributedCMSSW
230406_084615:cmsbot_crab_maxMemoryMB
230406_084616:cmsbot_crab_maxJobRuntimeMin
230406_084618:cmsbot_crab_numCores
230406_084619:cmsbot_crab_scriptExe
230406_084621:cmsbot_crab_scriptArgs
230406_084622:cmsbot_crab_sendPythonFolder
230406_084632:cmsbot_crab_sendExternalFolder
230406_084633:cmsbot_crab_inputDBS
230406_084635:cmsbot_crab_useParent
230406_084636:cmsbot_crab_secondaryInputDataset
230406_084638:cmsbot_crab_lumiMaskFile
230406_084639:cmsbot_crab_lumiMaskUrl
230406_084642:cmsbot_crab_outLFNDirBase
230406_084643:cmsbot_crab_runRange
230406_084645:cmsbot_crab_ignoreLocality
230406_084646:cmsbot_crab_userInputFiles
230406_084648:cmsbot_crab_whitelist
230406_084649:cmsbot_crab_blacklist
230406_084651:cmsbot_crab_ignoreGlobalBlacklist
230406_084652:cmsbot_crab_voRole
230406_084654:cmsbot_crab_voGroup
230406_084655:cmsbot_crab_scheddName
230406_084657:cmsbot_crab_collector
230406_084658:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230406_084602:cmsbot_crab_20230406_104600
```

Finished at: 2023-04-06 10:46:59
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/380/console)

## Comment (cmsdmwmbot, 2023-04-06T09:08:37Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-04-06 11:08:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/339/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/339//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-04-06T09:10:35Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-04-06 11:10:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/592/console

```
RETRY TESTS:
numCores-check.sh 230406_084618:cmsbot_crab_numCores - 2
lumiMaskFile-check.sh 230406_084638:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230406_084639:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230406_084643:cmsbot_crab_runRange - 2
whitelist-check.sh 230406_084648:cmsbot_crab_whitelist - 2
blacklist-check.sh 230406_084649:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230406_084651:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230406_084652:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230406_084604:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230406_084605:cmsbot_crab_transferLogs - 0
activity-check.sh 230406_084607:cmsbot_crab_activity - 0
inputFiles-check.sh 230406_084609:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230406_084610:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230406_084612:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230406_084613:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230406_084615:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230406_084616:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230406_084619:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230406_084621:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230406_084622:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230406_084632:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230406_084633:cmsbot_crab_inputDBS - 0
useParent-check.sh 230406_084635:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230406_084636:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 230406_084642:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230406_084645:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230406_084646:cmsbot_crab_userInputFiles - 0
voGroup-check.sh 230406_084654:cmsbot_crab_voGroup - 0
scheddName-check.sh 230406_084655:cmsbot_crab_scheddName - 0
collector-check.sh 230406_084657:cmsbot_crab_collector - 0
extraJDL-check.sh 230406_084658:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-04-06T09:33:05Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-04-06 11:33:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/593/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230406_084604:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230406_084605:cmsbot_crab_transferLogs - 0
activity-check.sh 230406_084607:cmsbot_crab_activity - 0
inputFiles-check.sh 230406_084609:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230406_084610:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230406_084612:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230406_084613:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230406_084615:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230406_084616:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230406_084618:cmsbot_crab_numCores - 0
scriptExe-check.sh 230406_084619:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230406_084621:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230406_084622:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230406_084632:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230406_084633:cmsbot_crab_inputDBS - 0
useParent-check.sh 230406_084635:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230406_084636:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230406_084638:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230406_084639:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230406_084642:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230406_084643:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230406_084645:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230406_084646:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230406_084648:cmsbot_crab_whitelist - 0
blacklist-check.sh 230406_084649:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230406_084651:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230406_084652:cmsbot_crab_voRole - 0
voGroup-check.sh 230406_084654:cmsbot_crab_voGroup - 0
scheddName-check.sh 230406_084655:cmsbot_crab_scheddName - 0
collector-check.sh 230406_084657:cmsbot_crab_collector - 0
extraJDL-check.sh 230406_084658:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-04-06T12:22:06Z)

this validates crab client v3.230404
