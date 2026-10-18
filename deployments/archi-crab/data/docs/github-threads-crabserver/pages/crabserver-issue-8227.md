# dmwm/CRABServer issue #8227: #707: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-02-02T17:12:03Z
Closed: 2024-02-03T18:09:28Z
URL: https://github.com/dmwm/CRABServer/issues/8227

## Opening post (cmsdmwmbot, 2024-02-02T17:12:03Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-02-02 18:12:02
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/707/)

## Comment (cmsdmwmbot, 2024-02-02T17:13:24Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_171225:cmsbot_crab_transferOutputs
240202_171232:cmsbot_crab_transferLogs
240202_171233:cmsbot_crab_activity
240202_171233:cmsbot_crab_inputFiles
240202_171235:cmsbot_crab_disableAutomaticOutputCollection
240202_171236:cmsbot_crab_outputFiles
240202_171236:cmsbot_crab_allowUndistributedCMSSW
240202_171237:cmsbot_crab_maxMemoryMB
240202_171238:cmsbot_crab_maxJobRuntimeMin
240202_171239:cmsbot_crab_numCores
240202_171240:cmsbot_crab_scriptExe
240202_171241:cmsbot_crab_scriptArgs
240202_171242:cmsbot_crab_sendVenvFolder
240202_171246:cmsbot_crab_sendExternalFolder
240202_171247:cmsbot_crab_inputDBS
240202_171248:cmsbot_crab_useParent
240202_171249:cmsbot_crab_secondaryInputDataset
240202_171249:cmsbot_crab_lumiMaskFile
240202_171250:cmsbot_crab_lumiMaskUrl
240202_171252:cmsbot_crab_outLFNDirBase
240202_171253:cmsbot_crab_runRange
240202_171254:cmsbot_crab_ignoreLocality
240202_171255:cmsbot_crab_userInputFiles
240202_171256:cmsbot_crab_whitelist
240202_171257:cmsbot_crab_blacklist
240202_171258:cmsbot_crab_ignoreGlobalBlacklist
240202_171258:cmsbot_crab_voRole
240202_171259:cmsbot_crab_voGroup
240202_171300:cmsbot_crab_scheddName
240202_171301:cmsbot_crab_collector
240202_171302:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 18:13:03
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/707/console)

## Comment (cmsdmwmbot, 2024-02-02T17:36:41Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 18:36:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/940/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240202_171238:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240202_171239:cmsbot_crab_numCores - 2
scriptExe-check.sh 240202_171240:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240202_171241:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240202_171250:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240202_171253:cmsbot_crab_runRange - 2
whitelist-check.sh 240202_171256:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_171257:cmsbot_crab_blacklist - 2
voGroup-check.sh 240202_171259:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_171225:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_171232:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_171233:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_171233:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_171235:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_171236:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_171236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_171237:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240202_171242:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_171246:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_171247:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_171248:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_171249:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_171249:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240202_171252:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240202_171254:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_171255:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240202_171258:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_171258:cmsbot_crab_voRole - 0
scheddName-check.sh 240202_171300:cmsbot_crab_scheddName - 0
collector-check.sh 240202_171301:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_171302:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T17:59:43Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-02-02 18:59:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/943/console

```
RETRY TESTS:
blacklist-check.sh 240202_171257:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_171225:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_171232:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_171233:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_171233:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_171235:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_171236:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_171236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_171237:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_171238:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_171239:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_171240:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_171241:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_171242:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_171246:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_171247:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_171248:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_171249:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_171249:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_171250:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_171252:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_171253:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_171254:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_171255:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_171256:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240202_171258:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_171258:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_171259:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_171300:cmsbot_crab_scheddName - 0
collector-check.sh 240202_171301:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_171302:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T18:23:44Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-02-02 19:23:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/947/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_171225:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_171232:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_171233:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_171233:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_171235:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_171236:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_171236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_171237:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_171238:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_171239:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_171240:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_171241:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_171242:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_171246:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_171247:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_171248:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_171249:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_171249:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_171250:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_171252:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_171253:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_171254:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_171255:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_171256:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_171257:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_171258:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_171258:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_171259:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_171300:cmsbot_crab_scheddName - 0
collector-check.sh 240202_171301:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_171302:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
