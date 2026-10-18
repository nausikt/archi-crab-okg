# dmwm/CRABServer issue #7728: #429: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-07T20:25:24Z
Closed: 2023-07-07T22:42:23Z
URL: https://github.com/dmwm/CRABServer/issues/7728

## Opening post (cmsdmwmbot, 2023-07-07T20:25:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-07-07 22:25:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/429/)

## Comment (cmsdmwmbot, 2023-07-07T20:27:23Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230707_202546:cmsbot_crab_transferOutputs
230707_202547:cmsbot_crab_transferLogs
230707_202548:cmsbot_crab_activity
230707_202550:cmsbot_crab_inputFiles
230707_202551:cmsbot_crab_disableAutomaticOutputCollection
230707_202552:cmsbot_crab_outputFiles
230707_202553:cmsbot_crab_allowUndistributedCMSSW
230707_202555:cmsbot_crab_maxMemoryMB
230707_202556:cmsbot_crab_maxJobRuntimeMin
230707_202557:cmsbot_crab_numCores
230707_202558:cmsbot_crab_scriptExe
230707_202600:cmsbot_crab_scriptArgs
230707_202601:cmsbot_crab_sendPythonFolder
230707_202639:cmsbot_crab_sendExternalFolder
230707_202640:cmsbot_crab_inputDBS
230707_202641:cmsbot_crab_useParent
230707_202642:cmsbot_crab_secondaryInputDataset
230707_202643:cmsbot_crab_lumiMaskFile
230707_202645:cmsbot_crab_lumiMaskUrl
230707_202647:cmsbot_crab_outLFNDirBase
230707_202649:cmsbot_crab_runRange
230707_202650:cmsbot_crab_ignoreLocality
230707_202651:cmsbot_crab_userInputFiles
230707_202652:cmsbot_crab_whitelist
230707_202654:cmsbot_crab_blacklist
230707_202655:cmsbot_crab_ignoreGlobalBlacklist
230707_202656:cmsbot_crab_voRole
230707_202657:cmsbot_crab_voGroup
230707_202659:cmsbot_crab_scheddName
230707_202700:cmsbot_crab_collector
230707_202701:cmsbot_crab_extraJDL
```

Finished at: 2023-07-07 22:27:02
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/429/console)

## Comment (cmsdmwmbot, 2023-07-07T20:49:08Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 22:49:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/701/console

```
RETRY TESTS:
outputFiles-check.sh 230707_202552:cmsbot_crab_outputFiles - 2
numCores-check.sh 230707_202557:cmsbot_crab_numCores - 2
scriptArgs-check.sh 230707_202600:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 230707_202645:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230707_202649:cmsbot_crab_runRange - 2
whitelist-check.sh 230707_202652:cmsbot_crab_whitelist - 2
blacklist-check.sh 230707_202654:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_202546:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_202547:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_202548:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_202550:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_202551:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230707_202553:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_202555:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_202556:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230707_202558:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230707_202601:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_202639:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 230707_202641:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_202642:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_202643:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_202647:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_202650:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_202651:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230707_202655:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_202656:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_202657:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_202659:cmsbot_crab_scheddName - 0
collector-check.sh 230707_202700:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_202701:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputDBS-check.sh 230707_202640:cmsbot_crab_inputDBS - 1
```

## Comment (cmsdmwmbot, 2023-07-07T21:11:01Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-07 23:10:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/703/console

```
RETRY TESTS:
outputFiles-check.sh 230707_202552:cmsbot_crab_outputFiles - 2
numCores-check.sh 230707_202557:cmsbot_crab_numCores - 2
scriptArgs-check.sh 230707_202600:cmsbot_crab_scriptArgs - 2
whitelist-check.sh 230707_202652:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_202546:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_202547:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_202548:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_202550:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_202551:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230707_202553:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_202555:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_202556:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230707_202558:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230707_202601:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_202639:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 230707_202641:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_202642:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_202643:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_202645:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_202647:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_202649:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_202650:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_202651:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230707_202654:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_202655:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_202656:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_202657:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_202659:cmsbot_crab_scheddName - 0
collector-check.sh 230707_202700:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_202701:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputDBS-check.sh 230707_202640:cmsbot_crab_inputDBS - 1
```

## Comment (cmsdmwmbot, 2023-07-07T21:32:52Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-07 23:32:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/705/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_202546:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_202547:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_202548:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_202550:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_202551:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_202552:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_202553:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_202555:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_202556:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_202557:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_202558:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_202600:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_202601:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_202639:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 230707_202641:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_202642:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_202643:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_202645:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_202647:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_202649:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_202650:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_202651:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_202652:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_202654:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_202655:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_202656:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_202657:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_202659:cmsbot_crab_scheddName - 0
collector-check.sh 230707_202700:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_202701:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputDBS-check.sh 230707_202640:cmsbot_crab_inputDBS - 1
```

## Comment (belforte, 2023-07-07T22:42:23Z)

inputDBS test use a dataset on pys03. Location is not tracked in Rucio for those and locking must not be done. COde changed. Test fully OK
