# dmwm/CRABServer issue #7679: #394: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-27T13:25:40Z
Closed: 2023-06-27T14:47:38Z
URL: https://github.com/dmwm/CRABServer/issues/7679

## Opening post (cmsdmwmbot, 2023-06-27T13:25:40Z)

this is to vallidate https://github.com/belforte/CRABServer/tree/expand-user-tar-fix-7661

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2023-06-27 15:25:39
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/394/)

## Comment (cmsdmwmbot, 2023-06-27T13:27:52Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230627_132601:cmsbot_crab_transferOutputs
230627_132602:cmsbot_crab_transferLogs
230627_132603:cmsbot_crab_activity
230627_132605:cmsbot_crab_inputFiles
230627_132606:cmsbot_crab_disableAutomaticOutputCollection
230627_132607:cmsbot_crab_outputFiles
230627_132609:cmsbot_crab_allowUndistributedCMSSW
230627_132610:cmsbot_crab_maxMemoryMB
230627_132611:cmsbot_crab_maxJobRuntimeMin
230627_132613:cmsbot_crab_numCores
230627_132614:cmsbot_crab_scriptExe
230627_132615:cmsbot_crab_scriptArgs
230627_132617:cmsbot_crab_sendPythonFolder
230627_132706:cmsbot_crab_sendExternalFolder
230627_132708:cmsbot_crab_inputDBS
230627_132709:cmsbot_crab_useParent
230627_132710:cmsbot_crab_secondaryInputDataset
230627_132711:cmsbot_crab_lumiMaskFile
230627_132713:cmsbot_crab_lumiMaskUrl
230627_132715:cmsbot_crab_outLFNDirBase
230627_132716:cmsbot_crab_runRange
230627_132718:cmsbot_crab_ignoreLocality
230627_132719:cmsbot_crab_userInputFiles
230627_132720:cmsbot_crab_whitelist
230627_132722:cmsbot_crab_blacklist
230627_132723:cmsbot_crab_ignoreGlobalBlacklist
230627_132724:cmsbot_crab_voRole
230627_132726:cmsbot_crab_voGroup
230627_132727:cmsbot_crab_scheddName
230627_132728:cmsbot_crab_collector
230627_132730:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230627_132559:cmsbot_crab_20230627_152557
```

Finished at: 2023-06-27 15:27:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/394/console)

## Comment (cmsdmwmbot, 2023-06-27T13:48:50Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-27 15:48:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/346/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/346//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-27T13:49:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-27 15:49:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/612/console

```
RETRY TESTS:
outputFiles-check.sh 230627_132607:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230627_132610:cmsbot_crab_maxMemoryMB - 2
lumiMaskUrl-check.sh 230627_132713:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230627_132715:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230627_132716:cmsbot_crab_runRange - 2
whitelist-check.sh 230627_132720:cmsbot_crab_whitelist - 2
blacklist-check.sh 230627_132722:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230627_132601:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230627_132602:cmsbot_crab_transferLogs - 0
activity-check.sh 230627_132603:cmsbot_crab_activity - 0
inputFiles-check.sh 230627_132605:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230627_132606:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230627_132609:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230627_132611:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230627_132613:cmsbot_crab_numCores - 0
scriptExe-check.sh 230627_132614:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230627_132615:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230627_132617:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_132706:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_132708:cmsbot_crab_inputDBS - 0
useParent-check.sh 230627_132709:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230627_132710:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230627_132711:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230627_132718:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230627_132719:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230627_132723:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230627_132724:cmsbot_crab_voRole - 0
voGroup-check.sh 230627_132726:cmsbot_crab_voGroup - 0
scheddName-check.sh 230627_132727:cmsbot_crab_scheddName - 0
collector-check.sh 230627_132728:cmsbot_crab_collector - 0
extraJDL-check.sh 230627_132730:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-27T14:12:06Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-27 16:12:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/613/console

```
RETRY TESTS:
runRange-check.sh 230627_132716:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230627_132601:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230627_132602:cmsbot_crab_transferLogs - 0
activity-check.sh 230627_132603:cmsbot_crab_activity - 0
inputFiles-check.sh 230627_132605:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230627_132606:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230627_132607:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230627_132609:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230627_132610:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230627_132611:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230627_132613:cmsbot_crab_numCores - 0
scriptExe-check.sh 230627_132614:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230627_132615:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230627_132617:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_132706:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_132708:cmsbot_crab_inputDBS - 0
useParent-check.sh 230627_132709:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230627_132710:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230627_132711:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230627_132713:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230627_132715:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230627_132718:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230627_132719:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230627_132720:cmsbot_crab_whitelist - 0
blacklist-check.sh 230627_132722:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230627_132723:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230627_132724:cmsbot_crab_voRole - 0
voGroup-check.sh 230627_132726:cmsbot_crab_voGroup - 0
scheddName-check.sh 230627_132727:cmsbot_crab_scheddName - 0
collector-check.sh 230627_132728:cmsbot_crab_collector - 0
extraJDL-check.sh 230627_132730:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-27T14:34:15Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-06-27 16:34:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/614/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230627_132601:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230627_132602:cmsbot_crab_transferLogs - 0
activity-check.sh 230627_132603:cmsbot_crab_activity - 0
inputFiles-check.sh 230627_132605:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230627_132606:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230627_132607:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230627_132609:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230627_132610:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230627_132611:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230627_132613:cmsbot_crab_numCores - 0
scriptExe-check.sh 230627_132614:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230627_132615:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230627_132617:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_132706:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_132708:cmsbot_crab_inputDBS - 0
useParent-check.sh 230627_132709:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230627_132710:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230627_132711:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230627_132713:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230627_132715:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230627_132716:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230627_132718:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230627_132719:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230627_132720:cmsbot_crab_whitelist - 0
blacklist-check.sh 230627_132722:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230627_132723:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230627_132724:cmsbot_crab_voRole - 0
voGroup-check.sh 230627_132726:cmsbot_crab_voGroup - 0
scheddName-check.sh 230627_132727:cmsbot_crab_scheddName - 0
collector-check.sh 230627_132728:cmsbot_crab_collector - 0
extraJDL-check.sh 230627_132730:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
