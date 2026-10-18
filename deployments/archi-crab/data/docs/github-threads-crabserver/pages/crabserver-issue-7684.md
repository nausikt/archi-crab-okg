# dmwm/CRABServer issue #7684: #398: Test prod CRABClient using test2 REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2023-06-27T23:07:30Z
Closed: 2023-06-29T20:16:18Z
URL: https://github.com/dmwm/CRABServer/issues/7684

## Opening post (cmsdmwmbot, 2023-06-27T23:07:30Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-06-28 01:07:30
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/398/)

## Comment (cmsdmwmbot, 2023-06-27T23:10:45Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230627_230855:cmsbot_crab_transferOutputs
230627_230858:cmsbot_crab_transferLogs
230627_230901:cmsbot_crab_activity
230627_230904:cmsbot_crab_inputFiles
230627_230907:cmsbot_crab_disableAutomaticOutputCollection
230627_230911:cmsbot_crab_outputFiles
230627_230913:cmsbot_crab_allowUndistributedCMSSW
230627_230916:cmsbot_crab_maxMemoryMB
230627_230918:cmsbot_crab_maxJobRuntimeMin
230627_230922:cmsbot_crab_numCores
230627_230925:cmsbot_crab_scriptExe
230627_230927:cmsbot_crab_scriptArgs
230627_230931:cmsbot_crab_sendPythonFolder
230627_230938:cmsbot_crab_sendExternalFolder
230627_230940:cmsbot_crab_inputDBS
230627_230943:cmsbot_crab_useParent
230627_230945:cmsbot_crab_secondaryInputDataset
230627_230948:cmsbot_crab_lumiMaskFile
230627_230951:cmsbot_crab_lumiMaskUrl
230627_230955:cmsbot_crab_outLFNDirBase
230627_230957:cmsbot_crab_runRange
230627_231000:cmsbot_crab_ignoreLocality
230627_231003:cmsbot_crab_userInputFiles
230627_231005:cmsbot_crab_whitelist
230627_231008:cmsbot_crab_blacklist
230627_231010:cmsbot_crab_ignoreGlobalBlacklist
230627_231013:cmsbot_crab_voRole
230627_231015:cmsbot_crab_voGroup
230627_231018:cmsbot_crab_scheddName
230627_231021:cmsbot_crab_collector
230627_231023:cmsbot_crab_extraJDL
```

Finished at: 2023-06-28 01:10:24
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/398/console)

## Comment (cmsdmwmbot, 2023-06-27T23:35:11Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-28 01:35:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/617/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230627_230916:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230627_230918:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230627_230922:cmsbot_crab_numCores - 2
useParent-check.sh 230627_230943:cmsbot_crab_useParent - 2
lumiMaskFile-check.sh 230627_230948:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230627_230951:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230627_230955:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230627_230957:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 230627_231000:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 230627_231003:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230627_231005:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 230627_230904:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230627_230913:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230627_230931:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_230938:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_230940:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230627_231018:cmsbot_crab_scheddName - 0
collector-check.sh 230627_231021:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 230627_230855:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230627_230858:cmsbot_crab_transferLogs - 1
activity-check.sh 230627_230901:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230627_230907:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230627_230911:cmsbot_crab_outputFiles - 1
scriptExe-check.sh 230627_230925:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230627_230927:cmsbot_crab_scriptArgs - 1
secondaryInputDataset-check.sh 230627_230945:cmsbot_crab_secondaryInputDataset - 1
blacklist-check.sh 230627_231008:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230627_231010:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230627_231013:cmsbot_crab_voRole - 1
voGroup-check.sh 230627_231015:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230627_231023:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-06-27T23:59:22Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-28 01:59:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/621/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
inputFiles-check.sh 230627_230904:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230627_230913:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230627_230931:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_230938:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_230940:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230627_231018:cmsbot_crab_scheddName - 0
collector-check.sh 230627_231021:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 230627_230855:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230627_230858:cmsbot_crab_transferLogs - 1
activity-check.sh 230627_230901:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230627_230907:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230627_230911:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230627_230916:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230627_230918:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230627_230922:cmsbot_crab_numCores - 1
scriptExe-check.sh 230627_230925:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230627_230927:cmsbot_crab_scriptArgs - 1
useParent-check.sh 230627_230943:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230627_230945:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230627_230948:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230627_230951:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230627_230955:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230627_230957:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230627_231000:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230627_231003:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230627_231005:cmsbot_crab_whitelist - 1
blacklist-check.sh 230627_231008:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230627_231010:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230627_231013:cmsbot_crab_voRole - 1
voGroup-check.sh 230627_231015:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230627_231023:cmsbot_crab_extraJDL - 1
```
