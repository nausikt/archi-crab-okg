# dmwm/CRABServer issue #7685: #399: Test prod CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-06-27T23:22:14Z
Closed: 2023-06-29T20:16:18Z
URL: https://github.com/dmwm/CRABServer/issues/7685

## Opening post (cmsdmwmbot, 2023-06-27T23:22:14Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-06-28 01:22:13
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/399/)

## Comment (cmsdmwmbot, 2023-06-27T23:23:50Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230627_232242:cmsbot_crab_transferOutputs
230627_232244:cmsbot_crab_transferLogs
230627_232245:cmsbot_crab_activity
230627_232246:cmsbot_crab_inputFiles
230627_232247:cmsbot_crab_disableAutomaticOutputCollection
230627_232249:cmsbot_crab_outputFiles
230627_232250:cmsbot_crab_allowUndistributedCMSSW
230627_232251:cmsbot_crab_maxMemoryMB
230627_232252:cmsbot_crab_maxJobRuntimeMin
230627_232254:cmsbot_crab_numCores
230627_232255:cmsbot_crab_scriptExe
230627_232256:cmsbot_crab_scriptArgs
230627_232257:cmsbot_crab_sendPythonFolder
230627_232306:cmsbot_crab_sendExternalFolder
230627_232307:cmsbot_crab_inputDBS
230627_232308:cmsbot_crab_useParent
230627_232309:cmsbot_crab_secondaryInputDataset
230627_232310:cmsbot_crab_lumiMaskFile
230627_232312:cmsbot_crab_lumiMaskUrl
230627_232314:cmsbot_crab_outLFNDirBase
230627_232315:cmsbot_crab_runRange
230627_232317:cmsbot_crab_ignoreLocality
230627_232318:cmsbot_crab_userInputFiles
230627_232319:cmsbot_crab_whitelist
230627_232320:cmsbot_crab_blacklist
230627_232321:cmsbot_crab_ignoreGlobalBlacklist
230627_232323:cmsbot_crab_voRole
230627_232324:cmsbot_crab_voGroup
230627_232325:cmsbot_crab_scheddName
230627_232327:cmsbot_crab_collector
230627_232328:cmsbot_crab_extraJDL
```

Finished at: 2023-06-28 01:23:29
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/399/console)

## Comment (cmsdmwmbot, 2023-06-27T23:45:18Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-28 01:45:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/618/console

```
RETRY TESTS:
transferOutputs-check.sh 230627_232242:cmsbot_crab_transferOutputs - 2
activity-check.sh 230627_232245:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 230627_232251:cmsbot_crab_maxMemoryMB - 2
useParent-check.sh 230627_232308:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230627_232309:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 230627_232310:cmsbot_crab_lumiMaskFile - 2
whitelist-check.sh 230627_232319:cmsbot_crab_whitelist - 2
blacklist-check.sh 230627_232320:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230627_232321:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230627_232323:cmsbot_crab_voRole - 2
voGroup-check.sh 230627_232324:cmsbot_crab_voGroup - 2
extraJDL-check.sh 230627_232328:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 230627_232246:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230627_232250:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230627_232257:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_232306:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_232307:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230627_232325:cmsbot_crab_scheddName - 0
collector-check.sh 230627_232327:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 230627_232244:cmsbot_crab_transferLogs - 1
disableAutomaticOutputCollection-check.sh 230627_232247:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230627_232249:cmsbot_crab_outputFiles - 1
maxJobRuntimeMin-check.sh 230627_232252:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230627_232254:cmsbot_crab_numCores - 1
scriptExe-check.sh 230627_232255:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230627_232256:cmsbot_crab_scriptArgs - 1
lumiMaskUrl-check.sh 230627_232312:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230627_232314:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230627_232315:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230627_232317:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230627_232318:cmsbot_crab_userInputFiles - 1
```

## Comment (cmsdmwmbot, 2023-06-28T00:07:03Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-28 02:07:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/622/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
inputFiles-check.sh 230627_232246:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230627_232250:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230627_232257:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_232306:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_232307:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230627_232325:cmsbot_crab_scheddName - 0
collector-check.sh 230627_232327:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 230627_232242:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230627_232244:cmsbot_crab_transferLogs - 1
activity-check.sh 230627_232245:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230627_232247:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230627_232249:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230627_232251:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230627_232252:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230627_232254:cmsbot_crab_numCores - 1
scriptExe-check.sh 230627_232255:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230627_232256:cmsbot_crab_scriptArgs - 1
useParent-check.sh 230627_232308:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230627_232309:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230627_232310:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230627_232312:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230627_232314:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230627_232315:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230627_232317:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230627_232318:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230627_232319:cmsbot_crab_whitelist - 1
blacklist-check.sh 230627_232320:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230627_232321:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230627_232323:cmsbot_crab_voRole - 1
voGroup-check.sh 230627_232324:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230627_232328:cmsbot_crab_extraJDL - 1
```
