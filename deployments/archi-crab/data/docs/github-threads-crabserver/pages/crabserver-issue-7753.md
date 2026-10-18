# dmwm/CRABServer issue #7753: #438: Test prod CRABClient using preprod REST instance and CMSSW_8_0_36 CMSSW release

State: closed
Opened: 2023-07-12T20:57:41Z
Closed: 2023-07-12T22:11:09Z
URL: https://github.com/dmwm/CRABServer/issues/7753

## Opening post (cmsdmwmbot, 2023-07-12T20:57:41Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_8_0_36**
- SCRAM_ARCH: **slc7_amd64_gcc530**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-07-12 22:57:40
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/438/)

## Comment (cmsdmwmbot, 2023-07-12T21:01:14Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230712_205908:cmsbot_crab_transferOutputs
230712_205911:cmsbot_crab_transferLogs
230712_205914:cmsbot_crab_activity
230712_205917:cmsbot_crab_inputFiles
230712_205920:cmsbot_crab_disableAutomaticOutputCollection
230712_205923:cmsbot_crab_outputFiles
230712_205927:cmsbot_crab_allowUndistributedCMSSW
230712_205930:cmsbot_crab_maxMemoryMB
230712_205933:cmsbot_crab_maxJobRuntimeMin
230712_205936:cmsbot_crab_numCores
230712_205938:cmsbot_crab_scriptExe
230712_205941:cmsbot_crab_scriptArgs
230712_205945:cmsbot_crab_sendPythonFolder
230712_205950:cmsbot_crab_sendExternalFolder
230712_205953:cmsbot_crab_inputDBS
230712_205956:cmsbot_crab_useParent
230712_205959:cmsbot_crab_secondaryInputDataset
230712_210003:cmsbot_crab_lumiMaskFile
230712_210006:cmsbot_crab_lumiMaskUrl
230712_210017:cmsbot_crab_outLFNDirBase
230712_210020:cmsbot_crab_runRange
230712_210024:cmsbot_crab_ignoreLocality
230712_210027:cmsbot_crab_userInputFiles
230712_210030:cmsbot_crab_whitelist
230712_210033:cmsbot_crab_blacklist
230712_210036:cmsbot_crab_ignoreGlobalBlacklist
230712_210039:cmsbot_crab_voRole
230712_210042:cmsbot_crab_voGroup
230712_210045:cmsbot_crab_scheddName
230712_210049:cmsbot_crab_collector
230712_210052:cmsbot_crab_extraJDL
```

Finished at: 2023-07-12 23:00:52
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/438/console)

## Comment (cmsdmwmbot, 2023-07-12T21:26:32Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-12 23:26:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/728/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 230712_205933:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 230712_205938:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 230712_210006:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230712_210020:cmsbot_crab_runRange - 2
whitelist-check.sh 230712_210030:cmsbot_crab_whitelist - 2
blacklist-check.sh 230712_210033:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_205908:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_205911:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_205914:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_205917:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_205920:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_205923:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_205927:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_205930:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230712_205936:cmsbot_crab_numCores - 0
scriptArgs-check.sh 230712_205941:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_205945:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_205950:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_205953:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_205956:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_205959:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_210003:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230712_210017:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230712_210024:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_210027:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230712_210036:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_210039:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_210042:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_210045:cmsbot_crab_scheddName - 0
collector-check.sh 230712_210049:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_210052:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-12T21:52:49Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-07-12 23:52:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/730/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_205908:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_205911:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_205914:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_205917:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_205920:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_205923:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_205927:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_205930:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_205933:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230712_205936:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_205938:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_205941:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_205945:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_205950:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_205953:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_205956:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_205959:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_210003:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230712_210006:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230712_210017:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230712_210020:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230712_210024:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_210027:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230712_210030:cmsbot_crab_whitelist - 0
blacklist-check.sh 230712_210033:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230712_210036:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_210039:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_210042:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_210045:cmsbot_crab_scheddName - 0
collector-check.sh 230712_210049:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_210052:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
