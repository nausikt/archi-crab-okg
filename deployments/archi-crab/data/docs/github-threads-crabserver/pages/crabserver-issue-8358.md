# dmwm/CRABServer issue #8358: #763: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-25T13:39:07Z
Closed: 2024-04-26T14:01:37Z
URL: https://github.com/dmwm/CRABServer/issues/8358

## Opening post (cmsdmwmbot, 2024-04-25T13:39:07Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-04-25 15:39:06
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/763/)

## Comment (cmsdmwmbot, 2024-04-25T13:41:12Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240425_133933:cmsbot_crab_transferOutputs
240425_133936:cmsbot_crab_transferLogs
240425_133938:cmsbot_crab_activity
240425_133941:cmsbot_crab_inputFiles
240425_133944:cmsbot_crab_disableAutomaticOutputCollection
240425_133946:cmsbot_crab_outputFiles
240425_133949:cmsbot_crab_allowUndistributedCMSSW
240425_133951:cmsbot_crab_maxMemoryMB
240425_133954:cmsbot_crab_maxJobRuntimeMin
240425_133956:cmsbot_crab_numCores
240425_133959:cmsbot_crab_scriptExe
240425_134001:cmsbot_crab_scriptArgs
240425_134004:cmsbot_crab_sendVenvFolder
240425_134006:cmsbot_crab_sendExternalFolder
240425_134009:cmsbot_crab_inputDBS
240425_134011:cmsbot_crab_useParent
240425_134014:cmsbot_crab_secondaryInputDataset
240425_134016:cmsbot_crab_lumiMaskFile
240425_134019:cmsbot_crab_lumiMaskUrl
240425_134023:cmsbot_crab_outLFNDirBase
240425_134025:cmsbot_crab_runRange
240425_134028:cmsbot_crab_ignoreLocality
240425_134031:cmsbot_crab_userInputFiles
240425_134033:cmsbot_crab_whitelist
240425_134036:cmsbot_crab_blacklist
240425_134038:cmsbot_crab_ignoreGlobalBlacklist
240425_134041:cmsbot_crab_voRole
240425_134043:cmsbot_crab_voGroup
240425_134045:cmsbot_crab_scheddName
240425_134047:cmsbot_crab_collector
240425_134049:cmsbot_crab_extraJDL
```

Finished at: 2024-04-25 15:40:50
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/763/console)

## Comment (cmsdmwmbot, 2024-04-25T14:06:36Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-25 16:06:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1044/console

```
RETRY TESTS:
maxMemoryMB-check.sh 240425_133951:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240425_133954:cmsbot_crab_maxJobRuntimeMin - 2
secondaryInputDataset-check.sh 240425_134014:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240425_134019:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240425_134025:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240425_134031:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240425_134033:cmsbot_crab_whitelist - 2
blacklist-check.sh 240425_134036:cmsbot_crab_blacklist - 2
voRole-check.sh 240425_134041:cmsbot_crab_voRole - 2
voGroup-check.sh 240425_134043:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240425_133933:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240425_133936:cmsbot_crab_transferLogs - 0
activity-check.sh 240425_133938:cmsbot_crab_activity - 0
inputFiles-check.sh 240425_133941:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240425_133944:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240425_133949:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240425_133956:cmsbot_crab_numCores - 0
scriptExe-check.sh 240425_133959:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240425_134001:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240425_134004:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240425_134006:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240425_134009:cmsbot_crab_inputDBS - 0
useParent-check.sh 240425_134011:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 240425_134016:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240425_134023:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240425_134028:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240425_134038:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240425_134045:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240425_134049:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240425_133946:cmsbot_crab_outputFiles - 1
collector-check.sh 240425_134047:cmsbot_crab_collector - 1
```
