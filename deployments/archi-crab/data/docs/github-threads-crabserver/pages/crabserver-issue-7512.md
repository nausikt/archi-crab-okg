# dmwm/CRABServer issue #7512: #370: Test dev CRABClient using test2 REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-01-27T14:39:24Z
Closed: 2023-01-30T10:38:22Z
URL: https://github.com/dmwm/CRABServer/issues/7512

## Opening post (cmsdmwmbot, 2023-01-27T14:39:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-01-27 15:39:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/370/)

## Comment (cmsdmwmbot, 2023-01-27T14:44:37Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230127_144331:cmsbot_crab_20230127_154329
230127_144334:cmsbot_crab_20230127_154332
230127_144337:cmsbot_crab_20230127_154335
230127_144340:cmsbot_crab_20230127_154338
230127_144344:cmsbot_crab_20230127_154341
230127_144415:cmsbot_crab_20230127_154344
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230127_144146:cmsbot_crab_transferOutputs
230127_144150:cmsbot_crab_transferLogs
230127_144153:cmsbot_crab_activity
230127_144156:cmsbot_crab_inputFiles
230127_144159:cmsbot_crab_disableAutomaticOutputCollection
230127_144202:cmsbot_crab_outputFiles
230127_144205:cmsbot_crab_allowUndistributedCMSSW
230127_144208:cmsbot_crab_maxMemoryMB
230127_144211:cmsbot_crab_maxJobRuntimeMin
230127_144215:cmsbot_crab_numCores
230127_144218:cmsbot_crab_scriptExe
230127_144221:cmsbot_crab_scriptArgs
230127_144224:cmsbot_crab_sendPythonFolder
230127_144235:cmsbot_crab_sendExternalFolder
230127_144238:cmsbot_crab_inputDBS
230127_144241:cmsbot_crab_useParent
230127_144244:cmsbot_crab_secondaryInputDataset
230127_144247:cmsbot_crab_lumiMaskFile
230127_144250:cmsbot_crab_lumiMaskUrl
230127_144254:cmsbot_crab_outLFNDirBase
230127_144257:cmsbot_crab_runRange
230127_144300:cmsbot_crab_ignoreLocality
230127_144303:cmsbot_crab_userInputFiles
230127_144306:cmsbot_crab_whitelist
230127_144309:cmsbot_crab_blacklist
230127_144313:cmsbot_crab_ignoreGlobalBlacklist
230127_144316:cmsbot_crab_voRole
230127_144319:cmsbot_crab_voGroup
230127_144322:cmsbot_crab_scheddName
230127_144325:cmsbot_crab_collector
230127_144328:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230127_144143:cmsbot_crab_20230127_154136
```

Finished at: 2023-01-27 15:44:16
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/370/console)

## Comment (cmsdmwmbot, 2023-01-27T15:07:50Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-01-27 16:07:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/332/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/332//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-01-27T15:11:04Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-01-27 16:11:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/571/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 230127_144244:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230127_144250:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230127_144257:cmsbot_crab_runRange - 2
whitelist-check.sh 230127_144306:cmsbot_crab_whitelist - 2
blacklist-check.sh 230127_144309:cmsbot_crab_blacklist - 2
voRole-check.sh 230127_144316:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230127_144146:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230127_144150:cmsbot_crab_transferLogs - 0
activity-check.sh 230127_144153:cmsbot_crab_activity - 0
inputFiles-check.sh 230127_144156:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230127_144159:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230127_144202:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230127_144205:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230127_144208:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230127_144211:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230127_144215:cmsbot_crab_numCores - 0
scriptExe-check.sh 230127_144218:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230127_144221:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230127_144224:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230127_144235:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230127_144238:cmsbot_crab_inputDBS - 0
useParent-check.sh 230127_144241:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230127_144247:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230127_144254:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230127_144300:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230127_144303:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230127_144313:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230127_144319:cmsbot_crab_voGroup - 0
scheddName-check.sh 230127_144322:cmsbot_crab_scheddName - 0
collector-check.sh 230127_144325:cmsbot_crab_collector - 0
extraJDL-check.sh 230127_144328:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-01-27T15:36:56Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-01-27 16:36:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/572/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230127_144146:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230127_144150:cmsbot_crab_transferLogs - 0
activity-check.sh 230127_144153:cmsbot_crab_activity - 0
inputFiles-check.sh 230127_144156:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230127_144159:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230127_144202:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230127_144205:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230127_144208:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230127_144211:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230127_144215:cmsbot_crab_numCores - 0
scriptExe-check.sh 230127_144218:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230127_144221:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230127_144224:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230127_144235:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230127_144238:cmsbot_crab_inputDBS - 0
useParent-check.sh 230127_144241:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230127_144244:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230127_144247:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230127_144250:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230127_144254:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230127_144257:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230127_144300:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230127_144303:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230127_144306:cmsbot_crab_whitelist - 0
blacklist-check.sh 230127_144309:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230127_144313:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230127_144316:cmsbot_crab_voRole - 0
voGroup-check.sh 230127_144319:cmsbot_crab_voGroup - 0
scheddName-check.sh 230127_144322:cmsbot_crab_scheddName - 0
collector-check.sh 230127_144325:cmsbot_crab_collector - 0
extraJDL-check.sh 230127_144328:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-01-27T15:46:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-01-27 16:46:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/421/console

```
{'TN': '230127_144331:cmsbot_crab_20230127_154329', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_144334:cmsbot_crab_20230127_154332', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230127_144337:cmsbot_crab_20230127_154335', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_144340:cmsbot_crab_20230127_154338', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_144344:cmsbot_crab_20230127_154341', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_144415:cmsbot_crab_20230127_154344', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-01-27T16:49:27Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-01-27 17:49:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/422/console

```
{'TN': '230127_144331:cmsbot_crab_20230127_154329', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_144334:cmsbot_crab_20230127_154332', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 7}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_144337:cmsbot_crab_20230127_154335', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_144340:cmsbot_crab_20230127_154338', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_144344:cmsbot_crab_20230127_154341', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230127_144415:cmsbot_crab_20230127_154344', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-01-30T10:38:22Z)

all OK
