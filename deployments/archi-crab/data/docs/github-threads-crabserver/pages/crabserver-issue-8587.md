# dmwm/CRABServer issue #8587: #819: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-06T14:50:50Z
Closed: 2024-08-06T15:37:35Z
URL: https://github.com/dmwm/CRABServer/issues/8587

## Opening post (cmsdmwmbot, 2024-08-06T14:50:50Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-08-06 16:50:49
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/819/)

## Comment (cmsdmwmbot, 2024-08-06T14:52:37Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240806_145110:cmsbot_crab_transferOutputs
240806_145112:cmsbot_crab_transferLogs
240806_145114:cmsbot_crab_activity
240806_145116:cmsbot_crab_inputFiles
240806_145118:cmsbot_crab_disableAutomaticOutputCollection
240806_145121:cmsbot_crab_outputFiles
240806_145123:cmsbot_crab_allowUndistributedCMSSW
240806_145125:cmsbot_crab_maxMemoryMB
240806_145127:cmsbot_crab_maxJobRuntimeMin
240806_145129:cmsbot_crab_numCores
240806_145132:cmsbot_crab_scriptExe
240806_145134:cmsbot_crab_scriptArgs
240806_145136:cmsbot_crab_sendVenvFolder
240806_145138:cmsbot_crab_sendExternalFolder
240806_145140:cmsbot_crab_inputDBS
240806_145142:cmsbot_crab_useParent
240806_145144:cmsbot_crab_secondaryInputDataset
240806_145146:cmsbot_crab_lumiMaskFile
240806_145149:cmsbot_crab_lumiMaskUrl
240806_145151:cmsbot_crab_outLFNDirBase
240806_145154:cmsbot_crab_runRange
240806_145156:cmsbot_crab_ignoreLocality
240806_145158:cmsbot_crab_userInputFiles
240806_145200:cmsbot_crab_whitelist
240806_145202:cmsbot_crab_blacklist
240806_145204:cmsbot_crab_ignoreGlobalBlacklist
240806_145206:cmsbot_crab_voRole
240806_145208:cmsbot_crab_voGroup
240806_145210:cmsbot_crab_scheddName
240806_145212:cmsbot_crab_collector
240806_145215:cmsbot_crab_extraJDL
```

Finished at: 2024-08-06 16:52:15
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/819/console)

## Comment (cmsdmwmbot, 2024-08-06T15:16:22Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-08-06 17:16:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1142/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 240806_145110:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240806_145112:cmsbot_crab_transferLogs - 1
activity-check.sh 240806_145114:cmsbot_crab_activity - 1
inputFiles-check.sh 240806_145116:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240806_145118:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240806_145121:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240806_145123:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240806_145125:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240806_145127:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240806_145129:cmsbot_crab_numCores - 1
scriptExe-check.sh 240806_145132:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240806_145134:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240806_145136:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240806_145138:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240806_145140:cmsbot_crab_inputDBS - 1
useParent-check.sh 240806_145142:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240806_145144:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240806_145146:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240806_145149:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240806_145151:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240806_145154:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240806_145156:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240806_145158:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240806_145200:cmsbot_crab_whitelist - 1
blacklist-check.sh 240806_145202:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240806_145204:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240806_145206:cmsbot_crab_voRole - 1
voGroup-check.sh 240806_145208:cmsbot_crab_voGroup - 1
scheddName-check.sh 240806_145210:cmsbot_crab_scheddName - 1
collector-check.sh 240806_145212:cmsbot_crab_collector - 1
extraJDL-check.sh 240806_145215:cmsbot_crab_extraJDL - 1
```

## Comment (belforte, 2024-08-06T15:37:35Z)

:-1:
