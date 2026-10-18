# dmwm/CRABServer issue #8722: #842: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-26T16:57:41Z
Closed: 2024-09-26T21:31:36Z
URL: https://github.com/dmwm/CRABServer/issues/8722

## Opening post (cmsdmwmbot, 2024-09-26T16:57:41Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-09-26 18:57:40
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/842/)

## Comment (cmsdmwmbot, 2024-09-26T17:00:56Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240926_165945:cmsbot_crab_20240926_185945
240926_165948:cmsbot_crab_20240926_185947
240926_165951:cmsbot_crab_20240926_185950
240926_165953:cmsbot_crab_20240926_185953
240926_165956:cmsbot_crab_20240926_185956
240926_170014:cmsbot_crab_20240926_185958
240926_170017:cmsbot_crab_rucio_transfers_20240926_190016
240926_170020:cmsbot_crab_rucio_transfers_group_20240926_190020
240926_170023:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240926_190022
240926_170027:cmsbot_crab_rucio_transfers_nopublication_20240926_190026
240926_170030:cmsbot_crab_rucio_transfers_withnoneedm_20240926_190029
240926_170035:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240926_190033
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240926_165822:cmsbot_crab_transferOutputs
240926_165825:cmsbot_crab_transferLogs
240926_165827:cmsbot_crab_activity
240926_165830:cmsbot_crab_inputFiles
240926_165832:cmsbot_crab_disableAutomaticOutputCollection
240926_165835:cmsbot_crab_outputFiles
240926_165837:cmsbot_crab_allowUndistributedCMSSW
240926_165840:cmsbot_crab_maxMemoryMB
240926_165842:cmsbot_crab_maxJobRuntimeMin
240926_165845:cmsbot_crab_numCores
240926_165848:cmsbot_crab_scriptExe
240926_165850:cmsbot_crab_scriptArgs
240926_165853:cmsbot_crab_sendVenvFolder
240926_165856:cmsbot_crab_sendExternalFolder
240926_165859:cmsbot_crab_inputDBS
240926_165901:cmsbot_crab_useParent
240926_165904:cmsbot_crab_secondaryInputDataset
240926_165907:cmsbot_crab_lumiMaskFile
240926_165910:cmsbot_crab_lumiMaskUrl
240926_165913:cmsbot_crab_outLFNDirBase
240926_165915:cmsbot_crab_runRange
240926_165918:cmsbot_crab_ignoreLocality
240926_165921:cmsbot_crab_userInputFiles
240926_165923:cmsbot_crab_whitelist
240926_165926:cmsbot_crab_blacklist
240926_165929:cmsbot_crab_ignoreGlobalBlacklist
240926_165931:cmsbot_crab_voRole
240926_165934:cmsbot_crab_voGroup
240926_165937:cmsbot_crab_scheddName
240926_165939:cmsbot_crab_collector
240926_165942:cmsbot_crab_extraJDL
```

Finished at: 2024-09-26 19:00:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/842/console)

## Comment (cmsdmwmbot, 2024-09-26T17:22:34Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-26 19:22:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1090/console

```
{'TN': '240926_165945:cmsbot_crab_20240926_185945', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_165948:cmsbot_crab_20240926_185947', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_165951:cmsbot_crab_20240926_185950', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_165953:cmsbot_crab_20240926_185953', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_165956:cmsbot_crab_20240926_185956', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170014:cmsbot_crab_20240926_185958', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 8, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170017:cmsbot_crab_rucio_transfers_20240926_190016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170020:cmsbot_crab_rucio_transfers_group_20240926_190020', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240926_170023:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240926_190022', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170027:cmsbot_crab_rucio_transfers_nopublication_20240926_190026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170030:cmsbot_crab_rucio_transfers_withnoneedm_20240926_190029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170035:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240926_190033', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-09-26T17:26:35Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-26 19:26:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1202/console

```
RETRY TESTS:
transferLogs-check.sh 240926_165825:cmsbot_crab_transferLogs - 2
activity-check.sh 240926_165827:cmsbot_crab_activity - 2
maxJobRuntimeMin-check.sh 240926_165842:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240926_165845:cmsbot_crab_numCores - 2
scriptExe-check.sh 240926_165848:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240926_165850:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240926_165907:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240926_165910:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240926_165915:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240926_165921:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240926_165923:cmsbot_crab_whitelist - 2
blacklist-check.sh 240926_165926:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240926_165929:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240926_165931:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240926_165822:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240926_165830:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240926_165832:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240926_165835:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240926_165837:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240926_165840:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240926_165853:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240926_165856:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240926_165859:cmsbot_crab_inputDBS - 0
useParent-check.sh 240926_165901:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240926_165904:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240926_165913:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240926_165918:cmsbot_crab_ignoreLocality - 0
voGroup-check.sh 240926_165934:cmsbot_crab_voGroup - 0
scheddName-check.sh 240926_165937:cmsbot_crab_scheddName - 0
collector-check.sh 240926_165939:cmsbot_crab_collector - 0
extraJDL-check.sh 240926_165942:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-09-26T17:40:43Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-09-26 19:40:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1091/console

```
{'TN': '240926_165945:cmsbot_crab_20240926_185945', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_165948:cmsbot_crab_20240926_185947', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_165951:cmsbot_crab_20240926_185950', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_165953:cmsbot_crab_20240926_185953', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_165956:cmsbot_crab_20240926_185956', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170014:cmsbot_crab_20240926_185958', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170017:cmsbot_crab_rucio_transfers_20240926_190016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170020:cmsbot_crab_rucio_transfers_group_20240926_190020', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240926_170023:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240926_190022', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170027:cmsbot_crab_rucio_transfers_nopublication_20240926_190026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170030:cmsbot_crab_rucio_transfers_withnoneedm_20240926_190029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170035:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240926_190033', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-09-26T17:52:11Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-09-26 19:52:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1203/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240926_165822:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240926_165825:cmsbot_crab_transferLogs - 0
activity-check.sh 240926_165827:cmsbot_crab_activity - 0
inputFiles-check.sh 240926_165830:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240926_165832:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240926_165835:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240926_165837:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240926_165840:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240926_165842:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240926_165845:cmsbot_crab_numCores - 0
scriptExe-check.sh 240926_165848:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240926_165850:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240926_165853:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240926_165856:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240926_165859:cmsbot_crab_inputDBS - 0
useParent-check.sh 240926_165901:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240926_165904:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240926_165907:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240926_165910:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240926_165913:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240926_165915:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240926_165918:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240926_165921:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240926_165923:cmsbot_crab_whitelist - 0
blacklist-check.sh 240926_165926:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240926_165929:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240926_165931:cmsbot_crab_voRole - 0
voGroup-check.sh 240926_165934:cmsbot_crab_voGroup - 0
scheddName-check.sh 240926_165937:cmsbot_crab_scheddName - 0
collector-check.sh 240926_165939:cmsbot_crab_collector - 0
extraJDL-check.sh 240926_165942:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-09-26T18:28:43Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-09-26 20:28:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1092/console

```
{'TN': '240926_165945:cmsbot_crab_20240926_185945', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240926_165948:cmsbot_crab_20240926_185947', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_165951:cmsbot_crab_20240926_185950', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240926_165953:cmsbot_crab_20240926_185953', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240926_165956:cmsbot_crab_20240926_185956', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240926_170014:cmsbot_crab_20240926_185958', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240926_170017:cmsbot_crab_rucio_transfers_20240926_190016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240926_170020:cmsbot_crab_rucio_transfers_group_20240926_190020', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240926_170023:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240926_190022', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170027:cmsbot_crab_rucio_transfers_nopublication_20240926_190026', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170030:cmsbot_crab_rucio_transfers_withnoneedm_20240926_190029', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240926_170035:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240926_190033', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-09-26T20:00:45Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-09-26 22:00:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1093/console

```
{'TN': '240926_165945:cmsbot_crab_20240926_185945', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240926_165948:cmsbot_crab_20240926_185947', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240926_165951:cmsbot_crab_20240926_185950', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240926_165953:cmsbot_crab_20240926_185953', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240926_165956:cmsbot_crab_20240926_185956', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240926_170014:cmsbot_crab_20240926_185958', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240926_170017:cmsbot_crab_rucio_transfers_20240926_190016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240926_170020:cmsbot_crab_rucio_transfers_group_20240926_190020', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240926_170023:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240926_190022', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170027:cmsbot_crab_rucio_transfers_nopublication_20240926_190026', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170030:cmsbot_crab_rucio_transfers_withnoneedm_20240926_190029', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240926_170035:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240926_190033', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-09-26T21:24:13Z)

pff... again `crab_rucio_transfers_group` failed to be submitted witth
```
Error = Not enough Rucio quota at T2_IT_Legnaro:/store/group/rucio/crab_test/ruciotransfers-1727370020. Remain quota: -0.7039571069180965 GB.
```
but
```
 rucio list-account-usage crab_test_group
+----------------+------------+------------+--------------+
| RSE            | USAGE      | LIMIT      | QUOTA LEFT   |
|----------------+------------+------------+--------------|
| T1_DE_KIT_Disk | 755.868 MB | 500.000 GB | 499.244 GB   |
| T2_IT_Legnaro  | 3.837 GB   | 2.000 TB   | 1.996 TB     |
+----------------+------------+------------+--------------+
```

## Comment (belforte, 2024-09-26T21:31:36Z)

since all other tests passed, let's call it success
indeed I submitted the ST suite again and it worked
#8723

## Comment (cmsdmwmbot, 2024-09-26T22:01:41Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-09-27 00:01:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1095/console

```
{'TN': '240926_165945:cmsbot_crab_20240926_185945', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240926_165948:cmsbot_crab_20240926_185947', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240926_165951:cmsbot_crab_20240926_185950', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240926_165953:cmsbot_crab_20240926_185953', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240926_165956:cmsbot_crab_20240926_185956', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240926_170014:cmsbot_crab_20240926_185958', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240926_170017:cmsbot_crab_rucio_transfers_20240926_190016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240926_170020:cmsbot_crab_rucio_transfers_group_20240926_190020', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240926_170023:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240926_190022', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170027:cmsbot_crab_rucio_transfers_nopublication_20240926_190026', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170030:cmsbot_crab_rucio_transfers_withnoneedm_20240926_190029', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240926_170035:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240926_190033', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-09-27T00:04:34Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-09-27 02:04:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1098/console

```
{'TN': '240926_165945:cmsbot_crab_20240926_185945', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240926_165948:cmsbot_crab_20240926_185947', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240926_165951:cmsbot_crab_20240926_185950', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240926_165953:cmsbot_crab_20240926_185953', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240926_165956:cmsbot_crab_20240926_185956', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240926_170014:cmsbot_crab_20240926_185958', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240926_170017:cmsbot_crab_rucio_transfers_20240926_190016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240926_170020:cmsbot_crab_rucio_transfers_group_20240926_190020', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240926_170023:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240926_190022', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170027:cmsbot_crab_rucio_transfers_nopublication_20240926_190026', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240926_170030:cmsbot_crab_rucio_transfers_withnoneedm_20240926_190029', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240926_170035:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240926_190033', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
