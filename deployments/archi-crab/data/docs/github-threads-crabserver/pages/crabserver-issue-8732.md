# dmwm/CRABServer issue #8732: #852: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-10-04T08:54:29Z
Closed: 2024-10-10T22:42:25Z
URL: https://github.com/dmwm/CRABServer/issues/8732

## Opening post (cmsdmwmbot, 2024-10-04T08:54:29Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-10-04 10:35:36
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/852/)

## Comment (cmsdmwmbot, 2024-10-04T08:56:50Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241004_085456:cmsbot_crab_transferOutputs
241004_085509:cmsbot_crab_transferLogs
241004_085511:cmsbot_crab_activity
241004_085514:cmsbot_crab_inputFiles
241004_085517:cmsbot_crab_disableAutomaticOutputCollection
241004_085519:cmsbot_crab_outputFiles
241004_085522:cmsbot_crab_allowUndistributedCMSSW
241004_085525:cmsbot_crab_maxMemoryMB
241004_085527:cmsbot_crab_maxJobRuntimeMin
241004_085530:cmsbot_crab_numCores
241004_085533:cmsbot_crab_scriptExe
241004_085536:cmsbot_crab_scriptArgs
241004_085539:cmsbot_crab_sendVenvFolder
241004_085541:cmsbot_crab_sendExternalFolder
241004_085544:cmsbot_crab_inputDBS
241004_085547:cmsbot_crab_useParent
241004_085549:cmsbot_crab_secondaryInputDataset
241004_085552:cmsbot_crab_lumiMaskFile
241004_085555:cmsbot_crab_lumiMaskUrl
241004_085558:cmsbot_crab_outLFNDirBase
241004_085601:cmsbot_crab_runRange
241004_085604:cmsbot_crab_ignoreLocality
241004_085607:cmsbot_crab_userInputFiles
241004_085609:cmsbot_crab_whitelist
241004_085612:cmsbot_crab_blacklist
241004_085614:cmsbot_crab_ignoreGlobalBlacklist
241004_085617:cmsbot_crab_voRole
241004_085620:cmsbot_crab_voGroup
241004_085622:cmsbot_crab_scheddName
241004_085625:cmsbot_crab_collector
241004_085628:cmsbot_crab_extraJDL
```

Finished at: 2024-10-04 10:56:29
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/852/console)

## Comment (cmsdmwmbot, 2024-10-04T09:54:37Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-10-04 11:22:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1204/console

```
RETRY TESTS:
numCores-check.sh 241004_085530:cmsbot_crab_numCores - 2
lumiMaskFile-check.sh 241004_085552:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241004_085555:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 241004_085601:cmsbot_crab_runRange - 2
whitelist-check.sh 241004_085609:cmsbot_crab_whitelist - 2
blacklist-check.sh 241004_085612:cmsbot_crab_blacklist - 2
voRole-check.sh 241004_085617:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241004_085456:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241004_085509:cmsbot_crab_transferLogs - 0
activity-check.sh 241004_085511:cmsbot_crab_activity - 0
inputFiles-check.sh 241004_085514:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241004_085517:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241004_085519:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241004_085522:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241004_085525:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241004_085527:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 241004_085533:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241004_085536:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241004_085539:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241004_085541:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241004_085544:cmsbot_crab_inputDBS - 0
useParent-check.sh 241004_085547:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241004_085549:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 241004_085558:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 241004_085604:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241004_085607:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 241004_085614:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 241004_085620:cmsbot_crab_voGroup - 0
scheddName-check.sh 241004_085622:cmsbot_crab_scheddName - 0
collector-check.sh 241004_085625:cmsbot_crab_collector - 0
extraJDL-check.sh 241004_085628:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-10-04T10:54:45Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-10-04 12:19:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1205/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241004_085456:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241004_085509:cmsbot_crab_transferLogs - 0
activity-check.sh 241004_085511:cmsbot_crab_activity - 0
inputFiles-check.sh 241004_085514:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241004_085517:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241004_085519:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241004_085522:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241004_085525:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241004_085527:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241004_085530:cmsbot_crab_numCores - 0
scriptExe-check.sh 241004_085533:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241004_085536:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241004_085539:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241004_085541:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241004_085544:cmsbot_crab_inputDBS - 0
useParent-check.sh 241004_085547:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241004_085549:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241004_085552:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241004_085555:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241004_085558:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241004_085601:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241004_085604:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241004_085607:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241004_085609:cmsbot_crab_whitelist - 0
blacklist-check.sh 241004_085612:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241004_085614:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241004_085617:cmsbot_crab_voRole - 0
voGroup-check.sh 241004_085620:cmsbot_crab_voGroup - 0
scheddName-check.sh 241004_085622:cmsbot_crab_scheddName - 0
collector-check.sh 241004_085625:cmsbot_crab_collector - 0
extraJDL-check.sh 241004_085628:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
