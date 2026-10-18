# dmwm/CRABServer issue #8458: #789: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-02T15:41:49Z
Closed: 2024-06-03T10:08:08Z
URL: https://github.com/dmwm/CRABServer/issues/8458

## Opening post (cmsdmwmbot, 2024-06-02T15:41:49Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-06-02 17:41:48
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/789/)

## Comment (cmsdmwmbot, 2024-06-02T15:44:27Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240602_154335:cmsbot_crab_20240602_174334
240602_154337:cmsbot_crab_20240602_174336
240602_154339:cmsbot_crab_20240602_174338
240602_154341:cmsbot_crab_20240602_174341
240602_154343:cmsbot_crab_20240602_174343
240602_154347:cmsbot_crab_20240602_174345
240602_154350:cmsbot_crab_rucio_transfers_20240602_174349
240602_154352:cmsbot_crab_rucio_transfers_group_20240602_174352
240602_154355:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240602_174354
240602_154358:cmsbot_crab_rucio_transfers_nopublication_20240602_174357
240602_154402:cmsbot_crab_rucio_transfers_withnoneedm_20240602_174400
240602_154405:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240602_174404
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240602_154216:cmsbot_crab_transferOutputs
240602_154225:cmsbot_crab_transferLogs
240602_154228:cmsbot_crab_activity
240602_154230:cmsbot_crab_inputFiles
240602_154232:cmsbot_crab_disableAutomaticOutputCollection
240602_154234:cmsbot_crab_outputFiles
240602_154236:cmsbot_crab_allowUndistributedCMSSW
240602_154238:cmsbot_crab_maxMemoryMB
240602_154240:cmsbot_crab_maxJobRuntimeMin
240602_154243:cmsbot_crab_numCores
240602_154245:cmsbot_crab_scriptExe
240602_154247:cmsbot_crab_scriptArgs
240602_154249:cmsbot_crab_sendVenvFolder
240602_154252:cmsbot_crab_sendExternalFolder
240602_154254:cmsbot_crab_inputDBS
240602_154256:cmsbot_crab_useParent
240602_154259:cmsbot_crab_secondaryInputDataset
240602_154301:cmsbot_crab_lumiMaskFile
240602_154304:cmsbot_crab_lumiMaskUrl
240602_154307:cmsbot_crab_outLFNDirBase
240602_154309:cmsbot_crab_runRange
240602_154311:cmsbot_crab_ignoreLocality
240602_154313:cmsbot_crab_userInputFiles
240602_154315:cmsbot_crab_whitelist
240602_154317:cmsbot_crab_blacklist
240602_154320:cmsbot_crab_ignoreGlobalBlacklist
240602_154322:cmsbot_crab_voRole
240602_154324:cmsbot_crab_voGroup
240602_154327:cmsbot_crab_scheddName
240602_154329:cmsbot_crab_collector
240602_154332:cmsbot_crab_extraJDL
```

Finished at: 2024-06-02 17:44:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/789/console)

## Comment (cmsdmwmbot, 2024-06-02T16:05:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-02 18:05:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/945/console

```
{'TN': '240602_154335:cmsbot_crab_20240602_174334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 411, 'transferring': 582, 'idle': 6, 'unsubmitted': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154337:cmsbot_crab_20240602_174336', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154339:cmsbot_crab_20240602_174338', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154341:cmsbot_crab_20240602_174341', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154343:cmsbot_crab_20240602_174343', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154347:cmsbot_crab_20240602_174345', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154350:cmsbot_crab_rucio_transfers_20240602_174349', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 1, 'transferring': 39}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154352:cmsbot_crab_rucio_transfers_group_20240602_174352', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154355:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240602_174354', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154358:cmsbot_crab_rucio_transfers_nopublication_20240602_174357', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154402:cmsbot_crab_rucio_transfers_withnoneedm_20240602_174400', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 37, 'idle': 1, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154405:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240602_174404', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-02T16:08:45Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-02 18:08:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1083/console

```
RETRY TESTS:
outputFiles-check.sh 240602_154234:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240602_154240:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240602_154243:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240602_154247:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240602_154301:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240602_154304:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240602_154309:cmsbot_crab_runRange - 2
whitelist-check.sh 240602_154315:cmsbot_crab_whitelist - 2
blacklist-check.sh 240602_154317:cmsbot_crab_blacklist - 2
voRole-check.sh 240602_154322:cmsbot_crab_voRole - 2
voGroup-check.sh 240602_154324:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240602_154216:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240602_154225:cmsbot_crab_transferLogs - 0
activity-check.sh 240602_154228:cmsbot_crab_activity - 0
inputFiles-check.sh 240602_154230:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240602_154232:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240602_154236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240602_154238:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240602_154245:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240602_154249:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240602_154252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240602_154254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240602_154256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240602_154259:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240602_154307:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240602_154311:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240602_154313:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240602_154320:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240602_154327:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240602_154332:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240602_154329:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-06-02T16:21:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-02 18:21:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/946/console

```
{'TN': '240602_154335:cmsbot_crab_20240602_174334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 411, 'transferring': 582, 'idle': 6, 'unsubmitted': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154337:cmsbot_crab_20240602_174336', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154339:cmsbot_crab_20240602_174338', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154341:cmsbot_crab_20240602_174341', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154343:cmsbot_crab_20240602_174343', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154347:cmsbot_crab_20240602_174345', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154350:cmsbot_crab_rucio_transfers_20240602_174349', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154352:cmsbot_crab_rucio_transfers_group_20240602_174352', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154355:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240602_174354', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154358:cmsbot_crab_rucio_transfers_nopublication_20240602_174357', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154402:cmsbot_crab_rucio_transfers_withnoneedm_20240602_174400', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154405:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240602_174404', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-02T16:32:15Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-06-02 18:32:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1084/console

```
RETRY TESTS:
outputFiles-check.sh 240602_154234:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240602_154240:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240602_154243:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240602_154247:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240602_154301:cmsbot_crab_lumiMaskFile - 2
runRange-check.sh 240602_154309:cmsbot_crab_runRange - 2
whitelist-check.sh 240602_154315:cmsbot_crab_whitelist - 2
blacklist-check.sh 240602_154317:cmsbot_crab_blacklist - 2
voRole-check.sh 240602_154322:cmsbot_crab_voRole - 2
voGroup-check.sh 240602_154324:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240602_154216:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240602_154225:cmsbot_crab_transferLogs - 0
activity-check.sh 240602_154228:cmsbot_crab_activity - 0
inputFiles-check.sh 240602_154230:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240602_154232:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240602_154236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240602_154238:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240602_154245:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240602_154249:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240602_154252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240602_154254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240602_154256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240602_154259:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240602_154304:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240602_154307:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240602_154311:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240602_154313:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240602_154320:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240602_154327:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240602_154332:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240602_154329:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-06-02T16:55:47Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-06-02 18:55:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1085/console

```
RETRY TESTS:
outputFiles-check.sh 240602_154234:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240602_154240:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240602_154243:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240602_154247:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240602_154301:cmsbot_crab_lumiMaskFile - 2
runRange-check.sh 240602_154309:cmsbot_crab_runRange - 2
whitelist-check.sh 240602_154315:cmsbot_crab_whitelist - 2
blacklist-check.sh 240602_154317:cmsbot_crab_blacklist - 2
voRole-check.sh 240602_154322:cmsbot_crab_voRole - 2
voGroup-check.sh 240602_154324:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240602_154216:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240602_154225:cmsbot_crab_transferLogs - 0
activity-check.sh 240602_154228:cmsbot_crab_activity - 0
inputFiles-check.sh 240602_154230:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240602_154232:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240602_154236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240602_154238:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240602_154245:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240602_154249:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240602_154252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240602_154254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240602_154256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240602_154259:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240602_154304:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240602_154307:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240602_154311:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240602_154313:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240602_154320:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240602_154327:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240602_154332:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240602_154329:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-06-02T17:07:11Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-02 19:07:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/947/console

```
{'TN': '240602_154335:cmsbot_crab_20240602_174334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 411, 'transferring': 582, 'idle': 6, 'unsubmitted': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154337:cmsbot_crab_20240602_174336', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154339:cmsbot_crab_20240602_174338', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154341:cmsbot_crab_20240602_174341', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154343:cmsbot_crab_20240602_174343', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154347:cmsbot_crab_20240602_174345', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154350:cmsbot_crab_rucio_transfers_20240602_174349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154352:cmsbot_crab_rucio_transfers_group_20240602_174352', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154355:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240602_174354', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154358:cmsbot_crab_rucio_transfers_nopublication_20240602_174357', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154402:cmsbot_crab_rucio_transfers_withnoneedm_20240602_174400', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154405:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240602_174404', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-02T17:19:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2024-06-02 19:19:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1086/console

```
RETRY TESTS:
outputFiles-check.sh 240602_154234:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240602_154240:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240602_154243:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240602_154247:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240602_154301:cmsbot_crab_lumiMaskFile - 2
runRange-check.sh 240602_154309:cmsbot_crab_runRange - 2
whitelist-check.sh 240602_154315:cmsbot_crab_whitelist - 2
blacklist-check.sh 240602_154317:cmsbot_crab_blacklist - 2
voRole-check.sh 240602_154322:cmsbot_crab_voRole - 2
voGroup-check.sh 240602_154324:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240602_154216:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240602_154225:cmsbot_crab_transferLogs - 0
activity-check.sh 240602_154228:cmsbot_crab_activity - 0
inputFiles-check.sh 240602_154230:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240602_154232:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240602_154236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240602_154238:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240602_154245:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240602_154249:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240602_154252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240602_154254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240602_154256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240602_154259:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240602_154304:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240602_154307:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240602_154311:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240602_154313:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240602_154320:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240602_154327:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240602_154332:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240602_154329:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-06-02T17:42:57Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-02 19:42:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1087/console

```
RETRY TESTS:
outputFiles-check.sh 240602_154234:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240602_154240:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240602_154243:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240602_154247:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240602_154301:cmsbot_crab_lumiMaskFile - 2
runRange-check.sh 240602_154309:cmsbot_crab_runRange - 2
whitelist-check.sh 240602_154315:cmsbot_crab_whitelist - 2
blacklist-check.sh 240602_154317:cmsbot_crab_blacklist - 2
voRole-check.sh 240602_154322:cmsbot_crab_voRole - 2
voGroup-check.sh 240602_154324:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240602_154216:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240602_154225:cmsbot_crab_transferLogs - 0
activity-check.sh 240602_154228:cmsbot_crab_activity - 0
inputFiles-check.sh 240602_154230:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240602_154232:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240602_154236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240602_154238:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240602_154245:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240602_154249:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240602_154252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240602_154254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240602_154256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240602_154259:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240602_154304:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240602_154307:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240602_154311:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240602_154313:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240602_154320:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240602_154327:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240602_154332:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240602_154329:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-06-02T18:39:52Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-06-02 20:39:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/948/console

```
{'TN': '240602_154335:cmsbot_crab_20240602_174334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 411, 'transferring': 582, 'idle': 6, 'unsubmitted': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154337:cmsbot_crab_20240602_174336', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154339:cmsbot_crab_20240602_174338', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154341:cmsbot_crab_20240602_174341', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154343:cmsbot_crab_20240602_174343', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154347:cmsbot_crab_20240602_174345', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154350:cmsbot_crab_rucio_transfers_20240602_174349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154352:cmsbot_crab_rucio_transfers_group_20240602_174352', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154355:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240602_174354', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154358:cmsbot_crab_rucio_transfers_nopublication_20240602_174357', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154402:cmsbot_crab_rucio_transfers_withnoneedm_20240602_174400', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154405:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240602_174404', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-02T20:41:48Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-06-02 22:41:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/949/console

```
{'TN': '240602_154335:cmsbot_crab_20240602_174334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 411, 'transferring': 582, 'idle': 6, 'unsubmitted': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154337:cmsbot_crab_20240602_174336', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154339:cmsbot_crab_20240602_174338', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154341:cmsbot_crab_20240602_174341', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154343:cmsbot_crab_20240602_174343', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154347:cmsbot_crab_20240602_174345', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154350:cmsbot_crab_rucio_transfers_20240602_174349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154352:cmsbot_crab_rucio_transfers_group_20240602_174352', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154355:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240602_174354', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154358:cmsbot_crab_rucio_transfers_nopublication_20240602_174357', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154402:cmsbot_crab_rucio_transfers_withnoneedm_20240602_174400', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154405:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240602_174404', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-02T22:42:44Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-03 00:42:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/950/console

```
{'TN': '240602_154335:cmsbot_crab_20240602_174334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 411, 'transferring': 582, 'idle': 6, 'unsubmitted': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154337:cmsbot_crab_20240602_174336', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154339:cmsbot_crab_20240602_174338', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154341:cmsbot_crab_20240602_174341', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154343:cmsbot_crab_20240602_174343', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154347:cmsbot_crab_20240602_174345', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154350:cmsbot_crab_rucio_transfers_20240602_174349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154352:cmsbot_crab_rucio_transfers_group_20240602_174352', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154355:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240602_174354', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154358:cmsbot_crab_rucio_transfers_nopublication_20240602_174357', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154402:cmsbot_crab_rucio_transfers_withnoneedm_20240602_174400', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154405:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240602_174404', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T08:33:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 0. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-03 10:33:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/951/console

```
{'TN': '240602_154335:cmsbot_crab_20240602_174334', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 411, 'transferring': 582, 'idle': 6, 'unsubmitted': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154337:cmsbot_crab_20240602_174336', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154339:cmsbot_crab_20240602_174338', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154341:cmsbot_crab_20240602_174341', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154343:cmsbot_crab_20240602_174343', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154347:cmsbot_crab_20240602_174345', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154350:cmsbot_crab_rucio_transfers_20240602_174349', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154352:cmsbot_crab_rucio_transfers_group_20240602_174352', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154355:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240602_174354', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154358:cmsbot_crab_rucio_transfers_nopublication_20240602_174357', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240602_154402:cmsbot_crab_rucio_transfers_withnoneedm_20240602_174400', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240602_154405:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240602_174404', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-03T08:34:41Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 0. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-03 10:34:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1088/console

```
RETRY TESTS:
outputFiles-check.sh 240602_154234:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240602_154240:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240602_154243:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240602_154247:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240602_154301:cmsbot_crab_lumiMaskFile - 2
runRange-check.sh 240602_154309:cmsbot_crab_runRange - 2
whitelist-check.sh 240602_154315:cmsbot_crab_whitelist - 2
blacklist-check.sh 240602_154317:cmsbot_crab_blacklist - 2
voRole-check.sh 240602_154322:cmsbot_crab_voRole - 2
voGroup-check.sh 240602_154324:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240602_154216:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240602_154225:cmsbot_crab_transferLogs - 0
activity-check.sh 240602_154228:cmsbot_crab_activity - 0
inputFiles-check.sh 240602_154230:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240602_154232:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240602_154236:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240602_154238:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 240602_154245:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240602_154249:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240602_154252:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240602_154254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240602_154256:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240602_154259:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240602_154304:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240602_154307:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240602_154311:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240602_154313:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240602_154320:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240602_154327:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240602_154332:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240602_154329:cmsbot_crab_collector - 1
```

## Comment (belforte, 2024-06-03T10:11:08Z)

ASO problems due to FTS
