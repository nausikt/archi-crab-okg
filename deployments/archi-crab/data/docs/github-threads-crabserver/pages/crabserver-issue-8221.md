# dmwm/CRABServer issue #8221: #702: Test prod CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2024-02-02T11:43:05Z
Closed: 2024-02-02T14:47:10Z
URL: https://github.com/dmwm/CRABServer/issues/8221

## Opening post (cmsdmwmbot, 2024-02-02T11:43:05Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-02-02 12:43:04
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/702/)

## Comment (cmsdmwmbot, 2024-02-02T11:45:07Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_114349:cmsbot_crab_transferOutputs
240202_114350:cmsbot_crab_transferLogs
240202_114351:cmsbot_crab_activity
240202_114353:cmsbot_crab_inputFiles
240202_114354:cmsbot_crab_disableAutomaticOutputCollection
240202_114356:cmsbot_crab_outputFiles
240202_114357:cmsbot_crab_allowUndistributedCMSSW
240202_114358:cmsbot_crab_maxMemoryMB
240202_114359:cmsbot_crab_maxJobRuntimeMin
240202_114401:cmsbot_crab_numCores
240202_114402:cmsbot_crab_scriptExe
240202_114404:cmsbot_crab_scriptArgs
240202_114406:cmsbot_crab_sendVenvFolder
240202_114412:cmsbot_crab_sendExternalFolder
240202_114413:cmsbot_crab_inputDBS
240202_114414:cmsbot_crab_useParent
240202_114415:cmsbot_crab_secondaryInputDataset
240202_114416:cmsbot_crab_lumiMaskFile
240202_114418:cmsbot_crab_lumiMaskUrl
240202_114433:cmsbot_crab_outLFNDirBase
240202_114434:cmsbot_crab_runRange
240202_114435:cmsbot_crab_ignoreLocality
240202_114436:cmsbot_crab_userInputFiles
240202_114437:cmsbot_crab_whitelist
240202_114438:cmsbot_crab_blacklist
240202_114439:cmsbot_crab_ignoreGlobalBlacklist
240202_114440:cmsbot_crab_voRole
240202_114441:cmsbot_crab_voGroup
240202_114443:cmsbot_crab_scheddName
240202_114444:cmsbot_crab_collector
240202_114445:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 12:44:46
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/702/console)

## Comment (cmsdmwmbot, 2024-02-02T12:10:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 13:10:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/929/console

```
RETRY TESTS:
transferLogs-check.sh 240202_114350:cmsbot_crab_transferLogs - 2
maxJobRuntimeMin-check.sh 240202_114359:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240202_114401:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240202_114418:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240202_114434:cmsbot_crab_runRange - 2
whitelist-check.sh 240202_114437:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_114438:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114349:cmsbot_crab_transferOutputs - 0
activity-check.sh 240202_114351:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_114353:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114354:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_114356:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_114357:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_114358:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240202_114402:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_114404:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_114406:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114412:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114413:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_114414:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_114415:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114416:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240202_114433:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240202_114435:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_114436:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240202_114439:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_114440:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_114441:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_114443:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114444:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_114445:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T12:34:58Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-02-02 13:34:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/934/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114349:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_114350:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_114351:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_114353:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114354:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_114356:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_114357:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_114358:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_114359:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_114401:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_114402:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_114404:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_114406:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114412:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114413:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_114414:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_114415:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114416:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_114418:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_114433:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_114434:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_114435:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_114436:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_114437:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_114438:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_114439:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_114440:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_114441:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_114443:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114444:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_114445:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-02-02T14:47:10Z)

OK
