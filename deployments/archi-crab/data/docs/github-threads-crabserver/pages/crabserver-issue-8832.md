# dmwm/CRABServer issue #8832: #898: Test GH CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2024-11-25T22:37:17Z
Closed: 2024-11-26T08:42:17Z
URL: https://github.com/dmwm/CRABServer/issues/8832

## Opening post (cmsdmwmbot, 2024-11-25T22:37:17Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**
- CRABServer_tag: **v3.241125**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-11-25 23:37:16
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/898/)

## Comment (cmsdmwmbot, 2024-11-25T22:38:35Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241125_223749:cmsbot_crab_transferOutputs
241125_223750:cmsbot_crab_transferLogs
241125_223750:cmsbot_crab_activity
241125_223752:cmsbot_crab_inputFiles
241125_223752:cmsbot_crab_disableAutomaticOutputCollection
241125_223754:cmsbot_crab_outputFiles
241125_223755:cmsbot_crab_allowUndistributedCMSSW
241125_223755:cmsbot_crab_maxMemoryMB
241125_223756:cmsbot_crab_maxJobRuntimeMin
241125_223757:cmsbot_crab_numCores
241125_223758:cmsbot_crab_scriptExe
241125_223759:cmsbot_crab_scriptArgs
241125_223802:cmsbot_crab_sendVenvFolder
241125_223803:cmsbot_crab_sendExternalFolder
241125_223804:cmsbot_crab_inputDBS
241125_223804:cmsbot_crab_useParent
241125_223805:cmsbot_crab_secondaryInputDataset
241125_223806:cmsbot_crab_lumiMaskFile
241125_223806:cmsbot_crab_lumiMaskUrl
241125_223807:cmsbot_crab_outLFNDirBase
241125_223808:cmsbot_crab_runRange
241125_223809:cmsbot_crab_ignoreLocality
241125_223809:cmsbot_crab_userInputFiles
241125_223810:cmsbot_crab_whitelist
241125_223810:cmsbot_crab_blacklist
241125_223811:cmsbot_crab_ignoreGlobalBlacklist
241125_223811:cmsbot_crab_voRole
241125_223812:cmsbot_crab_voGroup
241125_223812:cmsbot_crab_scheddName
241125_223813:cmsbot_crab_collector
241125_223814:cmsbot_crab_extraJDL
```

Finished at: 2024-11-25 23:38:14
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/898/console)

## Comment (cmsdmwmbot, 2024-11-25T23:02:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-26 00:02:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1244/console

```
RETRY TESTS:
outputFiles-check.sh 241125_223754:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 241125_223755:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 241125_223757:cmsbot_crab_numCores - 2
scriptExe-check.sh 241125_223758:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 241125_223759:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 241125_223806:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241125_223806:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241125_223807:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241125_223808:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241125_223809:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241125_223810:cmsbot_crab_whitelist - 2
blacklist-check.sh 241125_223810:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241125_223811:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241125_223811:cmsbot_crab_voRole - 2
voGroup-check.sh 241125_223812:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_223749:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_223750:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_223750:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_223752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_223752:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241125_223755:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 241125_223756:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 241125_223802:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_223803:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_223804:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_223804:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_223805:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 241125_223809:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 241125_223812:cmsbot_crab_scheddName - 0
collector-check.sh 241125_223813:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_223814:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-25T23:26:32Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-11-26 00:26:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1247/console

```
RETRY TESTS:
outputFiles-check.sh 241125_223754:cmsbot_crab_outputFiles - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_223749:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_223750:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_223750:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_223752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_223752:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241125_223755:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_223755:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241125_223756:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241125_223757:cmsbot_crab_numCores - 0
scriptExe-check.sh 241125_223758:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_223759:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_223802:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_223803:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_223804:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_223804:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_223805:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_223806:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241125_223806:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241125_223807:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241125_223808:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241125_223809:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241125_223809:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241125_223810:cmsbot_crab_whitelist - 0
blacklist-check.sh 241125_223810:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241125_223811:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241125_223811:cmsbot_crab_voRole - 0
voGroup-check.sh 241125_223812:cmsbot_crab_voGroup - 0
scheddName-check.sh 241125_223812:cmsbot_crab_scheddName - 0
collector-check.sh 241125_223813:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_223814:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-25T23:50:27Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-11-26 00:50:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1249/console

```
RETRY TESTS:
outputFiles-check.sh 241125_223754:cmsbot_crab_outputFiles - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_223749:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_223750:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_223750:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_223752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_223752:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241125_223755:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_223755:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241125_223756:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241125_223757:cmsbot_crab_numCores - 0
scriptExe-check.sh 241125_223758:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_223759:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_223802:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_223803:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_223804:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_223804:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_223805:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_223806:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241125_223806:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241125_223807:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241125_223808:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241125_223809:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241125_223809:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241125_223810:cmsbot_crab_whitelist - 0
blacklist-check.sh 241125_223810:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241125_223811:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241125_223811:cmsbot_crab_voRole - 0
voGroup-check.sh 241125_223812:cmsbot_crab_voGroup - 0
scheddName-check.sh 241125_223812:cmsbot_crab_scheddName - 0
collector-check.sh 241125_223813:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_223814:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-26T00:13:59Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-11-26 01:13:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1250/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_223749:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_223750:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_223750:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_223752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_223752:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241125_223755:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_223755:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241125_223756:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241125_223757:cmsbot_crab_numCores - 0
scriptExe-check.sh 241125_223758:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_223759:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_223802:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_223803:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_223804:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_223804:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_223805:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_223806:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241125_223806:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241125_223807:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241125_223808:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241125_223809:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241125_223809:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241125_223810:cmsbot_crab_whitelist - 0
blacklist-check.sh 241125_223810:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241125_223811:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241125_223811:cmsbot_crab_voRole - 0
voGroup-check.sh 241125_223812:cmsbot_crab_voGroup - 0
scheddName-check.sh 241125_223812:cmsbot_crab_scheddName - 0
collector-check.sh 241125_223813:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_223814:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 241125_223754:cmsbot_crab_outputFiles - 1
```

## Comment (belforte, 2024-11-26T08:41:49Z)

failure was a job stuck in reading data in Florida
