# dmwm/CRABServer issue #7953: #519: Test GH CRABClient using preprod REST instance and CMSSW_8_0_36 CMSSW release

State: closed
Opened: 2023-10-17T20:57:27Z
Closed: 2023-10-18T07:46:51Z
URL: https://github.com/dmwm/CRABServer/issues/7953

## Opening post (cmsdmwmbot, 2023-10-17T20:57:27Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_8_0_36**
- SCRAM_ARCH: **slc7_amd64_gcc530**
- CRABServer_tag: **HEAD**

**Tests started:**

- [ ] Client_Validation
Started at: 2023-10-17 22:57:26
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/519/)

## Comment (cmsdmwmbot, 2023-10-17T20:59:21Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
231017_205858:cmsbot_crab_20231017_225851
```

Finished at: 2023-10-17 22:58:59
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/519/console)

## Comment (cmsdmwmbot, 2023-10-17T21:23:37Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2023-10-17 23:23:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/399/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/399//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab tasks  --days=1  --status=NEW  --proxy=/tmp/x509up_u501  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status NEW
ERROR: TypeError: list indices must be integers, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=HOLDING  --proxy=/tmp/x509up_u501  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status HOLDING
ERROR: TypeError: list indices must be integers, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=QUEUED  --proxy=/tmp/x509up_u501  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status QUEUED
ERROR: TypeError: list indices must be integers, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=SUBMITFAILED  --proxy=/tmp/x509up_u501  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status SUBMITFAILED
ERROR: TypeError: list indices must be integers, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=KILLED  --proxy=/tmp/x509up_u501  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status KILLED
ERROR: TypeError: list indices must be integers, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=KILLFAILED  --proxy=/tmp/x509up_u501  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status KILLFAILED
ERROR: TypeError: list indices must be integers, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=RESUBMITFAILED  --proxy=/tmp/x509up_u501  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status RESUBMITFAILED
ERROR: TypeError: list indices must be integers, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=FAILED  --proxy=/tmp/x509up_u501  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status FAILED
ERROR: TypeError: list indices must be integers, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.
```
