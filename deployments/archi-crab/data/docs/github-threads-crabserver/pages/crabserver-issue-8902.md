# dmwm/CRABServer issue #8902: #931: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2025-01-29T21:37:45Z
Closed: 2025-01-29T23:40:28Z
URL: https://github.com/dmwm/CRABServer/issues/8902

## Opening post (cmsdmwmbot, 2025-01-29T21:37:45Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2025-01-29 22:37:42
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/931/)

## Comment (cmsdmwmbot, 2025-01-29T21:40:15Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250129_213820:cmsbot_crab_20250129_223817
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250129_213823:cmsbot_crab_transferOutputs
250129_213826:cmsbot_crab_transferLogs
250129_213829:cmsbot_crab_activity
250129_213832:cmsbot_crab_inputFiles
250129_213836:cmsbot_crab_disableAutomaticOutputCollection
250129_213839:cmsbot_crab_outputFiles
250129_213842:cmsbot_crab_allowUndistributedCMSSW
250129_213845:cmsbot_crab_maxMemoryMB
250129_213848:cmsbot_crab_maxJobRuntimeMin
250129_213851:cmsbot_crab_numCores
250129_213854:cmsbot_crab_scriptExe
250129_213857:cmsbot_crab_scriptArgs
250129_213900:cmsbot_crab_sendVenvFolder
250129_213903:cmsbot_crab_sendExternalFolder
250129_213906:cmsbot_crab_inputDBS
250129_213909:cmsbot_crab_useParent
250129_213912:cmsbot_crab_secondaryInputDataset
250129_213915:cmsbot_crab_lumiMaskFile
250129_213918:cmsbot_crab_lumiMaskUrl
250129_213922:cmsbot_crab_outLFNDirBase
250129_213925:cmsbot_crab_runRange
250129_213928:cmsbot_crab_ignoreLocality
250129_213932:cmsbot_crab_userInputFiles
250129_213935:cmsbot_crab_whitelist
250129_213938:cmsbot_crab_blacklist
250129_213941:cmsbot_crab_ignoreGlobalBlacklist
250129_213944:cmsbot_crab_voRole
250129_213947:cmsbot_crab_scheddName
250129_213950:cmsbot_crab_collector
250129_213953:cmsbot_crab_extraJDL
```

Finished at: 2025-01-29 22:39:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/931/console)

## Comment (cmsdmwmbot, 2025-01-29T22:03:11Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-01-29 23:03:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/598/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/598//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-01-29T22:03:43Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2025-01-29 23:03:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1271/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250129_213823:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250129_213826:cmsbot_crab_transferLogs - 0
activity-check.sh 250129_213829:cmsbot_crab_activity - 0
inputFiles-check.sh 250129_213832:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250129_213836:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250129_213839:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250129_213842:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 250129_213848:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 250129_213900:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250129_213903:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250129_213906:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 250129_213912:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250129_213915:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 250129_213928:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250129_213932:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 250129_213938:cmsbot_crab_blacklist - 0
voRole-check.sh 250129_213944:cmsbot_crab_voRole - 0
scheddName-check.sh 250129_213947:cmsbot_crab_scheddName - 0
collector-check.sh 250129_213950:cmsbot_crab_collector - 0
extraJDL-check.sh 250129_213953:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
maxMemoryMB-check.sh 250129_213845:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 250129_213851:cmsbot_crab_numCores - 2
scriptExe-check.sh 250129_213854:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 250129_213857:cmsbot_crab_scriptArgs - 2
useParent-check.sh 250129_213909:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 250129_213918:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 250129_213922:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 250129_213925:cmsbot_crab_runRange - 2
whitelist-check.sh 250129_213935:cmsbot_crab_whitelist - 2
ignoreGlobalBlacklist-check.sh 250129_213941:cmsbot_crab_ignoreGlobalBlacklist - 2
```

## Comment (cmsdmwmbot, 2025-01-29T22:27:57Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2025-01-29 23:27:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1273/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250129_213823:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250129_213826:cmsbot_crab_transferLogs - 0
activity-check.sh 250129_213829:cmsbot_crab_activity - 0
inputFiles-check.sh 250129_213832:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250129_213836:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250129_213839:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250129_213842:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 250129_213848:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250129_213851:cmsbot_crab_numCores - 0
scriptExe-check.sh 250129_213854:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250129_213857:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250129_213900:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250129_213903:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250129_213906:cmsbot_crab_inputDBS - 0
useParent-check.sh 250129_213909:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250129_213912:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250129_213915:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250129_213918:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250129_213922:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250129_213925:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250129_213928:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250129_213932:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250129_213935:cmsbot_crab_whitelist - 0
blacklist-check.sh 250129_213938:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250129_213941:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250129_213944:cmsbot_crab_voRole - 0
scheddName-check.sh 250129_213947:cmsbot_crab_scheddName - 0
collector-check.sh 250129_213950:cmsbot_crab_collector - 0
extraJDL-check.sh 250129_213953:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
maxMemoryMB-check.sh 250129_213845:cmsbot_crab_maxMemoryMB - 2
```

## Comment (cmsdmwmbot, 2025-01-29T22:52:01Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2025-01-29 23:52:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1275/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250129_213823:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250129_213826:cmsbot_crab_transferLogs - 0
activity-check.sh 250129_213829:cmsbot_crab_activity - 0
inputFiles-check.sh 250129_213832:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250129_213836:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250129_213839:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250129_213842:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250129_213845:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250129_213848:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250129_213851:cmsbot_crab_numCores - 0
scriptExe-check.sh 250129_213854:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250129_213857:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250129_213900:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250129_213903:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250129_213906:cmsbot_crab_inputDBS - 0
useParent-check.sh 250129_213909:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250129_213912:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250129_213915:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250129_213918:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250129_213922:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250129_213925:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250129_213928:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250129_213932:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250129_213935:cmsbot_crab_whitelist - 0
blacklist-check.sh 250129_213938:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250129_213941:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250129_213944:cmsbot_crab_voRole - 0
scheddName-check.sh 250129_213947:cmsbot_crab_scheddName - 0
collector-check.sh 250129_213950:cmsbot_crab_collector - 0
extraJDL-check.sh 250129_213953:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```

## Comment (belforte, 2025-01-29T23:40:10Z)

all OK
