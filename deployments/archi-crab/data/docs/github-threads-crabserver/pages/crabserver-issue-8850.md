# dmwm/CRABServer issue #8850: #916: Test prod CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2024-11-27T19:44:43Z
Closed: 2024-11-27T20:13:06Z
URL: https://github.com/dmwm/CRABServer/issues/8850

## Opening post (cmsdmwmbot, 2024-11-27T19:44:43Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
Started at: 2024-11-27 20:44:42
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/916/)

## Comment (cmsdmwmbot, 2024-11-27T19:46:03Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
241127_194541:cmsbot_crab_20241127_204538
```

Finished at: 2024-11-27 20:45:41
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/916/console)

## Comment (cmsdmwmbot, 2024-11-27T20:12:26Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-27 21:12:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/590/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/590//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241127_204538  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'killed', 'finished', 'failed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241127_204538/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241127_194541:cmsbot_crab_20241127_204538  --instance=test2  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241127_204538/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'finished', 'killed', 'failed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241127_204538/crab.log
```

## Comment (belforte, 2024-11-27T20:13:06Z)

known problem with recover. all OK
