# dmwm/CRABServer issue #7702: #412: Test prod CRABClient using test2 REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2023-06-29T20:43:29Z
Closed: 2023-06-30T09:05:48Z
URL: https://github.com/dmwm/CRABServer/issues/7702

## Opening post (cmsdmwmbot, 2023-06-29T20:43:29Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2023-06-29 22:43:28
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/412/)

## Comment (cmsdmwmbot, 2023-06-29T20:45:27Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_204359:cmsbot_crab_transferOutputs
230629_204400:cmsbot_crab_transferLogs
230629_204402:cmsbot_crab_activity
230629_204405:cmsbot_crab_inputFiles
230629_204407:cmsbot_crab_disableAutomaticOutputCollection
230629_204410:cmsbot_crab_outputFiles
230629_204417:cmsbot_crab_allowUndistributedCMSSW
230629_204419:cmsbot_crab_maxMemoryMB
230629_204421:cmsbot_crab_maxJobRuntimeMin
230629_204424:cmsbot_crab_numCores
230629_204426:cmsbot_crab_scriptExe
230629_204428:cmsbot_crab_scriptArgs
230629_204431:cmsbot_crab_sendPythonFolder
230629_204436:cmsbot_crab_sendExternalFolder
230629_204437:cmsbot_crab_inputDBS
230629_204439:cmsbot_crab_useParent
230629_204441:cmsbot_crab_secondaryInputDataset
230629_204443:cmsbot_crab_lumiMaskFile
230629_204446:cmsbot_crab_outLFNDirBase
230629_204447:cmsbot_crab_runRange
230629_204449:cmsbot_crab_ignoreLocality
230629_204450:cmsbot_crab_userInputFiles
230629_204452:cmsbot_crab_whitelist
230629_204454:cmsbot_crab_blacklist
230629_204456:cmsbot_crab_ignoreGlobalBlacklist
230629_204458:cmsbot_crab_voRole
230629_204500:cmsbot_crab_voGroup
230629_204502:cmsbot_crab_scheddName
230629_204504:cmsbot_crab_collector
230629_204506:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230629_204357:cmsbot_crab_20230629_224353
```

Finished at: 2023-06-29 22:45:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/412/console)

## Comment (cmsdmwmbot, 2023-06-29T21:07:14Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-29 23:07:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/353/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/353//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-29T21:11:11Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 23:11:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/640/console

```
RETRY TESTS:
transferLogs-check.sh 230629_204400:cmsbot_crab_transferLogs - 2
activity-check.sh 230629_204402:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 230629_204407:cmsbot_crab_disableAutomaticOutputCollection - 2
maxMemoryMB-check.sh 230629_204419:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230629_204421:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230629_204424:cmsbot_crab_numCores - 2
scriptExe-check.sh 230629_204426:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230629_204428:cmsbot_crab_scriptArgs - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_204359:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230629_204405:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 230629_204410:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_204417:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230629_204431:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_204436:cmsbot_crab_sendExternalFolder - 0
secondaryInputDataset-check.sh 230629_204441:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_204443:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230629_204446:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_204447:cmsbot_crab_runRange - 0
userInputFiles-check.sh 230629_204450:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_204452:cmsbot_crab_whitelist - 0

FAILED TESTS:
inputDBS-check.sh 230629_204437:cmsbot_crab_inputDBS - 1
useParent-check.sh 230629_204439:cmsbot_crab_useParent - 1
ignoreLocality-check.sh 230629_204449:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 230629_204454:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230629_204456:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230629_204458:cmsbot_crab_voRole - 1
voGroup-check.sh 230629_204500:cmsbot_crab_voGroup - 1
scheddName-check.sh 230629_204502:cmsbot_crab_scheddName - 1
collector-check.sh 230629_204504:cmsbot_crab_collector - 1
extraJDL-check.sh 230629_204506:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-06-29T21:34:02Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-29 23:34:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/646/console

```
RETRY TESTS:
transferLogs-check.sh 230629_204400:cmsbot_crab_transferLogs - 2
activity-check.sh 230629_204402:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 230629_204419:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230629_204421:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230629_204424:cmsbot_crab_numCores - 2
scriptExe-check.sh 230629_204426:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230629_204428:cmsbot_crab_scriptArgs - 2
blacklist-check.sh 230629_204454:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230629_204456:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230629_204458:cmsbot_crab_voRole - 2
voGroup-check.sh 230629_204500:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_204359:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230629_204405:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_204407:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_204410:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_204417:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230629_204431:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_204436:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_204437:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230629_204441:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_204443:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230629_204446:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_204447:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_204449:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_204450:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_204452:cmsbot_crab_whitelist - 0
scheddName-check.sh 230629_204502:cmsbot_crab_scheddName - 0
collector-check.sh 230629_204504:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_204506:cmsbot_crab_extraJDL - 0

FAILED TESTS:
useParent-check.sh 230629_204439:cmsbot_crab_useParent - 1
```

## Comment (cmsdmwmbot, 2023-06-29T21:57:51Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-29 23:57:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/652/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_204359:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_204400:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_204402:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_204405:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_204407:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_204410:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_204417:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_204419:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_204421:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_204424:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_204426:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_204428:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_204431:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_204436:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_204437:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230629_204441:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_204443:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230629_204446:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_204447:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_204449:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_204450:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_204452:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_204454:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_204456:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_204458:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_204500:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_204502:cmsbot_crab_scheddName - 0
collector-check.sh 230629_204504:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_204506:cmsbot_crab_extraJDL - 0

FAILED TESTS:
useParent-check.sh 230629_204439:cmsbot_crab_useParent - 1
```

## Comment (belforte, 2023-06-30T09:03:48Z)

useParent fails here becasue that file is not on disk. Let's call it success !
