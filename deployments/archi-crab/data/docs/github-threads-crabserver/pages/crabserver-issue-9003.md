# dmwm/CRABServer issue #9003: #950: Test dev CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2025-03-19T14:49:30Z
Closed: 2025-03-19T16:04:11Z
URL: https://github.com/dmwm/CRABServer/issues/9003

## Opening post (cmsdmwmbot, 2025-03-19T14:49:30Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2025-03-19 15:49:29
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/950/)

## Comment (cmsdmwmbot, 2025-03-19T14:51:00Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_145001:cmsbot_crab_20250319_154958
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_145002:cmsbot_crab_transferOutputs
250319_145003:cmsbot_crab_transferLogs
250319_145003:cmsbot_crab_activity
250319_145006:cmsbot_crab_inputFiles
250319_145007:cmsbot_crab_disableAutomaticOutputCollection
250319_145010:cmsbot_crab_outputFiles
250319_145011:cmsbot_crab_allowUndistributedCMSSW
250319_145012:cmsbot_crab_maxMemoryMB
250319_145012:cmsbot_crab_maxJobRuntimeMin
250319_145015:cmsbot_crab_numCores
250319_145016:cmsbot_crab_scriptExe
250319_145017:cmsbot_crab_scriptArgs
250319_145022:cmsbot_crab_sendVenvFolder
250319_145025:cmsbot_crab_sendExternalFolder
250319_145026:cmsbot_crab_inputDBS
250319_145026:cmsbot_crab_useParent
250319_145027:cmsbot_crab_secondaryInputDataset
250319_145028:cmsbot_crab_lumiMaskFile
250319_145029:cmsbot_crab_lumiMaskUrl
250319_145030:cmsbot_crab_outLFNDirBase
250319_145031:cmsbot_crab_runRange
250319_145032:cmsbot_crab_ignoreLocality
250319_145032:cmsbot_crab_userInputFiles
250319_145033:cmsbot_crab_whitelist
250319_145034:cmsbot_crab_blacklist
250319_145034:cmsbot_crab_ignoreGlobalBlacklist
250319_145035:cmsbot_crab_voRole
250319_145036:cmsbot_crab_voGroup
250319_145037:cmsbot_crab_scheddName
250319_145037:cmsbot_crab_collector
250319_145038:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 15:50:38
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/950/console)

## Comment (cmsdmwmbot, 2025-03-19T15:12:45Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-03-19 16:12:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1283/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250319_145002:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250319_145003:cmsbot_crab_transferLogs - 0
activity-check.sh 250319_145003:cmsbot_crab_activity - 0
inputFiles-check.sh 250319_145006:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250319_145007:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250319_145010:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250319_145011:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250319_145012:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250319_145012:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250319_145015:cmsbot_crab_numCores - 0
scriptExe-check.sh 250319_145016:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250319_145017:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250319_145022:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250319_145025:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250319_145026:cmsbot_crab_inputDBS - 0
useParent-check.sh 250319_145026:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250319_145027:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_145028:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250319_145029:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250319_145030:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_145031:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250319_145032:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250319_145032:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_145033:cmsbot_crab_whitelist - 0
blacklist-check.sh 250319_145034:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250319_145034:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250319_145035:cmsbot_crab_voRole - 0
voGroup-check.sh 250319_145036:cmsbot_crab_voGroup - 0
scheddName-check.sh 250319_145037:cmsbot_crab_scheddName - 0
collector-check.sh 250319_145037:cmsbot_crab_collector - 0
extraJDL-check.sh 250319_145038:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```

## Comment (cmsdmwmbot, 2025-03-19T15:12:52Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2025-03-19 16:12:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/615/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/615//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=250319_145001:cmsbot_crab_20250319_154958  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20250319_154958/.requestcache not created, because it already exists.
Collecting information about original task ...
The server answered with an error.
Server answered with: Execution error
Reason is: You cannot kill a task if it is in the QUEUED status
Error Id: 5436557501f9ac496c9b006b5b6ebd46
```

## Comment (nausikt, 2025-03-19T15:21:59Z)

Failed because in QUEUED? may be wait a little and retry later

## Comment (nausikt, 2025-03-19T16:04:12Z)

Succeed by retry. #9007

## Comment (belforte, 2025-03-19T17:01:25Z)

something is wrong here. That task was transferrring output, so in SUBMITTED status, not QUEUED.
I suspect that the `crab recover` command does now wait enough after issuing the `kill` command and taks was QUEUED because the TW had to process the kill command.

Of course it only happens when the TW is full of work todo. But at the very least output should be more clear.

## Comment (belforte, 2025-03-19T17:36:22Z)

opened https://github.com/dmwm/CRABClient/issues/5381
