# dmwm/CRABServer issue #7745: #432: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-12T14:21:42Z
Closed: 2023-07-12T21:01:01Z
URL: https://github.com/dmwm/CRABServer/issues/7745

## Opening post (cmsdmwmbot, 2023-07-12T14:21:42Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-07-12 16:21:41
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/432/)

## Comment (cmsdmwmbot, 2023-07-12T14:25:02Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230712_142411:cmsbot_crab_20230712_162411
230712_142413:cmsbot_crab_20230712_162412
230712_142414:cmsbot_crab_20230712_162414
230712_142416:cmsbot_crab_20230712_162415
230712_142417:cmsbot_crab_20230712_162416
230712_142440:cmsbot_crab_20230712_162418
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230712_142225:cmsbot_crab_transferOutputs
230712_142228:cmsbot_crab_transferLogs
230712_142231:cmsbot_crab_activity
230712_142234:cmsbot_crab_inputFiles
230712_142236:cmsbot_crab_disableAutomaticOutputCollection
230712_142238:cmsbot_crab_outputFiles
230712_142241:cmsbot_crab_allowUndistributedCMSSW
230712_142243:cmsbot_crab_maxMemoryMB
230712_142246:cmsbot_crab_maxJobRuntimeMin
230712_142247:cmsbot_crab_numCores
230712_142248:cmsbot_crab_scriptExe
230712_142250:cmsbot_crab_scriptArgs
230712_142251:cmsbot_crab_sendPythonFolder
230712_142341:cmsbot_crab_sendExternalFolder
230712_142342:cmsbot_crab_inputDBS
230712_142344:cmsbot_crab_useParent
230712_142345:cmsbot_crab_secondaryInputDataset
230712_142348:cmsbot_crab_lumiMaskFile
230712_142350:cmsbot_crab_lumiMaskUrl
230712_142352:cmsbot_crab_outLFNDirBase
230712_142354:cmsbot_crab_runRange
230712_142356:cmsbot_crab_ignoreLocality
230712_142357:cmsbot_crab_userInputFiles
230712_142359:cmsbot_crab_whitelist
230712_142400:cmsbot_crab_blacklist
230712_142401:cmsbot_crab_ignoreGlobalBlacklist
230712_142403:cmsbot_crab_voRole
230712_142404:cmsbot_crab_voGroup
230712_142406:cmsbot_crab_scheddName
230712_142407:cmsbot_crab_collector
230712_142409:cmsbot_crab_extraJDL
```

Finished at: 2023-07-12 16:24:41
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/432/console)

## Comment (cmsdmwmbot, 2023-07-12T14:46:58Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-12 16:46:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/713/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230712_142243:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230712_142246:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 230712_142248:cmsbot_crab_scriptExe - 2
outLFNDirBase-check.sh 230712_142352:cmsbot_crab_outLFNDirBase - 2
ignoreLocality-check.sh 230712_142356:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 230712_142357:cmsbot_crab_userInputFiles - 2
voGroup-check.sh 230712_142404:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_142225:cmsbot_crab_transferOutputs - 0
activity-check.sh 230712_142231:cmsbot_crab_activity - 0
disableAutomaticOutputCollection-check.sh 230712_142236:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230712_142241:cmsbot_crab_allowUndistributedCMSSW - 0
sendExternalFolder-check.sh 230712_142341:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_142342:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_142344:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230712_142348:cmsbot_crab_lumiMaskFile - 0
ignoreGlobalBlacklist-check.sh 230712_142401:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 230712_142406:cmsbot_crab_scheddName - 0
collector-check.sh 230712_142407:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_142409:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferLogs-check.sh 230712_142228:cmsbot_crab_transferLogs - 1
inputFiles-check.sh 230712_142234:cmsbot_crab_inputFiles - 1
outputFiles-check.sh 230712_142238:cmsbot_crab_outputFiles - 1
numCores-check.sh 230712_142247:cmsbot_crab_numCores - 1
scriptArgs-check.sh 230712_142250:cmsbot_crab_scriptArgs - 1
sendPythonFolder-check.sh 230712_142251:cmsbot_crab_sendPythonFolder - 1
secondaryInputDataset-check.sh 230712_142345:cmsbot_crab_secondaryInputDataset - 1
lumiMaskUrl-check.sh 230712_142350:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 230712_142354:cmsbot_crab_runRange - 1
whitelist-check.sh 230712_142359:cmsbot_crab_whitelist - 1
blacklist-check.sh 230712_142400:cmsbot_crab_blacklist - 1
voRole-check.sh 230712_142403:cmsbot_crab_voRole - 1
```

## Comment (cmsdmwmbot, 2023-07-12T15:08:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-12 17:08:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/717/console

```
RETRY TESTS:
transferLogs-check.sh 230712_142228:cmsbot_crab_transferLogs - 2
outputFiles-check.sh 230712_142238:cmsbot_crab_outputFiles - 2
numCores-check.sh 230712_142247:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230712_142350:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230712_142354:cmsbot_crab_runRange - 2
whitelist-check.sh 230712_142359:cmsbot_crab_whitelist - 2
blacklist-check.sh 230712_142400:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_142225:cmsbot_crab_transferOutputs - 0
activity-check.sh 230712_142231:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_142234:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_142236:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230712_142241:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_142243:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_142246:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230712_142248:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_142250:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_142251:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_142341:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_142342:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_142344:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_142345:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_142348:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230712_142352:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230712_142356:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_142357:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230712_142401:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_142403:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_142404:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_142406:cmsbot_crab_scheddName - 0
collector-check.sh 230712_142407:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_142409:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-12T15:27:12Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-12 17:27:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/492/console

```
{'TN': '230712_142411:cmsbot_crab_20230712_162411', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 997, 'running': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230712_142413:cmsbot_crab_20230712_162412', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230712_142414:cmsbot_crab_20230712_162414', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230712_142416:cmsbot_crab_20230712_162415', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230712_142417:cmsbot_crab_20230712_162416', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 92, 'transferring': 7, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230712_142440:cmsbot_crab_20230712_162418', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-12T15:31:03Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-07-12 17:31:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/721/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230712_142225:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230712_142228:cmsbot_crab_transferLogs - 0
activity-check.sh 230712_142231:cmsbot_crab_activity - 0
inputFiles-check.sh 230712_142234:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230712_142236:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230712_142238:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230712_142241:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230712_142243:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230712_142246:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230712_142247:cmsbot_crab_numCores - 0
scriptExe-check.sh 230712_142248:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230712_142250:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230712_142251:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230712_142341:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230712_142342:cmsbot_crab_inputDBS - 0
useParent-check.sh 230712_142344:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230712_142345:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230712_142348:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230712_142350:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230712_142352:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230712_142354:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230712_142356:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230712_142357:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230712_142359:cmsbot_crab_whitelist - 0
blacklist-check.sh 230712_142400:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230712_142401:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230712_142403:cmsbot_crab_voRole - 0
voGroup-check.sh 230712_142404:cmsbot_crab_voGroup - 0
scheddName-check.sh 230712_142406:cmsbot_crab_scheddName - 0
collector-check.sh 230712_142407:cmsbot_crab_collector - 0
extraJDL-check.sh 230712_142409:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-12T16:28:46Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Something went wrong. Investigate manually.
**Finished at:** 2023-07-12 18:28:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/493/console

```

```

## Comment (belforte, 2023-07-12T21:01:01Z)

status tracking failed due to crab remake failing because of gitlab downtime.
But changes in v3.230712 may only touch job submissions.

So call it OK !
