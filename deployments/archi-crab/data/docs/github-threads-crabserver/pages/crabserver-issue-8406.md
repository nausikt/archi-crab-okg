# dmwm/CRABServer issue #8406: #779: Test GH CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-15T15:28:44Z
Closed: 2024-05-15T19:36:46Z
URL: https://github.com/dmwm/CRABServer/issues/8406

## Opening post (cmsdmwmbot, 2024-05-15T15:28:44Z)

**AIM: test my REST changes with CRABClient candidate https://github.com/dmwm/CRABClient/issues/5309**

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-05-15 17:28:44
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/779/)

## Comment (cmsdmwmbot, 2024-05-15T15:30:27Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240515_152906:cmsbot_crab_transferOutputs
240515_152908:cmsbot_crab_transferLogs
240515_152910:cmsbot_crab_activity
240515_152912:cmsbot_crab_inputFiles
240515_152914:cmsbot_crab_disableAutomaticOutputCollection
240515_152916:cmsbot_crab_outputFiles
240515_152918:cmsbot_crab_allowUndistributedCMSSW
240515_152920:cmsbot_crab_maxMemoryMB
240515_152922:cmsbot_crab_maxJobRuntimeMin
240515_152924:cmsbot_crab_numCores
240515_152926:cmsbot_crab_scriptExe
240515_152928:cmsbot_crab_scriptArgs
240515_152930:cmsbot_crab_sendVenvFolder
240515_152932:cmsbot_crab_sendExternalFolder
240515_152934:cmsbot_crab_inputDBS
240515_152935:cmsbot_crab_useParent
240515_152937:cmsbot_crab_secondaryInputDataset
240515_152939:cmsbot_crab_lumiMaskFile
240515_152941:cmsbot_crab_lumiMaskUrl
240515_152944:cmsbot_crab_outLFNDirBase
240515_152946:cmsbot_crab_runRange
240515_152948:cmsbot_crab_ignoreLocality
240515_152950:cmsbot_crab_userInputFiles
240515_152952:cmsbot_crab_whitelist
240515_152954:cmsbot_crab_blacklist
240515_152956:cmsbot_crab_ignoreGlobalBlacklist
240515_152958:cmsbot_crab_voRole
240515_153000:cmsbot_crab_voGroup
240515_153002:cmsbot_crab_scheddName
240515_153004:cmsbot_crab_collector
240515_153005:cmsbot_crab_extraJDL
```

Finished at: 2024-05-15 17:30:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/779/console)

## Comment (cmsdmwmbot, 2024-05-15T15:54:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-15 17:54:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1060/console

```
RETRY TESTS:
activity-check.sh 240515_152910:cmsbot_crab_activity - 2
scriptArgs-check.sh 240515_152928:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240515_152935:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240515_152937:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240515_152941:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240515_152944:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240515_152946:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240515_152948:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 240515_152950:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240515_152952:cmsbot_crab_whitelist - 2
blacklist-check.sh 240515_152954:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240515_152956:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240515_152906:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240515_152908:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240515_152912:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240515_152914:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240515_152916:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240515_152918:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240515_152920:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240515_152922:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240515_152924:cmsbot_crab_numCores - 0
scriptExe-check.sh 240515_152926:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240515_152930:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240515_152932:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240515_152934:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240515_152939:cmsbot_crab_lumiMaskFile - 0
voRole-check.sh 240515_152958:cmsbot_crab_voRole - 0
voGroup-check.sh 240515_153000:cmsbot_crab_voGroup - 0
scheddName-check.sh 240515_153002:cmsbot_crab_scheddName - 0
collector-check.sh 240515_153004:cmsbot_crab_collector - 0
extraJDL-check.sh 240515_153005:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-15T16:18:10Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-05-15 18:18:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1062/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240515_152941:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240515_152946:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240515_152950:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240515_152952:cmsbot_crab_whitelist - 2
blacklist-check.sh 240515_152954:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240515_152906:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240515_152908:cmsbot_crab_transferLogs - 0
activity-check.sh 240515_152910:cmsbot_crab_activity - 0
inputFiles-check.sh 240515_152912:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240515_152914:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240515_152916:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240515_152918:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240515_152920:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240515_152922:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240515_152924:cmsbot_crab_numCores - 0
scriptExe-check.sh 240515_152926:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240515_152928:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240515_152930:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240515_152932:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240515_152934:cmsbot_crab_inputDBS - 0
useParent-check.sh 240515_152935:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240515_152937:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240515_152939:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240515_152944:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240515_152948:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240515_152956:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240515_152958:cmsbot_crab_voRole - 0
voGroup-check.sh 240515_153000:cmsbot_crab_voGroup - 0
scheddName-check.sh 240515_153002:cmsbot_crab_scheddName - 0
collector-check.sh 240515_153004:cmsbot_crab_collector - 0
extraJDL-check.sh 240515_153005:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-15T16:42:06Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-05-15 18:42:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1064/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240515_152906:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240515_152908:cmsbot_crab_transferLogs - 0
activity-check.sh 240515_152910:cmsbot_crab_activity - 0
inputFiles-check.sh 240515_152912:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240515_152914:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240515_152916:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240515_152918:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240515_152920:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240515_152922:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240515_152924:cmsbot_crab_numCores - 0
scriptExe-check.sh 240515_152926:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240515_152928:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240515_152930:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240515_152932:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240515_152934:cmsbot_crab_inputDBS - 0
useParent-check.sh 240515_152935:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240515_152937:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240515_152939:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240515_152941:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240515_152944:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240515_152946:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240515_152948:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240515_152950:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240515_152952:cmsbot_crab_whitelist - 0
blacklist-check.sh 240515_152954:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240515_152956:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240515_152958:cmsbot_crab_voRole - 0
voGroup-check.sh 240515_153000:cmsbot_crab_voGroup - 0
scheddName-check.sh 240515_153002:cmsbot_crab_scheddName - 0
collector-check.sh 240515_153004:cmsbot_crab_collector - 0
extraJDL-check.sh 240515_153005:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
