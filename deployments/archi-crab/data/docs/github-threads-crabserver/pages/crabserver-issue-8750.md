# dmwm/CRABServer issue #8750: #856: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-10-24T11:17:11Z
Closed: 2024-10-29T20:20:40Z
URL: https://github.com/dmwm/CRABServer/issues/8750

## Opening post (cmsdmwmbot, 2024-10-24T11:17:11Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-10-24 13:17:10
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/856/)

## Comment (cmsdmwmbot, 2024-10-24T11:19:54Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
241024_111856:cmsbot_crab_20241024_131856
241024_111859:cmsbot_crab_20241024_131858
241024_111901:cmsbot_crab_20241024_131901
241024_111904:cmsbot_crab_20241024_131903
241024_111906:cmsbot_crab_20241024_131905
241024_111914:cmsbot_crab_20241024_131908
241024_111918:cmsbot_crab_rucio_transfers_20241024_131916
241024_111920:cmsbot_crab_rucio_transfers_group_20241024_131920
241024_111923:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131922
241024_111926:cmsbot_crab_rucio_transfers_nopublication_20241024_131925
241024_111929:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131928
241024_111932:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131931
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
241024_111733:cmsbot_crab_transferOutputs
241024_111736:cmsbot_crab_transferLogs
241024_111738:cmsbot_crab_activity
241024_111740:cmsbot_crab_inputFiles
241024_111751:cmsbot_crab_disableAutomaticOutputCollection
241024_111753:cmsbot_crab_outputFiles
241024_111755:cmsbot_crab_allowUndistributedCMSSW
241024_111758:cmsbot_crab_maxMemoryMB
241024_111800:cmsbot_crab_maxJobRuntimeMin
241024_111802:cmsbot_crab_numCores
241024_111805:cmsbot_crab_scriptExe
241024_111807:cmsbot_crab_scriptArgs
241024_111810:cmsbot_crab_sendVenvFolder
241024_111812:cmsbot_crab_sendExternalFolder
241024_111814:cmsbot_crab_inputDBS
241024_111817:cmsbot_crab_useParent
241024_111819:cmsbot_crab_secondaryInputDataset
241024_111821:cmsbot_crab_lumiMaskFile
241024_111824:cmsbot_crab_lumiMaskUrl
241024_111827:cmsbot_crab_outLFNDirBase
241024_111829:cmsbot_crab_runRange
241024_111831:cmsbot_crab_ignoreLocality
241024_111834:cmsbot_crab_userInputFiles
241024_111837:cmsbot_crab_whitelist
241024_111839:cmsbot_crab_blacklist
241024_111842:cmsbot_crab_ignoreGlobalBlacklist
241024_111844:cmsbot_crab_voRole
241024_111846:cmsbot_crab_voGroup
241024_111849:cmsbot_crab_scheddName
241024_111851:cmsbot_crab_collector
241024_111854:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241024_111731:cmsbot_crab_20241024_131730
```

Finished at: 2024-10-24 13:19:32
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/856/console)

## Comment (cmsdmwmbot, 2024-10-24T12:15:11Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-10-24 14:15:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1103/console

```
{'TN': '241024_111856:cmsbot_crab_20241024_131856', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111859:cmsbot_crab_20241024_131858', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111901:cmsbot_crab_20241024_131901', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111904:cmsbot_crab_20241024_131903', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111906:cmsbot_crab_20241024_131905', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111914:cmsbot_crab_20241024_131908', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111918:cmsbot_crab_rucio_transfers_20241024_131916', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 32, 'finished': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111920:cmsbot_crab_rucio_transfers_group_20241024_131920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 8, 'finished': 32}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111923:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111926:cmsbot_crab_rucio_transfers_nopublication_20241024_131925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 35, 'transferring': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111929:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131928', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111932:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131931', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-10-24T12:17:44Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-10-24 14:17:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/552/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/552//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241024_131730  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Command recover failed


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241024_111731:cmsbot_crab_20241024_131730  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241024_131730/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
step kill - task already killed
Command recover failed
```

## Comment (cmsdmwmbot, 2024-10-24T12:22:49Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2024-10-24 14:22:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1209/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241024_111733:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241024_111736:cmsbot_crab_transferLogs - 0
activity-check.sh 241024_111738:cmsbot_crab_activity - 0
inputFiles-check.sh 241024_111740:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241024_111751:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241024_111753:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241024_111755:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241024_111758:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241024_111800:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241024_111802:cmsbot_crab_numCores - 0
scriptExe-check.sh 241024_111805:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241024_111807:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241024_111810:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241024_111812:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241024_111814:cmsbot_crab_inputDBS - 0
useParent-check.sh 241024_111817:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241024_111819:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241024_111821:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241024_111824:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241024_111827:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241024_111829:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241024_111831:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241024_111834:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241024_111837:cmsbot_crab_whitelist - 0
blacklist-check.sh 241024_111839:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241024_111842:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241024_111844:cmsbot_crab_voRole - 0
voGroup-check.sh 241024_111846:cmsbot_crab_voGroup - 0
scheddName-check.sh 241024_111849:cmsbot_crab_scheddName - 0
collector-check.sh 241024_111851:cmsbot_crab_collector - 0
extraJDL-check.sh 241024_111854:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-10-24T12:31:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-10-24 14:31:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1106/console

```
{'TN': '241024_111856:cmsbot_crab_20241024_131856', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '241024_111859:cmsbot_crab_20241024_131858', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111901:cmsbot_crab_20241024_131901', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_111904:cmsbot_crab_20241024_131903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111906:cmsbot_crab_20241024_131905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241024_111914:cmsbot_crab_20241024_131908', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111918:cmsbot_crab_rucio_transfers_20241024_131916', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 32, 'finished': 8}, 'publication (fail/tdb/DBS)': '0/8/8'}
{'TN': '241024_111920:cmsbot_crab_rucio_transfers_group_20241024_131920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 8, 'finished': 32}, 'publication (fail/tdb/DBS)': '0/32/32'}
{'TN': '241024_111923:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111926:cmsbot_crab_rucio_transfers_nopublication_20241024_131925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 35, 'transferring': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111929:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131928', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/30/30'}
{'TN': '241024_111932:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131931', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-10-24T13:17:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-10-24 15:17:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1107/console

```
{'TN': '241024_111856:cmsbot_crab_20241024_131856', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/999/999'}
{'TN': '241024_111859:cmsbot_crab_20241024_131858', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111901:cmsbot_crab_20241024_131901', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_111904:cmsbot_crab_20241024_131903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111906:cmsbot_crab_20241024_131905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241024_111914:cmsbot_crab_20241024_131908', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111918:cmsbot_crab_rucio_transfers_20241024_131916', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/22/22'}
{'TN': '241024_111920:cmsbot_crab_rucio_transfers_group_20241024_131920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/37/37'}
{'TN': '241024_111923:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131922', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111926:cmsbot_crab_rucio_transfers_nopublication_20241024_131925', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111929:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131928', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/31/31'}
{'TN': '241024_111932:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131931', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-10-24T15:14:38Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-10-24 16:48:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1109/console

```
{'TN': '241024_111856:cmsbot_crab_20241024_131856', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241024_111859:cmsbot_crab_20241024_131858', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_111901:cmsbot_crab_20241024_131901', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_111904:cmsbot_crab_20241024_131903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111906:cmsbot_crab_20241024_131905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241024_111914:cmsbot_crab_20241024_131908', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111918:cmsbot_crab_rucio_transfers_20241024_131916', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_111920:cmsbot_crab_rucio_transfers_group_20241024_131920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '241024_111923:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131922', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111926:cmsbot_crab_rucio_transfers_nopublication_20241024_131925', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111929:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131928', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_111932:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131931', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-10-24T17:17:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-10-24 19:17:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1110/console

```
{'TN': '241024_111856:cmsbot_crab_20241024_131856', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241024_111859:cmsbot_crab_20241024_131858', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_111901:cmsbot_crab_20241024_131901', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_111904:cmsbot_crab_20241024_131903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111906:cmsbot_crab_20241024_131905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241024_111914:cmsbot_crab_20241024_131908', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111918:cmsbot_crab_rucio_transfers_20241024_131916', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_111920:cmsbot_crab_rucio_transfers_group_20241024_131920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '241024_111923:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131922', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111926:cmsbot_crab_rucio_transfers_nopublication_20241024_131925', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111929:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131928', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_111932:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131931', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-10-24T19:19:27Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-10-24 21:19:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1111/console

```
{'TN': '241024_111856:cmsbot_crab_20241024_131856', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241024_111859:cmsbot_crab_20241024_131858', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_111901:cmsbot_crab_20241024_131901', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241024_111904:cmsbot_crab_20241024_131903', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111906:cmsbot_crab_20241024_131905', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241024_111914:cmsbot_crab_20241024_131908', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241024_111918:cmsbot_crab_rucio_transfers_20241024_131916', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_111920:cmsbot_crab_rucio_transfers_group_20241024_131920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '241024_111923:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131922', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111926:cmsbot_crab_rucio_transfers_nopublication_20241024_131925', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111929:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131928', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241024_111932:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131931', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
