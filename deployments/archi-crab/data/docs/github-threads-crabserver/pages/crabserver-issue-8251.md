# dmwm/CRABServer issue #8251: #717: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-02-19T10:13:58Z
Closed: 2024-02-19T15:30:09Z
URL: https://github.com/dmwm/CRABServer/issues/8251

## Opening post (cmsdmwmbot, 2024-02-19T10:13:58Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-02-19 11:13:57
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/717/)

## Comment (cmsdmwmbot, 2024-02-19T10:16:09Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240219_101458:cmsbot_crab_20240219_111456
240219_101500:cmsbot_crab_20240219_111458
240219_101502:cmsbot_crab_20240219_111500
240219_101504:cmsbot_crab_20240219_111502
240219_101506:cmsbot_crab_20240219_111504
240219_101529:cmsbot_crab_20240219_111506
240219_101532:cmsbot_crab_rucio_transfers_20240219_111529
240219_101534:cmsbot_crab_rucio_transfers_group_20240219_111532
240219_101538:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111534
240219_101541:cmsbot_crab_rucio_transfers_nopublication_20240219_111538
240219_101545:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111541
240219_101548:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111545
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240219_101418:cmsbot_crab_transferOutputs
240219_101419:cmsbot_crab_transferLogs
240219_101420:cmsbot_crab_activity
240219_101422:cmsbot_crab_inputFiles
240219_101423:cmsbot_crab_disableAutomaticOutputCollection
240219_101425:cmsbot_crab_outputFiles
240219_101426:cmsbot_crab_allowUndistributedCMSSW
240219_101427:cmsbot_crab_maxMemoryMB
240219_101428:cmsbot_crab_maxJobRuntimeMin
240219_101429:cmsbot_crab_numCores
240219_101430:cmsbot_crab_scriptExe
240219_101431:cmsbot_crab_scriptArgs
240219_101434:cmsbot_crab_sendVenvFolder
240219_101438:cmsbot_crab_sendExternalFolder
240219_101439:cmsbot_crab_inputDBS
240219_101440:cmsbot_crab_useParent
240219_101441:cmsbot_crab_secondaryInputDataset
240219_101442:cmsbot_crab_lumiMaskFile
240219_101443:cmsbot_crab_lumiMaskUrl
240219_101445:cmsbot_crab_outLFNDirBase
240219_101446:cmsbot_crab_runRange
240219_101447:cmsbot_crab_ignoreLocality
240219_101448:cmsbot_crab_userInputFiles
240219_101449:cmsbot_crab_whitelist
240219_101449:cmsbot_crab_blacklist
240219_101451:cmsbot_crab_ignoreGlobalBlacklist
240219_101451:cmsbot_crab_voRole
240219_101452:cmsbot_crab_voGroup
240219_101453:cmsbot_crab_scheddName
240219_101454:cmsbot_crab_collector
240219_101455:cmsbot_crab_extraJDL
```

Finished at: 2024-02-19 11:15:48
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/717/console)

## Comment (cmsdmwmbot, 2024-02-19T10:37:39Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-19 11:37:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/776/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '240219_101458:cmsbot_crab_20240219_111456', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'finished': 5}, 'TN': '240219_101500:cmsbot_crab_20240219_111458', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240219_101502:cmsbot_crab_20240219_111500', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240219_101504:cmsbot_crab_20240219_111502', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '240219_101506:cmsbot_crab_20240219_111504', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'transferring': 8}, 'TN': '240219_101529:cmsbot_crab_20240219_111506', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101532:cmsbot_crab_rucio_transfers_20240219_111529', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101534:cmsbot_crab_rucio_transfers_group_20240219_111532', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101538:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111534', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101541:cmsbot_crab_rucio_transfers_nopublication_20240219_111538', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101545:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111541', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101548:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111545', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-19T10:45:47Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-19 11:45:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/963/console

```
RETRY TESTS:
activity-check.sh 240219_101420:cmsbot_crab_activity - 2
outputFiles-check.sh 240219_101425:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240219_101428:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240219_101429:cmsbot_crab_numCores - 2
scriptExe-check.sh 240219_101430:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240219_101443:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240219_101446:cmsbot_crab_runRange - 2
whitelist-check.sh 240219_101449:cmsbot_crab_whitelist - 2
blacklist-check.sh 240219_101449:cmsbot_crab_blacklist - 2
voGroup-check.sh 240219_101452:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240219_101418:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240219_101419:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240219_101422:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240219_101423:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240219_101426:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240219_101427:cmsbot_crab_maxMemoryMB - 0
scriptArgs-check.sh 240219_101431:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240219_101434:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240219_101438:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240219_101439:cmsbot_crab_inputDBS - 0
useParent-check.sh 240219_101440:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240219_101441:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240219_101442:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240219_101445:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240219_101447:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240219_101448:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240219_101451:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240219_101451:cmsbot_crab_voRole - 0
scheddName-check.sh 240219_101453:cmsbot_crab_scheddName - 0
collector-check.sh 240219_101454:cmsbot_crab_collector - 0
extraJDL-check.sh 240219_101455:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-19T10:54:31Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-02-19 11:54:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/778/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '240219_101458:cmsbot_crab_20240219_111456', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '240219_101500:cmsbot_crab_20240219_111458', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240219_101502:cmsbot_crab_20240219_111500', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240219_101504:cmsbot_crab_20240219_111502', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '240219_101506:cmsbot_crab_20240219_111504', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240219_101529:cmsbot_crab_20240219_111506', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101532:cmsbot_crab_rucio_transfers_20240219_111529', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101534:cmsbot_crab_rucio_transfers_group_20240219_111532', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101538:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111534', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101541:cmsbot_crab_rucio_transfers_nopublication_20240219_111538', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101545:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111541', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101548:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111545', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-19T11:12:37Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-02-19 12:12:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/966/console

```
RETRY TESTS:
activity-check.sh 240219_101420:cmsbot_crab_activity - 2
outputFiles-check.sh 240219_101425:cmsbot_crab_outputFiles - 2
numCores-check.sh 240219_101429:cmsbot_crab_numCores - 2
whitelist-check.sh 240219_101449:cmsbot_crab_whitelist - 2
blacklist-check.sh 240219_101449:cmsbot_crab_blacklist - 2
voGroup-check.sh 240219_101452:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240219_101418:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240219_101419:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240219_101422:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240219_101423:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240219_101426:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240219_101427:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240219_101428:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240219_101430:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240219_101431:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240219_101434:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240219_101438:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240219_101439:cmsbot_crab_inputDBS - 0
useParent-check.sh 240219_101440:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240219_101441:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240219_101442:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240219_101443:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240219_101445:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240219_101446:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240219_101447:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240219_101448:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240219_101451:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240219_101451:cmsbot_crab_voRole - 0
scheddName-check.sh 240219_101453:cmsbot_crab_scheddName - 0
collector-check.sh 240219_101454:cmsbot_crab_collector - 0
extraJDL-check.sh 240219_101455:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-19T11:38:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-02-19 12:38:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/967/console

```
RETRY TESTS:
activity-check.sh 240219_101420:cmsbot_crab_activity - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240219_101418:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240219_101419:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240219_101422:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240219_101423:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240219_101426:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240219_101427:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240219_101428:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240219_101429:cmsbot_crab_numCores - 0
scriptExe-check.sh 240219_101430:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240219_101431:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240219_101434:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240219_101438:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240219_101439:cmsbot_crab_inputDBS - 0
useParent-check.sh 240219_101440:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240219_101441:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240219_101442:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240219_101443:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240219_101445:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240219_101446:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240219_101447:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240219_101448:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240219_101449:cmsbot_crab_whitelist - 0
blacklist-check.sh 240219_101449:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240219_101451:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240219_101451:cmsbot_crab_voRole - 0
voGroup-check.sh 240219_101452:cmsbot_crab_voGroup - 0
scheddName-check.sh 240219_101453:cmsbot_crab_scheddName - 0
collector-check.sh 240219_101454:cmsbot_crab_collector - 0
extraJDL-check.sh 240219_101455:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240219_101425:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-19T11:40:16Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-02-19 12:40:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/780/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 811, 'transferring': 189}, 'TN': '240219_101458:cmsbot_crab_20240219_111456', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '240219_101500:cmsbot_crab_20240219_111458', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240219_101502:cmsbot_crab_20240219_111500', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'TN': '240219_101504:cmsbot_crab_20240219_111502', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 60, 'transferring': 40}, 'TN': '240219_101506:cmsbot_crab_20240219_111504', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'TN': '240219_101529:cmsbot_crab_20240219_111506', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'TN': '240219_101532:cmsbot_crab_rucio_transfers_20240219_111529', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101534:cmsbot_crab_rucio_transfers_group_20240219_111532', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'TN': '240219_101538:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111534', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 36, 'transferring': 4}, 'TN': '240219_101541:cmsbot_crab_rucio_transfers_nopublication_20240219_111538', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'TN': '240219_101545:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111541', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'TN': '240219_101548:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111545', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-19T12:04:58Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-19 13:04:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/968/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240219_101418:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240219_101419:cmsbot_crab_transferLogs - 0
activity-check.sh 240219_101420:cmsbot_crab_activity - 0
inputFiles-check.sh 240219_101422:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240219_101423:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240219_101426:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240219_101427:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240219_101428:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240219_101429:cmsbot_crab_numCores - 0
scriptExe-check.sh 240219_101430:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240219_101431:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240219_101434:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240219_101438:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240219_101439:cmsbot_crab_inputDBS - 0
useParent-check.sh 240219_101440:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240219_101441:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240219_101442:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240219_101443:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240219_101445:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240219_101446:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240219_101447:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240219_101448:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240219_101449:cmsbot_crab_whitelist - 0
blacklist-check.sh 240219_101449:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240219_101451:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240219_101451:cmsbot_crab_voRole - 0
voGroup-check.sh 240219_101452:cmsbot_crab_voGroup - 0
scheddName-check.sh 240219_101453:cmsbot_crab_scheddName - 0
collector-check.sh 240219_101454:cmsbot_crab_collector - 0
extraJDL-check.sh 240219_101455:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240219_101425:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-19T13:11:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-02-19 14:11:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/782/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240219_101458:cmsbot_crab_20240219_111456', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 6}, 'TN': '240219_101500:cmsbot_crab_20240219_111458', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240219_101502:cmsbot_crab_20240219_111500', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101504:cmsbot_crab_20240219_111502', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240219_101506:cmsbot_crab_20240219_111504', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101529:cmsbot_crab_20240219_111506', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101532:cmsbot_crab_rucio_transfers_20240219_111529', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101534:cmsbot_crab_rucio_transfers_group_20240219_111532', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101538:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111534', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101541:cmsbot_crab_rucio_transfers_nopublication_20240219_111538', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101545:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111541', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '1/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101548:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111545', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-19T15:12:47Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-02-19 16:12:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/783/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240219_101458:cmsbot_crab_20240219_111456', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 6}, 'TN': '240219_101500:cmsbot_crab_20240219_111458', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240219_101502:cmsbot_crab_20240219_111500', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101504:cmsbot_crab_20240219_111502', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240219_101506:cmsbot_crab_20240219_111504', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101529:cmsbot_crab_20240219_111506', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101532:cmsbot_crab_rucio_transfers_20240219_111529', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101534:cmsbot_crab_rucio_transfers_group_20240219_111532', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101538:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111534', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101541:cmsbot_crab_rucio_transfers_nopublication_20240219_111538', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101545:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111541', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '1/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101548:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111545', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-02-19T15:30:09Z)

all OK

## Comment (cmsdmwmbot, 2024-02-19T17:16:48Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-02-19 18:16:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/784/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240219_101458:cmsbot_crab_20240219_111456', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 6}, 'TN': '240219_101500:cmsbot_crab_20240219_111458', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240219_101502:cmsbot_crab_20240219_111500', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101504:cmsbot_crab_20240219_111502', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240219_101506:cmsbot_crab_20240219_111504', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101529:cmsbot_crab_20240219_111506', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101532:cmsbot_crab_rucio_transfers_20240219_111529', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101534:cmsbot_crab_rucio_transfers_group_20240219_111532', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101538:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111534', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101541:cmsbot_crab_rucio_transfers_nopublication_20240219_111538', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101545:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111541', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '1/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101548:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111545', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-19T20:30:38Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 0. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-02-19 21:30:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/785/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240219_101458:cmsbot_crab_20240219_111456', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 6}, 'TN': '240219_101500:cmsbot_crab_20240219_111458', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240219_101502:cmsbot_crab_20240219_111500', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101504:cmsbot_crab_20240219_111502', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240219_101506:cmsbot_crab_20240219_111504', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101529:cmsbot_crab_20240219_111506', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101532:cmsbot_crab_rucio_transfers_20240219_111529', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101534:cmsbot_crab_rucio_transfers_group_20240219_111532', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101538:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111534', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101541:cmsbot_crab_rucio_transfers_nopublication_20240219_111538', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101545:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111541', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '1/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101548:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111545', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```
