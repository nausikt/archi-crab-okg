# dmwm/CRABServer issue #8609: #828: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-11T16:27:14Z
Closed: 2024-08-12T08:14:30Z
URL: https://github.com/dmwm/CRABServer/issues/8609

## Opening post (cmsdmwmbot, 2024-08-11T16:27:14Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-08-11 18:27:13
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/828/)

## Comment (cmsdmwmbot, 2024-08-11T16:29:32Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240811_162843:cmsbot_crab_20240811_182842
240811_162845:cmsbot_crab_20240811_182845
240811_162847:cmsbot_crab_20240811_182847
240811_162849:cmsbot_crab_20240811_182849
240811_162851:cmsbot_crab_20240811_182851
240811_162855:cmsbot_crab_20240811_182853
240811_162858:cmsbot_crab_rucio_transfers_20240811_182857
240811_162900:cmsbot_crab_rucio_transfers_group_20240811_182859
240811_162903:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240811_182901
240811_162905:cmsbot_crab_rucio_transfers_nopublication_20240811_182904
240811_162908:cmsbot_crab_rucio_transfers_withnoneedm_20240811_182907
240811_162911:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240811_182910
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240811_162735:cmsbot_crab_transferOutputs
240811_162737:cmsbot_crab_transferLogs
240811_162739:cmsbot_crab_activity
240811_162741:cmsbot_crab_inputFiles
240811_162743:cmsbot_crab_disableAutomaticOutputCollection
240811_162745:cmsbot_crab_outputFiles
240811_162747:cmsbot_crab_allowUndistributedCMSSW
240811_162749:cmsbot_crab_maxMemoryMB
240811_162752:cmsbot_crab_maxJobRuntimeMin
240811_162754:cmsbot_crab_numCores
240811_162756:cmsbot_crab_scriptExe
240811_162758:cmsbot_crab_scriptArgs
240811_162801:cmsbot_crab_sendVenvFolder
240811_162803:cmsbot_crab_sendExternalFolder
240811_162805:cmsbot_crab_inputDBS
240811_162807:cmsbot_crab_useParent
240811_162809:cmsbot_crab_secondaryInputDataset
240811_162811:cmsbot_crab_lumiMaskFile
240811_162814:cmsbot_crab_lumiMaskUrl
240811_162816:cmsbot_crab_outLFNDirBase
240811_162818:cmsbot_crab_runRange
240811_162821:cmsbot_crab_ignoreLocality
240811_162823:cmsbot_crab_userInputFiles
240811_162825:cmsbot_crab_whitelist
240811_162827:cmsbot_crab_blacklist
240811_162829:cmsbot_crab_ignoreGlobalBlacklist
240811_162832:cmsbot_crab_voRole
240811_162834:cmsbot_crab_voGroup
240811_162836:cmsbot_crab_scheddName
240811_162838:cmsbot_crab_collector
240811_162840:cmsbot_crab_extraJDL
```

Finished at: 2024-08-11 18:29:11
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/828/console)

## Comment (cmsdmwmbot, 2024-08-11T16:51:53Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-11 18:51:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1073/console

```
{'TN': '240811_162843:cmsbot_crab_20240811_182842', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162845:cmsbot_crab_20240811_182845', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162847:cmsbot_crab_20240811_182847', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162849:cmsbot_crab_20240811_182849', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162851:cmsbot_crab_20240811_182851', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162855:cmsbot_crab_20240811_182853', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162858:cmsbot_crab_rucio_transfers_20240811_182857', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162900:cmsbot_crab_rucio_transfers_group_20240811_182859', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162903:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240811_182901', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162905:cmsbot_crab_rucio_transfers_nopublication_20240811_182904', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162908:cmsbot_crab_rucio_transfers_withnoneedm_20240811_182907', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162911:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240811_182910', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-11T16:54:11Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-11 18:54:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1159/console

```
RETRY TESTS:
transferLogs-check.sh 240811_162737:cmsbot_crab_transferLogs - 2
activity-check.sh 240811_162739:cmsbot_crab_activity - 2
outputFiles-check.sh 240811_162745:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240811_162752:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240811_162754:cmsbot_crab_numCores - 2
scriptExe-check.sh 240811_162756:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240811_162758:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240811_162811:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240811_162814:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240811_162816:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240811_162818:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240811_162823:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240811_162825:cmsbot_crab_whitelist - 2
blacklist-check.sh 240811_162827:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240811_162829:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240811_162832:cmsbot_crab_voRole - 2
voGroup-check.sh 240811_162834:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240811_162735:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240811_162741:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240811_162743:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240811_162747:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240811_162749:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240811_162801:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240811_162803:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240811_162805:cmsbot_crab_inputDBS - 0
useParent-check.sh 240811_162807:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240811_162809:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240811_162821:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 240811_162836:cmsbot_crab_scheddName - 0
collector-check.sh 240811_162838:cmsbot_crab_collector - 0
extraJDL-check.sh 240811_162840:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-11T17:08:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-08-11 19:08:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1074/console

```
{'TN': '240811_162843:cmsbot_crab_20240811_182842', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162845:cmsbot_crab_20240811_182845', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162847:cmsbot_crab_20240811_182847', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162849:cmsbot_crab_20240811_182849', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162851:cmsbot_crab_20240811_182851', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162855:cmsbot_crab_20240811_182853', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162858:cmsbot_crab_rucio_transfers_20240811_182857', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162900:cmsbot_crab_rucio_transfers_group_20240811_182859', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162903:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240811_182901', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162905:cmsbot_crab_rucio_transfers_nopublication_20240811_182904', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162908:cmsbot_crab_rucio_transfers_withnoneedm_20240811_182907', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162911:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240811_182910', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-11T17:18:43Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-08-11 19:18:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1160/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240811_162735:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240811_162737:cmsbot_crab_transferLogs - 0
activity-check.sh 240811_162739:cmsbot_crab_activity - 0
inputFiles-check.sh 240811_162741:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240811_162743:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240811_162745:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240811_162747:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240811_162749:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240811_162752:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240811_162754:cmsbot_crab_numCores - 0
scriptExe-check.sh 240811_162756:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240811_162758:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240811_162801:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240811_162803:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240811_162805:cmsbot_crab_inputDBS - 0
useParent-check.sh 240811_162807:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240811_162809:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240811_162811:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240811_162814:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240811_162816:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240811_162818:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240811_162821:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240811_162823:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240811_162825:cmsbot_crab_whitelist - 0
blacklist-check.sh 240811_162827:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240811_162829:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240811_162832:cmsbot_crab_voRole - 0
voGroup-check.sh 240811_162834:cmsbot_crab_voGroup - 0
scheddName-check.sh 240811_162836:cmsbot_crab_scheddName - 0
collector-check.sh 240811_162838:cmsbot_crab_collector - 0
extraJDL-check.sh 240811_162840:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-08-11T17:55:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-08-11 19:55:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1075/console

```
{'TN': '240811_162843:cmsbot_crab_20240811_182842', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240811_162845:cmsbot_crab_20240811_182845', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162847:cmsbot_crab_20240811_182847', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240811_162849:cmsbot_crab_20240811_182849', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240811_162851:cmsbot_crab_20240811_182851', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240811_162855:cmsbot_crab_20240811_182853', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240811_162858:cmsbot_crab_rucio_transfers_20240811_182857', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240811_162900:cmsbot_crab_rucio_transfers_group_20240811_182859', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240811_162903:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240811_182901', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162905:cmsbot_crab_rucio_transfers_nopublication_20240811_182904', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162908:cmsbot_crab_rucio_transfers_withnoneedm_20240811_182907', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240811_162911:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240811_182910', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-11T19:27:56Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-08-11 21:27:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1076/console

```
{'TN': '240811_162843:cmsbot_crab_20240811_182842', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240811_162845:cmsbot_crab_20240811_182845', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240811_162847:cmsbot_crab_20240811_182847', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240811_162849:cmsbot_crab_20240811_182849', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240811_162851:cmsbot_crab_20240811_182851', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240811_162855:cmsbot_crab_20240811_182853', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240811_162858:cmsbot_crab_rucio_transfers_20240811_182857', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240811_162900:cmsbot_crab_rucio_transfers_group_20240811_182859', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240811_162903:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240811_182901', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162905:cmsbot_crab_rucio_transfers_nopublication_20240811_182904', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240811_162908:cmsbot_crab_rucio_transfers_withnoneedm_20240811_182907', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240811_162911:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240811_182910', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-08-12T08:14:30Z)

all OK
