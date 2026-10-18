# dmwm/CRABServer issue #8046: #570: Test GH CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-11-30T11:24:44Z
Closed: 2023-11-30T12:39:00Z
URL: https://github.com/dmwm/CRABServer/issues/8046

## Opening post (cmsdmwmbot, 2023-11-30T11:24:44Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Validation
Started at: 2023-11-30 12:24:44
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/570/)

## Comment (cmsdmwmbot, 2023-11-30T11:26:06Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
231130_112544:cmsbot_crab_20231130_122543
```

Finished at: 2023-11-30 12:25:44
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/570/console)

## Comment (cmsdmwmbot, 2023-11-30T11:54:10Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2023-11-30 12:54:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/436/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/436//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20231130_122543  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20231130_122543  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20231130_122543  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20231130_122543  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20231130_122543  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20231130_122543  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20231130_122543  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files
```
