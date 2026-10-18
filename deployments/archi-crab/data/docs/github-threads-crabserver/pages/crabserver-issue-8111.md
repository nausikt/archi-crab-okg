# dmwm/CRABServer issue #8111: #626: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-12-18T18:07:22Z
Closed: 2023-12-18T20:33:03Z
URL: https://github.com/dmwm/CRABServer/issues/8111

## Opening post (cmsdmwmbot, 2023-12-18T18:07:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-12-18 19:07:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/626/)

## Comment (cmsdmwmbot, 2023-12-18T18:11:03Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231218_180851:cmsbot_crab_transferOutputs
231218_180853:cmsbot_crab_transferLogs
231218_180855:cmsbot_crab_activity
231218_180857:cmsbot_crab_inputFiles
231218_180859:cmsbot_crab_disableAutomaticOutputCollection
231218_180901:cmsbot_crab_outputFiles
231218_180903:cmsbot_crab_allowUndistributedCMSSW
231218_180905:cmsbot_crab_maxMemoryMB
231218_180907:cmsbot_crab_maxJobRuntimeMin
231218_180909:cmsbot_crab_numCores
231218_180911:cmsbot_crab_scriptExe
231218_180913:cmsbot_crab_scriptArgs
231218_180915:cmsbot_crab_sendVenvFolder
231218_181005:cmsbot_crab_sendExternalFolder
231218_181008:cmsbot_crab_inputDBS
231218_181010:cmsbot_crab_useParent
231218_181012:cmsbot_crab_secondaryInputDataset
231218_181014:cmsbot_crab_lumiMaskFile
231218_181016:cmsbot_crab_lumiMaskUrl
231218_181019:cmsbot_crab_outLFNDirBase
231218_181021:cmsbot_crab_runRange
231218_181023:cmsbot_crab_ignoreLocality
231218_181025:cmsbot_crab_userInputFiles
231218_181027:cmsbot_crab_whitelist
231218_181029:cmsbot_crab_blacklist
231218_181031:cmsbot_crab_ignoreGlobalBlacklist
231218_181033:cmsbot_crab_voRole
231218_181035:cmsbot_crab_voGroup
231218_181037:cmsbot_crab_scheddName
231218_181039:cmsbot_crab_collector
231218_181041:cmsbot_crab_extraJDL
```

Finished at: 2023-12-18 19:10:42
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/626/console)

## Comment (cmsdmwmbot, 2023-12-18T18:36:49Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-18 19:36:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/796/console

```
RETRY TESTS:
maxMemoryMB-check.sh 231218_180905:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 231218_180907:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 231218_180909:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 231218_181016:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231218_181021:cmsbot_crab_runRange - 2
whitelist-check.sh 231218_181027:cmsbot_crab_whitelist - 2
blacklist-check.sh 231218_181029:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231218_180851:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231218_180853:cmsbot_crab_transferLogs - 0
activity-check.sh 231218_180855:cmsbot_crab_activity - 0
inputFiles-check.sh 231218_180857:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231218_180859:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231218_180901:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231218_180903:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 231218_180911:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231218_180913:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231218_180915:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231218_181005:cmsbot_crab_sendExternalFolder - 0
lumiMaskFile-check.sh 231218_181014:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231218_181019:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231218_181023:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231218_181025:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231218_181031:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231218_181033:cmsbot_crab_voRole - 0
voGroup-check.sh 231218_181035:cmsbot_crab_voGroup - 0
scheddName-check.sh 231218_181037:cmsbot_crab_scheddName - 0
collector-check.sh 231218_181039:cmsbot_crab_collector - 0
extraJDL-check.sh 231218_181041:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputDBS-check.sh 231218_181008:cmsbot_crab_inputDBS - 1
useParent-check.sh 231218_181010:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231218_181012:cmsbot_crab_secondaryInputDataset - 1
```

## Comment (cmsdmwmbot, 2023-12-18T19:02:31Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-12-18 20:02:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/797/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231218_180851:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231218_180853:cmsbot_crab_transferLogs - 0
activity-check.sh 231218_180855:cmsbot_crab_activity - 0
inputFiles-check.sh 231218_180857:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231218_180859:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231218_180901:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231218_180903:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231218_180905:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231218_180907:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231218_180909:cmsbot_crab_numCores - 0
scriptExe-check.sh 231218_180911:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231218_180913:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231218_180915:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231218_181005:cmsbot_crab_sendExternalFolder - 0
lumiMaskFile-check.sh 231218_181014:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231218_181016:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231218_181019:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231218_181021:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231218_181023:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231218_181025:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231218_181027:cmsbot_crab_whitelist - 0
blacklist-check.sh 231218_181029:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231218_181031:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231218_181033:cmsbot_crab_voRole - 0
voGroup-check.sh 231218_181035:cmsbot_crab_voGroup - 0
scheddName-check.sh 231218_181037:cmsbot_crab_scheddName - 0
collector-check.sh 231218_181039:cmsbot_crab_collector - 0
extraJDL-check.sh 231218_181041:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputDBS-check.sh 231218_181008:cmsbot_crab_inputDBS - 1
useParent-check.sh 231218_181010:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231218_181012:cmsbot_crab_secondaryInputDataset - 1
```

## Comment (belforte, 2023-12-18T20:33:00Z)

OK. Only the expected failures
