# dmwm/CRABServer issue #8829: #895: Test GH CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2024-11-25T22:12:03Z
Closed: 2024-11-26T08:42:17Z
URL: https://github.com/dmwm/CRABServer/issues/8829

## Opening post (cmsdmwmbot, 2024-11-25T22:12:03Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**
- CRABServer_tag: **v3.241125**

**Tests started:**

- [x] Client_Validation
Started at: 2024-11-25 23:12:02
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/895/)

## Comment (cmsdmwmbot, 2024-11-25T22:12:52Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
241125_221230:cmsbot_crab_20241125_231228
```

Finished at: 2024-11-25 23:12:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/895/console)

## Comment (cmsdmwmbot, 2024-11-25T22:37:00Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-25 23:36:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/574/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/574//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241125_231228  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'killed', 'finished'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241125_231228/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241125_221230:cmsbot_crab_20241125_231228  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241125_231228/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'finished', 'killed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241125_231228/crab.log
```
