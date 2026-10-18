# dmwm/CRABServer issue #8465: #793: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-03T19:15:14Z
Closed: 2024-06-03T21:25:40Z
URL: https://github.com/dmwm/CRABServer/issues/8465

## Opening post (cmsdmwmbot, 2024-06-03T19:15:14Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-06-03 21:15:13
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/793/)

## Comment (cmsdmwmbot, 2024-06-03T19:17:01Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240603_191537:cmsbot_crab_transferOutputs
240603_191539:cmsbot_crab_transferLogs
240603_191541:cmsbot_crab_activity
240603_191543:cmsbot_crab_inputFiles
240603_191546:cmsbot_crab_disableAutomaticOutputCollection
240603_191548:cmsbot_crab_outputFiles
240603_191550:cmsbot_crab_allowUndistributedCMSSW
240603_191552:cmsbot_crab_maxMemoryMB
240603_191554:cmsbot_crab_maxJobRuntimeMin
240603_191556:cmsbot_crab_numCores
240603_191558:cmsbot_crab_scriptExe
240603_191600:cmsbot_crab_scriptArgs
240603_191602:cmsbot_crab_sendVenvFolder
240603_191604:cmsbot_crab_sendExternalFolder
240603_191606:cmsbot_crab_inputDBS
240603_191608:cmsbot_crab_useParent
240603_191610:cmsbot_crab_secondaryInputDataset
240603_191612:cmsbot_crab_lumiMaskFile
240603_191614:cmsbot_crab_lumiMaskUrl
240603_191617:cmsbot_crab_outLFNDirBase
240603_191619:cmsbot_crab_runRange
240603_191621:cmsbot_crab_ignoreLocality
240603_191623:cmsbot_crab_userInputFiles
240603_191625:cmsbot_crab_whitelist
240603_191627:cmsbot_crab_blacklist
240603_191629:cmsbot_crab_ignoreGlobalBlacklist
240603_191631:cmsbot_crab_voRole
240603_191633:cmsbot_crab_voGroup
240603_191635:cmsbot_crab_scheddName
240603_191637:cmsbot_crab_collector
240603_191639:cmsbot_crab_extraJDL
```

Finished at: 2024-06-03 21:16:40
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/793/console)

## Comment (cmsdmwmbot, 2024-06-03T19:42:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-03 21:42:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1092/console

```
RETRY TESTS:
transferLogs-check.sh 240603_191539:cmsbot_crab_transferLogs - 2
activity-check.sh 240603_191541:cmsbot_crab_activity - 2
outputFiles-check.sh 240603_191548:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240603_191552:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 240603_191556:cmsbot_crab_numCores - 2
scriptExe-check.sh 240603_191558:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240603_191614:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240603_191619:cmsbot_crab_runRange - 2
whitelist-check.sh 240603_191625:cmsbot_crab_whitelist - 2
blacklist-check.sh 240603_191627:cmsbot_crab_blacklist - 2
voGroup-check.sh 240603_191633:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_191537:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240603_191543:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_191546:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240603_191550:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240603_191554:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 240603_191600:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240603_191602:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_191604:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_191606:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_191608:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_191610:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240603_191612:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240603_191617:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240603_191621:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_191623:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240603_191629:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_191631:cmsbot_crab_voRole - 0
scheddName-check.sh 240603_191635:cmsbot_crab_scheddName - 0
collector-check.sh 240603_191637:cmsbot_crab_collector - 0
extraJDL-check.sh 240603_191639:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-03T20:07:16Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-03 22:07:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1093/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_191537:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_191539:cmsbot_crab_transferLogs - 0
activity-check.sh 240603_191541:cmsbot_crab_activity - 0
inputFiles-check.sh 240603_191543:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_191546:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240603_191548:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240603_191550:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240603_191552:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240603_191554:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240603_191556:cmsbot_crab_numCores - 0
scriptExe-check.sh 240603_191558:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240603_191600:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240603_191602:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_191604:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_191606:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_191608:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_191610:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240603_191612:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240603_191614:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240603_191617:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240603_191619:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240603_191621:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_191623:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240603_191625:cmsbot_crab_whitelist - 0
blacklist-check.sh 240603_191627:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240603_191629:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_191631:cmsbot_crab_voRole - 0
voGroup-check.sh 240603_191633:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_191635:cmsbot_crab_scheddName - 0
collector-check.sh 240603_191637:cmsbot_crab_collector - 0
extraJDL-check.sh 240603_191639:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-06-03T21:25:40Z)

perfect !
