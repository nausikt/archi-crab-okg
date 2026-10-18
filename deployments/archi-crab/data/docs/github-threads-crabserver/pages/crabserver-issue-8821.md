# dmwm/CRABServer issue #8821: #888: Test GH CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-11-25T18:28:23Z
Closed: 2024-11-25T20:17:05Z
URL: https://github.com/dmwm/CRABServer/issues/8821

## Opening post (cmsdmwmbot, 2024-11-25T18:28:23Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**
- CRABServer_tag: **v3.241125**

**Tests started:**

- [x] Client_Validation
Started at: 2024-11-25 19:28:22
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/888/)

## Comment (cmsdmwmbot, 2024-11-25T18:29:04Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
241125_182842:cmsbot_crab_20241125_192841
```

Finished at: 2024-11-25 19:28:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/888/console)

## Comment (cmsdmwmbot, 2024-11-25T18:52:48Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-25 19:52:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/572/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/572//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241125_192841  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'finished', 'failed', 'killed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241125_192841/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241125_182842:cmsbot_crab_20241125_192841  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241125_192841/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'finished', 'killed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241125_192841/crab.log
```

## Comment (belforte, 2024-11-25T20:17:05Z)

usual problem with crab recovery issued while transferring
