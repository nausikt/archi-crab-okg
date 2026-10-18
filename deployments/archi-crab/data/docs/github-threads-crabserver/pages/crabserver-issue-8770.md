# dmwm/CRABServer issue #8770: #870: Test GH CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-07T08:32:54Z
Closed: 2024-11-07T09:36:48Z
URL: https://github.com/dmwm/CRABServer/issues/8770

## Opening post (cmsdmwmbot, 2024-11-07T08:32:54Z)

**This is a test of https://github.com/belforte/CRABClient/tree/new-preparelocal-dryrun**

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
Started at: 2024-11-07 09:32:53
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/870/)

## Comment (cmsdmwmbot, 2024-11-07T08:35:43Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241107_083325:cmsbot_crab_transferOutputs
241107_083338:cmsbot_crab_transferLogs
241107_083342:cmsbot_crab_activity
241107_083345:cmsbot_crab_inputFiles
241107_083349:cmsbot_crab_disableAutomaticOutputCollection
241107_083353:cmsbot_crab_outputFiles
241107_083356:cmsbot_crab_allowUndistributedCMSSW
241107_083400:cmsbot_crab_maxMemoryMB
241107_083403:cmsbot_crab_maxJobRuntimeMin
241107_083407:cmsbot_crab_numCores
241107_083410:cmsbot_crab_scriptExe
241107_083414:cmsbot_crab_scriptArgs
241107_083417:cmsbot_crab_sendVenvFolder
241107_083421:cmsbot_crab_sendExternalFolder
241107_083424:cmsbot_crab_inputDBS
241107_083428:cmsbot_crab_useParent
241107_083431:cmsbot_crab_secondaryInputDataset
241107_083435:cmsbot_crab_lumiMaskFile
241107_083439:cmsbot_crab_lumiMaskUrl
241107_083443:cmsbot_crab_outLFNDirBase
241107_083446:cmsbot_crab_runRange
241107_083450:cmsbot_crab_ignoreLocality
241107_083453:cmsbot_crab_userInputFiles
241107_083457:cmsbot_crab_whitelist
241107_083500:cmsbot_crab_blacklist
241107_083503:cmsbot_crab_ignoreGlobalBlacklist
241107_083507:cmsbot_crab_voRole
241107_083510:cmsbot_crab_voGroup
241107_083514:cmsbot_crab_scheddName
241107_083517:cmsbot_crab_collector
241107_083521:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241107_083321:cmsbot_crab_20241107_093318
```

Finished at: 2024-11-07 09:35:21
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/870/console)

## Comment (cmsdmwmbot, 2024-11-07T08:59:39Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-07 09:59:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/563/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/563//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241107_093318  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'killed', 'finished'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241107_093318/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241107_083321:cmsbot_crab_20241107_093318  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241107_093318/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'killed', 'finished', 'failed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241107_093318/crab.log
```

## Comment (cmsdmwmbot, 2024-11-07T09:01:04Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-07 10:01:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1222/console

```
RETRY TESTS:
transferLogs-check.sh 241107_083338:cmsbot_crab_transferLogs - 2
scriptArgs-check.sh 241107_083414:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 241107_083435:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241107_083439:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241107_083443:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241107_083446:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241107_083453:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241107_083457:cmsbot_crab_whitelist - 2
blacklist-check.sh 241107_083500:cmsbot_crab_blacklist - 2
voRole-check.sh 241107_083507:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241107_083325:cmsbot_crab_transferOutputs - 0
activity-check.sh 241107_083342:cmsbot_crab_activity - 0
inputFiles-check.sh 241107_083345:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241107_083349:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241107_083353:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241107_083356:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241107_083400:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241107_083403:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241107_083407:cmsbot_crab_numCores - 0
scriptExe-check.sh 241107_083410:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 241107_083417:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241107_083421:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241107_083424:cmsbot_crab_inputDBS - 0
useParent-check.sh 241107_083428:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241107_083431:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 241107_083450:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 241107_083503:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 241107_083510:cmsbot_crab_voGroup - 0
scheddName-check.sh 241107_083514:cmsbot_crab_scheddName - 0
collector-check.sh 241107_083517:cmsbot_crab_collector - 0
extraJDL-check.sh 241107_083521:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-07T09:07:12Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-07 10:07:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/564/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/564//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20241107_093318  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/tmpdgkvbq7g
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is KILLED


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241107_093318  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
All the jobs of the original task failed. Better investigate and submit it again than recover.
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241107_093318/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241107_083321:cmsbot_crab_20241107_093318  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241107_093318/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
All the jobs of the original task failed. Better investigate and submit it again than recover.
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241107_093318/crab.log
```

## Comment (belforte, 2024-11-07T09:23:16Z)

CV failed becasue crab recover did not wait long enough after issuing kill. Will submit again

## Comment (cmsdmwmbot, 2024-11-07T09:25:30Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-07 10:25:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1223/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241107_083325:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241107_083338:cmsbot_crab_transferLogs - 0
activity-check.sh 241107_083342:cmsbot_crab_activity - 0
inputFiles-check.sh 241107_083345:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241107_083349:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241107_083353:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241107_083356:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241107_083400:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241107_083403:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241107_083407:cmsbot_crab_numCores - 0
scriptExe-check.sh 241107_083410:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241107_083414:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241107_083417:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241107_083421:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241107_083424:cmsbot_crab_inputDBS - 0
useParent-check.sh 241107_083428:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241107_083431:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241107_083435:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241107_083439:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241107_083443:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241107_083446:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241107_083450:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241107_083453:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241107_083457:cmsbot_crab_whitelist - 0
blacklist-check.sh 241107_083500:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241107_083503:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241107_083507:cmsbot_crab_voRole - 0
voGroup-check.sh 241107_083510:cmsbot_crab_voGroup - 0
scheddName-check.sh 241107_083514:cmsbot_crab_scheddName - 0
collector-check.sh 241107_083517:cmsbot_crab_collector - 0
extraJDL-check.sh 241107_083521:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
