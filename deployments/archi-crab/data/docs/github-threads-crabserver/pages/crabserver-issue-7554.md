# dmwm/CRABServer issue #7554: #377: Test GH CRABClient using preprod REST instance and CMSSW_12_6_0_pre4 CMSSW release

State: closed
Opened: 2023-02-27T11:57:14Z
Closed: 2023-02-27T13:16:00Z
URL: https://github.com/dmwm/CRABServer/issues/7554

## Opening post (cmsdmwmbot, 2023-02-27T11:57:14Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_0_pre4**
- SCRAM_ARCH: **el8_amd64_gcc10**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2023-02-27 12:57:13
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/377/)

## Comment (cmsdmwmbot, 2023-02-27T11:58:49Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230227_115739:cmsbot_crab_transferOutputs
230227_115741:cmsbot_crab_transferLogs
230227_115742:cmsbot_crab_activity
230227_115743:cmsbot_crab_inputFiles
230227_115745:cmsbot_crab_disableAutomaticOutputCollection
230227_115747:cmsbot_crab_outputFiles
230227_115748:cmsbot_crab_allowUndistributedCMSSW
230227_115749:cmsbot_crab_maxMemoryMB
230227_115751:cmsbot_crab_maxJobRuntimeMin
230227_115752:cmsbot_crab_numCores
230227_115754:cmsbot_crab_scriptExe
230227_115755:cmsbot_crab_scriptArgs
230227_115757:cmsbot_crab_sendPythonFolder
230227_115802:cmsbot_crab_sendExternalFolder
230227_115803:cmsbot_crab_inputDBS
230227_115805:cmsbot_crab_useParent
230227_115806:cmsbot_crab_secondaryInputDataset
230227_115808:cmsbot_crab_lumiMaskFile
230227_115809:cmsbot_crab_lumiMaskUrl
230227_115811:cmsbot_crab_outLFNDirBase
230227_115813:cmsbot_crab_runRange
230227_115814:cmsbot_crab_ignoreLocality
230227_115816:cmsbot_crab_userInputFiles
230227_115817:cmsbot_crab_whitelist
230227_115819:cmsbot_crab_blacklist
230227_115820:cmsbot_crab_ignoreGlobalBlacklist
230227_115821:cmsbot_crab_voRole
230227_115823:cmsbot_crab_voGroup
230227_115824:cmsbot_crab_scheddName
230227_115826:cmsbot_crab_collector
230227_115827:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230227_115738:cmsbot_crab_20230227_125737
```

Finished at: 2023-02-27 12:58:28
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/377/console)

## Comment (mapellidario, 2023-02-27T12:01:41Z)

I am testing CRABClient master branch, after https://github.com/dmwm/CRABClient/pull/5188

## Comment (cmsdmwmbot, 2023-02-27T12:19:48Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-02-27 13:19:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/338/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/338//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-02-27T12:21:42Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-27 13:21:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/587/console

```
RETRY TESTS:
numCores-check.sh 230227_115752:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230227_115809:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230227_115813:cmsbot_crab_runRange - 2
whitelist-check.sh 230227_115817:cmsbot_crab_whitelist - 2
blacklist-check.sh 230227_115819:cmsbot_crab_blacklist - 2
voGroup-check.sh 230227_115823:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230227_115739:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230227_115741:cmsbot_crab_transferLogs - 0
activity-check.sh 230227_115742:cmsbot_crab_activity - 0
inputFiles-check.sh 230227_115743:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230227_115745:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230227_115747:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230227_115748:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230227_115749:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230227_115751:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230227_115754:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230227_115755:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230227_115757:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230227_115802:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230227_115803:cmsbot_crab_inputDBS - 0
useParent-check.sh 230227_115805:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230227_115806:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230227_115808:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230227_115811:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230227_115814:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230227_115816:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230227_115820:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230227_115821:cmsbot_crab_voRole - 0
scheddName-check.sh 230227_115824:cmsbot_crab_scheddName - 0
collector-check.sh 230227_115826:cmsbot_crab_collector - 0
extraJDL-check.sh 230227_115827:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-02-27T12:43:50Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-02-27 13:43:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/588/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230227_115809:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230227_115739:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230227_115741:cmsbot_crab_transferLogs - 0
activity-check.sh 230227_115742:cmsbot_crab_activity - 0
inputFiles-check.sh 230227_115743:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230227_115745:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230227_115747:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230227_115748:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230227_115749:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230227_115751:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230227_115752:cmsbot_crab_numCores - 0
scriptExe-check.sh 230227_115754:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230227_115755:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230227_115757:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230227_115802:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230227_115803:cmsbot_crab_inputDBS - 0
useParent-check.sh 230227_115805:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230227_115806:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230227_115808:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230227_115811:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230227_115813:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230227_115814:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230227_115816:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230227_115817:cmsbot_crab_whitelist - 0
blacklist-check.sh 230227_115819:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230227_115820:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230227_115821:cmsbot_crab_voRole - 0
voGroup-check.sh 230227_115823:cmsbot_crab_voGroup - 0
scheddName-check.sh 230227_115824:cmsbot_crab_scheddName - 0
collector-check.sh 230227_115826:cmsbot_crab_collector - 0
extraJDL-check.sh 230227_115827:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-02-27T13:06:05Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-02-27 14:06:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/589/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230227_115739:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230227_115741:cmsbot_crab_transferLogs - 0
activity-check.sh 230227_115742:cmsbot_crab_activity - 0
inputFiles-check.sh 230227_115743:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230227_115745:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230227_115747:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230227_115748:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230227_115749:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230227_115751:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230227_115752:cmsbot_crab_numCores - 0
scriptExe-check.sh 230227_115754:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230227_115755:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230227_115757:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230227_115802:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230227_115803:cmsbot_crab_inputDBS - 0
useParent-check.sh 230227_115805:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230227_115806:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230227_115808:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230227_115809:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230227_115811:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230227_115813:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230227_115814:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230227_115816:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230227_115817:cmsbot_crab_whitelist - 0
blacklist-check.sh 230227_115819:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230227_115820:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230227_115821:cmsbot_crab_voRole - 0
voGroup-check.sh 230227_115823:cmsbot_crab_voGroup - 0
scheddName-check.sh 230227_115824:cmsbot_crab_scheddName - 0
collector-check.sh 230227_115826:cmsbot_crab_collector - 0
extraJDL-check.sh 230227_115827:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (mapellidario, 2023-02-27T13:16:00Z)

Good! I will create a new CRABClient tag
