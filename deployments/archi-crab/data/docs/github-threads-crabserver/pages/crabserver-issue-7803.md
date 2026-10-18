# dmwm/CRABServer issue #7803: #452: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-08-10T20:54:01Z
Closed: 2023-08-11T11:08:28Z
URL: https://github.com/dmwm/CRABServer/issues/7803

## Opening post (cmsdmwmbot, 2023-08-10T20:54:01Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-08-10 22:54:00
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/452/)

## Comment (cmsdmwmbot, 2023-08-10T20:56:27Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230810_205557:cmsbot_crab_20230810_225556
230810_205558:cmsbot_crab_20230810_225558
230810_205600:cmsbot_crab_20230810_225559
230810_205601:cmsbot_crab_20230810_225601
230810_205603:cmsbot_crab_20230810_225602
230810_205606:cmsbot_crab_20230810_225604
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230810_205421:cmsbot_crab_transferOutputs
230810_205425:cmsbot_crab_transferLogs
230810_205427:cmsbot_crab_activity
230810_205429:cmsbot_crab_inputFiles
230810_205431:cmsbot_crab_disableAutomaticOutputCollection
230810_205433:cmsbot_crab_outputFiles
230810_205435:cmsbot_crab_allowUndistributedCMSSW
230810_205437:cmsbot_crab_maxMemoryMB
230810_205439:cmsbot_crab_maxJobRuntimeMin
230810_205441:cmsbot_crab_numCores
230810_205443:cmsbot_crab_scriptExe
230810_205445:cmsbot_crab_scriptArgs
230810_205446:cmsbot_crab_sendPythonFolder
230810_205527:cmsbot_crab_sendExternalFolder
230810_205529:cmsbot_crab_inputDBS
230810_205530:cmsbot_crab_useParent
230810_205532:cmsbot_crab_secondaryInputDataset
230810_205534:cmsbot_crab_lumiMaskFile
230810_205536:cmsbot_crab_lumiMaskUrl
230810_205538:cmsbot_crab_outLFNDirBase
230810_205539:cmsbot_crab_runRange
230810_205541:cmsbot_crab_ignoreLocality
230810_205542:cmsbot_crab_userInputFiles
230810_205544:cmsbot_crab_whitelist
230810_205545:cmsbot_crab_blacklist
230810_205547:cmsbot_crab_ignoreGlobalBlacklist
230810_205549:cmsbot_crab_voRole
230810_205550:cmsbot_crab_voGroup
230810_205551:cmsbot_crab_scheddName
230810_205553:cmsbot_crab_collector
230810_205555:cmsbot_crab_extraJDL
```

Finished at: 2023-08-10 22:56:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/452/console)

## Comment (cmsdmwmbot, 2023-08-10T21:18:47Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-10 23:18:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/775/console

```
RETRY TESTS:
transferLogs-check.sh 230810_205425:cmsbot_crab_transferLogs - 2
outputFiles-check.sh 230810_205433:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 230810_205439:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 230810_205443:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 230810_205536:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230810_205538:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230810_205539:cmsbot_crab_runRange - 2
whitelist-check.sh 230810_205544:cmsbot_crab_whitelist - 2
blacklist-check.sh 230810_205545:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230810_205547:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230810_205421:cmsbot_crab_transferOutputs - 0
activity-check.sh 230810_205427:cmsbot_crab_activity - 0
inputFiles-check.sh 230810_205429:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230810_205431:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230810_205435:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230810_205437:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230810_205441:cmsbot_crab_numCores - 0
scriptArgs-check.sh 230810_205445:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230810_205446:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230810_205527:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230810_205529:cmsbot_crab_inputDBS - 0
useParent-check.sh 230810_205530:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230810_205532:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230810_205534:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230810_205541:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230810_205542:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230810_205549:cmsbot_crab_voRole - 0
voGroup-check.sh 230810_205550:cmsbot_crab_voGroup - 0
scheddName-check.sh 230810_205551:cmsbot_crab_scheddName - 0
collector-check.sh 230810_205553:cmsbot_crab_collector - 0
extraJDL-check.sh 230810_205555:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-10T21:43:01Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-08-10 23:43:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/777/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230810_205421:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230810_205425:cmsbot_crab_transferLogs - 0
activity-check.sh 230810_205427:cmsbot_crab_activity - 0
inputFiles-check.sh 230810_205429:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230810_205431:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230810_205433:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230810_205435:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230810_205437:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230810_205439:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230810_205441:cmsbot_crab_numCores - 0
scriptExe-check.sh 230810_205443:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230810_205445:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230810_205446:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230810_205527:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230810_205529:cmsbot_crab_inputDBS - 0
useParent-check.sh 230810_205530:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230810_205532:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230810_205534:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230810_205536:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230810_205538:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230810_205539:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230810_205541:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230810_205542:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230810_205544:cmsbot_crab_whitelist - 0
blacklist-check.sh 230810_205545:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230810_205547:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230810_205549:cmsbot_crab_voRole - 0
voGroup-check.sh 230810_205550:cmsbot_crab_voGroup - 0
scheddName-check.sh 230810_205551:cmsbot_crab_scheddName - 0
collector-check.sh 230810_205553:cmsbot_crab_collector - 0
extraJDL-check.sh 230810_205555:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-10T21:59:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-10 23:59:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/531/console

```
{'TN': '230810_205557:cmsbot_crab_20230810_225556', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230810_205558:cmsbot_crab_20230810_225558', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230810_205600:cmsbot_crab_20230810_225559', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205601:cmsbot_crab_20230810_225601', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205603:cmsbot_crab_20230810_225602', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 99, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230810_205606:cmsbot_crab_20230810_225604', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-08-10T23:02:55Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-08-11 01:02:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/533/console

```
{'TN': '230810_205557:cmsbot_crab_20230810_225556', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205558:cmsbot_crab_20230810_225558', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205600:cmsbot_crab_20230810_225559', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205601:cmsbot_crab_20230810_225601', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205603:cmsbot_crab_20230810_225602', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 99}, 'combinedStatus': 'FAILED'}
{'TN': '230810_205606:cmsbot_crab_20230810_225604', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-08-11T11:04:47Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 0. Test is done.
**Finished at:** 2023-08-11 13:04:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/535/console

```
{'TN': '230810_205557:cmsbot_crab_20230810_225556', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205558:cmsbot_crab_20230810_225558', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205600:cmsbot_crab_20230810_225559', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205601:cmsbot_crab_20230810_225601', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205603:cmsbot_crab_20230810_225602', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205606:cmsbot_crab_20230810_225604', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-08-11T11:08:28Z)

all OK
