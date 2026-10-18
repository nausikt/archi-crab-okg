# dmwm/CRABServer issue #7710: #419: Test dev CRABClient using test2 REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-06-30T21:07:32Z
Closed: 2023-06-30T23:14:22Z
URL: https://github.com/dmwm/CRABServer/issues/7710

## Opening post (cmsdmwmbot, 2023-06-30T21:07:32Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-06-30 23:07:32
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/419/)

## Comment (cmsdmwmbot, 2023-06-30T21:10:46Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230630_210859:cmsbot_crab_transferOutputs
230630_210902:cmsbot_crab_transferLogs
230630_210904:cmsbot_crab_activity
230630_210907:cmsbot_crab_inputFiles
230630_210910:cmsbot_crab_disableAutomaticOutputCollection
230630_210912:cmsbot_crab_outputFiles
230630_210915:cmsbot_crab_allowUndistributedCMSSW
230630_210918:cmsbot_crab_maxMemoryMB
230630_210920:cmsbot_crab_maxJobRuntimeMin
230630_210923:cmsbot_crab_numCores
230630_210926:cmsbot_crab_scriptExe
230630_210928:cmsbot_crab_scriptArgs
230630_210931:cmsbot_crab_sendPythonFolder
230630_210938:cmsbot_crab_sendExternalFolder
230630_210940:cmsbot_crab_inputDBS
230630_210943:cmsbot_crab_useParent
230630_210946:cmsbot_crab_secondaryInputDataset
230630_210948:cmsbot_crab_lumiMaskFile
230630_210951:cmsbot_crab_lumiMaskUrl
230630_210955:cmsbot_crab_outLFNDirBase
230630_210957:cmsbot_crab_runRange
230630_211000:cmsbot_crab_ignoreLocality
230630_211003:cmsbot_crab_userInputFiles
230630_211006:cmsbot_crab_whitelist
230630_211008:cmsbot_crab_blacklist
230630_211011:cmsbot_crab_ignoreGlobalBlacklist
230630_211014:cmsbot_crab_voRole
230630_211016:cmsbot_crab_voGroup
230630_211019:cmsbot_crab_scheddName
230630_211022:cmsbot_crab_collector
230630_211024:cmsbot_crab_extraJDL
```

Finished at: 2023-06-30 23:10:25
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/419/console)

## Comment (cmsdmwmbot, 2023-06-30T21:34:52Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-30 23:34:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/667/console

```
RETRY TESTS:
transferLogs-check.sh 230630_210902:cmsbot_crab_transferLogs - 2
activity-check.sh 230630_210904:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 230630_210910:cmsbot_crab_disableAutomaticOutputCollection - 2
outputFiles-check.sh 230630_210912:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230630_210918:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230630_210920:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230630_210923:cmsbot_crab_numCores - 2
scriptExe-check.sh 230630_210926:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230630_210928:cmsbot_crab_scriptArgs - 2
useParent-check.sh 230630_210943:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230630_210946:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 230630_210948:cmsbot_crab_lumiMaskFile - 2
runRange-check.sh 230630_210957:cmsbot_crab_runRange - 2
whitelist-check.sh 230630_211006:cmsbot_crab_whitelist - 2
blacklist-check.sh 230630_211008:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230630_211011:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230630_211014:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 230630_210907:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230630_210915:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230630_210931:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_210938:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_210940:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230630_211019:cmsbot_crab_scheddName - 0
collector-check.sh 230630_211022:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 230630_210859:cmsbot_crab_transferOutputs - 1
lumiMaskUrl-check.sh 230630_210951:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230630_210955:cmsbot_crab_outLFNDirBase - 1
ignoreLocality-check.sh 230630_211000:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230630_211003:cmsbot_crab_userInputFiles - 1
voGroup-check.sh 230630_211016:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230630_211024:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-06-30T21:59:05Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-30 23:59:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/669/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
inputFiles-check.sh 230630_210907:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230630_210915:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230630_210931:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_210938:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_210940:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230630_211019:cmsbot_crab_scheddName - 0
collector-check.sh 230630_211022:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 230630_210859:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230630_210902:cmsbot_crab_transferLogs - 1
activity-check.sh 230630_210904:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230630_210910:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230630_210912:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230630_210918:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230630_210920:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230630_210923:cmsbot_crab_numCores - 1
scriptExe-check.sh 230630_210926:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230630_210928:cmsbot_crab_scriptArgs - 1
useParent-check.sh 230630_210943:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230630_210946:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230630_210948:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230630_210951:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230630_210955:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230630_210957:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230630_211000:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230630_211003:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230630_211006:cmsbot_crab_whitelist - 1
blacklist-check.sh 230630_211008:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230630_211011:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230630_211014:cmsbot_crab_voRole - 1
voGroup-check.sh 230630_211016:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230630_211024:cmsbot_crab_extraJDL - 1
```
