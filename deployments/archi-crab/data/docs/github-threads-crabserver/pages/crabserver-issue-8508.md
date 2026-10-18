# dmwm/CRABServer issue #8508: #808: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-18T13:34:52Z
Closed: 2024-06-18T16:12:02Z
URL: https://github.com/dmwm/CRABServer/issues/8508

## Opening post (cmsdmwmbot, 2024-06-18T13:34:52Z)

**To validate current master (with PreJob fix) on crab-dev-tw01**

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-06-18 15:34:51
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/808/)

## Comment (cmsdmwmbot, 2024-06-18T13:37:16Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240618_133625:cmsbot_crab_20240618_153624
240618_133627:cmsbot_crab_20240618_153626
240618_133629:cmsbot_crab_20240618_153629
240618_133632:cmsbot_crab_20240618_153631
240618_133634:cmsbot_crab_20240618_153633
240618_133638:cmsbot_crab_20240618_153635
240618_133641:cmsbot_crab_rucio_transfers_20240618_153639
240618_133643:cmsbot_crab_rucio_transfers_group_20240618_153642
240618_133646:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240618_153645
240618_133648:cmsbot_crab_rucio_transfers_nopublication_20240618_153647
240618_133651:cmsbot_crab_rucio_transfers_withnoneedm_20240618_153650
240618_133654:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240618_153653
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240618_133515:cmsbot_crab_transferOutputs
240618_133517:cmsbot_crab_transferLogs
240618_133520:cmsbot_crab_activity
240618_133522:cmsbot_crab_inputFiles
240618_133524:cmsbot_crab_disableAutomaticOutputCollection
240618_133526:cmsbot_crab_outputFiles
240618_133529:cmsbot_crab_allowUndistributedCMSSW
240618_133531:cmsbot_crab_maxMemoryMB
240618_133534:cmsbot_crab_maxJobRuntimeMin
240618_133536:cmsbot_crab_numCores
240618_133538:cmsbot_crab_scriptExe
240618_133540:cmsbot_crab_scriptArgs
240618_133543:cmsbot_crab_sendVenvFolder
240618_133545:cmsbot_crab_sendExternalFolder
240618_133547:cmsbot_crab_inputDBS
240618_133549:cmsbot_crab_useParent
240618_133551:cmsbot_crab_secondaryInputDataset
240618_133553:cmsbot_crab_lumiMaskFile
240618_133556:cmsbot_crab_lumiMaskUrl
240618_133559:cmsbot_crab_outLFNDirBase
240618_133601:cmsbot_crab_runRange
240618_133603:cmsbot_crab_ignoreLocality
240618_133605:cmsbot_crab_userInputFiles
240618_133607:cmsbot_crab_whitelist
240618_133609:cmsbot_crab_blacklist
240618_133612:cmsbot_crab_ignoreGlobalBlacklist
240618_133614:cmsbot_crab_voRole
240618_133616:cmsbot_crab_voGroup
240618_133618:cmsbot_crab_scheddName
240618_133620:cmsbot_crab_collector
240618_133622:cmsbot_crab_extraJDL
```

Finished at: 2024-06-18 15:36:54
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/808/console)

## Comment (cmsdmwmbot, 2024-06-18T13:58:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-18 15:58:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1006/console

```
{'TN': '240618_133625:cmsbot_crab_20240618_153624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133627:cmsbot_crab_20240618_153626', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 1, 'finished': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133629:cmsbot_crab_20240618_153629', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133632:cmsbot_crab_20240618_153631', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133634:cmsbot_crab_20240618_153633', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133638:cmsbot_crab_20240618_153635', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 7, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133641:cmsbot_crab_rucio_transfers_20240618_153639', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133643:cmsbot_crab_rucio_transfers_group_20240618_153642', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133646:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240618_153645', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133648:cmsbot_crab_rucio_transfers_nopublication_20240618_153647', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133651:cmsbot_crab_rucio_transfers_withnoneedm_20240618_153650', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133654:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240618_153653', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-18T14:01:09Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-18 16:01:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1127/console

```
RETRY TESTS:
useParent-check.sh 240618_133549:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240618_133551:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240618_133556:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240618_133559:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240618_133601:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240618_133605:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240618_133607:cmsbot_crab_whitelist - 2
blacklist-check.sh 240618_133609:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240618_133612:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240618_133515:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240618_133517:cmsbot_crab_transferLogs - 0
activity-check.sh 240618_133520:cmsbot_crab_activity - 0
inputFiles-check.sh 240618_133522:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240618_133524:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240618_133526:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240618_133529:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240618_133531:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240618_133534:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240618_133536:cmsbot_crab_numCores - 0
scriptExe-check.sh 240618_133538:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240618_133540:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240618_133543:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240618_133545:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240618_133547:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240618_133553:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240618_133603:cmsbot_crab_ignoreLocality - 0
voRole-check.sh 240618_133614:cmsbot_crab_voRole - 0
voGroup-check.sh 240618_133616:cmsbot_crab_voGroup - 0
scheddName-check.sh 240618_133618:cmsbot_crab_scheddName - 0
collector-check.sh 240618_133620:cmsbot_crab_collector - 0
extraJDL-check.sh 240618_133622:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-18T14:14:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-18 16:14:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1007/console

```
{'TN': '240618_133625:cmsbot_crab_20240618_153624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133627:cmsbot_crab_20240618_153626', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133629:cmsbot_crab_20240618_153629', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133632:cmsbot_crab_20240618_153631', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133634:cmsbot_crab_20240618_153633', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133638:cmsbot_crab_20240618_153635', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133641:cmsbot_crab_rucio_transfers_20240618_153639', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133643:cmsbot_crab_rucio_transfers_group_20240618_153642', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133646:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240618_153645', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133648:cmsbot_crab_rucio_transfers_nopublication_20240618_153647', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133651:cmsbot_crab_rucio_transfers_withnoneedm_20240618_153650', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133654:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240618_153653', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-18T14:24:58Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-18 16:24:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1128/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240618_133515:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240618_133517:cmsbot_crab_transferLogs - 0
activity-check.sh 240618_133520:cmsbot_crab_activity - 0
inputFiles-check.sh 240618_133522:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240618_133524:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240618_133526:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240618_133529:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240618_133531:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240618_133534:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240618_133536:cmsbot_crab_numCores - 0
scriptExe-check.sh 240618_133538:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240618_133540:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240618_133543:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240618_133545:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240618_133547:cmsbot_crab_inputDBS - 0
useParent-check.sh 240618_133549:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240618_133551:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240618_133553:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240618_133556:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240618_133559:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240618_133601:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240618_133603:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240618_133605:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240618_133607:cmsbot_crab_whitelist - 0
blacklist-check.sh 240618_133609:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240618_133612:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240618_133614:cmsbot_crab_voRole - 0
voGroup-check.sh 240618_133616:cmsbot_crab_voGroup - 0
scheddName-check.sh 240618_133618:cmsbot_crab_scheddName - 0
collector-check.sh 240618_133620:cmsbot_crab_collector - 0
extraJDL-check.sh 240618_133622:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-18T15:00:26Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-18 17:00:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1008/console

```
{'TN': '240618_133625:cmsbot_crab_20240618_153624', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240618_133627:cmsbot_crab_20240618_153626', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133629:cmsbot_crab_20240618_153629', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240618_133632:cmsbot_crab_20240618_153631', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_133634:cmsbot_crab_20240618_153633', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240618_133638:cmsbot_crab_20240618_153635', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_133641:cmsbot_crab_rucio_transfers_20240618_153639', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133643:cmsbot_crab_rucio_transfers_group_20240618_153642', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133646:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240618_153645', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133648:cmsbot_crab_rucio_transfers_nopublication_20240618_153647', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133651:cmsbot_crab_rucio_transfers_withnoneedm_20240618_153650', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133654:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240618_153653', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-18T16:12:02Z)

CCV is fine. And DESY fixed their dCache !
But automatic splitting fails :-(
I opned #8509

## Comment (cmsdmwmbot, 2024-06-18T16:34:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-06-18 18:34:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1009/console

```
{'TN': '240618_133625:cmsbot_crab_20240618_153624', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240618_133627:cmsbot_crab_20240618_153626', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133629:cmsbot_crab_20240618_153629', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240618_133632:cmsbot_crab_20240618_153631', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_133634:cmsbot_crab_20240618_153633', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240618_133638:cmsbot_crab_20240618_153635', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_133641:cmsbot_crab_rucio_transfers_20240618_153639', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133643:cmsbot_crab_rucio_transfers_group_20240618_153642', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133646:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240618_153645', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133648:cmsbot_crab_rucio_transfers_nopublication_20240618_153647', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133651:cmsbot_crab_rucio_transfers_withnoneedm_20240618_153650', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133654:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240618_153653', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-18T18:36:27Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-06-18 20:36:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1010/console

```
{'TN': '240618_133625:cmsbot_crab_20240618_153624', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240618_133627:cmsbot_crab_20240618_153626', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133629:cmsbot_crab_20240618_153629', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240618_133632:cmsbot_crab_20240618_153631', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_133634:cmsbot_crab_20240618_153633', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240618_133638:cmsbot_crab_20240618_153635', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_133641:cmsbot_crab_rucio_transfers_20240618_153639', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133643:cmsbot_crab_rucio_transfers_group_20240618_153642', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133646:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240618_153645', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133648:cmsbot_crab_rucio_transfers_nopublication_20240618_153647', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133651:cmsbot_crab_rucio_transfers_withnoneedm_20240618_153650', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133654:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240618_153653', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-18T20:38:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-18 22:38:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1011/console

```
{'TN': '240618_133625:cmsbot_crab_20240618_153624', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240618_133627:cmsbot_crab_20240618_153626', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133629:cmsbot_crab_20240618_153629', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240618_133632:cmsbot_crab_20240618_153631', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_133634:cmsbot_crab_20240618_153633', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240618_133638:cmsbot_crab_20240618_153635', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240618_133641:cmsbot_crab_rucio_transfers_20240618_153639', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133643:cmsbot_crab_rucio_transfers_group_20240618_153642', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133646:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240618_153645', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133648:cmsbot_crab_rucio_transfers_nopublication_20240618_153647', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240618_133651:cmsbot_crab_rucio_transfers_withnoneedm_20240618_153650', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240618_133654:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240618_153653', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
