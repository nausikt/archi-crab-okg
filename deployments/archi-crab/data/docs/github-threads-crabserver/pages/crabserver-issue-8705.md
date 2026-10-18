# dmwm/CRABServer issue #8705: #833: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-20T10:51:05Z
Closed: 2024-09-20T12:19:52Z
URL: https://github.com/dmwm/CRABServer/issues/8705

## Opening post (cmsdmwmbot, 2024-09-20T10:51:05Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-09-20 12:51:04
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/833/)

## Comment (cmsdmwmbot, 2024-09-20T10:53:37Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240920_105149:cmsbot_crab_transferOutputs
240920_105151:cmsbot_crab_transferLogs
240920_105154:cmsbot_crab_activity
240920_105157:cmsbot_crab_inputFiles
240920_105200:cmsbot_crab_disableAutomaticOutputCollection
240920_105203:cmsbot_crab_outputFiles
240920_105206:cmsbot_crab_allowUndistributedCMSSW
240920_105209:cmsbot_crab_maxMemoryMB
240920_105212:cmsbot_crab_maxJobRuntimeMin
240920_105215:cmsbot_crab_numCores
240920_105218:cmsbot_crab_scriptExe
240920_105221:cmsbot_crab_scriptArgs
240920_105224:cmsbot_crab_sendVenvFolder
240920_105227:cmsbot_crab_sendExternalFolder
240920_105229:cmsbot_crab_inputDBS
240920_105232:cmsbot_crab_useParent
240920_105235:cmsbot_crab_secondaryInputDataset
240920_105238:cmsbot_crab_lumiMaskFile
240920_105241:cmsbot_crab_lumiMaskUrl
240920_105244:cmsbot_crab_outLFNDirBase
240920_105247:cmsbot_crab_runRange
240920_105250:cmsbot_crab_ignoreLocality
240920_105252:cmsbot_crab_userInputFiles
240920_105255:cmsbot_crab_whitelist
240920_105258:cmsbot_crab_blacklist
240920_105301:cmsbot_crab_ignoreGlobalBlacklist
240920_105304:cmsbot_crab_voRole
240920_105307:cmsbot_crab_voGroup
240920_105309:cmsbot_crab_scheddName
240920_105312:cmsbot_crab_collector
240920_105315:cmsbot_crab_extraJDL
```

Finished at: 2024-09-20 12:53:16
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/833/console)

## Comment (cmsdmwmbot, 2024-09-20T11:17:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-20 13:17:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1171/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240920_105212:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240920_105215:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240920_105221:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240920_105232:cmsbot_crab_useParent - 2
lumiMaskFile-check.sh 240920_105238:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240920_105241:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240920_105247:cmsbot_crab_runRange - 2
whitelist-check.sh 240920_105255:cmsbot_crab_whitelist - 2
blacklist-check.sh 240920_105258:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_105149:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_105151:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_105154:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_105157:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240920_105200:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240920_105203:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_105206:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240920_105209:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240920_105218:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240920_105224:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_105227:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_105229:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240920_105235:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240920_105244:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240920_105250:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_105252:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240920_105301:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240920_105304:cmsbot_crab_voRole - 0
voGroup-check.sh 240920_105307:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_105309:cmsbot_crab_scheddName - 0
collector-check.sh 240920_105312:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_105315:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-09-20T11:42:16Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-09-20 13:42:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1172/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_105149:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_105151:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_105154:cmsbot_crab_activity - 0
inputFiles-check.sh 240920_105157:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240920_105200:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240920_105203:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240920_105206:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240920_105209:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240920_105212:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240920_105215:cmsbot_crab_numCores - 0
scriptExe-check.sh 240920_105218:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240920_105221:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240920_105224:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_105227:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240920_105229:cmsbot_crab_inputDBS - 0
useParent-check.sh 240920_105232:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240920_105235:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240920_105238:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240920_105241:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240920_105244:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240920_105247:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240920_105250:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240920_105252:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240920_105255:cmsbot_crab_whitelist - 0
blacklist-check.sh 240920_105258:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240920_105301:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240920_105304:cmsbot_crab_voRole - 0
voGroup-check.sh 240920_105307:cmsbot_crab_voGroup - 0
scheddName-check.sh 240920_105309:cmsbot_crab_scheddName - 0
collector-check.sh 240920_105312:cmsbot_crab_collector - 0
extraJDL-check.sh 240920_105315:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-09-20T12:19:52Z)

OK
