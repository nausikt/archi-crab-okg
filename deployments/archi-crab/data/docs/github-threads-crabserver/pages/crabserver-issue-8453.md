# dmwm/CRABServer issue #8453: #786: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-31T15:57:11Z
Closed: 2024-06-03T10:11:24Z
URL: https://github.com/dmwm/CRABServer/issues/8453

## Opening post (cmsdmwmbot, 2024-05-31T15:57:11Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-05-31 17:57:10
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/786/)

## Comment (cmsdmwmbot, 2024-05-31T15:58:56Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240531_155731:cmsbot_crab_transferOutputs
240531_155733:cmsbot_crab_transferLogs
240531_155735:cmsbot_crab_activity
240531_155737:cmsbot_crab_inputFiles
240531_155739:cmsbot_crab_disableAutomaticOutputCollection
240531_155741:cmsbot_crab_outputFiles
240531_155744:cmsbot_crab_allowUndistributedCMSSW
240531_155745:cmsbot_crab_maxMemoryMB
240531_155748:cmsbot_crab_maxJobRuntimeMin
240531_155750:cmsbot_crab_numCores
240531_155752:cmsbot_crab_scriptExe
240531_155754:cmsbot_crab_scriptArgs
240531_155756:cmsbot_crab_sendVenvFolder
240531_155758:cmsbot_crab_sendExternalFolder
240531_155800:cmsbot_crab_inputDBS
240531_155802:cmsbot_crab_useParent
240531_155804:cmsbot_crab_secondaryInputDataset
240531_155806:cmsbot_crab_lumiMaskFile
240531_155809:cmsbot_crab_lumiMaskUrl
240531_155812:cmsbot_crab_outLFNDirBase
240531_155814:cmsbot_crab_runRange
240531_155816:cmsbot_crab_ignoreLocality
240531_155818:cmsbot_crab_userInputFiles
240531_155820:cmsbot_crab_whitelist
240531_155822:cmsbot_crab_blacklist
240531_155824:cmsbot_crab_ignoreGlobalBlacklist
240531_155826:cmsbot_crab_voRole
240531_155828:cmsbot_crab_voGroup
240531_155830:cmsbot_crab_scheddName
240531_155832:cmsbot_crab_collector
240531_155834:cmsbot_crab_extraJDL
```

Finished at: 2024-05-31 17:58:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/786/console)

## Comment (cmsdmwmbot, 2024-05-31T16:27:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-31 18:27:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1077/console

```
RETRY TESTS:
lumiMaskFile-check.sh 240531_155806:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240531_155809:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240531_155812:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240531_155814:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240531_155818:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240531_155820:cmsbot_crab_whitelist - 2
blacklist-check.sh 240531_155822:cmsbot_crab_blacklist - 2
voRole-check.sh 240531_155826:cmsbot_crab_voRole - 2
voGroup-check.sh 240531_155828:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240531_155731:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240531_155733:cmsbot_crab_transferLogs - 0
activity-check.sh 240531_155735:cmsbot_crab_activity - 0
inputFiles-check.sh 240531_155737:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240531_155739:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240531_155744:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240531_155745:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240531_155748:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240531_155752:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240531_155754:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240531_155756:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240531_155758:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240531_155800:cmsbot_crab_inputDBS - 0
useParent-check.sh 240531_155802:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240531_155804:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240531_155816:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240531_155824:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240531_155830:cmsbot_crab_scheddName - 0
collector-check.sh 240531_155832:cmsbot_crab_collector - 0
extraJDL-check.sh 240531_155834:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240531_155741:cmsbot_crab_outputFiles - 1
numCores-check.sh 240531_155750:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-05-31T16:53:54Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-05-31 18:53:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1078/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240531_155731:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240531_155733:cmsbot_crab_transferLogs - 0
activity-check.sh 240531_155735:cmsbot_crab_activity - 0
inputFiles-check.sh 240531_155737:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240531_155739:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240531_155744:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240531_155745:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240531_155748:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240531_155752:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240531_155754:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240531_155756:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240531_155758:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240531_155800:cmsbot_crab_inputDBS - 0
useParent-check.sh 240531_155802:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240531_155804:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240531_155806:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240531_155809:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240531_155812:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240531_155814:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240531_155816:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240531_155818:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240531_155820:cmsbot_crab_whitelist - 0
blacklist-check.sh 240531_155822:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240531_155824:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240531_155826:cmsbot_crab_voRole - 0
voGroup-check.sh 240531_155828:cmsbot_crab_voGroup - 0
scheddName-check.sh 240531_155830:cmsbot_crab_scheddName - 0
collector-check.sh 240531_155832:cmsbot_crab_collector - 0
extraJDL-check.sh 240531_155834:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240531_155741:cmsbot_crab_outputFiles - 1
numCores-check.sh 240531_155750:cmsbot_crab_numCores - 1
```
