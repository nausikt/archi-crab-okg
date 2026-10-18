# dmwm/CRABServer issue #8830: #896: Test GH CRABClient using preprod REST instance and CMSSW_12_5_0 CMSSW release

State: closed
Opened: 2024-11-25T22:13:01Z
Closed: 2024-11-26T08:42:17Z
URL: https://github.com/dmwm/CRABServer/issues/8830

## Opening post (cmsdmwmbot, 2024-11-25T22:13:01Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_5_0**
- SCRAM_ARCH: **el8_amd64_gcc10**
- CRABServer_tag: **v3.241125**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-11-25 23:13:00
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/896/)

## Comment (cmsdmwmbot, 2024-11-25T22:15:55Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241125_221344:cmsbot_crab_transferOutputs
241125_221347:cmsbot_crab_transferLogs
241125_221350:cmsbot_crab_activity
241125_221355:cmsbot_crab_inputFiles
241125_221358:cmsbot_crab_disableAutomaticOutputCollection
241125_221402:cmsbot_crab_outputFiles
241125_221406:cmsbot_crab_allowUndistributedCMSSW
241125_221409:cmsbot_crab_maxMemoryMB
241125_221412:cmsbot_crab_maxJobRuntimeMin
241125_221416:cmsbot_crab_numCores
241125_221420:cmsbot_crab_scriptExe
241125_221423:cmsbot_crab_scriptArgs
241125_221433:cmsbot_crab_sendVenvFolder
241125_221437:cmsbot_crab_sendExternalFolder
241125_221440:cmsbot_crab_inputDBS
241125_221444:cmsbot_crab_useParent
241125_221447:cmsbot_crab_secondaryInputDataset
241125_221450:cmsbot_crab_lumiMaskFile
241125_221454:cmsbot_crab_lumiMaskUrl
241125_221458:cmsbot_crab_outLFNDirBase
241125_221501:cmsbot_crab_runRange
241125_221504:cmsbot_crab_ignoreLocality
241125_221507:cmsbot_crab_userInputFiles
241125_221511:cmsbot_crab_whitelist
241125_221514:cmsbot_crab_blacklist
241125_221517:cmsbot_crab_ignoreGlobalBlacklist
241125_221520:cmsbot_crab_voRole
241125_221524:cmsbot_crab_voGroup
241125_221527:cmsbot_crab_scheddName
241125_221530:cmsbot_crab_collector
241125_221533:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241125_221340:cmsbot_crab_20241125_231337
```

Finished at: 2024-11-25 23:15:34
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/896/console)

## Comment (cmsdmwmbot, 2024-11-25T22:39:52Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-25 23:39:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1241/console

```
RETRY TESTS:
transferLogs-check.sh 241125_221347:cmsbot_crab_transferLogs - 2
activity-check.sh 241125_221350:cmsbot_crab_activity - 2
outputFiles-check.sh 241125_221402:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 241125_221409:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 241125_221412:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241125_221416:cmsbot_crab_numCores - 2
scriptExe-check.sh 241125_221420:cmsbot_crab_scriptExe - 2
secondaryInputDataset-check.sh 241125_221447:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 241125_221454:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241125_221458:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241125_221501:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241125_221507:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241125_221511:cmsbot_crab_whitelist - 2
blacklist-check.sh 241125_221514:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241125_221517:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241125_221520:cmsbot_crab_voRole - 2
voGroup-check.sh 241125_221524:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_221344:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241125_221355:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_221358:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241125_221406:cmsbot_crab_allowUndistributedCMSSW - 0
scriptArgs-check.sh 241125_221423:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_221433:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_221437:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_221440:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_221444:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 241125_221450:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 241125_221504:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 241125_221527:cmsbot_crab_scheddName - 0
collector-check.sh 241125_221530:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_221533:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-25T22:39:58Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-25 23:39:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/575/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/575//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241125_231337  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'finished', 'killed', 'failed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241125_231337/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241125_221340:cmsbot_crab_20241125_231337  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241125_231337/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'killed', 'finished'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241125_231337/crab.log
```

## Comment (cmsdmwmbot, 2024-11-25T23:06:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-11-26 00:06:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1245/console

```
RETRY TESTS:
runRange-check.sh 241125_221501:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241125_221507:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241125_221511:cmsbot_crab_whitelist - 2
blacklist-check.sh 241125_221514:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241125_221517:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_221344:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_221347:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_221350:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_221355:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_221358:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241125_221402:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241125_221406:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_221409:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241125_221412:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241125_221416:cmsbot_crab_numCores - 0
scriptExe-check.sh 241125_221420:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_221423:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_221433:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_221437:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_221440:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_221444:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_221447:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_221450:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241125_221454:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241125_221458:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 241125_221504:cmsbot_crab_ignoreLocality - 0
voRole-check.sh 241125_221520:cmsbot_crab_voRole - 0
voGroup-check.sh 241125_221524:cmsbot_crab_voGroup - 0
scheddName-check.sh 241125_221527:cmsbot_crab_scheddName - 0
collector-check.sh 241125_221530:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_221533:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-25T23:32:12Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-11-26 00:32:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1248/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_221344:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_221347:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_221350:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_221355:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_221358:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241125_221402:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241125_221406:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_221409:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241125_221412:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241125_221416:cmsbot_crab_numCores - 0
scriptExe-check.sh 241125_221420:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_221423:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_221433:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_221437:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_221440:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_221444:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_221447:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_221450:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241125_221454:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241125_221458:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241125_221501:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241125_221504:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241125_221507:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241125_221511:cmsbot_crab_whitelist - 0
blacklist-check.sh 241125_221514:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241125_221517:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241125_221520:cmsbot_crab_voRole - 0
voGroup-check.sh 241125_221524:cmsbot_crab_voGroup - 0
scheddName-check.sh 241125_221527:cmsbot_crab_scheddName - 0
collector-check.sh 241125_221530:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_221533:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
