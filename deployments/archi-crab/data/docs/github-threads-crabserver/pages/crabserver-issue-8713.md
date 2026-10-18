# dmwm/CRABServer issue #8713: #838: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-20T17:42:44Z
Closed: 2024-09-23T21:04:25Z
URL: https://github.com/dmwm/CRABServer/issues/8713

## Opening post (cmsdmwmbot, 2024-09-20T17:42:44Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-09-20 19:42:44
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/838/)

## Comment (cmsdmwmbot, 2024-09-20T17:44:45Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240920_174304:cmsbot_crab_transferOutputs
240920_174308:cmsbot_crab_transferLogs
240920_174310:cmsbot_crab_activity
240920_174313:cmsbot_crab_inputFiles
240920_174315:cmsbot_crab_disableAutomaticOutputCollection
240920_174318:cmsbot_crab_outputFiles
240920_174320:cmsbot_crab_allowUndistributedCMSSW
240920_174323:cmsbot_crab_maxMemoryMB
240920_174326:cmsbot_crab_maxJobRuntimeMin
240920_174329:cmsbot_crab_numCores
240920_174331:cmsbot_crab_scriptExe
240920_174334:cmsbot_crab_scriptArgs
240920_174336:cmsbot_crab_sendVenvFolder
240920_174339:cmsbot_crab_sendExternalFolder
240920_174341:cmsbot_crab_inputDBS
240920_174344:cmsbot_crab_useParent
240920_174347:cmsbot_crab_secondaryInputDataset
240920_174349:cmsbot_crab_lumiMaskFile
240920_174351:cmsbot_crab_lumiMaskUrl
240920_174355:cmsbot_crab_outLFNDirBase
240920_174357:cmsbot_crab_runRange
240920_174400:cmsbot_crab_ignoreLocality
240920_174403:cmsbot_crab_userInputFiles
240920_174405:cmsbot_crab_whitelist
240920_174408:cmsbot_crab_blacklist
240920_174410:cmsbot_crab_ignoreGlobalBlacklist
240920_174413:cmsbot_crab_voRole
240920_174415:cmsbot_crab_voGroup
240920_174418:cmsbot_crab_scheddName
240920_174420:cmsbot_crab_collector
240920_174423:cmsbot_crab_extraJDL
```

Finished at: 2024-09-20 19:44:24
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/838/console)

## Comment (cmsdmwmbot, 2024-09-20T18:09:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-20 20:09:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1186/console

```
RETRY TESTS:
transferLogs-check.sh 240920_174308:cmsbot_crab_transferLogs - 2
scriptExe-check.sh 240920_174331:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240920_174334:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240920_174349:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240920_174351:cmsbot_crab_lumiMaskUrl - 2
whitelist-check.sh 240920_174405:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
allowUndistributedCMSSW-check.sh 240920_174320:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240920_174336:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174339:cmsbot_crab_sendExternalFolder - 0
outLFNDirBase-check.sh 240920_174355:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_174400:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240920_174410:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240920_174415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_174418:cmsbot_crab_scheddName - 0
collector-check.sh 240920_174420:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_174423:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_174304:cmsbot_crab_transferOutputs - 1
activity-check.sh 240920_174310:cmsbot_crab_activity - 1
inputFiles-check.sh 240920_174313:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174315:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240920_174318:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240920_174323:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_174326:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174329:cmsbot_crab_numCores - 1
inputDBS-check.sh 240920_174341:cmsbot_crab_inputDBS - 1
useParent-check.sh 240920_174344:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_174347:cmsbot_crab_secondaryInputDataset - 1
runRange-check.sh 240920_174357:cmsbot_crab_runRange - 1
userInputFiles-check.sh 240920_174403:cmsbot_crab_userInputFiles - 1
blacklist-check.sh 240920_174408:cmsbot_crab_blacklist - 1
voRole-check.sh 240920_174413:cmsbot_crab_voRole - 1
```

## Comment (cmsdmwmbot, 2024-09-20T18:32:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-09-20 20:32:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1189/console

```
RETRY TESTS:
transferLogs-check.sh 240920_174308:cmsbot_crab_transferLogs - 2
scriptArgs-check.sh 240920_174334:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240920_174349:cmsbot_crab_lumiMaskFile - 2
whitelist-check.sh 240920_174405:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
allowUndistributedCMSSW-check.sh 240920_174320:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 240920_174331:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240920_174336:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174339:cmsbot_crab_sendExternalFolder - 0
lumiMaskUrl-check.sh 240920_174351:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_174355:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_174400:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240920_174410:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240920_174415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_174418:cmsbot_crab_scheddName - 0
collector-check.sh 240920_174420:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_174423:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_174304:cmsbot_crab_transferOutputs - 1
activity-check.sh 240920_174310:cmsbot_crab_activity - 1
inputFiles-check.sh 240920_174313:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174315:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240920_174318:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240920_174323:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_174326:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174329:cmsbot_crab_numCores - 1
inputDBS-check.sh 240920_174341:cmsbot_crab_inputDBS - 1
useParent-check.sh 240920_174344:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_174347:cmsbot_crab_secondaryInputDataset - 1
runRange-check.sh 240920_174357:cmsbot_crab_runRange - 1
userInputFiles-check.sh 240920_174403:cmsbot_crab_userInputFiles - 1
blacklist-check.sh 240920_174408:cmsbot_crab_blacklist - 1
voRole-check.sh 240920_174413:cmsbot_crab_voRole - 1
```

## Comment (cmsdmwmbot, 2024-09-20T18:57:07Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-09-20 20:57:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1191/console

```
RETRY TESTS:
scriptArgs-check.sh 240920_174334:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240920_174349:cmsbot_crab_lumiMaskFile - 2
whitelist-check.sh 240920_174405:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferLogs-check.sh 240920_174308:cmsbot_crab_transferLogs - 0
allowUndistributedCMSSW-check.sh 240920_174320:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 240920_174331:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240920_174336:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174339:cmsbot_crab_sendExternalFolder - 0
lumiMaskUrl-check.sh 240920_174351:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_174355:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_174400:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240920_174410:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240920_174415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_174418:cmsbot_crab_scheddName - 0
collector-check.sh 240920_174420:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_174423:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_174304:cmsbot_crab_transferOutputs - 1
activity-check.sh 240920_174310:cmsbot_crab_activity - 1
inputFiles-check.sh 240920_174313:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174315:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240920_174318:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240920_174323:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_174326:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174329:cmsbot_crab_numCores - 1
inputDBS-check.sh 240920_174341:cmsbot_crab_inputDBS - 1
useParent-check.sh 240920_174344:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_174347:cmsbot_crab_secondaryInputDataset - 1
runRange-check.sh 240920_174357:cmsbot_crab_runRange - 1
userInputFiles-check.sh 240920_174403:cmsbot_crab_userInputFiles - 1
blacklist-check.sh 240920_174408:cmsbot_crab_blacklist - 1
voRole-check.sh 240920_174413:cmsbot_crab_voRole - 1
```

## Comment (cmsdmwmbot, 2024-09-20T19:20:43Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2024-09-20 21:20:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1193/console

```
RETRY TESTS:
scriptArgs-check.sh 240920_174334:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240920_174349:cmsbot_crab_lumiMaskFile - 2

SUCCESSFUL TESTS:
transferLogs-check.sh 240920_174308:cmsbot_crab_transferLogs - 0
allowUndistributedCMSSW-check.sh 240920_174320:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 240920_174331:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240920_174336:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174339:cmsbot_crab_sendExternalFolder - 0
lumiMaskUrl-check.sh 240920_174351:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_174355:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_174400:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 240920_174405:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240920_174410:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240920_174415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_174418:cmsbot_crab_scheddName - 0
collector-check.sh 240920_174420:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_174423:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_174304:cmsbot_crab_transferOutputs - 1
activity-check.sh 240920_174310:cmsbot_crab_activity - 1
inputFiles-check.sh 240920_174313:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174315:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240920_174318:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240920_174323:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_174326:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174329:cmsbot_crab_numCores - 1
inputDBS-check.sh 240920_174341:cmsbot_crab_inputDBS - 1
useParent-check.sh 240920_174344:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_174347:cmsbot_crab_secondaryInputDataset - 1
runRange-check.sh 240920_174357:cmsbot_crab_runRange - 1
userInputFiles-check.sh 240920_174403:cmsbot_crab_userInputFiles - 1
blacklist-check.sh 240920_174408:cmsbot_crab_blacklist - 1
voRole-check.sh 240920_174413:cmsbot_crab_voRole - 1
```

## Comment (cmsdmwmbot, 2024-09-20T19:44:25Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-09-20 21:44:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1195/console

```
RETRY TESTS:
scriptArgs-check.sh 240920_174334:cmsbot_crab_scriptArgs - 2

SUCCESSFUL TESTS:
transferLogs-check.sh 240920_174308:cmsbot_crab_transferLogs - 0
allowUndistributedCMSSW-check.sh 240920_174320:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 240920_174331:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240920_174336:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174339:cmsbot_crab_sendExternalFolder - 0
lumiMaskUrl-check.sh 240920_174351:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_174355:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_174400:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 240920_174405:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240920_174410:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240920_174415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_174418:cmsbot_crab_scheddName - 0
collector-check.sh 240920_174420:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_174423:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240920_174304:cmsbot_crab_transferOutputs - 1
activity-check.sh 240920_174310:cmsbot_crab_activity - 1
inputFiles-check.sh 240920_174313:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174315:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240920_174318:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240920_174323:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240920_174326:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174329:cmsbot_crab_numCores - 1
inputDBS-check.sh 240920_174341:cmsbot_crab_inputDBS - 1
useParent-check.sh 240920_174344:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240920_174347:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_174349:cmsbot_crab_lumiMaskFile - 1
runRange-check.sh 240920_174357:cmsbot_crab_runRange - 1
userInputFiles-check.sh 240920_174403:cmsbot_crab_userInputFiles - 1
blacklist-check.sh 240920_174408:cmsbot_crab_blacklist - 1
voRole-check.sh 240920_174413:cmsbot_crab_voRole - 1
```
