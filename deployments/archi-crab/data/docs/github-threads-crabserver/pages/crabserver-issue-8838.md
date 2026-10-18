# dmwm/CRABServer issue #8838: #904: Test dev CRABClient using prod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-11-26T11:04:24Z
Closed: 2024-11-26T14:17:56Z
URL: https://github.com/dmwm/CRABServer/issues/8838

## Opening post (cmsdmwmbot, 2024-11-26T11:04:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Validation
Started at: 2024-11-26 12:04:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/904/)

## Comment (cmsdmwmbot, 2024-11-26T11:05:03Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
241126_110441:cmsbot_crab_20241126_120440
```

Finished at: 2024-11-26 12:04:41
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/904/console)

## Comment (cmsdmwmbot, 2024-11-26T11:29:45Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-26 12:29:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/581/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/581//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241126_120440  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'killed', 'failed', 'finished'}). You have dict_keys(['transferring', 'finished'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241126_120440/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241126_110441:cmsbot_crab_20241126_120440  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241126_120440/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'killed', 'finished'}). You have dict_keys(['transferring', 'finished'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241126_120440/crab.log
```

## Comment (belforte, 2024-11-26T14:17:56Z)

OK. known problem with recover
