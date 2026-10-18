# dmwm/CRABServer issue #8156: #663: Test dev CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2024-01-11T19:49:02Z
Closed: 2024-01-11T20:50:59Z
URL: https://github.com/dmwm/CRABServer/issues/8156

## Opening post (cmsdmwmbot, 2024-01-11T19:49:02Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 20:49:02
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/663/)

## Comment (cmsdmwmbot, 2024-01-11T19:50:50Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_194922:cmsbot_crab_transferOutputs
240111_194924:cmsbot_crab_transferLogs
240111_194926:cmsbot_crab_activity
240111_194928:cmsbot_crab_inputFiles
240111_194930:cmsbot_crab_disableAutomaticOutputCollection
240111_194932:cmsbot_crab_outputFiles
240111_194934:cmsbot_crab_allowUndistributedCMSSW
240111_194936:cmsbot_crab_maxMemoryMB
240111_194938:cmsbot_crab_maxJobRuntimeMin
240111_194940:cmsbot_crab_numCores
240111_194943:cmsbot_crab_scriptExe
240111_194945:cmsbot_crab_scriptArgs
240111_194947:cmsbot_crab_sendVenvFolder
240111_194952:cmsbot_crab_sendExternalFolder
240111_194954:cmsbot_crab_inputDBS
240111_194957:cmsbot_crab_useParent
240111_194959:cmsbot_crab_secondaryInputDataset
240111_195001:cmsbot_crab_lumiMaskFile
240111_195003:cmsbot_crab_lumiMaskUrl
240111_195006:cmsbot_crab_outLFNDirBase
240111_195008:cmsbot_crab_runRange
240111_195010:cmsbot_crab_ignoreLocality
240111_195012:cmsbot_crab_userInputFiles
240111_195014:cmsbot_crab_whitelist
240111_195016:cmsbot_crab_blacklist
240111_195018:cmsbot_crab_ignoreGlobalBlacklist
240111_195020:cmsbot_crab_voRole
240111_195022:cmsbot_crab_voGroup
240111_195024:cmsbot_crab_scheddName
240111_195026:cmsbot_crab_collector
240111_195028:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_194920:cmsbot_crab_20240111_204919
```

Finished at: 2024-01-11 20:50:28
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/663/console)

## Comment (cmsdmwmbot, 2024-01-11T20:13:53Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 21:13:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/484/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/484//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-11T20:17:31Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 21:17:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/880/console

```
RETRY TESTS:
maxMemoryMB-check.sh 240111_194936:cmsbot_crab_maxMemoryMB - 2
lumiMaskFile-check.sh 240111_195001:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240111_195003:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240111_195008:cmsbot_crab_runRange - 2
whitelist-check.sh 240111_195014:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_195016:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_194922:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_194924:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_194926:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_194928:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_194930:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_194932:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_194934:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240111_194938:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_194940:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_194943:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_194945:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_194947:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_194952:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_194954:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_194957:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_194959:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240111_195006:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240111_195010:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_195012:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240111_195018:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_195020:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_195022:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_195024:cmsbot_crab_scheddName - 0
collector-check.sh 240111_195026:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_195028:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T20:41:35Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-01-11 21:41:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/882/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_194922:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_194924:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_194926:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_194928:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_194930:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_194932:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_194934:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_194936:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_194938:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_194940:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_194943:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_194945:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_194947:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_194952:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_194954:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_194957:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_194959:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_195001:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_195003:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_195006:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_195008:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_195010:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_195012:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_195014:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_195016:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_195018:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_195020:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_195022:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_195024:cmsbot_crab_scheddName - 0
collector-check.sh 240111_195026:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_195028:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-11T20:50:59Z)

all OK
