# dmwm/CRABServer issue #7717: #422: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-05T11:11:50Z
Closed: 2023-07-06T06:02:06Z
URL: https://github.com/dmwm/CRABServer/issues/7717

## Opening post (cmsdmwmbot, 2023-07-05T11:11:50Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-07-05 13:11:49
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/422/)

## Comment (cmsdmwmbot, 2023-07-05T11:14:27Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230705_111357:cmsbot_crab_20230705_131356
230705_111358:cmsbot_crab_20230705_131358
230705_111359:cmsbot_crab_20230705_131359
230705_111401:cmsbot_crab_20230705_131400
230705_111403:cmsbot_crab_20230705_131402
230705_111406:cmsbot_crab_20230705_131404
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230705_111224:cmsbot_crab_transferOutputs
230705_111226:cmsbot_crab_transferLogs
230705_111228:cmsbot_crab_activity
230705_111230:cmsbot_crab_inputFiles
230705_111232:cmsbot_crab_disableAutomaticOutputCollection
230705_111234:cmsbot_crab_outputFiles
230705_111236:cmsbot_crab_allowUndistributedCMSSW
230705_111237:cmsbot_crab_maxMemoryMB
230705_111238:cmsbot_crab_maxJobRuntimeMin
230705_111240:cmsbot_crab_numCores
230705_111242:cmsbot_crab_scriptExe
230705_111244:cmsbot_crab_scriptArgs
230705_111246:cmsbot_crab_sendPythonFolder
230705_111328:cmsbot_crab_sendExternalFolder
230705_111330:cmsbot_crab_inputDBS
230705_111332:cmsbot_crab_useParent
230705_111333:cmsbot_crab_secondaryInputDataset
230705_111335:cmsbot_crab_lumiMaskFile
230705_111336:cmsbot_crab_lumiMaskUrl
230705_111339:cmsbot_crab_outLFNDirBase
230705_111340:cmsbot_crab_runRange
230705_111341:cmsbot_crab_ignoreLocality
230705_111343:cmsbot_crab_userInputFiles
230705_111344:cmsbot_crab_whitelist
230705_111346:cmsbot_crab_blacklist
230705_111347:cmsbot_crab_ignoreGlobalBlacklist
230705_111349:cmsbot_crab_voRole
230705_111350:cmsbot_crab_voGroup
230705_111352:cmsbot_crab_scheddName
230705_111353:cmsbot_crab_collector
230705_111355:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230705_111221:cmsbot_crab_20230705_131206
```

Finished at: 2023-07-05 13:14:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/422/console)

## Comment (cmsdmwmbot, 2023-07-05T11:36:20Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-05 13:36:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/358/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/358//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-05T11:37:25Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-05 13:37:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/676/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230705_111237:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230705_111238:cmsbot_crab_maxJobRuntimeMin - 2
secondaryInputDataset-check.sh 230705_111333:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230705_111336:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230705_111340:cmsbot_crab_runRange - 2
whitelist-check.sh 230705_111344:cmsbot_crab_whitelist - 2
blacklist-check.sh 230705_111346:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230705_111224:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230705_111226:cmsbot_crab_transferLogs - 0
activity-check.sh 230705_111228:cmsbot_crab_activity - 0
inputFiles-check.sh 230705_111230:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230705_111232:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230705_111234:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230705_111236:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 230705_111240:cmsbot_crab_numCores - 0
scriptExe-check.sh 230705_111242:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230705_111244:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230705_111246:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230705_111328:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230705_111330:cmsbot_crab_inputDBS - 0
useParent-check.sh 230705_111332:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230705_111335:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230705_111339:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230705_111341:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230705_111343:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230705_111347:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230705_111349:cmsbot_crab_voRole - 0
voGroup-check.sh 230705_111350:cmsbot_crab_voGroup - 0
scheddName-check.sh 230705_111352:cmsbot_crab_scheddName - 0
collector-check.sh 230705_111353:cmsbot_crab_collector - 0
extraJDL-check.sh 230705_111355:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-05T12:01:36Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-07-05 14:01:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/677/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230705_111224:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230705_111226:cmsbot_crab_transferLogs - 0
activity-check.sh 230705_111228:cmsbot_crab_activity - 0
inputFiles-check.sh 230705_111230:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230705_111232:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230705_111234:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230705_111236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230705_111237:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230705_111238:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230705_111240:cmsbot_crab_numCores - 0
scriptExe-check.sh 230705_111242:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230705_111244:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230705_111246:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230705_111328:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230705_111330:cmsbot_crab_inputDBS - 0
useParent-check.sh 230705_111332:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230705_111333:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230705_111335:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230705_111336:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230705_111339:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230705_111340:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230705_111341:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230705_111343:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230705_111344:cmsbot_crab_whitelist - 0
blacklist-check.sh 230705_111346:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230705_111347:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230705_111349:cmsbot_crab_voRole - 0
voGroup-check.sh 230705_111350:cmsbot_crab_voGroup - 0
scheddName-check.sh 230705_111352:cmsbot_crab_scheddName - 0
collector-check.sh 230705_111353:cmsbot_crab_collector - 0
extraJDL-check.sh 230705_111355:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-05T12:17:30Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-05 14:17:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/467/console

```
{'TN': '230705_111357:cmsbot_crab_20230705_131356', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 991, 'transferring': 4, 'running': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230705_111358:cmsbot_crab_20230705_131358', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230705_111359:cmsbot_crab_20230705_131359', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230705_111401:cmsbot_crab_20230705_131400', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230705_111403:cmsbot_crab_20230705_131402', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230705_111406:cmsbot_crab_20230705_131404', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-07-05T13:21:41Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-05 15:21:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/468/console

```
{'TN': '230705_111357:cmsbot_crab_20230705_131356', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 5, 'finished': 995}, 'combinedStatus': 'FAILED'}
{'TN': '230705_111358:cmsbot_crab_20230705_131358', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230705_111359:cmsbot_crab_20230705_131359', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230705_111401:cmsbot_crab_20230705_131400', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230705_111403:cmsbot_crab_20230705_131402', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230705_111406:cmsbot_crab_20230705_131404', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (novicecpp, 2023-07-06T06:02:06Z)

Test passed!
