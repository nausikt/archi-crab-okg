# dmwm/CRABServer issue #8117: #630: Test dev CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-12-19T20:27:09Z
Closed: 2023-12-20T11:23:34Z
URL: https://github.com/dmwm/CRABServer/issues/8117

## Opening post (cmsdmwmbot, 2023-12-19T20:27:09Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-19 21:27:08
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/630/)

## Comment (cmsdmwmbot, 2023-12-19T20:29:26Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_202752:cmsbot_crab_transferOutputs
231219_202754:cmsbot_crab_transferLogs
231219_202756:cmsbot_crab_activity
231219_202758:cmsbot_crab_inputFiles
231219_202800:cmsbot_crab_disableAutomaticOutputCollection
231219_202802:cmsbot_crab_outputFiles
231219_202804:cmsbot_crab_allowUndistributedCMSSW
231219_202806:cmsbot_crab_maxMemoryMB
231219_202808:cmsbot_crab_maxJobRuntimeMin
231219_202811:cmsbot_crab_numCores
231219_202813:cmsbot_crab_scriptExe
231219_202815:cmsbot_crab_scriptArgs
231219_202817:cmsbot_crab_sendVenvFolder
231219_202826:cmsbot_crab_sendExternalFolder
231219_202829:cmsbot_crab_inputDBS
231219_202831:cmsbot_crab_useParent
231219_202833:cmsbot_crab_secondaryInputDataset
231219_202835:cmsbot_crab_lumiMaskFile
231219_202837:cmsbot_crab_lumiMaskUrl
231219_202841:cmsbot_crab_outLFNDirBase
231219_202843:cmsbot_crab_runRange
231219_202845:cmsbot_crab_ignoreLocality
231219_202847:cmsbot_crab_userInputFiles
231219_202849:cmsbot_crab_whitelist
231219_202851:cmsbot_crab_blacklist
231219_202854:cmsbot_crab_ignoreGlobalBlacklist
231219_202856:cmsbot_crab_voRole
231219_202858:cmsbot_crab_voGroup
231219_202900:cmsbot_crab_scheddName
231219_202902:cmsbot_crab_collector
231219_202904:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 21:29:05
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/630/console)

## Comment (cmsdmwmbot, 2023-12-19T20:55:38Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 21:55:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/803/console

```
RETRY TESTS:
numCores-check.sh 231219_202811:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 231219_202837:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231219_202843:cmsbot_crab_runRange - 2
whitelist-check.sh 231219_202849:cmsbot_crab_whitelist - 2
blacklist-check.sh 231219_202851:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_202752:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_202754:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_202756:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_202758:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_202800:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_202802:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_202804:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_202806:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_202808:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 231219_202813:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_202815:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_202817:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_202826:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_202829:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_202831:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_202833:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_202835:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_202841:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231219_202845:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_202847:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231219_202854:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_202856:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_202858:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_202900:cmsbot_crab_scheddName - 0
collector-check.sh 231219_202902:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_202904:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T21:19:54Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-12-19 22:19:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/808/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_202752:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_202754:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_202756:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_202758:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_202800:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_202802:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_202804:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_202806:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_202808:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_202811:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_202813:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_202815:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_202817:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_202826:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_202829:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_202831:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_202833:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_202835:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231219_202837:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231219_202841:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_202843:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_202845:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_202847:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_202849:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_202851:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_202854:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_202856:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_202858:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_202900:cmsbot_crab_scheddName - 0
collector-check.sh 231219_202902:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_202904:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (mapellidario, 2023-12-20T11:23:35Z)

looks good to me
