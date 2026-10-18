# dmwm/CRABServer issue #7508: #369: Test prod CRABClient using test2 REST instance and CMSSW_12_5_2_patch1 CMSSW release

State: closed
Opened: 2023-01-27T12:02:37Z
Closed: 2023-01-27T14:34:39Z
URL: https://github.com/dmwm/CRABServer/issues/7508

## Opening post (cmsdmwmbot, 2023-01-27T12:02:37Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_5_2_patch1**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-01-27 13:02:36
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/369/)

## Comment (cmsdmwmbot, 2023-01-27T12:04:50Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230127_120416:cmsbot_crab_20230127_130415
230127_120417:cmsbot_crab_20230127_130417
230127_120419:cmsbot_crab_20230127_130418
230127_120420:cmsbot_crab_20230127_130420
230127_120422:cmsbot_crab_20230127_130421
230127_120428:cmsbot_crab_20230127_130423
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230127_120317:cmsbot_crab_transferOutputs
230127_120319:cmsbot_crab_transferLogs
230127_120320:cmsbot_crab_activity
230127_120322:cmsbot_crab_inputFiles
230127_120323:cmsbot_crab_disableAutomaticOutputCollection
230127_120325:cmsbot_crab_outputFiles
230127_120327:cmsbot_crab_allowUndistributedCMSSW
230127_120328:cmsbot_crab_maxMemoryMB
230127_120330:cmsbot_crab_maxJobRuntimeMin
230127_120331:cmsbot_crab_numCores
230127_120333:cmsbot_crab_scriptExe
230127_120334:cmsbot_crab_scriptArgs
230127_120336:cmsbot_crab_sendPythonFolder
230127_120348:cmsbot_crab_sendExternalFolder
230127_120349:cmsbot_crab_inputDBS
230127_120351:cmsbot_crab_useParent
230127_120352:cmsbot_crab_secondaryInputDataset
230127_120353:cmsbot_crab_lumiMaskFile
230127_120355:cmsbot_crab_lumiMaskUrl
230127_120357:cmsbot_crab_outLFNDirBase
230127_120359:cmsbot_crab_runRange
230127_120400:cmsbot_crab_ignoreLocality
230127_120402:cmsbot_crab_userInputFiles
230127_120403:cmsbot_crab_whitelist
230127_120405:cmsbot_crab_blacklist
230127_120406:cmsbot_crab_ignoreGlobalBlacklist
230127_120408:cmsbot_crab_voRole
230127_120409:cmsbot_crab_voGroup
230127_120411:cmsbot_crab_scheddName
230127_120412:cmsbot_crab_collector
230127_120414:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230127_120315:cmsbot_crab_20230127_130314
```

Finished at: 2023-01-27 13:04:29
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/369/console)

## Comment (cmsdmwmbot, 2023-01-27T12:25:53Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-01-27 13:25:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/331/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/331//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-01-27T12:27:47Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-01-27 13:27:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/566/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230127_120355:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230127_120359:cmsbot_crab_runRange - 2
whitelist-check.sh 230127_120403:cmsbot_crab_whitelist - 2
blacklist-check.sh 230127_120405:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230127_120317:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230127_120319:cmsbot_crab_transferLogs - 0
activity-check.sh 230127_120320:cmsbot_crab_activity - 0
inputFiles-check.sh 230127_120322:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230127_120323:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230127_120327:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230127_120328:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230127_120330:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230127_120331:cmsbot_crab_numCores - 0
scriptExe-check.sh 230127_120333:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230127_120334:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230127_120336:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230127_120348:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230127_120349:cmsbot_crab_inputDBS - 0
useParent-check.sh 230127_120351:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230127_120352:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230127_120353:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230127_120357:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230127_120400:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230127_120402:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230127_120406:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230127_120408:cmsbot_crab_voRole - 0
voGroup-check.sh 230127_120409:cmsbot_crab_voGroup - 0
scheddName-check.sh 230127_120411:cmsbot_crab_scheddName - 0
collector-check.sh 230127_120412:cmsbot_crab_collector - 0
extraJDL-check.sh 230127_120414:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 230127_120325:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2023-01-27T12:49:58Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-01-27 13:49:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/567/console

```
RETRY TESTS:
runRange-check.sh 230127_120359:cmsbot_crab_runRange - 2
whitelist-check.sh 230127_120403:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230127_120317:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230127_120319:cmsbot_crab_transferLogs - 0
activity-check.sh 230127_120320:cmsbot_crab_activity - 0
inputFiles-check.sh 230127_120322:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230127_120323:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230127_120327:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230127_120328:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230127_120330:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230127_120331:cmsbot_crab_numCores - 0
scriptExe-check.sh 230127_120333:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230127_120334:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230127_120336:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230127_120348:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230127_120349:cmsbot_crab_inputDBS - 0
useParent-check.sh 230127_120351:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230127_120352:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230127_120353:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230127_120355:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230127_120357:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230127_120400:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230127_120402:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230127_120405:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230127_120406:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230127_120408:cmsbot_crab_voRole - 0
voGroup-check.sh 230127_120409:cmsbot_crab_voGroup - 0
scheddName-check.sh 230127_120411:cmsbot_crab_scheddName - 0
collector-check.sh 230127_120412:cmsbot_crab_collector - 0
extraJDL-check.sh 230127_120414:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 230127_120325:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2023-01-27T13:07:15Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-01-27 14:07:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/419/console

```
{'TN': '230127_120416:cmsbot_crab_20230127_130415', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 987, 'transferring': 7, 'running': 6}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230127_120417:cmsbot_crab_20230127_130417', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 3, 'transferring': 1, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230127_120419:cmsbot_crab_20230127_130418', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_120420:cmsbot_crab_20230127_130420', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'finished': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230127_120422:cmsbot_crab_20230127_130421', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230127_120428:cmsbot_crab_20230127_130423', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-01-27T13:12:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-01-27 14:12:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/568/console

```
RETRY TESTS:
runRange-check.sh 230127_120359:cmsbot_crab_runRange - 2
whitelist-check.sh 230127_120403:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230127_120317:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230127_120319:cmsbot_crab_transferLogs - 0
activity-check.sh 230127_120320:cmsbot_crab_activity - 0
inputFiles-check.sh 230127_120322:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230127_120323:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230127_120327:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230127_120328:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230127_120330:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230127_120331:cmsbot_crab_numCores - 0
scriptExe-check.sh 230127_120333:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230127_120334:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230127_120336:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230127_120348:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230127_120349:cmsbot_crab_inputDBS - 0
useParent-check.sh 230127_120351:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230127_120352:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230127_120353:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230127_120355:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230127_120357:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230127_120400:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230127_120402:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230127_120405:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230127_120406:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230127_120408:cmsbot_crab_voRole - 0
voGroup-check.sh 230127_120409:cmsbot_crab_voGroup - 0
scheddName-check.sh 230127_120411:cmsbot_crab_scheddName - 0
collector-check.sh 230127_120412:cmsbot_crab_collector - 0
extraJDL-check.sh 230127_120414:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 230127_120325:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2023-01-27T13:34:31Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-01-27 14:34:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/569/console

```
RETRY TESTS:
runRange-check.sh 230127_120359:cmsbot_crab_runRange - 2
whitelist-check.sh 230127_120403:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230127_120317:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230127_120319:cmsbot_crab_transferLogs - 0
activity-check.sh 230127_120320:cmsbot_crab_activity - 0
inputFiles-check.sh 230127_120322:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230127_120323:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230127_120327:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230127_120328:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230127_120330:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230127_120331:cmsbot_crab_numCores - 0
scriptExe-check.sh 230127_120333:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230127_120334:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230127_120336:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230127_120348:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230127_120349:cmsbot_crab_inputDBS - 0
useParent-check.sh 230127_120351:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230127_120352:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230127_120353:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230127_120355:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230127_120357:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230127_120400:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230127_120402:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230127_120405:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230127_120406:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230127_120408:cmsbot_crab_voRole - 0
voGroup-check.sh 230127_120409:cmsbot_crab_voGroup - 0
scheddName-check.sh 230127_120411:cmsbot_crab_scheddName - 0
collector-check.sh 230127_120412:cmsbot_crab_collector - 0
extraJDL-check.sh 230127_120414:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 230127_120325:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2023-01-27T13:39:52Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-01-27 14:39:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/570/console

```
RETRY TESTS:
runRange-check.sh 230127_120359:cmsbot_crab_runRange - 2
whitelist-check.sh 230127_120403:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230127_120317:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230127_120319:cmsbot_crab_transferLogs - 0
activity-check.sh 230127_120320:cmsbot_crab_activity - 0
inputFiles-check.sh 230127_120322:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230127_120323:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230127_120325:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230127_120327:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230127_120328:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230127_120330:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230127_120331:cmsbot_crab_numCores - 0
scriptExe-check.sh 230127_120333:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230127_120334:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230127_120336:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230127_120348:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230127_120349:cmsbot_crab_inputDBS - 0
useParent-check.sh 230127_120351:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230127_120352:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230127_120353:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230127_120355:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230127_120357:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230127_120400:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230127_120402:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230127_120405:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230127_120406:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230127_120408:cmsbot_crab_voRole - 0
voGroup-check.sh 230127_120409:cmsbot_crab_voGroup - 0
scheddName-check.sh 230127_120411:cmsbot_crab_scheddName - 0
collector-check.sh 230127_120412:cmsbot_crab_collector - 0
extraJDL-check.sh 230127_120414:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-01-27T14:09:45Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-01-27 15:09:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/420/console

```
{'TN': '230127_120416:cmsbot_crab_20230127_130415', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 998}, 'combinedStatus': 'FAILED'}
{'TN': '230127_120417:cmsbot_crab_20230127_130417', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 0, 'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230127_120419:cmsbot_crab_20230127_130418', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_120420:cmsbot_crab_20230127_130420', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_120422:cmsbot_crab_20230127_130421', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_120428:cmsbot_crab_20230127_130423', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-01-27T14:34:39Z)

all failures are "known limitations in our testing". Overall: success.
