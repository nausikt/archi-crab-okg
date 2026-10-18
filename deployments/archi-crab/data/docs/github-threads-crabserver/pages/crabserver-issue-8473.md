# dmwm/CRABServer issue #8473: #797: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-04T13:32:35Z
Closed: 2024-06-06T13:48:33Z
URL: https://github.com/dmwm/CRABServer/issues/8473

## Opening post (cmsdmwmbot, 2024-06-04T13:32:35Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-06-04 15:32:34
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/797/)

## Comment (cmsdmwmbot, 2024-06-04T13:34:31Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240604_133258:cmsbot_crab_transferOutputs
240604_133303:cmsbot_crab_transferLogs
240604_133305:cmsbot_crab_activity
240604_133307:cmsbot_crab_inputFiles
240604_133310:cmsbot_crab_disableAutomaticOutputCollection
240604_133312:cmsbot_crab_outputFiles
240604_133314:cmsbot_crab_allowUndistributedCMSSW
240604_133317:cmsbot_crab_maxMemoryMB
240604_133319:cmsbot_crab_maxJobRuntimeMin
240604_133321:cmsbot_crab_numCores
240604_133323:cmsbot_crab_scriptExe
240604_133326:cmsbot_crab_scriptArgs
240604_133328:cmsbot_crab_sendVenvFolder
240604_133330:cmsbot_crab_sendExternalFolder
240604_133333:cmsbot_crab_inputDBS
240604_133335:cmsbot_crab_useParent
240604_133337:cmsbot_crab_secondaryInputDataset
240604_133339:cmsbot_crab_lumiMaskFile
240604_133341:cmsbot_crab_lumiMaskUrl
240604_133345:cmsbot_crab_outLFNDirBase
240604_133347:cmsbot_crab_runRange
240604_133349:cmsbot_crab_ignoreLocality
240604_133351:cmsbot_crab_userInputFiles
240604_133353:cmsbot_crab_whitelist
240604_133356:cmsbot_crab_blacklist
240604_133358:cmsbot_crab_ignoreGlobalBlacklist
240604_133400:cmsbot_crab_voRole
240604_133403:cmsbot_crab_voGroup
240604_133405:cmsbot_crab_scheddName
240604_133407:cmsbot_crab_collector
240604_133409:cmsbot_crab_extraJDL
```

Finished at: 2024-06-04 15:34:10
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/797/console)

## Comment (cmsdmwmbot, 2024-06-04T13:58:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-04 15:58:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1101/console

```
RETRY TESTS:
activity-check.sh 240604_133305:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 240604_133310:cmsbot_crab_disableAutomaticOutputCollection - 2
useParent-check.sh 240604_133335:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240604_133337:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240604_133341:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240604_133347:cmsbot_crab_runRange - 2
whitelist-check.sh 240604_133353:cmsbot_crab_whitelist - 2
blacklist-check.sh 240604_133356:cmsbot_crab_blacklist - 2
voRole-check.sh 240604_133400:cmsbot_crab_voRole - 2
voGroup-check.sh 240604_133403:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240604_133409:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240604_133258:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240604_133303:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240604_133307:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 240604_133312:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240604_133314:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240604_133317:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240604_133319:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240604_133323:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240604_133326:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240604_133328:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240604_133330:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240604_133333:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240604_133339:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240604_133345:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240604_133349:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240604_133351:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240604_133358:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240604_133405:cmsbot_crab_scheddName - 0
collector-check.sh 240604_133407:cmsbot_crab_collector - 0

FAILED TESTS:
numCores-check.sh 240604_133321:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-06-04T14:22:39Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-06-04 16:22:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1102/console

```
RETRY TESTS:
useParent-check.sh 240604_133335:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240604_133337:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240604_133341:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240604_133347:cmsbot_crab_runRange - 2
whitelist-check.sh 240604_133353:cmsbot_crab_whitelist - 2
blacklist-check.sh 240604_133356:cmsbot_crab_blacklist - 2
voRole-check.sh 240604_133400:cmsbot_crab_voRole - 2
voGroup-check.sh 240604_133403:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240604_133409:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240604_133258:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240604_133303:cmsbot_crab_transferLogs - 0
activity-check.sh 240604_133305:cmsbot_crab_activity - 0
inputFiles-check.sh 240604_133307:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240604_133310:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240604_133312:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240604_133314:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240604_133317:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240604_133319:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240604_133323:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240604_133326:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240604_133328:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240604_133330:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240604_133333:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240604_133339:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240604_133345:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240604_133349:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240604_133351:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240604_133358:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240604_133405:cmsbot_crab_scheddName - 0
collector-check.sh 240604_133407:cmsbot_crab_collector - 0

FAILED TESTS:
numCores-check.sh 240604_133321:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-06-04T14:46:50Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-06-04 16:46:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1103/console

```
RETRY TESTS:
useParent-check.sh 240604_133335:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240604_133337:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240604_133341:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240604_133347:cmsbot_crab_runRange - 2
whitelist-check.sh 240604_133353:cmsbot_crab_whitelist - 2
blacklist-check.sh 240604_133356:cmsbot_crab_blacklist - 2
voRole-check.sh 240604_133400:cmsbot_crab_voRole - 2
voGroup-check.sh 240604_133403:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240604_133409:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240604_133258:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240604_133303:cmsbot_crab_transferLogs - 0
activity-check.sh 240604_133305:cmsbot_crab_activity - 0
inputFiles-check.sh 240604_133307:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240604_133310:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240604_133312:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240604_133314:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240604_133317:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240604_133319:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240604_133323:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240604_133326:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240604_133328:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240604_133330:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240604_133333:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240604_133339:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240604_133345:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240604_133349:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240604_133351:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240604_133358:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240604_133405:cmsbot_crab_scheddName - 0
collector-check.sh 240604_133407:cmsbot_crab_collector - 0

FAILED TESTS:
numCores-check.sh 240604_133321:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-06-04T15:10:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2024-06-04 17:10:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1104/console

```
RETRY TESTS:
useParent-check.sh 240604_133335:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240604_133337:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240604_133341:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240604_133347:cmsbot_crab_runRange - 2
whitelist-check.sh 240604_133353:cmsbot_crab_whitelist - 2
blacklist-check.sh 240604_133356:cmsbot_crab_blacklist - 2
voGroup-check.sh 240604_133403:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240604_133409:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240604_133258:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240604_133303:cmsbot_crab_transferLogs - 0
activity-check.sh 240604_133305:cmsbot_crab_activity - 0
inputFiles-check.sh 240604_133307:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240604_133310:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240604_133312:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240604_133314:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240604_133317:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240604_133319:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240604_133323:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240604_133326:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240604_133328:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240604_133330:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240604_133333:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240604_133339:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240604_133345:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240604_133349:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240604_133351:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240604_133358:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240604_133400:cmsbot_crab_voRole - 0
scheddName-check.sh 240604_133405:cmsbot_crab_scheddName - 0
collector-check.sh 240604_133407:cmsbot_crab_collector - 0

FAILED TESTS:
numCores-check.sh 240604_133321:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-06-04T15:34:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-04 17:34:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1105/console

```
RETRY TESTS:
useParent-check.sh 240604_133335:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240604_133337:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240604_133341:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240604_133347:cmsbot_crab_runRange - 2
whitelist-check.sh 240604_133353:cmsbot_crab_whitelist - 2
blacklist-check.sh 240604_133356:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240604_133258:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240604_133303:cmsbot_crab_transferLogs - 0
activity-check.sh 240604_133305:cmsbot_crab_activity - 0
inputFiles-check.sh 240604_133307:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240604_133310:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240604_133312:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240604_133314:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240604_133317:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240604_133319:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240604_133323:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240604_133326:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240604_133328:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240604_133330:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240604_133333:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240604_133339:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240604_133345:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240604_133349:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240604_133351:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240604_133358:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240604_133400:cmsbot_crab_voRole - 0
voGroup-check.sh 240604_133403:cmsbot_crab_voGroup - 0
scheddName-check.sh 240604_133405:cmsbot_crab_scheddName - 0
collector-check.sh 240604_133407:cmsbot_crab_collector - 0
extraJDL-check.sh 240604_133409:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 240604_133321:cmsbot_crab_numCores - 1
```

## Comment (belforte, 2024-06-06T13:48:33Z)

my code problems
