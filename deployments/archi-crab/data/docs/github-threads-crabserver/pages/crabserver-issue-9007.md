# dmwm/CRABServer issue #9007: #953: Test dev CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2025-03-19T15:37:46Z
Closed: 2025-03-19T16:03:34Z
URL: https://github.com/dmwm/CRABServer/issues/9007

## Opening post (cmsdmwmbot, 2025-03-19T15:37:46Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2025-03-19 16:37:44
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/953/)

## Comment (cmsdmwmbot, 2025-03-19T15:38:43Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_153756:cmsbot_crab_20250319_163756
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_153757:cmsbot_crab_transferOutputs
250319_153758:cmsbot_crab_transferLogs
250319_153759:cmsbot_crab_activity
250319_153800:cmsbot_crab_inputFiles
250319_153801:cmsbot_crab_disableAutomaticOutputCollection
250319_153801:cmsbot_crab_outputFiles
250319_153802:cmsbot_crab_allowUndistributedCMSSW
250319_153803:cmsbot_crab_maxMemoryMB
250319_153804:cmsbot_crab_maxJobRuntimeMin
250319_153805:cmsbot_crab_numCores
250319_153805:cmsbot_crab_scriptExe
250319_153806:cmsbot_crab_scriptArgs
250319_153807:cmsbot_crab_sendVenvFolder
250319_153808:cmsbot_crab_sendExternalFolder
250319_153808:cmsbot_crab_inputDBS
250319_153809:cmsbot_crab_useParent
250319_153810:cmsbot_crab_secondaryInputDataset
250319_153811:cmsbot_crab_lumiMaskFile
250319_153812:cmsbot_crab_lumiMaskUrl
250319_153813:cmsbot_crab_outLFNDirBase
250319_153814:cmsbot_crab_runRange
250319_153815:cmsbot_crab_ignoreLocality
250319_153815:cmsbot_crab_userInputFiles
250319_153816:cmsbot_crab_whitelist
250319_153817:cmsbot_crab_blacklist
250319_153817:cmsbot_crab_ignoreGlobalBlacklist
250319_153818:cmsbot_crab_voRole
250319_153819:cmsbot_crab_voGroup
250319_153820:cmsbot_crab_scheddName
250319_153820:cmsbot_crab_collector
250319_153821:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 16:38:21
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/953/console)

## Comment (cmsdmwmbot, 2025-03-19T16:00:56Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-03-19 17:00:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1286/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250319_153757:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250319_153758:cmsbot_crab_transferLogs - 0
activity-check.sh 250319_153759:cmsbot_crab_activity - 0
inputFiles-check.sh 250319_153800:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250319_153801:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250319_153801:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250319_153802:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250319_153803:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250319_153804:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250319_153805:cmsbot_crab_numCores - 0
scriptExe-check.sh 250319_153805:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250319_153806:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250319_153807:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250319_153808:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250319_153808:cmsbot_crab_inputDBS - 0
useParent-check.sh 250319_153809:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250319_153810:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_153811:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250319_153812:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250319_153813:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_153814:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250319_153815:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250319_153815:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_153816:cmsbot_crab_whitelist - 0
blacklist-check.sh 250319_153817:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250319_153817:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250319_153818:cmsbot_crab_voRole - 0
voGroup-check.sh 250319_153819:cmsbot_crab_voGroup - 0
scheddName-check.sh 250319_153820:cmsbot_crab_scheddName - 0
collector-check.sh 250319_153820:cmsbot_crab_collector - 0
extraJDL-check.sh 250319_153821:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```

## Comment (cmsdmwmbot, 2025-03-19T16:01:01Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-03-19 17:01:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/618/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/618//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.
