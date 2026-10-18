# dmwm/CRABServer issue #8132: #643: Test prod CRABClient using preprod REST instance and CMSSW_7_1_29 CMSSW release

State: closed
Opened: 2023-12-19T22:27:50Z
Closed: 2023-12-20T11:24:03Z
URL: https://github.com/dmwm/CRABServer/issues/8132

## Opening post (cmsdmwmbot, 2023-12-19T22:27:50Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_1_29**
- SCRAM_ARCH: **slc6_amd64_gcc481**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-19 23:27:48
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/643/)

## Comment (cmsdmwmbot, 2023-12-19T22:29:35Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231219_222803:cmsbot_crab_transferOutputs
231219_222804:cmsbot_crab_transferLogs
231219_222805:cmsbot_crab_activity
231219_222807:cmsbot_crab_inputFiles
231219_222808:cmsbot_crab_disableAutomaticOutputCollection
231219_222810:cmsbot_crab_outputFiles
231219_222811:cmsbot_crab_allowUndistributedCMSSW
231219_222812:cmsbot_crab_maxMemoryMB
231219_222813:cmsbot_crab_maxJobRuntimeMin
231219_222814:cmsbot_crab_numCores
231219_222815:cmsbot_crab_scriptExe
231219_222816:cmsbot_crab_scriptArgs
231219_222818:cmsbot_crab_sendVenvFolder
231219_222858:cmsbot_crab_sendExternalFolder
231219_222900:cmsbot_crab_inputDBS
231219_222900:cmsbot_crab_useParent
231219_222901:cmsbot_crab_secondaryInputDataset
231219_222902:cmsbot_crab_lumiMaskFile
231219_222904:cmsbot_crab_outLFNDirBase
231219_222905:cmsbot_crab_runRange
231219_222906:cmsbot_crab_ignoreLocality
231219_222907:cmsbot_crab_userInputFiles
231219_222908:cmsbot_crab_whitelist
231219_222908:cmsbot_crab_blacklist
231219_222909:cmsbot_crab_ignoreGlobalBlacklist
231219_222910:cmsbot_crab_voRole
231219_222911:cmsbot_crab_voGroup
231219_222912:cmsbot_crab_scheddName
231219_222913:cmsbot_crab_collector
231219_222914:cmsbot_crab_extraJDL
```

Finished at: 2023-12-19 23:29:14
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/643/console)

## Comment (cmsdmwmbot, 2023-12-19T22:50:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-19 23:50:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/816/console

```
RETRY TESTS:
transferLogs-check.sh 231219_222804:cmsbot_crab_transferLogs - 2
activity-check.sh 231219_222805:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 231219_222812:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 231219_222813:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 231219_222814:cmsbot_crab_numCores - 2
scriptExe-check.sh 231219_222815:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 231219_222816:cmsbot_crab_scriptArgs - 2
useParent-check.sh 231219_222900:cmsbot_crab_useParent - 2
blacklist-check.sh 231219_222908:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 231219_222909:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 231219_222910:cmsbot_crab_voRole - 2
voGroup-check.sh 231219_222911:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222803:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 231219_222807:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222808:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222810:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222811:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 231219_222818:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222858:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222900:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 231219_222901:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222902:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222904:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222905:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222906:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222907:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222908:cmsbot_crab_whitelist - 0
scheddName-check.sh 231219_222912:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222913:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:11:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-12-20 00:11:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/821/console

```
RETRY TESTS:
transferLogs-check.sh 231219_222804:cmsbot_crab_transferLogs - 2
activity-check.sh 231219_222805:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 231219_222812:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 231219_222813:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 231219_222814:cmsbot_crab_numCores - 2
scriptExe-check.sh 231219_222815:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 231219_222816:cmsbot_crab_scriptArgs - 2
blacklist-check.sh 231219_222908:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 231219_222909:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 231219_222910:cmsbot_crab_voRole - 2
voGroup-check.sh 231219_222911:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222803:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 231219_222807:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222808:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222810:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222811:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 231219_222818:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222858:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222900:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222900:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222901:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222902:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222904:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222905:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222906:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222907:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222908:cmsbot_crab_whitelist - 0
scheddName-check.sh 231219_222912:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222913:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:32:53Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-12-20 00:32:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/824/console

```
RETRY TESTS:
numCores-check.sh 231219_222814:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222803:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222804:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222805:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222807:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222808:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222810:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222811:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222812:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222813:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 231219_222815:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222816:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222818:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222858:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222900:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222900:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222901:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222902:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222904:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222905:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222906:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222907:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222908:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_222908:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_222909:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222910:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222911:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222912:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222913:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-19T23:53:49Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-12-20 00:53:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/826/console

```
RETRY TESTS:
numCores-check.sh 231219_222814:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222803:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222804:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222805:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222807:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222808:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222810:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222811:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222812:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222813:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 231219_222815:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222816:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222818:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222858:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222900:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222900:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222901:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222902:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222904:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222905:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222906:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222907:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222908:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_222908:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_222909:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222910:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222911:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222912:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222913:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-20T00:15:02Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 4. Test is done.
**Finished at:** 2023-12-20 01:15:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/828/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231219_222803:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231219_222804:cmsbot_crab_transferLogs - 0
activity-check.sh 231219_222805:cmsbot_crab_activity - 0
inputFiles-check.sh 231219_222807:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231219_222808:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231219_222810:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231219_222811:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231219_222812:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231219_222813:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231219_222814:cmsbot_crab_numCores - 0
scriptExe-check.sh 231219_222815:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231219_222816:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231219_222818:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231219_222858:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231219_222900:cmsbot_crab_inputDBS - 0
useParent-check.sh 231219_222900:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231219_222901:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231219_222902:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231219_222904:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231219_222905:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231219_222906:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231219_222907:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231219_222908:cmsbot_crab_whitelist - 0
blacklist-check.sh 231219_222908:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231219_222909:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231219_222910:cmsbot_crab_voRole - 0
voGroup-check.sh 231219_222911:cmsbot_crab_voGroup - 0
scheddName-check.sh 231219_222912:cmsbot_crab_scheddName - 0
collector-check.sh 231219_222913:cmsbot_crab_collector - 0
extraJDL-check.sh 231219_222914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (mapellidario, 2023-12-20T11:24:03Z)

looks good to me
