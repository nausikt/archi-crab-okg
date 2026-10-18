# dmwm/CRABServer issue #7706: #416: Test dev CRABClient using test2 REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-06-30T15:55:33Z
Closed: 2023-06-30T17:19:17Z
URL: https://github.com/dmwm/CRABServer/issues/7706

## Opening post (cmsdmwmbot, 2023-06-30T15:55:33Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-06-30 17:55:33
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/416/)

## Comment (cmsdmwmbot, 2023-06-30T15:58:51Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230630_155659:cmsbot_crab_transferOutputs
230630_155703:cmsbot_crab_transferLogs
230630_155705:cmsbot_crab_activity
230630_155708:cmsbot_crab_inputFiles
230630_155711:cmsbot_crab_disableAutomaticOutputCollection
230630_155713:cmsbot_crab_outputFiles
230630_155716:cmsbot_crab_allowUndistributedCMSSW
230630_155719:cmsbot_crab_maxMemoryMB
230630_155721:cmsbot_crab_maxJobRuntimeMin
230630_155724:cmsbot_crab_numCores
230630_155727:cmsbot_crab_scriptExe
230630_155730:cmsbot_crab_scriptArgs
230630_155733:cmsbot_crab_sendPythonFolder
230630_155742:cmsbot_crab_sendExternalFolder
230630_155745:cmsbot_crab_inputDBS
230630_155748:cmsbot_crab_useParent
230630_155750:cmsbot_crab_secondaryInputDataset
230630_155753:cmsbot_crab_lumiMaskFile
230630_155756:cmsbot_crab_lumiMaskUrl
230630_155759:cmsbot_crab_outLFNDirBase
230630_155802:cmsbot_crab_runRange
230630_155805:cmsbot_crab_ignoreLocality
230630_155808:cmsbot_crab_userInputFiles
230630_155811:cmsbot_crab_whitelist
230630_155813:cmsbot_crab_blacklist
230630_155816:cmsbot_crab_ignoreGlobalBlacklist
230630_155818:cmsbot_crab_voRole
230630_155821:cmsbot_crab_voGroup
230630_155824:cmsbot_crab_scheddName
230630_155827:cmsbot_crab_collector
230630_155829:cmsbot_crab_extraJDL
```

Finished at: 2023-06-30 17:58:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/416/console)

## Comment (cmsdmwmbot, 2023-06-30T16:25:53Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-30 18:25:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/660/console

```
RETRY TESTS:
transferLogs-check.sh 230630_155703:cmsbot_crab_transferLogs - 2
activity-check.sh 230630_155705:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 230630_155711:cmsbot_crab_disableAutomaticOutputCollection - 2
useParent-check.sh 230630_155748:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230630_155750:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 230630_155753:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230630_155756:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230630_155802:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230630_155808:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230630_155811:cmsbot_crab_whitelist - 2
blacklist-check.sh 230630_155813:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_155659:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230630_155708:cmsbot_crab_inputFiles - 0
outLFNDirBase-check.sh 230630_155759:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230630_155805:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230630_155816:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230630_155818:cmsbot_crab_voRole - 0
voGroup-check.sh 230630_155821:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_155824:cmsbot_crab_scheddName - 0
collector-check.sh 230630_155827:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_155829:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 230630_155713:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 230630_155716:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 230630_155719:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230630_155721:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230630_155724:cmsbot_crab_numCores - 1
scriptExe-check.sh 230630_155727:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230630_155730:cmsbot_crab_scriptArgs - 1
sendPythonFolder-check.sh 230630_155733:cmsbot_crab_sendPythonFolder - 1
sendExternalFolder-check.sh 230630_155742:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 230630_155745:cmsbot_crab_inputDBS - 1
```

## Comment (cmsdmwmbot, 2023-06-30T16:52:38Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-30 18:52:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/662/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230630_155719:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230630_155721:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230630_155724:cmsbot_crab_numCores - 2
scriptArgs-check.sh 230630_155730:cmsbot_crab_scriptArgs - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_155659:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_155703:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_155705:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_155708:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_155711:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_155713:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_155716:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 230630_155727:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230630_155733:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_155742:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_155745:cmsbot_crab_inputDBS - 0
useParent-check.sh 230630_155748:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230630_155750:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230630_155753:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230630_155756:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230630_155759:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230630_155802:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230630_155805:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_155808:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230630_155811:cmsbot_crab_whitelist - 0
blacklist-check.sh 230630_155813:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230630_155816:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230630_155818:cmsbot_crab_voRole - 0
voGroup-check.sh 230630_155821:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_155824:cmsbot_crab_scheddName - 0
collector-check.sh 230630_155827:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_155829:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-30T17:18:47Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-06-30 19:18:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/664/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_155659:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_155703:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_155705:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_155708:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_155711:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_155713:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_155716:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_155719:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230630_155721:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230630_155724:cmsbot_crab_numCores - 0
scriptExe-check.sh 230630_155727:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230630_155730:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_155733:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_155742:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_155745:cmsbot_crab_inputDBS - 0
useParent-check.sh 230630_155748:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230630_155750:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230630_155753:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230630_155756:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230630_155759:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230630_155802:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230630_155805:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_155808:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230630_155811:cmsbot_crab_whitelist - 0
blacklist-check.sh 230630_155813:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230630_155816:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230630_155818:cmsbot_crab_voRole - 0
voGroup-check.sh 230630_155821:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_155824:cmsbot_crab_scheddName - 0
collector-check.sh 230630_155827:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_155829:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-06-30T17:19:17Z)

ok
