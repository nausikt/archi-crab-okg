# dmwm/CRABServer issue #8134: #645: Test dev CRABClient using preprod REST instance and CMSSW_9_4_21 CMSSW release

State: closed
Opened: 2023-12-20T13:06:27Z
Closed: 2023-12-20T17:04:45Z
URL: https://github.com/dmwm/CRABServer/issues/8134

## Opening post (cmsdmwmbot, 2023-12-20T13:06:27Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_9_4_21**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-20 14:06:26
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/645/)

## Comment (cmsdmwmbot, 2023-12-20T13:07:40Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231220_130642:cmsbot_crab_transferOutputs
231220_130643:cmsbot_crab_transferLogs
231220_130644:cmsbot_crab_activity
231220_130645:cmsbot_crab_inputFiles
231220_130646:cmsbot_crab_disableAutomaticOutputCollection
231220_130647:cmsbot_crab_outputFiles
231220_130648:cmsbot_crab_allowUndistributedCMSSW
231220_130649:cmsbot_crab_maxMemoryMB
231220_130651:cmsbot_crab_maxJobRuntimeMin
231220_130652:cmsbot_crab_numCores
231220_130653:cmsbot_crab_scriptExe
231220_130654:cmsbot_crab_scriptArgs
231220_130655:cmsbot_crab_sendVenvFolder
231220_130659:cmsbot_crab_sendExternalFolder
231220_130700:cmsbot_crab_inputDBS
231220_130701:cmsbot_crab_useParent
231220_130702:cmsbot_crab_secondaryInputDataset
231220_130703:cmsbot_crab_lumiMaskFile
231220_130704:cmsbot_crab_lumiMaskUrl
231220_130707:cmsbot_crab_outLFNDirBase
231220_130708:cmsbot_crab_runRange
231220_130709:cmsbot_crab_ignoreLocality
231220_130710:cmsbot_crab_userInputFiles
231220_130711:cmsbot_crab_whitelist
231220_130712:cmsbot_crab_blacklist
231220_130713:cmsbot_crab_ignoreGlobalBlacklist
231220_130714:cmsbot_crab_voRole
231220_130715:cmsbot_crab_voGroup
231220_130716:cmsbot_crab_scheddName
231220_130717:cmsbot_crab_collector
231220_130718:cmsbot_crab_extraJDL
```

Finished at: 2023-12-20 14:07:18
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/645/console)

## Comment (cmsdmwmbot, 2023-12-20T13:29:35Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-20 14:29:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/829/console

```
RETRY TESTS:
transferLogs-check.sh 231220_130643:cmsbot_crab_transferLogs - 2
activity-check.sh 231220_130644:cmsbot_crab_activity - 2
scriptArgs-check.sh 231220_130654:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 231220_130704:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 231220_130707:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 231220_130708:cmsbot_crab_runRange - 2
whitelist-check.sh 231220_130711:cmsbot_crab_whitelist - 2
blacklist-check.sh 231220_130712:cmsbot_crab_blacklist - 2
voRole-check.sh 231220_130714:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_130642:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 231220_130645:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_130646:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_130647:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_130648:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231220_130649:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231220_130651:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231220_130652:cmsbot_crab_numCores - 0
scriptExe-check.sh 231220_130653:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 231220_130655:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_130659:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_130700:cmsbot_crab_inputDBS - 0
useParent-check.sh 231220_130701:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231220_130702:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_130703:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 231220_130709:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_130710:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231220_130713:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 231220_130715:cmsbot_crab_voGroup - 0
scheddName-check.sh 231220_130716:cmsbot_crab_scheddName - 0
collector-check.sh 231220_130717:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_130718:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-20T13:52:00Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-12-20 14:51:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/830/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_130642:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231220_130643:cmsbot_crab_transferLogs - 0
activity-check.sh 231220_130644:cmsbot_crab_activity - 0
inputFiles-check.sh 231220_130645:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_130646:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_130647:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_130648:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231220_130649:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231220_130651:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231220_130652:cmsbot_crab_numCores - 0
scriptExe-check.sh 231220_130653:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231220_130654:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231220_130655:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_130659:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_130700:cmsbot_crab_inputDBS - 0
useParent-check.sh 231220_130701:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231220_130702:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_130703:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231220_130704:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231220_130707:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231220_130708:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231220_130709:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_130710:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231220_130711:cmsbot_crab_whitelist - 0
blacklist-check.sh 231220_130712:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231220_130713:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231220_130714:cmsbot_crab_voRole - 0
voGroup-check.sh 231220_130715:cmsbot_crab_voGroup - 0
scheddName-check.sh 231220_130716:cmsbot_crab_scheddName - 0
collector-check.sh 231220_130717:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_130718:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
