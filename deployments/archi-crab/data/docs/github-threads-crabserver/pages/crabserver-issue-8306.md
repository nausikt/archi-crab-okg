# dmwm/CRABServer issue #8306: #738: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-03-26T15:22:20Z
Closed: 2024-03-26T19:43:18Z
URL: https://github.com/dmwm/CRABServer/issues/8306

## Opening post (cmsdmwmbot, 2024-03-26T15:22:20Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-03-26 16:22:19
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/738/)

## Comment (cmsdmwmbot, 2024-03-26T15:24:58Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240326_152400:cmsbot_crab_20240326_162358
240326_152402:cmsbot_crab_20240326_162400
240326_152404:cmsbot_crab_20240326_162402
240326_152406:cmsbot_crab_20240326_162404
240326_152408:cmsbot_crab_20240326_162406
240326_152418:cmsbot_crab_20240326_162408
240326_152421:cmsbot_crab_rucio_transfers_20240326_162418
240326_152423:cmsbot_crab_rucio_transfers_group_20240326_162421
240326_152427:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162423
240326_152430:cmsbot_crab_rucio_transfers_nopublication_20240326_162427
240326_152434:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162430
240326_152437:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162434
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240326_152248:cmsbot_crab_transferOutputs
240326_152250:cmsbot_crab_transferLogs
240326_152252:cmsbot_crab_activity
240326_152255:cmsbot_crab_inputFiles
240326_152257:cmsbot_crab_disableAutomaticOutputCollection
240326_152300:cmsbot_crab_outputFiles
240326_152302:cmsbot_crab_allowUndistributedCMSSW
240326_152304:cmsbot_crab_maxMemoryMB
240326_152306:cmsbot_crab_maxJobRuntimeMin
240326_152309:cmsbot_crab_numCores
240326_152311:cmsbot_crab_scriptExe
240326_152313:cmsbot_crab_scriptArgs
240326_152316:cmsbot_crab_sendVenvFolder
240326_152322:cmsbot_crab_sendExternalFolder
240326_152325:cmsbot_crab_inputDBS
240326_152327:cmsbot_crab_useParent
240326_152328:cmsbot_crab_secondaryInputDataset
240326_152330:cmsbot_crab_lumiMaskFile
240326_152332:cmsbot_crab_lumiMaskUrl
240326_152335:cmsbot_crab_outLFNDirBase
240326_152337:cmsbot_crab_runRange
240326_152339:cmsbot_crab_ignoreLocality
240326_152341:cmsbot_crab_userInputFiles
240326_152343:cmsbot_crab_whitelist
240326_152345:cmsbot_crab_blacklist
240326_152347:cmsbot_crab_ignoreGlobalBlacklist
240326_152349:cmsbot_crab_voRole
240326_152351:cmsbot_crab_voGroup
240326_152353:cmsbot_crab_scheddName
240326_152355:cmsbot_crab_collector
240326_152357:cmsbot_crab_extraJDL
```

Finished at: 2024-03-26 16:24:37
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/738/console)

## Comment (cmsdmwmbot, 2024-03-26T15:45:50Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-26 16:45:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/841/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 4, 'transferring': 996}, 'TN': '240326_152400:cmsbot_crab_20240326_162358', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'finished': 5}, 'TN': '240326_152402:cmsbot_crab_20240326_162400', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240326_152404:cmsbot_crab_20240326_162402', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240326_152406:cmsbot_crab_20240326_162404', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'transferring': 98}, 'TN': '240326_152408:cmsbot_crab_20240326_162406', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 3, 'transferring': 7}, 'TN': '240326_152418:cmsbot_crab_20240326_162408', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152421:cmsbot_crab_rucio_transfers_20240326_162418', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152423:cmsbot_crab_rucio_transfers_group_20240326_162421', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152427:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162423', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152430:cmsbot_crab_rucio_transfers_nopublication_20240326_162427', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152434:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162430', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152437:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162434', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T15:52:15Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-26 16:52:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/994/console

```
RETRY TESTS:
numCores-check.sh 240326_152309:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240326_152332:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240326_152337:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240326_152341:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240326_152343:cmsbot_crab_whitelist - 2
blacklist-check.sh 240326_152345:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240326_152347:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240326_152349:cmsbot_crab_voRole - 2
voGroup-check.sh 240326_152351:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_152248:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_152250:cmsbot_crab_transferLogs - 0
activity-check.sh 240326_152252:cmsbot_crab_activity - 0
inputFiles-check.sh 240326_152255:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_152257:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240326_152300:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240326_152302:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240326_152304:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240326_152306:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240326_152311:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240326_152313:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240326_152316:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_152322:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_152325:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_152327:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_152328:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_152330:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240326_152335:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240326_152339:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 240326_152353:cmsbot_crab_scheddName - 0
collector-check.sh 240326_152355:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_152357:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-26T16:01:41Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-26 17:01:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/844/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 999}, 'TN': '240326_152400:cmsbot_crab_20240326_162358', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '240326_152402:cmsbot_crab_20240326_162400', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240326_152404:cmsbot_crab_20240326_162402', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240326_152406:cmsbot_crab_20240326_162404', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '240326_152408:cmsbot_crab_20240326_162406', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240326_152418:cmsbot_crab_20240326_162408', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152421:cmsbot_crab_rucio_transfers_20240326_162418', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152423:cmsbot_crab_rucio_transfers_group_20240326_162421', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152427:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162423', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152430:cmsbot_crab_rucio_transfers_nopublication_20240326_162427', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152434:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162430', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240326_152437:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162434', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T16:16:16Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-03-26 17:16:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/997/console

```
RETRY TESTS:
voGroup-check.sh 240326_152351:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_152248:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_152250:cmsbot_crab_transferLogs - 0
activity-check.sh 240326_152252:cmsbot_crab_activity - 0
inputFiles-check.sh 240326_152255:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_152257:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240326_152300:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240326_152302:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240326_152304:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240326_152306:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240326_152309:cmsbot_crab_numCores - 0
scriptExe-check.sh 240326_152311:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240326_152313:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240326_152316:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_152322:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_152325:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_152327:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_152328:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_152330:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240326_152332:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240326_152335:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240326_152337:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240326_152339:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240326_152341:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240326_152343:cmsbot_crab_whitelist - 0
blacklist-check.sh 240326_152345:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240326_152347:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240326_152349:cmsbot_crab_voRole - 0
scheddName-check.sh 240326_152353:cmsbot_crab_scheddName - 0
collector-check.sh 240326_152355:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_152357:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-26T16:39:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-03-26 17:39:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/999/console

```
RETRY TESTS:
voGroup-check.sh 240326_152351:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_152248:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_152250:cmsbot_crab_transferLogs - 0
activity-check.sh 240326_152252:cmsbot_crab_activity - 0
inputFiles-check.sh 240326_152255:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_152257:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240326_152300:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240326_152302:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240326_152304:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240326_152306:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240326_152309:cmsbot_crab_numCores - 0
scriptExe-check.sh 240326_152311:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240326_152313:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240326_152316:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_152322:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_152325:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_152327:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_152328:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_152330:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240326_152332:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240326_152335:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240326_152337:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240326_152339:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240326_152341:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240326_152343:cmsbot_crab_whitelist - 0
blacklist-check.sh 240326_152345:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240326_152347:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240326_152349:cmsbot_crab_voRole - 0
scheddName-check.sh 240326_152353:cmsbot_crab_scheddName - 0
collector-check.sh 240326_152355:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_152357:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-26T16:47:29Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-26 17:47:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/847/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'TN': '240326_152400:cmsbot_crab_20240326_162358', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/900/900'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '240326_152402:cmsbot_crab_20240326_162400', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240326_152404:cmsbot_crab_20240326_162402', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240326_152406:cmsbot_crab_20240326_162404', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240326_152408:cmsbot_crab_20240326_162406', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240326_152418:cmsbot_crab_20240326_162408', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152421:cmsbot_crab_rucio_transfers_20240326_162418', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152423:cmsbot_crab_rucio_transfers_group_20240326_162421', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152427:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162423', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152430:cmsbot_crab_rucio_transfers_nopublication_20240326_162427', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152434:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162430', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152437:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162434', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T17:02:43Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-03-26 18:02:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1000/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_152248:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_152250:cmsbot_crab_transferLogs - 0
activity-check.sh 240326_152252:cmsbot_crab_activity - 0
inputFiles-check.sh 240326_152255:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_152257:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240326_152300:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240326_152302:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240326_152304:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240326_152306:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240326_152309:cmsbot_crab_numCores - 0
scriptExe-check.sh 240326_152311:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240326_152313:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240326_152316:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_152322:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_152325:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_152327:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_152328:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_152330:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240326_152332:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240326_152335:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240326_152337:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240326_152339:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240326_152341:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240326_152343:cmsbot_crab_whitelist - 0
blacklist-check.sh 240326_152345:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240326_152347:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240326_152349:cmsbot_crab_voRole - 0
scheddName-check.sh 240326_152353:cmsbot_crab_scheddName - 0
collector-check.sh 240326_152355:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_152357:cmsbot_crab_extraJDL - 0

FAILED TESTS:
voGroup-check.sh 240326_152351:cmsbot_crab_voGroup - 1
```

## Comment (belforte, 2024-03-26T17:40:01Z)

one CCV job timed out for task `240326_152351:cmsbot_crab_voGroup` . I issued crab resubmit

## Comment (cmsdmwmbot, 2024-03-26T18:20:36Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-03-26 19:20:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/850/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240326_152400:cmsbot_crab_20240326_162358', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '240326_152402:cmsbot_crab_20240326_162400', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240326_152404:cmsbot_crab_20240326_162402', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240326_152406:cmsbot_crab_20240326_162404', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240326_152408:cmsbot_crab_20240326_162406', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240326_152418:cmsbot_crab_20240326_162408', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152421:cmsbot_crab_rucio_transfers_20240326_162418', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152423:cmsbot_crab_rucio_transfers_group_20240326_162421', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152427:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_162423', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152430:cmsbot_crab_rucio_transfers_nopublication_20240326_162427', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152434:cmsbot_crab_rucio_transfers_withnoneedm_20240326_162430', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240326_152437:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_162434', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T19:42:28Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2024-03-26 20:42:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1001/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_152248:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_152250:cmsbot_crab_transferLogs - 0
activity-check.sh 240326_152252:cmsbot_crab_activity - 0
inputFiles-check.sh 240326_152255:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_152257:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240326_152300:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240326_152302:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240326_152304:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240326_152306:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240326_152309:cmsbot_crab_numCores - 0
scriptExe-check.sh 240326_152311:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240326_152313:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240326_152316:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_152322:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_152325:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_152327:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_152328:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_152330:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240326_152332:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240326_152335:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240326_152337:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240326_152339:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240326_152341:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240326_152343:cmsbot_crab_whitelist - 0
blacklist-check.sh 240326_152345:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240326_152347:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240326_152349:cmsbot_crab_voRole - 0
voGroup-check.sh 240326_152351:cmsbot_crab_voGroup - 0
scheddName-check.sh 240326_152353:cmsbot_crab_scheddName - 0
collector-check.sh 240326_152355:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_152357:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-03-26T19:43:18Z)

ALL OK
