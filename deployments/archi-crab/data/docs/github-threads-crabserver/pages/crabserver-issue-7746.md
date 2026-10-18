# dmwm/CRABServer issue #7746: #433: Test prod CRABClient using preprod REST instance and CMSSW_12_5_0 CMSSW release

State: closed
Opened: 2023-07-12T14:25:11Z
Closed: 2023-07-12T16:07:56Z
URL: https://github.com/dmwm/CRABServer/issues/7746

## Opening post (cmsdmwmbot, 2023-07-12T14:25:11Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_5_0**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-07-12 16:25:10
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/433/)

## Comment (cmsdmwmbot, 2023-07-12T14:26:42Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230712_142528:cmsbot_crab_transferOutputs
230712_142530:cmsbot_crab_transferLogs
230712_142531:cmsbot_crab_activity
230712_142533:cmsbot_crab_inputFiles
230712_142534:cmsbot_crab_disableAutomaticOutputCollection
230712_142536:cmsbot_crab_outputFiles
230712_142537:cmsbot_crab_allowUndistributedCMSSW
230712_142539:cmsbot_crab_maxMemoryMB
230712_142540:cmsbot_crab_maxJobRuntimeMin
230712_142542:cmsbot_crab_numCores
230712_142543:cmsbot_crab_scriptExe
230712_142545:cmsbot_crab_scriptArgs
230712_142546:cmsbot_crab_sendPythonFolder
230712_142554:cmsbot_crab_sendExternalFolder
230712_142556:cmsbot_crab_inputDBS
230712_142557:cmsbot_crab_useParent
230712_142558:cmsbot_crab_secondaryInputDataset
230712_142600:cmsbot_crab_lumiMaskFile
230712_142601:cmsbot_crab_lumiMaskUrl
230712_142604:cmsbot_crab_outLFNDirBase
230712_142605:cmsbot_crab_runRange
230712_142607:cmsbot_crab_ignoreLocality
230712_142608:cmsbot_crab_userInputFiles
230712_142610:cmsbot_crab_whitelist
230712_142611:cmsbot_crab_blacklist
230712_142613:cmsbot_crab_ignoreGlobalBlacklist
230712_142615:cmsbot_crab_voRole
230712_142616:cmsbot_crab_voGroup
230712_142618:cmsbot_crab_scheddName
230712_142619:cmsbot_crab_collector
230712_142620:cmsbot_crab_extraJDL
```

Finished at: 2023-07-12 16:26:21
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/433/console)

## Comment (cmsdmwmbot, 2023-07-12T14:48:37Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-12 16:48:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/714/console

```
RETRY TESTS:
transferOutputs-check.sh 230712_142528:cmsbot_crab_transferOutputs - 2
transferLogs-check.sh 230712_142530:cmsbot_crab_transferLogs - 2
disableAutomaticOutputCollection-check.sh 230712_142534:cmsbot_crab_disableAutomaticOutputCollection - 2
outputFiles-check.sh 230712_142536:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 230712_142540:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230712_142542:cmsbot_crab_numCores - 2
scriptExe-check.sh 230712_142543:cmsbot_crab_scriptExe - 2
useParent-check.sh 230712_142557:cmsbot_crab_useParent - 2
lumiMaskFile-check.sh 230712_142600:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230712_142601:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230712_142604:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230712_142605:cmsbot_crab_runRange - 2
whitelist-check.sh 230712_142610:cmsbot_crab_whitelist - 2
blacklist-check.sh 230712_142611:cmsbot_crab_blacklist - 2
extraJDL-check.sh 230712_142620:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
activity-check.sh 230712_142531:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_142533:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230712_142537:cmsbot_crab_allowUndistributedCMSSW - 0
scriptArgs-check.sh 230712_142545:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_142546:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_142554:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_142556:cmsbot_crab_inputDBS - 0
userInputFiles-check.sh 230712_142608:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230712_142613:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_142615:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_142616:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_142618:cmsbot_crab_scheddName - 0
collector-check.sh 230712_142619:cmsbot_crab_collector - 0

FAILED TESTS:
maxMemoryMB-check.sh 230712_142539:cmsbot_crab_maxMemoryMB - 1
secondaryInputDataset-check.sh 230712_142558:cmsbot_crab_secondaryInputDataset - 1
ignoreLocality-check.sh 230712_142607:cmsbot_crab_ignoreLocality - 1
```

## Comment (cmsdmwmbot, 2023-07-12T15:10:50Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-12 17:10:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/718/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 230712_142540:cmsbot_crab_maxJobRuntimeMin - 2
runRange-check.sh 230712_142605:cmsbot_crab_runRange - 2
whitelist-check.sh 230712_142610:cmsbot_crab_whitelist - 2
blacklist-check.sh 230712_142611:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_142528:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_142530:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_142531:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_142533:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_142534:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_142536:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_142537:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_142539:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230712_142542:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_142543:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_142545:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_142546:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_142554:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_142556:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_142557:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_142558:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_142600:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230712_142601:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230712_142604:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230712_142607:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_142608:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230712_142613:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_142615:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_142616:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_142618:cmsbot_crab_scheddName - 0
collector-check.sh 230712_142619:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_142620:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-12T15:33:09Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-07-12 17:33:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/722/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_142528:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_142530:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_142531:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_142533:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_142534:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_142536:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_142537:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_142539:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_142540:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230712_142542:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_142543:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_142545:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_142546:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_142554:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_142556:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_142557:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_142558:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_142600:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230712_142601:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230712_142604:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230712_142605:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230712_142607:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_142608:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230712_142610:cmsbot_crab_whitelist - 0
blacklist-check.sh 230712_142611:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230712_142613:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_142615:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_142616:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_142618:cmsbot_crab_scheddName - 0
collector-check.sh 230712_142619:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_142620:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
