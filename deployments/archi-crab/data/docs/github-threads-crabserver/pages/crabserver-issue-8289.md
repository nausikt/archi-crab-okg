# dmwm/CRABServer issue #8289: #724: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-15T13:56:26Z
Closed: 2024-03-15T16:04:06Z
URL: https://github.com/dmwm/CRABServer/issues/8289

## Opening post (cmsdmwmbot, 2024-03-15T13:56:26Z)

**Tests started for following configuration:**
**Aimed to validate crab-sched-901 on alma9**

**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-03-15 14:56:25
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/724/)

## Comment (cmsdmwmbot, 2024-03-15T13:59:31Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240315_135839:cmsbot_crab_20240315_145839
240315_135841:cmsbot_crab_20240315_145841
240315_135843:cmsbot_crab_20240315_145843
240315_135845:cmsbot_crab_20240315_145845
240315_135847:cmsbot_crab_20240315_145847
240315_135852:cmsbot_crab_20240315_145849
240315_135855:cmsbot_crab_rucio_transfers_20240315_145854
240315_135857:cmsbot_crab_rucio_transfers_group_20240315_145857
240315_135900:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240315_145859
240315_135903:cmsbot_crab_rucio_transfers_nopublication_20240315_145902
240315_135906:cmsbot_crab_rucio_transfers_withnoneedm_20240315_145905
240315_135909:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240315_145908
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240315_135649:cmsbot_crab_transferOutputs
240315_135651:cmsbot_crab_transferLogs
240315_135653:cmsbot_crab_activity
240315_135655:cmsbot_crab_inputFiles
240315_135657:cmsbot_crab_disableAutomaticOutputCollection
240315_135659:cmsbot_crab_outputFiles
240315_135701:cmsbot_crab_allowUndistributedCMSSW
240315_135703:cmsbot_crab_maxMemoryMB
240315_135705:cmsbot_crab_maxJobRuntimeMin
240315_135707:cmsbot_crab_numCores
240315_135709:cmsbot_crab_scriptExe
240315_135711:cmsbot_crab_scriptArgs
240315_135713:cmsbot_crab_sendVenvFolder
240315_135801:cmsbot_crab_sendExternalFolder
240315_135803:cmsbot_crab_inputDBS
240315_135805:cmsbot_crab_useParent
240315_135807:cmsbot_crab_secondaryInputDataset
240315_135809:cmsbot_crab_lumiMaskFile
240315_135811:cmsbot_crab_lumiMaskUrl
240315_135814:cmsbot_crab_outLFNDirBase
240315_135816:cmsbot_crab_runRange
240315_135818:cmsbot_crab_ignoreLocality
240315_135820:cmsbot_crab_userInputFiles
240315_135822:cmsbot_crab_whitelist
240315_135824:cmsbot_crab_blacklist
240315_135826:cmsbot_crab_ignoreGlobalBlacklist
240315_135828:cmsbot_crab_voRole
240315_135830:cmsbot_crab_voGroup
240315_135832:cmsbot_crab_scheddName
240315_135834:cmsbot_crab_collector
240315_135836:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240315_135647:cmsbot_crab_20240315_145646
```

Finished at: 2024-03-15 14:59:10
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/724/console)

## Comment (cmsdmwmbot, 2024-03-15T14:48:48Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-03-15 15:48:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/510/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/510//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab status  --long --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --verboseErrors --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status   --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=state  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
```

## Comment (cmsdmwmbot, 2024-03-15T14:49:32Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-15 15:49:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/972/console

```
RETRY TESTS:
outputFiles-check.sh 240315_135659:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240315_135703:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240315_135705:cmsbot_crab_maxJobRuntimeMin - 2
scriptArgs-check.sh 240315_135711:cmsbot_crab_scriptArgs - 2
secondaryInputDataset-check.sh 240315_135807:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240315_135811:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240315_135816:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240315_135818:cmsbot_crab_ignoreLocality - 2
whitelist-check.sh 240315_135822:cmsbot_crab_whitelist - 2
blacklist-check.sh 240315_135824:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240315_135826:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240315_135828:cmsbot_crab_voRole - 2
voGroup-check.sh 240315_135830:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240315_135836:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 240315_135655:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240315_135657:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240315_135701:cmsbot_crab_allowUndistributedCMSSW - 0
sendExternalFolder-check.sh 240315_135801:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240315_135803:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240315_135809:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240315_135814:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240315_135820:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240315_135832:cmsbot_crab_scheddName - 0
collector-check.sh 240315_135834:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 240315_135649:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240315_135651:cmsbot_crab_transferLogs - 1
activity-check.sh 240315_135653:cmsbot_crab_activity - 1
numCores-check.sh 240315_135707:cmsbot_crab_numCores - 1
scriptExe-check.sh 240315_135709:cmsbot_crab_scriptExe - 1
sendVenvFolder-check.sh 240315_135713:cmsbot_crab_sendVenvFolder - 1
useParent-check.sh 240315_135805:cmsbot_crab_useParent - 1
```

## Comment (cmsdmwmbot, 2024-03-15T15:29:42Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-03-15 16:29:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/973/console

```
RETRY TESTS:
transferLogs-check.sh 240315_135651:cmsbot_crab_transferLogs - 2
outputFiles-check.sh 240315_135659:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240315_135703:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240315_135705:cmsbot_crab_maxJobRuntimeMin - 2
secondaryInputDataset-check.sh 240315_135807:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240315_135811:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240315_135816:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240315_135818:cmsbot_crab_ignoreLocality - 2
whitelist-check.sh 240315_135822:cmsbot_crab_whitelist - 2
blacklist-check.sh 240315_135824:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240315_135826:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240315_135828:cmsbot_crab_voRole - 2
voGroup-check.sh 240315_135830:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240315_135836:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240315_135649:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240315_135655:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240315_135657:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240315_135701:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240315_135707:cmsbot_crab_numCores - 0
scriptExe-check.sh 240315_135709:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240315_135713:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240315_135801:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240315_135803:cmsbot_crab_inputDBS - 0
useParent-check.sh 240315_135805:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 240315_135809:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240315_135814:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240315_135820:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240315_135832:cmsbot_crab_scheddName - 0
collector-check.sh 240315_135834:cmsbot_crab_collector - 0

FAILED TESTS:
activity-check.sh 240315_135653:cmsbot_crab_activity - 1
scriptArgs-check.sh 240315_135711:cmsbot_crab_scriptArgs - 1
```

## Comment (belforte, 2024-03-15T16:04:06Z)

I asked for too much. crab-sched-901 ran out of memory under the load and died

## Comment (cmsdmwmbot, 2024-03-15T16:12:58Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-03-15 17:12:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/511/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/511//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/tmp323ccn_3
ERROR: AttributeError: 'Logger' object has no attribute 'errror'

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --long --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --verboseErrors --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=site  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=memory  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=cpu  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=retries  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=waste  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab status  --sort=exitcode  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
CRAB project directory:		/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646
Task name:			240315_135647:cmsbot_crab_20240315_145646
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_135647%3Acmsbot_crab_20240315_145646
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_135647%3Acmsbot_crab_20240315_145646&from=1710507407000&to=now
Format error in status_cache. Empty file ?
ERROR: TypeError: 'NoneType' object is not subscriptable

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.240110
	Please use 'crab uploadlog' to upload the log file /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20240315_145646/crab.log to the CRAB cache.


TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Running crab status first to fetch necessary information.
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240315_145646  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
```

## Comment (cmsdmwmbot, 2024-03-15T16:13:10Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-03-15 17:13:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/974/console

```
RETRY TESTS:
outputFiles-check.sh 240315_135659:cmsbot_crab_outputFiles - 2
lumiMaskUrl-check.sh 240315_135811:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240315_135816:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240315_135818:cmsbot_crab_ignoreLocality - 2
whitelist-check.sh 240315_135822:cmsbot_crab_whitelist - 2
blacklist-check.sh 240315_135824:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240315_135826:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240315_135828:cmsbot_crab_voRole - 2
voGroup-check.sh 240315_135830:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240315_135836:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 240315_135655:cmsbot_crab_inputFiles - 0
lumiMaskFile-check.sh 240315_135809:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240315_135814:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240315_135820:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240315_135832:cmsbot_crab_scheddName - 0
collector-check.sh 240315_135834:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 240315_135649:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240315_135651:cmsbot_crab_transferLogs - 1
activity-check.sh 240315_135653:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 240315_135657:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240315_135701:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240315_135703:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240315_135705:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240315_135707:cmsbot_crab_numCores - 1
scriptExe-check.sh 240315_135709:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240315_135711:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240315_135713:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240315_135801:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240315_135803:cmsbot_crab_inputDBS - 1
useParent-check.sh 240315_135805:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240315_135807:cmsbot_crab_secondaryInputDataset - 1
```

## Comment (cmsdmwmbot, 2024-03-15T16:38:49Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2024-03-15 17:38:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/975/console

```
RETRY TESTS:
transferLogs-check.sh 240315_135651:cmsbot_crab_transferLogs - 2
outputFiles-check.sh 240315_135659:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240315_135703:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240315_135705:cmsbot_crab_maxJobRuntimeMin - 2
scriptArgs-check.sh 240315_135711:cmsbot_crab_scriptArgs - 2
secondaryInputDataset-check.sh 240315_135807:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240315_135811:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240315_135816:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240315_135818:cmsbot_crab_ignoreLocality - 2
whitelist-check.sh 240315_135822:cmsbot_crab_whitelist - 2
blacklist-check.sh 240315_135824:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240315_135826:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240315_135828:cmsbot_crab_voRole - 2
voGroup-check.sh 240315_135830:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240315_135836:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240315_135649:cmsbot_crab_transferOutputs - 0
activity-check.sh 240315_135653:cmsbot_crab_activity - 0
inputFiles-check.sh 240315_135655:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240315_135657:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240315_135701:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240315_135707:cmsbot_crab_numCores - 0
scriptExe-check.sh 240315_135709:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240315_135713:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240315_135801:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240315_135803:cmsbot_crab_inputDBS - 0
useParent-check.sh 240315_135805:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 240315_135809:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240315_135814:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240315_135820:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240315_135832:cmsbot_crab_scheddName - 0
collector-check.sh 240315_135834:cmsbot_crab_collector - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-15T17:21:00Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 4 out of 4. Test failed. Investigate manually
**Finished at:** 2024-03-15 18:20:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/976/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
scheddName-check.sh 240315_135832:cmsbot_crab_scheddName - 0
collector-check.sh 240315_135834:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 240315_135649:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240315_135651:cmsbot_crab_transferLogs - 1
activity-check.sh 240315_135653:cmsbot_crab_activity - 1
inputFiles-check.sh 240315_135655:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240315_135657:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240315_135659:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240315_135701:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240315_135703:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240315_135705:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240315_135707:cmsbot_crab_numCores - 1
scriptExe-check.sh 240315_135709:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240315_135711:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240315_135713:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240315_135801:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240315_135803:cmsbot_crab_inputDBS - 1
useParent-check.sh 240315_135805:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240315_135807:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240315_135809:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240315_135811:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240315_135814:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240315_135816:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240315_135818:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240315_135820:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240315_135822:cmsbot_crab_whitelist - 1
blacklist-check.sh 240315_135824:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240315_135826:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240315_135828:cmsbot_crab_voRole - 1
voGroup-check.sh 240315_135830:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240315_135836:cmsbot_crab_extraJDL - 1
```
