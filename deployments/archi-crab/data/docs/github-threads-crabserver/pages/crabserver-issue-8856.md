# dmwm/CRABServer issue #8856: #917: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-12-03T10:49:24Z
Closed: 2024-12-06T13:51:36Z
URL: https://github.com/dmwm/CRABServer/issues/8856

## Opening post (cmsdmwmbot, 2024-12-03T10:49:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-12-03 11:49:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/917/)

## Comment (cmsdmwmbot, 2024-12-03T10:54:06Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
241203_105221:cmsbot_crab_20241203_115219
241203_105225:cmsbot_crab_20241203_115223
241203_105228:cmsbot_crab_20241203_115227
241203_105232:cmsbot_crab_20241203_115230
241203_105235:cmsbot_crab_20241203_115234
241203_105319:cmsbot_crab_20241203_115237
241203_105324:cmsbot_crab_rucio_transfers_20241203_115321
241203_105327:cmsbot_crab_rucio_transfers_group_20241203_115326
241203_105331:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241203_115329
241203_105335:cmsbot_crab_rucio_transfers_nopublication_20241203_115333
241203_105340:cmsbot_crab_rucio_transfers_withnoneedm_20241203_115337
241203_105344:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241203_115342
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
241203_105022:cmsbot_crab_transferOutputs
241203_105026:cmsbot_crab_transferLogs
241203_105029:cmsbot_crab_activity
241203_105033:cmsbot_crab_inputFiles
241203_105037:cmsbot_crab_disableAutomaticOutputCollection
241203_105040:cmsbot_crab_outputFiles
241203_105044:cmsbot_crab_allowUndistributedCMSSW
241203_105048:cmsbot_crab_maxMemoryMB
241203_105052:cmsbot_crab_maxJobRuntimeMin
241203_105056:cmsbot_crab_numCores
241203_105100:cmsbot_crab_scriptExe
241203_105103:cmsbot_crab_scriptArgs
241203_105107:cmsbot_crab_sendVenvFolder
241203_105111:cmsbot_crab_sendExternalFolder
241203_105115:cmsbot_crab_inputDBS
241203_105118:cmsbot_crab_useParent
241203_105122:cmsbot_crab_secondaryInputDataset
241203_105126:cmsbot_crab_lumiMaskFile
241203_105130:cmsbot_crab_lumiMaskUrl
241203_105134:cmsbot_crab_outLFNDirBase
241203_105138:cmsbot_crab_runRange
241203_105142:cmsbot_crab_ignoreLocality
241203_105146:cmsbot_crab_userInputFiles
241203_105149:cmsbot_crab_whitelist
241203_105153:cmsbot_crab_blacklist
241203_105157:cmsbot_crab_ignoreGlobalBlacklist
241203_105201:cmsbot_crab_voRole
241203_105205:cmsbot_crab_voGroup
241203_105209:cmsbot_crab_scheddName
241203_105212:cmsbot_crab_collector
241203_105216:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241203_105018:cmsbot_crab_20241203_115016
```

Finished at: 2024-12-03 11:53:44
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/917/console)

## Comment (cmsdmwmbot, 2024-12-03T11:16:08Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-12-03 12:16:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1128/console

```
{'TN': '241203_105221:cmsbot_crab_20241203_115219', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105225:cmsbot_crab_20241203_115223', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105228:cmsbot_crab_20241203_115227', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105232:cmsbot_crab_20241203_115230', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105235:cmsbot_crab_20241203_115234', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105319:cmsbot_crab_20241203_115237', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105324:cmsbot_crab_rucio_transfers_20241203_115321', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105327:cmsbot_crab_rucio_transfers_group_20241203_115326', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105331:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241203_115329', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105335:cmsbot_crab_rucio_transfers_nopublication_20241203_115333', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105340:cmsbot_crab_rucio_transfers_withnoneedm_20241203_115337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105344:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241203_115342', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-12-03T11:19:27Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-12-03 12:19:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/591/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/591//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-12-03T11:20:16Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-12-03 12:20:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1260/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 241203_105052:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241203_105056:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 241203_105130:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 241203_105138:cmsbot_crab_runRange - 2
whitelist-check.sh 241203_105149:cmsbot_crab_whitelist - 2
blacklist-check.sh 241203_105153:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241203_105022:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241203_105026:cmsbot_crab_transferLogs - 0
activity-check.sh 241203_105029:cmsbot_crab_activity - 0
inputFiles-check.sh 241203_105033:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241203_105037:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241203_105040:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241203_105044:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241203_105048:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 241203_105100:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241203_105103:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241203_105107:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241203_105111:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241203_105115:cmsbot_crab_inputDBS - 0
useParent-check.sh 241203_105118:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241203_105122:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241203_105126:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 241203_105134:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 241203_105142:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241203_105146:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 241203_105157:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241203_105201:cmsbot_crab_voRole - 0
voGroup-check.sh 241203_105205:cmsbot_crab_voGroup - 0
scheddName-check.sh 241203_105209:cmsbot_crab_scheddName - 0
collector-check.sh 241203_105212:cmsbot_crab_collector - 0
extraJDL-check.sh 241203_105216:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-12-03T11:33:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-12-03 12:33:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1129/console

```
{'TN': '241203_105221:cmsbot_crab_20241203_115219', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105225:cmsbot_crab_20241203_115223', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105228:cmsbot_crab_20241203_115227', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105232:cmsbot_crab_20241203_115230', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105235:cmsbot_crab_20241203_115234', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105319:cmsbot_crab_20241203_115237', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 3, 'transferring': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105324:cmsbot_crab_rucio_transfers_20241203_115321', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105327:cmsbot_crab_rucio_transfers_group_20241203_115326', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105331:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241203_115329', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105335:cmsbot_crab_rucio_transfers_nopublication_20241203_115333', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105340:cmsbot_crab_rucio_transfers_withnoneedm_20241203_115337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 2, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105344:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241203_115342', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-12-03T11:45:23Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-12-03 12:45:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1261/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241203_105022:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241203_105026:cmsbot_crab_transferLogs - 0
activity-check.sh 241203_105029:cmsbot_crab_activity - 0
inputFiles-check.sh 241203_105033:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241203_105037:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241203_105040:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241203_105044:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241203_105048:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241203_105052:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241203_105056:cmsbot_crab_numCores - 0
scriptExe-check.sh 241203_105100:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241203_105103:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241203_105107:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241203_105111:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241203_105115:cmsbot_crab_inputDBS - 0
useParent-check.sh 241203_105118:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241203_105122:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241203_105126:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241203_105130:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241203_105134:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241203_105138:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241203_105142:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241203_105146:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241203_105149:cmsbot_crab_whitelist - 0
blacklist-check.sh 241203_105153:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241203_105157:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241203_105201:cmsbot_crab_voRole - 0
voGroup-check.sh 241203_105205:cmsbot_crab_voGroup - 0
scheddName-check.sh 241203_105209:cmsbot_crab_scheddName - 0
collector-check.sh 241203_105212:cmsbot_crab_collector - 0
extraJDL-check.sh 241203_105216:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-12-03T12:20:09Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-12-03 13:20:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1130/console

```
{'TN': '241203_105221:cmsbot_crab_20241203_115219', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241203_105225:cmsbot_crab_20241203_115223', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'failed': 0, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105228:cmsbot_crab_20241203_115227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241203_105232:cmsbot_crab_20241203_115230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241203_105235:cmsbot_crab_20241203_115234', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/99/99'}
{'TN': '241203_105319:cmsbot_crab_20241203_115237', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241203_105324:cmsbot_crab_rucio_transfers_20241203_115321', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105327:cmsbot_crab_rucio_transfers_group_20241203_115326', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105331:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241203_115329', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105335:cmsbot_crab_rucio_transfers_nopublication_20241203_115333', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105340:cmsbot_crab_rucio_transfers_withnoneedm_20241203_115337', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '241203_105344:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241203_115342', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-12-03T13:52:10Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-12-03 14:52:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1131/console

```
{'TN': '241203_105221:cmsbot_crab_20241203_115219', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241203_105225:cmsbot_crab_20241203_115223', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 5, 'failed': 0}, 'publication (fail/tdb/DBS)': '0/0/1'}
{'TN': '241203_105228:cmsbot_crab_20241203_115227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241203_105232:cmsbot_crab_20241203_115230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241203_105235:cmsbot_crab_20241203_115234', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241203_105319:cmsbot_crab_20241203_115237', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241203_105324:cmsbot_crab_rucio_transfers_20241203_115321', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105327:cmsbot_crab_rucio_transfers_group_20241203_115326', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105331:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241203_115329', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105335:cmsbot_crab_rucio_transfers_nopublication_20241203_115333', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105340:cmsbot_crab_rucio_transfers_withnoneedm_20241203_115337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '241203_105344:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241203_115342', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-12-03T15:54:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-12-03 16:54:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1132/console

```
{'TN': '241203_105221:cmsbot_crab_20241203_115219', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241203_105225:cmsbot_crab_20241203_115223', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 5, 'failed': 0}, 'publication (fail/tdb/DBS)': '0/0/1'}
{'TN': '241203_105228:cmsbot_crab_20241203_115227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241203_105232:cmsbot_crab_20241203_115230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241203_105235:cmsbot_crab_20241203_115234', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241203_105319:cmsbot_crab_20241203_115237', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241203_105324:cmsbot_crab_rucio_transfers_20241203_115321', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105327:cmsbot_crab_rucio_transfers_group_20241203_115326', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105331:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241203_115329', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105335:cmsbot_crab_rucio_transfers_nopublication_20241203_115333', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105340:cmsbot_crab_rucio_transfers_withnoneedm_20241203_115337', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105344:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241203_115342', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-12-03T17:57:08Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-12-03 18:57:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1133/console

```
{'TN': '241203_105221:cmsbot_crab_20241203_115219', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241203_105225:cmsbot_crab_20241203_115223', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 5, 'failed': 0}, 'publication (fail/tdb/DBS)': '0/0/1'}
{'TN': '241203_105228:cmsbot_crab_20241203_115227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241203_105232:cmsbot_crab_20241203_115230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241203_105235:cmsbot_crab_20241203_115234', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241203_105319:cmsbot_crab_20241203_115237', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241203_105324:cmsbot_crab_rucio_transfers_20241203_115321', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105327:cmsbot_crab_rucio_transfers_group_20241203_115326', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105331:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241203_115329', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105335:cmsbot_crab_rucio_transfers_nopublication_20241203_115333', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241203_105340:cmsbot_crab_rucio_transfers_withnoneedm_20241203_115337', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241203_105344:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241203_115342', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
