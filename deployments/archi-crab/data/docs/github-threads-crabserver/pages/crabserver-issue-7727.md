# dmwm/CRABServer issue #7727: #428: Test prod CRABClient using test2 REST instance and CMSSW_12_5_0 CMSSW release

State: closed
Opened: 2023-07-07T17:13:05Z
Closed: 2023-07-07T20:19:55Z
URL: https://github.com/dmwm/CRABServer/issues/7727

## Opening post (cmsdmwmbot, 2023-07-07T17:13:05Z)

**this is a test of https://github.com/belforte/CRABServer/tree/remove-rm_rest_from-filetransfersdb-fix-7721 on cmsweb-test2**

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_5_0**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-07-07 19:13:04
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/428/)

## Comment (cmsdmwmbot, 2023-07-07T17:15:05Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230707_171422:cmsbot_crab_20230707_191421
230707_171423:cmsbot_crab_20230707_191422
230707_171424:cmsbot_crab_20230707_191424
230707_171426:cmsbot_crab_20230707_191425
230707_171427:cmsbot_crab_20230707_191426
230707_171443:cmsbot_crab_20230707_191428
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230707_171332:cmsbot_crab_transferOutputs
230707_171333:cmsbot_crab_transferLogs
230707_171334:cmsbot_crab_activity
230707_171336:cmsbot_crab_inputFiles
230707_171337:cmsbot_crab_disableAutomaticOutputCollection
230707_171338:cmsbot_crab_outputFiles
230707_171340:cmsbot_crab_allowUndistributedCMSSW
230707_171341:cmsbot_crab_maxMemoryMB
230707_171342:cmsbot_crab_maxJobRuntimeMin
230707_171344:cmsbot_crab_numCores
230707_171345:cmsbot_crab_scriptExe
230707_171347:cmsbot_crab_scriptArgs
230707_171348:cmsbot_crab_sendPythonFolder
230707_171356:cmsbot_crab_sendExternalFolder
230707_171357:cmsbot_crab_inputDBS
230707_171358:cmsbot_crab_useParent
230707_171400:cmsbot_crab_secondaryInputDataset
230707_171401:cmsbot_crab_lumiMaskFile
230707_171403:cmsbot_crab_lumiMaskUrl
230707_171405:cmsbot_crab_outLFNDirBase
230707_171406:cmsbot_crab_runRange
230707_171408:cmsbot_crab_ignoreLocality
230707_171409:cmsbot_crab_userInputFiles
230707_171410:cmsbot_crab_whitelist
230707_171412:cmsbot_crab_blacklist
230707_171413:cmsbot_crab_ignoreGlobalBlacklist
230707_171414:cmsbot_crab_voRole
230707_171416:cmsbot_crab_voGroup
230707_171417:cmsbot_crab_scheddName
230707_171418:cmsbot_crab_collector
230707_171420:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230707_171330:cmsbot_crab_20230707_191328
```

Finished at: 2023-07-07 19:14:44
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/428/console)

## Comment (cmsdmwmbot, 2023-07-07T17:36:00Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-07 19:35:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/363/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/363//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-07T17:37:18Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 19:37:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/687/console

```
RETRY TESTS:
transferLogs-check.sh 230707_171333:cmsbot_crab_transferLogs - 2
activity-check.sh 230707_171334:cmsbot_crab_activity - 2
outputFiles-check.sh 230707_171338:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230707_171341:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230707_171342:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230707_171344:cmsbot_crab_numCores - 2
scriptExe-check.sh 230707_171345:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230707_171347:cmsbot_crab_scriptArgs - 2
secondaryInputDataset-check.sh 230707_171400:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230707_171403:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230707_171405:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230707_171406:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 230707_171408:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 230707_171409:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230707_171410:cmsbot_crab_whitelist - 2
blacklist-check.sh 230707_171412:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230707_171413:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230707_171414:cmsbot_crab_voRole - 2
extraJDL-check.sh 230707_171420:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_171332:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230707_171336:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_171337:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230707_171340:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230707_171348:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_171356:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_171357:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230707_171417:cmsbot_crab_scheddName - 0
collector-check.sh 230707_171418:cmsbot_crab_collector - 0

FAILED TESTS:
useParent-check.sh 230707_171358:cmsbot_crab_useParent - 1
lumiMaskFile-check.sh 230707_171401:cmsbot_crab_lumiMaskFile - 1
voGroup-check.sh 230707_171416:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2023-07-07T17:58:44Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-07 19:58:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/692/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_171332:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230707_171336:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_171337:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230707_171340:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230707_171348:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_171356:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_171357:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230707_171417:cmsbot_crab_scheddName - 0
collector-check.sh 230707_171418:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 230707_171333:cmsbot_crab_transferLogs - 1
activity-check.sh 230707_171334:cmsbot_crab_activity - 1
outputFiles-check.sh 230707_171338:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230707_171341:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230707_171342:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230707_171344:cmsbot_crab_numCores - 1
scriptExe-check.sh 230707_171345:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230707_171347:cmsbot_crab_scriptArgs - 1
useParent-check.sh 230707_171358:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230707_171400:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230707_171401:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230707_171403:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230707_171405:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230707_171406:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230707_171408:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230707_171409:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230707_171410:cmsbot_crab_whitelist - 1
blacklist-check.sh 230707_171412:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230707_171413:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230707_171414:cmsbot_crab_voRole - 1
voGroup-check.sh 230707_171416:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230707_171420:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-07-07T18:17:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 20:17:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/473/console

```
{'TN': '230707_171422:cmsbot_crab_20230707_191421', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 10, 'transferring': 989, 'cooloff': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171423:cmsbot_crab_20230707_191422', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171424:cmsbot_crab_20230707_191424', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171426:cmsbot_crab_20230707_191425', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 10}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171427:cmsbot_crab_20230707_191426', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'idle': 2, 'transferring': 95, 'cooloff': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171443:cmsbot_crab_20230707_191428', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 7, 'running': 3}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-07T19:19:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-07 21:19:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/478/console

```
{'TN': '230707_171422:cmsbot_crab_20230707_191421', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 5, 'transferring': 994, 'cooloff': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171423:cmsbot_crab_20230707_191422', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171424:cmsbot_crab_20230707_191424', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171426:cmsbot_crab_20230707_191425', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 10}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171427:cmsbot_crab_20230707_191426', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'running': 6, 'transferring': 90, 'idle': 1, 'cooloff': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171443:cmsbot_crab_20230707_191428', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 10}, 'combinedStatus': 'FAILED'}
```

## Comment (belforte, 2023-07-07T20:19:55Z)

there was a bug in https://github.com/belforte/CRABServer/tree/remove-rm_rest_from-filetransfersdb-fix-7721
will submit a new test

## Comment (cmsdmwmbot, 2023-07-07T20:21:12Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-07 22:21:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/481/console

```
{'TN': '230707_171422:cmsbot_crab_20230707_191421', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 5, 'transferring': 993, 'cooloff': 1, 'idle': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171423:cmsbot_crab_20230707_191422', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 5}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171424:cmsbot_crab_20230707_191424', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171426:cmsbot_crab_20230707_191425', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 10}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171427:cmsbot_crab_20230707_191426', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 18, 'running': 2, 'transferring': 77, 'idle': 1, 'cooloff': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171443:cmsbot_crab_20230707_191428', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 10}, 'combinedStatus': 'FAILED'}
```

## Comment (cmsdmwmbot, 2023-07-07T21:23:17Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-07 23:23:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/484/console

```
{'TN': '230707_171422:cmsbot_crab_20230707_191421', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 4, 'finished': 989, 'transferring': 7}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171423:cmsbot_crab_20230707_191422', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 5}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171424:cmsbot_crab_20230707_191424', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171426:cmsbot_crab_20230707_191425', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 10}, 'combinedStatus': 'FAILED'}
{'TN': '230707_171427:cmsbot_crab_20230707_191426', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 21, 'finished': 78, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_171443:cmsbot_crab_20230707_191428', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 10}, 'combinedStatus': 'FAILED'}
```
