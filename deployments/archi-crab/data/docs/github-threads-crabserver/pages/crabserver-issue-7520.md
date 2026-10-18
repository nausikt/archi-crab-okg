# dmwm/CRABServer issue #7520: #371: Test prod CRABClient using test2 REST instance and CMSSW_12_0_1 CMSSW release

State: closed
Opened: 2023-02-02T22:31:55Z
Closed: 2023-02-03T09:00:29Z
URL: https://github.com/dmwm/CRABServer/issues/7520

## Opening post (cmsdmwmbot, 2023-02-02T22:31:55Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_0_1**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-02-02 23:31:54
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/371/)

## Comment (belforte, 2023-02-02T22:32:41Z)

this is to validate https://github.com/belforte/CRABServer/tree/add-support-for-dbs_blockname-_block_complete-in-REST

## Comment (cmsdmwmbot, 2023-02-02T22:36:42Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230202_223558:cmsbot_crab_20230202_233555
230202_223602:cmsbot_crab_20230202_233559
230202_223605:cmsbot_crab_20230202_233603
230202_223609:cmsbot_crab_20230202_233606
230202_223612:cmsbot_crab_20230202_233610
230202_223620:cmsbot_crab_20230202_233613
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230202_223359:cmsbot_crab_transferOutputs
230202_223404:cmsbot_crab_transferLogs
230202_223407:cmsbot_crab_activity
230202_223411:cmsbot_crab_inputFiles
230202_223415:cmsbot_crab_disableAutomaticOutputCollection
230202_223418:cmsbot_crab_outputFiles
230202_223422:cmsbot_crab_allowUndistributedCMSSW
230202_223425:cmsbot_crab_maxMemoryMB
230202_223429:cmsbot_crab_maxJobRuntimeMin
230202_223433:cmsbot_crab_numCores
230202_223436:cmsbot_crab_scriptExe
230202_223440:cmsbot_crab_scriptArgs
230202_223443:cmsbot_crab_sendPythonFolder
230202_223452:cmsbot_crab_sendExternalFolder
230202_223456:cmsbot_crab_inputDBS
230202_223459:cmsbot_crab_useParent
230202_223503:cmsbot_crab_secondaryInputDataset
230202_223506:cmsbot_crab_lumiMaskFile
230202_223510:cmsbot_crab_lumiMaskUrl
230202_223515:cmsbot_crab_outLFNDirBase
230202_223518:cmsbot_crab_runRange
230202_223522:cmsbot_crab_ignoreLocality
230202_223525:cmsbot_crab_userInputFiles
230202_223529:cmsbot_crab_whitelist
230202_223533:cmsbot_crab_blacklist
230202_223536:cmsbot_crab_ignoreGlobalBlacklist
230202_223540:cmsbot_crab_voRole
230202_223543:cmsbot_crab_voGroup
230202_223547:cmsbot_crab_scheddName
230202_223550:cmsbot_crab_collector
230202_223554:cmsbot_crab_extraJDL
```

Finished at: 2023-02-02 23:36:20
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/371/console)

## Comment (cmsdmwmbot, 2023-02-02T23:03:06Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-03 00:03:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/573/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230202_223510:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230202_223515:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230202_223518:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230202_223525:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230202_223529:cmsbot_crab_whitelist - 2
blacklist-check.sh 230202_223533:cmsbot_crab_blacklist - 2
voGroup-check.sh 230202_223543:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230202_223359:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230202_223404:cmsbot_crab_transferLogs - 0
activity-check.sh 230202_223407:cmsbot_crab_activity - 0
inputFiles-check.sh 230202_223411:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230202_223415:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230202_223418:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230202_223422:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230202_223425:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230202_223429:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230202_223433:cmsbot_crab_numCores - 0
scriptExe-check.sh 230202_223436:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230202_223440:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230202_223443:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230202_223452:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230202_223456:cmsbot_crab_inputDBS - 0
useParent-check.sh 230202_223459:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230202_223503:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230202_223506:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230202_223522:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230202_223536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230202_223540:cmsbot_crab_voRole - 0
scheddName-check.sh 230202_223547:cmsbot_crab_scheddName - 0
collector-check.sh 230202_223550:cmsbot_crab_collector - 0
extraJDL-check.sh 230202_223554:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-02-02T23:29:45Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-02-03 00:29:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/574/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230202_223359:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230202_223404:cmsbot_crab_transferLogs - 0
activity-check.sh 230202_223407:cmsbot_crab_activity - 0
inputFiles-check.sh 230202_223411:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230202_223415:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230202_223418:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230202_223422:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230202_223425:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230202_223429:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230202_223433:cmsbot_crab_numCores - 0
scriptExe-check.sh 230202_223436:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230202_223440:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230202_223443:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230202_223452:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230202_223456:cmsbot_crab_inputDBS - 0
useParent-check.sh 230202_223459:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230202_223503:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230202_223506:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230202_223510:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230202_223515:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230202_223518:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230202_223522:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230202_223525:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230202_223529:cmsbot_crab_whitelist - 0
blacklist-check.sh 230202_223533:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230202_223536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230202_223540:cmsbot_crab_voRole - 0
voGroup-check.sh 230202_223543:cmsbot_crab_voGroup - 0
scheddName-check.sh 230202_223547:cmsbot_crab_scheddName - 0
collector-check.sh 230202_223550:cmsbot_crab_collector - 0
extraJDL-check.sh 230202_223554:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-02-02T23:39:37Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-03 00:39:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/423/console

```
{'TN': '230202_223558:cmsbot_crab_20230202_233555', 'dbStatus': u'NEW', 'testResult': 'TestRunning', 'jobsPerStatus': {'failed': 1, 'finished': 917, 'transferring': 52, 'running': 30}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230202_223602:cmsbot_crab_20230202_233559', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'finished': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230202_223605:cmsbot_crab_20230202_233603', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230202_223609:cmsbot_crab_20230202_233606', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230202_223612:cmsbot_crab_20230202_233610', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 98, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230202_223620:cmsbot_crab_20230202_233613', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-02-03T00:42:55Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-02-03 01:42:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/424/console

```
{'TN': '230202_223558:cmsbot_crab_20230202_233555', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230202_223602:cmsbot_crab_20230202_233559', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 0, 'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230202_223605:cmsbot_crab_20230202_233603', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230202_223609:cmsbot_crab_20230202_233606', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230202_223612:cmsbot_crab_20230202_233610', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230202_223620:cmsbot_crab_20230202_233613', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-02-03T01:45:28Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-02-03 02:45:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/425/console

```
{'TN': '230202_223558:cmsbot_crab_20230202_233555', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230202_223602:cmsbot_crab_20230202_233559', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'failed': 0, 'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230202_223605:cmsbot_crab_20230202_233603', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230202_223609:cmsbot_crab_20230202_233606', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230202_223612:cmsbot_crab_20230202_233610', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230202_223620:cmsbot_crab_20230202_233613', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-02-03T09:00:29Z)

all good
