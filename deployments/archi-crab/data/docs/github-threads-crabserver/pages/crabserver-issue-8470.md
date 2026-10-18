# dmwm/CRABServer issue #8470: #796: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-03T22:51:28Z
Closed: 2024-06-04T07:21:57Z
URL: https://github.com/dmwm/CRABServer/issues/8470

## Opening post (cmsdmwmbot, 2024-06-03T22:51:28Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-06-04 00:51:27
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/796/)

## Comment (cmsdmwmbot, 2024-06-03T22:53:55Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240603_225303:cmsbot_crab_20240604_005302
240603_225305:cmsbot_crab_20240604_005304
240603_225307:cmsbot_crab_20240604_005306
240603_225309:cmsbot_crab_20240604_005309
240603_225311:cmsbot_crab_20240604_005311
240603_225315:cmsbot_crab_20240604_005313
240603_225318:cmsbot_crab_rucio_transfers_20240604_005317
240603_225321:cmsbot_crab_rucio_transfers_group_20240604_005320
240603_225324:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_005322
240603_225327:cmsbot_crab_rucio_transfers_nopublication_20240604_005326
240603_225330:cmsbot_crab_rucio_transfers_withnoneedm_20240604_005329
240603_225334:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_005332
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240603_225152:cmsbot_crab_transferOutputs
240603_225155:cmsbot_crab_transferLogs
240603_225157:cmsbot_crab_activity
240603_225159:cmsbot_crab_inputFiles
240603_225201:cmsbot_crab_disableAutomaticOutputCollection
240603_225203:cmsbot_crab_outputFiles
240603_225205:cmsbot_crab_allowUndistributedCMSSW
240603_225208:cmsbot_crab_maxMemoryMB
240603_225210:cmsbot_crab_maxJobRuntimeMin
240603_225212:cmsbot_crab_numCores
240603_225214:cmsbot_crab_scriptExe
240603_225216:cmsbot_crab_scriptArgs
240603_225219:cmsbot_crab_sendVenvFolder
240603_225221:cmsbot_crab_sendExternalFolder
240603_225223:cmsbot_crab_inputDBS
240603_225226:cmsbot_crab_useParent
240603_225228:cmsbot_crab_secondaryInputDataset
240603_225230:cmsbot_crab_lumiMaskFile
240603_225232:cmsbot_crab_lumiMaskUrl
240603_225235:cmsbot_crab_outLFNDirBase
240603_225237:cmsbot_crab_runRange
240603_225240:cmsbot_crab_ignoreLocality
240603_225242:cmsbot_crab_userInputFiles
240603_225244:cmsbot_crab_whitelist
240603_225246:cmsbot_crab_blacklist
240603_225248:cmsbot_crab_ignoreGlobalBlacklist
240603_225251:cmsbot_crab_voRole
240603_225253:cmsbot_crab_voGroup
240603_225255:cmsbot_crab_scheddName
240603_225258:cmsbot_crab_collector
240603_225300:cmsbot_crab_extraJDL
```

Finished at: 2024-06-04 00:53:34
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/796/console)

## Comment (cmsdmwmbot, 2024-06-03T23:14:53Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-04 01:14:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/962/console

```
{'TN': '240603_225303:cmsbot_crab_20240604_005302', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 987, 'running': 12, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225305:cmsbot_crab_20240604_005304', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225307:cmsbot_crab_20240604_005306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225309:cmsbot_crab_20240604_005309', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225311:cmsbot_crab_20240604_005311', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225315:cmsbot_crab_20240604_005313', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 3, 'running': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225318:cmsbot_crab_rucio_transfers_20240604_005317', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225321:cmsbot_crab_rucio_transfers_group_20240604_005320', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225324:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_005322', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225327:cmsbot_crab_rucio_transfers_nopublication_20240604_005326', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225330:cmsbot_crab_rucio_transfers_withnoneedm_20240604_005329', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225334:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_005332', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T23:17:33Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-04 01:17:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1098/console

```
RETRY TESTS:
activity-check.sh 240603_225157:cmsbot_crab_activity - 2
outputFiles-check.sh 240603_225203:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240603_225208:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 240603_225212:cmsbot_crab_numCores - 2
scriptExe-check.sh 240603_225214:cmsbot_crab_scriptExe - 2
lumiMaskFile-check.sh 240603_225230:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240603_225232:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240603_225235:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240603_225237:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240603_225242:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240603_225244:cmsbot_crab_whitelist - 2
blacklist-check.sh 240603_225246:cmsbot_crab_blacklist - 2
voRole-check.sh 240603_225251:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_225152:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_225155:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240603_225159:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_225201:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240603_225205:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240603_225210:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 240603_225216:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240603_225219:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_225221:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_225223:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_225226:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_225228:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240603_225240:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240603_225248:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240603_225253:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_225255:cmsbot_crab_scheddName - 0
collector-check.sh 240603_225258:cmsbot_crab_collector - 0
extraJDL-check.sh 240603_225300:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-03T23:30:48Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-04 01:30:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/963/console

```
{'TN': '240603_225303:cmsbot_crab_20240604_005302', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225305:cmsbot_crab_20240604_005304', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225307:cmsbot_crab_20240604_005306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225309:cmsbot_crab_20240604_005309', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225311:cmsbot_crab_20240604_005311', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225315:cmsbot_crab_20240604_005313', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225318:cmsbot_crab_rucio_transfers_20240604_005317', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225321:cmsbot_crab_rucio_transfers_group_20240604_005320', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225324:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_005322', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225327:cmsbot_crab_rucio_transfers_nopublication_20240604_005326', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225330:cmsbot_crab_rucio_transfers_withnoneedm_20240604_005329', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225334:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_005332', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T23:41:42Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-04 01:41:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1100/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_225152:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_225155:cmsbot_crab_transferLogs - 0
activity-check.sh 240603_225157:cmsbot_crab_activity - 0
inputFiles-check.sh 240603_225159:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_225201:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240603_225203:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240603_225205:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240603_225208:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240603_225210:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240603_225212:cmsbot_crab_numCores - 0
scriptExe-check.sh 240603_225214:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240603_225216:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240603_225219:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_225221:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_225223:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_225226:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_225228:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240603_225230:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240603_225232:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240603_225235:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240603_225237:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240603_225240:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_225242:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240603_225244:cmsbot_crab_whitelist - 0
blacklist-check.sh 240603_225246:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240603_225248:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_225251:cmsbot_crab_voRole - 0
voGroup-check.sh 240603_225253:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_225255:cmsbot_crab_scheddName - 0
collector-check.sh 240603_225258:cmsbot_crab_collector - 0
extraJDL-check.sh 240603_225300:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-04T00:17:52Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-04 02:17:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/966/console

```
{'TN': '240603_225303:cmsbot_crab_20240604_005302', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240603_225305:cmsbot_crab_20240604_005304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225307:cmsbot_crab_20240604_005306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_225309:cmsbot_crab_20240604_005309', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_225311:cmsbot_crab_20240604_005311', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_225315:cmsbot_crab_20240604_005313', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_225318:cmsbot_crab_rucio_transfers_20240604_005317', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_225321:cmsbot_crab_rucio_transfers_group_20240604_005320', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_225324:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_005322', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225327:cmsbot_crab_rucio_transfers_nopublication_20240604_005326', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225330:cmsbot_crab_rucio_transfers_withnoneedm_20240604_005329', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_225334:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_005332', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-04T01:50:46Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-06-04 03:50:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/969/console

```
{'TN': '240603_225303:cmsbot_crab_20240604_005302', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240603_225305:cmsbot_crab_20240604_005304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_225307:cmsbot_crab_20240604_005306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_225309:cmsbot_crab_20240604_005309', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_225311:cmsbot_crab_20240604_005311', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_225315:cmsbot_crab_20240604_005313', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_225318:cmsbot_crab_rucio_transfers_20240604_005317', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_225321:cmsbot_crab_rucio_transfers_group_20240604_005320', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_225324:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_005322', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225327:cmsbot_crab_rucio_transfers_nopublication_20240604_005326', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_225330:cmsbot_crab_rucio_transfers_withnoneedm_20240604_005329', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_225334:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_005332', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-04T07:21:57Z)

All OK
