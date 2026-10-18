# dmwm/CRABServer issue #8212: #694: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-31T16:36:29Z
Closed: 2024-01-31T19:52:06Z
URL: https://github.com/dmwm/CRABServer/issues/8212

## Opening post (cmsdmwmbot, 2024-01-31T16:36:29Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-31 17:36:28
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/694/)

## Comment (cmsdmwmbot, 2024-01-31T16:38:56Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240131_163650:cmsbot_crab_transferOutputs
240131_163652:cmsbot_crab_transferLogs
240131_163654:cmsbot_crab_activity
240131_163656:cmsbot_crab_inputFiles
240131_163658:cmsbot_crab_disableAutomaticOutputCollection
240131_163700:cmsbot_crab_outputFiles
240131_163702:cmsbot_crab_allowUndistributedCMSSW
240131_163704:cmsbot_crab_maxMemoryMB
240131_163706:cmsbot_crab_maxJobRuntimeMin
240131_163708:cmsbot_crab_numCores
240131_163710:cmsbot_crab_scriptExe
240131_163712:cmsbot_crab_scriptArgs
240131_163714:cmsbot_crab_sendVenvFolder
240131_163800:cmsbot_crab_sendExternalFolder
240131_163802:cmsbot_crab_inputDBS
240131_163804:cmsbot_crab_useParent
240131_163805:cmsbot_crab_secondaryInputDataset
240131_163807:cmsbot_crab_lumiMaskFile
240131_163809:cmsbot_crab_lumiMaskUrl
240131_163812:cmsbot_crab_outLFNDirBase
240131_163814:cmsbot_crab_runRange
240131_163816:cmsbot_crab_ignoreLocality
240131_163818:cmsbot_crab_userInputFiles
240131_163820:cmsbot_crab_whitelist
240131_163822:cmsbot_crab_blacklist
240131_163824:cmsbot_crab_ignoreGlobalBlacklist
240131_163826:cmsbot_crab_voRole
240131_163828:cmsbot_crab_voGroup
240131_163830:cmsbot_crab_scheddName
240131_163832:cmsbot_crab_collector
240131_163834:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240131_163648:cmsbot_crab_20240131_173647
```

Finished at: 2024-01-31 17:38:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/694/console)

## Comment (cmsdmwmbot, 2024-01-31T17:02:05Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-31 18:02:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/507/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/507//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-31T17:02:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-31 18:02:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/913/console

```
RETRY TESTS:
transferLogs-check.sh 240131_163652:cmsbot_crab_transferLogs - 2
useParent-check.sh 240131_163804:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 240131_163809:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240131_163814:cmsbot_crab_runRange - 2
whitelist-check.sh 240131_163820:cmsbot_crab_whitelist - 2
blacklist-check.sh 240131_163822:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240131_163650:cmsbot_crab_transferOutputs - 0
activity-check.sh 240131_163654:cmsbot_crab_activity - 0
inputFiles-check.sh 240131_163656:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240131_163658:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240131_163700:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240131_163702:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240131_163704:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240131_163706:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240131_163708:cmsbot_crab_numCores - 0
scriptExe-check.sh 240131_163710:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240131_163712:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240131_163714:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240131_163800:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240131_163802:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240131_163805:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240131_163807:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240131_163812:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240131_163816:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240131_163818:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240131_163824:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240131_163826:cmsbot_crab_voRole - 0
voGroup-check.sh 240131_163828:cmsbot_crab_voGroup - 0
scheddName-check.sh 240131_163830:cmsbot_crab_scheddName - 0
collector-check.sh 240131_163832:cmsbot_crab_collector - 0
extraJDL-check.sh 240131_163834:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-31T17:26:43Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-31 18:26:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/915/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240131_163809:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240131_163814:cmsbot_crab_runRange - 2
blacklist-check.sh 240131_163822:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240131_163650:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240131_163652:cmsbot_crab_transferLogs - 0
activity-check.sh 240131_163654:cmsbot_crab_activity - 0
inputFiles-check.sh 240131_163656:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240131_163658:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240131_163700:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240131_163702:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240131_163704:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240131_163706:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240131_163708:cmsbot_crab_numCores - 0
scriptExe-check.sh 240131_163710:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240131_163712:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240131_163714:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240131_163800:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240131_163802:cmsbot_crab_inputDBS - 0
useParent-check.sh 240131_163804:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240131_163805:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240131_163807:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240131_163812:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240131_163816:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240131_163818:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240131_163820:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240131_163824:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240131_163826:cmsbot_crab_voRole - 0
voGroup-check.sh 240131_163828:cmsbot_crab_voGroup - 0
scheddName-check.sh 240131_163830:cmsbot_crab_scheddName - 0
collector-check.sh 240131_163832:cmsbot_crab_collector - 0
extraJDL-check.sh 240131_163834:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-31T17:50:43Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-01-31 18:50:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/917/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240131_163650:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240131_163652:cmsbot_crab_transferLogs - 0
activity-check.sh 240131_163654:cmsbot_crab_activity - 0
inputFiles-check.sh 240131_163656:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240131_163658:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240131_163700:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240131_163702:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240131_163704:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240131_163706:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240131_163708:cmsbot_crab_numCores - 0
scriptExe-check.sh 240131_163710:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240131_163712:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240131_163714:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240131_163800:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240131_163802:cmsbot_crab_inputDBS - 0
useParent-check.sh 240131_163804:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240131_163805:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240131_163807:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240131_163809:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240131_163812:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240131_163814:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240131_163816:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240131_163818:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240131_163820:cmsbot_crab_whitelist - 0
blacklist-check.sh 240131_163822:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240131_163824:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240131_163826:cmsbot_crab_voRole - 0
voGroup-check.sh 240131_163828:cmsbot_crab_voGroup - 0
scheddName-check.sh 240131_163830:cmsbot_crab_scheddName - 0
collector-check.sh 240131_163832:cmsbot_crab_collector - 0
extraJDL-check.sh 240131_163834:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-31T19:52:06Z)

all OK
