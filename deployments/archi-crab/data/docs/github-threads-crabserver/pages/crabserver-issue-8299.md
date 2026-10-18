# dmwm/CRABServer issue #8299: #732: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-18T20:44:22Z
Closed: 2024-03-19T20:21:12Z
URL: https://github.com/dmwm/CRABServer/issues/8299

## Opening post (cmsdmwmbot, 2024-03-18T20:44:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-03-18 21:44:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/732/)

## Comment (cmsdmwmbot, 2024-03-18T20:47:18Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240318_204627:cmsbot_crab_20240318_214626
240318_204629:cmsbot_crab_20240318_214628
240318_204631:cmsbot_crab_20240318_214630
240318_204633:cmsbot_crab_20240318_214632
240318_204635:cmsbot_crab_20240318_214634
240318_204639:cmsbot_crab_20240318_214636
240318_204642:cmsbot_crab_rucio_transfers_20240318_214641
240318_204644:cmsbot_crab_rucio_transfers_group_20240318_214644
240318_204647:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_214646
240318_204650:cmsbot_crab_rucio_transfers_nopublication_20240318_214648
240318_204654:cmsbot_crab_rucio_transfers_withnoneedm_20240318_214651
240318_204657:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_214655
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240318_204441:cmsbot_crab_transferOutputs
240318_204444:cmsbot_crab_transferLogs
240318_204446:cmsbot_crab_activity
240318_204448:cmsbot_crab_inputFiles
240318_204450:cmsbot_crab_disableAutomaticOutputCollection
240318_204452:cmsbot_crab_outputFiles
240318_204454:cmsbot_crab_allowUndistributedCMSSW
240318_204456:cmsbot_crab_maxMemoryMB
240318_204458:cmsbot_crab_maxJobRuntimeMin
240318_204500:cmsbot_crab_numCores
240318_204502:cmsbot_crab_scriptExe
240318_204504:cmsbot_crab_scriptArgs
240318_204506:cmsbot_crab_sendVenvFolder
240318_204548:cmsbot_crab_sendExternalFolder
240318_204550:cmsbot_crab_inputDBS
240318_204552:cmsbot_crab_useParent
240318_204554:cmsbot_crab_secondaryInputDataset
240318_204556:cmsbot_crab_lumiMaskFile
240318_204558:cmsbot_crab_lumiMaskUrl
240318_204601:cmsbot_crab_outLFNDirBase
240318_204603:cmsbot_crab_runRange
240318_204605:cmsbot_crab_ignoreLocality
240318_204607:cmsbot_crab_userInputFiles
240318_204610:cmsbot_crab_whitelist
240318_204612:cmsbot_crab_blacklist
240318_204614:cmsbot_crab_ignoreGlobalBlacklist
240318_204616:cmsbot_crab_voRole
240318_204618:cmsbot_crab_voGroup
240318_204620:cmsbot_crab_scheddName
240318_204622:cmsbot_crab_collector
240318_204624:cmsbot_crab_extraJDL
```

Finished at: 2024-03-18 21:46:57
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/732/console)

## Comment (cmsdmwmbot, 2024-03-18T21:09:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-18 22:09:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/814/console

```
{'TN': '240318_204627:cmsbot_crab_20240318_214626', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 989, 'running': 11}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204629:cmsbot_crab_20240318_214628', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204631:cmsbot_crab_20240318_214630', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204633:cmsbot_crab_20240318_214632', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204635:cmsbot_crab_20240318_214634', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204639:cmsbot_crab_20240318_214636', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 3, 'transferring': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204642:cmsbot_crab_rucio_transfers_20240318_214641', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204644:cmsbot_crab_rucio_transfers_group_20240318_214644', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204647:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_214646', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204650:cmsbot_crab_rucio_transfers_nopublication_20240318_214648', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204654:cmsbot_crab_rucio_transfers_withnoneedm_20240318_214651', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204657:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_214655', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-18T21:11:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-18 22:11:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/980/console

```
RETRY TESTS:
transferLogs-check.sh 240318_204444:cmsbot_crab_transferLogs - 2
activity-check.sh 240318_204446:cmsbot_crab_activity - 2
numCores-check.sh 240318_204500:cmsbot_crab_numCores - 2
scriptExe-check.sh 240318_204502:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240318_204504:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240318_204558:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240318_204603:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240318_204607:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240318_204610:cmsbot_crab_whitelist - 2
blacklist-check.sh 240318_204612:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240318_204441:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240318_204448:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240318_204450:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240318_204452:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240318_204454:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240318_204456:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240318_204458:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 240318_204506:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240318_204548:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240318_204550:cmsbot_crab_inputDBS - 0
useParent-check.sh 240318_204552:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240318_204554:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240318_204556:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240318_204601:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240318_204605:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240318_204614:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240318_204616:cmsbot_crab_voRole - 0
voGroup-check.sh 240318_204618:cmsbot_crab_voGroup - 0
scheddName-check.sh 240318_204620:cmsbot_crab_scheddName - 0
collector-check.sh 240318_204622:cmsbot_crab_collector - 0
extraJDL-check.sh 240318_204624:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-18T21:26:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-18 22:25:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/815/console

```
{'TN': '240318_204627:cmsbot_crab_20240318_214626', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 996, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204629:cmsbot_crab_20240318_214628', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204631:cmsbot_crab_20240318_214630', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204633:cmsbot_crab_20240318_214632', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204635:cmsbot_crab_20240318_214634', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204639:cmsbot_crab_20240318_214636', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204642:cmsbot_crab_rucio_transfers_20240318_214641', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204644:cmsbot_crab_rucio_transfers_group_20240318_214644', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204647:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_214646', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204650:cmsbot_crab_rucio_transfers_nopublication_20240318_214648', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204654:cmsbot_crab_rucio_transfers_withnoneedm_20240318_214651', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 34, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204657:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_214655', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-18T21:37:17Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-03-18 22:37:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/981/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240318_204441:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240318_204444:cmsbot_crab_transferLogs - 0
activity-check.sh 240318_204446:cmsbot_crab_activity - 0
inputFiles-check.sh 240318_204448:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240318_204450:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240318_204452:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240318_204454:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240318_204456:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240318_204458:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240318_204500:cmsbot_crab_numCores - 0
scriptExe-check.sh 240318_204502:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240318_204504:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240318_204506:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240318_204548:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240318_204550:cmsbot_crab_inputDBS - 0
useParent-check.sh 240318_204552:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240318_204554:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240318_204556:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240318_204558:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240318_204601:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240318_204603:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240318_204605:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240318_204607:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240318_204610:cmsbot_crab_whitelist - 0
blacklist-check.sh 240318_204612:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240318_204614:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240318_204616:cmsbot_crab_voRole - 0
voGroup-check.sh 240318_204618:cmsbot_crab_voGroup - 0
scheddName-check.sh 240318_204620:cmsbot_crab_scheddName - 0
collector-check.sh 240318_204622:cmsbot_crab_collector - 0
extraJDL-check.sh 240318_204624:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-18T22:14:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-18 23:14:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/817/console

```
{'TN': '240318_204627:cmsbot_crab_20240318_214626', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 999, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/905/905'}
{'TN': '240318_204629:cmsbot_crab_20240318_214628', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204631:cmsbot_crab_20240318_214630', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_204633:cmsbot_crab_20240318_214632', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_204635:cmsbot_crab_20240318_214634', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240318_204639:cmsbot_crab_20240318_214636', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_204642:cmsbot_crab_rucio_transfers_20240318_214641', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '38/1/1'}
{'TN': '240318_204644:cmsbot_crab_rucio_transfers_group_20240318_214644', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240318_204647:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_214646', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204650:cmsbot_crab_rucio_transfers_nopublication_20240318_214648', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204654:cmsbot_crab_rucio_transfers_withnoneedm_20240318_214651', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '16/24/24'}
{'TN': '240318_204657:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_214655', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-18T23:45:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-03-19 00:45:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/818/console

```
{'TN': '240318_204627:cmsbot_crab_20240318_214626', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240318_204629:cmsbot_crab_20240318_214628', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204631:cmsbot_crab_20240318_214630', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_204633:cmsbot_crab_20240318_214632', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_204635:cmsbot_crab_20240318_214634', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240318_204639:cmsbot_crab_20240318_214636', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_204642:cmsbot_crab_rucio_transfers_20240318_214641', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '38/2/2'}
{'TN': '240318_204644:cmsbot_crab_rucio_transfers_group_20240318_214644', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240318_204647:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_214646', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204650:cmsbot_crab_rucio_transfers_nopublication_20240318_214648', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204654:cmsbot_crab_rucio_transfers_withnoneedm_20240318_214651', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '16/24/24'}
{'TN': '240318_204657:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_214655', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-19T01:45:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-03-19 02:45:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/820/console

```
{'TN': '240318_204627:cmsbot_crab_20240318_214626', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240318_204629:cmsbot_crab_20240318_214628', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204631:cmsbot_crab_20240318_214630', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_204633:cmsbot_crab_20240318_214632', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_204635:cmsbot_crab_20240318_214634', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240318_204639:cmsbot_crab_20240318_214636', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_204642:cmsbot_crab_rucio_transfers_20240318_214641', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '38/2/2'}
{'TN': '240318_204644:cmsbot_crab_rucio_transfers_group_20240318_214644', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240318_204647:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_214646', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204650:cmsbot_crab_rucio_transfers_nopublication_20240318_214648', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204654:cmsbot_crab_rucio_transfers_withnoneedm_20240318_214651', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '16/24/24'}
{'TN': '240318_204657:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_214655', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-19T03:46:56Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-03-19 04:46:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/821/console

```
{'TN': '240318_204627:cmsbot_crab_20240318_214626', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240318_204629:cmsbot_crab_20240318_214628', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204631:cmsbot_crab_20240318_214630', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_204633:cmsbot_crab_20240318_214632', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_204635:cmsbot_crab_20240318_214634', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240318_204639:cmsbot_crab_20240318_214636', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_204642:cmsbot_crab_rucio_transfers_20240318_214641', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '38/2/2'}
{'TN': '240318_204644:cmsbot_crab_rucio_transfers_group_20240318_214644', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240318_204647:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_214646', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204650:cmsbot_crab_rucio_transfers_nopublication_20240318_214648', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_204654:cmsbot_crab_rucio_transfers_withnoneedm_20240318_214651', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '16/24/24'}
{'TN': '240318_204657:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_214655', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-03-19T16:17:49Z)

something bad happened to the automatic splitting task, there's no sign of the tail job in crab status
```
belforte@lxplus812/bot> crab status -d crab_20240318_214628/ --long 
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_20240318_214628
Task name:			240318_204629:cmsbot_crab_20240318_214628
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240318_204629%3Acmsbot_crab_20240318_214628
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240318_204629%3Acmsbot_crab_20240318_214628&from=1710791189000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_FR_GRIF', 'T2_UK_SGrid_Bristol']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	FAILED

The job splitting of this task is 'Automatic', please refer to this FAQ for a description of the jobs status summary:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_is_the_Automatic_splitting
Probe stage log:		https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/240318_204629:cmsbot_crab_20240318_214628/AutomaticSplitting_Log0.txt
More details of Automatic Splitting process for this task (including possible failures) are in the Dagman Log files in:
https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/240318_204629:cmsbot_crab_20240318_214628/AutomaticSplitting/

Probe jobs status:              no output    		100.0% (5/5)

Output dataset:			/GenericTTbar/cmsbot-autotest-1710794788-94ba0e06145abd65ccb1d21786dc7e1d/USER

No publication information available yet

Extended Job Status Table:

 Job State        Most Recent Site        Runtime   Mem (MB)      CPU %    Retries   Restarts      Waste       Exit Code
 0-1 no output    T2_US_UCSD              0:04:40        586         72          0          0    0:02:37               0
 0-2 no output    T2_US_Wisconsin         0:04:11       1019         55          0          0    0:02:39               0
 0-3 no output    T2_US_Wisconsin         0:03:23        977         62          0          0    0:02:40               0
 0-4 no output    T2_US_Wisconsin         0:03:25       1035         66          0          0    0:02:37               0
 0-5 no output    T2_US_Vanderbilt        0:04:22        382         57          0          0    0:02:36               0
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_20240318_214628/crab.log
belforte@lxplus812/bot> 

```
investigating

## Comment (belforte, 2024-03-19T16:25:15Z)

oh my
```
Mon, 18 Mar 2024 22:09:41 CET(+0100):INFO:DagmanCreator Resulting available sites: ['T3_IT_Trieste', 'T2_BE_IIHE', 'T2_RU_INR', 'T2_UA_KIPT', 'T2_IN_TIFR', 'T3_UK_London_RHUL', 'T3_US_FNALLPC', 'T2_FR_IPHC', 'T3_UK_ScotGrid_GLA', 'T2_HU_Budapest', 'T3_UK_London_QMUL', 'T2_PT_NCG_Lisbon', 'T2_CH_CERN', 'T2_FI_HIP', 'T2_US_Wisconsin', 'T2_ES_IFCA', 'T2_PK_NCP', 'T2_IT_Pisa', 'T2_PL_Swierk', 'T1_FR_CCIN2P3', 'T2_CN_Beijing', 'T1_UK_RAL', 'T2_BE_UCL', 'T3_US_Colorado', 'T3_US_UMiss', 'T1_IT_CNAF', 'T3_US_Baylor', 'T2_US_UCSD', 'T1_US_FNAL', 'T2_TW_NCHC', 'T2_KR_KISTI', 'T2_UK_London_Brunel', 'T2_RU_JINR', 'T2_BR_SPRACE', 'T2_TR_METU', 'T3_US_UMD', 'T2_US_MIT', 'T2_UK_SGrid_RALPP', 'T3_US_PuertoRico', 'T1_DE_KIT', 'T2_ES_CIEMAT', 'T2_IT_Rome', 'T2_US_Florida', 'T2_AT_Vienna', 'T2_CH_CSCS', 'T2_DE_DESY', 'T1_RU_JINR', 'T3_TW_NCU', 'T2_UK_London_IC', 'T2_EE_Estonia', 'T2_DE_RWTH', 'T2_US_Caltech', 'T2_US_Nebraska', 'T2_IT_Legnaro', 'T2_RU_ITEP', 'T2_US_Vanderbilt', 'T2_US_Purdue', 'T2_PL_Cyfronet', 'T2_IT_Bari', 'T1_ES_PIC', 'T3_KR_KNU', 'T2_RU_IHEP']
Mon, 18 Mar 2024 22:09:41 CET(+0100):DEBUG:DagmanCreator The site whitelist and blacklist will be applied by the pre-job. This is expected to result in DESIRED_SITES = ['T2_FR_IPHC', 'T2_US_Wisconsin', 'T2_ES_IFCA', 'T2_IT_Pisa', 'T1_FR_CCIN2P3', 'T1_UK_RAL', 'T1_IT_CNAF', 'T2_US_UCSD', 'T1_US_FNAL', 'T2_UK_London_Brunel', 'T2_US_MIT', 'T2_UK_SGrid_RALPP', 'T1_DE_KIT', 'T2_ES_CIEMAT', 'T2_IT_Rome', 'T2_US_Florida', 'T2_DE_DESY', 'T1_RU_JINR', 'T2_UK_London_IC', 'T2_DE_RWTH', 'T2_US_Caltech', 'T2_US_Nebraska', 'T2_IT_Legnaro', 'T2_US_Vanderbilt', 'T2_US_Purdue', 'T2_IT_Bari', 'T1_ES_PIC']
Got a fatal exception: 'ClassAdFileIterator' object does not support item assignment
Traceback (most recent call last):
  File "/usr/lib64/python3.6/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib64/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/data/srv/glidecondor/condor_local/spool/6907/0/cluster9536907.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py", line 85, in <module>
    retval = bootstrap()
  File "/data/srv/glidecondor/condor_local/spool/6907/0/cluster9536907.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py", line 28, in bootstrap
    return PreDAG.PreDAG().execute(*sys.argv[2:])
  File "/data/srv/glidecondor/condor_local/spool/6907/0/cluster9536907.proc0.subproc0/TaskWorker/Actions/PreDAG.py", line 142, in execute
    retval = self.executeInternal(*args)
  File "/data/srv/glidecondor/condor_local/spool/6907/0/cluster9536907.proc0.subproc0/TaskWorker/Actions/PreDAG.py", line 312, in executeInternal
    creator.createSubdag(split_result.result, task=task, parent=parent, stage=self.stage)
  File "/data/srv/glidecondor/condor_local/spool/6907/0/cluster9536907.proc0.subproc0/TaskWorker/Actions/DagmanCreator.py", line 948, in createSubdag
    datasites, outfiles, startjobid, parent=parent, stage=stage)
  File "/data/srv/glidecondor/condor_local/spool/6907/0/cluster9536907.proc0.subproc0/TaskWorker/Actions/DagmanCreator.py", line 619, in makeDagSpecs
    sitead['Job{0}'.format(count)] = list(availablesites)
TypeError: 'ClassAdFileIterator' object does not support item assignment
belforte@vocms059/prejob_logs> 

```

## Comment (belforte, 2024-03-19T20:21:12Z)

problem is https://github.com/dmwm/CRABServer/issues/8285#issuecomment-2008059316
