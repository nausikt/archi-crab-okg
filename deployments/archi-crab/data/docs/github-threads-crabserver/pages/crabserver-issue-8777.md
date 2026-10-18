# dmwm/CRABServer issue #8777: #874: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-08T11:07:46Z
Closed: 2024-11-08T14:02:50Z
URL: https://github.com/dmwm/CRABServer/issues/8777

## Opening post (cmsdmwmbot, 2024-11-08T11:07:46Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-11-08 12:07:45
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/874/)

## Comment (cmsdmwmbot, 2024-11-08T11:09:43Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241108_110811:cmsbot_crab_transferOutputs
241108_110813:cmsbot_crab_transferLogs
241108_110816:cmsbot_crab_activity
241108_110818:cmsbot_crab_inputFiles
241108_110820:cmsbot_crab_disableAutomaticOutputCollection
241108_110823:cmsbot_crab_outputFiles
241108_110825:cmsbot_crab_allowUndistributedCMSSW
241108_110827:cmsbot_crab_maxMemoryMB
241108_110830:cmsbot_crab_maxJobRuntimeMin
241108_110832:cmsbot_crab_numCores
241108_110835:cmsbot_crab_scriptExe
241108_110837:cmsbot_crab_scriptArgs
241108_110839:cmsbot_crab_sendVenvFolder
241108_110841:cmsbot_crab_sendExternalFolder
241108_110844:cmsbot_crab_inputDBS
241108_110846:cmsbot_crab_useParent
241108_110848:cmsbot_crab_secondaryInputDataset
241108_110851:cmsbot_crab_lumiMaskFile
241108_110853:cmsbot_crab_lumiMaskUrl
241108_110856:cmsbot_crab_outLFNDirBase
241108_110858:cmsbot_crab_runRange
241108_110901:cmsbot_crab_ignoreLocality
241108_110903:cmsbot_crab_userInputFiles
241108_110905:cmsbot_crab_whitelist
241108_110908:cmsbot_crab_blacklist
241108_110910:cmsbot_crab_ignoreGlobalBlacklist
241108_110912:cmsbot_crab_voRole
241108_110915:cmsbot_crab_voGroup
241108_110917:cmsbot_crab_scheddName
241108_110919:cmsbot_crab_collector
241108_110922:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241108_110808:cmsbot_crab_20241108_120808
```

Finished at: 2024-11-08 12:09:22
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/874/console)

## Comment (cmsdmwmbot, 2024-11-08T11:32:58Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-11-08 12:32:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/567/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/567//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-11-08T11:34:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-08 12:34:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1226/console

```
RETRY TESTS:
transferLogs-check.sh 241108_110813:cmsbot_crab_transferLogs - 2
activity-check.sh 241108_110816:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 241108_110820:cmsbot_crab_disableAutomaticOutputCollection - 2
outputFiles-check.sh 241108_110823:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 241108_110827:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 241108_110832:cmsbot_crab_numCores - 2
scriptExe-check.sh 241108_110835:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 241108_110837:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 241108_110853:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241108_110856:cmsbot_crab_outLFNDirBase - 2
blacklist-check.sh 241108_110908:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241108_110910:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241108_110912:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241108_110811:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241108_110818:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 241108_110825:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 241108_110830:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 241108_110839:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241108_110841:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241108_110844:cmsbot_crab_inputDBS - 0
useParent-check.sh 241108_110846:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241108_110848:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241108_110851:cmsbot_crab_lumiMaskFile - 0
voGroup-check.sh 241108_110915:cmsbot_crab_voGroup - 0
scheddName-check.sh 241108_110917:cmsbot_crab_scheddName - 0
collector-check.sh 241108_110919:cmsbot_crab_collector - 0
extraJDL-check.sh 241108_110922:cmsbot_crab_extraJDL - 0

FAILED TESTS:
runRange-check.sh 241108_110858:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 241108_110901:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 241108_110903:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 241108_110905:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2024-11-08T11:58:25Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-11-08 12:58:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1227/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 241108_110853:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 241108_110858:cmsbot_crab_runRange - 2
whitelist-check.sh 241108_110905:cmsbot_crab_whitelist - 2
blacklist-check.sh 241108_110908:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241108_110811:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241108_110813:cmsbot_crab_transferLogs - 0
activity-check.sh 241108_110816:cmsbot_crab_activity - 0
inputFiles-check.sh 241108_110818:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241108_110820:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241108_110823:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241108_110825:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241108_110827:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241108_110830:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241108_110832:cmsbot_crab_numCores - 0
scriptExe-check.sh 241108_110835:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241108_110837:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241108_110839:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241108_110841:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241108_110844:cmsbot_crab_inputDBS - 0
useParent-check.sh 241108_110846:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241108_110848:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241108_110851:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 241108_110856:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 241108_110901:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241108_110903:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 241108_110910:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241108_110912:cmsbot_crab_voRole - 0
voGroup-check.sh 241108_110915:cmsbot_crab_voGroup - 0
scheddName-check.sh 241108_110917:cmsbot_crab_scheddName - 0
collector-check.sh 241108_110919:cmsbot_crab_collector - 0
extraJDL-check.sh 241108_110922:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-08T12:22:41Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-11-08 13:22:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1229/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241108_110811:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241108_110813:cmsbot_crab_transferLogs - 0
activity-check.sh 241108_110816:cmsbot_crab_activity - 0
inputFiles-check.sh 241108_110818:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241108_110820:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241108_110823:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241108_110825:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241108_110827:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241108_110830:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241108_110832:cmsbot_crab_numCores - 0
scriptExe-check.sh 241108_110835:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241108_110837:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241108_110839:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241108_110841:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241108_110844:cmsbot_crab_inputDBS - 0
useParent-check.sh 241108_110846:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241108_110848:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241108_110851:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241108_110853:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241108_110856:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241108_110858:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241108_110901:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241108_110903:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241108_110905:cmsbot_crab_whitelist - 0
blacklist-check.sh 241108_110908:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241108_110910:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241108_110912:cmsbot_crab_voRole - 0
voGroup-check.sh 241108_110915:cmsbot_crab_voGroup - 0
scheddName-check.sh 241108_110917:cmsbot_crab_scheddName - 0
collector-check.sh 241108_110919:cmsbot_crab_collector - 0
extraJDL-check.sh 241108_110922:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-11-08T14:02:50Z)

all OK
