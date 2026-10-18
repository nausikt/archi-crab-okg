# dmwm/CRABServer issue #8225: #705: Test prod CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2024-02-02T17:06:53Z
Closed: 2024-02-03T18:09:05Z
URL: https://github.com/dmwm/CRABServer/issues/8225

## Opening post (cmsdmwmbot, 2024-02-02T17:06:53Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-02-02 18:06:52
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/705/)

## Comment (cmsdmwmbot, 2024-02-02T17:09:36Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240202_170824:cmsbot_crab_20240202_180824
240202_170826:cmsbot_crab_20240202_180826
240202_170828:cmsbot_crab_20240202_180827
240202_170830:cmsbot_crab_20240202_180829
240202_170832:cmsbot_crab_20240202_180831
240202_170859:cmsbot_crab_20240202_180833
240202_170901:cmsbot_crab_rucio_transfers_20240202_180900
240202_170903:cmsbot_crab_rucio_transfers_group_20240202_180903
240202_170906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_180905
240202_170909:cmsbot_crab_rucio_transfers_nopublication_20240202_180908
240202_170912:cmsbot_crab_rucio_transfers_withnoneedm_20240202_180910
240202_170915:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_180913
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_170715:cmsbot_crab_transferOutputs
240202_170718:cmsbot_crab_transferLogs
240202_170720:cmsbot_crab_activity
240202_170721:cmsbot_crab_inputFiles
240202_170723:cmsbot_crab_disableAutomaticOutputCollection
240202_170725:cmsbot_crab_outputFiles
240202_170727:cmsbot_crab_allowUndistributedCMSSW
240202_170729:cmsbot_crab_maxMemoryMB
240202_170731:cmsbot_crab_maxJobRuntimeMin
240202_170733:cmsbot_crab_numCores
240202_170735:cmsbot_crab_scriptExe
240202_170737:cmsbot_crab_scriptArgs
240202_170739:cmsbot_crab_sendVenvFolder
240202_170748:cmsbot_crab_sendExternalFolder
240202_170750:cmsbot_crab_inputDBS
240202_170752:cmsbot_crab_useParent
240202_170754:cmsbot_crab_secondaryInputDataset
240202_170756:cmsbot_crab_lumiMaskFile
240202_170758:cmsbot_crab_lumiMaskUrl
240202_170801:cmsbot_crab_outLFNDirBase
240202_170802:cmsbot_crab_runRange
240202_170804:cmsbot_crab_ignoreLocality
240202_170806:cmsbot_crab_userInputFiles
240202_170808:cmsbot_crab_whitelist
240202_170810:cmsbot_crab_blacklist
240202_170812:cmsbot_crab_ignoreGlobalBlacklist
240202_170814:cmsbot_crab_voRole
240202_170816:cmsbot_crab_voGroup
240202_170818:cmsbot_crab_scheddName
240202_170820:cmsbot_crab_collector
240202_170822:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 18:09:15
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/705/console)

## Comment (cmsdmwmbot, 2024-02-02T17:30:37Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 18:30:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/748/console

```
{'TN': '240202_170824:cmsbot_crab_20240202_180824', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170826:cmsbot_crab_20240202_180826', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170828:cmsbot_crab_20240202_180827', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170830:cmsbot_crab_20240202_180829', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170832:cmsbot_crab_20240202_180831', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170859:cmsbot_crab_20240202_180833', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170901:cmsbot_crab_rucio_transfers_20240202_180900', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170903:cmsbot_crab_rucio_transfers_group_20240202_180903', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_180905', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170909:cmsbot_crab_rucio_transfers_nopublication_20240202_180908', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170912:cmsbot_crab_rucio_transfers_withnoneedm_20240202_180910', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170915:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_180913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T17:32:55Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 18:32:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/939/console

```
RETRY TESTS:
activity-check.sh 240202_170720:cmsbot_crab_activity - 2
outputFiles-check.sh 240202_170725:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240202_170731:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240202_170733:cmsbot_crab_numCores - 2
scriptExe-check.sh 240202_170735:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240202_170737:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240202_170752:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240202_170754:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240202_170756:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240202_170758:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240202_170801:cmsbot_crab_outLFNDirBase - 2
voGroup-check.sh 240202_170816:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_170715:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_170718:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240202_170721:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_170723:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240202_170727:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_170729:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240202_170739:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_170748:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_170750:cmsbot_crab_inputDBS - 0
scheddName-check.sh 240202_170818:cmsbot_crab_scheddName - 0
collector-check.sh 240202_170820:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_170822:cmsbot_crab_extraJDL - 0

FAILED TESTS:
runRange-check.sh 240202_170802:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240202_170804:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240202_170806:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240202_170808:cmsbot_crab_whitelist - 1
blacklist-check.sh 240202_170810:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240202_170812:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240202_170814:cmsbot_crab_voRole - 1
```

## Comment (cmsdmwmbot, 2024-02-02T17:46:55Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-02-02 18:46:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/749/console

```
{'TN': '240202_170824:cmsbot_crab_20240202_180824', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 992, 'finished': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170826:cmsbot_crab_20240202_180826', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170828:cmsbot_crab_20240202_180827', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170830:cmsbot_crab_20240202_180829', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170832:cmsbot_crab_20240202_180831', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 96, 'transferring': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170859:cmsbot_crab_20240202_180833', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 7, 'finished': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170901:cmsbot_crab_rucio_transfers_20240202_180900', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170903:cmsbot_crab_rucio_transfers_group_20240202_180903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_180905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170909:cmsbot_crab_rucio_transfers_nopublication_20240202_180908', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170912:cmsbot_crab_rucio_transfers_withnoneedm_20240202_180910', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170915:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_180913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T17:56:42Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-02-02 18:56:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/942/console

```
RETRY TESTS:
numCores-check.sh 240202_170733:cmsbot_crab_numCores - 2
scriptExe-check.sh 240202_170735:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240202_170737:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240202_170758:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240202_170802:cmsbot_crab_runRange - 2
whitelist-check.sh 240202_170808:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_170810:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240202_170812:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_170715:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_170718:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_170720:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_170721:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_170723:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_170725:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_170727:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_170729:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_170731:cmsbot_crab_maxJobRuntimeMin - 0
sendVenvFolder-check.sh 240202_170739:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_170748:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_170750:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_170752:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_170754:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_170756:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240202_170801:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240202_170804:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_170806:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240202_170814:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_170816:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_170818:cmsbot_crab_scheddName - 0
collector-check.sh 240202_170820:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_170822:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T18:20:43Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-02-02 19:20:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/946/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_170715:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_170718:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_170720:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_170721:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_170723:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_170725:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_170727:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_170729:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_170731:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_170733:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_170735:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_170737:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_170739:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_170748:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_170750:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_170752:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_170754:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_170756:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_170758:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_170801:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_170802:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_170804:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_170806:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_170808:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_170810:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_170812:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_170814:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_170816:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_170818:cmsbot_crab_scheddName - 0
collector-check.sh 240202_170820:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_170822:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T18:32:53Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-02-02 19:32:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/752/console

```
{'TN': '240202_170824:cmsbot_crab_20240202_180824', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240202_170826:cmsbot_crab_20240202_180826', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170828:cmsbot_crab_20240202_180827', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240202_170830:cmsbot_crab_20240202_180829', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240202_170832:cmsbot_crab_20240202_180831', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240202_170859:cmsbot_crab_20240202_180833', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240202_170901:cmsbot_crab_rucio_transfers_20240202_180900', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170903:cmsbot_crab_rucio_transfers_group_20240202_180903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_180905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170909:cmsbot_crab_rucio_transfers_nopublication_20240202_180908', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170912:cmsbot_crab_rucio_transfers_withnoneedm_20240202_180910', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170915:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_180913', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T20:04:51Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-02-02 21:04:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/754/console

```
{'TN': '240202_170824:cmsbot_crab_20240202_180824', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240202_170826:cmsbot_crab_20240202_180826', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170828:cmsbot_crab_20240202_180827', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240202_170830:cmsbot_crab_20240202_180829', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240202_170832:cmsbot_crab_20240202_180831', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240202_170859:cmsbot_crab_20240202_180833', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240202_170901:cmsbot_crab_rucio_transfers_20240202_180900', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170903:cmsbot_crab_rucio_transfers_group_20240202_180903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170906:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_180905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170909:cmsbot_crab_rucio_transfers_nopublication_20240202_180908', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170912:cmsbot_crab_rucio_transfers_withnoneedm_20240202_180910', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240202_170915:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_180913', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
