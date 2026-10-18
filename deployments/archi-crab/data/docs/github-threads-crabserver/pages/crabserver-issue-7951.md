# dmwm/CRABServer issue #7951: #517: Test GH CRABClient using prod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-10-17T20:53:17Z
Closed: 2023-10-18T07:46:50Z
URL: https://github.com/dmwm/CRABServer/issues/7951

## Opening post (cmsdmwmbot, 2023-10-17T20:53:17Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**
- CRABServer_tag: **HEAD**

**Tests started:**

- [ ] Client_Validation
Started at: 2023-10-17 22:53:16
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/517/)

## Comment (cmsdmwmbot, 2023-10-17T20:55:14Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
231017_205452:cmsbot_crab_20231017_225448
```

Finished at: 2023-10-17 22:54:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/517/console)

## Comment (cmsdmwmbot, 2023-10-17T21:20:51Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2023-10-17 23:20:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/397/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/397//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab tasks  --days=1  --status=NEW  --proxy=/tmp/x509up_u501  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status NEW
ERROR: TypeError: list indices must be integers or slices, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=HOLDING  --proxy=/tmp/x509up_u501  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status HOLDING
ERROR: TypeError: list indices must be integers or slices, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=QUEUED  --proxy=/tmp/x509up_u501  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status QUEUED
ERROR: TypeError: list indices must be integers or slices, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=SUBMITFAILED  --proxy=/tmp/x509up_u501  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status SUBMITFAILED
ERROR: TypeError: list indices must be integers or slices, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=KILLED  --proxy=/tmp/x509up_u501  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status KILLED
ERROR: TypeError: list indices must be integers or slices, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=KILLFAILED  --proxy=/tmp/x509up_u501  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status KILLFAILED
ERROR: TypeError: list indices must be integers or slices, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=RESUBMITFAILED  --proxy=/tmp/x509up_u501  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status RESUBMITFAILED
ERROR: TypeError: list indices must be integers or slices, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.


TEST_COMMAND: crab tasks  --days=1  --status=FAILED  --proxy=/tmp/x509up_u501  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
No tasks found from 2023-10-16 until 2023-10-17 with status FAILED
ERROR: TypeError: list indices must be integers or slices, not str

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab.log to the CRAB cache.
```
