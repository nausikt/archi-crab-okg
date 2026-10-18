# dmwm/CRABServer issue #7763: #441: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-16T10:23:50Z
Closed: 2023-07-17T07:58:11Z
URL: https://github.com/dmwm/CRABServer/issues/7763

## Opening post (cmsdmwmbot, 2023-07-16T10:23:50Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-07-16 12:23:50
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/441/)

## Comment (cmsdmwmbot, 2023-07-16T10:26:14Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230716_102544:cmsbot_crab_20230716_122544
230716_102546:cmsbot_crab_20230716_122545
230716_102547:cmsbot_crab_20230716_122547
230716_102548:cmsbot_crab_20230716_122548
230716_102550:cmsbot_crab_20230716_122549
230716_102553:cmsbot_crab_20230716_122551
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230716_102413:cmsbot_crab_transferOutputs
230716_102414:cmsbot_crab_transferLogs
230716_102416:cmsbot_crab_activity
230716_102417:cmsbot_crab_inputFiles
230716_102418:cmsbot_crab_disableAutomaticOutputCollection
230716_102419:cmsbot_crab_outputFiles
230716_102421:cmsbot_crab_allowUndistributedCMSSW
230716_102422:cmsbot_crab_maxMemoryMB
230716_102424:cmsbot_crab_maxJobRuntimeMin
230716_102425:cmsbot_crab_numCores
230716_102426:cmsbot_crab_scriptExe
230716_102428:cmsbot_crab_scriptArgs
230716_102429:cmsbot_crab_sendPythonFolder
230716_102516:cmsbot_crab_sendExternalFolder
230716_102518:cmsbot_crab_inputDBS
230716_102519:cmsbot_crab_useParent
230716_102521:cmsbot_crab_secondaryInputDataset
230716_102522:cmsbot_crab_lumiMaskFile
230716_102524:cmsbot_crab_lumiMaskUrl
230716_102526:cmsbot_crab_outLFNDirBase
230716_102528:cmsbot_crab_runRange
230716_102529:cmsbot_crab_ignoreLocality
230716_102532:cmsbot_crab_userInputFiles
230716_102533:cmsbot_crab_whitelist
230716_102534:cmsbot_crab_blacklist
230716_102536:cmsbot_crab_ignoreGlobalBlacklist
230716_102537:cmsbot_crab_voRole
230716_102538:cmsbot_crab_voGroup
230716_102540:cmsbot_crab_scheddName
230716_102541:cmsbot_crab_collector
230716_102542:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230716_102411:cmsbot_crab_20230716_122409
```

Finished at: 2023-07-16 12:25:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/441/console)

## Comment (cmsdmwmbot, 2023-07-16T10:48:26Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-16 12:48:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/366/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/366//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-16T10:50:06Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-16 12:50:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/731/console

```
RETRY TESTS:
outputFiles-check.sh 230716_102419:cmsbot_crab_outputFiles - 2
scriptExe-check.sh 230716_102426:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230716_102428:cmsbot_crab_scriptArgs - 2
secondaryInputDataset-check.sh 230716_102521:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 230716_102522:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230716_102524:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230716_102528:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230716_102532:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230716_102533:cmsbot_crab_whitelist - 2
blacklist-check.sh 230716_102534:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230716_102536:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102413:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102414:cmsbot_crab_transferLogs - 0
activity-check.sh 230716_102416:cmsbot_crab_activity - 0
inputFiles-check.sh 230716_102417:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102418:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230716_102421:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102422:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102424:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102425:cmsbot_crab_numCores - 0
sendPythonFolder-check.sh 230716_102429:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102516:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102518:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102519:cmsbot_crab_useParent - 0
outLFNDirBase-check.sh 230716_102526:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230716_102529:cmsbot_crab_ignoreLocality - 0
voRole-check.sh 230716_102537:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102538:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102540:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102541:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102542:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-16T11:13:19Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-16 13:13:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/733/console

```
RETRY TESTS:
outputFiles-check.sh 230716_102419:cmsbot_crab_outputFiles - 2
scriptExe-check.sh 230716_102426:cmsbot_crab_scriptExe - 2
lumiMaskFile-check.sh 230716_102522:cmsbot_crab_lumiMaskFile - 2
whitelist-check.sh 230716_102533:cmsbot_crab_whitelist - 2
ignoreGlobalBlacklist-check.sh 230716_102536:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102413:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102414:cmsbot_crab_transferLogs - 0
activity-check.sh 230716_102416:cmsbot_crab_activity - 0
inputFiles-check.sh 230716_102417:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102418:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230716_102421:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102422:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102424:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102425:cmsbot_crab_numCores - 0
scriptArgs-check.sh 230716_102428:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230716_102429:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102516:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102518:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102519:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230716_102521:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 230716_102524:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230716_102526:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230716_102528:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230716_102529:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230716_102532:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230716_102534:cmsbot_crab_blacklist - 0
voRole-check.sh 230716_102537:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102538:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102540:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102541:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102542:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-16T11:29:31Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-16 13:29:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/495/console

```
{'TN': '230716_102544:cmsbot_crab_20230716_122544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 879, 'transferring': 119, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102546:cmsbot_crab_20230716_122545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102547:cmsbot_crab_20230716_122547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230716_102548:cmsbot_crab_20230716_122548', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102550:cmsbot_crab_20230716_122549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 82, 'transferring': 18}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102553:cmsbot_crab_20230716_122551', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-16T11:37:28Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-16 13:37:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/735/console

```
RETRY TESTS:
lumiMaskFile-check.sh 230716_102522:cmsbot_crab_lumiMaskFile - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102413:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102414:cmsbot_crab_transferLogs - 0
activity-check.sh 230716_102416:cmsbot_crab_activity - 0
inputFiles-check.sh 230716_102417:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102418:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230716_102419:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230716_102421:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102422:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102424:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102425:cmsbot_crab_numCores - 0
scriptExe-check.sh 230716_102426:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230716_102428:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230716_102429:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102516:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102518:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102519:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230716_102521:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 230716_102524:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230716_102526:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230716_102528:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230716_102529:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230716_102532:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230716_102533:cmsbot_crab_whitelist - 0
blacklist-check.sh 230716_102534:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230716_102536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230716_102537:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102538:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102540:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102541:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102542:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-16T12:01:39Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-16 14:01:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/737/console

```
RETRY TESTS:
lumiMaskFile-check.sh 230716_102522:cmsbot_crab_lumiMaskFile - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102413:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102414:cmsbot_crab_transferLogs - 0
activity-check.sh 230716_102416:cmsbot_crab_activity - 0
inputFiles-check.sh 230716_102417:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102418:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230716_102419:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230716_102421:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102422:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102424:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102425:cmsbot_crab_numCores - 0
scriptExe-check.sh 230716_102426:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230716_102428:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230716_102429:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102516:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102518:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102519:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230716_102521:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 230716_102524:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230716_102526:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230716_102528:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230716_102529:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230716_102532:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230716_102533:cmsbot_crab_whitelist - 0
blacklist-check.sh 230716_102534:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230716_102536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230716_102537:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102538:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102540:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102541:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102542:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-16T12:25:21Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 4. Test is done.
**Finished at:** 2023-07-16 14:25:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/739/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230716_102413:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230716_102414:cmsbot_crab_transferLogs - 0
activity-check.sh 230716_102416:cmsbot_crab_activity - 0
inputFiles-check.sh 230716_102417:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230716_102418:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230716_102419:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230716_102421:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230716_102422:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230716_102424:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230716_102425:cmsbot_crab_numCores - 0
scriptExe-check.sh 230716_102426:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230716_102428:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230716_102429:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230716_102516:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230716_102518:cmsbot_crab_inputDBS - 0
useParent-check.sh 230716_102519:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230716_102521:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230716_102522:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230716_102524:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230716_102526:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230716_102528:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230716_102529:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230716_102532:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230716_102533:cmsbot_crab_whitelist - 0
blacklist-check.sh 230716_102534:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230716_102536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230716_102537:cmsbot_crab_voRole - 0
voGroup-check.sh 230716_102538:cmsbot_crab_voGroup - 0
scheddName-check.sh 230716_102540:cmsbot_crab_scheddName - 0
collector-check.sh 230716_102541:cmsbot_crab_collector - 0
extraJDL-check.sh 230716_102542:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-16T12:31:39Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-16 14:31:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/496/console

```
{'TN': '230716_102544:cmsbot_crab_20230716_122544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 939, 'transferring': 59}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102546:cmsbot_crab_20230716_122545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230716_102547:cmsbot_crab_20230716_122547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230716_102548:cmsbot_crab_20230716_122548', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102550:cmsbot_crab_20230716_122549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 88, 'transferring': 12}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102553:cmsbot_crab_20230716_122551', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-16T13:33:47Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-16 15:33:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/497/console

```
{'TN': '230716_102544:cmsbot_crab_20230716_122544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 967, 'transferring': 31}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102546:cmsbot_crab_20230716_122545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230716_102547:cmsbot_crab_20230716_122547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230716_102548:cmsbot_crab_20230716_122548', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102550:cmsbot_crab_20230716_122549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 94, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102553:cmsbot_crab_20230716_122551', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-16T14:37:30Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-16 16:37:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/498/console

```
{'TN': '230716_102544:cmsbot_crab_20230716_122544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 967, 'transferring': 31}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102546:cmsbot_crab_20230716_122545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230716_102547:cmsbot_crab_20230716_122547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230716_102548:cmsbot_crab_20230716_122548', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102550:cmsbot_crab_20230716_122549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 94, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102553:cmsbot_crab_20230716_122551', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-16T15:39:31Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-16 17:39:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/499/console

```
{'TN': '230716_102544:cmsbot_crab_20230716_122544', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 969, 'transferring': 29}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102546:cmsbot_crab_20230716_122545', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230716_102547:cmsbot_crab_20230716_122547', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230716_102548:cmsbot_crab_20230716_122548', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102550:cmsbot_crab_20230716_122549', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 94, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230716_102553:cmsbot_crab_20230716_122551', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (belforte, 2023-07-17T07:58:11Z)

no failures in DBSDataDiscovery, which is what was being tested
