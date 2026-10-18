# dmwm/CRABServer issue #8276: #721: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-11T22:05:21Z
Closed: 2024-03-12T08:42:03Z
URL: https://github.com/dmwm/CRABServer/issues/8276

## Opening post (cmsdmwmbot, 2024-03-11T22:05:21Z)

**Validate vocms059 with new puppet code**

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-03-11 23:05:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/721/)

## Comment (cmsdmwmbot, 2024-03-11T22:09:07Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240311_220754:cmsbot_crab_20240311_230754
240311_220756:cmsbot_crab_20240311_230756
240311_220758:cmsbot_crab_20240311_230758
240311_220800:cmsbot_crab_20240311_230800
240311_220803:cmsbot_crab_20240311_230802
240311_220829:cmsbot_crab_20240311_230804
240311_220832:cmsbot_crab_rucio_transfers_20240311_230831
240311_220834:cmsbot_crab_rucio_transfers_group_20240311_230834
240311_220837:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240311_230835
240311_220840:cmsbot_crab_rucio_transfers_nopublication_20240311_230838
240311_220843:cmsbot_crab_rucio_transfers_withnoneedm_20240311_230841
240311_220845:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240311_230844
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240311_220600:cmsbot_crab_transferOutputs
240311_220602:cmsbot_crab_transferLogs
240311_220604:cmsbot_crab_activity
240311_220606:cmsbot_crab_inputFiles
240311_220608:cmsbot_crab_disableAutomaticOutputCollection
240311_220610:cmsbot_crab_outputFiles
240311_220612:cmsbot_crab_allowUndistributedCMSSW
240311_220614:cmsbot_crab_maxMemoryMB
240311_220616:cmsbot_crab_maxJobRuntimeMin
240311_220618:cmsbot_crab_numCores
240311_220620:cmsbot_crab_scriptExe
240311_220622:cmsbot_crab_scriptArgs
240311_220625:cmsbot_crab_sendVenvFolder
240311_220715:cmsbot_crab_sendExternalFolder
240311_220717:cmsbot_crab_inputDBS
240311_220719:cmsbot_crab_useParent
240311_220721:cmsbot_crab_secondaryInputDataset
240311_220723:cmsbot_crab_lumiMaskFile
240311_220726:cmsbot_crab_lumiMaskUrl
240311_220729:cmsbot_crab_outLFNDirBase
240311_220731:cmsbot_crab_runRange
240311_220733:cmsbot_crab_ignoreLocality
240311_220735:cmsbot_crab_userInputFiles
240311_220737:cmsbot_crab_whitelist
240311_220739:cmsbot_crab_blacklist
240311_220741:cmsbot_crab_ignoreGlobalBlacklist
240311_220743:cmsbot_crab_voRole
240311_220745:cmsbot_crab_voGroup
240311_220747:cmsbot_crab_scheddName
240311_220749:cmsbot_crab_collector
240311_220751:cmsbot_crab_extraJDL
```

Finished at: 2024-03-11 23:08:46
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/721/console)

## Comment (cmsdmwmbot, 2024-03-11T22:30:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-11 23:29:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/786/console

```
{'TN': '240311_220754:cmsbot_crab_20240311_230754', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220756:cmsbot_crab_20240311_230756', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220758:cmsbot_crab_20240311_230758', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220800:cmsbot_crab_20240311_230800', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220803:cmsbot_crab_20240311_230802', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220829:cmsbot_crab_20240311_230804', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220832:cmsbot_crab_rucio_transfers_20240311_230831', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220834:cmsbot_crab_rucio_transfers_group_20240311_230834', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220837:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240311_230835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220840:cmsbot_crab_rucio_transfers_nopublication_20240311_230838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220843:cmsbot_crab_rucio_transfers_withnoneedm_20240311_230841', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220845:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240311_230844', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-11T22:34:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-11 23:34:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/970/console

```
RETRY TESTS:
maxMemoryMB-check.sh 240311_220614:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240311_220616:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240311_220618:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240311_220622:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240311_220726:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240311_220731:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240311_220735:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240311_220737:cmsbot_crab_whitelist - 2
blacklist-check.sh 240311_220739:cmsbot_crab_blacklist - 2
voRole-check.sh 240311_220743:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240311_220600:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240311_220602:cmsbot_crab_transferLogs - 0
activity-check.sh 240311_220604:cmsbot_crab_activity - 0
inputFiles-check.sh 240311_220606:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240311_220608:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240311_220610:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240311_220612:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 240311_220620:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240311_220625:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240311_220715:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240311_220717:cmsbot_crab_inputDBS - 0
useParent-check.sh 240311_220719:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240311_220721:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240311_220723:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240311_220729:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240311_220733:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240311_220741:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240311_220745:cmsbot_crab_voGroup - 0
scheddName-check.sh 240311_220747:cmsbot_crab_scheddName - 0
collector-check.sh 240311_220749:cmsbot_crab_collector - 0
extraJDL-check.sh 240311_220751:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-11T22:45:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-11 23:45:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/787/console

```
{'TN': '240311_220754:cmsbot_crab_20240311_230754', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220756:cmsbot_crab_20240311_230756', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220758:cmsbot_crab_20240311_230758', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220800:cmsbot_crab_20240311_230800', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220803:cmsbot_crab_20240311_230802', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220829:cmsbot_crab_20240311_230804', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220832:cmsbot_crab_rucio_transfers_20240311_230831', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220834:cmsbot_crab_rucio_transfers_group_20240311_230834', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220837:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240311_230835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220840:cmsbot_crab_rucio_transfers_nopublication_20240311_230838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220843:cmsbot_crab_rucio_transfers_withnoneedm_20240311_230841', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220845:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240311_230844', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-11T22:58:27Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-03-11 23:58:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/971/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240311_220600:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240311_220602:cmsbot_crab_transferLogs - 0
activity-check.sh 240311_220604:cmsbot_crab_activity - 0
inputFiles-check.sh 240311_220606:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240311_220608:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240311_220610:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240311_220612:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240311_220614:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240311_220616:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240311_220618:cmsbot_crab_numCores - 0
scriptExe-check.sh 240311_220620:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240311_220622:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240311_220625:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240311_220715:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240311_220717:cmsbot_crab_inputDBS - 0
useParent-check.sh 240311_220719:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240311_220721:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240311_220723:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240311_220726:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240311_220729:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240311_220731:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240311_220733:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240311_220735:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240311_220737:cmsbot_crab_whitelist - 0
blacklist-check.sh 240311_220739:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240311_220741:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240311_220743:cmsbot_crab_voRole - 0
voGroup-check.sh 240311_220745:cmsbot_crab_voGroup - 0
scheddName-check.sh 240311_220747:cmsbot_crab_scheddName - 0
collector-check.sh 240311_220749:cmsbot_crab_collector - 0
extraJDL-check.sh 240311_220751:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-11T23:32:08Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-12 00:32:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/788/console

```
{'TN': '240311_220754:cmsbot_crab_20240311_230754', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240311_220756:cmsbot_crab_20240311_230756', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220758:cmsbot_crab_20240311_230758', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240311_220800:cmsbot_crab_20240311_230800', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240311_220803:cmsbot_crab_20240311_230802', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240311_220829:cmsbot_crab_20240311_230804', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240311_220832:cmsbot_crab_rucio_transfers_20240311_230831', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240311_220834:cmsbot_crab_rucio_transfers_group_20240311_230834', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240311_220837:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240311_230835', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220840:cmsbot_crab_rucio_transfers_nopublication_20240311_230838', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220843:cmsbot_crab_rucio_transfers_withnoneedm_20240311_230841', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240311_220845:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240311_230844', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-12T01:03:42Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-03-12 02:03:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/789/console

```
{'TN': '240311_220754:cmsbot_crab_20240311_230754', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240311_220756:cmsbot_crab_20240311_230756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240311_220758:cmsbot_crab_20240311_230758', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240311_220800:cmsbot_crab_20240311_230800', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240311_220803:cmsbot_crab_20240311_230802', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240311_220829:cmsbot_crab_20240311_230804', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240311_220832:cmsbot_crab_rucio_transfers_20240311_230831', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240311_220834:cmsbot_crab_rucio_transfers_group_20240311_230834', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240311_220837:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240311_230835', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220840:cmsbot_crab_rucio_transfers_nopublication_20240311_230838', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240311_220843:cmsbot_crab_rucio_transfers_withnoneedm_20240311_230841', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240311_220845:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240311_230844', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-03-12T08:42:03Z)

all good
