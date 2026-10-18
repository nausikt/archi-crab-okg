# dmwm/CRABServer issue #8849: #915: Test prod CRABClient using test2 REST instance and CMSSW_12_5_0 CMSSW release

State: closed
Opened: 2024-11-27T19:42:44Z
Closed: 2024-11-27T20:12:36Z
URL: https://github.com/dmwm/CRABServer/issues/8849

## Opening post (cmsdmwmbot, 2024-11-27T19:42:44Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_5_0**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
Started at: 2024-11-27 20:42:43
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/915/)

## Comment (cmsdmwmbot, 2024-11-27T19:43:54Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
241127_194332:cmsbot_crab_20241127_204329
```

Finished at: 2024-11-27 20:43:32
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/915/console)

## Comment (cmsdmwmbot, 2024-11-27T20:09:27Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-27 21:09:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/589/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/589//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241127_204329  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'finished', 'killed', 'failed'}). You have dict_keys(['finished', 'transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241127_204329/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241127_194332:cmsbot_crab_20241127_204329  --instance=test2  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241127_204329/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'finished', 'killed'}). You have dict_keys(['finished', 'transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241127_204329/crab.log
```

## Comment (belforte, 2024-11-27T20:12:36Z)

known problem with recover. all ok
