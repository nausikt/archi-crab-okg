# dmwm/CRABServer issue #8315: #745: Test dev CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-03T20:20:25Z
Closed: 2024-04-04T09:08:35Z
URL: https://github.com/dmwm/CRABServer/issues/8315

## Opening post (cmsdmwmbot, 2024-04-03T20:20:25Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-04-03 22:20:25
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/745/)

## Comment (cmsdmwmbot, 2024-04-03T20:23:43Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240403_202044:cmsbot_crab_transferOutputs
240403_202046:cmsbot_crab_transferLogs
240403_202048:cmsbot_crab_activity
240403_202051:cmsbot_crab_inputFiles
240403_202053:cmsbot_crab_disableAutomaticOutputCollection
240403_202055:cmsbot_crab_outputFiles
240403_202105:cmsbot_crab_allowUndistributedCMSSW
240403_202107:cmsbot_crab_maxMemoryMB
240403_202109:cmsbot_crab_maxJobRuntimeMin
240403_202119:cmsbot_crab_numCores
240403_202129:cmsbot_crab_scriptExe
240403_202132:cmsbot_crab_scriptArgs
240403_202142:cmsbot_crab_sendVenvFolder
240403_202227:cmsbot_crab_sendExternalFolder
240403_202229:cmsbot_crab_inputDBS
240403_202239:cmsbot_crab_useParent
240403_202241:cmsbot_crab_secondaryInputDataset
240403_202243:cmsbot_crab_lumiMaskFile
240403_202246:cmsbot_crab_lumiMaskUrl
240403_202249:cmsbot_crab_outLFNDirBase
240403_202251:cmsbot_crab_runRange
240403_202253:cmsbot_crab_ignoreLocality
240403_202255:cmsbot_crab_userInputFiles
240403_202257:cmsbot_crab_whitelist
240403_202259:cmsbot_crab_blacklist
240403_202309:cmsbot_crab_ignoreGlobalBlacklist
240403_202312:cmsbot_crab_voRole
240403_202314:cmsbot_crab_voGroup
240403_202316:cmsbot_crab_scheddName
240403_202318:cmsbot_crab_collector
240403_202321:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240403_202042:cmsbot_crab_20240403_222041
```

Finished at: 2024-04-03 22:23:22
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/745/console)

## Comment (cmsdmwmbot, 2024-04-03T20:46:47Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-03 22:46:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/519/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/519//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-03T20:47:54Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-03 22:47:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1005/console

```
RETRY TESTS:
transferLogs-check.sh 240403_202046:cmsbot_crab_transferLogs - 2
disableAutomaticOutputCollection-check.sh 240403_202053:cmsbot_crab_disableAutomaticOutputCollection - 2
outputFiles-check.sh 240403_202055:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240403_202107:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 240403_202119:cmsbot_crab_numCores - 2
scriptExe-check.sh 240403_202129:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240403_202132:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240403_202239:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240403_202241:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240403_202243:cmsbot_crab_lumiMaskFile - 2
runRange-check.sh 240403_202251:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240403_202253:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 240403_202255:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240403_202257:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240403_202044:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240403_202051:cmsbot_crab_inputFiles - 0
sendVenvFolder-check.sh 240403_202142:cmsbot_crab_sendVenvFolder - 0
inputDBS-check.sh 240403_202229:cmsbot_crab_inputDBS - 0

FAILED TESTS:
activity-check.sh 240403_202048:cmsbot_crab_activity - 1
allowUndistributedCMSSW-check.sh 240403_202105:cmsbot_crab_allowUndistributedCMSSW - 1
maxJobRuntimeMin-check.sh 240403_202109:cmsbot_crab_maxJobRuntimeMin - 1
sendExternalFolder-check.sh 240403_202227:cmsbot_crab_sendExternalFolder - 1
lumiMaskUrl-check.sh 240403_202246:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240403_202249:cmsbot_crab_outLFNDirBase - 1
blacklist-check.sh 240403_202259:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240403_202309:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240403_202312:cmsbot_crab_voRole - 1
voGroup-check.sh 240403_202314:cmsbot_crab_voGroup - 1
scheddName-check.sh 240403_202316:cmsbot_crab_scheddName - 1
collector-check.sh 240403_202318:cmsbot_crab_collector - 1
extraJDL-check.sh 240403_202321:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-04-03T21:14:36Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-04-03 23:14:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1009/console

```
RETRY TESTS:
activity-check.sh 240403_202048:cmsbot_crab_activity - 2
runRange-check.sh 240403_202251:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240403_202255:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240403_202257:cmsbot_crab_whitelist - 2
voGroup-check.sh 240403_202314:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240403_202044:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240403_202046:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240403_202051:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240403_202053:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240403_202055:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240403_202105:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240403_202107:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240403_202109:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_202119:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_202129:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_202132:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_202142:cmsbot_crab_sendVenvFolder - 0
inputDBS-check.sh 240403_202229:cmsbot_crab_inputDBS - 0
useParent-check.sh 240403_202239:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240403_202241:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240403_202243:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240403_202249:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240403_202253:cmsbot_crab_ignoreLocality - 0
voRole-check.sh 240403_202312:cmsbot_crab_voRole - 0
scheddName-check.sh 240403_202316:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240403_202321:cmsbot_crab_extraJDL - 0

FAILED TESTS:
sendExternalFolder-check.sh 240403_202227:cmsbot_crab_sendExternalFolder - 1
lumiMaskUrl-check.sh 240403_202246:cmsbot_crab_lumiMaskUrl - 1
blacklist-check.sh 240403_202259:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240403_202309:cmsbot_crab_ignoreGlobalBlacklist - 1
collector-check.sh 240403_202318:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-03T21:52:56Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-03 23:52:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1013/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240403_202044:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240403_202046:cmsbot_crab_transferLogs - 0
activity-check.sh 240403_202048:cmsbot_crab_activity - 0
inputFiles-check.sh 240403_202051:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240403_202053:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240403_202055:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240403_202105:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240403_202107:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240403_202109:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_202119:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_202129:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_202132:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_202142:cmsbot_crab_sendVenvFolder - 0
inputDBS-check.sh 240403_202229:cmsbot_crab_inputDBS - 0
useParent-check.sh 240403_202239:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240403_202241:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240403_202243:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240403_202249:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240403_202251:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240403_202253:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240403_202255:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240403_202257:cmsbot_crab_whitelist - 0
voRole-check.sh 240403_202312:cmsbot_crab_voRole - 0
voGroup-check.sh 240403_202314:cmsbot_crab_voGroup - 0
scheddName-check.sh 240403_202316:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240403_202321:cmsbot_crab_extraJDL - 0

FAILED TESTS:
sendExternalFolder-check.sh 240403_202227:cmsbot_crab_sendExternalFolder - 1
lumiMaskUrl-check.sh 240403_202246:cmsbot_crab_lumiMaskUrl - 1
blacklist-check.sh 240403_202259:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240403_202309:cmsbot_crab_ignoreGlobalBlacklist - 1
collector-check.sh 240403_202318:cmsbot_crab_collector - 1
```
