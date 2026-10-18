# dmwm/CRABServer issue #8592: #821: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-06T22:48:21Z
Closed: 2024-08-07T01:17:58Z
URL: https://github.com/dmwm/CRABServer/issues/8592

## Opening post (cmsdmwmbot, 2024-08-06T22:48:21Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-08-07 00:48:20
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/821/)

## Comment (cmsdmwmbot, 2024-08-06T22:50:07Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240806_224842:cmsbot_crab_transferOutputs
240806_224845:cmsbot_crab_transferLogs
240806_224847:cmsbot_crab_activity
240806_224849:cmsbot_crab_inputFiles
240806_224851:cmsbot_crab_disableAutomaticOutputCollection
240806_224853:cmsbot_crab_outputFiles
240806_224855:cmsbot_crab_allowUndistributedCMSSW
240806_224857:cmsbot_crab_maxMemoryMB
240806_224859:cmsbot_crab_maxJobRuntimeMin
240806_224901:cmsbot_crab_numCores
240806_224903:cmsbot_crab_scriptExe
240806_224905:cmsbot_crab_scriptArgs
240806_224907:cmsbot_crab_sendVenvFolder
240806_224909:cmsbot_crab_sendExternalFolder
240806_224911:cmsbot_crab_inputDBS
240806_224913:cmsbot_crab_useParent
240806_224915:cmsbot_crab_secondaryInputDataset
240806_224918:cmsbot_crab_lumiMaskFile
240806_224920:cmsbot_crab_lumiMaskUrl
240806_224923:cmsbot_crab_outLFNDirBase
240806_224925:cmsbot_crab_runRange
240806_224927:cmsbot_crab_ignoreLocality
240806_224929:cmsbot_crab_userInputFiles
240806_224931:cmsbot_crab_whitelist
240806_224933:cmsbot_crab_blacklist
240806_224935:cmsbot_crab_ignoreGlobalBlacklist
240806_224937:cmsbot_crab_voRole
240806_224939:cmsbot_crab_voGroup
240806_224941:cmsbot_crab_scheddName
240806_224943:cmsbot_crab_collector
240806_224945:cmsbot_crab_extraJDL
```

Finished at: 2024-08-07 00:49:46
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/821/console)

## Comment (cmsdmwmbot, 2024-08-06T23:13:19Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-07 01:13:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1145/console

```
RETRY TESTS:
transferLogs-check.sh 240806_224845:cmsbot_crab_transferLogs - 2
activity-check.sh 240806_224847:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 240806_224857:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240806_224859:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240806_224901:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240806_224905:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240806_224913:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240806_224915:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240806_224918:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240806_224920:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240806_224923:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240806_224925:cmsbot_crab_runRange - 2
whitelist-check.sh 240806_224931:cmsbot_crab_whitelist - 2
blacklist-check.sh 240806_224933:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240806_224935:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240806_224937:cmsbot_crab_voRole - 2
voGroup-check.sh 240806_224939:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240806_224945:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240806_224842:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240806_224849:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240806_224851:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240806_224853:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240806_224855:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 240806_224903:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240806_224907:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240806_224909:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240806_224911:cmsbot_crab_inputDBS - 0
ignoreLocality-check.sh 240806_224927:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240806_224929:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240806_224941:cmsbot_crab_scheddName - 0

FAILED TESTS:
collector-check.sh 240806_224943:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-08-06T23:36:53Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-08-07 01:36:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1146/console

```
RETRY TESTS:
transferLogs-check.sh 240806_224845:cmsbot_crab_transferLogs - 2
activity-check.sh 240806_224847:cmsbot_crab_activity - 2
maxJobRuntimeMin-check.sh 240806_224859:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240806_224901:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240806_224905:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240806_224913:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240806_224915:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240806_224918:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240806_224920:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240806_224923:cmsbot_crab_outLFNDirBase - 2
whitelist-check.sh 240806_224931:cmsbot_crab_whitelist - 2
blacklist-check.sh 240806_224933:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240806_224935:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240806_224937:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240806_224842:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240806_224849:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240806_224851:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240806_224853:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240806_224855:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240806_224857:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240806_224903:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240806_224907:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240806_224909:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240806_224911:cmsbot_crab_inputDBS - 0
runRange-check.sh 240806_224925:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240806_224927:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240806_224929:cmsbot_crab_userInputFiles - 0
voGroup-check.sh 240806_224939:cmsbot_crab_voGroup - 0
scheddName-check.sh 240806_224941:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240806_224945:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240806_224943:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-08-07T00:00:38Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-08-07 02:00:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1147/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240806_224842:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240806_224845:cmsbot_crab_transferLogs - 0
activity-check.sh 240806_224847:cmsbot_crab_activity - 0
inputFiles-check.sh 240806_224849:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240806_224851:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240806_224853:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240806_224855:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240806_224857:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240806_224859:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240806_224901:cmsbot_crab_numCores - 0
scriptExe-check.sh 240806_224903:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240806_224905:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240806_224907:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240806_224909:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240806_224911:cmsbot_crab_inputDBS - 0
useParent-check.sh 240806_224913:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240806_224915:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240806_224918:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240806_224920:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240806_224923:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240806_224925:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240806_224927:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240806_224929:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240806_224931:cmsbot_crab_whitelist - 0
blacklist-check.sh 240806_224933:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240806_224935:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240806_224937:cmsbot_crab_voRole - 0
voGroup-check.sh 240806_224939:cmsbot_crab_voGroup - 0
scheddName-check.sh 240806_224941:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240806_224945:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240806_224943:cmsbot_crab_collector - 1
```

## Comment (belforte, 2024-08-07T01:17:42Z)

collector test failure is expected since I forced tests to run on vocms059
