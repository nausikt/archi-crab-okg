# dmwm/CRABServer issue #7752: #437: Test prod CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-07-12T20:45:41Z
Closed: 2023-07-12T22:10:07Z
URL: https://github.com/dmwm/CRABServer/issues/7752

## Opening post (cmsdmwmbot, 2023-07-12T20:45:41Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-07-12 22:45:40
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/437/)

## Comment (cmsdmwmbot, 2023-07-12T20:49:23Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230712_204715:cmsbot_crab_transferOutputs
230712_204720:cmsbot_crab_transferLogs
230712_204724:cmsbot_crab_activity
230712_204728:cmsbot_crab_inputFiles
230712_204732:cmsbot_crab_disableAutomaticOutputCollection
230712_204735:cmsbot_crab_outputFiles
230712_204738:cmsbot_crab_allowUndistributedCMSSW
230712_204742:cmsbot_crab_maxMemoryMB
230712_204746:cmsbot_crab_maxJobRuntimeMin
230712_204749:cmsbot_crab_numCores
230712_204752:cmsbot_crab_scriptExe
230712_204755:cmsbot_crab_scriptArgs
230712_204758:cmsbot_crab_sendPythonFolder
230712_204805:cmsbot_crab_sendExternalFolder
230712_204809:cmsbot_crab_inputDBS
230712_204812:cmsbot_crab_useParent
230712_204815:cmsbot_crab_secondaryInputDataset
230712_204818:cmsbot_crab_lumiMaskFile
230712_204821:cmsbot_crab_lumiMaskUrl
230712_204825:cmsbot_crab_outLFNDirBase
230712_204829:cmsbot_crab_runRange
230712_204832:cmsbot_crab_ignoreLocality
230712_204835:cmsbot_crab_userInputFiles
230712_204838:cmsbot_crab_whitelist
230712_204841:cmsbot_crab_blacklist
230712_204846:cmsbot_crab_ignoreGlobalBlacklist
230712_204849:cmsbot_crab_voRole
230712_204852:cmsbot_crab_voGroup
230712_204855:cmsbot_crab_scheddName
230712_204858:cmsbot_crab_collector
230712_204901:cmsbot_crab_extraJDL
```

Finished at: 2023-07-12 22:49:01
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/437/console)

## Comment (cmsdmwmbot, 2023-07-12T21:15:29Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-12 23:15:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/727/console

```
RETRY TESTS:
transferLogs-check.sh 230712_204720:cmsbot_crab_transferLogs - 2
outputFiles-check.sh 230712_204735:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 230712_204746:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskUrl-check.sh 230712_204821:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230712_204829:cmsbot_crab_runRange - 2
whitelist-check.sh 230712_204838:cmsbot_crab_whitelist - 2
blacklist-check.sh 230712_204841:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_204715:cmsbot_crab_transferOutputs - 0
activity-check.sh 230712_204724:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_204728:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_204732:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230712_204738:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_204742:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230712_204749:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_204752:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_204755:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_204758:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_204805:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_204809:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_204812:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_204815:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_204818:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230712_204825:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230712_204832:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_204835:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230712_204846:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_204849:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_204852:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_204855:cmsbot_crab_scheddName - 0
collector-check.sh 230712_204858:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_204901:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-12T21:41:58Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-07-12 23:41:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/729/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_204715:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_204720:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_204724:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_204728:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_204732:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_204735:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_204738:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_204742:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_204746:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230712_204749:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_204752:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_204755:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_204758:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_204805:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_204809:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_204812:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_204815:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_204818:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230712_204821:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230712_204825:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230712_204829:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230712_204832:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_204835:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230712_204838:cmsbot_crab_whitelist - 0
blacklist-check.sh 230712_204841:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230712_204846:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_204849:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_204852:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_204855:cmsbot_crab_scheddName - 0
collector-check.sh 230712_204858:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_204901:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
