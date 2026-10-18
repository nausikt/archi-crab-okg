# dmwm/CRABServer issue #8247: #714: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-02-18T17:29:53Z
Closed: 2024-02-19T09:11:58Z
URL: https://github.com/dmwm/CRABServer/issues/8247

## Opening post (cmsdmwmbot, 2024-02-18T17:29:53Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-02-18 18:29:52
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/714/)

## Comment (cmsdmwmbot, 2024-02-18T17:33:08Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240218_173158:cmsbot_crab_20240218_183158
240218_173200:cmsbot_crab_20240218_183200
240218_173202:cmsbot_crab_20240218_183202
240218_173205:cmsbot_crab_20240218_183204
240218_173207:cmsbot_crab_20240218_183206
240218_173230:cmsbot_crab_20240218_183208
240218_173233:cmsbot_crab_rucio_transfers_20240218_183231
240218_173235:cmsbot_crab_rucio_transfers_group_20240218_183234
240218_173237:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240218_183236
240218_173240:cmsbot_crab_rucio_transfers_nopublication_20240218_183239
240218_173243:cmsbot_crab_rucio_transfers_withnoneedm_20240218_183242
240218_173246:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240218_183245
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240218_173013:cmsbot_crab_transferOutputs
240218_173015:cmsbot_crab_transferLogs
240218_173017:cmsbot_crab_activity
240218_173019:cmsbot_crab_inputFiles
240218_173021:cmsbot_crab_disableAutomaticOutputCollection
240218_173023:cmsbot_crab_outputFiles
240218_173025:cmsbot_crab_allowUndistributedCMSSW
240218_173028:cmsbot_crab_maxMemoryMB
240218_173030:cmsbot_crab_maxJobRuntimeMin
240218_173032:cmsbot_crab_numCores
240218_173034:cmsbot_crab_scriptExe
240218_173036:cmsbot_crab_scriptArgs
240218_173039:cmsbot_crab_sendVenvFolder
240218_173119:cmsbot_crab_sendExternalFolder
240218_173121:cmsbot_crab_inputDBS
240218_173123:cmsbot_crab_useParent
240218_173125:cmsbot_crab_secondaryInputDataset
240218_173127:cmsbot_crab_lumiMaskFile
240218_173130:cmsbot_crab_lumiMaskUrl
240218_173133:cmsbot_crab_outLFNDirBase
240218_173135:cmsbot_crab_runRange
240218_173137:cmsbot_crab_ignoreLocality
240218_173139:cmsbot_crab_userInputFiles
240218_173141:cmsbot_crab_whitelist
240218_173143:cmsbot_crab_blacklist
240218_173145:cmsbot_crab_ignoreGlobalBlacklist
240218_173147:cmsbot_crab_voRole
240218_173149:cmsbot_crab_voGroup
240218_173151:cmsbot_crab_scheddName
240218_173153:cmsbot_crab_collector
240218_173155:cmsbot_crab_extraJDL
```

Finished at: 2024-02-18 18:32:47
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/714/console)

## Comment (cmsdmwmbot, 2024-02-18T17:55:39Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-18 18:55:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/771/console

```
{'TN': '240218_173158:cmsbot_crab_20240218_183158', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173200:cmsbot_crab_20240218_183200', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173202:cmsbot_crab_20240218_183202', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173205:cmsbot_crab_20240218_183204', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173207:cmsbot_crab_20240218_183206', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173230:cmsbot_crab_20240218_183208', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173233:cmsbot_crab_rucio_transfers_20240218_183231', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173235:cmsbot_crab_rucio_transfers_group_20240218_183234', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173237:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240218_183236', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173240:cmsbot_crab_rucio_transfers_nopublication_20240218_183239', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173243:cmsbot_crab_rucio_transfers_withnoneedm_20240218_183242', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173246:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240218_183245', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-18T18:01:05Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-18 19:01:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/957/console

```
RETRY TESTS:
transferLogs-check.sh 240218_173015:cmsbot_crab_transferLogs - 2
activity-check.sh 240218_173017:cmsbot_crab_activity - 2
numCores-check.sh 240218_173032:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240218_173130:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240218_173135:cmsbot_crab_runRange - 2
whitelist-check.sh 240218_173141:cmsbot_crab_whitelist - 2
blacklist-check.sh 240218_173143:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240218_173145:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240218_173013:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240218_173019:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240218_173021:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240218_173025:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240218_173028:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240218_173030:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240218_173034:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240218_173036:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240218_173039:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240218_173119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240218_173121:cmsbot_crab_inputDBS - 0
useParent-check.sh 240218_173123:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240218_173125:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240218_173127:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240218_173133:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240218_173137:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240218_173139:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240218_173147:cmsbot_crab_voRole - 0
voGroup-check.sh 240218_173149:cmsbot_crab_voGroup - 0
scheddName-check.sh 240218_173151:cmsbot_crab_scheddName - 0
collector-check.sh 240218_173153:cmsbot_crab_collector - 0
extraJDL-check.sh 240218_173155:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240218_173023:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-18T18:12:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-02-18 19:12:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/772/console

```
{'TN': '240218_173158:cmsbot_crab_20240218_183158', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173200:cmsbot_crab_20240218_183200', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173202:cmsbot_crab_20240218_183202', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173205:cmsbot_crab_20240218_183204', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173207:cmsbot_crab_20240218_183206', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 98, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173230:cmsbot_crab_20240218_183208', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173233:cmsbot_crab_rucio_transfers_20240218_183231', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 36, 'transferring': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173235:cmsbot_crab_rucio_transfers_group_20240218_183234', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173237:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240218_183236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173240:cmsbot_crab_rucio_transfers_nopublication_20240218_183239', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173243:cmsbot_crab_rucio_transfers_withnoneedm_20240218_183242', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 22, 'transferring': 18}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173246:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240218_183245', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 26, 'transferring': 14}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-18T18:25:23Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-02-18 19:25:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/958/console

```
RETRY TESTS:
numCores-check.sh 240218_173032:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240218_173013:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240218_173015:cmsbot_crab_transferLogs - 0
activity-check.sh 240218_173017:cmsbot_crab_activity - 0
inputFiles-check.sh 240218_173019:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240218_173021:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240218_173023:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240218_173025:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240218_173028:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240218_173030:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240218_173034:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240218_173036:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240218_173039:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240218_173119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240218_173121:cmsbot_crab_inputDBS - 0
useParent-check.sh 240218_173123:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240218_173125:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240218_173127:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240218_173130:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240218_173133:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240218_173135:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240218_173137:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240218_173139:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240218_173141:cmsbot_crab_whitelist - 0
blacklist-check.sh 240218_173143:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240218_173145:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240218_173147:cmsbot_crab_voRole - 0
voGroup-check.sh 240218_173149:cmsbot_crab_voGroup - 0
scheddName-check.sh 240218_173151:cmsbot_crab_scheddName - 0
collector-check.sh 240218_173153:cmsbot_crab_collector - 0
extraJDL-check.sh 240218_173155:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-18T18:50:50Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-02-18 19:50:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/959/console

```
RETRY TESTS:
numCores-check.sh 240218_173032:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240218_173013:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240218_173015:cmsbot_crab_transferLogs - 0
activity-check.sh 240218_173017:cmsbot_crab_activity - 0
inputFiles-check.sh 240218_173019:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240218_173021:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240218_173023:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240218_173025:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240218_173028:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240218_173030:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240218_173034:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240218_173036:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240218_173039:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240218_173119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240218_173121:cmsbot_crab_inputDBS - 0
useParent-check.sh 240218_173123:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240218_173125:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240218_173127:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240218_173130:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240218_173133:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240218_173135:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240218_173137:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240218_173139:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240218_173141:cmsbot_crab_whitelist - 0
blacklist-check.sh 240218_173143:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240218_173145:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240218_173147:cmsbot_crab_voRole - 0
voGroup-check.sh 240218_173149:cmsbot_crab_voGroup - 0
scheddName-check.sh 240218_173151:cmsbot_crab_scheddName - 0
collector-check.sh 240218_173153:cmsbot_crab_collector - 0
extraJDL-check.sh 240218_173155:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-18T18:59:38Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-02-18 19:59:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/773/console

```
{'TN': '240218_173158:cmsbot_crab_20240218_183158', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 988, 'transferring': 12}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240218_173200:cmsbot_crab_20240218_183200', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240218_173202:cmsbot_crab_20240218_183202', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240218_173205:cmsbot_crab_20240218_183204', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/5/5'}
{'TN': '240218_173207:cmsbot_crab_20240218_183206', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240218_173230:cmsbot_crab_20240218_183208', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240218_173233:cmsbot_crab_rucio_transfers_20240218_183231', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '240218_173235:cmsbot_crab_rucio_transfers_group_20240218_183234', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240218_173237:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240218_183236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173240:cmsbot_crab_rucio_transfers_nopublication_20240218_183239', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173243:cmsbot_crab_rucio_transfers_withnoneedm_20240218_183242', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 28, 'transferring': 12}, 'publication (fail/tdb/DBS)': '1/27/27'}
{'TN': '240218_173246:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240218_183245', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 31, 'transferring': 9}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-18T19:19:05Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-18 20:19:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/960/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240218_173013:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240218_173015:cmsbot_crab_transferLogs - 0
activity-check.sh 240218_173017:cmsbot_crab_activity - 0
inputFiles-check.sh 240218_173019:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240218_173021:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240218_173025:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240218_173028:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240218_173030:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240218_173032:cmsbot_crab_numCores - 0
scriptExe-check.sh 240218_173034:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240218_173036:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240218_173039:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240218_173119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240218_173121:cmsbot_crab_inputDBS - 0
useParent-check.sh 240218_173123:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240218_173125:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240218_173127:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240218_173130:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240218_173133:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240218_173135:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240218_173137:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240218_173139:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240218_173141:cmsbot_crab_whitelist - 0
blacklist-check.sh 240218_173143:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240218_173145:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240218_173147:cmsbot_crab_voRole - 0
voGroup-check.sh 240218_173149:cmsbot_crab_voGroup - 0
scheddName-check.sh 240218_173151:cmsbot_crab_scheddName - 0
collector-check.sh 240218_173153:cmsbot_crab_collector - 0
extraJDL-check.sh 240218_173155:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240218_173023:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-18T20:31:40Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-02-18 21:31:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/774/console

```
{'TN': '240218_173158:cmsbot_crab_20240218_183158', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240218_173200:cmsbot_crab_20240218_183200', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240218_173202:cmsbot_crab_20240218_183202', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240218_173205:cmsbot_crab_20240218_183204', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240218_173207:cmsbot_crab_20240218_183206', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240218_173230:cmsbot_crab_20240218_183208', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240218_173233:cmsbot_crab_rucio_transfers_20240218_183231', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240218_173235:cmsbot_crab_rucio_transfers_group_20240218_183234', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240218_173237:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240218_183236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173240:cmsbot_crab_rucio_transfers_nopublication_20240218_183239', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240218_173243:cmsbot_crab_rucio_transfers_withnoneedm_20240218_183242', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '3/37/37'}
{'TN': '240218_173246:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240218_183245', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-02-19T09:11:41Z)

somehow retriieving non root files from xrd-cms-global is failing in these days. Maybe a redirector problelm.
Maybe time to get PFN from Rucio and avoid the redirector. Anyhow test is good.
