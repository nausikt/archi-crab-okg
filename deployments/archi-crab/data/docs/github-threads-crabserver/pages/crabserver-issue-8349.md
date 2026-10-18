# dmwm/CRABServer issue #8349: #761: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-23T16:02:52Z
Closed: 2024-04-24T15:02:04Z
URL: https://github.com/dmwm/CRABServer/issues/8349

## Opening post (cmsdmwmbot, 2024-04-23T16:02:52Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-04-23 18:02:51
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/761/)

## Comment (cmsdmwmbot, 2024-04-23T16:06:13Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240423_160459:cmsbot_crab_20240423_180458
240423_160501:cmsbot_crab_20240423_180501
240423_160503:cmsbot_crab_20240423_180503
240423_160506:cmsbot_crab_20240423_180505
240423_160508:cmsbot_crab_20240423_180507
240423_160533:cmsbot_crab_20240423_180510
240423_160536:cmsbot_crab_rucio_transfers_20240423_180535
240423_160539:cmsbot_crab_rucio_transfers_group_20240423_180538
240423_160542:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240423_180540
240423_160545:cmsbot_crab_rucio_transfers_nopublication_20240423_180543
240423_160548:cmsbot_crab_rucio_transfers_withnoneedm_20240423_180547
240423_160551:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240423_180550
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240423_160352:cmsbot_crab_transferOutputs
240423_160354:cmsbot_crab_transferLogs
240423_160356:cmsbot_crab_activity
240423_160358:cmsbot_crab_inputFiles
240423_160400:cmsbot_crab_disableAutomaticOutputCollection
240423_160402:cmsbot_crab_outputFiles
240423_160404:cmsbot_crab_allowUndistributedCMSSW
240423_160407:cmsbot_crab_maxMemoryMB
240423_160409:cmsbot_crab_maxJobRuntimeMin
240423_160411:cmsbot_crab_numCores
240423_160413:cmsbot_crab_scriptExe
240423_160415:cmsbot_crab_scriptArgs
240423_160418:cmsbot_crab_sendVenvFolder
240423_160420:cmsbot_crab_sendExternalFolder
240423_160422:cmsbot_crab_inputDBS
240423_160424:cmsbot_crab_useParent
240423_160426:cmsbot_crab_secondaryInputDataset
240423_160428:cmsbot_crab_lumiMaskFile
240423_160431:cmsbot_crab_lumiMaskUrl
240423_160434:cmsbot_crab_outLFNDirBase
240423_160436:cmsbot_crab_runRange
240423_160438:cmsbot_crab_ignoreLocality
240423_160440:cmsbot_crab_userInputFiles
240423_160442:cmsbot_crab_whitelist
240423_160444:cmsbot_crab_blacklist
240423_160446:cmsbot_crab_ignoreGlobalBlacklist
240423_160448:cmsbot_crab_voRole
240423_160450:cmsbot_crab_voGroup
240423_160452:cmsbot_crab_scheddName
240423_160454:cmsbot_crab_collector
240423_160456:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240423_160349:cmsbot_crab_20240423_180348
```

Finished at: 2024-04-23 18:05:52
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/761/console)

## Comment (cmsdmwmbot, 2024-04-23T16:30:22Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-23 18:30:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/873/console

```
{'TN': '240423_160459:cmsbot_crab_20240423_180458', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 993, 'running': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160501:cmsbot_crab_20240423_180501', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160503:cmsbot_crab_20240423_180503', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160506:cmsbot_crab_20240423_180505', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160508:cmsbot_crab_20240423_180507', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160533:cmsbot_crab_20240423_180510', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160536:cmsbot_crab_rucio_transfers_20240423_180535', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160539:cmsbot_crab_rucio_transfers_group_20240423_180538', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160542:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240423_180540', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160545:cmsbot_crab_rucio_transfers_nopublication_20240423_180543', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160548:cmsbot_crab_rucio_transfers_withnoneedm_20240423_180547', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160551:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240423_180550', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-23T16:33:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-23 18:33:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1039/console

```
RETRY TESTS:
transferLogs-check.sh 240423_160354:cmsbot_crab_transferLogs - 2
activity-check.sh 240423_160356:cmsbot_crab_activity - 2
outputFiles-check.sh 240423_160402:cmsbot_crab_outputFiles - 2
scriptExe-check.sh 240423_160413:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240423_160415:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240423_160431:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240423_160436:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240423_160440:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240423_160442:cmsbot_crab_whitelist - 2
blacklist-check.sh 240423_160444:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240423_160352:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240423_160358:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240423_160400:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240423_160404:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240423_160407:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240423_160409:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240423_160411:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240423_160418:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240423_160420:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240423_160422:cmsbot_crab_inputDBS - 0
useParent-check.sh 240423_160424:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240423_160426:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240423_160428:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240423_160434:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240423_160438:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240423_160446:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240423_160448:cmsbot_crab_voRole - 0
voGroup-check.sh 240423_160450:cmsbot_crab_voGroup - 0
scheddName-check.sh 240423_160452:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240423_160456:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240423_160454:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-23T16:33:29Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-23 18:33:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/535/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/535//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-23T16:47:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-04-23 18:47:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/874/console

```
{'TN': '240423_160459:cmsbot_crab_20240423_180458', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 551, 'transferring': 444, 'running': 5}, 'publication (fail/tdb/DBS)': '0/300/300'}
{'TN': '240423_160501:cmsbot_crab_20240423_180501', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160503:cmsbot_crab_20240423_180503', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240423_160506:cmsbot_crab_20240423_180505', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240423_160508:cmsbot_crab_20240423_180507', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 87, 'transferring': 13}, 'publication (fail/tdb/DBS)': '0/87/87'}
{'TN': '240423_160533:cmsbot_crab_20240423_180510', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160536:cmsbot_crab_rucio_transfers_20240423_180535', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 36, 'transferring': 4}, 'publication (fail/tdb/DBS)': '0/37/37'}
{'TN': '240423_160539:cmsbot_crab_rucio_transfers_group_20240423_180538', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 34, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/35/35'}
{'TN': '240423_160542:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240423_180540', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 32, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160545:cmsbot_crab_rucio_transfers_nopublication_20240423_180543', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160548:cmsbot_crab_rucio_transfers_withnoneedm_20240423_180547', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 34, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/35/35'}
{'TN': '240423_160551:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240423_180550', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-23T16:58:31Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-23 18:58:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1040/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240423_160352:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240423_160354:cmsbot_crab_transferLogs - 0
activity-check.sh 240423_160356:cmsbot_crab_activity - 0
inputFiles-check.sh 240423_160358:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240423_160400:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240423_160404:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240423_160407:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240423_160409:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240423_160411:cmsbot_crab_numCores - 0
scriptExe-check.sh 240423_160413:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240423_160415:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240423_160418:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240423_160420:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240423_160422:cmsbot_crab_inputDBS - 0
useParent-check.sh 240423_160424:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240423_160426:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240423_160428:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240423_160431:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240423_160434:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240423_160436:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240423_160438:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240423_160440:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240423_160442:cmsbot_crab_whitelist - 0
blacklist-check.sh 240423_160444:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240423_160446:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240423_160448:cmsbot_crab_voRole - 0
voGroup-check.sh 240423_160450:cmsbot_crab_voGroup - 0
scheddName-check.sh 240423_160452:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240423_160456:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240423_160402:cmsbot_crab_outputFiles - 1
collector-check.sh 240423_160454:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-23T17:34:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-04-23 19:34:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/875/console

```
{'TN': '240423_160459:cmsbot_crab_20240423_180458', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 995, 'failed': 5}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240423_160501:cmsbot_crab_20240423_180501', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160503:cmsbot_crab_20240423_180503', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240423_160506:cmsbot_crab_20240423_180505', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240423_160508:cmsbot_crab_20240423_180507', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240423_160533:cmsbot_crab_20240423_180510', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240423_160536:cmsbot_crab_rucio_transfers_20240423_180535', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/37'}
{'TN': '240423_160539:cmsbot_crab_rucio_transfers_group_20240423_180538', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/35'}
{'TN': '240423_160542:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240423_180540', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160545:cmsbot_crab_rucio_transfers_nopublication_20240423_180543', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160548:cmsbot_crab_rucio_transfers_withnoneedm_20240423_180547', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/35'}
{'TN': '240423_160551:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240423_180550', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-23T19:06:27Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-04-23 21:06:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/876/console

```
{'TN': '240423_160459:cmsbot_crab_20240423_180458', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/995/995'}
{'TN': '240423_160501:cmsbot_crab_20240423_180501', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160503:cmsbot_crab_20240423_180503', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240423_160506:cmsbot_crab_20240423_180505', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240423_160508:cmsbot_crab_20240423_180507', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240423_160533:cmsbot_crab_20240423_180510', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240423_160536:cmsbot_crab_rucio_transfers_20240423_180535', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/37'}
{'TN': '240423_160539:cmsbot_crab_rucio_transfers_group_20240423_180538', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/35'}
{'TN': '240423_160542:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240423_180540', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160545:cmsbot_crab_rucio_transfers_nopublication_20240423_180543', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240423_160548:cmsbot_crab_rucio_transfers_withnoneedm_20240423_180547', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/35'}
{'TN': '240423_160551:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240423_180550', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (novicecpp, 2024-04-24T15:02:04Z)

Validating new [v3.240423](https://github.com/dmwm/CRABServer/releases/tag/v3.240423).
Well, so far so good (see fail reasons of CCV tasks in [MM](https://mattermost.web.cern.ch/cms-o-and-c/pl/mui3f9fhafga5rnrxc84x6dzic))
