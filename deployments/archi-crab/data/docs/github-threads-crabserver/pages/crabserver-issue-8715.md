# dmwm/CRABServer issue #8715: #841: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-20T22:47:53Z
Closed: 2024-09-23T21:04:25Z
URL: https://github.com/dmwm/CRABServer/issues/8715

## Opening post (cmsdmwmbot, 2024-09-20T22:47:53Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-09-21 00:47:52
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/841/)

## Comment (cmsdmwmbot, 2024-09-20T22:49:53Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240920_224815:cmsbot_crab_transferOutputs
240920_224818:cmsbot_crab_transferLogs
240920_224820:cmsbot_crab_activity
240920_224823:cmsbot_crab_inputFiles
240920_224825:cmsbot_crab_disableAutomaticOutputCollection
240920_224827:cmsbot_crab_outputFiles
240920_224830:cmsbot_crab_allowUndistributedCMSSW
240920_224832:cmsbot_crab_maxMemoryMB
240920_224835:cmsbot_crab_maxJobRuntimeMin
240920_224838:cmsbot_crab_numCores
240920_224840:cmsbot_crab_scriptExe
240920_224843:cmsbot_crab_scriptArgs
240920_224845:cmsbot_crab_sendVenvFolder
240920_224848:cmsbot_crab_sendExternalFolder
240920_224850:cmsbot_crab_inputDBS
240920_224853:cmsbot_crab_useParent
240920_224855:cmsbot_crab_secondaryInputDataset
240920_224858:cmsbot_crab_lumiMaskFile
240920_224900:cmsbot_crab_lumiMaskUrl
240920_224904:cmsbot_crab_outLFNDirBase
240920_224906:cmsbot_crab_runRange
240920_224909:cmsbot_crab_ignoreLocality
240920_224911:cmsbot_crab_userInputFiles
240920_224914:cmsbot_crab_whitelist
240920_224916:cmsbot_crab_blacklist
240920_224919:cmsbot_crab_ignoreGlobalBlacklist
240920_224921:cmsbot_crab_voRole
240920_224924:cmsbot_crab_voGroup
240920_224927:cmsbot_crab_scheddName
240920_224929:cmsbot_crab_collector
240920_224931:cmsbot_crab_extraJDL
```

Finished at: 2024-09-21 00:49:32
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/841/console)

## Comment (cmsdmwmbot, 2024-09-20T23:13:56Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-21 01:13:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1199/console

```
RETRY TESTS:
outputFiles-check.sh 240920_224827:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240920_224832:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 240920_224838:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240920_224900:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240920_224906:cmsbot_crab_runRange - 2
whitelist-check.sh 240920_224914:cmsbot_crab_whitelist - 2
blacklist-check.sh 240920_224916:cmsbot_crab_blacklist - 2
voRole-check.sh 240920_224921:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_224815:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_224818:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_224820:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_224823:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240920_224825:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240920_224830:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240920_224835:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240920_224840:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240920_224843:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_224845:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_224848:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_224850:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_224853:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240920_224855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240920_224858:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240920_224904:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_224909:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_224911:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240920_224919:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240920_224924:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_224927:cmsbot_crab_scheddName - 0
collector-check.sh 240920_224929:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_224931:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-09-20T23:38:15Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-09-21 01:38:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1200/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240920_224900:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240920_224906:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_224815:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_224818:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_224820:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_224823:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240920_224825:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240920_224827:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_224830:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240920_224832:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240920_224835:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240920_224838:cmsbot_crab_numCores - 0
scriptExe-check.sh 240920_224840:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240920_224843:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_224845:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_224848:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_224850:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_224853:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240920_224855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240920_224858:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240920_224904:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_224909:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_224911:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240920_224914:cmsbot_crab_whitelist - 0
blacklist-check.sh 240920_224916:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240920_224919:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240920_224921:cmsbot_crab_voRole - 0
voGroup-check.sh 240920_224924:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_224927:cmsbot_crab_scheddName - 0
collector-check.sh 240920_224929:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_224931:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-09-21T00:02:43Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-09-21 02:02:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1201/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_224815:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_224818:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_224820:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_224823:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240920_224825:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240920_224827:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_224830:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240920_224832:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240920_224835:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240920_224838:cmsbot_crab_numCores - 0
scriptExe-check.sh 240920_224840:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240920_224843:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_224845:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_224848:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_224850:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_224853:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240920_224855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240920_224858:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240920_224900:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_224904:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240920_224906:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240920_224909:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_224911:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240920_224914:cmsbot_crab_whitelist - 0
blacklist-check.sh 240920_224916:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240920_224919:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240920_224921:cmsbot_crab_voRole - 0
voGroup-check.sh 240920_224924:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_224927:cmsbot_crab_scheddName - 0
collector-check.sh 240920_224929:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_224931:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
