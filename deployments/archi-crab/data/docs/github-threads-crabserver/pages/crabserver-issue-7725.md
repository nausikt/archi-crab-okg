# dmwm/CRABServer issue #7725: #426: Test prod CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2023-07-07T16:33:40Z
Closed: 2023-07-07T21:48:28Z
URL: https://github.com/dmwm/CRABServer/issues/7725

## Opening post (cmsdmwmbot, 2023-07-07T16:33:40Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-07-07 18:33:39
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/426/)

## Comment (cmsdmwmbot, 2023-07-07T16:36:07Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230707_163520:cmsbot_crab_20230707_183518
230707_163522:cmsbot_crab_20230707_183520
230707_163524:cmsbot_crab_20230707_183522
230707_163526:cmsbot_crab_20230707_183524
230707_163528:cmsbot_crab_20230707_183526
230707_163546:cmsbot_crab_20230707_183528
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230707_163414:cmsbot_crab_transferOutputs
230707_163416:cmsbot_crab_transferLogs
230707_163418:cmsbot_crab_activity
230707_163421:cmsbot_crab_inputFiles
230707_163423:cmsbot_crab_disableAutomaticOutputCollection
230707_163426:cmsbot_crab_outputFiles
230707_163428:cmsbot_crab_allowUndistributedCMSSW
230707_163430:cmsbot_crab_maxMemoryMB
230707_163432:cmsbot_crab_maxJobRuntimeMin
230707_163435:cmsbot_crab_numCores
230707_163437:cmsbot_crab_scriptExe
230707_163439:cmsbot_crab_scriptArgs
230707_163442:cmsbot_crab_sendPythonFolder
230707_163448:cmsbot_crab_sendExternalFolder
230707_163449:cmsbot_crab_inputDBS
230707_163451:cmsbot_crab_useParent
230707_163453:cmsbot_crab_secondaryInputDataset
230707_163455:cmsbot_crab_lumiMaskFile
230707_163457:cmsbot_crab_outLFNDirBase
230707_163458:cmsbot_crab_runRange
230707_163500:cmsbot_crab_ignoreLocality
230707_163501:cmsbot_crab_userInputFiles
230707_163503:cmsbot_crab_whitelist
230707_163505:cmsbot_crab_blacklist
230707_163508:cmsbot_crab_ignoreGlobalBlacklist
230707_163510:cmsbot_crab_voRole
230707_163512:cmsbot_crab_voGroup
230707_163514:cmsbot_crab_scheddName
230707_163516:cmsbot_crab_collector
230707_163517:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230707_163412:cmsbot_crab_20230707_183409
```

Finished at: 2023-07-07 18:35:46
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/426/console)

## Comment (cmsdmwmbot, 2023-07-07T16:57:20Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-07 18:57:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/361/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/361//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-07T16:58:58Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 18:58:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/680/console

```
RETRY TESTS:
transferLogs-check.sh 230707_163416:cmsbot_crab_transferLogs - 2
activity-check.sh 230707_163418:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 230707_163430:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230707_163432:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 230707_163437:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230707_163439:cmsbot_crab_scriptArgs - 2
useParent-check.sh 230707_163451:cmsbot_crab_useParent - 2
blacklist-check.sh 230707_163505:cmsbot_crab_blacklist - 2
voRole-check.sh 230707_163510:cmsbot_crab_voRole - 2
voGroup-check.sh 230707_163512:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163414:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230707_163421:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163423:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163426:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163428:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230707_163442:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163448:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163449:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230707_163453:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163455:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_163457:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_163458:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_163500:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163501:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163503:cmsbot_crab_whitelist - 0
scheddName-check.sh 230707_163514:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163516:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163517:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 230707_163435:cmsbot_crab_numCores - 1
ignoreGlobalBlacklist-check.sh 230707_163508:cmsbot_crab_ignoreGlobalBlacklist - 1
```

## Comment (cmsdmwmbot, 2023-07-07T17:24:12Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-07 19:24:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/684/console

```
RETRY TESTS:
transferLogs-check.sh 230707_163416:cmsbot_crab_transferLogs - 2
maxJobRuntimeMin-check.sh 230707_163432:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230707_163435:cmsbot_crab_numCores - 2
useParent-check.sh 230707_163451:cmsbot_crab_useParent - 2
blacklist-check.sh 230707_163505:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230707_163508:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163414:cmsbot_crab_transferOutputs - 0
activity-check.sh 230707_163418:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163421:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163423:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163426:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163428:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163430:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 230707_163437:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163439:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163442:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163448:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163449:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230707_163453:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163455:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_163457:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_163458:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_163500:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163501:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163503:cmsbot_crab_whitelist - 0
voRole-check.sh 230707_163510:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163512:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163514:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163516:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163517:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T17:38:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 19:38:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/471/console

```
{'TN': '230707_163520:cmsbot_crab_20230707_183518', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 949, 'transferring': 3, 'running': 48}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163522:cmsbot_crab_20230707_183520', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'finished': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163524:cmsbot_crab_20230707_183522', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'finished': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163526:cmsbot_crab_20230707_183524', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'running': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163528:cmsbot_crab_20230707_183526', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 29, 'finished': 71}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163546:cmsbot_crab_20230707_183528', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-07-07T17:49:31Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-07 19:49:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/689/console

```
RETRY TESTS:
useParent-check.sh 230707_163451:cmsbot_crab_useParent - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163414:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163416:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163418:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163421:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163423:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163426:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163428:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163430:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163432:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163435:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163437:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163439:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163442:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163448:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163449:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230707_163453:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163455:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_163457:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_163458:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_163500:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163501:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163503:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163505:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163508:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163510:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163512:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163514:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163516:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163517:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T18:14:39Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-07 20:14:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/694/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163414:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163416:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163418:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163421:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163423:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163426:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163428:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163430:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163432:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163435:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163437:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163439:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163442:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163448:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163449:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230707_163453:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163455:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_163457:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_163458:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_163500:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163501:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163503:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163505:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163508:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163510:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163512:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163514:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163516:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163517:cmsbot_crab_extraJDL - 0

FAILED TESTS:
useParent-check.sh 230707_163451:cmsbot_crab_useParent - 1
```

## Comment (cmsdmwmbot, 2023-07-07T18:41:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-07 20:41:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/476/console

```
{'TN': '230707_163520:cmsbot_crab_20230707_183518', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 997, 'running': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163522:cmsbot_crab_20230707_183520', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163524:cmsbot_crab_20230707_183522', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 2}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163526:cmsbot_crab_20230707_183524', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'running': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163528:cmsbot_crab_20230707_183526', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163546:cmsbot_crab_20230707_183528', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-07-07T19:44:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-07 21:44:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/479/console

```
{'TN': '230707_163520:cmsbot_crab_20230707_183518', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163522:cmsbot_crab_20230707_183520', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163524:cmsbot_crab_20230707_183522', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 2}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163526:cmsbot_crab_20230707_183524', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'running': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163528:cmsbot_crab_20230707_183526', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163546:cmsbot_crab_20230707_183528', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-07-07T19:52:08Z)

useParent is doomed on CMSSW_7, parent is not on disk

## Comment (cmsdmwmbot, 2023-07-07T20:46:48Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-07 22:46:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/483/console

```
{'TN': '230707_163520:cmsbot_crab_20230707_183518', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163522:cmsbot_crab_20230707_183520', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163524:cmsbot_crab_20230707_183522', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 2}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163526:cmsbot_crab_20230707_183524', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 2, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163528:cmsbot_crab_20230707_183526', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163546:cmsbot_crab_20230707_183528', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-07-07T21:47:12Z)

the last failing job is just stuck in Florida. All is goo.

## Comment (cmsdmwmbot, 2023-07-07T21:49:00Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 4 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-07 23:48:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/486/console

```
{'TN': '230707_163520:cmsbot_crab_20230707_183518', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163522:cmsbot_crab_20230707_183520', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163524:cmsbot_crab_20230707_183522', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 2}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163526:cmsbot_crab_20230707_183524', 'dbStatus': u'KILLED', 'testResult': 'TestFailed', 'jobsPerStatus': {'finished': 9, 'killed': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163528:cmsbot_crab_20230707_183526', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163546:cmsbot_crab_20230707_183528', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```
