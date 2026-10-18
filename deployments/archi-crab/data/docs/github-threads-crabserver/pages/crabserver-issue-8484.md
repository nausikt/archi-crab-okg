# dmwm/CRABServer issue #8484: #800: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-10T18:32:02Z
Closed: 2024-06-11T09:39:14Z
URL: https://github.com/dmwm/CRABServer/issues/8484

## Opening post (cmsdmwmbot, 2024-06-10T18:32:02Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-06-10 20:32:01
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/800/)

## Comment (belforte, 2024-06-10T18:33:10Z)

use this to test latest [Modernize_HTC branch](https://github.com/belforte/CRABServer/tree/modernize_HTC) on crab-dev-tw01

## Comment (cmsdmwmbot, 2024-06-10T18:34:23Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240610_183332:cmsbot_crab_20240610_203331
240610_183334:cmsbot_crab_20240610_203333
240610_183336:cmsbot_crab_20240610_203336
240610_183338:cmsbot_crab_20240610_203338
240610_183340:cmsbot_crab_20240610_203340
240610_183344:cmsbot_crab_20240610_203342
240610_183347:cmsbot_crab_rucio_transfers_20240610_203346
240610_183349:cmsbot_crab_rucio_transfers_group_20240610_203349
240610_183353:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240610_203351
240610_183356:cmsbot_crab_rucio_transfers_nopublication_20240610_203354
240610_183359:cmsbot_crab_rucio_transfers_withnoneedm_20240610_203357
240610_183402:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240610_203400
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240610_183223:cmsbot_crab_transferOutputs
240610_183225:cmsbot_crab_transferLogs
240610_183227:cmsbot_crab_activity
240610_183229:cmsbot_crab_inputFiles
240610_183231:cmsbot_crab_disableAutomaticOutputCollection
240610_183234:cmsbot_crab_outputFiles
240610_183236:cmsbot_crab_allowUndistributedCMSSW
240610_183238:cmsbot_crab_maxMemoryMB
240610_183240:cmsbot_crab_maxJobRuntimeMin
240610_183243:cmsbot_crab_numCores
240610_183245:cmsbot_crab_scriptExe
240610_183247:cmsbot_crab_scriptArgs
240610_183250:cmsbot_crab_sendVenvFolder
240610_183252:cmsbot_crab_sendExternalFolder
240610_183254:cmsbot_crab_inputDBS
240610_183256:cmsbot_crab_useParent
240610_183258:cmsbot_crab_secondaryInputDataset
240610_183300:cmsbot_crab_lumiMaskFile
240610_183303:cmsbot_crab_lumiMaskUrl
240610_183306:cmsbot_crab_outLFNDirBase
240610_183308:cmsbot_crab_runRange
240610_183310:cmsbot_crab_ignoreLocality
240610_183312:cmsbot_crab_userInputFiles
240610_183314:cmsbot_crab_whitelist
240610_183316:cmsbot_crab_blacklist
240610_183318:cmsbot_crab_ignoreGlobalBlacklist
240610_183320:cmsbot_crab_voRole
240610_183323:cmsbot_crab_voGroup
240610_183325:cmsbot_crab_scheddName
240610_183327:cmsbot_crab_collector
240610_183329:cmsbot_crab_extraJDL
```

Finished at: 2024-06-10 20:34:02
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/800/console)

## Comment (cmsdmwmbot, 2024-06-10T18:56:49Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-10 20:56:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/984/console

```
{'TN': '240610_183332:cmsbot_crab_20240610_203331', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 996, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183334:cmsbot_crab_20240610_203333', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183336:cmsbot_crab_20240610_203336', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183338:cmsbot_crab_20240610_203338', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183340:cmsbot_crab_20240610_203340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183344:cmsbot_crab_20240610_203342', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183347:cmsbot_crab_rucio_transfers_20240610_203346', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183349:cmsbot_crab_rucio_transfers_group_20240610_203349', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183353:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240610_203351', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183356:cmsbot_crab_rucio_transfers_nopublication_20240610_203354', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183359:cmsbot_crab_rucio_transfers_withnoneedm_20240610_203357', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183402:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240610_203400', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-10T19:00:22Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-10 21:00:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1107/console

```
RETRY TESTS:
scriptExe-check.sh 240610_183245:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240610_183303:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240610_183308:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240610_183312:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240610_183314:cmsbot_crab_whitelist - 2
blacklist-check.sh 240610_183316:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240610_183223:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240610_183225:cmsbot_crab_transferLogs - 0
activity-check.sh 240610_183227:cmsbot_crab_activity - 0
inputFiles-check.sh 240610_183229:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240610_183231:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240610_183234:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240610_183236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240610_183238:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240610_183240:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 240610_183247:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240610_183250:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240610_183252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240610_183254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240610_183256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240610_183258:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240610_183300:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240610_183306:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240610_183310:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240610_183318:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240610_183320:cmsbot_crab_voRole - 0
voGroup-check.sh 240610_183323:cmsbot_crab_voGroup - 0
scheddName-check.sh 240610_183325:cmsbot_crab_scheddName - 0
collector-check.sh 240610_183327:cmsbot_crab_collector - 0
extraJDL-check.sh 240610_183329:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 240610_183243:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-06-10T19:14:48Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-10 21:14:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/985/console

```
{'TN': '240610_183332:cmsbot_crab_20240610_203331', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 996, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183334:cmsbot_crab_20240610_203333', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183336:cmsbot_crab_20240610_203336', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183338:cmsbot_crab_20240610_203338', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183340:cmsbot_crab_20240610_203340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183344:cmsbot_crab_20240610_203342', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183347:cmsbot_crab_rucio_transfers_20240610_203346', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183349:cmsbot_crab_rucio_transfers_group_20240610_203349', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183353:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240610_203351', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183356:cmsbot_crab_rucio_transfers_nopublication_20240610_203354', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183359:cmsbot_crab_rucio_transfers_withnoneedm_20240610_203357', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183402:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240610_203400', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-10T19:24:37Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-06-10 21:24:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1108/console

```
RETRY TESTS:
blacklist-check.sh 240610_183316:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240610_183223:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240610_183225:cmsbot_crab_transferLogs - 0
activity-check.sh 240610_183227:cmsbot_crab_activity - 0
inputFiles-check.sh 240610_183229:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240610_183231:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240610_183234:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240610_183236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240610_183238:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240610_183240:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240610_183245:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240610_183247:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240610_183250:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240610_183252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240610_183254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240610_183256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240610_183258:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240610_183300:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240610_183303:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240610_183306:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240610_183308:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240610_183310:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240610_183312:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240610_183314:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240610_183318:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240610_183320:cmsbot_crab_voRole - 0
voGroup-check.sh 240610_183323:cmsbot_crab_voGroup - 0
scheddName-check.sh 240610_183325:cmsbot_crab_scheddName - 0
collector-check.sh 240610_183327:cmsbot_crab_collector - 0
extraJDL-check.sh 240610_183329:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 240610_183243:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-06-10T19:48:41Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-10 21:48:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1109/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240610_183223:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240610_183225:cmsbot_crab_transferLogs - 0
activity-check.sh 240610_183227:cmsbot_crab_activity - 0
inputFiles-check.sh 240610_183229:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240610_183231:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240610_183234:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240610_183236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240610_183238:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240610_183240:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240610_183245:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240610_183247:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240610_183250:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240610_183252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240610_183254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240610_183256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240610_183258:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240610_183300:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240610_183303:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240610_183306:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240610_183308:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240610_183310:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240610_183312:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240610_183314:cmsbot_crab_whitelist - 0
blacklist-check.sh 240610_183316:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240610_183318:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240610_183320:cmsbot_crab_voRole - 0
voGroup-check.sh 240610_183323:cmsbot_crab_voGroup - 0
scheddName-check.sh 240610_183325:cmsbot_crab_scheddName - 0
collector-check.sh 240610_183327:cmsbot_crab_collector - 0
extraJDL-check.sh 240610_183329:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 240610_183243:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2024-06-10T20:01:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-10 22:01:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/986/console

```
{'TN': '240610_183332:cmsbot_crab_20240610_203331', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 996, 'failed': 4}, 'publication (fail/tdb/DBS)': '0/996/996'}
{'TN': '240610_183334:cmsbot_crab_20240610_203333', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240610_183336:cmsbot_crab_20240610_203336', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240610_183338:cmsbot_crab_20240610_203338', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240610_183340:cmsbot_crab_20240610_203340', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240610_183344:cmsbot_crab_20240610_203342', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240610_183347:cmsbot_crab_rucio_transfers_20240610_203346', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240610_183349:cmsbot_crab_rucio_transfers_group_20240610_203349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240610_183353:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240610_203351', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183356:cmsbot_crab_rucio_transfers_nopublication_20240610_203354', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183359:cmsbot_crab_rucio_transfers_withnoneedm_20240610_203357', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240610_183402:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240610_203400', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-10T21:34:52Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-06-10 23:34:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/987/console

```
{'TN': '240610_183332:cmsbot_crab_20240610_203331', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240610_183334:cmsbot_crab_20240610_203333', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240610_183336:cmsbot_crab_20240610_203336', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240610_183338:cmsbot_crab_20240610_203338', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240610_183340:cmsbot_crab_20240610_203340', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240610_183344:cmsbot_crab_20240610_203342', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240610_183347:cmsbot_crab_rucio_transfers_20240610_203346', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240610_183349:cmsbot_crab_rucio_transfers_group_20240610_203349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240610_183353:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240610_203351', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183356:cmsbot_crab_rucio_transfers_nopublication_20240610_203354', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240610_183359:cmsbot_crab_rucio_transfers_withnoneedm_20240610_203357', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240610_183402:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240610_203400', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-11T09:39:14Z)

all OK. I understand the problem with numCores and will fix
