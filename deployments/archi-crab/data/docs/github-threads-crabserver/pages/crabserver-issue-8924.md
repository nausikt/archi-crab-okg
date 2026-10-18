# dmwm/CRABServer issue #8924: #933: Test GH CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2025-02-17T09:41:40Z
Closed: 2025-02-17T11:22:35Z
URL: https://github.com/dmwm/CRABServer/issues/8924

## Opening post (cmsdmwmbot, 2025-02-17T09:41:40Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2025-02-17 10:41:38
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/933/)

## Comment (cmsdmwmbot, 2025-02-17T09:44:30Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250217_094218:cmsbot_crab_20250217_104215
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250217_094221:cmsbot_crab_transferOutputs
250217_094226:cmsbot_crab_transferLogs
250217_094230:cmsbot_crab_activity
250217_094235:cmsbot_crab_inputFiles
250217_094238:cmsbot_crab_disableAutomaticOutputCollection
250217_094243:cmsbot_crab_outputFiles
250217_094246:cmsbot_crab_allowUndistributedCMSSW
250217_094249:cmsbot_crab_maxMemoryMB
250217_094252:cmsbot_crab_maxJobRuntimeMin
250217_094256:cmsbot_crab_numCores
250217_094300:cmsbot_crab_scriptExe
250217_094304:cmsbot_crab_scriptArgs
250217_094308:cmsbot_crab_sendVenvFolder
250217_094312:cmsbot_crab_sendExternalFolder
250217_094316:cmsbot_crab_inputDBS
250217_094320:cmsbot_crab_useParent
250217_094323:cmsbot_crab_secondaryInputDataset
250217_094326:cmsbot_crab_lumiMaskFile
250217_094331:cmsbot_crab_lumiMaskUrl
250217_094334:cmsbot_crab_outLFNDirBase
250217_094337:cmsbot_crab_runRange
250217_094341:cmsbot_crab_ignoreLocality
250217_094344:cmsbot_crab_userInputFiles
250217_094347:cmsbot_crab_whitelist
250217_094350:cmsbot_crab_blacklist
250217_094353:cmsbot_crab_ignoreGlobalBlacklist
250217_094356:cmsbot_crab_voRole
250217_094359:cmsbot_crab_voGroup
250217_094402:cmsbot_crab_scheddName
250217_094405:cmsbot_crab_collector
250217_094409:cmsbot_crab_extraJDL
```

Finished at: 2025-02-17 10:44:09
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/933/console)

## Comment (cmsdmwmbot, 2025-02-17T10:08:36Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2025-02-17 11:08:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/600/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/600//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=250217_094218:cmsbot_crab_20250217_104215  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20250217_104215/.requestcache not created, because it already exists.
Collecting information about original task ...
Rucio client intialized for account cmsbot
The server answered with an error.
Server answered with: Execution error
Reason is: You cannot kill a task if it is in the HOLDING status
Error Id: 8efd24e3f6e961edd2f955a46c1c00cc
```

## Comment (cmsdmwmbot, 2025-02-17T10:09:05Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-02-17 11:09:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1277/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250217_094221:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250217_094226:cmsbot_crab_transferLogs - 0
activity-check.sh 250217_094230:cmsbot_crab_activity - 0
inputFiles-check.sh 250217_094235:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250217_094238:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250217_094243:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250217_094246:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250217_094249:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250217_094252:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250217_094256:cmsbot_crab_numCores - 0
scriptExe-check.sh 250217_094300:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250217_094304:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250217_094308:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250217_094312:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250217_094316:cmsbot_crab_inputDBS - 0
useParent-check.sh 250217_094320:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250217_094323:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250217_094326:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250217_094331:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250217_094334:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250217_094337:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250217_094341:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250217_094344:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250217_094347:cmsbot_crab_whitelist - 0
blacklist-check.sh 250217_094350:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250217_094353:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250217_094356:cmsbot_crab_voRole - 0
voGroup-check.sh 250217_094359:cmsbot_crab_voGroup - 0
scheddName-check.sh 250217_094402:cmsbot_crab_scheddName - 0
collector-check.sh 250217_094405:cmsbot_crab_collector - 0
extraJDL-check.sh 250217_094409:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```

## Comment (cmsdmwmbot, 2025-02-17T10:27:19Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2025-02-17 11:27:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/601/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/601//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20250217_104215  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/tmplcw4y6pg
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is KILLED
```

## Comment (belforte, 2025-02-17T11:22:35Z)

CCV all OK. CV failed becasue it ran too soon, when I retried it failed because `crab recover` from previous try set the task in KILLED, making `crab preparelocal` failing. Call it OK and put a protection in the devel. queue.
