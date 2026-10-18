# dmwm/CRABServer issue #8228: #708: Test prod CRABClient using test2 REST instance and CMSSW_9_4_21 CMSSW release

State: closed
Opened: 2024-02-02T17:13:31Z
Closed: 2024-02-03T18:09:52Z
URL: https://github.com/dmwm/CRABServer/issues/8228

## Opening post (cmsdmwmbot, 2024-02-02T17:13:31Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_9_4_21**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-02-02 18:13:31
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/708/)

## Comment (cmsdmwmbot, 2024-02-02T17:14:44Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_171351:cmsbot_crab_transferOutputs
240202_171352:cmsbot_crab_transferLogs
240202_171352:cmsbot_crab_activity
240202_171353:cmsbot_crab_inputFiles
240202_171354:cmsbot_crab_disableAutomaticOutputCollection
240202_171355:cmsbot_crab_outputFiles
240202_171356:cmsbot_crab_allowUndistributedCMSSW
240202_171357:cmsbot_crab_maxMemoryMB
240202_171358:cmsbot_crab_maxJobRuntimeMin
240202_171359:cmsbot_crab_numCores
240202_171359:cmsbot_crab_scriptExe
240202_171400:cmsbot_crab_scriptArgs
240202_171401:cmsbot_crab_sendVenvFolder
240202_171406:cmsbot_crab_sendExternalFolder
240202_171407:cmsbot_crab_inputDBS
240202_171408:cmsbot_crab_useParent
240202_171409:cmsbot_crab_secondaryInputDataset
240202_171409:cmsbot_crab_lumiMaskFile
240202_171410:cmsbot_crab_lumiMaskUrl
240202_171412:cmsbot_crab_outLFNDirBase
240202_171413:cmsbot_crab_runRange
240202_171414:cmsbot_crab_ignoreLocality
240202_171415:cmsbot_crab_userInputFiles
240202_171416:cmsbot_crab_whitelist
240202_171417:cmsbot_crab_blacklist
240202_171418:cmsbot_crab_ignoreGlobalBlacklist
240202_171419:cmsbot_crab_voRole
240202_171420:cmsbot_crab_voGroup
240202_171421:cmsbot_crab_scheddName
240202_171421:cmsbot_crab_collector
240202_171423:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 18:14:23
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/708/console)

## Comment (cmsdmwmbot, 2024-02-02T17:37:46Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 18:37:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/941/console

```
RETRY TESTS:
transferOutputs-check.sh 240202_171351:cmsbot_crab_transferOutputs - 2
transferLogs-check.sh 240202_171352:cmsbot_crab_transferLogs - 2
activity-check.sh 240202_171352:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 240202_171354:cmsbot_crab_disableAutomaticOutputCollection - 2
outputFiles-check.sh 240202_171355:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240202_171357:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240202_171358:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 240202_171359:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240202_171400:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240202_171409:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240202_171410:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240202_171413:cmsbot_crab_runRange - 2
whitelist-check.sh 240202_171416:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_171417:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240202_171418:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240202_171419:cmsbot_crab_voRole - 2
voGroup-check.sh 240202_171420:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 240202_171353:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 240202_171356:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240202_171359:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240202_171401:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_171406:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_171407:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_171408:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_171409:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240202_171412:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240202_171414:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_171415:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240202_171421:cmsbot_crab_scheddName - 0
collector-check.sh 240202_171421:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_171423:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T18:00:56Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-02-02 19:00:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/944/console

```
RETRY TESTS:
transferLogs-check.sh 240202_171352:cmsbot_crab_transferLogs - 2
lumiMaskFile-check.sh 240202_171409:cmsbot_crab_lumiMaskFile - 2
whitelist-check.sh 240202_171416:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_171417:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240202_171418:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240202_171419:cmsbot_crab_voRole - 2
voGroup-check.sh 240202_171420:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_171351:cmsbot_crab_transferOutputs - 0
activity-check.sh 240202_171352:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_171353:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_171354:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_171355:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_171356:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_171357:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_171358:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_171359:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_171359:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_171400:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_171401:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_171406:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_171407:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_171408:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_171409:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240202_171410:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_171412:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_171413:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_171414:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_171415:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240202_171421:cmsbot_crab_scheddName - 0
collector-check.sh 240202_171421:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_171423:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T18:25:02Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-02-02 19:25:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/948/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_171351:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_171352:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_171352:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_171353:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_171354:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_171355:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_171356:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_171357:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_171358:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_171359:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_171359:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_171400:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_171401:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_171406:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_171407:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_171408:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_171409:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_171409:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_171410:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_171412:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_171413:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_171414:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_171415:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_171416:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_171417:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_171418:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_171419:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_171420:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_171421:cmsbot_crab_scheddName - 0
collector-check.sh 240202_171421:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_171423:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
