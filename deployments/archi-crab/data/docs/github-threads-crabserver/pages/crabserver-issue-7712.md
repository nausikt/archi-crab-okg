# dmwm/CRABServer issue #7712: #421: Test dev CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-06-30T23:13:24Z
Closed: 2023-07-01T12:14:22Z
URL: https://github.com/dmwm/CRABServer/issues/7712

## Opening post (cmsdmwmbot, 2023-06-30T23:13:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-07-01 01:13:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/421/)

## Comment (cmsdmwmbot, 2023-06-30T23:15:16Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230630_231424:cmsbot_crab_20230701_011424
230630_231425:cmsbot_crab_20230701_011425
230630_231427:cmsbot_crab_20230701_011426
230630_231428:cmsbot_crab_20230701_011427
230630_231429:cmsbot_crab_20230701_011429
230630_231455:cmsbot_crab_20230701_011430
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230630_231341:cmsbot_crab_transferOutputs
230630_231342:cmsbot_crab_transferLogs
230630_231343:cmsbot_crab_activity
230630_231344:cmsbot_crab_inputFiles
230630_231345:cmsbot_crab_disableAutomaticOutputCollection
230630_231347:cmsbot_crab_outputFiles
230630_231348:cmsbot_crab_allowUndistributedCMSSW
230630_231349:cmsbot_crab_maxMemoryMB
230630_231350:cmsbot_crab_maxJobRuntimeMin
230630_231352:cmsbot_crab_numCores
230630_231353:cmsbot_crab_scriptExe
230630_231354:cmsbot_crab_scriptArgs
230630_231355:cmsbot_crab_sendPythonFolder
230630_231400:cmsbot_crab_sendExternalFolder
230630_231401:cmsbot_crab_inputDBS
230630_231402:cmsbot_crab_useParent
230630_231404:cmsbot_crab_secondaryInputDataset
230630_231405:cmsbot_crab_lumiMaskFile
230630_231406:cmsbot_crab_lumiMaskUrl
230630_231408:cmsbot_crab_outLFNDirBase
230630_231410:cmsbot_crab_runRange
230630_231411:cmsbot_crab_ignoreLocality
230630_231412:cmsbot_crab_userInputFiles
230630_231413:cmsbot_crab_whitelist
230630_231415:cmsbot_crab_blacklist
230630_231416:cmsbot_crab_ignoreGlobalBlacklist
230630_231417:cmsbot_crab_voRole
230630_231419:cmsbot_crab_voGroup
230630_231420:cmsbot_crab_scheddName
230630_231421:cmsbot_crab_collector
230630_231422:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230630_231339:cmsbot_crab_20230701_011339
```

Finished at: 2023-07-01 01:14:55
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/421/console)

## Comment (cmsdmwmbot, 2023-06-30T23:36:09Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-01 01:36:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/357/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/357//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-30T23:36:55Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-01 01:36:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/671/console

```
RETRY TESTS:
numCores-check.sh 230630_231352:cmsbot_crab_numCores - 2
scriptExe-check.sh 230630_231353:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 230630_231406:cmsbot_crab_lumiMaskUrl - 2
whitelist-check.sh 230630_231413:cmsbot_crab_whitelist - 2
blacklist-check.sh 230630_231415:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 230630_231344:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_231345:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_231347:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_231348:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_231349:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230630_231350:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 230630_231354:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_231355:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_231400:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_231401:cmsbot_crab_inputDBS - 0
useParent-check.sh 230630_231402:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230630_231404:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230630_231405:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230630_231408:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230630_231410:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230630_231411:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_231412:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230630_231416:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230630_231417:cmsbot_crab_voRole - 0
voGroup-check.sh 230630_231419:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_231420:cmsbot_crab_scheddName - 0
collector-check.sh 230630_231421:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_231422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 230630_231341:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230630_231342:cmsbot_crab_transferLogs - 1
activity-check.sh 230630_231343:cmsbot_crab_activity - 1
```

## Comment (cmsdmwmbot, 2023-06-30T23:58:46Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-01 01:58:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/673/console

```
RETRY TESTS:
whitelist-check.sh 230630_231413:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_231341:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_231342:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_231343:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_231344:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_231345:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_231347:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_231348:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_231349:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230630_231350:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230630_231352:cmsbot_crab_numCores - 0
scriptExe-check.sh 230630_231353:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230630_231354:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_231355:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_231400:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_231401:cmsbot_crab_inputDBS - 0
useParent-check.sh 230630_231402:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230630_231404:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230630_231405:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230630_231406:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230630_231408:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230630_231410:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230630_231411:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_231412:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230630_231415:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230630_231416:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230630_231417:cmsbot_crab_voRole - 0
voGroup-check.sh 230630_231419:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_231420:cmsbot_crab_scheddName - 0
collector-check.sh 230630_231421:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_231422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-01T00:17:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-01 02:17:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/464/console

```
{'TN': '230630_231424:cmsbot_crab_20230701_011424', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 994, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230630_231425:cmsbot_crab_20230701_011425', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230630_231427:cmsbot_crab_20230701_011426', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230630_231428:cmsbot_crab_20230701_011427', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230630_231429:cmsbot_crab_20230701_011429', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230630_231455:cmsbot_crab_20230701_011430', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-07-01T00:20:56Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-07-01 02:20:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/675/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_231341:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_231342:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_231343:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_231344:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_231345:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_231347:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_231348:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_231349:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230630_231350:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230630_231352:cmsbot_crab_numCores - 0
scriptExe-check.sh 230630_231353:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230630_231354:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_231355:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_231400:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_231401:cmsbot_crab_inputDBS - 0
useParent-check.sh 230630_231402:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230630_231404:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230630_231405:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230630_231406:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230630_231408:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230630_231410:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230630_231411:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_231412:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230630_231413:cmsbot_crab_whitelist - 0
blacklist-check.sh 230630_231415:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230630_231416:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230630_231417:cmsbot_crab_voRole - 0
voGroup-check.sh 230630_231419:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_231420:cmsbot_crab_scheddName - 0
collector-check.sh 230630_231421:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_231422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-01T01:20:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-01 03:20:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/465/console

```
{'TN': '230630_231424:cmsbot_crab_20230701_011424', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230630_231425:cmsbot_crab_20230701_011425', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230630_231427:cmsbot_crab_20230701_011426', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230630_231428:cmsbot_crab_20230701_011427', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230630_231429:cmsbot_crab_20230701_011429', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230630_231455:cmsbot_crab_20230701_011430', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-07-01T02:23:30Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-07-01 04:23:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/466/console

```
{'TN': '230630_231424:cmsbot_crab_20230701_011424', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230630_231425:cmsbot_crab_20230701_011425', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230630_231427:cmsbot_crab_20230701_011426', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230630_231428:cmsbot_crab_20230701_011427', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230630_231429:cmsbot_crab_20230701_011429', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230630_231455:cmsbot_crab_20230701_011430', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-07-01T12:14:21Z)

all OK
