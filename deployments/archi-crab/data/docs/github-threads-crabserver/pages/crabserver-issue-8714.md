# dmwm/CRABServer issue #8714: #839: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-20T20:55:11Z
Closed: 2024-09-20T22:48:25Z
URL: https://github.com/dmwm/CRABServer/issues/8714

## Opening post (cmsdmwmbot, 2024-09-20T20:55:11Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-09-20 22:55:10
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/839/)

## Comment (cmsdmwmbot, 2024-09-20T20:57:28Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240920_205545:cmsbot_crab_transferOutputs
240920_205548:cmsbot_crab_transferLogs
240920_205550:cmsbot_crab_activity
240920_205553:cmsbot_crab_inputFiles
240920_205556:cmsbot_crab_disableAutomaticOutputCollection
240920_205558:cmsbot_crab_outputFiles
240920_205601:cmsbot_crab_allowUndistributedCMSSW
240920_205603:cmsbot_crab_maxMemoryMB
240920_205605:cmsbot_crab_maxJobRuntimeMin
240920_205608:cmsbot_crab_numCores
240920_205611:cmsbot_crab_scriptExe
240920_205614:cmsbot_crab_scriptArgs
240920_205616:cmsbot_crab_sendVenvFolder
240920_205619:cmsbot_crab_sendExternalFolder
240920_205621:cmsbot_crab_inputDBS
240920_205624:cmsbot_crab_useParent
240920_205627:cmsbot_crab_secondaryInputDataset
240920_205629:cmsbot_crab_lumiMaskFile
240920_205632:cmsbot_crab_lumiMaskUrl
240920_205635:cmsbot_crab_outLFNDirBase
240920_205638:cmsbot_crab_runRange
240920_205640:cmsbot_crab_ignoreLocality
240920_205643:cmsbot_crab_userInputFiles
240920_205646:cmsbot_crab_whitelist
240920_205648:cmsbot_crab_blacklist
240920_205651:cmsbot_crab_ignoreGlobalBlacklist
240920_205654:cmsbot_crab_voRole
240920_205657:cmsbot_crab_voGroup
240920_205659:cmsbot_crab_scheddName
240920_205702:cmsbot_crab_collector
240920_205705:cmsbot_crab_extraJDL
```

Finished at: 2024-09-20 22:57:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/839/console)

## Comment (cmsdmwmbot, 2024-09-20T21:22:31Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-20 23:22:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1196/console

```
RETRY TESTS:
numCores-check.sh 240920_205608:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240920_205632:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240920_205638:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240920_205643:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240920_205646:cmsbot_crab_whitelist - 2
blacklist-check.sh 240920_205648:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240920_205651:cmsbot_crab_ignoreGlobalBlacklist - 2
voGroup-check.sh 240920_205657:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_205545:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_205548:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_205550:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_205553:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240920_205556:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240920_205558:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_205601:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240920_205603:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240920_205605:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240920_205611:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240920_205614:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_205616:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_205619:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_205621:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_205624:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240920_205627:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240920_205629:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240920_205635:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_205640:cmsbot_crab_ignoreLocality - 0
voRole-check.sh 240920_205654:cmsbot_crab_voRole - 0
scheddName-check.sh 240920_205659:cmsbot_crab_scheddName - 0
collector-check.sh 240920_205702:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_205705:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-09-20T21:47:47Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-09-20 23:47:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1197/console

```
RETRY TESTS:
numCores-check.sh 240920_205608:cmsbot_crab_numCores - 2
userInputFiles-check.sh 240920_205643:cmsbot_crab_userInputFiles - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_205545:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_205548:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_205550:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_205553:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240920_205556:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240920_205558:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_205601:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240920_205603:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240920_205605:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240920_205611:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240920_205614:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_205616:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_205619:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_205621:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_205624:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240920_205627:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240920_205629:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240920_205632:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_205635:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240920_205638:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240920_205640:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 240920_205646:cmsbot_crab_whitelist - 0
blacklist-check.sh 240920_205648:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240920_205651:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240920_205654:cmsbot_crab_voRole - 0
voGroup-check.sh 240920_205657:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_205659:cmsbot_crab_scheddName - 0
collector-check.sh 240920_205702:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_205705:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-09-20T22:12:24Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-09-21 00:12:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1198/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_205545:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_205548:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_205550:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_205553:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240920_205556:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240920_205558:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_205601:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240920_205603:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240920_205605:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240920_205608:cmsbot_crab_numCores - 0
scriptExe-check.sh 240920_205611:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240920_205614:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_205616:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_205619:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_205621:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_205624:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240920_205627:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240920_205629:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240920_205632:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_205635:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240920_205638:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240920_205640:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_205643:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240920_205646:cmsbot_crab_whitelist - 0
blacklist-check.sh 240920_205648:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240920_205651:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240920_205654:cmsbot_crab_voRole - 0
voGroup-check.sh 240920_205657:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_205659:cmsbot_crab_scheddName - 0
collector-check.sh 240920_205702:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_205705:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-09-20T22:48:25Z)

success
