# dmwm/CRABServer issue #8138: #649: Test dev CRABClient using preprod REST instance and CMSSW_7_1_29 CMSSW release

State: closed
Opened: 2023-12-20T13:35:30Z
Closed: 2023-12-20T17:04:46Z
URL: https://github.com/dmwm/CRABServer/issues/8138

## Opening post (cmsdmwmbot, 2023-12-20T13:35:30Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_1_29**
- SCRAM_ARCH: **slc6_amd64_gcc481**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-20 14:35:30
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/649/)

## Comment (cmsdmwmbot, 2023-12-20T13:37:12Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231220_133543:cmsbot_crab_transferOutputs
231220_133544:cmsbot_crab_transferLogs
231220_133544:cmsbot_crab_activity
231220_133546:cmsbot_crab_inputFiles
231220_133547:cmsbot_crab_disableAutomaticOutputCollection
231220_133549:cmsbot_crab_outputFiles
231220_133550:cmsbot_crab_allowUndistributedCMSSW
231220_133551:cmsbot_crab_maxMemoryMB
231220_133552:cmsbot_crab_maxJobRuntimeMin
231220_133554:cmsbot_crab_numCores
231220_133555:cmsbot_crab_scriptExe
231220_133556:cmsbot_crab_scriptArgs
231220_133558:cmsbot_crab_sendVenvFolder
231220_133634:cmsbot_crab_sendExternalFolder
231220_133635:cmsbot_crab_inputDBS
231220_133636:cmsbot_crab_useParent
231220_133637:cmsbot_crab_secondaryInputDataset
231220_133638:cmsbot_crab_lumiMaskFile
231220_133640:cmsbot_crab_outLFNDirBase
231220_133640:cmsbot_crab_runRange
231220_133642:cmsbot_crab_ignoreLocality
231220_133643:cmsbot_crab_userInputFiles
231220_133644:cmsbot_crab_whitelist
231220_133645:cmsbot_crab_blacklist
231220_133645:cmsbot_crab_ignoreGlobalBlacklist
231220_133646:cmsbot_crab_voRole
231220_133647:cmsbot_crab_voGroup
231220_133648:cmsbot_crab_scheddName
231220_133649:cmsbot_crab_collector
231220_133650:cmsbot_crab_extraJDL
```

Finished at: 2023-12-20 14:36:51
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/649/console)

## Comment (cmsdmwmbot, 2023-12-20T13:58:07Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-20 14:58:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/833/console

```
RETRY TESTS:
transferLogs-check.sh 231220_133544:cmsbot_crab_transferLogs - 2
activity-check.sh 231220_133544:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 231220_133551:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 231220_133552:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 231220_133554:cmsbot_crab_numCores - 2
scriptExe-check.sh 231220_133555:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 231220_133556:cmsbot_crab_scriptArgs - 2
useParent-check.sh 231220_133636:cmsbot_crab_useParent - 2
blacklist-check.sh 231220_133645:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 231220_133645:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 231220_133646:cmsbot_crab_voRole - 2
voGroup-check.sh 231220_133647:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_133543:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 231220_133546:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_133547:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_133549:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_133550:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 231220_133558:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_133634:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_133635:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 231220_133637:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_133638:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231220_133640:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231220_133640:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231220_133642:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_133643:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231220_133644:cmsbot_crab_whitelist - 0
scheddName-check.sh 231220_133648:cmsbot_crab_scheddName - 0
collector-check.sh 231220_133649:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_133650:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-20T14:18:58Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-12-20 15:18:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/836/console

```
RETRY TESTS:
maxMemoryMB-check.sh 231220_133551:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 231220_133552:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 231220_133554:cmsbot_crab_numCores - 2
scriptExe-check.sh 231220_133555:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 231220_133556:cmsbot_crab_scriptArgs - 2
ignoreGlobalBlacklist-check.sh 231220_133645:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 231220_133646:cmsbot_crab_voRole - 2
voGroup-check.sh 231220_133647:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_133543:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231220_133544:cmsbot_crab_transferLogs - 0
activity-check.sh 231220_133544:cmsbot_crab_activity - 0
inputFiles-check.sh 231220_133546:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_133547:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_133549:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_133550:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 231220_133558:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_133634:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_133635:cmsbot_crab_inputDBS - 0
useParent-check.sh 231220_133636:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231220_133637:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_133638:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231220_133640:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231220_133640:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231220_133642:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_133643:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231220_133644:cmsbot_crab_whitelist - 0
blacklist-check.sh 231220_133645:cmsbot_crab_blacklist - 0
scheddName-check.sh 231220_133648:cmsbot_crab_scheddName - 0
collector-check.sh 231220_133649:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_133650:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-20T14:40:21Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-12-20 15:40:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/838/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_133543:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231220_133544:cmsbot_crab_transferLogs - 0
activity-check.sh 231220_133544:cmsbot_crab_activity - 0
inputFiles-check.sh 231220_133546:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_133547:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_133549:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_133550:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231220_133551:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231220_133552:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231220_133554:cmsbot_crab_numCores - 0
scriptExe-check.sh 231220_133555:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231220_133556:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231220_133558:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_133634:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_133635:cmsbot_crab_inputDBS - 0
useParent-check.sh 231220_133636:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231220_133637:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_133638:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231220_133640:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231220_133640:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231220_133642:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_133643:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231220_133644:cmsbot_crab_whitelist - 0
blacklist-check.sh 231220_133645:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231220_133645:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231220_133646:cmsbot_crab_voRole - 0
voGroup-check.sh 231220_133647:cmsbot_crab_voGroup - 0
scheddName-check.sh 231220_133648:cmsbot_crab_scheddName - 0
collector-check.sh 231220_133649:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_133650:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
