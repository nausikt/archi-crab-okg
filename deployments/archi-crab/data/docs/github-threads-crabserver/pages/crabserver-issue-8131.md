# dmwm/CRABServer issue #8131: #642: Test prod CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2023-12-19T22:25:52Z
Closed: 2023-12-20T11:24:29Z
URL: https://github.com/dmwm/CRABServer/issues/8131

## Opening post (cmsdmwmbot, 2023-12-19T22:25:52Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-19 23:25:52
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/642/)

## Comment (cmsdmwmbot, 2023-12-19T22:27:41Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_222614:cmsbot_crab_transferOutputs
231219_222616:cmsbot_crab_transferLogs
231219_222618:cmsbot_crab_activity
231219_222621:cmsbot_crab_inputFiles
231219_222623:cmsbot_crab_disableAutomaticOutputCollection
231219_222626:cmsbot_crab_outputFiles
231219_222628:cmsbot_crab_allowUndistributedCMSSW
231219_222630:cmsbot_crab_maxMemoryMB
231219_222632:cmsbot_crab_maxJobRuntimeMin
231219_222635:cmsbot_crab_numCores
231219_222638:cmsbot_crab_scriptExe
231219_222640:cmsbot_crab_scriptArgs
231219_222643:cmsbot_crab_sendVenvFolder
231219_222648:cmsbot_crab_sendExternalFolder
231219_222649:cmsbot_crab_inputDBS
231219_222651:cmsbot_crab_useParent
231219_222653:cmsbot_crab_secondaryInputDataset
231219_222655:cmsbot_crab_lumiMaskFile
231219_222658:cmsbot_crab_outLFNDirBase
231219_222659:cmsbot_crab_runRange
231219_222701:cmsbot_crab_ignoreLocality
231219_222702:cmsbot_crab_userInputFiles
231219_222704:cmsbot_crab_whitelist
231219_222706:cmsbot_crab_blacklist
231219_222708:cmsbot_crab_ignoreGlobalBlacklist
231219_222711:cmsbot_crab_voRole
231219_222713:cmsbot_crab_voGroup
231219_222715:cmsbot_crab_scheddName
231219_222717:cmsbot_crab_collector
231219_222719:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 23:27:20
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/642/console)

## Comment (cmsdmwmbot, 2023-12-19T22:48:38Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 23:48:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/815/console

```
RETRY TESTS:
transferLogs-check.sh 231219_222616:cmsbot_crab_transferLogs - 2
activity-check.sh 231219_222618:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 231219_222630:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 231219_222632:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 231219_222635:cmsbot_crab_numCores - 2
scriptExe-check.sh 231219_222638:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 231219_222640:cmsbot_crab_scriptArgs - 2
blacklist-check.sh 231219_222706:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 231219_222708:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 231219_222711:cmsbot_crab_voRole - 2
voGroup-check.sh 231219_222713:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222614:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 231219_222621:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222623:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222626:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222628:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 231219_222643:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222648:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222649:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222651:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222653:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222655:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222658:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222659:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222701:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222702:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222704:cmsbot_crab_whitelist - 0
scheddName-check.sh 231219_222715:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222717:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:10:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-12-20 00:10:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/820/console

```
RETRY TESTS:
activity-check.sh 231219_222618:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 231219_222630:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 231219_222632:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 231219_222635:cmsbot_crab_numCores - 2
scriptExe-check.sh 231219_222638:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 231219_222640:cmsbot_crab_scriptArgs - 2
blacklist-check.sh 231219_222706:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 231219_222708:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 231219_222711:cmsbot_crab_voRole - 2
voGroup-check.sh 231219_222713:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222614:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222616:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 231219_222621:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222623:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222626:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222628:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 231219_222643:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222648:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222649:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222651:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222653:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222655:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222658:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222659:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222701:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222702:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222704:cmsbot_crab_whitelist - 0
scheddName-check.sh 231219_222715:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222717:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:31:54Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-12-20 00:31:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/823/console

```
RETRY TESTS:
numCores-check.sh 231219_222635:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222614:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222616:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222618:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222621:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222623:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222626:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222628:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222630:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222632:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 231219_222638:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222640:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222643:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222648:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222649:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222651:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222653:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222655:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222658:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222659:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222701:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222702:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222704:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_222706:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_222708:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222711:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222713:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222715:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222717:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:52:57Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-12-20 00:52:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/825/console

```
RETRY TESTS:
numCores-check.sh 231219_222635:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222614:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222616:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222618:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222621:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222623:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222626:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222628:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222630:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222632:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 231219_222638:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222640:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222643:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222648:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222649:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222651:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222653:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222655:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222658:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222659:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222701:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222702:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222704:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_222706:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_222708:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222711:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222713:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222715:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222717:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-20T00:14:09Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 4. Test is done.
**Finished at:** 2023-12-20 01:14:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/827/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222614:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222616:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222618:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222621:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222623:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222626:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222628:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222630:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222632:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_222635:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_222638:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222640:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222643:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222648:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222649:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222651:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222653:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222655:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222658:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222659:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222701:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222702:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222704:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_222706:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_222708:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222711:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222713:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222715:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222717:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (mapellidario, 2023-12-20T11:24:29Z)

looks good to me
