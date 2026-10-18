# dmwm/CRABServer issue #8778: #875: Test GH CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-08T11:31:51Z
Closed: 2024-11-08T13:52:09Z
URL: https://github.com/dmwm/CRABServer/issues/8778

## Opening post (cmsdmwmbot, 2024-11-08T11:31:51Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [ ] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-11-08 12:31:50
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/875/)

## Comment (cmsdmwmbot, 2024-11-08T11:34:24Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241108_113218:cmsbot_crab_transferOutputs
241108_113222:cmsbot_crab_transferLogs
241108_113225:cmsbot_crab_activity
241108_113229:cmsbot_crab_inputFiles
241108_113233:cmsbot_crab_disableAutomaticOutputCollection
241108_113236:cmsbot_crab_outputFiles
241108_113239:cmsbot_crab_allowUndistributedCMSSW
241108_113243:cmsbot_crab_maxMemoryMB
241108_113246:cmsbot_crab_maxJobRuntimeMin
241108_113249:cmsbot_crab_numCores
241108_113253:cmsbot_crab_scriptExe
241108_113256:cmsbot_crab_scriptArgs
241108_113300:cmsbot_crab_sendVenvFolder
241108_113303:cmsbot_crab_sendExternalFolder
241108_113307:cmsbot_crab_inputDBS
241108_113310:cmsbot_crab_useParent
241108_113314:cmsbot_crab_secondaryInputDataset
241108_113317:cmsbot_crab_lumiMaskFile
241108_113321:cmsbot_crab_lumiMaskUrl
241108_113325:cmsbot_crab_outLFNDirBase
241108_113328:cmsbot_crab_runRange
241108_113332:cmsbot_crab_ignoreLocality
241108_113335:cmsbot_crab_userInputFiles
241108_113338:cmsbot_crab_whitelist
241108_113342:cmsbot_crab_blacklist
241108_113345:cmsbot_crab_ignoreGlobalBlacklist
241108_113349:cmsbot_crab_voRole
241108_113352:cmsbot_crab_voGroup
241108_113355:cmsbot_crab_scheddName
241108_113359:cmsbot_crab_collector
241108_113402:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241108_113215:cmsbot_crab_20241108_123213
```

Finished at: 2024-11-08 12:34:03
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/875/console)

## Comment (cmsdmwmbot, 2024-11-08T11:57:53Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-08 12:57:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/568/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/568//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241108_123213  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'killed', 'failed', 'finished'}). You have dict_keys(['transferring', 'finished'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241108_123213/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241108_113215:cmsbot_crab_20241108_123213  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241108_123213/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'killed', 'failed', 'finished'}). You have dict_keys(['transferring', 'finished'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241108_123213/crab.log
```

## Comment (cmsdmwmbot, 2024-11-08T12:01:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-08 13:01:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1228/console

```
RETRY TESTS:
transferLogs-check.sh 241108_113222:cmsbot_crab_transferLogs - 2
activity-check.sh 241108_113225:cmsbot_crab_activity - 2
outputFiles-check.sh 241108_113236:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 241108_113246:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241108_113249:cmsbot_crab_numCores - 2
scriptExe-check.sh 241108_113253:cmsbot_crab_scriptExe - 2
useParent-check.sh 241108_113310:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 241108_113321:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241108_113325:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241108_113328:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 241108_113332:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 241108_113335:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241108_113338:cmsbot_crab_whitelist - 2
blacklist-check.sh 241108_113342:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241108_113345:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241108_113349:cmsbot_crab_voRole - 2
voGroup-check.sh 241108_113352:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241108_113218:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241108_113229:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241108_113233:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241108_113239:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241108_113243:cmsbot_crab_maxMemoryMB - 0
inputDBS-check.sh 241108_113307:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 241108_113314:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241108_113317:cmsbot_crab_lumiMaskFile - 0

FAILED TESTS:
scriptArgs-check.sh 241108_113256:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 241108_113300:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 241108_113303:cmsbot_crab_sendExternalFolder - 1
scheddName-check.sh 241108_113355:cmsbot_crab_scheddName - 1
collector-check.sh 241108_113359:cmsbot_crab_collector - 1
extraJDL-check.sh 241108_113402:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-11-08T12:26:18Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-11-08 13:26:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1230/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 241108_113321:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241108_113325:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241108_113328:cmsbot_crab_runRange - 2
whitelist-check.sh 241108_113338:cmsbot_crab_whitelist - 2
blacklist-check.sh 241108_113342:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241108_113218:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241108_113222:cmsbot_crab_transferLogs - 0
activity-check.sh 241108_113225:cmsbot_crab_activity - 0
inputFiles-check.sh 241108_113229:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241108_113233:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241108_113236:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241108_113239:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241108_113243:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241108_113246:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241108_113249:cmsbot_crab_numCores - 0
scriptExe-check.sh 241108_113253:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241108_113256:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241108_113300:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241108_113303:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241108_113307:cmsbot_crab_inputDBS - 0
useParent-check.sh 241108_113310:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241108_113314:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241108_113317:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 241108_113332:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241108_113335:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 241108_113345:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241108_113349:cmsbot_crab_voRole - 0
voGroup-check.sh 241108_113352:cmsbot_crab_voGroup - 0
scheddName-check.sh 241108_113355:cmsbot_crab_scheddName - 0
collector-check.sh 241108_113359:cmsbot_crab_collector - 0
extraJDL-check.sh 241108_113402:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-08T12:50:28Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-11-08 13:50:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1231/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241108_113218:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241108_113222:cmsbot_crab_transferLogs - 0
activity-check.sh 241108_113225:cmsbot_crab_activity - 0
inputFiles-check.sh 241108_113229:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241108_113233:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241108_113236:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241108_113239:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241108_113243:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241108_113246:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241108_113249:cmsbot_crab_numCores - 0
scriptExe-check.sh 241108_113253:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241108_113256:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241108_113300:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241108_113303:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241108_113307:cmsbot_crab_inputDBS - 0
useParent-check.sh 241108_113310:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241108_113314:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241108_113317:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241108_113321:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241108_113325:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241108_113328:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241108_113332:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241108_113335:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241108_113338:cmsbot_crab_whitelist - 0
blacklist-check.sh 241108_113342:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241108_113345:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241108_113349:cmsbot_crab_voRole - 0
voGroup-check.sh 241108_113352:cmsbot_crab_voGroup - 0
scheddName-check.sh 241108_113355:cmsbot_crab_scheddName - 0
collector-check.sh 241108_113359:cmsbot_crab_collector - 0
extraJDL-check.sh 241108_113402:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-11-08T13:52:09Z)

"usual" failure from recover when ran "too soon"
