# dmwm/CRABServer issue #8726: #844: Test GH CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-30T12:27:50Z
Closed: 2024-10-10T22:42:24Z
URL: https://github.com/dmwm/CRABServer/issues/8726

## Opening post (cmsdmwmbot, 2024-09-30T12:27:50Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **v3.240904**

**Tests started:**

- [ ] Client_Validation
Started at: 2024-09-30 14:27:49
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/844/)

## Comment (cmsdmwmbot, 2024-09-30T12:28:35Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
240930_122814:cmsbot_crab_20240930_142813
```

Finished at: 2024-09-30 14:28:14
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/844/console)

## Comment (cmsdmwmbot, 2024-09-30T12:52:43Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-09-30 14:52:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/547/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/547//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240930_142813  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240930_142813  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240930_142813  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240930_142813  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240930_142813  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240930_142813  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240930_142813  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20240930_142813  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Command recover failed


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=240930_122814:cmsbot_crab_20240930_142813  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20240930_142813/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
step kill - task already killed
Command recover failed
```
