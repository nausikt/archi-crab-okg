# dmwm/CRABServer issue #8301: #734: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-20T21:02:16Z
Closed: 2024-03-21T09:23:37Z
URL: https://github.com/dmwm/CRABServer/issues/8301

## Opening post (cmsdmwmbot, 2024-03-20T21:02:16Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-03-20 22:02:15
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/734/)

## Comment (cmsdmwmbot, 2024-03-20T21:05:17Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240320_210425:cmsbot_crab_20240320_220424
240320_210427:cmsbot_crab_20240320_220426
240320_210429:cmsbot_crab_20240320_220429
240320_210431:cmsbot_crab_20240320_220431
240320_210433:cmsbot_crab_20240320_220433
240320_210437:cmsbot_crab_20240320_220435
240320_210440:cmsbot_crab_rucio_transfers_20240320_220438
240320_210442:cmsbot_crab_rucio_transfers_group_20240320_220442
240320_210446:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240320_220444
240320_210449:cmsbot_crab_rucio_transfers_nopublication_20240320_220448
240320_210452:cmsbot_crab_rucio_transfers_withnoneedm_20240320_220451
240320_210455:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240320_220454
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240320_210237:cmsbot_crab_transferOutputs
240320_210239:cmsbot_crab_transferLogs
240320_210241:cmsbot_crab_activity
240320_210243:cmsbot_crab_inputFiles
240320_210245:cmsbot_crab_disableAutomaticOutputCollection
240320_210248:cmsbot_crab_outputFiles
240320_210250:cmsbot_crab_allowUndistributedCMSSW
240320_210252:cmsbot_crab_maxMemoryMB
240320_210254:cmsbot_crab_maxJobRuntimeMin
240320_210256:cmsbot_crab_numCores
240320_210258:cmsbot_crab_scriptExe
240320_210300:cmsbot_crab_scriptArgs
240320_210302:cmsbot_crab_sendVenvFolder
240320_210345:cmsbot_crab_sendExternalFolder
240320_210347:cmsbot_crab_inputDBS
240320_210349:cmsbot_crab_useParent
240320_210351:cmsbot_crab_secondaryInputDataset
240320_210354:cmsbot_crab_lumiMaskFile
240320_210356:cmsbot_crab_lumiMaskUrl
240320_210359:cmsbot_crab_outLFNDirBase
240320_210401:cmsbot_crab_runRange
240320_210403:cmsbot_crab_ignoreLocality
240320_210405:cmsbot_crab_userInputFiles
240320_210407:cmsbot_crab_whitelist
240320_210409:cmsbot_crab_blacklist
240320_210411:cmsbot_crab_ignoreGlobalBlacklist
240320_210413:cmsbot_crab_voRole
240320_210415:cmsbot_crab_voGroup
240320_210417:cmsbot_crab_scheddName
240320_210420:cmsbot_crab_collector
240320_210422:cmsbot_crab_extraJDL
```

Finished at: 2024-03-20 22:04:56
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/734/console)

## Comment (cmsdmwmbot, 2024-03-20T21:27:04Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-20 22:27:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/828/console

```
{'TN': '240320_210425:cmsbot_crab_20240320_220424', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 995, 'running': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210427:cmsbot_crab_20240320_220426', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210429:cmsbot_crab_20240320_220429', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210431:cmsbot_crab_20240320_220431', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210433:cmsbot_crab_20240320_220433', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210437:cmsbot_crab_20240320_220435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210440:cmsbot_crab_rucio_transfers_20240320_220438', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210442:cmsbot_crab_rucio_transfers_group_20240320_220442', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210446:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240320_220444', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210449:cmsbot_crab_rucio_transfers_nopublication_20240320_220448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210452:cmsbot_crab_rucio_transfers_withnoneedm_20240320_220451', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210455:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240320_220454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 3, 'transferring': 37}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-20T21:30:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-20 22:30:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/982/console

```
RETRY TESTS:
transferLogs-check.sh 240320_210239:cmsbot_crab_transferLogs - 2
activity-check.sh 240320_210241:cmsbot_crab_activity - 2
numCores-check.sh 240320_210256:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240320_210300:cmsbot_crab_scriptArgs - 2
secondaryInputDataset-check.sh 240320_210351:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240320_210354:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240320_210356:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240320_210359:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240320_210401:cmsbot_crab_runRange - 2
whitelist-check.sh 240320_210407:cmsbot_crab_whitelist - 2
blacklist-check.sh 240320_210409:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240320_210237:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240320_210243:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240320_210245:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240320_210248:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240320_210250:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240320_210252:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240320_210254:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240320_210258:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240320_210302:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240320_210345:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240320_210347:cmsbot_crab_inputDBS - 0
useParent-check.sh 240320_210349:cmsbot_crab_useParent - 0
ignoreLocality-check.sh 240320_210403:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240320_210405:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240320_210411:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240320_210413:cmsbot_crab_voRole - 0
voGroup-check.sh 240320_210415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240320_210417:cmsbot_crab_scheddName - 0
collector-check.sh 240320_210420:cmsbot_crab_collector - 0
extraJDL-check.sh 240320_210422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-20T21:45:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-20 22:45:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/829/console

```
{'TN': '240320_210425:cmsbot_crab_20240320_220424', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210427:cmsbot_crab_20240320_220426', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210429:cmsbot_crab_20240320_220429', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210431:cmsbot_crab_20240320_220431', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210433:cmsbot_crab_20240320_220433', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 41, 'transferring': 58, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210437:cmsbot_crab_20240320_220435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210440:cmsbot_crab_rucio_transfers_20240320_220438', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 21, 'transferring': 19}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210442:cmsbot_crab_rucio_transfers_group_20240320_220442', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210446:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240320_220444', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210449:cmsbot_crab_rucio_transfers_nopublication_20240320_220448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210452:cmsbot_crab_rucio_transfers_withnoneedm_20240320_220451', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210455:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240320_220454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-20T21:55:06Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-03-20 22:55:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/983/console

```
RETRY TESTS:
numCores-check.sh 240320_210256:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240320_210300:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240320_210356:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240320_210359:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240320_210401:cmsbot_crab_runRange - 2
whitelist-check.sh 240320_210407:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240320_210237:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240320_210239:cmsbot_crab_transferLogs - 0
activity-check.sh 240320_210241:cmsbot_crab_activity - 0
inputFiles-check.sh 240320_210243:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240320_210245:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240320_210248:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240320_210250:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240320_210252:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240320_210254:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240320_210258:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240320_210302:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240320_210345:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240320_210347:cmsbot_crab_inputDBS - 0
useParent-check.sh 240320_210349:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240320_210351:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240320_210354:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240320_210403:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240320_210405:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240320_210409:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240320_210411:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240320_210413:cmsbot_crab_voRole - 0
voGroup-check.sh 240320_210415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240320_210417:cmsbot_crab_scheddName - 0
collector-check.sh 240320_210420:cmsbot_crab_collector - 0
extraJDL-check.sh 240320_210422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-20T22:19:56Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-03-20 23:19:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/984/console

```
RETRY TESTS:
numCores-check.sh 240320_210256:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240320_210300:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240320_210356:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240320_210359:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240320_210401:cmsbot_crab_runRange - 2
whitelist-check.sh 240320_210407:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240320_210237:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240320_210239:cmsbot_crab_transferLogs - 0
activity-check.sh 240320_210241:cmsbot_crab_activity - 0
inputFiles-check.sh 240320_210243:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240320_210245:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240320_210248:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240320_210250:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240320_210252:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240320_210254:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240320_210258:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240320_210302:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240320_210345:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240320_210347:cmsbot_crab_inputDBS - 0
useParent-check.sh 240320_210349:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240320_210351:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240320_210354:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240320_210403:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240320_210405:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240320_210409:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240320_210411:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240320_210413:cmsbot_crab_voRole - 0
voGroup-check.sh 240320_210415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240320_210417:cmsbot_crab_scheddName - 0
collector-check.sh 240320_210420:cmsbot_crab_collector - 0
extraJDL-check.sh 240320_210422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-20T22:32:06Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-20 23:32:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/830/console

```
{'TN': '240320_210425:cmsbot_crab_20240320_220424', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 408, 'transferring': 591, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/400/400'}
{'TN': '240320_210427:cmsbot_crab_20240320_220426', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210429:cmsbot_crab_20240320_220429', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240320_210431:cmsbot_crab_20240320_220431', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240320_210433:cmsbot_crab_20240320_220433', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 43, 'transferring': 56, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/43/43'}
{'TN': '240320_210437:cmsbot_crab_20240320_220435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 7, 'finished': 3}, 'publication (fail/tdb/DBS)': '0/2/2'}
{'TN': '240320_210440:cmsbot_crab_rucio_transfers_20240320_220438', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 21, 'transferring': 19}, 'publication (fail/tdb/DBS)': '0/21/21'}
{'TN': '240320_210442:cmsbot_crab_rucio_transfers_group_20240320_220442', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '9/31/31'}
{'TN': '240320_210446:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240320_220444', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 22, 'finished': 18}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210449:cmsbot_crab_rucio_transfers_nopublication_20240320_220448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 30, 'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210452:cmsbot_crab_rucio_transfers_withnoneedm_20240320_220451', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 23, 'finished': 17}, 'publication (fail/tdb/DBS)': '0/13/10'}
{'TN': '240320_210455:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240320_220454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 19, 'finished': 21}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-20T22:43:58Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2024-03-20 23:43:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/985/console

```
RETRY TESTS:
numCores-check.sh 240320_210256:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240320_210300:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240320_210356:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240320_210401:cmsbot_crab_runRange - 2
whitelist-check.sh 240320_210407:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240320_210237:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240320_210239:cmsbot_crab_transferLogs - 0
activity-check.sh 240320_210241:cmsbot_crab_activity - 0
inputFiles-check.sh 240320_210243:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240320_210245:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240320_210248:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240320_210250:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240320_210252:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240320_210254:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240320_210258:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240320_210302:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240320_210345:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240320_210347:cmsbot_crab_inputDBS - 0
useParent-check.sh 240320_210349:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240320_210351:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240320_210354:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240320_210359:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240320_210403:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240320_210405:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240320_210409:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240320_210411:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240320_210413:cmsbot_crab_voRole - 0
voGroup-check.sh 240320_210415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240320_210417:cmsbot_crab_scheddName - 0
collector-check.sh 240320_210420:cmsbot_crab_collector - 0
extraJDL-check.sh 240320_210422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-20T23:09:08Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-03-21 00:09:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/986/console

```
RETRY TESTS:
scriptArgs-check.sh 240320_210300:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240320_210356:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240320_210401:cmsbot_crab_runRange - 2
whitelist-check.sh 240320_210407:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240320_210237:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240320_210239:cmsbot_crab_transferLogs - 0
activity-check.sh 240320_210241:cmsbot_crab_activity - 0
inputFiles-check.sh 240320_210243:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240320_210245:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240320_210248:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240320_210250:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240320_210252:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240320_210254:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240320_210256:cmsbot_crab_numCores - 0
scriptExe-check.sh 240320_210258:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240320_210302:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240320_210345:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240320_210347:cmsbot_crab_inputDBS - 0
useParent-check.sh 240320_210349:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240320_210351:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240320_210354:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240320_210359:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240320_210403:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240320_210405:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240320_210409:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240320_210411:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240320_210413:cmsbot_crab_voRole - 0
voGroup-check.sh 240320_210415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240320_210417:cmsbot_crab_scheddName - 0
collector-check.sh 240320_210420:cmsbot_crab_collector - 0
extraJDL-check.sh 240320_210422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-20T23:22:06Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 0. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-03-21 00:22:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/987/console

```
RETRY TESTS:
scriptArgs-check.sh 240320_210300:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240320_210356:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240320_210401:cmsbot_crab_runRange - 2
whitelist-check.sh 240320_210407:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240320_210237:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240320_210239:cmsbot_crab_transferLogs - 0
activity-check.sh 240320_210241:cmsbot_crab_activity - 0
inputFiles-check.sh 240320_210243:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240320_210245:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240320_210248:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240320_210250:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240320_210252:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240320_210254:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240320_210256:cmsbot_crab_numCores - 0
scriptExe-check.sh 240320_210258:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240320_210302:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240320_210345:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240320_210347:cmsbot_crab_inputDBS - 0
useParent-check.sh 240320_210349:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240320_210351:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240320_210354:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240320_210359:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240320_210403:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240320_210405:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 240320_210409:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240320_210411:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240320_210413:cmsbot_crab_voRole - 0
voGroup-check.sh 240320_210415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240320_210417:cmsbot_crab_scheddName - 0
collector-check.sh 240320_210420:cmsbot_crab_collector - 0
extraJDL-check.sh 240320_210422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-21T00:04:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-03-21 01:04:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/831/console

```
{'TN': '240320_210425:cmsbot_crab_20240320_220424', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 463, 'transferring': 537}, 'publication (fail/tdb/DBS)': '0/443/443'}
{'TN': '240320_210427:cmsbot_crab_20240320_220426', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210429:cmsbot_crab_20240320_220429', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240320_210431:cmsbot_crab_20240320_220431', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 8, 'finished': 2}, 'publication (fail/tdb/DBS)': '0/2/2'}
{'TN': '240320_210433:cmsbot_crab_20240320_220433', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 53, 'transferring': 47}, 'publication (fail/tdb/DBS)': '0/53/53'}
{'TN': '240320_210437:cmsbot_crab_20240320_220435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/7/7'}
{'TN': '240320_210440:cmsbot_crab_rucio_transfers_20240320_220438', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 26, 'transferring': 14}, 'publication (fail/tdb/DBS)': '0/26/26'}
{'TN': '240320_210442:cmsbot_crab_rucio_transfers_group_20240320_220442', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '9/31/31'}
{'TN': '240320_210446:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240320_220444', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 21, 'finished': 19}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210449:cmsbot_crab_rucio_transfers_nopublication_20240320_220448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 26, 'finished': 14}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210452:cmsbot_crab_rucio_transfers_withnoneedm_20240320_220451', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 23, 'finished': 17}, 'publication (fail/tdb/DBS)': '2/15/12'}
{'TN': '240320_210455:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240320_220454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 25, 'transferring': 15}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-21T02:06:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-03-21 03:05:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/832/console

```
{'TN': '240320_210425:cmsbot_crab_20240320_220424', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 942, 'transferring': 58}, 'publication (fail/tdb/DBS)': '0/843/843'}
{'TN': '240320_210427:cmsbot_crab_20240320_220426', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210429:cmsbot_crab_20240320_220429', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240320_210431:cmsbot_crab_20240320_220431', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240320_210433:cmsbot_crab_20240320_220433', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 97, 'transferring': 2, 'running': 1}, 'publication (fail/tdb/DBS)': '0/97/97'}
{'TN': '240320_210437:cmsbot_crab_20240320_220435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240320_210440:cmsbot_crab_rucio_transfers_20240320_220438', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240320_210442:cmsbot_crab_rucio_transfers_group_20240320_220442', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '9/31/31'}
{'TN': '240320_210446:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240320_220444', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210449:cmsbot_crab_rucio_transfers_nopublication_20240320_220448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210452:cmsbot_crab_rucio_transfers_withnoneedm_20240320_220451', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '6/25/22'}
{'TN': '240320_210455:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240320_220454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-21T04:09:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-03-21 05:09:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/833/console

```
{'TN': '240320_210425:cmsbot_crab_20240320_220424', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 967, 'transferring': 33}, 'publication (fail/tdb/DBS)': '0/967/967'}
{'TN': '240320_210427:cmsbot_crab_20240320_220426', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210429:cmsbot_crab_20240320_220429', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240320_210431:cmsbot_crab_20240320_220431', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240320_210433:cmsbot_crab_20240320_220433', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240320_210437:cmsbot_crab_20240320_220435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240320_210440:cmsbot_crab_rucio_transfers_20240320_220438', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240320_210442:cmsbot_crab_rucio_transfers_group_20240320_220442', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '9/31/31'}
{'TN': '240320_210446:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240320_220444', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210449:cmsbot_crab_rucio_transfers_nopublication_20240320_220448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210452:cmsbot_crab_rucio_transfers_withnoneedm_20240320_220451', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '12/28/25'}
{'TN': '240320_210455:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240320_220454', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-21T09:10:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 0. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-03-21 10:10:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/834/console

```
{'TN': '240320_210425:cmsbot_crab_20240320_220424', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 974, 'transferring': 26}, 'publication (fail/tdb/DBS)': '0/974/0'}
{'TN': '240320_210427:cmsbot_crab_20240320_220426', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210429:cmsbot_crab_20240320_220429', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/0'}
{'TN': '240320_210431:cmsbot_crab_20240320_220431', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/0'}
{'TN': '240320_210433:cmsbot_crab_20240320_220433', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/0'}
{'TN': '240320_210437:cmsbot_crab_20240320_220435', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/0'}
{'TN': '240320_210440:cmsbot_crab_rucio_transfers_20240320_220438', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/0'}
{'TN': '240320_210442:cmsbot_crab_rucio_transfers_group_20240320_220442', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '9/31/0'}
{'TN': '240320_210446:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240320_220444', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210449:cmsbot_crab_rucio_transfers_nopublication_20240320_220448', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240320_210452:cmsbot_crab_rucio_transfers_withnoneedm_20240320_220451', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '12/28/0'}
{'TN': '240320_210455:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240320_220454', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-21T09:12:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 0. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-03-21 10:12:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/988/console

```
RETRY TESTS:
scriptArgs-check.sh 240320_210300:cmsbot_crab_scriptArgs - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240320_210237:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240320_210239:cmsbot_crab_transferLogs - 0
activity-check.sh 240320_210241:cmsbot_crab_activity - 0
inputFiles-check.sh 240320_210243:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240320_210245:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240320_210248:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240320_210250:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240320_210252:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240320_210254:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240320_210256:cmsbot_crab_numCores - 0
scriptExe-check.sh 240320_210258:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240320_210302:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240320_210345:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240320_210347:cmsbot_crab_inputDBS - 0
useParent-check.sh 240320_210349:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240320_210351:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240320_210354:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240320_210356:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240320_210359:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240320_210401:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240320_210403:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240320_210405:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240320_210407:cmsbot_crab_whitelist - 0
blacklist-check.sh 240320_210409:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240320_210411:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240320_210413:cmsbot_crab_voRole - 0
voGroup-check.sh 240320_210415:cmsbot_crab_voGroup - 0
scheddName-check.sh 240320_210417:cmsbot_crab_scheddName - 0
collector-check.sh 240320_210420:cmsbot_crab_collector - 0
extraJDL-check.sh 240320_210422:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-03-21T09:23:37Z)

jobs ran OK. But stage out from Vanderbilt to CERN has a large queue.
