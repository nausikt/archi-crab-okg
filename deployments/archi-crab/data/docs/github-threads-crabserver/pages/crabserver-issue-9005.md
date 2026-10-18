# dmwm/CRABServer issue #9005: #952: Test dev CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2025-03-19T14:59:09Z
Closed: 2025-03-31T08:31:23Z
URL: https://github.com/dmwm/CRABServer/issues/9005

## Opening post (cmsdmwmbot, 2025-03-19T14:59:09Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2025-03-19 15:59:08
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/952/)

## Comment (cmsdmwmbot, 2025-03-19T15:01:46Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_145951:cmsbot_crab_20250319_155945
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_145954:cmsbot_crab_transferOutputs
250319_145957:cmsbot_crab_transferLogs
250319_150000:cmsbot_crab_activity
250319_150005:cmsbot_crab_inputFiles
250319_150008:cmsbot_crab_disableAutomaticOutputCollection
250319_150013:cmsbot_crab_outputFiles
250319_150016:cmsbot_crab_allowUndistributedCMSSW
250319_150019:cmsbot_crab_maxMemoryMB
250319_150022:cmsbot_crab_maxJobRuntimeMin
250319_150027:cmsbot_crab_numCores
250319_150030:cmsbot_crab_scriptExe
250319_150033:cmsbot_crab_scriptArgs
250319_150038:cmsbot_crab_sendVenvFolder
250319_150043:cmsbot_crab_sendExternalFolder
250319_150044:cmsbot_crab_inputDBS
250319_150047:cmsbot_crab_useParent
250319_150050:cmsbot_crab_secondaryInputDataset
250319_150053:cmsbot_crab_lumiMaskFile
250319_150057:cmsbot_crab_outLFNDirBase
250319_150058:cmsbot_crab_runRange
250319_150101:cmsbot_crab_ignoreLocality
250319_150101:cmsbot_crab_userInputFiles
250319_150104:cmsbot_crab_whitelist
250319_150107:cmsbot_crab_blacklist
250319_150110:cmsbot_crab_ignoreGlobalBlacklist
250319_150113:cmsbot_crab_voRole
250319_150116:cmsbot_crab_voGroup
250319_150119:cmsbot_crab_scheddName
250319_150121:cmsbot_crab_collector
250319_150124:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 16:01:25
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/952/console)

## Comment (cmsdmwmbot, 2025-03-19T15:23:09Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-03-19 16:23:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/617/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/617//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-03-19T15:23:22Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2025-03-19 16:23:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1285/console

```
SUCCESSFUL TESTS:
outputFiles-check.sh 250319_150013:cmsbot_crab_outputFiles - 0
inputDBS-check.sh 250319_150044:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 250319_150050:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_150053:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 250319_150057:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_150058:cmsbot_crab_runRange - 0
userInputFiles-check.sh 250319_150101:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_150104:cmsbot_crab_whitelist - 0

FAILED TESTS:
transferOutputs-check.sh 250319_145954:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 250319_145957:cmsbot_crab_transferLogs - 1
activity-check.sh 250319_150000:cmsbot_crab_activity - 1
inputFiles-check.sh 250319_150005:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 250319_150008:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 250319_150016:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 250319_150019:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 250319_150022:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 250319_150027:cmsbot_crab_numCores - 1
scriptExe-check.sh 250319_150030:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250319_150033:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 250319_150038:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 250319_150043:cmsbot_crab_sendExternalFolder - 1
useParent-check.sh 250319_150047:cmsbot_crab_useParent - 1
ignoreLocality-check.sh 250319_150101:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 250319_150107:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 250319_150110:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 250319_150113:cmsbot_crab_voRole - 1
voGroup-check.sh 250319_150116:cmsbot_crab_voGroup - 1
scheddName-check.sh 250319_150119:cmsbot_crab_scheddName - 1
collector-check.sh 250319_150121:cmsbot_crab_collector - 1
extraJDL-check.sh 250319_150124:cmsbot_crab_extraJDL - 1

RETRY TESTS:
 none
```
