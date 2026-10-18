# dmwm/CRABServer issue #8766: #869: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-04T23:46:28Z
Closed: 2024-11-06T14:07:22Z
URL: https://github.com/dmwm/CRABServer/issues/8766

## Opening post (cmsdmwmbot, 2024-11-04T23:46:28Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-11-05 00:46:27
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/869/)

## Comment (cmsdmwmbot, 2024-11-04T23:48:18Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241104_234650:cmsbot_crab_transferOutputs
241104_234652:cmsbot_crab_transferLogs
241104_234655:cmsbot_crab_activity
241104_234657:cmsbot_crab_inputFiles
241104_234659:cmsbot_crab_disableAutomaticOutputCollection
241104_234701:cmsbot_crab_outputFiles
241104_234703:cmsbot_crab_allowUndistributedCMSSW
241104_234706:cmsbot_crab_maxMemoryMB
241104_234708:cmsbot_crab_maxJobRuntimeMin
241104_234710:cmsbot_crab_numCores
241104_234712:cmsbot_crab_scriptExe
241104_234715:cmsbot_crab_scriptArgs
241104_234717:cmsbot_crab_sendVenvFolder
241104_234719:cmsbot_crab_sendExternalFolder
241104_234721:cmsbot_crab_inputDBS
241104_234723:cmsbot_crab_useParent
241104_234726:cmsbot_crab_secondaryInputDataset
241104_234728:cmsbot_crab_lumiMaskFile
241104_234730:cmsbot_crab_lumiMaskUrl
241104_234733:cmsbot_crab_outLFNDirBase
241104_234735:cmsbot_crab_runRange
241104_234737:cmsbot_crab_ignoreLocality
241104_234739:cmsbot_crab_userInputFiles
241104_234742:cmsbot_crab_whitelist
241104_234744:cmsbot_crab_blacklist
241104_234746:cmsbot_crab_ignoreGlobalBlacklist
241104_234748:cmsbot_crab_voRole
241104_234750:cmsbot_crab_voGroup
241104_234752:cmsbot_crab_scheddName
241104_234754:cmsbot_crab_collector
241104_234757:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241104_234648:cmsbot_crab_20241105_004647
```

Finished at: 2024-11-05 00:47:57
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/869/console)

## Comment (cmsdmwmbot, 2024-11-05T00:11:13Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-05 01:11:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/562/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/562//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Running crab status first to fetch necessary information.
Rucio client intialized for account cmsbot
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241105_004647/crab.log


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Cannot retrieve job list from the status command.


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241105_004647  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241105_004647/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241104_234648:cmsbot_crab_20241105_004647  --instance=test2  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241105_004647/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241105_004647/crab.log
```

## Comment (cmsdmwmbot, 2024-11-05T00:11:51Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-11-05 01:11:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1221/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 241104_234650:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 241104_234652:cmsbot_crab_transferLogs - 1
activity-check.sh 241104_234655:cmsbot_crab_activity - 1
inputFiles-check.sh 241104_234657:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 241104_234659:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 241104_234701:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 241104_234703:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 241104_234706:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 241104_234708:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 241104_234710:cmsbot_crab_numCores - 1
scriptExe-check.sh 241104_234712:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 241104_234715:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 241104_234717:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 241104_234719:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 241104_234721:cmsbot_crab_inputDBS - 1
useParent-check.sh 241104_234723:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 241104_234726:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 241104_234728:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 241104_234730:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 241104_234733:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 241104_234735:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 241104_234737:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 241104_234739:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 241104_234742:cmsbot_crab_whitelist - 1
blacklist-check.sh 241104_234744:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 241104_234746:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 241104_234748:cmsbot_crab_voRole - 1
voGroup-check.sh 241104_234750:cmsbot_crab_voGroup - 1
scheddName-check.sh 241104_234752:cmsbot_crab_scheddName - 1
collector-check.sh 241104_234754:cmsbot_crab_collector - 1
extraJDL-check.sh 241104_234757:cmsbot_crab_extraJDL - 1
```

## Comment (belforte, 2024-11-06T14:07:22Z)

understood and fixed
