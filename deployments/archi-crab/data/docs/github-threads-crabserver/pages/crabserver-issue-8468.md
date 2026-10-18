# dmwm/CRABServer issue #8468: #794: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-03T22:11:09Z
Closed: 2024-06-03T23:56:59Z
URL: https://github.com/dmwm/CRABServer/issues/8468

## Opening post (cmsdmwmbot, 2024-06-03T22:11:09Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-06-04 00:11:08
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/794/)

## Comment (cmsdmwmbot, 2024-06-03T22:13:51Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240603_221258:cmsbot_crab_20240604_001257
240603_221300:cmsbot_crab_20240604_001300
240603_221302:cmsbot_crab_20240604_001302
240603_221305:cmsbot_crab_20240604_001304
240603_221307:cmsbot_crab_20240604_001306
240603_221311:cmsbot_crab_20240604_001308
240603_221314:cmsbot_crab_rucio_transfers_20240604_001312
240603_221316:cmsbot_crab_rucio_transfers_group_20240604_001315
240603_221320:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001317
240603_221323:cmsbot_crab_rucio_transfers_nopublication_20240604_001322
240603_221326:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001325
240603_221329:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001328
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240603_221127:cmsbot_crab_transferOutputs
240603_221154:cmsbot_crab_transferLogs
240603_221156:cmsbot_crab_activity
240603_221158:cmsbot_crab_inputFiles
240603_221200:cmsbot_crab_disableAutomaticOutputCollection
240603_221202:cmsbot_crab_outputFiles
240603_221204:cmsbot_crab_allowUndistributedCMSSW
240603_221206:cmsbot_crab_maxMemoryMB
240603_221208:cmsbot_crab_maxJobRuntimeMin
240603_221210:cmsbot_crab_numCores
240603_221212:cmsbot_crab_scriptExe
240603_221215:cmsbot_crab_scriptArgs
240603_221217:cmsbot_crab_sendVenvFolder
240603_221219:cmsbot_crab_sendExternalFolder
240603_221221:cmsbot_crab_inputDBS
240603_221223:cmsbot_crab_useParent
240603_221225:cmsbot_crab_secondaryInputDataset
240603_221227:cmsbot_crab_lumiMaskFile
240603_221229:cmsbot_crab_lumiMaskUrl
240603_221232:cmsbot_crab_outLFNDirBase
240603_221234:cmsbot_crab_runRange
240603_221236:cmsbot_crab_ignoreLocality
240603_221238:cmsbot_crab_userInputFiles
240603_221240:cmsbot_crab_whitelist
240603_221242:cmsbot_crab_blacklist
240603_221244:cmsbot_crab_ignoreGlobalBlacklist
240603_221246:cmsbot_crab_voRole
240603_221248:cmsbot_crab_voGroup
240603_221251:cmsbot_crab_scheddName
240603_221253:cmsbot_crab_collector
240603_221255:cmsbot_crab_extraJDL
```

Finished at: 2024-06-04 00:13:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/794/console)

## Comment (cmsdmwmbot, 2024-06-03T22:34:45Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-04 00:34:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/958/console

```
{'TN': '240603_221258:cmsbot_crab_20240604_001257', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 1, 'idle': 516, 'unsubmitted': 483}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221300:cmsbot_crab_20240604_001300', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'idle': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221302:cmsbot_crab_20240604_001302', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221305:cmsbot_crab_20240604_001304', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221307:cmsbot_crab_20240604_001306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'idle': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221311:cmsbot_crab_20240604_001308', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'idle': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221314:cmsbot_crab_rucio_transfers_20240604_001312', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'idle': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221316:cmsbot_crab_rucio_transfers_group_20240604_001315', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'idle': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221320:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001317', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221323:cmsbot_crab_rucio_transfers_nopublication_20240604_001322', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221326:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001325', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221329:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001328', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T22:37:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-04 00:37:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1094/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240603_221208:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 240603_221212:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240603_221215:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240603_221227:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240603_221229:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240603_221232:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240603_221234:cmsbot_crab_runRange - 2
whitelist-check.sh 240603_221240:cmsbot_crab_whitelist - 2
blacklist-check.sh 240603_221242:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_221127:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_221154:cmsbot_crab_transferLogs - 0
activity-check.sh 240603_221156:cmsbot_crab_activity - 0
inputFiles-check.sh 240603_221158:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_221200:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240603_221202:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240603_221204:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240603_221206:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240603_221217:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_221219:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_221221:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_221223:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_221225:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240603_221236:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_221238:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240603_221244:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_221246:cmsbot_crab_voRole - 0
voGroup-check.sh 240603_221248:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_221251:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240603_221255:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 240603_221210:cmsbot_crab_numCores - 1
collector-check.sh 240603_221253:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-06-03T22:50:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-04 00:50:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/960/console

```
{'TN': '240603_221258:cmsbot_crab_20240604_001257', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 995, 'running': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221300:cmsbot_crab_20240604_001300', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221302:cmsbot_crab_20240604_001302', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221305:cmsbot_crab_20240604_001304', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221307:cmsbot_crab_20240604_001306', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221311:cmsbot_crab_20240604_001308', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 7, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221314:cmsbot_crab_rucio_transfers_20240604_001312', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221316:cmsbot_crab_rucio_transfers_group_20240604_001315', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221320:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001317', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221323:cmsbot_crab_rucio_transfers_nopublication_20240604_001322', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221326:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001325', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221329:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001328', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T23:01:55Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-06-04 01:01:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1096/console

```
RETRY TESTS:
scriptExe-check.sh 240603_221212:cmsbot_crab_scriptExe - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_221127:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_221154:cmsbot_crab_transferLogs - 0
activity-check.sh 240603_221156:cmsbot_crab_activity - 0
inputFiles-check.sh 240603_221158:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_221200:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240603_221202:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240603_221204:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240603_221206:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240603_221208:cmsbot_crab_maxJobRuntimeMin - 0
scriptArgs-check.sh 240603_221215:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240603_221217:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_221219:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_221221:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_221223:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_221225:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240603_221227:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240603_221229:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240603_221232:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240603_221234:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240603_221236:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_221238:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240603_221240:cmsbot_crab_whitelist - 0
blacklist-check.sh 240603_221242:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240603_221244:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_221246:cmsbot_crab_voRole - 0
voGroup-check.sh 240603_221248:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_221251:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240603_221255:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 240603_221210:cmsbot_crab_numCores - 1
collector-check.sh 240603_221253:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-06-03T23:26:04Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-04 01:26:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1099/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240603_221127:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240603_221154:cmsbot_crab_transferLogs - 0
activity-check.sh 240603_221156:cmsbot_crab_activity - 0
inputFiles-check.sh 240603_221158:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240603_221200:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240603_221202:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240603_221204:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240603_221206:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240603_221208:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240603_221212:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240603_221215:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240603_221217:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240603_221219:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240603_221221:cmsbot_crab_inputDBS - 0
useParent-check.sh 240603_221223:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240603_221225:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240603_221227:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240603_221229:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240603_221232:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240603_221234:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240603_221236:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240603_221238:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240603_221240:cmsbot_crab_whitelist - 0
blacklist-check.sh 240603_221242:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240603_221244:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240603_221246:cmsbot_crab_voRole - 0
voGroup-check.sh 240603_221248:cmsbot_crab_voGroup - 0
scheddName-check.sh 240603_221251:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240603_221255:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 240603_221210:cmsbot_crab_numCores - 1
collector-check.sh 240603_221253:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-06-03T23:36:34Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-04 01:36:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/964/console

```
{'TN': '240603_221258:cmsbot_crab_20240604_001257', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 995, 'running': 2, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240603_221300:cmsbot_crab_20240604_001300', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221302:cmsbot_crab_20240604_001302', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221305:cmsbot_crab_20240604_001304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221307:cmsbot_crab_20240604_001306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/99/99'}
{'TN': '240603_221311:cmsbot_crab_20240604_001308', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/7/7'}
{'TN': '240603_221314:cmsbot_crab_rucio_transfers_20240604_001312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221316:cmsbot_crab_rucio_transfers_group_20240604_001315', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221320:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001317', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221323:cmsbot_crab_rucio_transfers_nopublication_20240604_001322', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221326:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001325', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221329:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001328', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-03T23:56:59Z)

wrong code, my bad

## Comment (cmsdmwmbot, 2024-06-04T01:07:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-06-04 03:07:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/967/console

```
{'TN': '240603_221258:cmsbot_crab_20240604_001257', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 998, 'failed': 2}, 'publication (fail/tdb/DBS)': '0/998/998'}
{'TN': '240603_221300:cmsbot_crab_20240604_001300', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221302:cmsbot_crab_20240604_001302', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221305:cmsbot_crab_20240604_001304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221307:cmsbot_crab_20240604_001306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_221311:cmsbot_crab_20240604_001308', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221314:cmsbot_crab_rucio_transfers_20240604_001312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221316:cmsbot_crab_rucio_transfers_group_20240604_001315', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221320:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001317', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221323:cmsbot_crab_rucio_transfers_nopublication_20240604_001322', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240603_221326:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001325', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221329:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001328', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-04T03:10:04Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-06-04 05:10:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/970/console

```
{'TN': '240603_221258:cmsbot_crab_20240604_001257', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 998, 'failed': 2}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240603_221300:cmsbot_crab_20240604_001300', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221302:cmsbot_crab_20240604_001302', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221305:cmsbot_crab_20240604_001304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221307:cmsbot_crab_20240604_001306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_221311:cmsbot_crab_20240604_001308', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221314:cmsbot_crab_rucio_transfers_20240604_001312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221316:cmsbot_crab_rucio_transfers_group_20240604_001315', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221320:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001317', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221323:cmsbot_crab_rucio_transfers_nopublication_20240604_001322', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240603_221326:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001325', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221329:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001328', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-04T05:14:01Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-04 07:13:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/972/console

```
{'TN': '240603_221258:cmsbot_crab_20240604_001257', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 998, 'failed': 2}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240603_221300:cmsbot_crab_20240604_001300', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221302:cmsbot_crab_20240604_001302', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240603_221305:cmsbot_crab_20240604_001304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221307:cmsbot_crab_20240604_001306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240603_221311:cmsbot_crab_20240604_001308', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240603_221314:cmsbot_crab_rucio_transfers_20240604_001312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221316:cmsbot_crab_rucio_transfers_group_20240604_001315', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221320:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_001317', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240603_221323:cmsbot_crab_rucio_transfers_nopublication_20240604_001322', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240603_221326:cmsbot_crab_rucio_transfers_withnoneedm_20240604_001325', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240603_221329:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_001328', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
