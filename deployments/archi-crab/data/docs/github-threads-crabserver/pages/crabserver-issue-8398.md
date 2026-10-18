# dmwm/CRABServer issue #8398: #775: Test prod CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2024-05-13T12:21:40Z
Closed: 2024-05-13T17:32:21Z
URL: https://github.com/dmwm/CRABServer/issues/8398

## Opening post (cmsdmwmbot, 2024-05-13T12:21:40Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-05-13 14:21:39
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/775/)

## Comment (cmsdmwmbot, 2024-05-13T12:23:34Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240513_122234:cmsbot_crab_transferOutputs
240513_122236:cmsbot_crab_transferLogs
240513_122237:cmsbot_crab_activity
240513_122238:cmsbot_crab_inputFiles
240513_122239:cmsbot_crab_disableAutomaticOutputCollection
240513_122240:cmsbot_crab_outputFiles
240513_122242:cmsbot_crab_allowUndistributedCMSSW
240513_122243:cmsbot_crab_maxMemoryMB
240513_122245:cmsbot_crab_maxJobRuntimeMin
240513_122246:cmsbot_crab_numCores
240513_122247:cmsbot_crab_scriptExe
240513_122249:cmsbot_crab_scriptArgs
240513_122250:cmsbot_crab_sendVenvFolder
240513_122251:cmsbot_crab_sendExternalFolder
240513_122252:cmsbot_crab_inputDBS
240513_122254:cmsbot_crab_useParent
240513_122255:cmsbot_crab_secondaryInputDataset
240513_122256:cmsbot_crab_lumiMaskFile
240513_122257:cmsbot_crab_lumiMaskUrl
240513_122259:cmsbot_crab_outLFNDirBase
240513_122300:cmsbot_crab_runRange
240513_122301:cmsbot_crab_ignoreLocality
240513_122302:cmsbot_crab_userInputFiles
240513_122304:cmsbot_crab_whitelist
240513_122305:cmsbot_crab_blacklist
240513_122306:cmsbot_crab_ignoreGlobalBlacklist
240513_122307:cmsbot_crab_voRole
240513_122308:cmsbot_crab_voGroup
240513_122309:cmsbot_crab_scheddName
240513_122310:cmsbot_crab_collector
240513_122312:cmsbot_crab_extraJDL
```

Finished at: 2024-05-13 14:23:13
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/775/console)

## Comment (cmsdmwmbot, 2024-05-13T12:49:16Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-13 14:49:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1054/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240513_122245:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskFile-check.sh 240513_122256:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240513_122257:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240513_122300:cmsbot_crab_runRange - 2
whitelist-check.sh 240513_122304:cmsbot_crab_whitelist - 2
blacklist-check.sh 240513_122305:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240513_122234:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240513_122236:cmsbot_crab_transferLogs - 0
activity-check.sh 240513_122237:cmsbot_crab_activity - 0
inputFiles-check.sh 240513_122238:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240513_122239:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240513_122240:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240513_122242:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240513_122243:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 240513_122246:cmsbot_crab_numCores - 0
scriptExe-check.sh 240513_122247:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240513_122249:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240513_122250:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240513_122251:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240513_122252:cmsbot_crab_inputDBS - 0
useParent-check.sh 240513_122254:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240513_122255:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240513_122259:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240513_122301:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240513_122302:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240513_122306:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240513_122307:cmsbot_crab_voRole - 0
voGroup-check.sh 240513_122308:cmsbot_crab_voGroup - 0
scheddName-check.sh 240513_122309:cmsbot_crab_scheddName - 0
collector-check.sh 240513_122310:cmsbot_crab_collector - 0
extraJDL-check.sh 240513_122312:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-13T13:13:11Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-05-13 15:13:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1055/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240513_122245:cmsbot_crab_maxJobRuntimeMin - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240513_122234:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240513_122236:cmsbot_crab_transferLogs - 0
activity-check.sh 240513_122237:cmsbot_crab_activity - 0
inputFiles-check.sh 240513_122238:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240513_122239:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240513_122240:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240513_122242:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240513_122243:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 240513_122246:cmsbot_crab_numCores - 0
scriptExe-check.sh 240513_122247:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240513_122249:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240513_122250:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240513_122251:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240513_122252:cmsbot_crab_inputDBS - 0
useParent-check.sh 240513_122254:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240513_122255:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240513_122256:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240513_122257:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240513_122259:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240513_122300:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240513_122301:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240513_122302:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240513_122304:cmsbot_crab_whitelist - 0
blacklist-check.sh 240513_122305:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240513_122306:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240513_122307:cmsbot_crab_voRole - 0
voGroup-check.sh 240513_122308:cmsbot_crab_voGroup - 0
scheddName-check.sh 240513_122309:cmsbot_crab_scheddName - 0
collector-check.sh 240513_122310:cmsbot_crab_collector - 0
extraJDL-check.sh 240513_122312:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-13T13:37:30Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-05-13 15:37:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1056/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240513_122234:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240513_122236:cmsbot_crab_transferLogs - 0
activity-check.sh 240513_122237:cmsbot_crab_activity - 0
inputFiles-check.sh 240513_122238:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240513_122239:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240513_122240:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240513_122242:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240513_122243:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240513_122245:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240513_122246:cmsbot_crab_numCores - 0
scriptExe-check.sh 240513_122247:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240513_122249:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240513_122250:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240513_122251:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240513_122252:cmsbot_crab_inputDBS - 0
useParent-check.sh 240513_122254:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240513_122255:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240513_122256:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240513_122257:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240513_122259:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240513_122300:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240513_122301:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240513_122302:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240513_122304:cmsbot_crab_whitelist - 0
blacklist-check.sh 240513_122305:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240513_122306:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240513_122307:cmsbot_crab_voRole - 0
voGroup-check.sh 240513_122308:cmsbot_crab_voGroup - 0
scheddName-check.sh 240513_122309:cmsbot_crab_scheddName - 0
collector-check.sh 240513_122310:cmsbot_crab_collector - 0
extraJDL-check.sh 240513_122312:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
