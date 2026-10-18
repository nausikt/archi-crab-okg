# dmwm/CRABServer issue #8602: #825: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-09T15:21:12Z
Closed: 2024-08-09T21:39:39Z
URL: https://github.com/dmwm/CRABServer/issues/8602

## Opening post (cmsdmwmbot, 2024-08-09T15:21:12Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-08-09 17:21:11
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/825/)

## Comment (cmsdmwmbot, 2024-08-09T15:23:04Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240809_152136:cmsbot_crab_transferOutputs
240809_152138:cmsbot_crab_transferLogs
240809_152141:cmsbot_crab_activity
240809_152143:cmsbot_crab_inputFiles
240809_152145:cmsbot_crab_disableAutomaticOutputCollection
240809_152147:cmsbot_crab_outputFiles
240809_152149:cmsbot_crab_allowUndistributedCMSSW
240809_152152:cmsbot_crab_maxMemoryMB
240809_152154:cmsbot_crab_maxJobRuntimeMin
240809_152156:cmsbot_crab_numCores
240809_152158:cmsbot_crab_scriptExe
240809_152200:cmsbot_crab_scriptArgs
240809_152203:cmsbot_crab_sendVenvFolder
240809_152205:cmsbot_crab_sendExternalFolder
240809_152207:cmsbot_crab_inputDBS
240809_152209:cmsbot_crab_useParent
240809_152211:cmsbot_crab_secondaryInputDataset
240809_152213:cmsbot_crab_lumiMaskFile
240809_152216:cmsbot_crab_lumiMaskUrl
240809_152219:cmsbot_crab_outLFNDirBase
240809_152221:cmsbot_crab_runRange
240809_152223:cmsbot_crab_ignoreLocality
240809_152225:cmsbot_crab_userInputFiles
240809_152227:cmsbot_crab_whitelist
240809_152229:cmsbot_crab_blacklist
240809_152231:cmsbot_crab_ignoreGlobalBlacklist
240809_152234:cmsbot_crab_voRole
240809_152236:cmsbot_crab_voGroup
240809_152238:cmsbot_crab_scheddName
240809_152240:cmsbot_crab_collector
240809_152242:cmsbot_crab_extraJDL
```

Finished at: 2024-08-09 17:22:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/825/console)

## Comment (cmsdmwmbot, 2024-08-09T15:46:16Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-08-09 17:46:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1151/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
scheddName-check.sh 240809_152238:cmsbot_crab_scheddName - 0

FAILED TESTS:
transferOutputs-check.sh 240809_152136:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240809_152138:cmsbot_crab_transferLogs - 1
activity-check.sh 240809_152141:cmsbot_crab_activity - 1
inputFiles-check.sh 240809_152143:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240809_152145:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240809_152147:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240809_152149:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240809_152152:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240809_152154:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240809_152156:cmsbot_crab_numCores - 1
scriptExe-check.sh 240809_152158:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240809_152200:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240809_152203:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240809_152205:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240809_152207:cmsbot_crab_inputDBS - 1
useParent-check.sh 240809_152209:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240809_152211:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240809_152213:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240809_152216:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240809_152219:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240809_152221:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240809_152223:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240809_152225:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240809_152227:cmsbot_crab_whitelist - 1
blacklist-check.sh 240809_152229:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240809_152231:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240809_152234:cmsbot_crab_voRole - 1
voGroup-check.sh 240809_152236:cmsbot_crab_voGroup - 1
collector-check.sh 240809_152240:cmsbot_crab_collector - 1
extraJDL-check.sh 240809_152242:cmsbot_crab_extraJDL - 1
```

## Comment (belforte, 2024-08-09T17:24:07Z)

well.. failure here is expected since tasks are not constrained to run on the only scheduler (059) which supports V2 bindings
