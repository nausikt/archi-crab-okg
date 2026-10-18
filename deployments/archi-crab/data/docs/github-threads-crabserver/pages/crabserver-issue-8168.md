# dmwm/CRABServer issue #8168: #675: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-11T22:01:02Z
Closed: 2024-01-12T14:48:41Z
URL: https://github.com/dmwm/CRABServer/issues/8168

## Opening post (cmsdmwmbot, 2024-01-11T22:01:02Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-01-11 23:01:01
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/675/)

## Comment (cmsdmwmbot, 2024-01-11T22:04:10Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240111_220304:cmsbot_crab_20240111_230304
240111_220306:cmsbot_crab_20240111_230306
240111_220308:cmsbot_crab_20240111_230308
240111_220310:cmsbot_crab_20240111_230310
240111_220312:cmsbot_crab_20240111_230312
240111_220330:cmsbot_crab_20240111_230314
240111_220333:cmsbot_crab_rucio_transfers_20240111_230331
240111_220335:cmsbot_crab_rucio_transfers_group_20240111_230335
240111_220338:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240111_230337
240111_220342:cmsbot_crab_rucio_transfers_nopublication_20240111_230340
240111_220345:cmsbot_crab_rucio_transfers_withnoneedm_20240111_230343
240111_220348:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240111_230347
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_220122:cmsbot_crab_transferOutputs
240111_220124:cmsbot_crab_transferLogs
240111_220126:cmsbot_crab_activity
240111_220128:cmsbot_crab_inputFiles
240111_220130:cmsbot_crab_disableAutomaticOutputCollection
240111_220132:cmsbot_crab_outputFiles
240111_220134:cmsbot_crab_allowUndistributedCMSSW
240111_220136:cmsbot_crab_maxMemoryMB
240111_220138:cmsbot_crab_maxJobRuntimeMin
240111_220141:cmsbot_crab_numCores
240111_220143:cmsbot_crab_scriptExe
240111_220145:cmsbot_crab_scriptArgs
240111_220147:cmsbot_crab_sendVenvFolder
240111_220226:cmsbot_crab_sendExternalFolder
240111_220228:cmsbot_crab_inputDBS
240111_220230:cmsbot_crab_useParent
240111_220232:cmsbot_crab_secondaryInputDataset
240111_220234:cmsbot_crab_lumiMaskFile
240111_220236:cmsbot_crab_lumiMaskUrl
240111_220239:cmsbot_crab_outLFNDirBase
240111_220241:cmsbot_crab_runRange
240111_220243:cmsbot_crab_ignoreLocality
240111_220245:cmsbot_crab_userInputFiles
240111_220247:cmsbot_crab_whitelist
240111_220249:cmsbot_crab_blacklist
240111_220251:cmsbot_crab_ignoreGlobalBlacklist
240111_220253:cmsbot_crab_voRole
240111_220255:cmsbot_crab_voGroup
240111_220257:cmsbot_crab_scheddName
240111_220259:cmsbot_crab_collector
240111_220301:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_220120:cmsbot_crab_20240111_230120
```

Finished at: 2024-01-11 23:03:49
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/675/console)

## Comment (cmsdmwmbot, 2024-01-11T22:25:59Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 0 out of 4. Something went wrong. Investigate manually.
**Finished at:** 2024-01-11 23:25:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/691/console

```

```

## Comment (cmsdmwmbot, 2024-01-11T22:28:55Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 23:28:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/494/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/494//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-11T22:30:00Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 23:29:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/883/console

```
RETRY TESTS:
numCores-check.sh 240111_220141:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240111_220145:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240111_220236:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240111_220241:cmsbot_crab_runRange - 2
whitelist-check.sh 240111_220247:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_220249:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240111_220251:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_220122:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_220124:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_220126:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_220128:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_220130:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_220132:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_220134:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_220136:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_220138:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240111_220143:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240111_220147:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_220226:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_220228:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_220230:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_220232:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_220234:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_220239:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240111_220243:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_220245:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240111_220253:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_220255:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_220257:cmsbot_crab_scheddName - 0
collector-check.sh 240111_220259:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_220301:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T22:53:58Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-01-11 23:53:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/884/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_220122:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_220124:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_220126:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_220128:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_220130:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_220132:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_220134:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_220136:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_220138:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_220141:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_220143:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_220145:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_220147:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_220226:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_220228:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_220230:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_220232:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_220234:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_220236:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_220239:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_220241:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_220243:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_220245:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_220247:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_220249:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_220251:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_220253:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_220255:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_220257:cmsbot_crab_scheddName - 0
collector-check.sh 240111_220259:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_220301:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-12T09:59:09Z)

TaskSubmissionStatusTtracking failure was due to #8169 
I have pushed a fix and am retrying the test

## Comment (cmsdmwmbot, 2024-01-12T10:00:26Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 0 out of 0. Something went wrong. Investigate manually.
**Finished at:** 2024-01-12 11:00:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/692/console

```

```

## Comment (belforte, 2024-01-12T10:34:48Z)

turns out that TSST test still uses the testing container, not singularity. So frozen version of code. Let's change.

## Comment (cmsdmwmbot, 2024-01-12T14:05:40Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-01-12 15:05:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/703/console

```
{'TN': '240111_220304:cmsbot_crab_20240111_230304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240111_220306:cmsbot_crab_20240111_230306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220308:cmsbot_crab_20240111_230308', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220310:cmsbot_crab_20240111_230310', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220312:cmsbot_crab_20240111_230312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240111_220330:cmsbot_crab_20240111_230314', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220333:cmsbot_crab_rucio_transfers_20240111_230331', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '26/14/14'}
{'TN': '240111_220335:cmsbot_crab_rucio_transfers_group_20240111_230335', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220338:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240111_230337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220342:cmsbot_crab_rucio_transfers_nopublication_20240111_230340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220345:cmsbot_crab_rucio_transfers_withnoneedm_20240111_230343', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '3/37/37'}
{'TN': '240111_220348:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240111_230347', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-01-12T14:17:00Z)

FInally jenkis test runs !
But there are publication failures in some of the new `*rucio_transfers*` tests.

I guess it is safe to ignore them for the purpose of this validation, I gave a look at Publisher logs and it appears that some block got files added after it was closed, or maybe the Publisher got confused. 

also now some rucio tests allows for publication, some not, but we only have a global flag which makes Jenkins wait until all files in all tasks were published (or reached the retry limit).

## Comment (belforte, 2024-01-12T14:48:41Z)

publication failures tracked in #8178 
closing

## Comment (cmsdmwmbot, 2024-01-12T14:51:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-01-12 15:51:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/704/console

```
{'TN': '240111_220304:cmsbot_crab_20240111_230304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240111_220306:cmsbot_crab_20240111_230306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220308:cmsbot_crab_20240111_230308', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220310:cmsbot_crab_20240111_230310', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220312:cmsbot_crab_20240111_230312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240111_220330:cmsbot_crab_20240111_230314', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220333:cmsbot_crab_rucio_transfers_20240111_230331', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '26/14/14'}
{'TN': '240111_220335:cmsbot_crab_rucio_transfers_group_20240111_230335', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220338:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240111_230337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220342:cmsbot_crab_rucio_transfers_nopublication_20240111_230340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220345:cmsbot_crab_rucio_transfers_withnoneedm_20240111_230343', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '3/37/37'}
{'TN': '240111_220348:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240111_230347', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T16:22:51Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-01-12 17:22:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/710/console

```
{'TN': '240111_220304:cmsbot_crab_20240111_230304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240111_220306:cmsbot_crab_20240111_230306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220308:cmsbot_crab_20240111_230308', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220310:cmsbot_crab_20240111_230310', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220312:cmsbot_crab_20240111_230312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240111_220330:cmsbot_crab_20240111_230314', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220333:cmsbot_crab_rucio_transfers_20240111_230331', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '26/14/14'}
{'TN': '240111_220335:cmsbot_crab_rucio_transfers_group_20240111_230335', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220338:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240111_230337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220342:cmsbot_crab_rucio_transfers_nopublication_20240111_230340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220345:cmsbot_crab_rucio_transfers_withnoneedm_20240111_230343', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '3/37/37'}
{'TN': '240111_220348:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240111_230347', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T18:24:26Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-01-12 19:24:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/714/console

```
{'TN': '240111_220304:cmsbot_crab_20240111_230304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240111_220306:cmsbot_crab_20240111_230306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220308:cmsbot_crab_20240111_230308', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220310:cmsbot_crab_20240111_230310', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220312:cmsbot_crab_20240111_230312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240111_220330:cmsbot_crab_20240111_230314', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220333:cmsbot_crab_rucio_transfers_20240111_230331', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '26/14/14'}
{'TN': '240111_220335:cmsbot_crab_rucio_transfers_group_20240111_230335', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220338:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240111_230337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220342:cmsbot_crab_rucio_transfers_nopublication_20240111_230340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220345:cmsbot_crab_rucio_transfers_withnoneedm_20240111_230343', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '3/37/37'}
{'TN': '240111_220348:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240111_230347', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T20:26:20Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-01-12 21:26:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/717/console

```
{'TN': '240111_220304:cmsbot_crab_20240111_230304', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240111_220306:cmsbot_crab_20240111_230306', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220308:cmsbot_crab_20240111_230308', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240111_220310:cmsbot_crab_20240111_230310', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220312:cmsbot_crab_20240111_230312', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240111_220330:cmsbot_crab_20240111_230314', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240111_220333:cmsbot_crab_rucio_transfers_20240111_230331', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '26/14/14'}
{'TN': '240111_220335:cmsbot_crab_rucio_transfers_group_20240111_230335', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220338:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240111_230337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220342:cmsbot_crab_rucio_transfers_nopublication_20240111_230340', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240111_220345:cmsbot_crab_rucio_transfers_withnoneedm_20240111_230343', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '3/37/37'}
{'TN': '240111_220348:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240111_230347', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
