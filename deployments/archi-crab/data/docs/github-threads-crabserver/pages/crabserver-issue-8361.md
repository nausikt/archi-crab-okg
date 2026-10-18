# dmwm/CRABServer issue #8361: #764: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-25T20:19:41Z
Closed: 2024-04-26T14:01:37Z
URL: https://github.com/dmwm/CRABServer/issues/8361

## Opening post (cmsdmwmbot, 2024-04-25T20:19:41Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-04-25 22:19:40
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/764/)

## Comment (cmsdmwmbot, 2024-04-25T20:21:27Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240425_202002:cmsbot_crab_transferOutputs
240425_202005:cmsbot_crab_transferLogs
240425_202007:cmsbot_crab_activity
240425_202009:cmsbot_crab_inputFiles
240425_202011:cmsbot_crab_disableAutomaticOutputCollection
240425_202013:cmsbot_crab_outputFiles
240425_202015:cmsbot_crab_allowUndistributedCMSSW
240425_202017:cmsbot_crab_maxMemoryMB
240425_202019:cmsbot_crab_maxJobRuntimeMin
240425_202021:cmsbot_crab_numCores
240425_202023:cmsbot_crab_scriptExe
240425_202025:cmsbot_crab_scriptArgs
240425_202027:cmsbot_crab_sendVenvFolder
240425_202029:cmsbot_crab_sendExternalFolder
240425_202031:cmsbot_crab_inputDBS
240425_202033:cmsbot_crab_useParent
240425_202035:cmsbot_crab_secondaryInputDataset
240425_202037:cmsbot_crab_lumiMaskFile
240425_202039:cmsbot_crab_lumiMaskUrl
240425_202042:cmsbot_crab_outLFNDirBase
240425_202044:cmsbot_crab_runRange
240425_202046:cmsbot_crab_ignoreLocality
240425_202048:cmsbot_crab_userInputFiles
240425_202051:cmsbot_crab_whitelist
240425_202053:cmsbot_crab_blacklist
240425_202055:cmsbot_crab_ignoreGlobalBlacklist
240425_202057:cmsbot_crab_voRole
240425_202059:cmsbot_crab_voGroup
240425_202101:cmsbot_crab_scheddName
240425_202103:cmsbot_crab_collector
240425_202105:cmsbot_crab_extraJDL
```

Finished at: 2024-04-25 22:21:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/764/console)

## Comment (cmsdmwmbot, 2024-04-25T22:06:26Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 0. Test failed. Investigate manually
**Finished at:** 2024-04-26 00:06:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1049/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240425_202002:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240425_202005:cmsbot_crab_transferLogs - 0
activity-check.sh 240425_202007:cmsbot_crab_activity - 0
inputFiles-check.sh 240425_202009:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240425_202011:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240425_202015:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240425_202017:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240425_202019:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240425_202021:cmsbot_crab_numCores - 0
scriptExe-check.sh 240425_202023:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240425_202025:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240425_202027:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240425_202029:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240425_202031:cmsbot_crab_inputDBS - 0
useParent-check.sh 240425_202033:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240425_202035:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240425_202037:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240425_202039:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240425_202042:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240425_202044:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240425_202046:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240425_202048:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240425_202051:cmsbot_crab_whitelist - 0
blacklist-check.sh 240425_202053:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240425_202055:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240425_202057:cmsbot_crab_voRole - 0
voGroup-check.sh 240425_202059:cmsbot_crab_voGroup - 0
scheddName-check.sh 240425_202101:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240425_202105:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240425_202013:cmsbot_crab_outputFiles - 1
collector-check.sh 240425_202103:cmsbot_crab_collector - 1
```
