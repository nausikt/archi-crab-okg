# dmwm/CRABServer issue #8146: #654: Test dev CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2024-01-11T17:32:22Z
Closed: 2024-01-11T20:06:56Z
URL: https://github.com/dmwm/CRABServer/issues/8146

## Opening post (cmsdmwmbot, 2024-01-11T17:32:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [ ] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 18:32:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/654/)

## Comment (cmsdmwmbot, 2024-01-11T17:34:21Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_173250:cmsbot_crab_transferOutputs
240111_173252:cmsbot_crab_transferLogs
240111_173254:cmsbot_crab_activity
240111_173256:cmsbot_crab_inputFiles
240111_173258:cmsbot_crab_disableAutomaticOutputCollection
240111_173300:cmsbot_crab_outputFiles
240111_173302:cmsbot_crab_allowUndistributedCMSSW
240111_173304:cmsbot_crab_maxMemoryMB
240111_173306:cmsbot_crab_maxJobRuntimeMin
240111_173308:cmsbot_crab_numCores
240111_173310:cmsbot_crab_scriptExe
240111_173312:cmsbot_crab_scriptArgs
240111_173315:cmsbot_crab_sendVenvFolder
240111_173323:cmsbot_crab_sendExternalFolder
240111_173325:cmsbot_crab_inputDBS
240111_173327:cmsbot_crab_useParent
240111_173329:cmsbot_crab_secondaryInputDataset
240111_173331:cmsbot_crab_lumiMaskFile
240111_173333:cmsbot_crab_lumiMaskUrl
240111_173336:cmsbot_crab_outLFNDirBase
240111_173338:cmsbot_crab_runRange
240111_173340:cmsbot_crab_ignoreLocality
240111_173342:cmsbot_crab_userInputFiles
240111_173344:cmsbot_crab_whitelist
240111_173346:cmsbot_crab_blacklist
240111_173348:cmsbot_crab_ignoreGlobalBlacklist
240111_173350:cmsbot_crab_voRole
240111_173353:cmsbot_crab_voGroup
240111_173355:cmsbot_crab_scheddName
240111_173357:cmsbot_crab_collector
240111_173359:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_173248:cmsbot_crab_20240111_183246
```

Finished at: 2024-01-11 18:34:00
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/654/console)

## Comment (cmsdmwmbot, 2024-01-11T17:57:53Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-01-11 18:57:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/471/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/471//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183246  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183246  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183246  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183246  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183246  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183246  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183246  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files
```

## Comment (cmsdmwmbot, 2024-01-11T18:01:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 19:01:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/848/console

```
RETRY TESTS:
transferOutputs-check.sh 240111_173250:cmsbot_crab_transferOutputs - 2
transferLogs-check.sh 240111_173252:cmsbot_crab_transferLogs - 2
activity-check.sh 240111_173254:cmsbot_crab_activity - 2
outputFiles-check.sh 240111_173300:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240111_173304:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240111_173306:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 240111_173310:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240111_173333:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240111_173338:cmsbot_crab_runRange - 2
whitelist-check.sh 240111_173344:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_173346:cmsbot_crab_blacklist - 2
extraJDL-check.sh 240111_173359:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 240111_173256:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173258:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240111_173302:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240111_173308:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240111_173312:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173315:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173323:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173325:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173327:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 240111_173331:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_173336:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240111_173340:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173342:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240111_173348:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173350:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173353:cmsbot_crab_voGroup - 0
collector-check.sh 240111_173357:cmsbot_crab_collector - 0

FAILED TESTS:
secondaryInputDataset-check.sh 240111_173329:cmsbot_crab_secondaryInputDataset - 1
scheddName-check.sh 240111_173355:cmsbot_crab_scheddName - 1
```

## Comment (cmsdmwmbot, 2024-01-11T18:25:54Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-01-11 19:25:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/857/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173250:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173252:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173254:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173256:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173258:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173300:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173302:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173304:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173306:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173308:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173310:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173312:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173315:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173323:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173325:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173327:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173329:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173331:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_173333:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_173336:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173338:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173340:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173342:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_173344:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_173346:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_173348:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173350:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173353:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173355:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173357:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173359:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-11T19:48:19Z)

failure likely caused by too many jobs around. Anyhow will try again.

## Comment (belforte, 2024-01-11T20:06:52Z)

ClientValidation test was too old and deleted from Jenkins, can't retry it. So I submitted a new test https://github.com/dmwm/CRABServer/issues/8156
