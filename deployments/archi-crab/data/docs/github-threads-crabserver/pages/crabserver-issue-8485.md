# dmwm/CRABServer issue #8485: #801: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-11T09:47:10Z
Closed: 2024-06-11T12:56:03Z
URL: https://github.com/dmwm/CRABServer/issues/8485

## Opening post (cmsdmwmbot, 2024-06-11T09:47:10Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-06-11 11:47:09
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/801/)

## Comment (cmsdmwmbot, 2024-06-11T09:48:59Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240611_094731:cmsbot_crab_transferOutputs
240611_094735:cmsbot_crab_transferLogs
240611_094737:cmsbot_crab_activity
240611_094739:cmsbot_crab_inputFiles
240611_094741:cmsbot_crab_disableAutomaticOutputCollection
240611_094744:cmsbot_crab_outputFiles
240611_094746:cmsbot_crab_allowUndistributedCMSSW
240611_094748:cmsbot_crab_maxMemoryMB
240611_094750:cmsbot_crab_maxJobRuntimeMin
240611_094752:cmsbot_crab_numCores
240611_094754:cmsbot_crab_scriptExe
240611_094756:cmsbot_crab_scriptArgs
240611_094759:cmsbot_crab_sendVenvFolder
240611_094801:cmsbot_crab_sendExternalFolder
240611_094803:cmsbot_crab_inputDBS
240611_094805:cmsbot_crab_useParent
240611_094807:cmsbot_crab_secondaryInputDataset
240611_094809:cmsbot_crab_lumiMaskFile
240611_094811:cmsbot_crab_lumiMaskUrl
240611_094814:cmsbot_crab_outLFNDirBase
240611_094816:cmsbot_crab_runRange
240611_094818:cmsbot_crab_ignoreLocality
240611_094820:cmsbot_crab_userInputFiles
240611_094822:cmsbot_crab_whitelist
240611_094824:cmsbot_crab_blacklist
240611_094826:cmsbot_crab_ignoreGlobalBlacklist
240611_094828:cmsbot_crab_voRole
240611_094831:cmsbot_crab_voGroup
240611_094833:cmsbot_crab_scheddName
240611_094835:cmsbot_crab_collector
240611_094837:cmsbot_crab_extraJDL
```

Finished at: 2024-06-11 11:48:37
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/801/console)

## Comment (cmsdmwmbot, 2024-06-11T10:14:17Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-11 12:14:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1110/console

```
RETRY TESTS:
outputFiles-check.sh 240611_094744:cmsbot_crab_outputFiles - 2
numCores-check.sh 240611_094752:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240611_094756:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240611_094811:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240611_094816:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240611_094820:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240611_094822:cmsbot_crab_whitelist - 2
blacklist-check.sh 240611_094824:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240611_094731:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240611_094735:cmsbot_crab_transferLogs - 0
activity-check.sh 240611_094737:cmsbot_crab_activity - 0
inputFiles-check.sh 240611_094739:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240611_094741:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240611_094746:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240611_094748:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240611_094750:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240611_094754:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240611_094759:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240611_094801:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240611_094803:cmsbot_crab_inputDBS - 0
useParent-check.sh 240611_094805:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240611_094807:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240611_094809:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240611_094814:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240611_094818:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240611_094826:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240611_094828:cmsbot_crab_voRole - 0
voGroup-check.sh 240611_094831:cmsbot_crab_voGroup - 0
scheddName-check.sh 240611_094833:cmsbot_crab_scheddName - 0
collector-check.sh 240611_094835:cmsbot_crab_collector - 0
extraJDL-check.sh 240611_094837:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-11T10:39:04Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-11 12:39:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1111/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240611_094731:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240611_094735:cmsbot_crab_transferLogs - 0
activity-check.sh 240611_094737:cmsbot_crab_activity - 0
inputFiles-check.sh 240611_094739:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240611_094741:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240611_094744:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240611_094746:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240611_094748:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240611_094750:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240611_094752:cmsbot_crab_numCores - 0
scriptExe-check.sh 240611_094754:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240611_094756:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240611_094759:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240611_094801:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240611_094803:cmsbot_crab_inputDBS - 0
useParent-check.sh 240611_094805:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240611_094807:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240611_094809:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240611_094811:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240611_094814:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240611_094816:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240611_094818:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240611_094820:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240611_094822:cmsbot_crab_whitelist - 0
blacklist-check.sh 240611_094824:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240611_094826:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240611_094828:cmsbot_crab_voRole - 0
voGroup-check.sh 240611_094831:cmsbot_crab_voGroup - 0
scheddName-check.sh 240611_094833:cmsbot_crab_scheddName - 0
collector-check.sh 240611_094835:cmsbot_crab_collector - 0
extraJDL-check.sh 240611_094837:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-06-11T12:56:03Z)

all OK ! finally. Including resubmissions and numCores
