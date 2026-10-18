# dmwm/CRABServer issue #8322: #751: Test dev CRABClient using prod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2024-04-05T14:30:25Z
Closed: 2024-04-05T15:22:48Z
URL: https://github.com/dmwm/CRABServer/issues/8322

## Opening post (cmsdmwmbot, 2024-04-05T14:30:25Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-04-05 16:30:24
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/751/)

## Comment (cmsdmwmbot, 2024-04-05T14:32:04Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240405_143057:cmsbot_crab_transferOutputs
240405_143058:cmsbot_crab_transferLogs
240405_143059:cmsbot_crab_activity
240405_143101:cmsbot_crab_inputFiles
240405_143102:cmsbot_crab_disableAutomaticOutputCollection
240405_143105:cmsbot_crab_outputFiles
240405_143106:cmsbot_crab_allowUndistributedCMSSW
240405_143107:cmsbot_crab_maxMemoryMB
240405_143108:cmsbot_crab_maxJobRuntimeMin
240405_143110:cmsbot_crab_numCores
240405_143111:cmsbot_crab_scriptExe
240405_143112:cmsbot_crab_scriptArgs
240405_143114:cmsbot_crab_sendVenvFolder
240405_143116:cmsbot_crab_sendExternalFolder
240405_143116:cmsbot_crab_inputDBS
240405_143117:cmsbot_crab_useParent
240405_143118:cmsbot_crab_secondaryInputDataset
240405_143119:cmsbot_crab_lumiMaskFile
240405_143130:cmsbot_crab_lumiMaskUrl
240405_143132:cmsbot_crab_outLFNDirBase
240405_143133:cmsbot_crab_runRange
240405_143134:cmsbot_crab_ignoreLocality
240405_143135:cmsbot_crab_userInputFiles
240405_143136:cmsbot_crab_whitelist
240405_143137:cmsbot_crab_blacklist
240405_143138:cmsbot_crab_ignoreGlobalBlacklist
240405_143139:cmsbot_crab_voRole
240405_143140:cmsbot_crab_voGroup
240405_143141:cmsbot_crab_scheddName
240405_143141:cmsbot_crab_collector
240405_143142:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240405_143056:cmsbot_crab_20240405_163054
```

Finished at: 2024-04-05 16:31:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/751/console)

## Comment (cmsdmwmbot, 2024-04-05T14:56:11Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-05 16:56:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/526/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/526//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-05T14:57:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-05 16:57:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1024/console

```
RETRY TESTS:
transferLogs-check.sh 240405_143058:cmsbot_crab_transferLogs - 2
activity-check.sh 240405_143059:cmsbot_crab_activity - 2
outputFiles-check.sh 240405_143105:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240405_143108:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240405_143110:cmsbot_crab_numCores - 2
scriptExe-check.sh 240405_143111:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240405_143130:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240405_143133:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240405_143135:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240405_143136:cmsbot_crab_whitelist - 2
blacklist-check.sh 240405_143137:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240405_143138:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240405_143139:cmsbot_crab_voRole - 2
voGroup-check.sh 240405_143140:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240405_143057:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240405_143101:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240405_143102:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240405_143106:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240405_143107:cmsbot_crab_maxMemoryMB - 0
scriptArgs-check.sh 240405_143112:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240405_143114:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240405_143116:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240405_143116:cmsbot_crab_inputDBS - 0
useParent-check.sh 240405_143117:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240405_143118:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240405_143119:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240405_143132:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240405_143134:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 240405_143141:cmsbot_crab_scheddName - 0
collector-check.sh 240405_143141:cmsbot_crab_collector - 0
extraJDL-check.sh 240405_143142:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-04-05T15:21:39Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-04-05 17:21:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1027/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240405_143057:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240405_143058:cmsbot_crab_transferLogs - 0
activity-check.sh 240405_143059:cmsbot_crab_activity - 0
inputFiles-check.sh 240405_143101:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240405_143102:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240405_143105:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240405_143106:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240405_143107:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240405_143108:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240405_143110:cmsbot_crab_numCores - 0
scriptExe-check.sh 240405_143111:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240405_143112:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240405_143114:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240405_143116:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240405_143116:cmsbot_crab_inputDBS - 0
useParent-check.sh 240405_143117:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240405_143118:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240405_143119:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240405_143130:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240405_143132:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240405_143133:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240405_143134:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240405_143135:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240405_143136:cmsbot_crab_whitelist - 0
blacklist-check.sh 240405_143137:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240405_143138:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240405_143139:cmsbot_crab_voRole - 0
voGroup-check.sh 240405_143140:cmsbot_crab_voGroup - 0
scheddName-check.sh 240405_143141:cmsbot_crab_scheddName - 0
collector-check.sh 240405_143141:cmsbot_crab_collector - 0
extraJDL-check.sh 240405_143142:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-04-05T15:22:48Z)

OK
