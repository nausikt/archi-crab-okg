# dmwm/CRABServer issue #8611: #829: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-12T14:42:16Z
Closed: 2024-10-10T22:43:00Z
URL: https://github.com/dmwm/CRABServer/issues/8611

## Opening post (cmsdmwmbot, 2024-08-12T14:42:16Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-08-12 16:42:15
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/829/)

## Comment (cmsdmwmbot, 2024-08-12T14:45:03Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240812_144405:cmsbot_crab_20240812_164405
240812_144407:cmsbot_crab_20240812_164407
240812_144412:cmsbot_crab_20240812_164409
240812_144419:cmsbot_crab_20240812_164414
240812_144421:cmsbot_crab_20240812_164420
240812_144425:cmsbot_crab_20240812_164423
240812_144428:cmsbot_crab_rucio_transfers_20240812_164427
240812_144430:cmsbot_crab_rucio_transfers_group_20240812_164430
240812_144433:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240812_164432
240812_144436:cmsbot_crab_rucio_transfers_nopublication_20240812_164435
240812_144439:cmsbot_crab_rucio_transfers_withnoneedm_20240812_164437
240812_144441:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240812_164440
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240812_144239:cmsbot_crab_transferOutputs
240812_144242:cmsbot_crab_transferLogs
240812_144251:cmsbot_crab_activity
240812_144254:cmsbot_crab_inputFiles
240812_144256:cmsbot_crab_disableAutomaticOutputCollection
240812_144258:cmsbot_crab_outputFiles
240812_144300:cmsbot_crab_allowUndistributedCMSSW
240812_144302:cmsbot_crab_maxMemoryMB
240812_144304:cmsbot_crab_maxJobRuntimeMin
240812_144307:cmsbot_crab_numCores
240812_144309:cmsbot_crab_scriptExe
240812_144312:cmsbot_crab_scriptArgs
240812_144314:cmsbot_crab_sendVenvFolder
240812_144316:cmsbot_crab_sendExternalFolder
240812_144319:cmsbot_crab_inputDBS
240812_144321:cmsbot_crab_useParent
240812_144323:cmsbot_crab_secondaryInputDataset
240812_144325:cmsbot_crab_lumiMaskFile
240812_144327:cmsbot_crab_lumiMaskUrl
240812_144330:cmsbot_crab_outLFNDirBase
240812_144332:cmsbot_crab_runRange
240812_144334:cmsbot_crab_ignoreLocality
240812_144336:cmsbot_crab_userInputFiles
240812_144338:cmsbot_crab_whitelist
240812_144340:cmsbot_crab_blacklist
240812_144345:cmsbot_crab_ignoreGlobalBlacklist
240812_144352:cmsbot_crab_voRole
240812_144354:cmsbot_crab_voGroup
240812_144356:cmsbot_crab_scheddName
240812_144359:cmsbot_crab_collector
240812_144402:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240812_144237:cmsbot_crab_20240812_164235
```

Finished at: 2024-08-12 16:44:42
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/829/console)

## Comment (cmsdmwmbot, 2024-08-12T15:05:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-12 17:05:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1077/console

```
{'TN': '240812_144405:cmsbot_crab_20240812_164405', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 990, 'running': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144407:cmsbot_crab_20240812_164407', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144412:cmsbot_crab_20240812_164409', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144419:cmsbot_crab_20240812_164414', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144421:cmsbot_crab_20240812_164420', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144425:cmsbot_crab_20240812_164423', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144428:cmsbot_crab_rucio_transfers_20240812_164427', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144430:cmsbot_crab_rucio_transfers_group_20240812_164430', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144433:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240812_164432', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144436:cmsbot_crab_rucio_transfers_nopublication_20240812_164435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144439:cmsbot_crab_rucio_transfers_withnoneedm_20240812_164437', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144441:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240812_164440', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-12T15:08:30Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-08-12 17:08:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/545/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/545//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-08-12T15:09:44Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-12 17:09:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1161/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240812_144304:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskFile-check.sh 240812_144325:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240812_144327:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240812_144330:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240812_144332:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240812_144336:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240812_144338:cmsbot_crab_whitelist - 2
blacklist-check.sh 240812_144340:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240812_144345:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240812_144352:cmsbot_crab_voRole - 2
voGroup-check.sh 240812_144354:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240812_144239:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240812_144242:cmsbot_crab_transferLogs - 0
activity-check.sh 240812_144251:cmsbot_crab_activity - 0
inputFiles-check.sh 240812_144254:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240812_144256:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240812_144258:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240812_144300:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240812_144302:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 240812_144307:cmsbot_crab_numCores - 0
scriptExe-check.sh 240812_144309:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240812_144312:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240812_144314:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240812_144316:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240812_144319:cmsbot_crab_inputDBS - 0
useParent-check.sh 240812_144321:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240812_144323:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240812_144334:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 240812_144356:cmsbot_crab_scheddName - 0
collector-check.sh 240812_144359:cmsbot_crab_collector - 0
extraJDL-check.sh 240812_144402:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-12T15:21:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-08-12 17:21:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1078/console

```
{'TN': '240812_144405:cmsbot_crab_20240812_164405', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144407:cmsbot_crab_20240812_164407', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144412:cmsbot_crab_20240812_164409', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144419:cmsbot_crab_20240812_164414', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144421:cmsbot_crab_20240812_164420', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144425:cmsbot_crab_20240812_164423', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144428:cmsbot_crab_rucio_transfers_20240812_164427', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144430:cmsbot_crab_rucio_transfers_group_20240812_164430', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144433:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240812_164432', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144436:cmsbot_crab_rucio_transfers_nopublication_20240812_164435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144439:cmsbot_crab_rucio_transfers_withnoneedm_20240812_164437', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144441:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240812_164440', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-12T15:33:46Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-08-12 17:33:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1162/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240812_144239:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240812_144242:cmsbot_crab_transferLogs - 0
activity-check.sh 240812_144251:cmsbot_crab_activity - 0
inputFiles-check.sh 240812_144254:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240812_144256:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240812_144258:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240812_144300:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240812_144302:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240812_144304:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240812_144307:cmsbot_crab_numCores - 0
scriptExe-check.sh 240812_144309:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240812_144312:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240812_144314:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240812_144316:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240812_144319:cmsbot_crab_inputDBS - 0
useParent-check.sh 240812_144321:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240812_144323:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240812_144325:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240812_144327:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240812_144330:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240812_144332:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240812_144334:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240812_144336:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240812_144338:cmsbot_crab_whitelist - 0
blacklist-check.sh 240812_144340:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240812_144345:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240812_144352:cmsbot_crab_voRole - 0
voGroup-check.sh 240812_144354:cmsbot_crab_voGroup - 0
scheddName-check.sh 240812_144356:cmsbot_crab_scheddName - 0
collector-check.sh 240812_144359:cmsbot_crab_collector - 0
extraJDL-check.sh 240812_144402:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-12T16:10:55Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-08-12 18:10:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1079/console

```
{'TN': '240812_144405:cmsbot_crab_20240812_164405', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 871, 'transferring': 129}, 'publication (fail/tdb/DBS)': '0/870/870'}
{'TN': '240812_144407:cmsbot_crab_20240812_164407', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144412:cmsbot_crab_20240812_164409', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240812_144419:cmsbot_crab_20240812_164414', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240812_144421:cmsbot_crab_20240812_164420', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/99/99'}
{'TN': '240812_144425:cmsbot_crab_20240812_164423', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240812_144428:cmsbot_crab_rucio_transfers_20240812_164427', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240812_144430:cmsbot_crab_rucio_transfers_group_20240812_164430', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 36, 'transferring': 4}, 'publication (fail/tdb/DBS)': '0/36/36'}
{'TN': '240812_144433:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240812_164432', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 32, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144436:cmsbot_crab_rucio_transfers_nopublication_20240812_164435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144439:cmsbot_crab_rucio_transfers_withnoneedm_20240812_164437', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '240812_144441:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240812_164440', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-12T17:42:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-08-12 19:42:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1080/console

```
{'TN': '240812_144405:cmsbot_crab_20240812_164405', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 981, 'transferring': 18, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/973/973'}
{'TN': '240812_144407:cmsbot_crab_20240812_164407', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240812_144412:cmsbot_crab_20240812_164409', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240812_144419:cmsbot_crab_20240812_164414', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240812_144421:cmsbot_crab_20240812_164420', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240812_144425:cmsbot_crab_20240812_164423', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240812_144428:cmsbot_crab_rucio_transfers_20240812_164427', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240812_144430:cmsbot_crab_rucio_transfers_group_20240812_164430', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '240812_144433:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240812_164432', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 32, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144436:cmsbot_crab_rucio_transfers_nopublication_20240812_164435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144439:cmsbot_crab_rucio_transfers_withnoneedm_20240812_164437', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '240812_144441:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240812_164440', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-12T19:45:01Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-08-12 21:45:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1081/console

```
{'TN': '240812_144405:cmsbot_crab_20240812_164405', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 997, 'failed': 2, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/997/997'}
{'TN': '240812_144407:cmsbot_crab_20240812_164407', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240812_144412:cmsbot_crab_20240812_164409', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240812_144419:cmsbot_crab_20240812_164414', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240812_144421:cmsbot_crab_20240812_164420', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240812_144425:cmsbot_crab_20240812_164423', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240812_144428:cmsbot_crab_rucio_transfers_20240812_164427', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240812_144430:cmsbot_crab_rucio_transfers_group_20240812_164430', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '240812_144433:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240812_164432', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 32, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144436:cmsbot_crab_rucio_transfers_nopublication_20240812_164435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144439:cmsbot_crab_rucio_transfers_withnoneedm_20240812_164437', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240812_144441:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240812_164440', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-12T21:47:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-08-12 23:47:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1082/console

```
{'TN': '240812_144405:cmsbot_crab_20240812_164405', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240812_144407:cmsbot_crab_20240812_164407', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240812_144412:cmsbot_crab_20240812_164409', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240812_144419:cmsbot_crab_20240812_164414', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240812_144421:cmsbot_crab_20240812_164420', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240812_144425:cmsbot_crab_20240812_164423', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240812_144428:cmsbot_crab_rucio_transfers_20240812_164427', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240812_144430:cmsbot_crab_rucio_transfers_group_20240812_164430', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240812_144433:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240812_164432', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 32, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144436:cmsbot_crab_rucio_transfers_nopublication_20240812_164435', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240812_144439:cmsbot_crab_rucio_transfers_withnoneedm_20240812_164437', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240812_144441:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240812_164440', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
