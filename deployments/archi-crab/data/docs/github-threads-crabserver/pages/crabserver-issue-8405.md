# dmwm/CRABServer issue #8405: #778: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-15T15:20:57Z
Closed: 2024-05-15T19:36:45Z
URL: https://github.com/dmwm/CRABServer/issues/8405

## Opening post (cmsdmwmbot, 2024-05-15T15:20:57Z)

**AIM: validate my changes to REST with current client**

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-05-15 17:20:56
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/778/)

## Comment (cmsdmwmbot, 2024-05-15T15:23:41Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240515_152229:cmsbot_crab_20240515_172228
240515_152231:cmsbot_crab_20240515_172230
240515_152233:cmsbot_crab_20240515_172232
240515_152235:cmsbot_crab_20240515_172234
240515_152237:cmsbot_crab_20240515_172236
240515_152302:cmsbot_crab_20240515_172239
240515_152305:cmsbot_crab_rucio_transfers_20240515_172303
240515_152307:cmsbot_crab_rucio_transfers_group_20240515_172306
240515_152310:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240515_172308
240515_152313:cmsbot_crab_rucio_transfers_nopublication_20240515_172312
240515_152316:cmsbot_crab_rucio_transfers_withnoneedm_20240515_172315
240515_152319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240515_172318
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240515_152122:cmsbot_crab_transferOutputs
240515_152124:cmsbot_crab_transferLogs
240515_152126:cmsbot_crab_activity
240515_152128:cmsbot_crab_inputFiles
240515_152130:cmsbot_crab_disableAutomaticOutputCollection
240515_152133:cmsbot_crab_outputFiles
240515_152135:cmsbot_crab_allowUndistributedCMSSW
240515_152137:cmsbot_crab_maxMemoryMB
240515_152139:cmsbot_crab_maxJobRuntimeMin
240515_152141:cmsbot_crab_numCores
240515_152143:cmsbot_crab_scriptExe
240515_152146:cmsbot_crab_scriptArgs
240515_152148:cmsbot_crab_sendVenvFolder
240515_152150:cmsbot_crab_sendExternalFolder
240515_152152:cmsbot_crab_inputDBS
240515_152154:cmsbot_crab_useParent
240515_152156:cmsbot_crab_secondaryInputDataset
240515_152158:cmsbot_crab_lumiMaskFile
240515_152200:cmsbot_crab_lumiMaskUrl
240515_152203:cmsbot_crab_outLFNDirBase
240515_152205:cmsbot_crab_runRange
240515_152208:cmsbot_crab_ignoreLocality
240515_152210:cmsbot_crab_userInputFiles
240515_152212:cmsbot_crab_whitelist
240515_152214:cmsbot_crab_blacklist
240515_152216:cmsbot_crab_ignoreGlobalBlacklist
240515_152218:cmsbot_crab_voRole
240515_152220:cmsbot_crab_voGroup
240515_152222:cmsbot_crab_scheddName
240515_152224:cmsbot_crab_collector
240515_152226:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240515_152120:cmsbot_crab_20240515_172118
```

Finished at: 2024-05-15 17:23:20
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/778/console)

## Comment (cmsdmwmbot, 2024-05-15T15:44:38Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-15 17:44:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/918/console

```
{'TN': '240515_152229:cmsbot_crab_20240515_172228', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 987, 'idle': 1, 'running': 12}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152231:cmsbot_crab_20240515_172230', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152233:cmsbot_crab_20240515_172232', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152235:cmsbot_crab_20240515_172234', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152237:cmsbot_crab_20240515_172236', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152302:cmsbot_crab_20240515_172239', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152305:cmsbot_crab_rucio_transfers_20240515_172303', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152307:cmsbot_crab_rucio_transfers_group_20240515_172306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152310:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240515_172308', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152313:cmsbot_crab_rucio_transfers_nopublication_20240515_172312', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'held': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152316:cmsbot_crab_rucio_transfers_withnoneedm_20240515_172315', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240515_172318', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-15T15:48:21Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-15 17:48:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1059/console

```
RETRY TESTS:
transferLogs-check.sh 240515_152124:cmsbot_crab_transferLogs - 2
outputFiles-check.sh 240515_152133:cmsbot_crab_outputFiles - 2
numCores-check.sh 240515_152141:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240515_152200:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240515_152205:cmsbot_crab_runRange - 2
whitelist-check.sh 240515_152212:cmsbot_crab_whitelist - 2
blacklist-check.sh 240515_152214:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240515_152216:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240515_152218:cmsbot_crab_voRole - 2
voGroup-check.sh 240515_152220:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240515_152122:cmsbot_crab_transferOutputs - 0
activity-check.sh 240515_152126:cmsbot_crab_activity - 0
inputFiles-check.sh 240515_152128:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240515_152130:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240515_152135:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240515_152137:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240515_152139:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240515_152143:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240515_152146:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240515_152148:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240515_152150:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240515_152152:cmsbot_crab_inputDBS - 0
useParent-check.sh 240515_152154:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240515_152156:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240515_152158:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240515_152203:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240515_152208:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240515_152210:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 240515_152222:cmsbot_crab_scheddName - 0
collector-check.sh 240515_152224:cmsbot_crab_collector - 0
extraJDL-check.sh 240515_152226:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-15T15:48:27Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-05-15 17:48:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/538/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/538//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-05-15T16:00:35Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-05-15 18:00:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/919/console

```
{'TN': '240515_152229:cmsbot_crab_20240515_172228', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152231:cmsbot_crab_20240515_172230', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152233:cmsbot_crab_20240515_172232', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152235:cmsbot_crab_20240515_172234', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152237:cmsbot_crab_20240515_172236', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152302:cmsbot_crab_20240515_172239', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152305:cmsbot_crab_rucio_transfers_20240515_172303', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152307:cmsbot_crab_rucio_transfers_group_20240515_172306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152310:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240515_172308', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152313:cmsbot_crab_rucio_transfers_nopublication_20240515_172312', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152316:cmsbot_crab_rucio_transfers_withnoneedm_20240515_172315', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240515_172318', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-15T16:13:19Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-05-15 18:13:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1061/console

```
RETRY TESTS:
blacklist-check.sh 240515_152214:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240515_152122:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240515_152124:cmsbot_crab_transferLogs - 0
activity-check.sh 240515_152126:cmsbot_crab_activity - 0
inputFiles-check.sh 240515_152128:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240515_152130:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240515_152135:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240515_152137:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240515_152139:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240515_152141:cmsbot_crab_numCores - 0
scriptExe-check.sh 240515_152143:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240515_152146:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240515_152148:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240515_152150:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240515_152152:cmsbot_crab_inputDBS - 0
useParent-check.sh 240515_152154:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240515_152156:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240515_152158:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240515_152200:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240515_152203:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240515_152205:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240515_152208:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240515_152210:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240515_152212:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240515_152216:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240515_152218:cmsbot_crab_voRole - 0
voGroup-check.sh 240515_152220:cmsbot_crab_voGroup - 0
scheddName-check.sh 240515_152222:cmsbot_crab_scheddName - 0
collector-check.sh 240515_152224:cmsbot_crab_collector - 0
extraJDL-check.sh 240515_152226:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240515_152133:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-05-15T16:38:26Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-05-15 18:38:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1063/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240515_152122:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240515_152124:cmsbot_crab_transferLogs - 0
activity-check.sh 240515_152126:cmsbot_crab_activity - 0
inputFiles-check.sh 240515_152128:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240515_152130:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240515_152135:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240515_152137:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240515_152139:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240515_152141:cmsbot_crab_numCores - 0
scriptExe-check.sh 240515_152143:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240515_152146:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240515_152148:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240515_152150:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240515_152152:cmsbot_crab_inputDBS - 0
useParent-check.sh 240515_152154:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240515_152156:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240515_152158:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240515_152200:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240515_152203:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240515_152205:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240515_152208:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240515_152210:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240515_152212:cmsbot_crab_whitelist - 0
blacklist-check.sh 240515_152214:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240515_152216:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240515_152218:cmsbot_crab_voRole - 0
voGroup-check.sh 240515_152220:cmsbot_crab_voGroup - 0
scheddName-check.sh 240515_152222:cmsbot_crab_scheddName - 0
collector-check.sh 240515_152224:cmsbot_crab_collector - 0
extraJDL-check.sh 240515_152226:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240515_152133:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-05-15T16:46:31Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-05-15 18:46:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/920/console

```
{'TN': '240515_152229:cmsbot_crab_20240515_172228', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 998, 'failed': 2}, 'publication (fail/tdb/DBS)': '0/831/831'}
{'TN': '240515_152231:cmsbot_crab_20240515_172230', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152233:cmsbot_crab_20240515_172232', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152235:cmsbot_crab_20240515_172234', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/6/6'}
{'TN': '240515_152237:cmsbot_crab_20240515_172236', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/85/85'}
{'TN': '240515_152302:cmsbot_crab_20240515_172239', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240515_152305:cmsbot_crab_rucio_transfers_20240515_172303', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 34, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/34/34'}
{'TN': '240515_152307:cmsbot_crab_rucio_transfers_group_20240515_172306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 22, 'transferring': 18}, 'publication (fail/tdb/DBS)': '0/22/22'}
{'TN': '240515_152310:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240515_172308', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152313:cmsbot_crab_rucio_transfers_nopublication_20240515_172312', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152316:cmsbot_crab_rucio_transfers_withnoneedm_20240515_172315', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240515_152319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240515_172318', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-15T18:20:11Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-05-15 20:20:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/921/console

```
{'TN': '240515_152229:cmsbot_crab_20240515_172228', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240515_152231:cmsbot_crab_20240515_172230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240515_152233:cmsbot_crab_20240515_172232', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240515_152235:cmsbot_crab_20240515_172234', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240515_152237:cmsbot_crab_20240515_172236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240515_152302:cmsbot_crab_20240515_172239', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240515_152305:cmsbot_crab_rucio_transfers_20240515_172303', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 34, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/34/34'}
{'TN': '240515_152307:cmsbot_crab_rucio_transfers_group_20240515_172306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 22, 'transferring': 18}, 'publication (fail/tdb/DBS)': '0/22/22'}
{'TN': '240515_152310:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240515_172308', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152313:cmsbot_crab_rucio_transfers_nopublication_20240515_172312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152316:cmsbot_crab_rucio_transfers_withnoneedm_20240515_172315', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240515_152319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240515_172318', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-05-15T19:04:10Z)

CCV failure on `outputFiles` is expected

## Comment (belforte, 2024-05-15T19:36:20Z)

There are some odd failures in Rucio transers (e.g. files disappeared from /store/temp at GRIF. But submission is cllearly working.

## Comment (cmsdmwmbot, 2024-05-15T20:21:21Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-05-15 22:21:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/922/console

```
{'TN': '240515_152229:cmsbot_crab_20240515_172228', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240515_152231:cmsbot_crab_20240515_172230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240515_152233:cmsbot_crab_20240515_172232', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240515_152235:cmsbot_crab_20240515_172234', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240515_152237:cmsbot_crab_20240515_172236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240515_152302:cmsbot_crab_20240515_172239', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240515_152305:cmsbot_crab_rucio_transfers_20240515_172303', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 34, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/34/34'}
{'TN': '240515_152307:cmsbot_crab_rucio_transfers_group_20240515_172306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 22, 'transferring': 18}, 'publication (fail/tdb/DBS)': '0/22/22'}
{'TN': '240515_152310:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240515_172308', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152313:cmsbot_crab_rucio_transfers_nopublication_20240515_172312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152316:cmsbot_crab_rucio_transfers_withnoneedm_20240515_172315', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240515_152319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240515_172318', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-15T22:22:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-05-16 00:22:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/923/console

```
{'TN': '240515_152229:cmsbot_crab_20240515_172228', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240515_152231:cmsbot_crab_20240515_172230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240515_152233:cmsbot_crab_20240515_172232', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240515_152235:cmsbot_crab_20240515_172234', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240515_152237:cmsbot_crab_20240515_172236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240515_152302:cmsbot_crab_20240515_172239', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240515_152305:cmsbot_crab_rucio_transfers_20240515_172303', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 34, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/34/34'}
{'TN': '240515_152307:cmsbot_crab_rucio_transfers_group_20240515_172306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 22, 'transferring': 18}, 'publication (fail/tdb/DBS)': '0/22/22'}
{'TN': '240515_152310:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240515_172308', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152313:cmsbot_crab_rucio_transfers_nopublication_20240515_172312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240515_152316:cmsbot_crab_rucio_transfers_withnoneedm_20240515_172315', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240515_152319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240515_172318', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
