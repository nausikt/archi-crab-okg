# dmwm/CRABServer issue #8330: #753: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-11T15:57:45Z
Closed: 2024-04-12T10:44:29Z
URL: https://github.com/dmwm/CRABServer/issues/8330

## Opening post (cmsdmwmbot, 2024-04-11T15:57:45Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-04-11 17:57:44
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/753/)

## Comment (cmsdmwmbot, 2024-04-11T16:01:04Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240411_155956:cmsbot_crab_20240411_175955
240411_155958:cmsbot_crab_20240411_175957
240411_160000:cmsbot_crab_20240411_180000
240411_160002:cmsbot_crab_20240411_180002
240411_160005:cmsbot_crab_20240411_180004
240411_160024:cmsbot_crab_20240411_180006
240411_160027:cmsbot_crab_rucio_transfers_20240411_180026
240411_160029:cmsbot_crab_rucio_transfers_group_20240411_180029
240411_160033:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240411_180031
240411_160036:cmsbot_crab_rucio_transfers_nopublication_20240411_180035
240411_160040:cmsbot_crab_rucio_transfers_withnoneedm_20240411_180038
240411_160042:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240411_180041
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240411_155835:cmsbot_crab_transferOutputs
240411_155838:cmsbot_crab_transferLogs
240411_155841:cmsbot_crab_activity
240411_155844:cmsbot_crab_inputFiles
240411_155846:cmsbot_crab_disableAutomaticOutputCollection
240411_155848:cmsbot_crab_outputFiles
240411_155851:cmsbot_crab_allowUndistributedCMSSW
240411_155853:cmsbot_crab_maxMemoryMB
240411_155855:cmsbot_crab_maxJobRuntimeMin
240411_155859:cmsbot_crab_numCores
240411_155902:cmsbot_crab_scriptExe
240411_155905:cmsbot_crab_scriptArgs
240411_155908:cmsbot_crab_sendVenvFolder
240411_155910:cmsbot_crab_sendExternalFolder
240411_155914:cmsbot_crab_inputDBS
240411_155918:cmsbot_crab_useParent
240411_155920:cmsbot_crab_secondaryInputDataset
240411_155922:cmsbot_crab_lumiMaskFile
240411_155924:cmsbot_crab_lumiMaskUrl
240411_155927:cmsbot_crab_outLFNDirBase
240411_155929:cmsbot_crab_runRange
240411_155931:cmsbot_crab_ignoreLocality
240411_155933:cmsbot_crab_userInputFiles
240411_155935:cmsbot_crab_whitelist
240411_155937:cmsbot_crab_blacklist
240411_155939:cmsbot_crab_ignoreGlobalBlacklist
240411_155941:cmsbot_crab_voRole
240411_155945:cmsbot_crab_voGroup
240411_155947:cmsbot_crab_scheddName
240411_155949:cmsbot_crab_collector
240411_155953:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240411_155832:cmsbot_crab_20240411_175830
```

Finished at: 2024-04-11 18:00:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/753/console)

## Comment (cmsdmwmbot, 2024-04-11T16:21:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-11 18:21:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/851/console

```
{'TN': '240411_155956:cmsbot_crab_20240411_175955', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 993, 'running': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_155958:cmsbot_crab_20240411_175957', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 1, 'finished': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160000:cmsbot_crab_20240411_180000', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160002:cmsbot_crab_20240411_180002', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160005:cmsbot_crab_20240411_180004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160024:cmsbot_crab_20240411_180006', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 8, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160027:cmsbot_crab_rucio_transfers_20240411_180026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160029:cmsbot_crab_rucio_transfers_group_20240411_180029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160033:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240411_180031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160036:cmsbot_crab_rucio_transfers_nopublication_20240411_180035', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160040:cmsbot_crab_rucio_transfers_withnoneedm_20240411_180038', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160042:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240411_180041', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-11T16:24:22Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-11 18:24:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/527/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/527//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-11T16:25:27Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-11 18:25:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1028/console

```
RETRY TESTS:
transferLogs-check.sh 240411_155838:cmsbot_crab_transferLogs - 2
activity-check.sh 240411_155841:cmsbot_crab_activity - 2
outputFiles-check.sh 240411_155848:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240411_155853:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240411_155855:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240411_155859:cmsbot_crab_numCores - 2
scriptExe-check.sh 240411_155902:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240411_155905:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240411_155922:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240411_155924:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240411_155927:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240411_155929:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240411_155933:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240411_155935:cmsbot_crab_whitelist - 2
blacklist-check.sh 240411_155937:cmsbot_crab_blacklist - 2
voRole-check.sh 240411_155941:cmsbot_crab_voRole - 2
voGroup-check.sh 240411_155945:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240411_155835:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240411_155844:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240411_155846:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240411_155851:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240411_155908:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240411_155910:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240411_155914:cmsbot_crab_inputDBS - 0
useParent-check.sh 240411_155918:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240411_155920:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240411_155931:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240411_155939:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240411_155947:cmsbot_crab_scheddName - 0
collector-check.sh 240411_155949:cmsbot_crab_collector - 0
extraJDL-check.sh 240411_155953:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-04-11T16:37:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-04-11 18:37:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/852/console

```
{'TN': '240411_155956:cmsbot_crab_20240411_175955', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 995, 'running': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_155958:cmsbot_crab_20240411_175957', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160000:cmsbot_crab_20240411_180000', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160002:cmsbot_crab_20240411_180002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160005:cmsbot_crab_20240411_180004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 92, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160024:cmsbot_crab_20240411_180006', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160027:cmsbot_crab_rucio_transfers_20240411_180026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160029:cmsbot_crab_rucio_transfers_group_20240411_180029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160033:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240411_180031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160036:cmsbot_crab_rucio_transfers_nopublication_20240411_180035', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160040:cmsbot_crab_rucio_transfers_withnoneedm_20240411_180038', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160042:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240411_180041', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-11T16:49:23Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-04-11 18:49:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1029/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240411_155835:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240411_155838:cmsbot_crab_transferLogs - 0
activity-check.sh 240411_155841:cmsbot_crab_activity - 0
inputFiles-check.sh 240411_155844:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240411_155846:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240411_155848:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240411_155851:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240411_155853:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240411_155855:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240411_155859:cmsbot_crab_numCores - 0
scriptExe-check.sh 240411_155902:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240411_155905:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240411_155908:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240411_155910:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240411_155914:cmsbot_crab_inputDBS - 0
useParent-check.sh 240411_155918:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240411_155920:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240411_155922:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240411_155924:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240411_155927:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240411_155929:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240411_155931:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240411_155933:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240411_155935:cmsbot_crab_whitelist - 0
blacklist-check.sh 240411_155937:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240411_155939:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240411_155941:cmsbot_crab_voRole - 0
voGroup-check.sh 240411_155945:cmsbot_crab_voGroup - 0
scheddName-check.sh 240411_155947:cmsbot_crab_scheddName - 0
collector-check.sh 240411_155949:cmsbot_crab_collector - 0
extraJDL-check.sh 240411_155953:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-04-11T17:25:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-04-11 19:25:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/853/console

```
{'TN': '240411_155956:cmsbot_crab_20240411_175955', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240411_155958:cmsbot_crab_20240411_175957', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160000:cmsbot_crab_20240411_180000', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240411_160002:cmsbot_crab_20240411_180002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240411_160005:cmsbot_crab_20240411_180004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 98, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/98/98'}
{'TN': '240411_160024:cmsbot_crab_20240411_180006', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240411_160027:cmsbot_crab_rucio_transfers_20240411_180026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160029:cmsbot_crab_rucio_transfers_group_20240411_180029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160033:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240411_180031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160036:cmsbot_crab_rucio_transfers_nopublication_20240411_180035', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160040:cmsbot_crab_rucio_transfers_withnoneedm_20240411_180038', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160042:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240411_180041', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-11T18:55:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-04-11 20:55:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/854/console

```
{'TN': '240411_155956:cmsbot_crab_20240411_175955', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/998/998'}
{'TN': '240411_155958:cmsbot_crab_20240411_175957', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240411_160000:cmsbot_crab_20240411_180000', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240411_160002:cmsbot_crab_20240411_180002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240411_160005:cmsbot_crab_20240411_180004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 98, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/98/98'}
{'TN': '240411_160024:cmsbot_crab_20240411_180006', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240411_160027:cmsbot_crab_rucio_transfers_20240411_180026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160029:cmsbot_crab_rucio_transfers_group_20240411_180029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160033:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240411_180031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160036:cmsbot_crab_rucio_transfers_nopublication_20240411_180035', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160040:cmsbot_crab_rucio_transfers_withnoneedm_20240411_180038', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160042:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240411_180041', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-11T20:57:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-04-11 22:57:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/855/console

```
{'TN': '240411_155956:cmsbot_crab_20240411_175955', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/998/998'}
{'TN': '240411_155958:cmsbot_crab_20240411_175957', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240411_160000:cmsbot_crab_20240411_180000', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240411_160002:cmsbot_crab_20240411_180002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240411_160005:cmsbot_crab_20240411_180004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 98, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/98/98'}
{'TN': '240411_160024:cmsbot_crab_20240411_180006', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240411_160027:cmsbot_crab_rucio_transfers_20240411_180026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160029:cmsbot_crab_rucio_transfers_group_20240411_180029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160033:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240411_180031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160036:cmsbot_crab_rucio_transfers_nopublication_20240411_180035', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160040:cmsbot_crab_rucio_transfers_withnoneedm_20240411_180038', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160042:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240411_180041', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-04-11T23:00:14Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-04-12 01:00:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/856/console

```
{'TN': '240411_155956:cmsbot_crab_20240411_175955', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/998/998'}
{'TN': '240411_155958:cmsbot_crab_20240411_175957', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240411_160000:cmsbot_crab_20240411_180000', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240411_160002:cmsbot_crab_20240411_180002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240411_160005:cmsbot_crab_20240411_180004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 98, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/98/98'}
{'TN': '240411_160024:cmsbot_crab_20240411_180006', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240411_160027:cmsbot_crab_rucio_transfers_20240411_180026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160029:cmsbot_crab_rucio_transfers_group_20240411_180029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160033:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240411_180031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160036:cmsbot_crab_rucio_transfers_nopublication_20240411_180035', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160040:cmsbot_crab_rucio_transfers_withnoneedm_20240411_180038', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240411_160042:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240411_180041', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (mapellidario, 2024-04-12T10:44:29Z)

all good, new s3 credentials are working correctly
