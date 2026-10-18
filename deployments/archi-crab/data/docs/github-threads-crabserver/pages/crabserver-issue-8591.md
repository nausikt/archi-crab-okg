# dmwm/CRABServer issue #8591: #820: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-06T21:10:09Z
Closed: 2024-08-07T01:19:19Z
URL: https://github.com/dmwm/CRABServer/issues/8591

## Opening post (cmsdmwmbot, 2024-08-06T21:10:09Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-08-06 23:10:09
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/820/)

## Comment (cmsdmwmbot, 2024-08-06T21:12:59Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240806_211148:cmsbot_crab_20240806_231147
240806_211150:cmsbot_crab_20240806_231150
240806_211152:cmsbot_crab_20240806_231152
240806_211155:cmsbot_crab_20240806_231154
240806_211157:cmsbot_crab_20240806_231157
240806_211220:cmsbot_crab_20240806_231159
240806_211223:cmsbot_crab_rucio_transfers_20240806_231222
240806_211225:cmsbot_crab_rucio_transfers_group_20240806_231225
240806_211228:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240806_231227
240806_211231:cmsbot_crab_rucio_transfers_nopublication_20240806_231230
240806_211234:cmsbot_crab_rucio_transfers_withnoneedm_20240806_231233
240806_211237:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240806_231236
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240806_211033:cmsbot_crab_transferOutputs
240806_211035:cmsbot_crab_transferLogs
240806_211038:cmsbot_crab_activity
240806_211040:cmsbot_crab_inputFiles
240806_211043:cmsbot_crab_disableAutomaticOutputCollection
240806_211045:cmsbot_crab_outputFiles
240806_211047:cmsbot_crab_allowUndistributedCMSSW
240806_211050:cmsbot_crab_maxMemoryMB
240806_211053:cmsbot_crab_maxJobRuntimeMin
240806_211055:cmsbot_crab_numCores
240806_211057:cmsbot_crab_scriptExe
240806_211100:cmsbot_crab_scriptArgs
240806_211102:cmsbot_crab_sendVenvFolder
240806_211104:cmsbot_crab_sendExternalFolder
240806_211107:cmsbot_crab_inputDBS
240806_211109:cmsbot_crab_useParent
240806_211111:cmsbot_crab_secondaryInputDataset
240806_211114:cmsbot_crab_lumiMaskFile
240806_211116:cmsbot_crab_lumiMaskUrl
240806_211119:cmsbot_crab_outLFNDirBase
240806_211121:cmsbot_crab_runRange
240806_211124:cmsbot_crab_ignoreLocality
240806_211126:cmsbot_crab_userInputFiles
240806_211128:cmsbot_crab_whitelist
240806_211131:cmsbot_crab_blacklist
240806_211133:cmsbot_crab_ignoreGlobalBlacklist
240806_211135:cmsbot_crab_voRole
240806_211138:cmsbot_crab_voGroup
240806_211140:cmsbot_crab_scheddName
240806_211142:cmsbot_crab_collector
240806_211145:cmsbot_crab_extraJDL
```

Finished at: 2024-08-06 23:12:38
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/820/console)

## Comment (cmsdmwmbot, 2024-08-06T21:34:22Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-06 23:34:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1049/console

```
{'TN': '240806_211148:cmsbot_crab_20240806_231147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 995, 'running': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211150:cmsbot_crab_20240806_231150', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211152:cmsbot_crab_20240806_231152', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211155:cmsbot_crab_20240806_231154', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211157:cmsbot_crab_20240806_231157', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211220:cmsbot_crab_20240806_231159', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 1, 'transferring': 9}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211223:cmsbot_crab_rucio_transfers_20240806_231222', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211225:cmsbot_crab_rucio_transfers_group_20240806_231225', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211228:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240806_231227', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211231:cmsbot_crab_rucio_transfers_nopublication_20240806_231230', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211234:cmsbot_crab_rucio_transfers_withnoneedm_20240806_231233', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211237:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240806_231236', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'cooloff': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-06T21:36:30Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-08-06 23:36:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1143/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
scheddName-check.sh 240806_211140:cmsbot_crab_scheddName - 0

FAILED TESTS:
transferOutputs-check.sh 240806_211033:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240806_211035:cmsbot_crab_transferLogs - 1
activity-check.sh 240806_211038:cmsbot_crab_activity - 1
inputFiles-check.sh 240806_211040:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240806_211043:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240806_211045:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240806_211047:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240806_211050:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240806_211053:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240806_211055:cmsbot_crab_numCores - 1
scriptExe-check.sh 240806_211057:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240806_211100:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240806_211102:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240806_211104:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240806_211107:cmsbot_crab_inputDBS - 1
useParent-check.sh 240806_211109:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240806_211111:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240806_211114:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240806_211116:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240806_211119:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240806_211121:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240806_211124:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240806_211126:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240806_211128:cmsbot_crab_whitelist - 1
blacklist-check.sh 240806_211131:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240806_211133:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240806_211135:cmsbot_crab_voRole - 1
voGroup-check.sh 240806_211138:cmsbot_crab_voGroup - 1
collector-check.sh 240806_211142:cmsbot_crab_collector - 1
extraJDL-check.sh 240806_211145:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-08-06T21:42:55Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-08-06 23:42:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1144/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
scheddName-check.sh 240806_211140:cmsbot_crab_scheddName - 0

FAILED TESTS:
transferOutputs-check.sh 240806_211033:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240806_211035:cmsbot_crab_transferLogs - 1
activity-check.sh 240806_211038:cmsbot_crab_activity - 1
inputFiles-check.sh 240806_211040:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240806_211043:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240806_211045:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240806_211047:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240806_211050:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240806_211053:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240806_211055:cmsbot_crab_numCores - 1
scriptExe-check.sh 240806_211057:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240806_211100:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240806_211102:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240806_211104:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240806_211107:cmsbot_crab_inputDBS - 1
useParent-check.sh 240806_211109:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240806_211111:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240806_211114:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240806_211116:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240806_211119:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240806_211121:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240806_211124:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240806_211126:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240806_211128:cmsbot_crab_whitelist - 1
blacklist-check.sh 240806_211131:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240806_211133:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240806_211135:cmsbot_crab_voRole - 1
voGroup-check.sh 240806_211138:cmsbot_crab_voGroup - 1
collector-check.sh 240806_211142:cmsbot_crab_collector - 1
extraJDL-check.sh 240806_211145:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-08-06T21:50:11Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-08-06 23:50:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1050/console

```
{'TN': '240806_211148:cmsbot_crab_20240806_231147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 997, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211150:cmsbot_crab_20240806_231150', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211152:cmsbot_crab_20240806_231152', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211155:cmsbot_crab_20240806_231154', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211157:cmsbot_crab_20240806_231157', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211220:cmsbot_crab_20240806_231159', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211223:cmsbot_crab_rucio_transfers_20240806_231222', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211225:cmsbot_crab_rucio_transfers_group_20240806_231225', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211228:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240806_231227', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211231:cmsbot_crab_rucio_transfers_nopublication_20240806_231230', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211234:cmsbot_crab_rucio_transfers_withnoneedm_20240806_231233', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211237:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240806_231236', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-08-06T22:00:20Z)

rats. CCV runs on "any scheduler" but only vocms059 is ready for V2 bindings.

## Comment (cmsdmwmbot, 2024-08-06T22:36:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-08-07 00:36:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1051/console

```
{'TN': '240806_211148:cmsbot_crab_20240806_231147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 53, 'transferring': 946, 'killed': 1}, 'publication (fail/tdb/DBS)': '0/51/51'}
{'TN': '240806_211150:cmsbot_crab_20240806_231150', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211152:cmsbot_crab_20240806_231152', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240806_211155:cmsbot_crab_20240806_231154', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240806_211157:cmsbot_crab_20240806_231157', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 51, 'transferring': 49}, 'publication (fail/tdb/DBS)': '0/46/46'}
{'TN': '240806_211220:cmsbot_crab_20240806_231159', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240806_211223:cmsbot_crab_rucio_transfers_20240806_231222', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211225:cmsbot_crab_rucio_transfers_group_20240806_231225', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211228:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240806_231227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211231:cmsbot_crab_rucio_transfers_nopublication_20240806_231230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211234:cmsbot_crab_rucio_transfers_withnoneedm_20240806_231233', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211237:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240806_231236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-07T00:07:06Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-08-07 02:07:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1052/console

```
{'TN': '240806_211148:cmsbot_crab_20240806_231147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 205, 'transferring': 795}, 'publication (fail/tdb/DBS)': '0/203/203'}
{'TN': '240806_211150:cmsbot_crab_20240806_231150', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240806_211152:cmsbot_crab_20240806_231152', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240806_211155:cmsbot_crab_20240806_231154', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240806_211157:cmsbot_crab_20240806_231157', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240806_211220:cmsbot_crab_20240806_231159', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240806_211223:cmsbot_crab_rucio_transfers_20240806_231222', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211225:cmsbot_crab_rucio_transfers_group_20240806_231225', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211228:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240806_231227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211231:cmsbot_crab_rucio_transfers_nopublication_20240806_231230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211234:cmsbot_crab_rucio_transfers_withnoneedm_20240806_231233', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211237:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240806_231236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-08-07T01:19:19Z)

things are working

## Comment (cmsdmwmbot, 2024-08-07T02:09:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-08-07 04:09:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1053/console

```
{'TN': '240806_211148:cmsbot_crab_20240806_231147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 413, 'transferring': 587}, 'publication (fail/tdb/DBS)': '0/403/403'}
{'TN': '240806_211150:cmsbot_crab_20240806_231150', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240806_211152:cmsbot_crab_20240806_231152', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240806_211155:cmsbot_crab_20240806_231154', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240806_211157:cmsbot_crab_20240806_231157', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240806_211220:cmsbot_crab_20240806_231159', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240806_211223:cmsbot_crab_rucio_transfers_20240806_231222', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211225:cmsbot_crab_rucio_transfers_group_20240806_231225', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211228:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240806_231227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211231:cmsbot_crab_rucio_transfers_nopublication_20240806_231230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211234:cmsbot_crab_rucio_transfers_withnoneedm_20240806_231233', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211237:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240806_231236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-07T04:09:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-08-07 06:09:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1054/console

```
{'TN': '240806_211148:cmsbot_crab_20240806_231147', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 614, 'transferring': 386}, 'publication (fail/tdb/DBS)': '0/602/602'}
{'TN': '240806_211150:cmsbot_crab_20240806_231150', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240806_211152:cmsbot_crab_20240806_231152', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240806_211155:cmsbot_crab_20240806_231154', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240806_211157:cmsbot_crab_20240806_231157', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240806_211220:cmsbot_crab_20240806_231159', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240806_211223:cmsbot_crab_rucio_transfers_20240806_231222', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211225:cmsbot_crab_rucio_transfers_group_20240806_231225', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211228:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240806_231227', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211231:cmsbot_crab_rucio_transfers_nopublication_20240806_231230', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240806_211234:cmsbot_crab_rucio_transfers_withnoneedm_20240806_231233', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240806_211237:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240806_231236', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
