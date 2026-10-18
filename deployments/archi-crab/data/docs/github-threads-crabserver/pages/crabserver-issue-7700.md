# dmwm/CRABServer issue #7700: #410: Test prod CRABClient using test2 REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2023-06-29T20:35:49Z
Closed: 2023-06-30T09:07:47Z
URL: https://github.com/dmwm/CRABServer/issues/7700

## Opening post (cmsdmwmbot, 2023-06-29T20:35:49Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-06-29 22:35:49
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/410/)

## Comment (cmsdmwmbot, 2023-06-29T20:39:43Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230629_203855:cmsbot_crab_20230629_223852
230629_203859:cmsbot_crab_20230629_223856
230629_203903:cmsbot_crab_20230629_223900
230629_203907:cmsbot_crab_20230629_223904
230629_203911:cmsbot_crab_20230629_223908
230629_203922:cmsbot_crab_20230629_223912
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_203722:cmsbot_crab_transferOutputs
230629_203725:cmsbot_crab_transferLogs
230629_203728:cmsbot_crab_activity
230629_203731:cmsbot_crab_inputFiles
230629_203734:cmsbot_crab_disableAutomaticOutputCollection
230629_203737:cmsbot_crab_outputFiles
230629_203740:cmsbot_crab_allowUndistributedCMSSW
230629_203743:cmsbot_crab_maxMemoryMB
230629_203746:cmsbot_crab_maxJobRuntimeMin
230629_203748:cmsbot_crab_numCores
230629_203751:cmsbot_crab_scriptExe
230629_203754:cmsbot_crab_scriptArgs
230629_203757:cmsbot_crab_sendPythonFolder
230629_203803:cmsbot_crab_sendExternalFolder
230629_203805:cmsbot_crab_inputDBS
230629_203808:cmsbot_crab_useParent
230629_203811:cmsbot_crab_secondaryInputDataset
230629_203814:cmsbot_crab_lumiMaskFile
230629_203817:cmsbot_crab_lumiMaskUrl
230629_203820:cmsbot_crab_outLFNDirBase
230629_203823:cmsbot_crab_runRange
230629_203826:cmsbot_crab_ignoreLocality
230629_203829:cmsbot_crab_userInputFiles
230629_203832:cmsbot_crab_whitelist
230629_203834:cmsbot_crab_blacklist
230629_203837:cmsbot_crab_ignoreGlobalBlacklist
230629_203840:cmsbot_crab_voRole
230629_203843:cmsbot_crab_voGroup
230629_203846:cmsbot_crab_scheddName
230629_203848:cmsbot_crab_collector
230629_203851:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230629_203719:cmsbot_crab_20230629_223715
```

Finished at: 2023-06-29 22:39:22
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/410/console)

## Comment (cmsdmwmbot, 2023-06-29T21:02:12Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2023-06-29 23:02:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/352/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/352//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/cmsbld/tmp48nkqJ
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is QUEUED


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/data/CRABTesting/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/data/CRABTesting/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20230629_223715  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Cannot retrieve job list from the status command.
```

## Comment (cmsdmwmbot, 2023-06-29T21:06:18Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 23:06:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/638/console

```
RETRY TESTS:
transferOutputs-check.sh 230629_203722:cmsbot_crab_transferOutputs - 2

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferLogs-check.sh 230629_203725:cmsbot_crab_transferLogs - 1
activity-check.sh 230629_203728:cmsbot_crab_activity - 1
inputFiles-check.sh 230629_203731:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 230629_203734:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230629_203737:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 230629_203740:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 230629_203743:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230629_203746:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230629_203748:cmsbot_crab_numCores - 1
scriptExe-check.sh 230629_203751:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230629_203754:cmsbot_crab_scriptArgs - 1
sendPythonFolder-check.sh 230629_203757:cmsbot_crab_sendPythonFolder - 1
sendExternalFolder-check.sh 230629_203803:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 230629_203805:cmsbot_crab_inputDBS - 1
useParent-check.sh 230629_203808:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230629_203811:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230629_203814:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230629_203817:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230629_203820:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230629_203823:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230629_203826:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230629_203829:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230629_203832:cmsbot_crab_whitelist - 1
blacklist-check.sh 230629_203834:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230629_203837:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230629_203840:cmsbot_crab_voRole - 1
voGroup-check.sh 230629_203843:cmsbot_crab_voGroup - 1
scheddName-check.sh 230629_203846:cmsbot_crab_scheddName - 1
collector-check.sh 230629_203848:cmsbot_crab_collector - 1
extraJDL-check.sh 230629_203851:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-06-29T21:33:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-29 23:33:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/645/console

```
RETRY TESTS:
scriptExe-check.sh 230629_203751:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 230629_203817:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230629_203823:cmsbot_crab_runRange - 2
whitelist-check.sh 230629_203832:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_203834:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230629_203837:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_203722:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_203725:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_203728:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_203731:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_203734:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_203737:cmsbot_crab_outputFiles - 0
scriptArgs-check.sh 230629_203754:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_203757:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_203803:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_203805:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_203808:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_203811:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_203814:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230629_203820:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230629_203826:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_203829:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230629_203840:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_203843:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_203846:cmsbot_crab_scheddName - 0
collector-check.sh 230629_203848:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_203851:cmsbot_crab_extraJDL - 0

FAILED TESTS:
allowUndistributedCMSSW-check.sh 230629_203740:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 230629_203743:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230629_203746:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230629_203748:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2023-06-29T21:41:24Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-29 23:41:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/354/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/354//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-29T21:42:38Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 23:42:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/461/console

```
{'TN': '230629_203855:cmsbot_crab_20230629_223852', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 6, 'transferring': 994}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_203859:cmsbot_crab_20230629_223856', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_203903:cmsbot_crab_20230629_223900', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_203907:cmsbot_crab_20230629_223904', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_203911:cmsbot_crab_20230629_223908', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_203922:cmsbot_crab_20230629_223912', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-06-29T21:56:49Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-06-29 23:56:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/651/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230629_203743:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 230629_203748:cmsbot_crab_numCores - 2
blacklist-check.sh 230629_203834:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_203722:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_203725:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_203728:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_203731:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_203734:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_203737:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_203740:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230629_203746:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230629_203751:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_203754:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_203757:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_203803:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_203805:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_203808:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_203811:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_203814:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_203817:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_203820:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_203823:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_203826:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_203829:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_203832:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 230629_203837:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_203840:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_203843:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_203846:cmsbot_crab_scheddName - 0
collector-check.sh 230629_203848:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_203851:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T22:22:14Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 3 out of 4. Test is done.
**Finished at:** 2023-06-30 00:22:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/655/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_203722:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_203725:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_203728:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_203731:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_203734:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_203737:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_203740:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_203743:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_203746:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_203748:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_203751:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_203754:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_203757:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_203803:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_203805:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_203808:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_203811:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_203814:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_203817:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_203820:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_203823:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_203826:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_203829:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_203832:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_203834:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_203837:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_203840:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_203843:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_203846:cmsbot_crab_scheddName - 0
collector-check.sh 230629_203848:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_203851:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T22:44:48Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-06-30 00:44:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/463/console

```
{'TN': '230629_203855:cmsbot_crab_20230629_223852', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_203859:cmsbot_crab_20230629_223856', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_203903:cmsbot_crab_20230629_223900', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_203907:cmsbot_crab_20230629_223904', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_203911:cmsbot_crab_20230629_223908', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_203922:cmsbot_crab_20230629_223912', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```
