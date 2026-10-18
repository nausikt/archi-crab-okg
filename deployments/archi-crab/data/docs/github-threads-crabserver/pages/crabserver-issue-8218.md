# dmwm/CRABServer issue #8218: #699: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-02-02T09:43:33Z
Closed: 2024-02-02T11:03:20Z
URL: https://github.com/dmwm/CRABServer/issues/8218

## Opening post (cmsdmwmbot, 2024-02-02T09:43:33Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-02-02 10:43:33
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/699/)

## Comment (cmsdmwmbot, 2024-02-02T09:45:51Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_094351:cmsbot_crab_transferOutputs
240202_094353:cmsbot_crab_transferLogs
240202_094355:cmsbot_crab_activity
240202_094357:cmsbot_crab_inputFiles
240202_094359:cmsbot_crab_disableAutomaticOutputCollection
240202_094401:cmsbot_crab_outputFiles
240202_094403:cmsbot_crab_allowUndistributedCMSSW
240202_094405:cmsbot_crab_maxMemoryMB
240202_094407:cmsbot_crab_maxJobRuntimeMin
240202_094409:cmsbot_crab_numCores
240202_094411:cmsbot_crab_scriptExe
240202_094413:cmsbot_crab_scriptArgs
240202_094415:cmsbot_crab_sendVenvFolder
240202_094454:cmsbot_crab_sendExternalFolder
240202_094456:cmsbot_crab_inputDBS
240202_094458:cmsbot_crab_useParent
240202_094500:cmsbot_crab_secondaryInputDataset
240202_094503:cmsbot_crab_lumiMaskFile
240202_094505:cmsbot_crab_lumiMaskUrl
240202_094507:cmsbot_crab_outLFNDirBase
240202_094509:cmsbot_crab_runRange
240202_094511:cmsbot_crab_ignoreLocality
240202_094513:cmsbot_crab_userInputFiles
240202_094515:cmsbot_crab_whitelist
240202_094517:cmsbot_crab_blacklist
240202_094519:cmsbot_crab_ignoreGlobalBlacklist
240202_094521:cmsbot_crab_voRole
240202_094523:cmsbot_crab_voGroup
240202_094525:cmsbot_crab_scheddName
240202_094527:cmsbot_crab_collector
240202_094529:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 10:45:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/699/console)

## Comment (cmsdmwmbot, 2024-02-02T10:10:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 11:10:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/924/console

```
RETRY TESTS:
scriptExe-check.sh 240202_094411:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240202_094413:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240202_094505:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240202_094509:cmsbot_crab_runRange - 2
whitelist-check.sh 240202_094515:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_094517:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240202_094519:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240202_094521:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_094351:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_094353:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_094355:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_094357:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_094359:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_094401:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_094403:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_094405:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_094407:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_094409:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240202_094415:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_094454:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_094456:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_094458:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_094500:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_094503:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240202_094507:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240202_094511:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_094513:cmsbot_crab_userInputFiles - 0
voGroup-check.sh 240202_094523:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_094525:cmsbot_crab_scheddName - 0
collector-check.sh 240202_094527:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_094529:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T10:35:32Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-02-02 11:35:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/925/console

```
RETRY TESTS:
blacklist-check.sh 240202_094517:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_094351:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_094353:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_094355:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_094357:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_094359:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_094401:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_094403:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_094405:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_094407:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_094409:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_094411:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_094413:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_094415:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_094454:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_094456:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_094458:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_094500:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_094503:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_094505:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_094507:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_094509:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_094511:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_094513:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_094515:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240202_094519:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_094521:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_094523:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_094525:cmsbot_crab_scheddName - 0
collector-check.sh 240202_094527:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_094529:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T10:59:38Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-02-02 11:59:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/926/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_094351:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_094353:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_094355:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_094357:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_094359:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_094401:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_094403:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_094405:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_094407:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_094409:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_094411:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_094413:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_094415:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_094454:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_094456:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_094458:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_094500:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_094503:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_094505:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_094507:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_094509:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_094511:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_094513:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_094515:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_094517:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_094519:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_094521:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_094523:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_094525:cmsbot_crab_scheddName - 0
collector-check.sh 240202_094527:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_094529:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-02-02T11:03:20Z)

all OK
