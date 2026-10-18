# dmwm/CRABServer issue #8317: #746: Test dev CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-04T09:06:23Z
Closed: 2024-04-04T10:03:45Z
URL: https://github.com/dmwm/CRABServer/issues/8317

## Opening post (cmsdmwmbot, 2024-04-04T09:06:23Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-04-04 11:06:22
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/746/)

## Comment (cmsdmwmbot, 2024-04-04T09:08:56Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240404_090645:cmsbot_crab_transferOutputs
240404_090647:cmsbot_crab_transferLogs
240404_090650:cmsbot_crab_activity
240404_090652:cmsbot_crab_inputFiles
240404_090655:cmsbot_crab_disableAutomaticOutputCollection
240404_090657:cmsbot_crab_outputFiles
240404_090701:cmsbot_crab_allowUndistributedCMSSW
240404_090703:cmsbot_crab_maxMemoryMB
240404_090705:cmsbot_crab_maxJobRuntimeMin
240404_090708:cmsbot_crab_numCores
240404_090710:cmsbot_crab_scriptExe
240404_090712:cmsbot_crab_scriptArgs
240404_090714:cmsbot_crab_sendVenvFolder
240404_090756:cmsbot_crab_sendExternalFolder
240404_090759:cmsbot_crab_inputDBS
240404_090801:cmsbot_crab_useParent
240404_090803:cmsbot_crab_secondaryInputDataset
240404_090805:cmsbot_crab_lumiMaskFile
240404_090807:cmsbot_crab_lumiMaskUrl
240404_090811:cmsbot_crab_outLFNDirBase
240404_090813:cmsbot_crab_runRange
240404_090815:cmsbot_crab_ignoreLocality
240404_090817:cmsbot_crab_userInputFiles
240404_090819:cmsbot_crab_whitelist
240404_090821:cmsbot_crab_blacklist
240404_090823:cmsbot_crab_ignoreGlobalBlacklist
240404_090825:cmsbot_crab_voRole
240404_090827:cmsbot_crab_voGroup
240404_090830:cmsbot_crab_scheddName
240404_090832:cmsbot_crab_collector
240404_090834:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240404_090643:cmsbot_crab_20240404_110642
```

Finished at: 2024-04-04 11:08:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/746/console)

## Comment (cmsdmwmbot, 2024-04-04T09:33:07Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-04 11:33:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/521/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/521//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-04T09:35:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-04 11:35:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1016/console

```
RETRY TESTS:
transferLogs-check.sh 240404_090647:cmsbot_crab_transferLogs - 2
lumiMaskUrl-check.sh 240404_090807:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240404_090811:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240404_090813:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240404_090817:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240404_090819:cmsbot_crab_whitelist - 2
blacklist-check.sh 240404_090821:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240404_090823:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240404_090825:cmsbot_crab_voRole - 2
voGroup-check.sh 240404_090827:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240404_090645:cmsbot_crab_transferOutputs - 0
activity-check.sh 240404_090650:cmsbot_crab_activity - 0
inputFiles-check.sh 240404_090652:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240404_090655:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240404_090657:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240404_090701:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240404_090703:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240404_090705:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240404_090708:cmsbot_crab_numCores - 0
scriptExe-check.sh 240404_090710:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240404_090712:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240404_090714:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240404_090756:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240404_090759:cmsbot_crab_inputDBS - 0
useParent-check.sh 240404_090801:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240404_090803:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240404_090805:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240404_090815:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 240404_090830:cmsbot_crab_scheddName - 0
collector-check.sh 240404_090832:cmsbot_crab_collector - 0
extraJDL-check.sh 240404_090834:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-04-04T10:01:07Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-04-04 12:01:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1018/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240404_090645:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240404_090647:cmsbot_crab_transferLogs - 0
activity-check.sh 240404_090650:cmsbot_crab_activity - 0
inputFiles-check.sh 240404_090652:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240404_090655:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240404_090657:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240404_090701:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240404_090703:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240404_090705:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240404_090708:cmsbot_crab_numCores - 0
scriptExe-check.sh 240404_090710:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240404_090712:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240404_090714:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240404_090756:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240404_090759:cmsbot_crab_inputDBS - 0
useParent-check.sh 240404_090801:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240404_090803:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240404_090805:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240404_090807:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240404_090811:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240404_090813:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240404_090815:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240404_090817:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240404_090819:cmsbot_crab_whitelist - 0
blacklist-check.sh 240404_090821:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240404_090823:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240404_090825:cmsbot_crab_voRole - 0
voGroup-check.sh 240404_090827:cmsbot_crab_voGroup - 0
scheddName-check.sh 240404_090830:cmsbot_crab_scheddName - 0
collector-check.sh 240404_090832:cmsbot_crab_collector - 0
extraJDL-check.sh 240404_090834:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-04-04T10:03:45Z)

all ok
