# dmwm/CRABServer issue #8710: #835: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-20T16:19:04Z
Closed: 2024-09-23T21:04:24Z
URL: https://github.com/dmwm/CRABServer/issues/8710

## Opening post (cmsdmwmbot, 2024-09-20T16:19:04Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-09-20 18:19:04
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/835/)

## Comment (cmsdmwmbot, 2024-09-20T16:21:02Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240920_161922:cmsbot_crab_transferOutputs
240920_161925:cmsbot_crab_transferLogs
240920_161927:cmsbot_crab_activity
240920_161929:cmsbot_crab_inputFiles
240920_161932:cmsbot_crab_disableAutomaticOutputCollection
240920_161935:cmsbot_crab_outputFiles
240920_161938:cmsbot_crab_allowUndistributedCMSSW
240920_161940:cmsbot_crab_maxMemoryMB
240920_161943:cmsbot_crab_maxJobRuntimeMin
240920_161945:cmsbot_crab_numCores
240920_161948:cmsbot_crab_scriptExe
240920_161950:cmsbot_crab_scriptArgs
240920_161953:cmsbot_crab_sendVenvFolder
240920_161956:cmsbot_crab_sendExternalFolder
240920_161958:cmsbot_crab_inputDBS
240920_162001:cmsbot_crab_useParent
240920_162004:cmsbot_crab_secondaryInputDataset
240920_162006:cmsbot_crab_lumiMaskFile
240920_162009:cmsbot_crab_lumiMaskUrl
240920_162012:cmsbot_crab_outLFNDirBase
240920_162015:cmsbot_crab_runRange
240920_162017:cmsbot_crab_ignoreLocality
240920_162020:cmsbot_crab_userInputFiles
240920_162022:cmsbot_crab_whitelist
240920_162025:cmsbot_crab_blacklist
240920_162027:cmsbot_crab_ignoreGlobalBlacklist
240920_162030:cmsbot_crab_voRole
240920_162033:cmsbot_crab_voGroup
240920_162035:cmsbot_crab_scheddName
240920_162038:cmsbot_crab_collector
240920_162040:cmsbot_crab_extraJDL
```

Finished at: 2024-09-20 18:20:41
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/835/console)

## Comment (cmsdmwmbot, 2024-09-20T16:44:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-20 18:44:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1174/console

```
RETRY TESTS:
transferLogs-check.sh 240920_161925:cmsbot_crab_transferLogs - 2
activity-check.sh 240920_161927:cmsbot_crab_activity - 2
outputFiles-check.sh 240920_161935:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240920_161940:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240920_161943:cmsbot_crab_maxJobRuntimeMin - 2
scriptArgs-check.sh 240920_161950:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240920_162006:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240920_162009:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240920_162012:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240920_162015:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240920_162017:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 240920_162020:cmsbot_crab_userInputFiles - 2
voRole-check.sh 240920_162030:cmsbot_crab_voRole - 2
voGroup-check.sh 240920_162033:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_161922:cmsbot_crab_transferOutputs - 0
allowUndistributedCMSSW-check.sh 240920_161938:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240920_161953:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_161956:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_161958:cmsbot_crab_inputDBS - 0
extraJDL-check.sh 240920_162040:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputFiles-check.sh 240920_161929:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_161932:cmsbot_crab_disableAutomaticOutputCollection - 1
numCores-check.sh 240920_161945:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_161948:cmsbot_crab_scriptExe - 1
useParent-check.sh 240920_162001:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_162004:cmsbot_crab_secondaryInputDataset - 1
whitelist-check.sh 240920_162022:cmsbot_crab_whitelist - 1
blacklist-check.sh 240920_162025:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_162027:cmsbot_crab_ignoreGlobalBlacklist - 1
scheddName-check.sh 240920_162035:cmsbot_crab_scheddName - 1
collector-check.sh 240920_162038:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-09-20T17:08:08Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-09-20 19:08:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1177/console

```
RETRY TESTS:
activity-check.sh 240920_161927:cmsbot_crab_activity - 2
outputFiles-check.sh 240920_161935:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240920_161940:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240920_161943:cmsbot_crab_maxJobRuntimeMin - 2
scriptArgs-check.sh 240920_161950:cmsbot_crab_scriptArgs - 2
runRange-check.sh 240920_162015:cmsbot_crab_runRange - 2
voRole-check.sh 240920_162030:cmsbot_crab_voRole - 2
voGroup-check.sh 240920_162033:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_161922:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_161925:cmsbot_crab_transferLogs - 0
allowUndistributedCMSSW-check.sh 240920_161938:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240920_161953:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_161956:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_161958:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240920_162006:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240920_162009:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_162012:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_162017:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_162020:cmsbot_crab_userInputFiles - 0
extraJDL-check.sh 240920_162040:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputFiles-check.sh 240920_161929:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_161932:cmsbot_crab_disableAutomaticOutputCollection - 1
numCores-check.sh 240920_161945:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_161948:cmsbot_crab_scriptExe - 1
useParent-check.sh 240920_162001:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_162004:cmsbot_crab_secondaryInputDataset - 1
whitelist-check.sh 240920_162022:cmsbot_crab_whitelist - 1
blacklist-check.sh 240920_162025:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_162027:cmsbot_crab_ignoreGlobalBlacklist - 1
scheddName-check.sh 240920_162035:cmsbot_crab_scheddName - 1
collector-check.sh 240920_162038:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-09-20T17:32:11Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-09-20 19:32:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1180/console

```
RETRY TESTS:
scriptArgs-check.sh 240920_161950:cmsbot_crab_scriptArgs - 2
runRange-check.sh 240920_162015:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_161922:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_161925:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_161927:cmsbot_crab_activity - 0
outputFiles-check.sh 240920_161935:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_161938:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240920_161940:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240920_161943:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 240920_161953:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_161956:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_161958:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240920_162006:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240920_162009:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_162012:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_162017:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_162020:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240920_162030:cmsbot_crab_voRole - 0
voGroup-check.sh 240920_162033:cmsbot_crab_voGroup - 0
extraJDL-check.sh 240920_162040:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputFiles-check.sh 240920_161929:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_161932:cmsbot_crab_disableAutomaticOutputCollection - 1
numCores-check.sh 240920_161945:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_161948:cmsbot_crab_scriptExe - 1
useParent-check.sh 240920_162001:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_162004:cmsbot_crab_secondaryInputDataset - 1
whitelist-check.sh 240920_162022:cmsbot_crab_whitelist - 1
blacklist-check.sh 240920_162025:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_162027:cmsbot_crab_ignoreGlobalBlacklist - 1
scheddName-check.sh 240920_162035:cmsbot_crab_scheddName - 1
collector-check.sh 240920_162038:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-09-20T17:56:10Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-09-20 19:56:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1183/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_161922:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_161925:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_161927:cmsbot_crab_activity - 0
outputFiles-check.sh 240920_161935:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_161938:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240920_161940:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240920_161943:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 240920_161950:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_161953:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_161956:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_161958:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240920_162006:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240920_162009:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_162012:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240920_162015:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240920_162017:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_162020:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240920_162030:cmsbot_crab_voRole - 0
voGroup-check.sh 240920_162033:cmsbot_crab_voGroup - 0
extraJDL-check.sh 240920_162040:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputFiles-check.sh 240920_161929:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_161932:cmsbot_crab_disableAutomaticOutputCollection - 1
numCores-check.sh 240920_161945:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_161948:cmsbot_crab_scriptExe - 1
useParent-check.sh 240920_162001:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_162004:cmsbot_crab_secondaryInputDataset - 1
whitelist-check.sh 240920_162022:cmsbot_crab_whitelist - 1
blacklist-check.sh 240920_162025:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_162027:cmsbot_crab_ignoreGlobalBlacklist - 1
scheddName-check.sh 240920_162035:cmsbot_crab_scheddName - 1
collector-check.sh 240920_162038:cmsbot_crab_collector - 1
```
