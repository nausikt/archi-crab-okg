# dmwm/CRABServer issue #8835: #901: Test dev CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2024-11-26T09:37:06Z
Closed: 2024-11-26T14:20:06Z
URL: https://github.com/dmwm/CRABServer/issues/8835

## Opening post (cmsdmwmbot, 2024-11-26T09:37:06Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-11-26 10:37:05
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/901/)

## Comment (cmsdmwmbot, 2024-11-26T09:38:05Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241126_093718:cmsbot_crab_transferOutputs
241126_093719:cmsbot_crab_transferLogs
241126_093720:cmsbot_crab_activity
241126_093721:cmsbot_crab_inputFiles
241126_093721:cmsbot_crab_disableAutomaticOutputCollection
241126_093722:cmsbot_crab_outputFiles
241126_093723:cmsbot_crab_allowUndistributedCMSSW
241126_093724:cmsbot_crab_maxMemoryMB
241126_093725:cmsbot_crab_maxJobRuntimeMin
241126_093725:cmsbot_crab_numCores
241126_093726:cmsbot_crab_scriptExe
241126_093727:cmsbot_crab_scriptArgs
241126_093728:cmsbot_crab_sendVenvFolder
241126_093729:cmsbot_crab_sendExternalFolder
241126_093729:cmsbot_crab_inputDBS
241126_093730:cmsbot_crab_useParent
241126_093731:cmsbot_crab_secondaryInputDataset
241126_093732:cmsbot_crab_lumiMaskFile
241126_093733:cmsbot_crab_lumiMaskUrl
241126_093734:cmsbot_crab_outLFNDirBase
241126_093735:cmsbot_crab_runRange
241126_093736:cmsbot_crab_ignoreLocality
241126_093737:cmsbot_crab_userInputFiles
241126_093738:cmsbot_crab_whitelist
241126_093738:cmsbot_crab_blacklist
241126_093739:cmsbot_crab_ignoreGlobalBlacklist
241126_093740:cmsbot_crab_voRole
241126_093741:cmsbot_crab_voGroup
241126_093741:cmsbot_crab_scheddName
241126_093742:cmsbot_crab_collector
241126_093743:cmsbot_crab_extraJDL
```

Finished at: 2024-11-26 10:37:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/901/console)

## Comment (cmsdmwmbot, 2024-11-26T09:59:22Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-26 10:59:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1253/console

```
RETRY TESTS:
activity-check.sh 241126_093720:cmsbot_crab_activity - 2
outputFiles-check.sh 241126_093722:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 241126_093724:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 241126_093725:cmsbot_crab_numCores - 2
scriptExe-check.sh 241126_093726:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 241126_093727:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 241126_093732:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241126_093733:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 241126_093735:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241126_093737:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241126_093738:cmsbot_crab_whitelist - 2
blacklist-check.sh 241126_093738:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241126_093739:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241126_093740:cmsbot_crab_voRole - 2
voGroup-check.sh 241126_093741:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241126_093718:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241126_093719:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 241126_093721:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241126_093721:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241126_093723:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 241126_093725:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 241126_093728:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241126_093729:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241126_093729:cmsbot_crab_inputDBS - 0
useParent-check.sh 241126_093730:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241126_093731:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 241126_093734:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 241126_093736:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 241126_093741:cmsbot_crab_scheddName - 0
collector-check.sh 241126_093742:cmsbot_crab_collector - 0
extraJDL-check.sh 241126_093743:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-26T10:21:29Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-11-26 11:21:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1254/console

```
RETRY TESTS:
numCores-check.sh 241126_093725:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241126_093718:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241126_093719:cmsbot_crab_transferLogs - 0
activity-check.sh 241126_093720:cmsbot_crab_activity - 0
inputFiles-check.sh 241126_093721:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241126_093721:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241126_093722:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241126_093723:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241126_093724:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241126_093725:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 241126_093726:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241126_093727:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241126_093728:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241126_093729:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241126_093729:cmsbot_crab_inputDBS - 0
useParent-check.sh 241126_093730:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241126_093731:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241126_093732:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241126_093733:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241126_093734:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241126_093735:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241126_093736:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241126_093737:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241126_093738:cmsbot_crab_whitelist - 0
blacklist-check.sh 241126_093738:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241126_093739:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241126_093740:cmsbot_crab_voRole - 0
voGroup-check.sh 241126_093741:cmsbot_crab_voGroup - 0
scheddName-check.sh 241126_093741:cmsbot_crab_scheddName - 0
collector-check.sh 241126_093742:cmsbot_crab_collector - 0
extraJDL-check.sh 241126_093743:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-26T10:43:31Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-11-26 11:43:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1255/console

```
RETRY TESTS:
numCores-check.sh 241126_093725:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241126_093718:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241126_093719:cmsbot_crab_transferLogs - 0
activity-check.sh 241126_093720:cmsbot_crab_activity - 0
inputFiles-check.sh 241126_093721:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241126_093721:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241126_093722:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241126_093723:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241126_093724:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241126_093725:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 241126_093726:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241126_093727:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241126_093728:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241126_093729:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241126_093729:cmsbot_crab_inputDBS - 0
useParent-check.sh 241126_093730:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241126_093731:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241126_093732:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241126_093733:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241126_093734:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241126_093735:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241126_093736:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241126_093737:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241126_093738:cmsbot_crab_whitelist - 0
blacklist-check.sh 241126_093738:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241126_093739:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241126_093740:cmsbot_crab_voRole - 0
voGroup-check.sh 241126_093741:cmsbot_crab_voGroup - 0
scheddName-check.sh 241126_093741:cmsbot_crab_scheddName - 0
collector-check.sh 241126_093742:cmsbot_crab_collector - 0
extraJDL-check.sh 241126_093743:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-26T11:05:04Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2024-11-26 12:05:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1256/console

```
RETRY TESTS:
numCores-check.sh 241126_093725:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241126_093718:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241126_093719:cmsbot_crab_transferLogs - 0
activity-check.sh 241126_093720:cmsbot_crab_activity - 0
inputFiles-check.sh 241126_093721:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241126_093721:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241126_093722:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241126_093723:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241126_093724:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241126_093725:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 241126_093726:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241126_093727:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241126_093728:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241126_093729:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241126_093729:cmsbot_crab_inputDBS - 0
useParent-check.sh 241126_093730:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241126_093731:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241126_093732:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241126_093733:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241126_093734:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241126_093735:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241126_093736:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241126_093737:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241126_093738:cmsbot_crab_whitelist - 0
blacklist-check.sh 241126_093738:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241126_093739:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241126_093740:cmsbot_crab_voRole - 0
voGroup-check.sh 241126_093741:cmsbot_crab_voGroup - 0
scheddName-check.sh 241126_093741:cmsbot_crab_scheddName - 0
collector-check.sh 241126_093742:cmsbot_crab_collector - 0
extraJDL-check.sh 241126_093743:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-26T11:29:47Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 4. Test is done.
**Finished at:** 2024-11-26 12:29:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1258/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241126_093718:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241126_093719:cmsbot_crab_transferLogs - 0
activity-check.sh 241126_093720:cmsbot_crab_activity - 0
inputFiles-check.sh 241126_093721:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241126_093721:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241126_093722:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241126_093723:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241126_093724:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241126_093725:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241126_093725:cmsbot_crab_numCores - 0
scriptExe-check.sh 241126_093726:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241126_093727:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241126_093728:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241126_093729:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241126_093729:cmsbot_crab_inputDBS - 0
useParent-check.sh 241126_093730:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241126_093731:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241126_093732:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241126_093733:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241126_093734:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241126_093735:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241126_093736:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241126_093737:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241126_093738:cmsbot_crab_whitelist - 0
blacklist-check.sh 241126_093738:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241126_093739:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241126_093740:cmsbot_crab_voRole - 0
voGroup-check.sh 241126_093741:cmsbot_crab_voGroup - 0
scheddName-check.sh 241126_093741:cmsbot_crab_scheddName - 0
collector-check.sh 241126_093742:cmsbot_crab_collector - 0
extraJDL-check.sh 241126_093743:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
