# dmwm/CRABServer issue #8243: #713: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-02-16T14:34:57Z
Closed: 2024-02-18T17:24:26Z
URL: https://github.com/dmwm/CRABServer/issues/8243

## Opening post (cmsdmwmbot, 2024-02-16T14:34:57Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-02-16 15:34:56
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/713/)

## Comment (cmsdmwmbot, 2024-02-16T14:38:04Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240216_143550:cmsbot_crab_transferOutputs
240216_143552:cmsbot_crab_transferLogs
240216_143554:cmsbot_crab_activity
240216_143556:cmsbot_crab_inputFiles
240216_143558:cmsbot_crab_disableAutomaticOutputCollection
240216_143600:cmsbot_crab_outputFiles
240216_143602:cmsbot_crab_allowUndistributedCMSSW
240216_143604:cmsbot_crab_maxMemoryMB
240216_143606:cmsbot_crab_maxJobRuntimeMin
240216_143610:cmsbot_crab_numCores
240216_143613:cmsbot_crab_scriptExe
240216_143615:cmsbot_crab_scriptArgs
240216_143617:cmsbot_crab_sendVenvFolder
240216_143706:cmsbot_crab_sendExternalFolder
240216_143708:cmsbot_crab_inputDBS
240216_143710:cmsbot_crab_useParent
240216_143712:cmsbot_crab_secondaryInputDataset
240216_143714:cmsbot_crab_lumiMaskFile
240216_143717:cmsbot_crab_lumiMaskUrl
240216_143720:cmsbot_crab_outLFNDirBase
240216_143722:cmsbot_crab_runRange
240216_143724:cmsbot_crab_ignoreLocality
240216_143726:cmsbot_crab_userInputFiles
240216_143728:cmsbot_crab_whitelist
240216_143730:cmsbot_crab_blacklist
240216_143732:cmsbot_crab_ignoreGlobalBlacklist
240216_143734:cmsbot_crab_voRole
240216_143736:cmsbot_crab_voGroup
240216_143738:cmsbot_crab_scheddName
240216_143740:cmsbot_crab_collector
240216_143742:cmsbot_crab_extraJDL
```

Finished at: 2024-02-16 15:37:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/713/console)

## Comment (cmsdmwmbot, 2024-02-16T15:04:23Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-16 16:04:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/952/console

```
RETRY TESTS:
transferLogs-check.sh 240216_143552:cmsbot_crab_transferLogs - 2
scriptArgs-check.sh 240216_143615:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240216_143714:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240216_143717:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240216_143722:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240216_143726:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240216_143728:cmsbot_crab_whitelist - 2
blacklist-check.sh 240216_143730:cmsbot_crab_blacklist - 2
voGroup-check.sh 240216_143736:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240216_143550:cmsbot_crab_transferOutputs - 0
activity-check.sh 240216_143554:cmsbot_crab_activity - 0
inputFiles-check.sh 240216_143556:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240216_143558:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240216_143602:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240216_143604:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240216_143606:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240216_143610:cmsbot_crab_numCores - 0
scriptExe-check.sh 240216_143613:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240216_143617:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240216_143706:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240216_143708:cmsbot_crab_inputDBS - 0
useParent-check.sh 240216_143710:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240216_143712:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240216_143720:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240216_143724:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240216_143732:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240216_143734:cmsbot_crab_voRole - 0
scheddName-check.sh 240216_143738:cmsbot_crab_scheddName - 0
collector-check.sh 240216_143740:cmsbot_crab_collector - 0
extraJDL-check.sh 240216_143742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240216_143600:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-16T15:30:55Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-02-16 16:30:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/953/console

```
RETRY TESTS:
transferLogs-check.sh 240216_143552:cmsbot_crab_transferLogs - 2
scriptArgs-check.sh 240216_143615:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240216_143714:cmsbot_crab_lumiMaskFile - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240216_143550:cmsbot_crab_transferOutputs - 0
activity-check.sh 240216_143554:cmsbot_crab_activity - 0
inputFiles-check.sh 240216_143556:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240216_143558:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240216_143602:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240216_143604:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240216_143606:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240216_143610:cmsbot_crab_numCores - 0
scriptExe-check.sh 240216_143613:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240216_143617:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240216_143706:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240216_143708:cmsbot_crab_inputDBS - 0
useParent-check.sh 240216_143710:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240216_143712:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240216_143717:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240216_143720:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240216_143722:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240216_143724:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240216_143726:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240216_143728:cmsbot_crab_whitelist - 0
blacklist-check.sh 240216_143730:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240216_143732:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240216_143734:cmsbot_crab_voRole - 0
voGroup-check.sh 240216_143736:cmsbot_crab_voGroup - 0
scheddName-check.sh 240216_143738:cmsbot_crab_scheddName - 0
collector-check.sh 240216_143740:cmsbot_crab_collector - 0
extraJDL-check.sh 240216_143742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240216_143600:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-16T15:57:30Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-02-16 16:57:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/954/console

```
RETRY TESTS:
transferLogs-check.sh 240216_143552:cmsbot_crab_transferLogs - 2
scriptArgs-check.sh 240216_143615:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240216_143714:cmsbot_crab_lumiMaskFile - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240216_143550:cmsbot_crab_transferOutputs - 0
activity-check.sh 240216_143554:cmsbot_crab_activity - 0
inputFiles-check.sh 240216_143556:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240216_143558:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240216_143602:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240216_143604:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240216_143606:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240216_143610:cmsbot_crab_numCores - 0
scriptExe-check.sh 240216_143613:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240216_143617:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240216_143706:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240216_143708:cmsbot_crab_inputDBS - 0
useParent-check.sh 240216_143710:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240216_143712:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240216_143717:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240216_143720:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240216_143722:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240216_143724:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240216_143726:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240216_143728:cmsbot_crab_whitelist - 0
blacklist-check.sh 240216_143730:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240216_143732:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240216_143734:cmsbot_crab_voRole - 0
voGroup-check.sh 240216_143736:cmsbot_crab_voGroup - 0
scheddName-check.sh 240216_143738:cmsbot_crab_scheddName - 0
collector-check.sh 240216_143740:cmsbot_crab_collector - 0
extraJDL-check.sh 240216_143742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240216_143600:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-16T16:23:43Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-16 17:23:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/955/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240216_143550:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240216_143552:cmsbot_crab_transferLogs - 0
activity-check.sh 240216_143554:cmsbot_crab_activity - 0
inputFiles-check.sh 240216_143556:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240216_143558:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240216_143602:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240216_143604:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240216_143606:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240216_143610:cmsbot_crab_numCores - 0
scriptExe-check.sh 240216_143613:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240216_143615:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240216_143617:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240216_143706:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240216_143708:cmsbot_crab_inputDBS - 0
useParent-check.sh 240216_143710:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240216_143712:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240216_143714:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240216_143717:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240216_143720:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240216_143722:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240216_143724:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240216_143726:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240216_143728:cmsbot_crab_whitelist - 0
blacklist-check.sh 240216_143730:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240216_143732:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240216_143734:cmsbot_crab_voRole - 0
voGroup-check.sh 240216_143736:cmsbot_crab_voGroup - 0
scheddName-check.sh 240216_143738:cmsbot_crab_scheddName - 0
collector-check.sh 240216_143740:cmsbot_crab_collector - 0
extraJDL-check.sh 240216_143742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240216_143600:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-16T21:45:31Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-16 22:45:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/956/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240216_143550:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240216_143552:cmsbot_crab_transferLogs - 0
activity-check.sh 240216_143554:cmsbot_crab_activity - 0
inputFiles-check.sh 240216_143556:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240216_143558:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240216_143602:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240216_143604:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240216_143606:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240216_143610:cmsbot_crab_numCores - 0
scriptExe-check.sh 240216_143613:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240216_143615:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240216_143617:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240216_143706:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240216_143708:cmsbot_crab_inputDBS - 0
useParent-check.sh 240216_143710:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240216_143712:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240216_143714:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240216_143717:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240216_143720:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240216_143722:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240216_143724:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240216_143726:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240216_143728:cmsbot_crab_whitelist - 0
blacklist-check.sh 240216_143730:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240216_143732:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240216_143734:cmsbot_crab_voRole - 0
voGroup-check.sh 240216_143736:cmsbot_crab_voGroup - 0
scheddName-check.sh 240216_143738:cmsbot_crab_scheddName - 0
collector-check.sh 240216_143740:cmsbot_crab_collector - 0
extraJDL-check.sh 240216_143742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240216_143600:cmsbot_crab_outputFiles - 1
```
