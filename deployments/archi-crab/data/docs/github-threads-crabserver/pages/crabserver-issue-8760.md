# dmwm/CRABServer issue #8760: #860: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-01T12:33:08Z
Closed: 2024-11-01T14:14:27Z
URL: https://github.com/dmwm/CRABServer/issues/8760

## Opening post (cmsdmwmbot, 2024-11-01T12:33:08Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-11-01 13:33:07
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/860/)

## Comment (cmsdmwmbot, 2024-11-01T12:35:14Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241101_123333:cmsbot_crab_transferOutputs
241101_123335:cmsbot_crab_transferLogs
241101_123338:cmsbot_crab_activity
241101_123341:cmsbot_crab_inputFiles
241101_123343:cmsbot_crab_disableAutomaticOutputCollection
241101_123346:cmsbot_crab_outputFiles
241101_123348:cmsbot_crab_allowUndistributedCMSSW
241101_123351:cmsbot_crab_maxMemoryMB
241101_123353:cmsbot_crab_maxJobRuntimeMin
241101_123356:cmsbot_crab_numCores
241101_123358:cmsbot_crab_scriptExe
241101_123401:cmsbot_crab_scriptArgs
241101_123404:cmsbot_crab_sendVenvFolder
241101_123406:cmsbot_crab_sendExternalFolder
241101_123411:cmsbot_crab_inputDBS
241101_123413:cmsbot_crab_useParent
241101_123416:cmsbot_crab_secondaryInputDataset
241101_123418:cmsbot_crab_lumiMaskFile
241101_123421:cmsbot_crab_lumiMaskUrl
241101_123424:cmsbot_crab_outLFNDirBase
241101_123427:cmsbot_crab_runRange
241101_123429:cmsbot_crab_ignoreLocality
241101_123432:cmsbot_crab_userInputFiles
241101_123434:cmsbot_crab_whitelist
241101_123437:cmsbot_crab_blacklist
241101_123439:cmsbot_crab_ignoreGlobalBlacklist
241101_123442:cmsbot_crab_voRole
241101_123444:cmsbot_crab_voGroup
241101_123447:cmsbot_crab_scheddName
241101_123449:cmsbot_crab_collector
241101_123452:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241101_123330:cmsbot_crab_20241101_133329
```

Finished at: 2024-11-01 13:34:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/860/console)

## Comment (cmsdmwmbot, 2024-11-01T12:59:16Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-11-01 13:59:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/557/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/557//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-11-01T13:00:37Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-01 14:00:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1213/console

```
RETRY TESTS:
activity-check.sh 241101_123338:cmsbot_crab_activity - 2
outputFiles-check.sh 241101_123346:cmsbot_crab_outputFiles - 2
scriptExe-check.sh 241101_123358:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 241101_123401:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 241101_123418:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241101_123421:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241101_123424:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241101_123427:cmsbot_crab_runRange - 2
whitelist-check.sh 241101_123434:cmsbot_crab_whitelist - 2
blacklist-check.sh 241101_123437:cmsbot_crab_blacklist - 2
voGroup-check.sh 241101_123444:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241101_123333:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241101_123335:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 241101_123341:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241101_123343:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241101_123348:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241101_123351:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241101_123353:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241101_123356:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 241101_123404:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241101_123406:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241101_123411:cmsbot_crab_inputDBS - 0
useParent-check.sh 241101_123413:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241101_123416:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 241101_123429:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241101_123432:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 241101_123439:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241101_123442:cmsbot_crab_voRole - 0
scheddName-check.sh 241101_123447:cmsbot_crab_scheddName - 0
collector-check.sh 241101_123449:cmsbot_crab_collector - 0
extraJDL-check.sh 241101_123452:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-01T13:25:22Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-01 14:25:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1215/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241101_123333:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241101_123335:cmsbot_crab_transferLogs - 0
activity-check.sh 241101_123338:cmsbot_crab_activity - 0
inputFiles-check.sh 241101_123341:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241101_123343:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241101_123346:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241101_123348:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241101_123351:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241101_123353:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241101_123356:cmsbot_crab_numCores - 0
scriptExe-check.sh 241101_123358:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241101_123401:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241101_123404:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241101_123406:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241101_123411:cmsbot_crab_inputDBS - 0
useParent-check.sh 241101_123413:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241101_123416:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241101_123418:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241101_123421:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241101_123424:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241101_123427:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241101_123429:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241101_123432:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241101_123434:cmsbot_crab_whitelist - 0
blacklist-check.sh 241101_123437:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241101_123439:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241101_123442:cmsbot_crab_voRole - 0
voGroup-check.sh 241101_123444:cmsbot_crab_voGroup - 0
scheddName-check.sh 241101_123447:cmsbot_crab_scheddName - 0
collector-check.sh 241101_123449:cmsbot_crab_collector - 0
extraJDL-check.sh 241101_123452:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-11-01T14:14:27Z)

all OK
