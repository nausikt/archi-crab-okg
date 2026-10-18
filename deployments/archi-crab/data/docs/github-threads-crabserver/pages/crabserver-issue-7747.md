# dmwm/CRABServer issue #7747: #434: Test prod CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-07-12T14:26:51Z
Closed: 2023-07-12T20:47:53Z
URL: https://github.com/dmwm/CRABServer/issues/7747

## Opening post (cmsdmwmbot, 2023-07-12T14:26:51Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-07-12 16:26:50
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/434/)

## Comment (cmsdmwmbot, 2023-07-12T14:30:10Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230712_142818:cmsbot_crab_transferOutputs
230712_142820:cmsbot_crab_transferLogs
230712_142823:cmsbot_crab_activity
230712_142826:cmsbot_crab_inputFiles
230712_142829:cmsbot_crab_disableAutomaticOutputCollection
230712_142832:cmsbot_crab_outputFiles
230712_142835:cmsbot_crab_allowUndistributedCMSSW
230712_142838:cmsbot_crab_maxMemoryMB
230712_142840:cmsbot_crab_maxJobRuntimeMin
230712_142843:cmsbot_crab_numCores
230712_142846:cmsbot_crab_scriptExe
230712_142849:cmsbot_crab_scriptArgs
230712_142852:cmsbot_crab_sendPythonFolder
230712_142858:cmsbot_crab_sendExternalFolder
230712_142901:cmsbot_crab_inputDBS
230712_142904:cmsbot_crab_useParent
230712_142907:cmsbot_crab_secondaryInputDataset
230712_142910:cmsbot_crab_lumiMaskFile
230712_142913:cmsbot_crab_lumiMaskUrl
230712_142917:cmsbot_crab_outLFNDirBase
230712_142920:cmsbot_crab_runRange
230712_142922:cmsbot_crab_ignoreLocality
230712_142925:cmsbot_crab_userInputFiles
230712_142928:cmsbot_crab_whitelist
230712_142931:cmsbot_crab_blacklist
230712_142934:cmsbot_crab_ignoreGlobalBlacklist
230712_142937:cmsbot_crab_voRole
230712_142940:cmsbot_crab_voGroup
230712_142943:cmsbot_crab_scheddName
230712_142945:cmsbot_crab_collector
230712_142948:cmsbot_crab_extraJDL
```

Finished at: 2023-07-12 16:29:49
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/434/console)

## Comment (cmsdmwmbot, 2023-07-12T14:55:21Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-12 16:55:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/715/console

```
RETRY TESTS:
transferLogs-check.sh 230712_142820:cmsbot_crab_transferLogs - 2
activity-check.sh 230712_142823:cmsbot_crab_activity - 2
secondaryInputDataset-check.sh 230712_142907:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 230712_142910:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230712_142913:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230712_142920:cmsbot_crab_runRange - 2
whitelist-check.sh 230712_142928:cmsbot_crab_whitelist - 2
blacklist-check.sh 230712_142931:cmsbot_crab_blacklist - 2
voRole-check.sh 230712_142937:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_142818:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230712_142826:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_142829:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_142832:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_142835:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_142838:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_142840:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230712_142843:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_142846:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_142849:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_142852:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_142858:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_142901:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_142904:cmsbot_crab_useParent - 0
outLFNDirBase-check.sh 230712_142917:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230712_142922:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_142925:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230712_142934:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230712_142940:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_142943:cmsbot_crab_scheddName - 0
collector-check.sh 230712_142945:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_142948:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-12T15:20:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-12 17:20:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/719/console

```
RETRY TESTS:
activity-check.sh 230712_142823:cmsbot_crab_activity - 2
secondaryInputDataset-check.sh 230712_142907:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230712_142913:cmsbot_crab_lumiMaskUrl - 2
blacklist-check.sh 230712_142931:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_142818:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_142820:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230712_142826:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_142829:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_142832:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_142835:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_142838:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_142840:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230712_142843:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_142846:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_142849:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_142852:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_142858:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_142901:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_142904:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230712_142910:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230712_142917:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230712_142920:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230712_142922:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_142925:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230712_142928:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 230712_142934:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_142937:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_142940:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_142943:cmsbot_crab_scheddName - 0
collector-check.sh 230712_142945:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_142948:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-12T15:49:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-12 17:49:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/724/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230712_142913:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_142818:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_142820:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_142823:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_142826:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_142829:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_142832:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_142835:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_142838:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_142840:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230712_142843:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_142846:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_142849:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_142852:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_142858:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_142901:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_142904:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_142907:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_142910:cmsbot_crab_lumiMaskFile - 0
runRange-check.sh 230712_142920:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230712_142922:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_142925:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230712_142928:cmsbot_crab_whitelist - 0
blacklist-check.sh 230712_142931:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230712_142934:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_142937:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_142940:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_142943:cmsbot_crab_scheddName - 0
collector-check.sh 230712_142945:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_142948:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outLFNDirBase-check.sh 230712_142917:cmsbot_crab_outLFNDirBase - 1
```

## Comment (cmsdmwmbot, 2023-07-12T16:12:52Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-12 18:12:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/726/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 230712_142818:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230712_142820:cmsbot_crab_transferLogs - 1
activity-check.sh 230712_142823:cmsbot_crab_activity - 1
inputFiles-check.sh 230712_142826:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 230712_142829:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230712_142832:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 230712_142835:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 230712_142838:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230712_142840:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230712_142843:cmsbot_crab_numCores - 1
scriptExe-check.sh 230712_142846:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230712_142849:cmsbot_crab_scriptArgs - 1
sendPythonFolder-check.sh 230712_142852:cmsbot_crab_sendPythonFolder - 1
sendExternalFolder-check.sh 230712_142858:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 230712_142901:cmsbot_crab_inputDBS - 1
useParent-check.sh 230712_142904:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230712_142907:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230712_142910:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230712_142913:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230712_142917:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230712_142920:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230712_142922:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230712_142925:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230712_142928:cmsbot_crab_whitelist - 1
blacklist-check.sh 230712_142931:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230712_142934:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230712_142937:cmsbot_crab_voRole - 1
voGroup-check.sh 230712_142940:cmsbot_crab_voGroup - 1
scheddName-check.sh 230712_142943:cmsbot_crab_scheddName - 1
collector-check.sh 230712_142945:cmsbot_crab_collector - 1
extraJDL-check.sh 230712_142948:cmsbot_crab_extraJDL - 1
```

## Comment (belforte, 2023-07-12T20:47:53Z)

FAILED DUE TO GITLAB DOWNTIME
