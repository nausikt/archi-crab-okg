# dmwm/CRABServer issue #8201: #685: Test GH CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-30T20:17:16Z
Closed: 2024-01-31T13:58:08Z
URL: https://github.com/dmwm/CRABServer/issues/8201

## Opening post (cmsdmwmbot, 2024-01-30T20:17:16Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-01-30 21:17:15
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/685/)

## Comment (cmsdmwmbot, 2024-01-30T20:19:43Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240130_201740:cmsbot_crab_transferOutputs
240130_201742:cmsbot_crab_transferLogs
240130_201744:cmsbot_crab_activity
240130_201746:cmsbot_crab_inputFiles
240130_201748:cmsbot_crab_disableAutomaticOutputCollection
240130_201749:cmsbot_crab_outputFiles
240130_201751:cmsbot_crab_allowUndistributedCMSSW
240130_201753:cmsbot_crab_maxMemoryMB
240130_201755:cmsbot_crab_maxJobRuntimeMin
240130_201757:cmsbot_crab_numCores
240130_201758:cmsbot_crab_scriptExe
240130_201800:cmsbot_crab_scriptArgs
240130_201802:cmsbot_crab_sendVenvFolder
240130_201848:cmsbot_crab_sendExternalFolder
240130_201850:cmsbot_crab_inputDBS
240130_201852:cmsbot_crab_useParent
240130_201854:cmsbot_crab_secondaryInputDataset
240130_201856:cmsbot_crab_lumiMaskFile
240130_201858:cmsbot_crab_lumiMaskUrl
240130_201901:cmsbot_crab_outLFNDirBase
240130_201903:cmsbot_crab_runRange
240130_201904:cmsbot_crab_ignoreLocality
240130_201906:cmsbot_crab_userInputFiles
240130_201908:cmsbot_crab_whitelist
240130_201910:cmsbot_crab_blacklist
240130_201912:cmsbot_crab_ignoreGlobalBlacklist
240130_201914:cmsbot_crab_voRole
240130_201916:cmsbot_crab_voGroup
240130_201917:cmsbot_crab_scheddName
240130_201919:cmsbot_crab_collector
240130_201921:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240130_201738:cmsbot_crab_20240130_211737
```

Finished at: 2024-01-30 21:19:22
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/685/console)

## Comment (cmsdmwmbot, 2024-01-30T20:42:38Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-30 21:42:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/499/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/499//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-30T20:43:01Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-30 21:43:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/894/console

```
RETRY TESTS:
outputFiles-check.sh 240130_201749:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240130_201753:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240130_201755:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240130_201757:cmsbot_crab_numCores - 2
scriptExe-check.sh 240130_201758:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240130_201800:cmsbot_crab_scriptArgs - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_201740:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_201746:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_201748:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240130_201751:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_201802:cmsbot_crab_sendVenvFolder - 0
scheddName-check.sh 240130_201917:cmsbot_crab_scheddName - 0
collector-check.sh 240130_201919:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240130_201742:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_201744:cmsbot_crab_activity - 1
sendExternalFolder-check.sh 240130_201848:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240130_201850:cmsbot_crab_inputDBS - 1
useParent-check.sh 240130_201852:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240130_201854:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240130_201856:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_201858:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_201901:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_201903:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_201904:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_201906:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_201908:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_201910:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_201912:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_201914:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_201916:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_201921:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-01-30T21:06:52Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-01-30 22:06:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/896/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_201740:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_201746:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_201748:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240130_201751:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_201802:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240130_201848:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240130_201850:cmsbot_crab_inputDBS - 0
scheddName-check.sh 240130_201917:cmsbot_crab_scheddName - 0
collector-check.sh 240130_201919:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240130_201742:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_201744:cmsbot_crab_activity - 1
outputFiles-check.sh 240130_201749:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240130_201753:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_201755:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_201757:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_201758:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_201800:cmsbot_crab_scriptArgs - 1
useParent-check.sh 240130_201852:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240130_201854:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240130_201856:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_201858:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_201901:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_201903:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_201904:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_201906:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_201908:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_201910:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_201912:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_201914:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_201916:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_201921:cmsbot_crab_extraJDL - 1
```
