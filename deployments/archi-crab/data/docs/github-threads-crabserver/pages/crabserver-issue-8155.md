# dmwm/CRABServer issue #8155: #662: Test dev CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2024-01-11T19:47:00Z
Closed: 2024-01-11T20:49:58Z
URL: https://github.com/dmwm/CRABServer/issues/8155

## Opening post (cmsdmwmbot, 2024-01-11T19:47:00Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 20:47:00
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/662/)

## Comment (cmsdmwmbot, 2024-01-11T19:48:15Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_194721:cmsbot_crab_transferOutputs
240111_194722:cmsbot_crab_transferLogs
240111_194723:cmsbot_crab_activity
240111_194724:cmsbot_crab_inputFiles
240111_194724:cmsbot_crab_disableAutomaticOutputCollection
240111_194725:cmsbot_crab_outputFiles
240111_194726:cmsbot_crab_allowUndistributedCMSSW
240111_194727:cmsbot_crab_maxMemoryMB
240111_194728:cmsbot_crab_maxJobRuntimeMin
240111_194729:cmsbot_crab_numCores
240111_194730:cmsbot_crab_scriptExe
240111_194730:cmsbot_crab_scriptArgs
240111_194732:cmsbot_crab_sendVenvFolder
240111_194737:cmsbot_crab_sendExternalFolder
240111_194738:cmsbot_crab_inputDBS
240111_194739:cmsbot_crab_useParent
240111_194740:cmsbot_crab_secondaryInputDataset
240111_194741:cmsbot_crab_lumiMaskFile
240111_194742:cmsbot_crab_lumiMaskUrl
240111_194744:cmsbot_crab_outLFNDirBase
240111_194745:cmsbot_crab_runRange
240111_194745:cmsbot_crab_ignoreLocality
240111_194746:cmsbot_crab_userInputFiles
240111_194747:cmsbot_crab_whitelist
240111_194748:cmsbot_crab_blacklist
240111_194749:cmsbot_crab_ignoreGlobalBlacklist
240111_194750:cmsbot_crab_voRole
240111_194750:cmsbot_crab_voGroup
240111_194751:cmsbot_crab_scheddName
240111_194752:cmsbot_crab_collector
240111_194753:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_194719:cmsbot_crab_20240111_204718
```

Finished at: 2024-01-11 20:47:54
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/662/console)

## Comment (cmsdmwmbot, 2024-01-11T20:10:49Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 21:10:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/483/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/483//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-11T20:13:27Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 21:13:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/879/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240111_194742:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240111_194745:cmsbot_crab_runRange - 2
whitelist-check.sh 240111_194747:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_194748:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_194721:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_194722:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_194723:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_194724:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_194724:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_194725:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_194726:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_194727:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_194728:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_194729:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_194730:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_194730:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_194732:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_194737:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_194738:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_194739:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_194740:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_194741:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_194744:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240111_194745:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_194746:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240111_194749:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_194750:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_194750:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_194751:cmsbot_crab_scheddName - 0
collector-check.sh 240111_194752:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_194753:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T20:37:33Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-01-11 21:37:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/881/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_194721:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_194722:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_194723:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_194724:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_194724:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_194725:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_194726:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_194727:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_194728:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_194729:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_194730:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_194730:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_194732:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_194737:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_194738:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_194739:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_194740:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_194741:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_194742:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_194744:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_194745:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_194745:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_194746:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_194747:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_194748:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_194749:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_194750:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_194750:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_194751:cmsbot_crab_scheddName - 0
collector-check.sh 240111_194752:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_194753:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-11T20:49:58Z)

all ok
