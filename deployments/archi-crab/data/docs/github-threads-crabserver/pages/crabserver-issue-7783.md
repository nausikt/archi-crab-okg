# dmwm/CRABServer issue #7783: #447: Test prod CRABClient using test11 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-20T17:04:06Z
Closed: 2023-07-21T13:20:18Z
URL: https://github.com/dmwm/CRABServer/issues/7783

## Opening post (cmsdmwmbot, 2023-07-20T17:04:06Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test11**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-07-20 19:04:06
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/447/)

## Comment (cmsdmwmbot, 2023-07-20T17:06:12Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230720_170543:cmsbot_crab_20230720_190542
230720_170544:cmsbot_crab_20230720_190544
230720_170545:cmsbot_crab_20230720_190545
230720_170547:cmsbot_crab_20230720_190546
230720_170548:cmsbot_crab_20230720_190547
230720_170551:cmsbot_crab_20230720_190549
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230720_170426:cmsbot_crab_transferOutputs
230720_170427:cmsbot_crab_transferLogs
230720_170428:cmsbot_crab_activity
230720_170429:cmsbot_crab_inputFiles
230720_170431:cmsbot_crab_disableAutomaticOutputCollection
230720_170432:cmsbot_crab_outputFiles
230720_170433:cmsbot_crab_allowUndistributedCMSSW
230720_170434:cmsbot_crab_maxMemoryMB
230720_170436:cmsbot_crab_maxJobRuntimeMin
230720_170437:cmsbot_crab_numCores
230720_170438:cmsbot_crab_scriptExe
230720_170439:cmsbot_crab_scriptArgs
230720_170441:cmsbot_crab_sendPythonFolder
230720_170519:cmsbot_crab_sendExternalFolder
230720_170520:cmsbot_crab_inputDBS
230720_170521:cmsbot_crab_useParent
230720_170523:cmsbot_crab_secondaryInputDataset
230720_170524:cmsbot_crab_lumiMaskFile
230720_170525:cmsbot_crab_lumiMaskUrl
230720_170527:cmsbot_crab_outLFNDirBase
230720_170529:cmsbot_crab_runRange
230720_170530:cmsbot_crab_ignoreLocality
230720_170531:cmsbot_crab_userInputFiles
230720_170532:cmsbot_crab_whitelist
230720_170534:cmsbot_crab_blacklist
230720_170535:cmsbot_crab_ignoreGlobalBlacklist
230720_170536:cmsbot_crab_voRole
230720_170537:cmsbot_crab_voGroup
230720_170538:cmsbot_crab_scheddName
230720_170540:cmsbot_crab_collector
230720_170541:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230720_170424:cmsbot_crab_20230720_190423
```

Finished at: 2023-07-20 19:05:51
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/447/console)

## Comment (mapellidario, 2023-07-20T17:06:37Z)

Testing crabserver+taskworker with py3-htcondor (no surprises expected). images built with https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_BuildOnRelease/117/.
If this is ok, I would close #7736

## Comment (cmsdmwmbot, 2023-07-20T17:27:11Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-20 19:27:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/370/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/370//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-20T17:27:56Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-20 19:27:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/761/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230720_170434:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230720_170436:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230720_170437:cmsbot_crab_numCores - 2
scriptExe-check.sh 230720_170438:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230720_170439:cmsbot_crab_scriptArgs - 2
secondaryInputDataset-check.sh 230720_170523:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230720_170525:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_170529:cmsbot_crab_runRange - 2
blacklist-check.sh 230720_170534:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230720_170535:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230720_170536:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_170426:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_170427:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_170428:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_170429:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_170431:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_170432:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_170433:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230720_170441:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_170519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_170520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_170521:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230720_170524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_170527:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_170530:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_170531:cmsbot_crab_userInputFiles - 0
voGroup-check.sh 230720_170537:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_170538:cmsbot_crab_scheddName - 0
collector-check.sh 230720_170540:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_170541:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_170532:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2023-07-20T17:49:38Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-20 19:49:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/762/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230720_170434:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230720_170436:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230720_170437:cmsbot_crab_numCores - 2
secondaryInputDataset-check.sh 230720_170523:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230720_170525:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_170529:cmsbot_crab_runRange - 2
blacklist-check.sh 230720_170534:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230720_170535:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230720_170536:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_170426:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_170427:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_170428:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_170429:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_170431:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_170432:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_170433:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 230720_170438:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_170439:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_170441:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_170519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_170520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_170521:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230720_170524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_170527:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_170530:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_170531:cmsbot_crab_userInputFiles - 0
voGroup-check.sh 230720_170537:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_170538:cmsbot_crab_scheddName - 0
collector-check.sh 230720_170540:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_170541:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_170532:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2023-07-20T18:08:26Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-20 20:08:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/515/console

```
{'TN': '230720_170543:cmsbot_crab_20230720_190542', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 443, 'transferring': 554, 'running': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170544:cmsbot_crab_20230720_190544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170545:cmsbot_crab_20230720_190545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230720_170547:cmsbot_crab_20230720_190546', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170548:cmsbot_crab_20230720_190547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 32, 'transferring': 68}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170551:cmsbot_crab_20230720_190549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-20T18:11:30Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-20 20:11:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/763/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 230720_170523:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230720_170525:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_170529:cmsbot_crab_runRange - 2
ignoreGlobalBlacklist-check.sh 230720_170535:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230720_170536:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_170426:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_170427:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_170428:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_170429:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_170431:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_170432:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_170433:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230720_170434:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230720_170436:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230720_170437:cmsbot_crab_numCores - 0
scriptExe-check.sh 230720_170438:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_170439:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_170441:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_170519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_170520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_170521:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230720_170524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_170527:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_170530:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_170531:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230720_170534:cmsbot_crab_blacklist - 0
voGroup-check.sh 230720_170537:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_170538:cmsbot_crab_scheddName - 0
collector-check.sh 230720_170540:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_170541:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_170532:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2023-07-20T18:33:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-20 20:33:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/764/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 230720_170523:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230720_170525:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_170529:cmsbot_crab_runRange - 2
ignoreGlobalBlacklist-check.sh 230720_170535:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230720_170536:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_170426:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_170427:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_170428:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_170429:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_170431:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_170432:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_170433:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230720_170434:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230720_170436:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230720_170437:cmsbot_crab_numCores - 0
scriptExe-check.sh 230720_170438:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_170439:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_170441:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_170519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_170520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_170521:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230720_170524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_170527:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_170530:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_170531:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230720_170534:cmsbot_crab_blacklist - 0
voGroup-check.sh 230720_170537:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_170538:cmsbot_crab_scheddName - 0
collector-check.sh 230720_170540:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_170541:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_170532:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2023-07-20T18:55:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-20 20:55:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/765/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 230720_170523:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230720_170525:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_170529:cmsbot_crab_runRange - 2
ignoreGlobalBlacklist-check.sh 230720_170535:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230720_170536:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_170426:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_170427:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_170428:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_170429:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_170431:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_170432:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_170433:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230720_170434:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230720_170436:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230720_170437:cmsbot_crab_numCores - 0
scriptExe-check.sh 230720_170438:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_170439:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_170441:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_170519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_170520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_170521:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230720_170524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_170527:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_170530:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_170531:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230720_170534:cmsbot_crab_blacklist - 0
voGroup-check.sh 230720_170537:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_170538:cmsbot_crab_scheddName - 0
collector-check.sh 230720_170540:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_170541:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_170532:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2023-07-20T19:10:26Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-20 21:10:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/516/console

```
{'TN': '230720_170543:cmsbot_crab_20230720_190542', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 510, 'transferring': 489}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170544:cmsbot_crab_20230720_190544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230720_170545:cmsbot_crab_20230720_190545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230720_170547:cmsbot_crab_20230720_190546', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170548:cmsbot_crab_20230720_190547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 43, 'transferring': 57}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170551:cmsbot_crab_20230720_190549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-20T20:12:53Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-20 22:12:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/517/console

```
{'TN': '230720_170543:cmsbot_crab_20230720_190542', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 562, 'transferring': 437}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170544:cmsbot_crab_20230720_190544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230720_170545:cmsbot_crab_20230720_190545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230720_170547:cmsbot_crab_20230720_190546', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170548:cmsbot_crab_20230720_190547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 47, 'transferring': 53}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170551:cmsbot_crab_20230720_190549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-20T21:16:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-20 23:16:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/518/console

```
{'TN': '230720_170543:cmsbot_crab_20230720_190542', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 577, 'transferring': 422}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170544:cmsbot_crab_20230720_190544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230720_170545:cmsbot_crab_20230720_190545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230720_170547:cmsbot_crab_20230720_190546', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170548:cmsbot_crab_20230720_190547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 47, 'transferring': 53}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170551:cmsbot_crab_20230720_190549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-20T22:20:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-21 00:20:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/519/console

```
{'TN': '230720_170543:cmsbot_crab_20230720_190542', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 583, 'transferring': 416}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170544:cmsbot_crab_20230720_190544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230720_170545:cmsbot_crab_20230720_190545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230720_170547:cmsbot_crab_20230720_190546', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170548:cmsbot_crab_20230720_190547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 47, 'transferring': 53}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230720_170551:cmsbot_crab_20230720_190549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (mapellidario, 2023-07-21T13:20:18Z)

CCV:

- [x] `230720_170532:cmsbot_crab_whitelist` was not submitted because the whitelist that we set is `['T2_DE_DESY']`, which is [currently down](https://cmssst.web.cern.ch/siteStatus/detail.html?site=T2_DE_DESY) https://github.com/dmwm/CRABServer/blob/1ebaa01e363c4ed6c0e31564f1590548a7dfb962/test/makeTests.py#L493

- [x] `230720_170529:cmsbot_crab_runRange`, postjob is still running, but the job run at mit, whose site readiness is intermittent in the last couple of days. I do not see why this can be our fault

Status tracking

- [x] `230720_170543:cmsbot_crab_20230720_190542` the only [job](https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/230720_170543:cmsbot_crab_20230720_190542/job_out.100.0.txt) that run at MIT failed. the job did print a single line to stdout, weird... maybe a storage problem? i do not see why this may be realated to a change to tw condor version.
- [x] `230720_170548:cmsbot_crab_20230720_190547` one job running at vanderbilt, it took 15min per event and run out of time [1]. likely a storage problem

---

[1]

<details>

from: https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/230720_170548:cmsbot_crab_20230720_190547/job_out.23.1.txt

```plaintext
======== Checking execution of user application (cmsRun and scriptExe) Fri Jul 21 06:42:55 GMT 2023========
the file cmsRun-stdout.log.tmp exists
the file cmsRun-stdout.log.tmp is non-empty. wc (newlines, words, bytes):  6 88 823 cmsRun-stdout.log.tmp
21-Jul-2023 00:59:40 CDT  Initiating request to open file file:/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root
21-Jul-2023 01:00:52 CDT  Successfully opened file file:/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root
Begin processing the 1st record. Run 1, Event 210601, LumiSection 703 on stream 0 at 21-Jul-2023 01:16:51.335 CDT
Begin processing the 2nd record. Run 1, Event 210602, LumiSection 703 on stream 0 at 21-Jul-2023 01:24:38.008 CDT
Begin processing the 3rd record. Run 1, Event 210603, LumiSection 703 on stream 0 at 21-Jul-2023 01:33:16.598 CDT
Begin processing the 4th record. Run 1, Event 210604, LumiSection 703 on stream 0 at 21-Jul-2023 01:40:14.874 CDT
[...]
```

</details>
