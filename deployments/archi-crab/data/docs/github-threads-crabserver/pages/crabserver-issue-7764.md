# dmwm/CRABServer issue #7764: #442: Test dev CRABClient using test2 REST instance and CMSSW_12_5_0 CMSSW release

State: closed
Opened: 2023-07-16T10:26:22Z
Closed: 2023-07-16T14:10:53Z
URL: https://github.com/dmwm/CRABServer/issues/7764

## Opening post (cmsdmwmbot, 2023-07-16T10:26:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_5_0**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2023-07-16 12:26:22
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/442/)

## Comment (cmsdmwmbot, 2023-07-16T10:27:52Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230716_102643:cmsbot_crab_transferOutputs
230716_102644:cmsbot_crab_transferLogs
230716_102645:cmsbot_crab_activity
230716_102647:cmsbot_crab_inputFiles
230716_102648:cmsbot_crab_disableAutomaticOutputCollection
230716_102650:cmsbot_crab_outputFiles
230716_102651:cmsbot_crab_allowUndistributedCMSSW
230716_102652:cmsbot_crab_maxMemoryMB
230716_102654:cmsbot_crab_maxJobRuntimeMin
230716_102655:cmsbot_crab_numCores
230716_102656:cmsbot_crab_scriptExe
230716_102658:cmsbot_crab_scriptArgs
230716_102659:cmsbot_crab_sendPythonFolder
230716_102707:cmsbot_crab_sendExternalFolder
230716_102708:cmsbot_crab_inputDBS
230716_102710:cmsbot_crab_useParent
230716_102711:cmsbot_crab_secondaryInputDataset
230716_102712:cmsbot_crab_lumiMaskFile
230716_102714:cmsbot_crab_lumiMaskUrl
230716_102716:cmsbot_crab_outLFNDirBase
230716_102717:cmsbot_crab_runRange
230716_102718:cmsbot_crab_ignoreLocality
230716_102720:cmsbot_crab_userInputFiles
230716_102721:cmsbot_crab_whitelist
230716_102722:cmsbot_crab_blacklist
230716_102724:cmsbot_crab_ignoreGlobalBlacklist
230716_102725:cmsbot_crab_voRole
230716_102726:cmsbot_crab_voGroup
230716_102728:cmsbot_crab_scheddName
230716_102729:cmsbot_crab_collector
230716_102730:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230716_102641:cmsbot_crab_20230716_122640
```

Finished at: 2023-07-16 12:27:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/442/console)

## Comment (cmsdmwmbot, 2023-07-16T10:50:06Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-16 12:50:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/367/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/367//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-16T10:51:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-16 12:51:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/732/console

```
RETRY TESTS:
activity-check.sh 230716_102645:cmsbot_crab_activity - 2
scriptExe-check.sh 230716_102656:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230716_102658:cmsbot_crab_scriptArgs - 2
secondaryInputDataset-check.sh 230716_102711:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230716_102714:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230716_102717:cmsbot_crab_runRange - 2
whitelist-check.sh 230716_102721:cmsbot_crab_whitelist - 2
blacklist-check.sh 230716_102722:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230716_102724:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102644:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230716_102647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230716_102650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230716_102651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102654:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102655:cmsbot_crab_numCores - 0
sendPythonFolder-check.sh 230716_102659:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102707:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102708:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102710:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230716_102712:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230716_102716:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230716_102718:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230716_102720:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230716_102725:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102726:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102728:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102729:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102730:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-16T11:15:09Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-16 13:15:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/734/console

```
RETRY TESTS:
activity-check.sh 230716_102645:cmsbot_crab_activity - 2
secondaryInputDataset-check.sh 230716_102711:cmsbot_crab_secondaryInputDataset - 2
whitelist-check.sh 230716_102721:cmsbot_crab_whitelist - 2
blacklist-check.sh 230716_102722:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230716_102724:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102644:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230716_102647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230716_102650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230716_102651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102654:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102655:cmsbot_crab_numCores - 0
scriptExe-check.sh 230716_102656:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230716_102658:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230716_102659:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102707:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102708:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102710:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230716_102712:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230716_102714:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230716_102716:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230716_102717:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230716_102718:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230716_102720:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230716_102725:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102726:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102728:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102729:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102730:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-16T11:39:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-16 13:39:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/736/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 230716_102711:cmsbot_crab_secondaryInputDataset - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102644:cmsbot_crab_transferLogs - 0
activity-check.sh 230716_102645:cmsbot_crab_activity - 0
inputFiles-check.sh 230716_102647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230716_102650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230716_102651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102654:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102655:cmsbot_crab_numCores - 0
scriptExe-check.sh 230716_102656:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230716_102658:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230716_102659:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102707:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102708:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102710:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230716_102712:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230716_102714:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230716_102716:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230716_102717:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230716_102718:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230716_102720:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230716_102721:cmsbot_crab_whitelist - 0
blacklist-check.sh 230716_102722:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230716_102724:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230716_102725:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102726:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102728:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102729:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102730:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-16T12:03:33Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-16 14:03:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/738/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 230716_102711:cmsbot_crab_secondaryInputDataset - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102644:cmsbot_crab_transferLogs - 0
activity-check.sh 230716_102645:cmsbot_crab_activity - 0
inputFiles-check.sh 230716_102647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230716_102650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230716_102651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102654:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102655:cmsbot_crab_numCores - 0
scriptExe-check.sh 230716_102656:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230716_102658:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230716_102659:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102707:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102708:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102710:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230716_102712:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230716_102714:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230716_102716:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230716_102717:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230716_102718:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230716_102720:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230716_102721:cmsbot_crab_whitelist - 0
blacklist-check.sh 230716_102722:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230716_102724:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230716_102725:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102726:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102728:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102729:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102730:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-16T12:27:14Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 4. Test is done.
**Finished at:** 2023-07-16 14:27:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/740/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102644:cmsbot_crab_transferLogs - 0
activity-check.sh 230716_102645:cmsbot_crab_activity - 0
inputFiles-check.sh 230716_102647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230716_102650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230716_102651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102654:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102655:cmsbot_crab_numCores - 0
scriptExe-check.sh 230716_102656:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230716_102658:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230716_102659:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102707:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102708:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102710:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230716_102711:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230716_102712:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230716_102714:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230716_102716:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230716_102717:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230716_102718:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230716_102720:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230716_102721:cmsbot_crab_whitelist - 0
blacklist-check.sh 230716_102722:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230716_102724:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230716_102725:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102726:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102728:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102729:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102730:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-07-16T14:10:53Z)

all OK
