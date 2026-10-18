# dmwm/CRABServer issue #8659: #831: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-27T20:47:43Z
Closed: 2024-10-10T22:43:01Z
URL: https://github.com/dmwm/CRABServer/issues/8659

## Opening post (cmsdmwmbot, 2024-08-27T20:47:43Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-08-27 22:47:42
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/831/)

## Comment (cmsdmwmbot, 2024-08-27T20:49:54Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240827_204807:cmsbot_crab_transferOutputs
240827_204809:cmsbot_crab_transferLogs
240827_204812:cmsbot_crab_activity
240827_204814:cmsbot_crab_inputFiles
240827_204817:cmsbot_crab_disableAutomaticOutputCollection
240827_204819:cmsbot_crab_outputFiles
240827_204822:cmsbot_crab_allowUndistributedCMSSW
240827_204824:cmsbot_crab_maxMemoryMB
240827_204827:cmsbot_crab_maxJobRuntimeMin
240827_204829:cmsbot_crab_numCores
240827_204832:cmsbot_crab_scriptExe
240827_204834:cmsbot_crab_scriptArgs
240827_204837:cmsbot_crab_sendVenvFolder
240827_204839:cmsbot_crab_sendExternalFolder
240827_204842:cmsbot_crab_inputDBS
240827_204845:cmsbot_crab_useParent
240827_204848:cmsbot_crab_secondaryInputDataset
240827_204850:cmsbot_crab_lumiMaskFile
240827_204853:cmsbot_crab_lumiMaskUrl
240827_204856:cmsbot_crab_outLFNDirBase
240827_204859:cmsbot_crab_runRange
240827_204901:cmsbot_crab_ignoreLocality
240827_204904:cmsbot_crab_userInputFiles
240827_204915:cmsbot_crab_whitelist
240827_204917:cmsbot_crab_blacklist
240827_204919:cmsbot_crab_ignoreGlobalBlacklist
240827_204922:cmsbot_crab_voRole
240827_204924:cmsbot_crab_voGroup
240827_204927:cmsbot_crab_scheddName
240827_204929:cmsbot_crab_collector
240827_204932:cmsbot_crab_extraJDL
```

Finished at: 2024-08-27 22:49:33
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/831/console)

## Comment (cmsdmwmbot, 2024-08-27T21:14:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-27 23:14:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1167/console

```
RETRY TESTS:
outputFiles-check.sh 240827_204819:cmsbot_crab_outputFiles - 2
numCores-check.sh 240827_204829:cmsbot_crab_numCores - 2
scriptExe-check.sh 240827_204832:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240827_204853:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240827_204859:cmsbot_crab_runRange - 2
whitelist-check.sh 240827_204915:cmsbot_crab_whitelist - 2
blacklist-check.sh 240827_204917:cmsbot_crab_blacklist - 2
voRole-check.sh 240827_204922:cmsbot_crab_voRole - 2
voGroup-check.sh 240827_204924:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240827_204807:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240827_204809:cmsbot_crab_transferLogs - 0
activity-check.sh 240827_204812:cmsbot_crab_activity - 0
inputFiles-check.sh 240827_204814:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240827_204817:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240827_204822:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240827_204824:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240827_204827:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 240827_204834:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240827_204837:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240827_204839:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240827_204842:cmsbot_crab_inputDBS - 0
useParent-check.sh 240827_204845:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240827_204848:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240827_204850:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240827_204856:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240827_204901:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240827_204904:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240827_204919:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240827_204927:cmsbot_crab_scheddName - 0
collector-check.sh 240827_204929:cmsbot_crab_collector - 0
extraJDL-check.sh 240827_204932:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-27T21:40:03Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-08-27 23:40:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1168/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240827_204807:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240827_204809:cmsbot_crab_transferLogs - 0
activity-check.sh 240827_204812:cmsbot_crab_activity - 0
inputFiles-check.sh 240827_204814:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240827_204817:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240827_204819:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240827_204822:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240827_204824:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240827_204827:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240827_204829:cmsbot_crab_numCores - 0
scriptExe-check.sh 240827_204832:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240827_204834:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240827_204837:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240827_204839:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240827_204842:cmsbot_crab_inputDBS - 0
useParent-check.sh 240827_204845:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240827_204848:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240827_204850:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240827_204853:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240827_204856:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240827_204859:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240827_204901:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240827_204904:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240827_204915:cmsbot_crab_whitelist - 0
blacklist-check.sh 240827_204917:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240827_204919:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240827_204922:cmsbot_crab_voRole - 0
voGroup-check.sh 240827_204924:cmsbot_crab_voGroup - 0
scheddName-check.sh 240827_204927:cmsbot_crab_scheddName - 0
collector-check.sh 240827_204929:cmsbot_crab_collector - 0
extraJDL-check.sh 240827_204932:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
