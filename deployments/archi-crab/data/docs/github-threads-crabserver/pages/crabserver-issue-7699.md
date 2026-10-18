# dmwm/CRABServer issue #7699: #409: Test prod CRABClient using test2 REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-06-29T20:32:09Z
Closed: 2023-06-29T21:53:18Z
URL: https://github.com/dmwm/CRABServer/issues/7699

## Opening post (cmsdmwmbot, 2023-06-29T20:32:09Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2023-06-29 22:32:08
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/409/)

## Comment (cmsdmwmbot, 2023-06-29T20:35:39Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_203346:cmsbot_crab_transferOutputs
230629_203349:cmsbot_crab_transferLogs
230629_203351:cmsbot_crab_activity
230629_203354:cmsbot_crab_inputFiles
230629_203357:cmsbot_crab_disableAutomaticOutputCollection
230629_203400:cmsbot_crab_outputFiles
230629_203403:cmsbot_crab_allowUndistributedCMSSW
230629_203406:cmsbot_crab_maxMemoryMB
230629_203409:cmsbot_crab_maxJobRuntimeMin
230629_203412:cmsbot_crab_numCores
230629_203414:cmsbot_crab_scriptExe
230629_203417:cmsbot_crab_scriptArgs
230629_203420:cmsbot_crab_sendPythonFolder
230629_203427:cmsbot_crab_sendExternalFolder
230629_203430:cmsbot_crab_inputDBS
230629_203433:cmsbot_crab_useParent
230629_203436:cmsbot_crab_secondaryInputDataset
230629_203439:cmsbot_crab_lumiMaskFile
230629_203442:cmsbot_crab_lumiMaskUrl
230629_203446:cmsbot_crab_outLFNDirBase
230629_203449:cmsbot_crab_runRange
230629_203452:cmsbot_crab_ignoreLocality
230629_203454:cmsbot_crab_userInputFiles
230629_203457:cmsbot_crab_whitelist
230629_203500:cmsbot_crab_blacklist
230629_203503:cmsbot_crab_ignoreGlobalBlacklist
230629_203506:cmsbot_crab_voRole
230629_203508:cmsbot_crab_voGroup
230629_203511:cmsbot_crab_scheddName
230629_203514:cmsbot_crab_collector
230629_203517:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230629_203343:cmsbot_crab_20230629_223338
```

Finished at: 2023-06-29 22:35:18
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/409/console)

## Comment (cmsdmwmbot, 2023-06-29T20:58:24Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-29 22:58:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/351/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/351//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-29T21:00:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 23:00:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/636/console

```
RETRY TESTS:
outputFiles-check.sh 230629_203400:cmsbot_crab_outputFiles - 2
numCores-check.sh 230629_203412:cmsbot_crab_numCores - 2
scriptExe-check.sh 230629_203414:cmsbot_crab_scriptExe - 2
useParent-check.sh 230629_203433:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230629_203436:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 230629_203439:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230629_203442:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230629_203446:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230629_203449:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_203346:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_203349:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_203351:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_203354:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_203357:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230629_203403:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_203406:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_203409:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 230629_203417:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_203420:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_203427:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_203430:cmsbot_crab_inputDBS - 0
voGroup-check.sh 230629_203508:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_203511:cmsbot_crab_scheddName - 0
collector-check.sh 230629_203514:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_203517:cmsbot_crab_extraJDL - 0

FAILED TESTS:
ignoreLocality-check.sh 230629_203452:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230629_203454:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230629_203457:cmsbot_crab_whitelist - 1
blacklist-check.sh 230629_203500:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230629_203503:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230629_203506:cmsbot_crab_voRole - 1
```

## Comment (cmsdmwmbot, 2023-06-29T21:26:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-29 23:26:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/643/console

```
RETRY TESTS:
outputFiles-check.sh 230629_203400:cmsbot_crab_outputFiles - 2
numCores-check.sh 230629_203412:cmsbot_crab_numCores - 2
scriptExe-check.sh 230629_203414:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 230629_203442:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230629_203449:cmsbot_crab_runRange - 2
whitelist-check.sh 230629_203457:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_203500:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230629_203503:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_203346:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_203349:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_203351:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_203354:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_203357:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230629_203403:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_203406:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_203409:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 230629_203417:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_203420:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_203427:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_203430:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_203433:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_203436:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_203439:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230629_203446:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230629_203452:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_203454:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230629_203506:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_203508:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_203511:cmsbot_crab_scheddName - 0
collector-check.sh 230629_203514:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_203517:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T21:51:48Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-06-29 23:51:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/650/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_203346:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_203349:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_203351:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_203354:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_203357:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_203400:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_203403:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_203406:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_203409:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_203412:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_203414:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_203417:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_203420:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_203427:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_203430:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_203433:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_203436:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_203439:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_203442:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_203446:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_203449:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_203452:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_203454:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_203457:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_203500:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_203503:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_203506:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_203508:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_203511:cmsbot_crab_scheddName - 0
collector-check.sh 230629_203514:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_203517:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-06-29T21:53:18Z)

All OK
