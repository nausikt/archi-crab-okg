# dmwm/CRABServer issue #8207: #691: Test prod CRABClient using test2 REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2024-01-30T20:48:27Z
Closed: 2024-01-31T13:58:11Z
URL: https://github.com/dmwm/CRABServer/issues/8207

## Opening post (cmsdmwmbot, 2024-01-30T20:48:27Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-01-30 21:48:26
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/691/)

## Comment (cmsdmwmbot, 2024-01-30T20:50:18Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240130_204855:cmsbot_crab_transferOutputs
240130_204857:cmsbot_crab_transferLogs
240130_204859:cmsbot_crab_activity
240130_204902:cmsbot_crab_inputFiles
240130_204904:cmsbot_crab_disableAutomaticOutputCollection
240130_204907:cmsbot_crab_outputFiles
240130_204909:cmsbot_crab_allowUndistributedCMSSW
240130_204911:cmsbot_crab_maxMemoryMB
240130_204913:cmsbot_crab_maxJobRuntimeMin
240130_204915:cmsbot_crab_numCores
240130_204917:cmsbot_crab_scriptExe
240130_204919:cmsbot_crab_scriptArgs
240130_204922:cmsbot_crab_sendVenvFolder
240130_204928:cmsbot_crab_sendExternalFolder
240130_204928:cmsbot_crab_inputDBS
240130_204930:cmsbot_crab_useParent
240130_204932:cmsbot_crab_secondaryInputDataset
240130_204934:cmsbot_crab_lumiMaskFile
240130_204937:cmsbot_crab_outLFNDirBase
240130_204938:cmsbot_crab_runRange
240130_204939:cmsbot_crab_ignoreLocality
240130_204940:cmsbot_crab_userInputFiles
240130_204942:cmsbot_crab_whitelist
240130_204944:cmsbot_crab_blacklist
240130_204946:cmsbot_crab_ignoreGlobalBlacklist
240130_204948:cmsbot_crab_voRole
240130_204950:cmsbot_crab_voGroup
240130_204952:cmsbot_crab_scheddName
240130_204954:cmsbot_crab_collector
240130_204956:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240130_204853:cmsbot_crab_20240130_214850
```

Finished at: 2024-01-30 21:49:57
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/691/console)

## Comment (cmsdmwmbot, 2024-01-30T21:14:49Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-30 22:14:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/505/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/505//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-30T21:20:10Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-30 22:20:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/902/console

```
RETRY TESTS:
useParent-check.sh 240130_204930:cmsbot_crab_useParent - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_204855:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_204902:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_204904:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240130_204907:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240130_204909:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_204922:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240130_204928:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240130_204928:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240130_204932:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240130_204934:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240130_204937:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240130_204938:cmsbot_crab_runRange - 0
userInputFiles-check.sh 240130_204940:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240130_204942:cmsbot_crab_whitelist - 0
scheddName-check.sh 240130_204952:cmsbot_crab_scheddName - 0
collector-check.sh 240130_204954:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240130_204857:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_204859:cmsbot_crab_activity - 1
maxMemoryMB-check.sh 240130_204911:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204913:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204915:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_204917:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_204919:cmsbot_crab_scriptArgs - 1
ignoreLocality-check.sh 240130_204939:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 240130_204944:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204946:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204948:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204950:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_204956:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-01-30T21:43:57Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-01-30 22:43:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/905/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_204855:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_204902:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_204904:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240130_204907:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240130_204909:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_204922:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240130_204928:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240130_204928:cmsbot_crab_inputDBS - 0
useParent-check.sh 240130_204930:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240130_204932:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240130_204934:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240130_204937:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240130_204938:cmsbot_crab_runRange - 0
userInputFiles-check.sh 240130_204940:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240130_204942:cmsbot_crab_whitelist - 0
scheddName-check.sh 240130_204952:cmsbot_crab_scheddName - 0
collector-check.sh 240130_204954:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240130_204857:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_204859:cmsbot_crab_activity - 1
maxMemoryMB-check.sh 240130_204911:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204913:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204915:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_204917:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_204919:cmsbot_crab_scriptArgs - 1
ignoreLocality-check.sh 240130_204939:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 240130_204944:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204946:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204948:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204950:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_204956:cmsbot_crab_extraJDL - 1
```
