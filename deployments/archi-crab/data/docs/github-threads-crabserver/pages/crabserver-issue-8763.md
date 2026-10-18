# dmwm/CRABServer issue #8763: #866: Test GH CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-04T10:36:46Z
Closed: 2024-11-04T11:39:27Z
URL: https://github.com/dmwm/CRABServer/issues/8763

## Opening post (cmsdmwmbot, 2024-11-04T10:36:46Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **v3.241030**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-11-04 11:36:45
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/866/)

## Comment (cmsdmwmbot, 2024-11-04T10:40:42Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241104_103836:cmsbot_crab_transferOutputs
241104_103840:cmsbot_crab_transferLogs
241104_103843:cmsbot_crab_activity
241104_103847:cmsbot_crab_inputFiles
241104_103851:cmsbot_crab_disableAutomaticOutputCollection
241104_103854:cmsbot_crab_outputFiles
241104_103858:cmsbot_crab_allowUndistributedCMSSW
241104_103901:cmsbot_crab_maxMemoryMB
241104_103904:cmsbot_crab_maxJobRuntimeMin
241104_103908:cmsbot_crab_numCores
241104_103911:cmsbot_crab_scriptExe
241104_103915:cmsbot_crab_scriptArgs
241104_103918:cmsbot_crab_sendVenvFolder
241104_103922:cmsbot_crab_sendExternalFolder
241104_103925:cmsbot_crab_inputDBS
241104_103928:cmsbot_crab_useParent
241104_103932:cmsbot_crab_secondaryInputDataset
241104_103935:cmsbot_crab_lumiMaskFile
241104_103939:cmsbot_crab_lumiMaskUrl
241104_103943:cmsbot_crab_outLFNDirBase
241104_103946:cmsbot_crab_runRange
241104_103949:cmsbot_crab_ignoreLocality
241104_103953:cmsbot_crab_userInputFiles
241104_103956:cmsbot_crab_whitelist
241104_104000:cmsbot_crab_blacklist
241104_104003:cmsbot_crab_ignoreGlobalBlacklist
241104_104007:cmsbot_crab_voRole
241104_104010:cmsbot_crab_voGroup
241104_104013:cmsbot_crab_scheddName
241104_104017:cmsbot_crab_collector
241104_104020:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241104_103817:cmsbot_crab_20241104_113814
```

Finished at: 2024-11-04 11:40:21
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/866/console)

## Comment (cmsdmwmbot, 2024-11-04T11:04:37Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-11-04 12:04:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/560/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/560//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-11-04T11:05:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-04 12:05:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1217/console

```
RETRY TESTS:
transferLogs-check.sh 241104_103840:cmsbot_crab_transferLogs - 2
activity-check.sh 241104_103843:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 241104_103901:cmsbot_crab_maxMemoryMB - 2
useParent-check.sh 241104_103928:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 241104_103939:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241104_103943:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241104_103946:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241104_103953:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241104_103956:cmsbot_crab_whitelist - 2
blacklist-check.sh 241104_104000:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241104_103836:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241104_103847:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241104_103851:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241104_103854:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241104_103858:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 241104_103904:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241104_103908:cmsbot_crab_numCores - 0
scriptExe-check.sh 241104_103911:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241104_103915:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241104_103918:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241104_103922:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241104_103925:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 241104_103932:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241104_103935:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 241104_103949:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 241104_104003:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241104_104007:cmsbot_crab_voRole - 0
voGroup-check.sh 241104_104010:cmsbot_crab_voGroup - 0
scheddName-check.sh 241104_104013:cmsbot_crab_scheddName - 0
collector-check.sh 241104_104017:cmsbot_crab_collector - 0
extraJDL-check.sh 241104_104020:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-04T11:29:34Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-04 12:29:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1218/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241104_103836:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241104_103840:cmsbot_crab_transferLogs - 0
activity-check.sh 241104_103843:cmsbot_crab_activity - 0
inputFiles-check.sh 241104_103847:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241104_103851:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241104_103854:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241104_103858:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241104_103901:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241104_103904:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241104_103908:cmsbot_crab_numCores - 0
scriptExe-check.sh 241104_103911:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241104_103915:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241104_103918:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241104_103922:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241104_103925:cmsbot_crab_inputDBS - 0
useParent-check.sh 241104_103928:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241104_103932:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241104_103935:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241104_103939:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241104_103943:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241104_103946:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241104_103949:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241104_103953:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241104_103956:cmsbot_crab_whitelist - 0
blacklist-check.sh 241104_104000:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241104_104003:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241104_104007:cmsbot_crab_voRole - 0
voGroup-check.sh 241104_104010:cmsbot_crab_voGroup - 0
scheddName-check.sh 241104_104013:cmsbot_crab_scheddName - 0
collector-check.sh 241104_104017:cmsbot_crab_collector - 0
extraJDL-check.sh 241104_104020:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-11-04T11:39:27Z)

all OK
