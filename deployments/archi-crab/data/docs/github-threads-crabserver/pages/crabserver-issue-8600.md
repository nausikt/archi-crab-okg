# dmwm/CRABServer issue #8600: #823: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-09T15:02:22Z
Closed: 2024-08-09T19:54:03Z
URL: https://github.com/dmwm/CRABServer/issues/8600

## Opening post (cmsdmwmbot, 2024-08-09T15:02:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-08-09 17:02:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/823/)

## Comment (cmsdmwmbot, 2024-08-09T15:04:08Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240809_150242:cmsbot_crab_transferOutputs
240809_150244:cmsbot_crab_transferLogs
240809_150246:cmsbot_crab_activity
240809_150249:cmsbot_crab_inputFiles
240809_150251:cmsbot_crab_disableAutomaticOutputCollection
240809_150253:cmsbot_crab_outputFiles
240809_150255:cmsbot_crab_allowUndistributedCMSSW
240809_150257:cmsbot_crab_maxMemoryMB
240809_150259:cmsbot_crab_maxJobRuntimeMin
240809_150301:cmsbot_crab_numCores
240809_150303:cmsbot_crab_scriptExe
240809_150305:cmsbot_crab_scriptArgs
240809_150308:cmsbot_crab_sendVenvFolder
240809_150310:cmsbot_crab_sendExternalFolder
240809_150312:cmsbot_crab_inputDBS
240809_150314:cmsbot_crab_useParent
240809_150316:cmsbot_crab_secondaryInputDataset
240809_150318:cmsbot_crab_lumiMaskFile
240809_150320:cmsbot_crab_lumiMaskUrl
240809_150323:cmsbot_crab_outLFNDirBase
240809_150325:cmsbot_crab_runRange
240809_150327:cmsbot_crab_ignoreLocality
240809_150329:cmsbot_crab_userInputFiles
240809_150331:cmsbot_crab_whitelist
240809_150333:cmsbot_crab_blacklist
240809_150336:cmsbot_crab_ignoreGlobalBlacklist
240809_150338:cmsbot_crab_voRole
240809_150340:cmsbot_crab_voGroup
240809_150342:cmsbot_crab_scheddName
240809_150344:cmsbot_crab_collector
240809_150346:cmsbot_crab_extraJDL
```

Finished at: 2024-08-09 17:03:47
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/823/console)

## Comment (cmsdmwmbot, 2024-08-09T15:27:49Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-09 17:27:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1150/console

```
RETRY TESTS:
numCores-check.sh 240809_150301:cmsbot_crab_numCores - 2
scriptExe-check.sh 240809_150303:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240809_150305:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240809_150314:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240809_150316:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240809_150318:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240809_150320:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240809_150325:cmsbot_crab_runRange - 2
whitelist-check.sh 240809_150331:cmsbot_crab_whitelist - 2
blacklist-check.sh 240809_150333:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240809_150242:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240809_150244:cmsbot_crab_transferLogs - 0
activity-check.sh 240809_150246:cmsbot_crab_activity - 0
inputFiles-check.sh 240809_150249:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240809_150251:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240809_150253:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240809_150255:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240809_150257:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240809_150259:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 240809_150308:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240809_150310:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240809_150312:cmsbot_crab_inputDBS - 0
outLFNDirBase-check.sh 240809_150323:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240809_150327:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240809_150329:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240809_150336:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240809_150338:cmsbot_crab_voRole - 0
voGroup-check.sh 240809_150340:cmsbot_crab_voGroup - 0
scheddName-check.sh 240809_150342:cmsbot_crab_scheddName - 0
collector-check.sh 240809_150344:cmsbot_crab_collector - 0
extraJDL-check.sh 240809_150346:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-09T15:51:32Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-08-09 17:51:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1152/console

```
RETRY TESTS:
scriptExe-check.sh 240809_150303:cmsbot_crab_scriptExe - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240809_150242:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240809_150244:cmsbot_crab_transferLogs - 0
activity-check.sh 240809_150246:cmsbot_crab_activity - 0
inputFiles-check.sh 240809_150249:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240809_150251:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240809_150253:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240809_150255:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240809_150257:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240809_150259:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240809_150301:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240809_150305:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240809_150308:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240809_150310:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240809_150312:cmsbot_crab_inputDBS - 0
useParent-check.sh 240809_150314:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240809_150316:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240809_150318:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240809_150320:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240809_150323:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240809_150325:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240809_150327:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240809_150329:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240809_150331:cmsbot_crab_whitelist - 0
blacklist-check.sh 240809_150333:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240809_150336:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240809_150338:cmsbot_crab_voRole - 0
voGroup-check.sh 240809_150340:cmsbot_crab_voGroup - 0
scheddName-check.sh 240809_150342:cmsbot_crab_scheddName - 0
collector-check.sh 240809_150344:cmsbot_crab_collector - 0
extraJDL-check.sh 240809_150346:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-09T16:15:25Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-08-09 18:15:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1153/console

```
RETRY TESTS:
scriptExe-check.sh 240809_150303:cmsbot_crab_scriptExe - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240809_150242:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240809_150244:cmsbot_crab_transferLogs - 0
activity-check.sh 240809_150246:cmsbot_crab_activity - 0
inputFiles-check.sh 240809_150249:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240809_150251:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240809_150253:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240809_150255:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240809_150257:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240809_150259:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240809_150301:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240809_150305:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240809_150308:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240809_150310:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240809_150312:cmsbot_crab_inputDBS - 0
useParent-check.sh 240809_150314:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240809_150316:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240809_150318:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240809_150320:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240809_150323:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240809_150325:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240809_150327:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240809_150329:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240809_150331:cmsbot_crab_whitelist - 0
blacklist-check.sh 240809_150333:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240809_150336:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240809_150338:cmsbot_crab_voRole - 0
voGroup-check.sh 240809_150340:cmsbot_crab_voGroup - 0
scheddName-check.sh 240809_150342:cmsbot_crab_scheddName - 0
collector-check.sh 240809_150344:cmsbot_crab_collector - 0
extraJDL-check.sh 240809_150346:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-09T16:39:08Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-08-09 18:39:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1154/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240809_150242:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240809_150244:cmsbot_crab_transferLogs - 0
activity-check.sh 240809_150246:cmsbot_crab_activity - 0
inputFiles-check.sh 240809_150249:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240809_150251:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240809_150253:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240809_150255:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240809_150257:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240809_150259:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240809_150301:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240809_150305:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240809_150308:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240809_150310:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240809_150312:cmsbot_crab_inputDBS - 0
useParent-check.sh 240809_150314:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240809_150316:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240809_150318:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240809_150320:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240809_150323:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240809_150325:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240809_150327:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240809_150329:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240809_150331:cmsbot_crab_whitelist - 0
blacklist-check.sh 240809_150333:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240809_150336:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240809_150338:cmsbot_crab_voRole - 0
voGroup-check.sh 240809_150340:cmsbot_crab_voGroup - 0
scheddName-check.sh 240809_150342:cmsbot_crab_scheddName - 0
collector-check.sh 240809_150344:cmsbot_crab_collector - 0
extraJDL-check.sh 240809_150346:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptExe-check.sh 240809_150303:cmsbot_crab_scriptExe - 1
```

## Comment (belforte, 2024-08-09T17:21:05Z)

the failed job simply timed out on some WN. Exit code 50664.

## Comment (cmsdmwmbot, 2024-08-09T19:47:57Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2024-08-09 21:47:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1155/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240809_150242:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240809_150244:cmsbot_crab_transferLogs - 0
activity-check.sh 240809_150246:cmsbot_crab_activity - 0
inputFiles-check.sh 240809_150249:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240809_150251:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240809_150253:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240809_150255:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240809_150257:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240809_150259:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240809_150301:cmsbot_crab_numCores - 0
scriptExe-check.sh 240809_150303:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240809_150305:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240809_150308:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240809_150310:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240809_150312:cmsbot_crab_inputDBS - 0
useParent-check.sh 240809_150314:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240809_150316:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240809_150318:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240809_150320:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240809_150323:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240809_150325:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240809_150327:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240809_150329:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240809_150331:cmsbot_crab_whitelist - 0
blacklist-check.sh 240809_150333:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240809_150336:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240809_150338:cmsbot_crab_voRole - 0
voGroup-check.sh 240809_150340:cmsbot_crab_voGroup - 0
scheddName-check.sh 240809_150342:cmsbot_crab_scheddName - 0
collector-check.sh 240809_150344:cmsbot_crab_collector - 0
extraJDL-check.sh 240809_150346:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-08-09T19:53:46Z)

good after resubmitting the failed job
