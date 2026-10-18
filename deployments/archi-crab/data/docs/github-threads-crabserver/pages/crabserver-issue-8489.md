# dmwm/CRABServer issue #8489: #802: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-11T21:14:15Z
Closed: 2024-06-12T07:32:41Z
URL: https://github.com/dmwm/CRABServer/issues/8489

## Opening post (cmsdmwmbot, 2024-06-11T21:14:15Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-06-11 23:14:14
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/802/)

## Comment (cmsdmwmbot, 2024-06-11T21:16:41Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240611_211550:cmsbot_crab_20240611_231549
240611_211552:cmsbot_crab_20240611_231551
240611_211554:cmsbot_crab_20240611_231554
240611_211557:cmsbot_crab_20240611_231556
240611_211559:cmsbot_crab_20240611_231558
240611_211603:cmsbot_crab_20240611_231600
240611_211605:cmsbot_crab_rucio_transfers_20240611_231604
240611_211608:cmsbot_crab_rucio_transfers_group_20240611_231607
240611_211611:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240611_231609
240611_211614:cmsbot_crab_rucio_transfers_nopublication_20240611_231612
240611_211617:cmsbot_crab_rucio_transfers_withnoneedm_20240611_231615
240611_211619:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240611_231618
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240611_211439:cmsbot_crab_transferOutputs
240611_211442:cmsbot_crab_transferLogs
240611_211444:cmsbot_crab_activity
240611_211446:cmsbot_crab_inputFiles
240611_211448:cmsbot_crab_disableAutomaticOutputCollection
240611_211450:cmsbot_crab_outputFiles
240611_211452:cmsbot_crab_allowUndistributedCMSSW
240611_211455:cmsbot_crab_maxMemoryMB
240611_211457:cmsbot_crab_maxJobRuntimeMin
240611_211459:cmsbot_crab_numCores
240611_211501:cmsbot_crab_scriptExe
240611_211504:cmsbot_crab_scriptArgs
240611_211506:cmsbot_crab_sendVenvFolder
240611_211508:cmsbot_crab_sendExternalFolder
240611_211511:cmsbot_crab_inputDBS
240611_211513:cmsbot_crab_useParent
240611_211515:cmsbot_crab_secondaryInputDataset
240611_211517:cmsbot_crab_lumiMaskFile
240611_211520:cmsbot_crab_lumiMaskUrl
240611_211522:cmsbot_crab_outLFNDirBase
240611_211525:cmsbot_crab_runRange
240611_211527:cmsbot_crab_ignoreLocality
240611_211529:cmsbot_crab_userInputFiles
240611_211531:cmsbot_crab_whitelist
240611_211534:cmsbot_crab_blacklist
240611_211536:cmsbot_crab_ignoreGlobalBlacklist
240611_211538:cmsbot_crab_voRole
240611_211540:cmsbot_crab_voGroup
240611_211543:cmsbot_crab_scheddName
240611_211545:cmsbot_crab_collector
240611_211547:cmsbot_crab_extraJDL
```

Finished at: 2024-06-11 23:16:20
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/802/console)

## Comment (cmsdmwmbot, 2024-06-11T21:37:38Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-11 23:37:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/988/console

```
{'TN': '240611_211550:cmsbot_crab_20240611_231549', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211552:cmsbot_crab_20240611_231551', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1, 'finished': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211554:cmsbot_crab_20240611_231554', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211557:cmsbot_crab_20240611_231556', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211559:cmsbot_crab_20240611_231558', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211603:cmsbot_crab_20240611_231600', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211605:cmsbot_crab_rucio_transfers_20240611_231604', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211608:cmsbot_crab_rucio_transfers_group_20240611_231607', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211611:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240611_231609', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211614:cmsbot_crab_rucio_transfers_nopublication_20240611_231612', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211617:cmsbot_crab_rucio_transfers_withnoneedm_20240611_231615', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211619:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240611_231618', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-11T21:40:25Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-11 23:40:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1112/console

```
RETRY TESTS:
transferLogs-check.sh 240611_211442:cmsbot_crab_transferLogs - 2
maxJobRuntimeMin-check.sh 240611_211457:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240611_211459:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240611_211504:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240611_211520:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240611_211525:cmsbot_crab_runRange - 2
whitelist-check.sh 240611_211531:cmsbot_crab_whitelist - 2
blacklist-check.sh 240611_211534:cmsbot_crab_blacklist - 2
voGroup-check.sh 240611_211540:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240611_211439:cmsbot_crab_transferOutputs - 0
activity-check.sh 240611_211444:cmsbot_crab_activity - 0
inputFiles-check.sh 240611_211446:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240611_211448:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240611_211450:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240611_211452:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240611_211455:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240611_211501:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240611_211506:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240611_211508:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240611_211511:cmsbot_crab_inputDBS - 0
useParent-check.sh 240611_211513:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240611_211515:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240611_211517:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240611_211522:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240611_211527:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240611_211529:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240611_211536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240611_211538:cmsbot_crab_voRole - 0
scheddName-check.sh 240611_211543:cmsbot_crab_scheddName - 0
collector-check.sh 240611_211545:cmsbot_crab_collector - 0
extraJDL-check.sh 240611_211547:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-11T21:53:40Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-11 23:53:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/989/console

```
{'TN': '240611_211550:cmsbot_crab_20240611_231549', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211552:cmsbot_crab_20240611_231551', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211554:cmsbot_crab_20240611_231554', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211557:cmsbot_crab_20240611_231556', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211559:cmsbot_crab_20240611_231558', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211603:cmsbot_crab_20240611_231600', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211605:cmsbot_crab_rucio_transfers_20240611_231604', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211608:cmsbot_crab_rucio_transfers_group_20240611_231607', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211611:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240611_231609', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211614:cmsbot_crab_rucio_transfers_nopublication_20240611_231612', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211617:cmsbot_crab_rucio_transfers_withnoneedm_20240611_231615', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211619:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240611_231618', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-11T22:04:35Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-12 00:04:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1113/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240611_211439:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240611_211442:cmsbot_crab_transferLogs - 0
activity-check.sh 240611_211444:cmsbot_crab_activity - 0
inputFiles-check.sh 240611_211446:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240611_211448:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240611_211450:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240611_211452:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240611_211455:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240611_211457:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240611_211459:cmsbot_crab_numCores - 0
scriptExe-check.sh 240611_211501:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240611_211504:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240611_211506:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240611_211508:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240611_211511:cmsbot_crab_inputDBS - 0
useParent-check.sh 240611_211513:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240611_211515:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240611_211517:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240611_211520:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240611_211522:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240611_211525:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240611_211527:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240611_211529:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240611_211531:cmsbot_crab_whitelist - 0
blacklist-check.sh 240611_211534:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240611_211536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240611_211538:cmsbot_crab_voRole - 0
voGroup-check.sh 240611_211540:cmsbot_crab_voGroup - 0
scheddName-check.sh 240611_211543:cmsbot_crab_scheddName - 0
collector-check.sh 240611_211545:cmsbot_crab_collector - 0
extraJDL-check.sh 240611_211547:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-11T22:39:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-12 00:39:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/990/console

```
{'TN': '240611_211550:cmsbot_crab_20240611_231549', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240611_211552:cmsbot_crab_20240611_231551', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211554:cmsbot_crab_20240611_231554', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240611_211557:cmsbot_crab_20240611_231556', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240611_211559:cmsbot_crab_20240611_231558', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240611_211603:cmsbot_crab_20240611_231600', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240611_211605:cmsbot_crab_rucio_transfers_20240611_231604', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240611_211608:cmsbot_crab_rucio_transfers_group_20240611_231607', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240611_211611:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240611_231609', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211614:cmsbot_crab_rucio_transfers_nopublication_20240611_231612', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211617:cmsbot_crab_rucio_transfers_withnoneedm_20240611_231615', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240611_211619:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240611_231618', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-12T00:12:08Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-06-12 02:12:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/991/console

```
{'TN': '240611_211550:cmsbot_crab_20240611_231549', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240611_211552:cmsbot_crab_20240611_231551', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240611_211554:cmsbot_crab_20240611_231554', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240611_211557:cmsbot_crab_20240611_231556', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240611_211559:cmsbot_crab_20240611_231558', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240611_211603:cmsbot_crab_20240611_231600', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240611_211605:cmsbot_crab_rucio_transfers_20240611_231604', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240611_211608:cmsbot_crab_rucio_transfers_group_20240611_231607', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240611_211611:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240611_231609', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211614:cmsbot_crab_rucio_transfers_nopublication_20240611_231612', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240611_211617:cmsbot_crab_rucio_transfers_withnoneedm_20240611_231615', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240611_211619:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240611_231618', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-12T07:32:42Z)

ALL OK !
