# dmwm/CRABServer issue #7532: #372: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2023-02-15T14:44:37Z
Closed: 2023-02-16T18:07:41Z
URL: https://github.com/dmwm/CRABServer/issues/7532

## Opening post (cmsdmwmbot, 2023-02-15T14:44:37Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-02-15 15:44:36
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/372/)

## Comment (cmsdmwmbot, 2023-02-15T14:49:52Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230215_144859:cmsbot_crab_20230215_154855
230215_144904:cmsbot_crab_20230215_154859
230215_144908:cmsbot_crab_20230215_154904
230215_144913:cmsbot_crab_20230215_154909
230215_144917:cmsbot_crab_20230215_154913
230215_144930:cmsbot_crab_20230215_154918
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230215_144631:cmsbot_crab_transferOutputs
230215_144635:cmsbot_crab_transferLogs
230215_144640:cmsbot_crab_activity
230215_144645:cmsbot_crab_inputFiles
230215_144649:cmsbot_crab_disableAutomaticOutputCollection
230215_144655:cmsbot_crab_outputFiles
230215_144659:cmsbot_crab_allowUndistributedCMSSW
230215_144704:cmsbot_crab_maxMemoryMB
230215_144708:cmsbot_crab_maxJobRuntimeMin
230215_144714:cmsbot_crab_numCores
230215_144718:cmsbot_crab_scriptExe
230215_144723:cmsbot_crab_scriptArgs
230215_144729:cmsbot_crab_sendPythonFolder
230215_144737:cmsbot_crab_sendExternalFolder
230215_144741:cmsbot_crab_inputDBS
230215_144746:cmsbot_crab_useParent
230215_144751:cmsbot_crab_secondaryInputDataset
230215_144755:cmsbot_crab_lumiMaskFile
230215_144759:cmsbot_crab_lumiMaskUrl
230215_144805:cmsbot_crab_outLFNDirBase
230215_144809:cmsbot_crab_runRange
230215_144814:cmsbot_crab_ignoreLocality
230215_144818:cmsbot_crab_userInputFiles
230215_144822:cmsbot_crab_whitelist
230215_144827:cmsbot_crab_blacklist
230215_144832:cmsbot_crab_ignoreGlobalBlacklist
230215_144836:cmsbot_crab_voRole
230215_144841:cmsbot_crab_voGroup
230215_144845:cmsbot_crab_scheddName
230215_144850:cmsbot_crab_collector
230215_144854:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230215_144625:cmsbot_crab_20230215_154617
```

Finished at: 2023-02-15 15:49:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/372/console)

## Comment (cmsdmwmbot, 2023-02-15T15:13:26Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2023-02-15 16:13:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/333/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/333//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/cmsbld/tmp_gxauK
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is HOLDING


TEST_COMMAND: crab getlog  --quantity=2  --short --outputpath=/data/CRABTesting/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Fatal error trying to connect to https://cmsweb-testbed.cern.ch:8443/crabserver/preprod/task?subresource=webdirprx&workflow=230215_144625%3Acmsbot_crab_20230215_154617 using subresource=webdirprx&workflow=230215_144625%3Acmsbot_crab_20230215_154617.
The server answered with an error.
Server answered with: Execution error
Reason is: Webdir not set in the database. Cannot build proxied webdir
Error Id: 3c71904df13d5bcae26e8e6529e325f8


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/data/CRABTesting/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230215_154617  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.
```

## Comment (cmsdmwmbot, 2023-02-15T15:17:34Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-02-15 16:17:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/575/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 230215_144631:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230215_144635:cmsbot_crab_transferLogs - 1
activity-check.sh 230215_144640:cmsbot_crab_activity - 1
inputFiles-check.sh 230215_144645:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 230215_144649:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230215_144655:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 230215_144659:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 230215_144704:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230215_144708:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230215_144714:cmsbot_crab_numCores - 1
scriptExe-check.sh 230215_144718:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230215_144723:cmsbot_crab_scriptArgs - 1
sendPythonFolder-check.sh 230215_144729:cmsbot_crab_sendPythonFolder - 1
sendExternalFolder-check.sh 230215_144737:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 230215_144741:cmsbot_crab_inputDBS - 1
useParent-check.sh 230215_144746:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230215_144751:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230215_144755:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230215_144759:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230215_144805:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230215_144809:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230215_144814:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230215_144818:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230215_144822:cmsbot_crab_whitelist - 1
blacklist-check.sh 230215_144827:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230215_144832:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230215_144836:cmsbot_crab_voRole - 1
voGroup-check.sh 230215_144841:cmsbot_crab_voGroup - 1
scheddName-check.sh 230215_144845:cmsbot_crab_scheddName - 1
collector-check.sh 230215_144850:cmsbot_crab_collector - 1
extraJDL-check.sh 230215_144854:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-02-15T15:53:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-15 16:53:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/426/console

```
{'TN': '230215_144859:cmsbot_crab_20230215_154855', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144904:cmsbot_crab_20230215_154859', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144908:cmsbot_crab_20230215_154904', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144913:cmsbot_crab_20230215_154909', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144917:cmsbot_crab_20230215_154913', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144930:cmsbot_crab_20230215_154918', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
```

## Comment (cmsdmwmbot, 2023-02-15T16:58:06Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-02-15 17:58:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/428/console

```
{'TN': '230215_144859:cmsbot_crab_20230215_154855', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144904:cmsbot_crab_20230215_154859', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144908:cmsbot_crab_20230215_154904', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144913:cmsbot_crab_20230215_154909', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144917:cmsbot_crab_20230215_154913', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144930:cmsbot_crab_20230215_154918', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
```

## Comment (cmsdmwmbot, 2023-02-15T18:02:50Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-02-15 19:02:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/430/console

```
{'TN': '230215_144859:cmsbot_crab_20230215_154855', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144904:cmsbot_crab_20230215_154859', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144908:cmsbot_crab_20230215_154904', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144913:cmsbot_crab_20230215_154909', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144917:cmsbot_crab_20230215_154913', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_144930:cmsbot_crab_20230215_154918', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
```

## Comment (novicecpp, 2023-02-16T17:58:51Z)

This one had bug I found in wmcore. Closing.
