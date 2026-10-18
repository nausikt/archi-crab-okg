# dmwm/CRABServer issue #8606: #827: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-09T20:48:22Z
Closed: 2024-08-09T23:13:36Z
URL: https://github.com/dmwm/CRABServer/issues/8606

## Opening post (cmsdmwmbot, 2024-08-09T20:48:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-08-09 22:48:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/827/)

## Comment (cmsdmwmbot, 2024-08-09T20:50:06Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240809_204840:cmsbot_crab_transferOutputs
240809_204842:cmsbot_crab_transferLogs
240809_204846:cmsbot_crab_activity
240809_204848:cmsbot_crab_inputFiles
240809_204850:cmsbot_crab_disableAutomaticOutputCollection
240809_204852:cmsbot_crab_outputFiles
240809_204854:cmsbot_crab_allowUndistributedCMSSW
240809_204856:cmsbot_crab_maxMemoryMB
240809_204858:cmsbot_crab_maxJobRuntimeMin
240809_204900:cmsbot_crab_numCores
240809_204902:cmsbot_crab_scriptExe
240809_204904:cmsbot_crab_scriptArgs
240809_204907:cmsbot_crab_sendVenvFolder
240809_204909:cmsbot_crab_sendExternalFolder
240809_204911:cmsbot_crab_inputDBS
240809_204913:cmsbot_crab_useParent
240809_204915:cmsbot_crab_secondaryInputDataset
240809_204917:cmsbot_crab_lumiMaskFile
240809_204919:cmsbot_crab_lumiMaskUrl
240809_204922:cmsbot_crab_outLFNDirBase
240809_204924:cmsbot_crab_runRange
240809_204926:cmsbot_crab_ignoreLocality
240809_204928:cmsbot_crab_userInputFiles
240809_204930:cmsbot_crab_whitelist
240809_204932:cmsbot_crab_blacklist
240809_204934:cmsbot_crab_ignoreGlobalBlacklist
240809_204936:cmsbot_crab_voRole
240809_204938:cmsbot_crab_voGroup
240809_204940:cmsbot_crab_scheddName
240809_204942:cmsbot_crab_collector
240809_204944:cmsbot_crab_extraJDL
```

Finished at: 2024-08-09 22:49:45
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/827/console)

## Comment (cmsdmwmbot, 2024-08-09T21:14:10Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-09 23:14:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1156/console

```
RETRY TESTS:
transferOutputs-check.sh 240809_204840:cmsbot_crab_transferOutputs - 2
outputFiles-check.sh 240809_204852:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240809_204858:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240809_204900:cmsbot_crab_numCores - 2
scriptExe-check.sh 240809_204902:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240809_204904:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240809_204913:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240809_204915:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240809_204917:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240809_204919:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240809_204922:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240809_204924:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240809_204926:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 240809_204928:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240809_204930:cmsbot_crab_whitelist - 2
blacklist-check.sh 240809_204932:cmsbot_crab_blacklist - 2
voGroup-check.sh 240809_204938:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferLogs-check.sh 240809_204842:cmsbot_crab_transferLogs - 0
activity-check.sh 240809_204846:cmsbot_crab_activity - 0
inputFiles-check.sh 240809_204848:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240809_204850:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240809_204854:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240809_204856:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240809_204907:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240809_204909:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240809_204911:cmsbot_crab_inputDBS - 0
ignoreGlobalBlacklist-check.sh 240809_204934:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240809_204936:cmsbot_crab_voRole - 0
scheddName-check.sh 240809_204940:cmsbot_crab_scheddName - 0
collector-check.sh 240809_204942:cmsbot_crab_collector - 0
extraJDL-check.sh 240809_204944:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-09T21:38:36Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-08-09 23:38:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1157/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240809_204858:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240809_204900:cmsbot_crab_numCores - 2
scriptExe-check.sh 240809_204902:cmsbot_crab_scriptExe - 2
useParent-check.sh 240809_204913:cmsbot_crab_useParent - 2
lumiMaskFile-check.sh 240809_204917:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240809_204919:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240809_204922:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240809_204924:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240809_204928:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240809_204930:cmsbot_crab_whitelist - 2
blacklist-check.sh 240809_204932:cmsbot_crab_blacklist - 2
voGroup-check.sh 240809_204938:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240809_204840:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240809_204842:cmsbot_crab_transferLogs - 0
activity-check.sh 240809_204846:cmsbot_crab_activity - 0
inputFiles-check.sh 240809_204848:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240809_204850:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240809_204852:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240809_204854:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240809_204856:cmsbot_crab_maxMemoryMB - 0
scriptArgs-check.sh 240809_204904:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240809_204907:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240809_204909:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240809_204911:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240809_204915:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240809_204926:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240809_204934:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240809_204936:cmsbot_crab_voRole - 0
scheddName-check.sh 240809_204940:cmsbot_crab_scheddName - 0
collector-check.sh 240809_204942:cmsbot_crab_collector - 0
extraJDL-check.sh 240809_204944:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-09T22:04:06Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-08-10 00:04:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1158/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240809_204840:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240809_204842:cmsbot_crab_transferLogs - 0
activity-check.sh 240809_204846:cmsbot_crab_activity - 0
inputFiles-check.sh 240809_204848:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240809_204850:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240809_204852:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240809_204854:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240809_204856:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240809_204858:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240809_204900:cmsbot_crab_numCores - 0
scriptExe-check.sh 240809_204902:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240809_204904:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240809_204907:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240809_204909:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240809_204911:cmsbot_crab_inputDBS - 0
useParent-check.sh 240809_204913:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240809_204915:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240809_204917:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240809_204919:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240809_204922:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240809_204924:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240809_204926:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240809_204928:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240809_204930:cmsbot_crab_whitelist - 0
blacklist-check.sh 240809_204932:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240809_204934:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240809_204936:cmsbot_crab_voRole - 0
voGroup-check.sh 240809_204938:cmsbot_crab_voGroup - 0
scheddName-check.sh 240809_204940:cmsbot_crab_scheddName - 0
collector-check.sh 240809_204942:cmsbot_crab_collector - 0
extraJDL-check.sh 240809_204944:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-08-09T23:13:36Z)

OK
