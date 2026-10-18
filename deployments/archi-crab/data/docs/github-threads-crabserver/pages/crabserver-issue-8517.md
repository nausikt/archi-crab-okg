# dmwm/CRABServer issue #8517: #812: Test dev CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2024-06-19T13:07:32Z
Closed: 2024-06-19T14:33:15Z
URL: https://github.com/dmwm/CRABServer/issues/8517

## Opening post (cmsdmwmbot, 2024-06-19T13:07:32Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-06-19 15:07:32
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/812/)

## Comment (cmsdmwmbot, 2024-06-19T13:09:29Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240619_130805:cmsbot_crab_transferOutputs
240619_130807:cmsbot_crab_transferLogs
240619_130809:cmsbot_crab_activity
240619_130812:cmsbot_crab_inputFiles
240619_130814:cmsbot_crab_disableAutomaticOutputCollection
240619_130817:cmsbot_crab_outputFiles
240619_130819:cmsbot_crab_allowUndistributedCMSSW
240619_130821:cmsbot_crab_maxMemoryMB
240619_130823:cmsbot_crab_maxJobRuntimeMin
240619_130826:cmsbot_crab_numCores
240619_130828:cmsbot_crab_scriptExe
240619_130830:cmsbot_crab_scriptArgs
240619_130834:cmsbot_crab_sendVenvFolder
240619_130837:cmsbot_crab_sendExternalFolder
240619_130838:cmsbot_crab_inputDBS
240619_130840:cmsbot_crab_useParent
240619_130842:cmsbot_crab_secondaryInputDataset
240619_130844:cmsbot_crab_lumiMaskFile
240619_130846:cmsbot_crab_outLFNDirBase
240619_130847:cmsbot_crab_runRange
240619_130849:cmsbot_crab_ignoreLocality
240619_130850:cmsbot_crab_userInputFiles
240619_130853:cmsbot_crab_whitelist
240619_130854:cmsbot_crab_blacklist
240619_130856:cmsbot_crab_ignoreGlobalBlacklist
240619_130859:cmsbot_crab_voRole
240619_130901:cmsbot_crab_voGroup
240619_130903:cmsbot_crab_scheddName
240619_130905:cmsbot_crab_collector
240619_130907:cmsbot_crab_extraJDL
```

Finished at: 2024-06-19 15:09:08
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/812/console)

## Comment (cmsdmwmbot, 2024-06-19T13:32:57Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-19 15:32:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1134/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
outputFiles-check.sh 240619_130817:cmsbot_crab_outputFiles - 0
inputDBS-check.sh 240619_130838:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240619_130842:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240619_130844:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240619_130846:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240619_130847:cmsbot_crab_runRange - 0
userInputFiles-check.sh 240619_130850:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240619_130853:cmsbot_crab_whitelist - 0

FAILED TESTS:
transferOutputs-check.sh 240619_130805:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240619_130807:cmsbot_crab_transferLogs - 1
activity-check.sh 240619_130809:cmsbot_crab_activity - 1
inputFiles-check.sh 240619_130812:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240619_130814:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240619_130819:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240619_130821:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240619_130823:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240619_130826:cmsbot_crab_numCores - 1
scriptExe-check.sh 240619_130828:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240619_130830:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240619_130834:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240619_130837:cmsbot_crab_sendExternalFolder - 1
useParent-check.sh 240619_130840:cmsbot_crab_useParent - 1
ignoreLocality-check.sh 240619_130849:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 240619_130854:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240619_130856:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240619_130859:cmsbot_crab_voRole - 1
voGroup-check.sh 240619_130901:cmsbot_crab_voGroup - 1
scheddName-check.sh 240619_130903:cmsbot_crab_scheddName - 1
collector-check.sh 240619_130905:cmsbot_crab_collector - 1
extraJDL-check.sh 240619_130907:cmsbot_crab_extraJDL - 1
```

## Comment (belforte, 2024-06-19T14:27:04Z)

something did not work as expected. ONly a subset of the full test suits works on SL6

## Comment (belforte, 2024-06-19T14:33:15Z)

explanation is simply that for CMSSW_7 we need dataset `/GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO` which currently is only on tape. Our tests are not prepared to deal with tape recall.
Let's call it success and move on !
