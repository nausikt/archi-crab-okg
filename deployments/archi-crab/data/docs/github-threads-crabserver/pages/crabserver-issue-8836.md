# dmwm/CRABServer issue #8836: #902: Test dev CRABClient using prod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2024-11-26T11:00:26Z
Closed: 2024-11-26T14:18:24Z
URL: https://github.com/dmwm/CRABServer/issues/8836

## Opening post (cmsdmwmbot, 2024-11-26T11:00:26Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [ ] Client_Validation
Started at: 2024-11-26 12:00:25
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/902/)

## Comment (cmsdmwmbot, 2024-11-26T11:01:04Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
241126_110042:cmsbot_crab_20241126_120039
```

Finished at: 2024-11-26 12:00:42
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/902/console)

## Comment (cmsdmwmbot, 2024-11-26T11:22:38Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-26 12:22:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/579/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/579//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241126_120039  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state (set(['failed', 'finished', 'killed'])). You have ['finished', 'transferring']
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241126_120039/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241126_110042:cmsbot_crab_20241126_120039  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241126_120039/.requestcache not created, because it already exists.
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state (set(['failed', 'finished', 'killed'])). You have ['finished', 'transferring']
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241126_120039/crab.log
```

## Comment (belforte, 2024-11-26T14:18:22Z)

OK. known problem with recover
