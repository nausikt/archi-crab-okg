# dmwm/CRABServer issue #8181: #678: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-12T15:15:48Z
Closed: 2024-01-13T09:41:26Z
URL: https://github.com/dmwm/CRABServer/issues/8181

## Opening post (cmsdmwmbot, 2024-01-12T15:15:48Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-01-12 16:15:47
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/678/)

## Comment (cmsdmwmbot, 2024-01-12T15:19:05Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240112_151810:cmsbot_crab_20240112_161809
240112_151812:cmsbot_crab_20240112_161812
240112_151814:cmsbot_crab_20240112_161814
240112_151817:cmsbot_crab_20240112_161816
240112_151819:cmsbot_crab_20240112_161819
240112_151824:cmsbot_crab_20240112_161821
240112_151828:cmsbot_crab_rucio_transfers_20240112_161826
240112_151830:cmsbot_crab_rucio_transfers_group_20240112_161830
240112_151833:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_161832
240112_151836:cmsbot_crab_rucio_transfers_nopublication_20240112_161835
240112_151840:cmsbot_crab_rucio_transfers_withnoneedm_20240112_161838
240112_151843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_161842
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240112_151613:cmsbot_crab_transferOutputs
240112_151616:cmsbot_crab_transferLogs
240112_151618:cmsbot_crab_activity
240112_151621:cmsbot_crab_inputFiles
240112_151623:cmsbot_crab_disableAutomaticOutputCollection
240112_151625:cmsbot_crab_outputFiles
240112_151628:cmsbot_crab_allowUndistributedCMSSW
240112_151630:cmsbot_crab_maxMemoryMB
240112_151632:cmsbot_crab_maxJobRuntimeMin
240112_151635:cmsbot_crab_numCores
240112_151637:cmsbot_crab_scriptExe
240112_151639:cmsbot_crab_scriptArgs
240112_151641:cmsbot_crab_sendVenvFolder
240112_151726:cmsbot_crab_sendExternalFolder
240112_151728:cmsbot_crab_inputDBS
240112_151731:cmsbot_crab_useParent
240112_151733:cmsbot_crab_secondaryInputDataset
240112_151735:cmsbot_crab_lumiMaskFile
240112_151738:cmsbot_crab_lumiMaskUrl
240112_151741:cmsbot_crab_outLFNDirBase
240112_151743:cmsbot_crab_runRange
240112_151746:cmsbot_crab_ignoreLocality
240112_151748:cmsbot_crab_userInputFiles
240112_151750:cmsbot_crab_whitelist
240112_151753:cmsbot_crab_blacklist
240112_151755:cmsbot_crab_ignoreGlobalBlacklist
240112_151757:cmsbot_crab_voRole
240112_151800:cmsbot_crab_voGroup
240112_151802:cmsbot_crab_scheddName
240112_151804:cmsbot_crab_collector
240112_151807:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240112_151611:cmsbot_crab_20240112_161608
```

Finished at: 2024-01-12 16:18:44
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/678/console)

## Comment (cmsdmwmbot, 2024-01-12T15:40:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-12 16:39:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/707/console

```
{'TN': '240112_151810:cmsbot_crab_20240112_161809', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 972, 'running': 27, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151812:cmsbot_crab_20240112_161812', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151814:cmsbot_crab_20240112_161814', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151817:cmsbot_crab_20240112_161816', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151819:cmsbot_crab_20240112_161819', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 89, 'running': 10, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151824:cmsbot_crab_20240112_161821', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 6, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151828:cmsbot_crab_rucio_transfers_20240112_161826', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151830:cmsbot_crab_rucio_transfers_group_20240112_161830', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151833:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_161832', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151836:cmsbot_crab_rucio_transfers_nopublication_20240112_161835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 37, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151840:cmsbot_crab_rucio_transfers_withnoneedm_20240112_161838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_161842', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T15:42:21Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-12 16:42:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/496/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/496//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-12T15:43:23Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-12 16:43:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/887/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240112_151738:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240112_151743:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240112_151748:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240112_151750:cmsbot_crab_whitelist - 2
blacklist-check.sh 240112_151753:cmsbot_crab_blacklist - 2
voRole-check.sh 240112_151757:cmsbot_crab_voRole - 2
voGroup-check.sh 240112_151800:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240112_151613:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240112_151616:cmsbot_crab_transferLogs - 0
activity-check.sh 240112_151618:cmsbot_crab_activity - 0
inputFiles-check.sh 240112_151621:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240112_151623:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240112_151625:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240112_151628:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240112_151630:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240112_151632:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240112_151635:cmsbot_crab_numCores - 0
scriptExe-check.sh 240112_151637:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240112_151639:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240112_151641:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240112_151726:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240112_151728:cmsbot_crab_inputDBS - 0
useParent-check.sh 240112_151731:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240112_151733:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240112_151735:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240112_151741:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240112_151746:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240112_151755:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240112_151802:cmsbot_crab_scheddName - 0
collector-check.sh 240112_151804:cmsbot_crab_collector - 0
extraJDL-check.sh 240112_151807:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-12T15:55:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-01-12 16:55:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/708/console

```
{'TN': '240112_151810:cmsbot_crab_20240112_161809', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151812:cmsbot_crab_20240112_161812', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151814:cmsbot_crab_20240112_161814', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151817:cmsbot_crab_20240112_161816', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151819:cmsbot_crab_20240112_161819', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 98, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151824:cmsbot_crab_20240112_161821', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 8, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151828:cmsbot_crab_rucio_transfers_20240112_161826', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151830:cmsbot_crab_rucio_transfers_group_20240112_161830', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151833:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_161832', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151836:cmsbot_crab_rucio_transfers_nopublication_20240112_161835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151840:cmsbot_crab_rucio_transfers_withnoneedm_20240112_161838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_161842', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T16:07:32Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-01-12 17:07:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/888/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240112_151613:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240112_151616:cmsbot_crab_transferLogs - 0
activity-check.sh 240112_151618:cmsbot_crab_activity - 0
inputFiles-check.sh 240112_151621:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240112_151623:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240112_151625:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240112_151628:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240112_151630:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240112_151632:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240112_151635:cmsbot_crab_numCores - 0
scriptExe-check.sh 240112_151637:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240112_151639:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240112_151641:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240112_151726:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240112_151728:cmsbot_crab_inputDBS - 0
useParent-check.sh 240112_151731:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240112_151733:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240112_151735:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240112_151738:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240112_151741:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240112_151743:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240112_151746:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240112_151748:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240112_151750:cmsbot_crab_whitelist - 0
blacklist-check.sh 240112_151753:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240112_151755:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240112_151757:cmsbot_crab_voRole - 0
voGroup-check.sh 240112_151800:cmsbot_crab_voGroup - 0
scheddName-check.sh 240112_151802:cmsbot_crab_scheddName - 0
collector-check.sh 240112_151804:cmsbot_crab_collector - 0
extraJDL-check.sh 240112_151807:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-12T16:41:53Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-01-12 17:41:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/711/console

```
{'TN': '240112_151810:cmsbot_crab_20240112_161809', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240112_151812:cmsbot_crab_20240112_161812', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_151814:cmsbot_crab_20240112_161814', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_151817:cmsbot_crab_20240112_161816', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_151819:cmsbot_crab_20240112_161819', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240112_151824:cmsbot_crab_20240112_161821', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240112_151828:cmsbot_crab_rucio_transfers_20240112_161826', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/38'}
{'TN': '240112_151830:cmsbot_crab_rucio_transfers_group_20240112_161830', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151833:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_161832', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151836:cmsbot_crab_rucio_transfers_nopublication_20240112_161835', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151840:cmsbot_crab_rucio_transfers_withnoneedm_20240112_161838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/38'}
{'TN': '240112_151843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_161842', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T18:13:21Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-01-12 19:13:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/713/console

```
{'TN': '240112_151810:cmsbot_crab_20240112_161809', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240112_151812:cmsbot_crab_20240112_161812', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_151814:cmsbot_crab_20240112_161814', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_151817:cmsbot_crab_20240112_161816', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_151819:cmsbot_crab_20240112_161819', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240112_151824:cmsbot_crab_20240112_161821', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_151828:cmsbot_crab_rucio_transfers_20240112_161826', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/38'}
{'TN': '240112_151830:cmsbot_crab_rucio_transfers_group_20240112_161830', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151833:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_161832', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151836:cmsbot_crab_rucio_transfers_nopublication_20240112_161835', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151840:cmsbot_crab_rucio_transfers_withnoneedm_20240112_161838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/38'}
{'TN': '240112_151843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_161842', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T20:15:21Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-01-12 21:15:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/716/console

```
{'TN': '240112_151810:cmsbot_crab_20240112_161809', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240112_151812:cmsbot_crab_20240112_161812', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_151814:cmsbot_crab_20240112_161814', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_151817:cmsbot_crab_20240112_161816', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_151819:cmsbot_crab_20240112_161819', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240112_151824:cmsbot_crab_20240112_161821', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_151828:cmsbot_crab_rucio_transfers_20240112_161826', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/38'}
{'TN': '240112_151830:cmsbot_crab_rucio_transfers_group_20240112_161830', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151833:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_161832', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151836:cmsbot_crab_rucio_transfers_nopublication_20240112_161835', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151840:cmsbot_crab_rucio_transfers_withnoneedm_20240112_161838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/38'}
{'TN': '240112_151843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_161842', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-12T22:17:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-01-12 23:17:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/719/console

```
{'TN': '240112_151810:cmsbot_crab_20240112_161809', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240112_151812:cmsbot_crab_20240112_161812', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_151814:cmsbot_crab_20240112_161814', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240112_151817:cmsbot_crab_20240112_161816', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_151819:cmsbot_crab_20240112_161819', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240112_151824:cmsbot_crab_20240112_161821', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240112_151828:cmsbot_crab_rucio_transfers_20240112_161826', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/38'}
{'TN': '240112_151830:cmsbot_crab_rucio_transfers_group_20240112_161830', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151833:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240112_161832', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151836:cmsbot_crab_rucio_transfers_nopublication_20240112_161835', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240112_151840:cmsbot_crab_rucio_transfers_withnoneedm_20240112_161838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/38'}
{'TN': '240112_151843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240112_161842', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-01-13T09:41:03Z)

OK. See https://github.com/dmwm/CRABServer/issues/8177#issuecomment-1890396454 about the task stuck in transferring
