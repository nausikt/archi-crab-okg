# dmwm/CRABServer issue #9010: #955: Test dev CRABClient using prod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2025-03-19T17:46:48Z
Closed: 2025-03-20T09:31:59Z
URL: https://github.com/dmwm/CRABServer/issues/9010

## Opening post (cmsdmwmbot, 2025-03-19T17:46:48Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2025-03-19 18:46:47
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/955/)

## Comment (cmsdmwmbot, 2025-03-19T17:49:05Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_174702:cmsbot_crab_transferOutputs
250319_174705:cmsbot_crab_transferLogs
250319_174709:cmsbot_crab_activity
250319_174714:cmsbot_crab_inputFiles
250319_174717:cmsbot_crab_disableAutomaticOutputCollection
250319_174722:cmsbot_crab_outputFiles
250319_174725:cmsbot_crab_allowUndistributedCMSSW
250319_174728:cmsbot_crab_maxMemoryMB
250319_174731:cmsbot_crab_maxJobRuntimeMin
250319_174736:cmsbot_crab_numCores
250319_174739:cmsbot_crab_scriptExe
250319_174742:cmsbot_crab_scriptArgs
250319_174747:cmsbot_crab_sendVenvFolder
250319_174752:cmsbot_crab_sendExternalFolder
250319_174755:cmsbot_crab_inputDBS
250319_174758:cmsbot_crab_useParent
250319_174801:cmsbot_crab_secondaryInputDataset
250319_174804:cmsbot_crab_lumiMaskFile
250319_174808:cmsbot_crab_outLFNDirBase
250319_174811:cmsbot_crab_runRange
250319_174814:cmsbot_crab_ignoreLocality
250319_174816:cmsbot_crab_userInputFiles
250319_174820:cmsbot_crab_whitelist
250319_174824:cmsbot_crab_blacklist
250319_174827:cmsbot_crab_ignoreGlobalBlacklist
250319_174830:cmsbot_crab_voRole
250319_174834:cmsbot_crab_voGroup
250319_174838:cmsbot_crab_scheddName
250319_174841:cmsbot_crab_collector
250319_174843:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 18:48:44
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/955/console)

## Comment (cmsdmwmbot, 2025-03-19T18:10:17Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2025-03-19 19:10:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1288/console

```
SUCCESSFUL TESTS:
activity-check.sh 250319_174709:cmsbot_crab_activity - 0
disableAutomaticOutputCollection-check.sh 250319_174717:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250319_174722:cmsbot_crab_outputFiles - 0
maxMemoryMB-check.sh 250319_174728:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 250319_174736:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 250319_174747:cmsbot_crab_sendVenvFolder - 0
secondaryInputDataset-check.sh 250319_174801:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_174804:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 250319_174808:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_174811:cmsbot_crab_runRange - 0
userInputFiles-check.sh 250319_174816:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_174820:cmsbot_crab_whitelist - 0

FAILED TESTS:
transferOutputs-check.sh 250319_174702:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 250319_174705:cmsbot_crab_transferLogs - 1
inputFiles-check.sh 250319_174714:cmsbot_crab_inputFiles - 1
allowUndistributedCMSSW-check.sh 250319_174725:cmsbot_crab_allowUndistributedCMSSW - 1
maxJobRuntimeMin-check.sh 250319_174731:cmsbot_crab_maxJobRuntimeMin - 1
scriptExe-check.sh 250319_174739:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250319_174742:cmsbot_crab_scriptArgs - 1
sendExternalFolder-check.sh 250319_174752:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 250319_174755:cmsbot_crab_inputDBS - 1
useParent-check.sh 250319_174758:cmsbot_crab_useParent - 1
ignoreLocality-check.sh 250319_174814:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 250319_174824:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 250319_174827:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 250319_174830:cmsbot_crab_voRole - 1
voGroup-check.sh 250319_174834:cmsbot_crab_voGroup - 1
scheddName-check.sh 250319_174838:cmsbot_crab_scheddName - 1
collector-check.sh 250319_174841:cmsbot_crab_collector - 1
extraJDL-check.sh 250319_174843:cmsbot_crab_extraJDL - 1

RETRY TESTS:
 none
```

## Comment (belforte, 2025-03-20T09:31:59Z)

checks ran too soon, most DAGs were still bootstrapping , pff...
