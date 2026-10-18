# dmwm/CRABServer issue #8119: #632: Test dev CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-12-19T20:31:56Z
Closed: 2023-12-20T11:25:02Z
URL: https://github.com/dmwm/CRABServer/issues/8119

## Opening post (cmsdmwmbot, 2023-12-19T20:31:56Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-19 21:31:55
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/632/)

## Comment (cmsdmwmbot, 2023-12-19T20:33:51Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_203216:cmsbot_crab_transferOutputs
231219_203218:cmsbot_crab_transferLogs
231219_203220:cmsbot_crab_activity
231219_203223:cmsbot_crab_inputFiles
231219_203225:cmsbot_crab_disableAutomaticOutputCollection
231219_203227:cmsbot_crab_outputFiles
231219_203229:cmsbot_crab_allowUndistributedCMSSW
231219_203232:cmsbot_crab_maxMemoryMB
231219_203234:cmsbot_crab_maxJobRuntimeMin
231219_203236:cmsbot_crab_numCores
231219_203238:cmsbot_crab_scriptExe
231219_203240:cmsbot_crab_scriptArgs
231219_203242:cmsbot_crab_sendVenvFolder
231219_203252:cmsbot_crab_sendExternalFolder
231219_203254:cmsbot_crab_inputDBS
231219_203256:cmsbot_crab_useParent
231219_203259:cmsbot_crab_secondaryInputDataset
231219_203301:cmsbot_crab_lumiMaskFile
231219_203303:cmsbot_crab_lumiMaskUrl
231219_203306:cmsbot_crab_outLFNDirBase
231219_203309:cmsbot_crab_runRange
231219_203311:cmsbot_crab_ignoreLocality
231219_203313:cmsbot_crab_userInputFiles
231219_203315:cmsbot_crab_whitelist
231219_203317:cmsbot_crab_blacklist
231219_203319:cmsbot_crab_ignoreGlobalBlacklist
231219_203321:cmsbot_crab_voRole
231219_203323:cmsbot_crab_voGroup
231219_203325:cmsbot_crab_scheddName
231219_203327:cmsbot_crab_collector
231219_203330:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 21:33:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/632/console)

## Comment (cmsdmwmbot, 2023-12-19T21:03:38Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 22:03:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/805/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 231219_203303:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231219_203309:cmsbot_crab_runRange - 2
whitelist-check.sh 231219_203315:cmsbot_crab_whitelist - 2
blacklist-check.sh 231219_203317:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 231219_203319:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_203216:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_203218:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_203220:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_203223:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_203225:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_203227:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_203229:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_203232:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_203234:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_203236:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_203238:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_203240:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_203242:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_203252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_203254:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_203256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_203259:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_203301:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_203306:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231219_203311:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_203313:cmsbot_crab_userInputFiles - 0
voRole-check.sh 231219_203321:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_203323:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_203325:cmsbot_crab_scheddName - 0
collector-check.sh 231219_203327:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_203330:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T21:27:47Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-12-19 22:27:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/810/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_203216:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_203218:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_203220:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_203223:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_203225:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_203227:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_203229:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_203232:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_203234:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_203236:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_203238:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_203240:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_203242:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_203252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_203254:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_203256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_203259:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_203301:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231219_203303:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231219_203306:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_203309:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_203311:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_203313:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_203315:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_203317:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_203319:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_203321:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_203323:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_203325:cmsbot_crab_scheddName - 0
collector-check.sh 231219_203327:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_203330:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (mapellidario, 2023-12-20T11:25:02Z)

looks good to me
