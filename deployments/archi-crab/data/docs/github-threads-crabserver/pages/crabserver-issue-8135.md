# dmwm/CRABServer issue #8135: #646: Test dev CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2023-12-20T13:32:02Z
Closed: 2023-12-20T17:04:46Z
URL: https://github.com/dmwm/CRABServer/issues/8135

## Opening post (cmsdmwmbot, 2023-12-20T13:32:02Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-12-20 14:32:01
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/646/)

## Comment (cmsdmwmbot, 2023-12-20T13:33:08Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231220_133214:cmsbot_crab_transferOutputs
231220_133215:cmsbot_crab_transferLogs
231220_133216:cmsbot_crab_activity
231220_133217:cmsbot_crab_inputFiles
231220_133218:cmsbot_crab_disableAutomaticOutputCollection
231220_133219:cmsbot_crab_outputFiles
231220_133220:cmsbot_crab_allowUndistributedCMSSW
231220_133221:cmsbot_crab_maxMemoryMB
231220_133221:cmsbot_crab_maxJobRuntimeMin
231220_133223:cmsbot_crab_numCores
231220_133224:cmsbot_crab_scriptExe
231220_133225:cmsbot_crab_scriptArgs
231220_133226:cmsbot_crab_sendVenvFolder
231220_133228:cmsbot_crab_sendExternalFolder
231220_133229:cmsbot_crab_inputDBS
231220_133230:cmsbot_crab_useParent
231220_133231:cmsbot_crab_secondaryInputDataset
231220_133232:cmsbot_crab_lumiMaskFile
231220_133233:cmsbot_crab_lumiMaskUrl
231220_133235:cmsbot_crab_outLFNDirBase
231220_133236:cmsbot_crab_runRange
231220_133237:cmsbot_crab_ignoreLocality
231220_133238:cmsbot_crab_userInputFiles
231220_133239:cmsbot_crab_whitelist
231220_133240:cmsbot_crab_blacklist
231220_133241:cmsbot_crab_ignoreGlobalBlacklist
231220_133242:cmsbot_crab_voRole
231220_133243:cmsbot_crab_voGroup
231220_133244:cmsbot_crab_scheddName
231220_133245:cmsbot_crab_collector
231220_133246:cmsbot_crab_extraJDL
```

Finished at: 2023-12-20 14:32:46
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/646/console)

## Comment (cmsdmwmbot, 2023-12-20T13:54:22Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-20 14:54:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/831/console

```
RETRY TESTS:
activity-check.sh 231220_133216:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 231220_133221:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 231220_133221:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 231220_133223:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 231220_133233:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 231220_133236:cmsbot_crab_runRange - 2
whitelist-check.sh 231220_133239:cmsbot_crab_whitelist - 2
blacklist-check.sh 231220_133240:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_133214:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231220_133215:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 231220_133217:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_133218:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_133219:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_133220:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 231220_133224:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231220_133225:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231220_133226:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_133228:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_133229:cmsbot_crab_inputDBS - 0
useParent-check.sh 231220_133230:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231220_133231:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_133232:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 231220_133235:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 231220_133237:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_133238:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 231220_133241:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231220_133242:cmsbot_crab_voRole - 0
voGroup-check.sh 231220_133243:cmsbot_crab_voGroup - 0
scheddName-check.sh 231220_133244:cmsbot_crab_scheddName - 0
collector-check.sh 231220_133245:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_133246:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-12-20T14:55:55Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 0. Test is done.
**Finished at:** 2023-12-20 15:55:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/839/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 231220_133214:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 231220_133215:cmsbot_crab_transferLogs - 0
activity-check.sh 231220_133216:cmsbot_crab_activity - 0
inputFiles-check.sh 231220_133217:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 231220_133218:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 231220_133219:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 231220_133220:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 231220_133221:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 231220_133221:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 231220_133223:cmsbot_crab_numCores - 0
scriptExe-check.sh 231220_133224:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 231220_133225:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 231220_133226:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 231220_133228:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 231220_133229:cmsbot_crab_inputDBS - 0
useParent-check.sh 231220_133230:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 231220_133231:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 231220_133232:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 231220_133233:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 231220_133235:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 231220_133236:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 231220_133237:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 231220_133238:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 231220_133239:cmsbot_crab_whitelist - 0
blacklist-check.sh 231220_133240:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 231220_133241:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 231220_133242:cmsbot_crab_voRole - 0
voGroup-check.sh 231220_133243:cmsbot_crab_voGroup - 0
scheddName-check.sh 231220_133244:cmsbot_crab_scheddName - 0
collector-check.sh 231220_133245:cmsbot_crab_collector - 0
extraJDL-check.sh 231220_133246:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
