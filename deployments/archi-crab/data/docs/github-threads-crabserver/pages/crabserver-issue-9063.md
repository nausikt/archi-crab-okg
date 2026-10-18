# dmwm/CRABServer issue #9063: #958: Test GH CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2025-05-06T08:06:52Z
Closed: 2025-05-07T14:02:02Z
URL: https://github.com/dmwm/CRABServer/issues/9063

## Opening post (cmsdmwmbot, 2025-05-06T08:06:52Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2025-05-06 10:06:49
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/958/)

## Comment (cmsdmwmbot, 2025-05-06T08:10:56Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
250506_080932:cmsbot_crab_20250506_100931
250506_080936:cmsbot_crab_20250506_100934
250506_080939:cmsbot_crab_20250506_100937
250506_080942:cmsbot_crab_20250506_100940
250506_080945:cmsbot_crab_20250506_100943
250506_081010:cmsbot_crab_20250506_100946
250506_081014:cmsbot_crab_rucio_transfers_20250506_101012
250506_081017:cmsbot_crab_rucio_transfers_group_20250506_101016
250506_081022:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250506_101019
250506_081026:cmsbot_crab_rucio_transfers_nopublication_20250506_101023
250506_081031:cmsbot_crab_rucio_transfers_withnoneedm_20250506_101027
250506_081034:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250506_101032
```

Task submission for **Client_Validation_Suite** successfully ended.
```
250506_080746:cmsbot_crab_20250506_100743
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250506_080759:cmsbot_crab_transferOutputs
250506_080802:cmsbot_crab_transferLogs
250506_080806:cmsbot_crab_activity
250506_080809:cmsbot_crab_inputFiles
250506_080812:cmsbot_crab_disableAutomaticOutputCollection
250506_080815:cmsbot_crab_outputFiles
250506_080818:cmsbot_crab_allowUndistributedCMSSW
250506_080821:cmsbot_crab_maxMemoryMB
250506_080824:cmsbot_crab_maxJobRuntimeMin
250506_080827:cmsbot_crab_numCores
250506_080830:cmsbot_crab_scriptExe
250506_080833:cmsbot_crab_scriptArgs
250506_080836:cmsbot_crab_sendVenvFolder
250506_080839:cmsbot_crab_sendExternalFolder
250506_080842:cmsbot_crab_inputDBS
250506_080845:cmsbot_crab_useParent
250506_080848:cmsbot_crab_secondaryInputDataset
250506_080851:cmsbot_crab_lumiMaskFile
250506_080855:cmsbot_crab_lumiMaskUrl
250506_080859:cmsbot_crab_outLFNDirBase
250506_080902:cmsbot_crab_runRange
250506_080905:cmsbot_crab_ignoreLocality
250506_080908:cmsbot_crab_userInputFiles
250506_080911:cmsbot_crab_whitelist
250506_080914:cmsbot_crab_blacklist
250506_080917:cmsbot_crab_ignoreGlobalBlacklist
250506_080920:cmsbot_crab_voGroup
250506_080923:cmsbot_crab_scheddName
250506_080926:cmsbot_crab_collector
250506_080929:cmsbot_crab_extraJDL
```

Finished at: 2025-05-06 10:10:34
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/958/console)

## Comment (cmsdmwmbot, 2025-05-06T08:33:53Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-05-06 10:33:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/620/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/620//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-05-06T08:36:28Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2025-05-06 10:36:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1291/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250506_080759:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250506_080802:cmsbot_crab_transferLogs - 0
activity-check.sh 250506_080806:cmsbot_crab_activity - 0
inputFiles-check.sh 250506_080809:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250506_080812:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250506_080815:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250506_080818:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250506_080821:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250506_080824:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250506_080827:cmsbot_crab_numCores - 0
scriptExe-check.sh 250506_080830:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250506_080833:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250506_080836:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250506_080839:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250506_080842:cmsbot_crab_inputDBS - 0
useParent-check.sh 250506_080845:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250506_080848:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250506_080851:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250506_080855:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250506_080859:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250506_080902:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250506_080905:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250506_080908:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250506_080911:cmsbot_crab_whitelist - 0
blacklist-check.sh 250506_080914:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250506_080917:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 250506_080920:cmsbot_crab_voGroup - 0
scheddName-check.sh 250506_080923:cmsbot_crab_scheddName - 0
collector-check.sh 250506_080926:cmsbot_crab_collector - 0
extraJDL-check.sh 250506_080929:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```

## Comment (cmsdmwmbot, 2025-05-06T15:19:28Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2025-05-06 17:19:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1150/console

```
{'TN': '250506_080932:cmsbot_crab_20250506_100931', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 968, 'transferring': 1, 'failed': 31}, 'publication (fail/tdb/DBS)': '0/968/968'}
{'TN': '250506_080936:cmsbot_crab_20250506_100934', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_080939:cmsbot_crab_20250506_100937', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250506_080942:cmsbot_crab_20250506_100940', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_080945:cmsbot_crab_20250506_100943', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250506_081010:cmsbot_crab_20250506_100946', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081014:cmsbot_crab_rucio_transfers_20250506_101012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081017:cmsbot_crab_rucio_transfers_group_20250506_101016', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081022:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250506_101019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081026:cmsbot_crab_rucio_transfers_nopublication_20250506_101023', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081031:cmsbot_crab_rucio_transfers_withnoneedm_20250506_101027', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081034:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250506_101032', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2025-05-06T15:35:29Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2025-05-06 17:35:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1151/console

```
{'TN': '250506_080932:cmsbot_crab_20250506_100931', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 968, 'transferring': 32}, 'publication (fail/tdb/DBS)': '0/968/968'}
{'TN': '250506_080936:cmsbot_crab_20250506_100934', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_080939:cmsbot_crab_20250506_100937', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250506_080942:cmsbot_crab_20250506_100940', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_080945:cmsbot_crab_20250506_100943', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250506_081010:cmsbot_crab_20250506_100946', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081014:cmsbot_crab_rucio_transfers_20250506_101012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081017:cmsbot_crab_rucio_transfers_group_20250506_101016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081022:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250506_101019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081026:cmsbot_crab_rucio_transfers_nopublication_20250506_101023', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081031:cmsbot_crab_rucio_transfers_withnoneedm_20250506_101027', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081034:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250506_101032', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2025-05-06T16:22:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2025-05-06 18:22:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1152/console

```
{'TN': '250506_080932:cmsbot_crab_20250506_100931', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 988, 'transferring': 12}, 'publication (fail/tdb/DBS)': '0/988/988'}
{'TN': '250506_080936:cmsbot_crab_20250506_100934', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_080939:cmsbot_crab_20250506_100937', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250506_080942:cmsbot_crab_20250506_100940', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_080945:cmsbot_crab_20250506_100943', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250506_081010:cmsbot_crab_20250506_100946', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081014:cmsbot_crab_rucio_transfers_20250506_101012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081017:cmsbot_crab_rucio_transfers_group_20250506_101016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081022:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250506_101019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081026:cmsbot_crab_rucio_transfers_nopublication_20250506_101023', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081031:cmsbot_crab_rucio_transfers_withnoneedm_20250506_101027', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081034:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250506_101032', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2025-05-06T17:54:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2025-05-06 19:54:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1153/console

```
{'TN': '250506_080932:cmsbot_crab_20250506_100931', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 988, 'transferring': 12}, 'publication (fail/tdb/DBS)': '0/988/988'}
{'TN': '250506_080936:cmsbot_crab_20250506_100934', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_080939:cmsbot_crab_20250506_100937', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250506_080942:cmsbot_crab_20250506_100940', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_080945:cmsbot_crab_20250506_100943', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250506_081010:cmsbot_crab_20250506_100946', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081014:cmsbot_crab_rucio_transfers_20250506_101012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081017:cmsbot_crab_rucio_transfers_group_20250506_101016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081022:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250506_101019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081026:cmsbot_crab_rucio_transfers_nopublication_20250506_101023', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081031:cmsbot_crab_rucio_transfers_withnoneedm_20250506_101027', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081034:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250506_101032', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2025-05-06T19:55:28Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2025-05-06 21:55:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1154/console

```
{'TN': '250506_080932:cmsbot_crab_20250506_100931', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 988, 'transferring': 12}, 'publication (fail/tdb/DBS)': '0/988/988'}
{'TN': '250506_080936:cmsbot_crab_20250506_100934', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_080939:cmsbot_crab_20250506_100937', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250506_080942:cmsbot_crab_20250506_100940', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_080945:cmsbot_crab_20250506_100943', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250506_081010:cmsbot_crab_20250506_100946', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081014:cmsbot_crab_rucio_transfers_20250506_101012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081017:cmsbot_crab_rucio_transfers_group_20250506_101016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081022:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250506_101019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081026:cmsbot_crab_rucio_transfers_nopublication_20250506_101023', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081031:cmsbot_crab_rucio_transfers_withnoneedm_20250506_101027', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081034:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250506_101032', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2025-05-06T21:56:27Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2025-05-06 23:56:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1155/console

```
{'TN': '250506_080932:cmsbot_crab_20250506_100931', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 988, 'transferring': 12}, 'publication (fail/tdb/DBS)': '0/988/988'}
{'TN': '250506_080936:cmsbot_crab_20250506_100934', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_080939:cmsbot_crab_20250506_100937', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250506_080942:cmsbot_crab_20250506_100940', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_080945:cmsbot_crab_20250506_100943', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250506_081010:cmsbot_crab_20250506_100946', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081014:cmsbot_crab_rucio_transfers_20250506_101012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081017:cmsbot_crab_rucio_transfers_group_20250506_101016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081022:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250506_101019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081026:cmsbot_crab_rucio_transfers_nopublication_20250506_101023', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081031:cmsbot_crab_rucio_transfers_withnoneedm_20250506_101027', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081034:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250506_101032', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2025-05-07T11:02:35Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 0. Exceeded configured retries. If needed restart manually.
**Finished at:** 2025-05-07 13:02:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1156/console

```
{'TN': '250506_080932:cmsbot_crab_20250506_100931', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 988, 'failed': 1, 'transferring': 11}, 'publication (fail/tdb/DBS)': '0/988/988'}
{'TN': '250506_080936:cmsbot_crab_20250506_100934', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'failed': 1, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_080939:cmsbot_crab_20250506_100937', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250506_080942:cmsbot_crab_20250506_100940', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_080945:cmsbot_crab_20250506_100943', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250506_081010:cmsbot_crab_20250506_100946', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081014:cmsbot_crab_rucio_transfers_20250506_101012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081017:cmsbot_crab_rucio_transfers_group_20250506_101016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081022:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250506_101019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081026:cmsbot_crab_rucio_transfers_nopublication_20250506_101023', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250506_081031:cmsbot_crab_rucio_transfers_withnoneedm_20250506_101027', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250506_081034:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250506_101032', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2025-05-07T14:02:02Z)

of the 3 still not passing tasks
- 250506_080932:cmsbot_crab_20250506_100931 some jobs are indeed failed, and transfers from JINR are apparely slow/stuck.0
- 250506_080936:cmsbot_crab_20250506_100934 everything is find from crab status. Still a bug in the test code for autom splitting ? 
- 250506_081017:cmsbot_crab_rucio_transfers_group_20250506_101016 there was a problem in Rucio rule creation https://github.com/dmwm/CRABServer/issues/9064 

all in all... test OK !
