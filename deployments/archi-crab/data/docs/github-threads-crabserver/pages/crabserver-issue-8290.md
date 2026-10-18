# dmwm/CRABServer issue #8290: #725: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-15T19:47:23Z
Closed: 2024-03-15T20:11:08Z
URL: https://github.com/dmwm/CRABServer/issues/8290

## Opening post (cmsdmwmbot, 2024-03-15T19:47:23Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
Started at: 2024-03-15 20:47:22
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/725/)

## Comment (cmsdmwmbot, 2024-03-15T19:48:04Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
240315_194742:cmsbot_crab_20240315_204741
```

Finished at: 2024-03-15 20:47:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/725/console)

## Comment (belforte, 2024-03-15T20:11:08Z)

bad scheduler config. try again

## Comment (cmsdmwmbot, 2024-03-15T20:11:48Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-03-15 21:11:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/512/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/512//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/tmp4j_bii9h
ERROR: AttributeError: 'Logger' object has no attribute 'errror'

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --long --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --verboseErrors --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status   --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status   --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=state  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=site  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=runtime  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=memory  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=cpu  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=retries  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=waste  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=exitcode  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741
Task name:			240315_194742:cmsbot_crab_20240315_204741
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_194742%3Acmsbot_crab_20240315_204741
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_194742%3Acmsbot_crab_20240315_204741&from=1710528462000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_204741/crab.log to the CRAB cache.


TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Running crab status first to fetch necessary information.
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240315_204741  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
```
