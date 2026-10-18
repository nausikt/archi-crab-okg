# dmwm/CRABServer issue #8304: #736: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-26T15:16:24Z
Closed: 2024-03-26T19:37:59Z
URL: https://github.com/dmwm/CRABServer/issues/8304

## Opening post (cmsdmwmbot, 2024-03-26T15:16:24Z)

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

Started at: 2024-03-26 16:16:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/736/)

## Comment (cmsdmwmbot, 2024-03-26T15:19:37Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240326_151846:cmsbot_crab_20240326_161845
240326_151848:cmsbot_crab_20240326_161847
240326_151850:cmsbot_crab_20240326_161849
240326_151852:cmsbot_crab_20240326_161851
240326_151854:cmsbot_crab_20240326_161854
240326_151858:cmsbot_crab_20240326_161856
240326_151901:cmsbot_crab_rucio_transfers_20240326_161859
240326_151903:cmsbot_crab_rucio_transfers_group_20240326_161903
240326_151906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_161905
240326_151910:cmsbot_crab_rucio_transfers_nopublication_20240326_161908
240326_151913:cmsbot_crab_rucio_transfers_withnoneedm_20240326_161911
240326_151916:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_161914
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240326_151653:cmsbot_crab_transferOutputs
240326_151656:cmsbot_crab_transferLogs
240326_151658:cmsbot_crab_activity
240326_151700:cmsbot_crab_inputFiles
240326_151702:cmsbot_crab_disableAutomaticOutputCollection
240326_151704:cmsbot_crab_outputFiles
240326_151707:cmsbot_crab_allowUndistributedCMSSW
240326_151709:cmsbot_crab_maxMemoryMB
240326_151711:cmsbot_crab_maxJobRuntimeMin
240326_151713:cmsbot_crab_numCores
240326_151715:cmsbot_crab_scriptExe
240326_151718:cmsbot_crab_scriptArgs
240326_151720:cmsbot_crab_sendVenvFolder
240326_151804:cmsbot_crab_sendExternalFolder
240326_151806:cmsbot_crab_inputDBS
240326_151809:cmsbot_crab_useParent
240326_151811:cmsbot_crab_secondaryInputDataset
240326_151814:cmsbot_crab_lumiMaskFile
240326_151816:cmsbot_crab_lumiMaskUrl
240326_151819:cmsbot_crab_outLFNDirBase
240326_151821:cmsbot_crab_runRange
240326_151824:cmsbot_crab_ignoreLocality
240326_151826:cmsbot_crab_userInputFiles
240326_151828:cmsbot_crab_whitelist
240326_151830:cmsbot_crab_blacklist
240326_151832:cmsbot_crab_ignoreGlobalBlacklist
240326_151834:cmsbot_crab_voRole
240326_151836:cmsbot_crab_voGroup
240326_151839:cmsbot_crab_scheddName
240326_151841:cmsbot_crab_collector
240326_151843:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240326_151644:cmsbot_crab_20240326_161643
```

Finished at: 2024-03-26 16:19:16
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/736/console)

## Comment (cmsdmwmbot, 2024-03-26T15:42:10Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-26 16:42:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/839/console

```
{'TN': '240326_151846:cmsbot_crab_20240326_161845', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151848:cmsbot_crab_20240326_161847', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151850:cmsbot_crab_20240326_161849', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151852:cmsbot_crab_20240326_161851', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151854:cmsbot_crab_20240326_161854', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151858:cmsbot_crab_20240326_161856', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151901:cmsbot_crab_rucio_transfers_20240326_161859', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 1, 'transferring': 39}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151903:cmsbot_crab_rucio_transfers_group_20240326_161903', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_161905', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151910:cmsbot_crab_rucio_transfers_nopublication_20240326_161908', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151913:cmsbot_crab_rucio_transfers_withnoneedm_20240326_161911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151916:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_161914', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T15:44:29Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-03-26 16:44:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/514/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/514//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-03-26T15:44:47Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-26 16:44:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/992/console

```
RETRY TESTS:
activity-check.sh 240326_151658:cmsbot_crab_activity - 2
outputFiles-check.sh 240326_151704:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240326_151709:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240326_151711:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240326_151713:cmsbot_crab_numCores - 2
scriptExe-check.sh 240326_151715:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240326_151718:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240326_151816:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240326_151819:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240326_151821:cmsbot_crab_runRange - 2
whitelist-check.sh 240326_151828:cmsbot_crab_whitelist - 2
blacklist-check.sh 240326_151830:cmsbot_crab_blacklist - 2
voRole-check.sh 240326_151834:cmsbot_crab_voRole - 2
voGroup-check.sh 240326_151836:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_151653:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_151656:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240326_151700:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_151702:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240326_151707:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240326_151720:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_151804:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_151806:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_151809:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_151811:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_151814:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240326_151824:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240326_151826:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240326_151832:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240326_151839:cmsbot_crab_scheddName - 0
collector-check.sh 240326_151841:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_151843:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-26T15:59:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-26 16:59:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/842/console

```
{'TN': '240326_151846:cmsbot_crab_20240326_161845', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 997, 'finished': 1, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151848:cmsbot_crab_20240326_161847', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151850:cmsbot_crab_20240326_161849', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151852:cmsbot_crab_20240326_161851', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151854:cmsbot_crab_20240326_161854', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 7, 'finished': 92, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151858:cmsbot_crab_20240326_161856', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151901:cmsbot_crab_rucio_transfers_20240326_161859', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1, 'finished': 39}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151903:cmsbot_crab_rucio_transfers_group_20240326_161903', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_161905', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151910:cmsbot_crab_rucio_transfers_nopublication_20240326_161908', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151913:cmsbot_crab_rucio_transfers_withnoneedm_20240326_161911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151916:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_161914', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T16:09:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-03-26 17:09:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/995/console

```
RETRY TESTS:
blacklist-check.sh 240326_151830:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_151653:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_151656:cmsbot_crab_transferLogs - 0
activity-check.sh 240326_151658:cmsbot_crab_activity - 0
inputFiles-check.sh 240326_151700:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_151702:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240326_151704:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240326_151707:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240326_151709:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240326_151711:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240326_151713:cmsbot_crab_numCores - 0
scriptExe-check.sh 240326_151715:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240326_151718:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240326_151720:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_151804:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_151806:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_151809:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_151811:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_151814:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240326_151816:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240326_151819:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240326_151821:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240326_151824:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240326_151826:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240326_151828:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240326_151832:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240326_151834:cmsbot_crab_voRole - 0
voGroup-check.sh 240326_151836:cmsbot_crab_voGroup - 0
scheddName-check.sh 240326_151839:cmsbot_crab_scheddName - 0
collector-check.sh 240326_151841:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_151843:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-26T16:33:11Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-03-26 17:33:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/998/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240326_151653:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240326_151656:cmsbot_crab_transferLogs - 0
activity-check.sh 240326_151658:cmsbot_crab_activity - 0
inputFiles-check.sh 240326_151700:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240326_151702:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240326_151704:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240326_151707:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240326_151709:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240326_151711:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240326_151713:cmsbot_crab_numCores - 0
scriptExe-check.sh 240326_151715:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240326_151718:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240326_151720:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240326_151804:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240326_151806:cmsbot_crab_inputDBS - 0
useParent-check.sh 240326_151809:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240326_151811:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240326_151814:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240326_151816:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240326_151819:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240326_151821:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240326_151824:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240326_151826:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240326_151828:cmsbot_crab_whitelist - 0
blacklist-check.sh 240326_151830:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240326_151832:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240326_151834:cmsbot_crab_voRole - 0
voGroup-check.sh 240326_151836:cmsbot_crab_voGroup - 0
scheddName-check.sh 240326_151839:cmsbot_crab_scheddName - 0
collector-check.sh 240326_151841:cmsbot_crab_collector - 0
extraJDL-check.sh 240326_151843:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-26T16:44:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-26 17:44:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/845/console

```
{'TN': '240326_151846:cmsbot_crab_20240326_161845', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240326_151848:cmsbot_crab_20240326_161847', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/1'}
{'TN': '240326_151850:cmsbot_crab_20240326_161849', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240326_151852:cmsbot_crab_20240326_161851', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240326_151854:cmsbot_crab_20240326_161854', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240326_151858:cmsbot_crab_20240326_161856', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240326_151901:cmsbot_crab_rucio_transfers_20240326_161859', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_151903:cmsbot_crab_rucio_transfers_group_20240326_161903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_151906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_161905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151910:cmsbot_crab_rucio_transfers_nopublication_20240326_161908', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151913:cmsbot_crab_rucio_transfers_withnoneedm_20240326_161911', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_151916:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_161914', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-26T18:18:57Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-03-26 19:18:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/848/console

```
{'TN': '240326_151846:cmsbot_crab_20240326_161845', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240326_151848:cmsbot_crab_20240326_161847', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240326_151850:cmsbot_crab_20240326_161849', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240326_151852:cmsbot_crab_20240326_161851', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240326_151854:cmsbot_crab_20240326_161854', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240326_151858:cmsbot_crab_20240326_161856', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240326_151901:cmsbot_crab_rucio_transfers_20240326_161859', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_151903:cmsbot_crab_rucio_transfers_group_20240326_161903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_151906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240326_161905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151910:cmsbot_crab_rucio_transfers_nopublication_20240326_161908', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240326_151913:cmsbot_crab_rucio_transfers_withnoneedm_20240326_161911', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240326_151916:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240326_161914', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-03-26T19:37:59Z)

All OK
