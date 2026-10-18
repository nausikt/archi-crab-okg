# dmwm/CRABServer issue #8129: #640: Test prod CRABClient using preprod REST instance and CMSSW_9_4_21 CMSSW release

State: closed
Opened: 2023-12-19T22:22:30Z
Closed: 2023-12-20T11:25:57Z
URL: https://github.com/dmwm/CRABServer/issues/8129

## Opening post (cmsdmwmbot, 2023-12-19T22:22:30Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_9_4_21**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-19 23:22:30
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/640/)

## Comment (cmsdmwmbot, 2023-12-19T22:23:50Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_222246:cmsbot_crab_transferOutputs
231219_222247:cmsbot_crab_transferLogs
231219_222248:cmsbot_crab_activity
231219_222251:cmsbot_crab_inputFiles
231219_222252:cmsbot_crab_disableAutomaticOutputCollection
231219_222254:cmsbot_crab_outputFiles
231219_222255:cmsbot_crab_allowUndistributedCMSSW
231219_222256:cmsbot_crab_maxMemoryMB
231219_222257:cmsbot_crab_maxJobRuntimeMin
231219_222259:cmsbot_crab_numCores
231219_222300:cmsbot_crab_scriptExe
231219_222302:cmsbot_crab_scriptArgs
231219_222304:cmsbot_crab_sendVenvFolder
231219_222309:cmsbot_crab_sendExternalFolder
231219_222310:cmsbot_crab_inputDBS
231219_222311:cmsbot_crab_useParent
231219_222312:cmsbot_crab_secondaryInputDataset
231219_222313:cmsbot_crab_lumiMaskFile
231219_222314:cmsbot_crab_lumiMaskUrl
231219_222316:cmsbot_crab_outLFNDirBase
231219_222317:cmsbot_crab_runRange
231219_222319:cmsbot_crab_ignoreLocality
231219_222319:cmsbot_crab_userInputFiles
231219_222321:cmsbot_crab_whitelist
231219_222322:cmsbot_crab_blacklist
231219_222323:cmsbot_crab_ignoreGlobalBlacklist
231219_222324:cmsbot_crab_voRole
231219_222325:cmsbot_crab_voGroup
231219_222326:cmsbot_crab_scheddName
231219_222327:cmsbot_crab_collector
231219_222328:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 23:23:29
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/640/console)

## Comment (cmsdmwmbot, 2023-12-19T22:45:58Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 23:45:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/813/console

```
RETRY TESTS:
lumiMaskFile-check.sh 231219_222313:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 231219_222314:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231219_222317:cmsbot_crab_runRange - 2
whitelist-check.sh 231219_222321:cmsbot_crab_whitelist - 2
blacklist-check.sh 231219_222322:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222246:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222247:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222248:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222251:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222252:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222254:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222255:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222256:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222257:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_222259:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_222300:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222302:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222304:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222309:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222310:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222311:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222312:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 231219_222316:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231219_222319:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222319:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231219_222323:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222324:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222325:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222326:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222327:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222328:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:08:10Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-12-20 00:08:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/818/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222246:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222247:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222248:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222251:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222252:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222254:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222255:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222256:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222257:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_222259:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_222300:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222302:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222304:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222309:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222310:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222311:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222312:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222313:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231219_222314:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231219_222316:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222317:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222319:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222319:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222321:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_222322:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_222323:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222324:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222325:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222326:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222327:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222328:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (mapellidario, 2023-12-20T11:25:57Z)

looks good to me
