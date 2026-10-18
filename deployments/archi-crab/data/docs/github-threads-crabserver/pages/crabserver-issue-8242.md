# dmwm/CRABServer issue #8242: #712: Test prod CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2024-02-16T14:02:43Z
Closed: 2024-02-18T17:24:26Z
URL: https://github.com/dmwm/CRABServer/issues/8242

## Opening post (cmsdmwmbot, 2024-02-16T14:02:43Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-02-16 15:02:42
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/712/)

## Comment (cmsdmwmbot, 2024-02-16T14:04:38Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240216_140303:cmsbot_crab_transferOutputs
240216_140305:cmsbot_crab_transferLogs
240216_140307:cmsbot_crab_activity
240216_140309:cmsbot_crab_inputFiles
240216_140311:cmsbot_crab_disableAutomaticOutputCollection
240216_140314:cmsbot_crab_outputFiles
240216_140316:cmsbot_crab_allowUndistributedCMSSW
240216_140318:cmsbot_crab_maxMemoryMB
240216_140320:cmsbot_crab_maxJobRuntimeMin
240216_140322:cmsbot_crab_numCores
240216_140325:cmsbot_crab_scriptExe
240216_140327:cmsbot_crab_scriptArgs
240216_140329:cmsbot_crab_sendVenvFolder
240216_140339:cmsbot_crab_sendExternalFolder
240216_140341:cmsbot_crab_inputDBS
240216_140343:cmsbot_crab_useParent
240216_140345:cmsbot_crab_secondaryInputDataset
240216_140347:cmsbot_crab_lumiMaskFile
240216_140349:cmsbot_crab_lumiMaskUrl
240216_140353:cmsbot_crab_outLFNDirBase
240216_140355:cmsbot_crab_runRange
240216_140357:cmsbot_crab_ignoreLocality
240216_140359:cmsbot_crab_userInputFiles
240216_140401:cmsbot_crab_whitelist
240216_140403:cmsbot_crab_blacklist
240216_140405:cmsbot_crab_ignoreGlobalBlacklist
240216_140407:cmsbot_crab_voRole
240216_140410:cmsbot_crab_voGroup
240216_140412:cmsbot_crab_scheddName
240216_140414:cmsbot_crab_collector
240216_140416:cmsbot_crab_extraJDL
```

Finished at: 2024-02-16 15:04:17
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/712/console)

## Comment (cmsdmwmbot, 2024-02-16T14:27:48Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-16 15:27:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/951/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 240216_140303:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240216_140305:cmsbot_crab_transferLogs - 1
activity-check.sh 240216_140307:cmsbot_crab_activity - 1
inputFiles-check.sh 240216_140309:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240216_140311:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240216_140314:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240216_140316:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240216_140318:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240216_140320:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240216_140322:cmsbot_crab_numCores - 1
scriptExe-check.sh 240216_140325:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240216_140327:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240216_140329:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240216_140339:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240216_140341:cmsbot_crab_inputDBS - 1
useParent-check.sh 240216_140343:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240216_140345:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240216_140347:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240216_140349:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240216_140353:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240216_140355:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240216_140357:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240216_140359:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240216_140401:cmsbot_crab_whitelist - 1
blacklist-check.sh 240216_140403:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240216_140405:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240216_140407:cmsbot_crab_voRole - 1
voGroup-check.sh 240216_140410:cmsbot_crab_voGroup - 1
scheddName-check.sh 240216_140412:cmsbot_crab_scheddName - 1
collector-check.sh 240216_140414:cmsbot_crab_collector - 1
extraJDL-check.sh 240216_140416:cmsbot_crab_extraJDL - 1
```
