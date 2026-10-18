# dmwm/CRABServer issue #8341: #756: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-16T12:51:45Z
Closed: 2024-04-22T15:49:01Z
URL: https://github.com/dmwm/CRABServer/issues/8341

## Opening post (cmsdmwmbot, 2024-04-16T12:51:45Z)

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

Started at: 2024-04-16 14:51:44
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/756/)

## Comment (cmsdmwmbot, 2024-04-16T12:54:13Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240416_125318:cmsbot_crab_20240416_145318
240416_125321:cmsbot_crab_20240416_145320
240416_125324:cmsbot_crab_20240416_145323
240416_125326:cmsbot_crab_20240416_145325
240416_125328:cmsbot_crab_20240416_145327
240416_125333:cmsbot_crab_20240416_145330
240416_125336:cmsbot_crab_rucio_transfers_20240416_145334
240416_125338:cmsbot_crab_rucio_transfers_group_20240416_145337
240416_125341:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240416_145340
240416_125344:cmsbot_crab_rucio_transfers_nopublication_20240416_145343
240416_125348:cmsbot_crab_rucio_transfers_withnoneedm_20240416_145346
240416_125351:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240416_145349
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240416_125205:cmsbot_crab_transferOutputs
240416_125208:cmsbot_crab_transferLogs
240416_125210:cmsbot_crab_activity
240416_125212:cmsbot_crab_inputFiles
240416_125214:cmsbot_crab_disableAutomaticOutputCollection
240416_125216:cmsbot_crab_outputFiles
240416_125218:cmsbot_crab_allowUndistributedCMSSW
240416_125221:cmsbot_crab_maxMemoryMB
240416_125223:cmsbot_crab_maxJobRuntimeMin
240416_125225:cmsbot_crab_numCores
240416_125227:cmsbot_crab_scriptExe
240416_125230:cmsbot_crab_scriptArgs
240416_125232:cmsbot_crab_sendVenvFolder
240416_125235:cmsbot_crab_sendExternalFolder
240416_125237:cmsbot_crab_inputDBS
240416_125240:cmsbot_crab_useParent
240416_125242:cmsbot_crab_secondaryInputDataset
240416_125244:cmsbot_crab_lumiMaskFile
240416_125246:cmsbot_crab_lumiMaskUrl
240416_125250:cmsbot_crab_outLFNDirBase
240416_125252:cmsbot_crab_runRange
240416_125254:cmsbot_crab_ignoreLocality
240416_125257:cmsbot_crab_userInputFiles
240416_125259:cmsbot_crab_whitelist
240416_125301:cmsbot_crab_blacklist
240416_125303:cmsbot_crab_ignoreGlobalBlacklist
240416_125306:cmsbot_crab_voRole
240416_125308:cmsbot_crab_voGroup
240416_125310:cmsbot_crab_scheddName
240416_125313:cmsbot_crab_collector
240416_125315:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240416_125203:cmsbot_crab_20240416_145202
```

Finished at: 2024-04-16 14:53:51
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/756/console)

## Comment (cmsdmwmbot, 2024-04-16T13:16:31Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-16 15:16:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/862/console

```
{'TN': '240416_125318:cmsbot_crab_20240416_145318', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 951, 'running': 49}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125321:cmsbot_crab_20240416_145320', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125324:cmsbot_crab_20240416_145323', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125326:cmsbot_crab_20240416_145325', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125328:cmsbot_crab_20240416_145327', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125333:cmsbot_crab_20240416_145330', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125336:cmsbot_crab_rucio_transfers_20240416_145334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125338:cmsbot_crab_rucio_transfers_group_20240416_145337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125341:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240416_145340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125344:cmsbot_crab_rucio_transfers_nopublication_20240416_145343', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125348:cmsbot_crab_rucio_transfers_withnoneedm_20240416_145346', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125351:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240416_145349', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-16T13:18:16Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-16 15:18:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/530/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/530//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-16T13:20:05Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-16 15:20:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1032/console

```
RETRY TESTS:
activity-check.sh 240416_125210:cmsbot_crab_activity - 2
outputFiles-check.sh 240416_125216:cmsbot_crab_outputFiles - 2
numCores-check.sh 240416_125225:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240416_125230:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240416_125246:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240416_125250:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240416_125252:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240416_125257:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240416_125259:cmsbot_crab_whitelist - 2
blacklist-check.sh 240416_125301:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240416_125205:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240416_125208:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240416_125212:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240416_125214:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240416_125218:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240416_125221:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240416_125223:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240416_125227:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240416_125232:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240416_125235:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240416_125237:cmsbot_crab_inputDBS - 0
useParent-check.sh 240416_125240:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240416_125242:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240416_125244:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240416_125254:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240416_125303:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240416_125306:cmsbot_crab_voRole - 0
voGroup-check.sh 240416_125308:cmsbot_crab_voGroup - 0
scheddName-check.sh 240416_125310:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240416_125315:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240416_125313:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-16T13:32:32Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-04-16 15:32:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/863/console

```
{'TN': '240416_125318:cmsbot_crab_20240416_145318', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 923, 'transferring': 74, 'running': 3}, 'publication (fail/tdb/DBS)': '0/800/800'}
{'TN': '240416_125321:cmsbot_crab_20240416_145320', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125324:cmsbot_crab_20240416_145323', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240416_125326:cmsbot_crab_20240416_145325', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240416_125328:cmsbot_crab_20240416_145327', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125333:cmsbot_crab_20240416_145330', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125336:cmsbot_crab_rucio_transfers_20240416_145334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125338:cmsbot_crab_rucio_transfers_group_20240416_145337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125341:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240416_145340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125344:cmsbot_crab_rucio_transfers_nopublication_20240416_145343', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125348:cmsbot_crab_rucio_transfers_withnoneedm_20240416_145346', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125351:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240416_145349', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-16T13:44:27Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-04-16 15:44:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1033/console

```
RETRY TESTS:
outLFNDirBase-check.sh 240416_125250:cmsbot_crab_outLFNDirBase - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240416_125205:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240416_125208:cmsbot_crab_transferLogs - 0
activity-check.sh 240416_125210:cmsbot_crab_activity - 0
inputFiles-check.sh 240416_125212:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240416_125214:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240416_125216:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240416_125218:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240416_125221:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240416_125223:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240416_125225:cmsbot_crab_numCores - 0
scriptExe-check.sh 240416_125227:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240416_125230:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240416_125232:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240416_125235:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240416_125237:cmsbot_crab_inputDBS - 0
useParent-check.sh 240416_125240:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240416_125242:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240416_125244:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240416_125246:cmsbot_crab_lumiMaskUrl - 0
runRange-check.sh 240416_125252:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240416_125254:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240416_125257:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240416_125259:cmsbot_crab_whitelist - 0
blacklist-check.sh 240416_125301:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240416_125303:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240416_125306:cmsbot_crab_voRole - 0
voGroup-check.sh 240416_125308:cmsbot_crab_voGroup - 0
scheddName-check.sh 240416_125310:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240416_125315:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240416_125313:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-16T14:08:29Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-16 16:08:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1034/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240416_125205:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240416_125208:cmsbot_crab_transferLogs - 0
activity-check.sh 240416_125210:cmsbot_crab_activity - 0
inputFiles-check.sh 240416_125212:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240416_125214:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240416_125216:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240416_125218:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240416_125221:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240416_125223:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240416_125225:cmsbot_crab_numCores - 0
scriptExe-check.sh 240416_125227:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240416_125230:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240416_125232:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240416_125235:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240416_125237:cmsbot_crab_inputDBS - 0
useParent-check.sh 240416_125240:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240416_125242:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240416_125244:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240416_125246:cmsbot_crab_lumiMaskUrl - 0
runRange-check.sh 240416_125252:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240416_125254:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240416_125257:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240416_125259:cmsbot_crab_whitelist - 0
blacklist-check.sh 240416_125301:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240416_125303:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240416_125306:cmsbot_crab_voRole - 0
voGroup-check.sh 240416_125308:cmsbot_crab_voGroup - 0
scheddName-check.sh 240416_125310:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240416_125315:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outLFNDirBase-check.sh 240416_125250:cmsbot_crab_outLFNDirBase - 1
collector-check.sh 240416_125313:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-16T14:19:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-04-16 16:19:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/864/console

```
{'TN': '240416_125318:cmsbot_crab_20240416_145318', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240416_125321:cmsbot_crab_20240416_145320', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125324:cmsbot_crab_20240416_145323', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240416_125326:cmsbot_crab_20240416_145325', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240416_125328:cmsbot_crab_20240416_145327', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240416_125333:cmsbot_crab_20240416_145330', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240416_125336:cmsbot_crab_rucio_transfers_20240416_145334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/34/34'}
{'TN': '240416_125338:cmsbot_crab_rucio_transfers_group_20240416_145337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240416_125341:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240416_145340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125344:cmsbot_crab_rucio_transfers_nopublication_20240416_145343', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125348:cmsbot_crab_rucio_transfers_withnoneedm_20240416_145346', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/30/30'}
{'TN': '240416_125351:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240416_145349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-16T15:50:22Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-04-16 17:50:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/865/console

```
{'TN': '240416_125318:cmsbot_crab_20240416_145318', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240416_125321:cmsbot_crab_20240416_145320', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240416_125324:cmsbot_crab_20240416_145323', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240416_125326:cmsbot_crab_20240416_145325', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240416_125328:cmsbot_crab_20240416_145327', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240416_125333:cmsbot_crab_20240416_145330', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240416_125336:cmsbot_crab_rucio_transfers_20240416_145334', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240416_125338:cmsbot_crab_rucio_transfers_group_20240416_145337', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240416_125341:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240416_145340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125344:cmsbot_crab_rucio_transfers_nopublication_20240416_145343', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125348:cmsbot_crab_rucio_transfers_withnoneedm_20240416_145346', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '4/35/35'}
{'TN': '240416_125351:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240416_145349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-16T17:52:30Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 4 out of 5. Test failed. Investigate manually
**Finished at:** 2024-04-16 19:52:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/866/console

```
{'TN': '240416_125318:cmsbot_crab_20240416_145318', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240416_125321:cmsbot_crab_20240416_145320', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240416_125324:cmsbot_crab_20240416_145323', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240416_125326:cmsbot_crab_20240416_145325', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240416_125328:cmsbot_crab_20240416_145327', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240416_125333:cmsbot_crab_20240416_145330', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240416_125336:cmsbot_crab_rucio_transfers_20240416_145334', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240416_125338:cmsbot_crab_rucio_transfers_group_20240416_145337', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240416_125341:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240416_145340', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125344:cmsbot_crab_rucio_transfers_nopublication_20240416_145343', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240416_125348:cmsbot_crab_rucio_transfers_withnoneedm_20240416_145346', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '4/36/35'}
{'TN': '240416_125351:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240416_145349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (novicecpp, 2024-04-22T15:49:02Z)

Transient error. Resubmit (including `--publisher`) was working fine.
