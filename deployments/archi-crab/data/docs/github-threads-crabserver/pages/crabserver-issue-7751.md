# dmwm/CRABServer issue #7751: #436: Test prod CRABClient using preprod REST instance and CMSSW_8_0_36 CMSSW release

State: closed
Opened: 2023-07-12T15:16:08Z
Closed: 2023-07-12T20:47:36Z
URL: https://github.com/dmwm/CRABServer/issues/7751

## Opening post (cmsdmwmbot, 2023-07-12T15:16:08Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_8_0_36**
- SCRAM_ARCH: **slc7_amd64_gcc530**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-07-12 17:16:07
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/436/)

## Comment (cmsdmwmbot, 2023-07-12T15:20:19Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230712_151743:cmsbot_crab_transferOutputs
230712_151748:cmsbot_crab_transferLogs
230712_151752:cmsbot_crab_activity
230712_151758:cmsbot_crab_inputFiles
230712_151802:cmsbot_crab_disableAutomaticOutputCollection
230712_151809:cmsbot_crab_outputFiles
230712_151813:cmsbot_crab_allowUndistributedCMSSW
230712_151817:cmsbot_crab_maxMemoryMB
230712_151821:cmsbot_crab_maxJobRuntimeMin
230712_151826:cmsbot_crab_numCores
230712_151831:cmsbot_crab_scriptExe
230712_151835:cmsbot_crab_scriptArgs
230712_151841:cmsbot_crab_sendPythonFolder
230712_151849:cmsbot_crab_sendExternalFolder
230712_151853:cmsbot_crab_inputDBS
230712_151857:cmsbot_crab_useParent
230712_151901:cmsbot_crab_secondaryInputDataset
230712_151905:cmsbot_crab_lumiMaskFile
230712_151908:cmsbot_crab_lumiMaskUrl
230712_151913:cmsbot_crab_outLFNDirBase
230712_151916:cmsbot_crab_runRange
230712_151920:cmsbot_crab_ignoreLocality
230712_151923:cmsbot_crab_userInputFiles
230712_151927:cmsbot_crab_whitelist
230712_151931:cmsbot_crab_blacklist
230712_151935:cmsbot_crab_ignoreGlobalBlacklist
230712_151939:cmsbot_crab_voRole
230712_151944:cmsbot_crab_voGroup
230712_151948:cmsbot_crab_scheddName
230712_151952:cmsbot_crab_collector
230712_151956:cmsbot_crab_extraJDL
```

Finished at: 2023-07-12 17:19:56
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/436/console)

## Comment (cmsdmwmbot, 2023-07-12T15:44:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-12 17:44:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/723/console

```
RETRY TESTS:
outputFiles-check.sh 230712_151809:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230712_151817:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230712_151821:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskFile-check.sh 230712_151905:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230712_151908:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230712_151913:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230712_151916:cmsbot_crab_runRange - 2
whitelist-check.sh 230712_151927:cmsbot_crab_whitelist - 2
blacklist-check.sh 230712_151931:cmsbot_crab_blacklist - 2
voRole-check.sh 230712_151939:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_151743:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_151748:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_151752:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_151758:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_151802:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230712_151813:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 230712_151826:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_151831:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_151835:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_151841:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_151849:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_151853:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_151857:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_151901:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 230712_151920:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_151923:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230712_151935:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230712_151944:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_151948:cmsbot_crab_scheddName - 0
collector-check.sh 230712_151952:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_151956:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-12T16:07:41Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-12 18:07:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/725/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
useParent-check.sh 230712_151857:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_151901:cmsbot_crab_secondaryInputDataset - 0
userInputFiles-check.sh 230712_151923:cmsbot_crab_userInputFiles - 0

FAILED TESTS:
transferOutputs-check.sh 230712_151743:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230712_151748:cmsbot_crab_transferLogs - 1
activity-check.sh 230712_151752:cmsbot_crab_activity - 1
inputFiles-check.sh 230712_151758:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 230712_151802:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230712_151809:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 230712_151813:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 230712_151817:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230712_151821:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230712_151826:cmsbot_crab_numCores - 1
scriptExe-check.sh 230712_151831:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230712_151835:cmsbot_crab_scriptArgs - 1
sendPythonFolder-check.sh 230712_151841:cmsbot_crab_sendPythonFolder - 1
sendExternalFolder-check.sh 230712_151849:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 230712_151853:cmsbot_crab_inputDBS - 1
lumiMaskFile-check.sh 230712_151905:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230712_151908:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230712_151913:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230712_151916:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230712_151920:cmsbot_crab_ignoreLocality - 1
whitelist-check.sh 230712_151927:cmsbot_crab_whitelist - 1
blacklist-check.sh 230712_151931:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230712_151935:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230712_151939:cmsbot_crab_voRole - 1
voGroup-check.sh 230712_151944:cmsbot_crab_voGroup - 1
scheddName-check.sh 230712_151948:cmsbot_crab_scheddName - 1
collector-check.sh 230712_151952:cmsbot_crab_collector - 1
extraJDL-check.sh 230712_151956:cmsbot_crab_extraJDL - 1
```

## Comment (belforte, 2023-07-12T20:47:36Z)

FAILED DUE TO GITLAB DOWNTIME
