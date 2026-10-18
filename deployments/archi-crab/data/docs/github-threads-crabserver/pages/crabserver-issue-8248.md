# dmwm/CRABServer issue #8248: #715: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-02-19T10:09:02Z
Closed: 2024-02-19T13:50:25Z
URL: https://github.com/dmwm/CRABServer/issues/8248

## Opening post (cmsdmwmbot, 2024-02-19T10:09:02Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-02-19 11:09:01
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/715/)

## Comment (cmsdmwmbot, 2024-02-19T10:11:31Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240219_100925:cmsbot_crab_transferOutputs
240219_100928:cmsbot_crab_transferLogs
240219_100930:cmsbot_crab_activity
240219_100932:cmsbot_crab_inputFiles
240219_100934:cmsbot_crab_disableAutomaticOutputCollection
240219_100936:cmsbot_crab_outputFiles
240219_100938:cmsbot_crab_allowUndistributedCMSSW
240219_100941:cmsbot_crab_maxMemoryMB
240219_100943:cmsbot_crab_maxJobRuntimeMin
240219_100945:cmsbot_crab_numCores
240219_100947:cmsbot_crab_scriptExe
240219_100949:cmsbot_crab_scriptArgs
240219_100951:cmsbot_crab_sendVenvFolder
240219_101031:cmsbot_crab_sendExternalFolder
240219_101034:cmsbot_crab_inputDBS
240219_101036:cmsbot_crab_useParent
240219_101038:cmsbot_crab_secondaryInputDataset
240219_101040:cmsbot_crab_lumiMaskFile
240219_101042:cmsbot_crab_lumiMaskUrl
240219_101045:cmsbot_crab_outLFNDirBase
240219_101047:cmsbot_crab_runRange
240219_101049:cmsbot_crab_ignoreLocality
240219_101051:cmsbot_crab_userInputFiles
240219_101053:cmsbot_crab_whitelist
240219_101055:cmsbot_crab_blacklist
240219_101058:cmsbot_crab_ignoreGlobalBlacklist
240219_101100:cmsbot_crab_voRole
240219_101102:cmsbot_crab_voGroup
240219_101104:cmsbot_crab_scheddName
240219_101107:cmsbot_crab_collector
240219_101109:cmsbot_crab_extraJDL
```

Finished at: 2024-02-19 11:11:10
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/715/console)

## Comment (cmsdmwmbot, 2024-02-19T10:35:46Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-19 11:35:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/961/console

```
RETRY TESTS:
numCores-check.sh 240219_100945:cmsbot_crab_numCores - 2
scriptExe-check.sh 240219_100947:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240219_101042:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240219_101047:cmsbot_crab_runRange - 2
whitelist-check.sh 240219_101053:cmsbot_crab_whitelist - 2
blacklist-check.sh 240219_101055:cmsbot_crab_blacklist - 2
voRole-check.sh 240219_101100:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240219_100925:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240219_100928:cmsbot_crab_transferLogs - 0
activity-check.sh 240219_100930:cmsbot_crab_activity - 0
inputFiles-check.sh 240219_100932:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240219_100934:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240219_100936:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240219_100938:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240219_100941:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240219_100943:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 240219_100949:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240219_100951:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240219_101031:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240219_101034:cmsbot_crab_inputDBS - 0
useParent-check.sh 240219_101036:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240219_101038:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240219_101040:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240219_101045:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240219_101049:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240219_101051:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240219_101058:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240219_101102:cmsbot_crab_voGroup - 0
scheddName-check.sh 240219_101104:cmsbot_crab_scheddName - 0
collector-check.sh 240219_101107:cmsbot_crab_collector - 0
extraJDL-check.sh 240219_101109:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-19T11:02:38Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-19 12:02:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/964/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240219_100925:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240219_100928:cmsbot_crab_transferLogs - 0
activity-check.sh 240219_100930:cmsbot_crab_activity - 0
inputFiles-check.sh 240219_100932:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240219_100934:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240219_100938:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240219_100941:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240219_100943:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240219_100945:cmsbot_crab_numCores - 0
scriptExe-check.sh 240219_100947:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240219_100949:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240219_100951:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240219_101031:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240219_101034:cmsbot_crab_inputDBS - 0
useParent-check.sh 240219_101036:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240219_101038:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240219_101040:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240219_101042:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240219_101045:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240219_101047:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240219_101049:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240219_101051:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240219_101053:cmsbot_crab_whitelist - 0
blacklist-check.sh 240219_101055:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240219_101058:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240219_101100:cmsbot_crab_voRole - 0
voGroup-check.sh 240219_101102:cmsbot_crab_voGroup - 0
scheddName-check.sh 240219_101104:cmsbot_crab_scheddName - 0
collector-check.sh 240219_101107:cmsbot_crab_collector - 0
extraJDL-check.sh 240219_101109:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240219_100936:cmsbot_crab_outputFiles - 1
```

## Comment (belforte, 2024-02-19T13:50:25Z)

OK
