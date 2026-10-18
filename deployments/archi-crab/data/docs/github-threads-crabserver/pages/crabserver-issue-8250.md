# dmwm/CRABServer issue #8250: #716: Test prod CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2024-02-19T10:11:40Z
Closed: 2024-02-19T13:50:00Z
URL: https://github.com/dmwm/CRABServer/issues/8250

## Opening post (cmsdmwmbot, 2024-02-19T10:11:40Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-02-19 11:11:39
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/716/)

## Comment (cmsdmwmbot, 2024-02-19T10:13:49Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240219_101244:cmsbot_crab_20240219_111242
240219_101245:cmsbot_crab_20240219_111244
240219_101246:cmsbot_crab_20240219_111245
240219_101247:cmsbot_crab_20240219_111246
240219_101248:cmsbot_crab_20240219_111247
240219_101317:cmsbot_crab_20240219_111248
240219_101319:cmsbot_crab_rucio_transfers_20240219_111318
240219_101320:cmsbot_crab_rucio_transfers_group_20240219_111320
240219_101322:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111321
240219_101324:cmsbot_crab_rucio_transfers_nopublication_20240219_111323
240219_101326:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111324
240219_101328:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111326
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240219_101159:cmsbot_crab_transferOutputs
240219_101200:cmsbot_crab_transferLogs
240219_101201:cmsbot_crab_activity
240219_101202:cmsbot_crab_inputFiles
240219_101203:cmsbot_crab_disableAutomaticOutputCollection
240219_101204:cmsbot_crab_outputFiles
240219_101206:cmsbot_crab_allowUndistributedCMSSW
240219_101207:cmsbot_crab_maxMemoryMB
240219_101208:cmsbot_crab_maxJobRuntimeMin
240219_101209:cmsbot_crab_numCores
240219_101210:cmsbot_crab_scriptExe
240219_101211:cmsbot_crab_scriptArgs
240219_101212:cmsbot_crab_sendVenvFolder
240219_101220:cmsbot_crab_sendExternalFolder
240219_101221:cmsbot_crab_inputDBS
240219_101222:cmsbot_crab_useParent
240219_101222:cmsbot_crab_secondaryInputDataset
240219_101223:cmsbot_crab_lumiMaskFile
240219_101225:cmsbot_crab_lumiMaskUrl
240219_101230:cmsbot_crab_outLFNDirBase
240219_101231:cmsbot_crab_runRange
240219_101232:cmsbot_crab_ignoreLocality
240219_101233:cmsbot_crab_userInputFiles
240219_101234:cmsbot_crab_whitelist
240219_101235:cmsbot_crab_blacklist
240219_101236:cmsbot_crab_ignoreGlobalBlacklist
240219_101237:cmsbot_crab_voRole
240219_101238:cmsbot_crab_voGroup
240219_101239:cmsbot_crab_scheddName
240219_101240:cmsbot_crab_collector
240219_101241:cmsbot_crab_extraJDL
```

Finished at: 2024-02-19 11:13:28
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/716/console)

## Comment (cmsdmwmbot, 2024-02-19T10:36:43Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-19 11:36:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/775/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 3, 'transferring': 996, 'running': 1}, 'TN': '240219_101244:cmsbot_crab_20240219_111242', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/3/3'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'finished': 5}, 'TN': '240219_101245:cmsbot_crab_20240219_111244', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240219_101246:cmsbot_crab_20240219_111245', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 2, 'transferring': 8}, 'TN': '240219_101247:cmsbot_crab_20240219_111246', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 98, 'finished': 1}, 'TN': '240219_101248:cmsbot_crab_20240219_111247', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'transferring': 8}, 'TN': '240219_101317:cmsbot_crab_20240219_111248', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101319:cmsbot_crab_rucio_transfers_20240219_111318', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101320:cmsbot_crab_rucio_transfers_group_20240219_111320', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101322:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111321', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101324:cmsbot_crab_rucio_transfers_nopublication_20240219_111323', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101326:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111324', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101328:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111326', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-19T10:42:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-19 11:42:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/962/console

```
RETRY TESTS:
lumiMaskFile-check.sh 240219_101223:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240219_101225:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240219_101231:cmsbot_crab_runRange - 2
whitelist-check.sh 240219_101234:cmsbot_crab_whitelist - 2
blacklist-check.sh 240219_101235:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240219_101159:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240219_101200:cmsbot_crab_transferLogs - 0
activity-check.sh 240219_101201:cmsbot_crab_activity - 0
inputFiles-check.sh 240219_101202:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240219_101203:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240219_101206:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240219_101207:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240219_101208:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240219_101209:cmsbot_crab_numCores - 0
scriptExe-check.sh 240219_101210:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240219_101211:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240219_101212:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240219_101220:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240219_101221:cmsbot_crab_inputDBS - 0
useParent-check.sh 240219_101222:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240219_101222:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240219_101230:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240219_101232:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240219_101233:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240219_101236:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240219_101237:cmsbot_crab_voRole - 0
voGroup-check.sh 240219_101238:cmsbot_crab_voGroup - 0
scheddName-check.sh 240219_101239:cmsbot_crab_scheddName - 0
collector-check.sh 240219_101240:cmsbot_crab_collector - 0
extraJDL-check.sh 240219_101241:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240219_101204:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-19T10:53:41Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-02-19 11:53:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/777/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 993}, 'TN': '240219_101244:cmsbot_crab_20240219_111242', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/3/3'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '240219_101245:cmsbot_crab_20240219_111244', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240219_101246:cmsbot_crab_20240219_111245', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 2, 'transferring': 8}, 'TN': '240219_101247:cmsbot_crab_20240219_111246', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 98, 'finished': 1}, 'TN': '240219_101248:cmsbot_crab_20240219_111247', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240219_101317:cmsbot_crab_20240219_111248', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101319:cmsbot_crab_rucio_transfers_20240219_111318', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101320:cmsbot_crab_rucio_transfers_group_20240219_111320', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101322:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111321', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101324:cmsbot_crab_rucio_transfers_nopublication_20240219_111323', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101326:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111324', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240219_101328:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111326', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-19T11:09:06Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-19 12:09:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/965/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240219_101159:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240219_101200:cmsbot_crab_transferLogs - 0
activity-check.sh 240219_101201:cmsbot_crab_activity - 0
inputFiles-check.sh 240219_101202:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240219_101203:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240219_101206:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240219_101207:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240219_101208:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240219_101209:cmsbot_crab_numCores - 0
scriptExe-check.sh 240219_101210:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240219_101211:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240219_101212:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240219_101220:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240219_101221:cmsbot_crab_inputDBS - 0
useParent-check.sh 240219_101222:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240219_101222:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240219_101223:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240219_101225:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240219_101230:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240219_101231:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240219_101232:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240219_101233:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240219_101234:cmsbot_crab_whitelist - 0
blacklist-check.sh 240219_101235:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240219_101236:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240219_101237:cmsbot_crab_voRole - 0
voGroup-check.sh 240219_101238:cmsbot_crab_voGroup - 0
scheddName-check.sh 240219_101239:cmsbot_crab_scheddName - 0
collector-check.sh 240219_101240:cmsbot_crab_collector - 0
extraJDL-check.sh 240219_101241:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240219_101204:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-02-19T11:39:31Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-02-19 12:39:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/779/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 969, 'transferring': 31}, 'TN': '240219_101244:cmsbot_crab_20240219_111242', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/903/903'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'finished': 6}, 'TN': '240219_101245:cmsbot_crab_20240219_111244', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240219_101246:cmsbot_crab_20240219_111245', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101247:cmsbot_crab_20240219_111246', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/2/2'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 89, 'transferring': 11}, 'TN': '240219_101248:cmsbot_crab_20240219_111247', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/15/15'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101317:cmsbot_crab_20240219_111248', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'TN': '240219_101319:cmsbot_crab_rucio_transfers_20240219_111318', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101320:cmsbot_crab_rucio_transfers_group_20240219_111320', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101322:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111321', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101324:cmsbot_crab_rucio_transfers_nopublication_20240219_111323', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101326:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111324', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'TN': '240219_101328:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111326', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-19T13:10:33Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-02-19 14:10:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/781/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240219_101244:cmsbot_crab_20240219_111242', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '240219_101245:cmsbot_crab_20240219_111244', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240219_101246:cmsbot_crab_20240219_111245', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101247:cmsbot_crab_20240219_111246', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240219_101248:cmsbot_crab_20240219_111247', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240219_101317:cmsbot_crab_20240219_111248', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101319:cmsbot_crab_rucio_transfers_20240219_111318', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101320:cmsbot_crab_rucio_transfers_group_20240219_111320', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101322:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240219_111321', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101324:cmsbot_crab_rucio_transfers_nopublication_20240219_111323', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101326:cmsbot_crab_rucio_transfers_withnoneedm_20240219_111324', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240219_101328:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240219_111326', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-02-19T13:50:00Z)

all OK
