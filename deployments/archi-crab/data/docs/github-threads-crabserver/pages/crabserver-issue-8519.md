# dmwm/CRABServer issue #8519: #813: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-19T15:20:41Z
Closed: 2024-06-19T18:30:56Z
URL: https://github.com/dmwm/CRABServer/issues/8519

## Opening post (cmsdmwmbot, 2024-06-19T15:20:41Z)

**Meant to validate fix for #8518**

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-06-19 17:20:41
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/813/)

## Comment (cmsdmwmbot, 2024-06-19T15:23:03Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240619_152214:cmsbot_crab_20240619_172214
240619_152216:cmsbot_crab_20240619_172216
240619_152218:cmsbot_crab_20240619_172218
240619_152220:cmsbot_crab_20240619_172220
240619_152222:cmsbot_crab_20240619_172222
240619_152226:cmsbot_crab_20240619_172224
240619_152229:cmsbot_crab_rucio_transfers_20240619_172227
240619_152231:cmsbot_crab_rucio_transfers_group_20240619_172230
240619_152233:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_172232
240619_152236:cmsbot_crab_rucio_transfers_nopublication_20240619_172235
240619_152239:cmsbot_crab_rucio_transfers_withnoneedm_20240619_172238
240619_152242:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_172240
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240619_152104:cmsbot_crab_transferOutputs
240619_152110:cmsbot_crab_transferLogs
240619_152112:cmsbot_crab_activity
240619_152115:cmsbot_crab_inputFiles
240619_152117:cmsbot_crab_disableAutomaticOutputCollection
240619_152119:cmsbot_crab_outputFiles
240619_152121:cmsbot_crab_allowUndistributedCMSSW
240619_152123:cmsbot_crab_maxMemoryMB
240619_152125:cmsbot_crab_maxJobRuntimeMin
240619_152127:cmsbot_crab_numCores
240619_152129:cmsbot_crab_scriptExe
240619_152131:cmsbot_crab_scriptArgs
240619_152133:cmsbot_crab_sendVenvFolder
240619_152135:cmsbot_crab_sendExternalFolder
240619_152138:cmsbot_crab_inputDBS
240619_152140:cmsbot_crab_useParent
240619_152142:cmsbot_crab_secondaryInputDataset
240619_152144:cmsbot_crab_lumiMaskFile
240619_152146:cmsbot_crab_lumiMaskUrl
240619_152149:cmsbot_crab_outLFNDirBase
240619_152151:cmsbot_crab_runRange
240619_152153:cmsbot_crab_ignoreLocality
240619_152155:cmsbot_crab_userInputFiles
240619_152157:cmsbot_crab_whitelist
240619_152159:cmsbot_crab_blacklist
240619_152201:cmsbot_crab_ignoreGlobalBlacklist
240619_152203:cmsbot_crab_voRole
240619_152205:cmsbot_crab_voGroup
240619_152207:cmsbot_crab_scheddName
240619_152209:cmsbot_crab_collector
240619_152211:cmsbot_crab_extraJDL
```

Finished at: 2024-06-19 17:22:42
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/813/console)

## Comment (cmsdmwmbot, 2024-06-19T15:43:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-19 17:43:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1016/console

```
{'TN': '240619_152214:cmsbot_crab_20240619_172214', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 994, 'running': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152216:cmsbot_crab_20240619_172216', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 3, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152218:cmsbot_crab_20240619_172218', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152220:cmsbot_crab_20240619_172220', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152222:cmsbot_crab_20240619_172222', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152226:cmsbot_crab_20240619_172224', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 7, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152229:cmsbot_crab_rucio_transfers_20240619_172227', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152231:cmsbot_crab_rucio_transfers_group_20240619_172230', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 3, 'transferring': 37}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152233:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_172232', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 37, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152236:cmsbot_crab_rucio_transfers_nopublication_20240619_172235', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152239:cmsbot_crab_rucio_transfers_withnoneedm_20240619_172238', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 36, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152242:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_172240', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-19T15:47:27Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-19 17:47:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1137/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240619_152146:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240619_152151:cmsbot_crab_runRange - 2
whitelist-check.sh 240619_152157:cmsbot_crab_whitelist - 2
blacklist-check.sh 240619_152159:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240619_152104:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240619_152110:cmsbot_crab_transferLogs - 0
activity-check.sh 240619_152112:cmsbot_crab_activity - 0
inputFiles-check.sh 240619_152115:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240619_152117:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240619_152119:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240619_152121:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240619_152123:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240619_152125:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240619_152127:cmsbot_crab_numCores - 0
scriptExe-check.sh 240619_152129:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240619_152131:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240619_152133:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240619_152135:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240619_152138:cmsbot_crab_inputDBS - 0
useParent-check.sh 240619_152140:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240619_152142:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240619_152144:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240619_152149:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240619_152153:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240619_152155:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240619_152201:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240619_152203:cmsbot_crab_voRole - 0
voGroup-check.sh 240619_152205:cmsbot_crab_voGroup - 0
scheddName-check.sh 240619_152207:cmsbot_crab_scheddName - 0
collector-check.sh 240619_152209:cmsbot_crab_collector - 0
extraJDL-check.sh 240619_152211:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-19T15:59:55Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-19 17:59:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1017/console

```
{'TN': '240619_152214:cmsbot_crab_20240619_172214', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152216:cmsbot_crab_20240619_172216', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152218:cmsbot_crab_20240619_172218', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152220:cmsbot_crab_20240619_172220', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152222:cmsbot_crab_20240619_172222', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152226:cmsbot_crab_20240619_172224', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152229:cmsbot_crab_rucio_transfers_20240619_172227', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152231:cmsbot_crab_rucio_transfers_group_20240619_172230', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152233:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_172232', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152236:cmsbot_crab_rucio_transfers_nopublication_20240619_172235', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152239:cmsbot_crab_rucio_transfers_withnoneedm_20240619_172238', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152242:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_172240', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-19T16:11:12Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-19 18:11:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1138/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240619_152104:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240619_152110:cmsbot_crab_transferLogs - 0
activity-check.sh 240619_152112:cmsbot_crab_activity - 0
inputFiles-check.sh 240619_152115:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240619_152117:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240619_152119:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240619_152121:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240619_152123:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240619_152125:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240619_152127:cmsbot_crab_numCores - 0
scriptExe-check.sh 240619_152129:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240619_152131:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240619_152133:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240619_152135:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240619_152138:cmsbot_crab_inputDBS - 0
useParent-check.sh 240619_152140:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240619_152142:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240619_152144:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240619_152146:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240619_152149:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240619_152151:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240619_152153:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240619_152155:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240619_152157:cmsbot_crab_whitelist - 0
blacklist-check.sh 240619_152159:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240619_152201:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240619_152203:cmsbot_crab_voRole - 0
voGroup-check.sh 240619_152205:cmsbot_crab_voGroup - 0
scheddName-check.sh 240619_152207:cmsbot_crab_scheddName - 0
collector-check.sh 240619_152209:cmsbot_crab_collector - 0
extraJDL-check.sh 240619_152211:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-19T16:48:16Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-19 18:48:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1018/console

```
{'TN': '240619_152214:cmsbot_crab_20240619_172214', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240619_152216:cmsbot_crab_20240619_172216', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152218:cmsbot_crab_20240619_172218', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240619_152220:cmsbot_crab_20240619_172220', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240619_152222:cmsbot_crab_20240619_172222', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240619_152226:cmsbot_crab_20240619_172224', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240619_152229:cmsbot_crab_rucio_transfers_20240619_172227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240619_152231:cmsbot_crab_rucio_transfers_group_20240619_172230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240619_152233:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_172232', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152236:cmsbot_crab_rucio_transfers_nopublication_20240619_172235', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152239:cmsbot_crab_rucio_transfers_withnoneedm_20240619_172238', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240619_152242:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_172240', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-19T18:20:21Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-06-19 20:20:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1019/console

```
{'TN': '240619_152214:cmsbot_crab_20240619_172214', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240619_152216:cmsbot_crab_20240619_172216', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240619_152218:cmsbot_crab_20240619_172218', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240619_152220:cmsbot_crab_20240619_172220', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240619_152222:cmsbot_crab_20240619_172222', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240619_152226:cmsbot_crab_20240619_172224', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240619_152229:cmsbot_crab_rucio_transfers_20240619_172227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240619_152231:cmsbot_crab_rucio_transfers_group_20240619_172230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240619_152233:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240619_172232', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152236:cmsbot_crab_rucio_transfers_nopublication_20240619_172235', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240619_152239:cmsbot_crab_rucio_transfers_withnoneedm_20240619_172238', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240619_152242:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240619_172240', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-19T18:30:56Z)

OK
