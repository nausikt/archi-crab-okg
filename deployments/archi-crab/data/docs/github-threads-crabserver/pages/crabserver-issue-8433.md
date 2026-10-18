# dmwm/CRABServer issue #8433: #782: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-28T11:56:06Z
Closed: 2024-05-29T07:15:28Z
URL: https://github.com/dmwm/CRABServer/issues/8433

## Opening post (cmsdmwmbot, 2024-05-28T11:56:06Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-05-28 13:56:05
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/782/)

## Comment (cmsdmwmbot, 2024-05-28T11:59:02Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240528_115747:cmsbot_crab_20240528_135746
240528_115749:cmsbot_crab_20240528_135748
240528_115751:cmsbot_crab_20240528_135751
240528_115754:cmsbot_crab_20240528_135753
240528_115756:cmsbot_crab_20240528_135756
240528_115820:cmsbot_crab_20240528_135758
240528_115824:cmsbot_crab_rucio_transfers_20240528_135822
240528_115826:cmsbot_crab_rucio_transfers_group_20240528_135825
240528_115829:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240528_135828
240528_115833:cmsbot_crab_rucio_transfers_nopublication_20240528_135831
240528_115837:cmsbot_crab_rucio_transfers_withnoneedm_20240528_135835
240528_115840:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240528_135838
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240528_115632:cmsbot_crab_transferOutputs
240528_115634:cmsbot_crab_transferLogs
240528_115637:cmsbot_crab_activity
240528_115639:cmsbot_crab_inputFiles
240528_115641:cmsbot_crab_disableAutomaticOutputCollection
240528_115644:cmsbot_crab_outputFiles
240528_115646:cmsbot_crab_allowUndistributedCMSSW
240528_115648:cmsbot_crab_maxMemoryMB
240528_115650:cmsbot_crab_maxJobRuntimeMin
240528_115653:cmsbot_crab_numCores
240528_115655:cmsbot_crab_scriptExe
240528_115657:cmsbot_crab_scriptArgs
240528_115700:cmsbot_crab_sendVenvFolder
240528_115702:cmsbot_crab_sendExternalFolder
240528_115704:cmsbot_crab_inputDBS
240528_115706:cmsbot_crab_useParent
240528_115709:cmsbot_crab_secondaryInputDataset
240528_115711:cmsbot_crab_lumiMaskFile
240528_115713:cmsbot_crab_lumiMaskUrl
240528_115718:cmsbot_crab_outLFNDirBase
240528_115720:cmsbot_crab_runRange
240528_115723:cmsbot_crab_ignoreLocality
240528_115725:cmsbot_crab_userInputFiles
240528_115727:cmsbot_crab_whitelist
240528_115730:cmsbot_crab_blacklist
240528_115732:cmsbot_crab_ignoreGlobalBlacklist
240528_115734:cmsbot_crab_voRole
240528_115737:cmsbot_crab_voGroup
240528_115739:cmsbot_crab_scheddName
240528_115741:cmsbot_crab_collector
240528_115744:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240528_115629:cmsbot_crab_20240528_135628
```

Finished at: 2024-05-28 13:58:40
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/782/console)

## Comment (cmsdmwmbot, 2024-05-28T12:20:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-28 14:20:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/930/console

```
{'TN': '240528_115747:cmsbot_crab_20240528_135746', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 993, 'idle': 3, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115749:cmsbot_crab_20240528_135748', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115751:cmsbot_crab_20240528_135751', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115754:cmsbot_crab_20240528_135753', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115756:cmsbot_crab_20240528_135756', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 98, 'idle': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115820:cmsbot_crab_20240528_135758', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 6, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115824:cmsbot_crab_rucio_transfers_20240528_135822', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115826:cmsbot_crab_rucio_transfers_group_20240528_135825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115829:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240528_135828', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115833:cmsbot_crab_rucio_transfers_nopublication_20240528_135831', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115837:cmsbot_crab_rucio_transfers_withnoneedm_20240528_135835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115840:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240528_135838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-28T12:24:03Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-05-28 14:24:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/539/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/539//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-05-28T12:25:30Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-28 14:25:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1072/console

```
RETRY TESTS:
numCores-check.sh 240528_115653:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240528_115713:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240528_115718:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240528_115720:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240528_115725:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240528_115727:cmsbot_crab_whitelist - 2
blacklist-check.sh 240528_115730:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240528_115632:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240528_115634:cmsbot_crab_transferLogs - 0
activity-check.sh 240528_115637:cmsbot_crab_activity - 0
inputFiles-check.sh 240528_115639:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240528_115641:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240528_115646:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240528_115648:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240528_115650:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240528_115655:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240528_115657:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240528_115700:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240528_115702:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240528_115704:cmsbot_crab_inputDBS - 0
useParent-check.sh 240528_115706:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240528_115709:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240528_115711:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240528_115723:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240528_115732:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240528_115734:cmsbot_crab_voRole - 0
voGroup-check.sh 240528_115737:cmsbot_crab_voGroup - 0
scheddName-check.sh 240528_115739:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240528_115744:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240528_115644:cmsbot_crab_outputFiles - 1
collector-check.sh 240528_115741:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-05-28T12:36:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-05-28 14:36:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/931/console

```
{'TN': '240528_115747:cmsbot_crab_20240528_135746', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 995, 'idle': 2, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115749:cmsbot_crab_20240528_135748', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115751:cmsbot_crab_20240528_135751', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115754:cmsbot_crab_20240528_135753', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115756:cmsbot_crab_20240528_135756', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115820:cmsbot_crab_20240528_135758', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115824:cmsbot_crab_rucio_transfers_20240528_135822', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115826:cmsbot_crab_rucio_transfers_group_20240528_135825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115829:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240528_135828', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115833:cmsbot_crab_rucio_transfers_nopublication_20240528_135831', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115837:cmsbot_crab_rucio_transfers_withnoneedm_20240528_135835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115840:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240528_135838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-28T12:50:46Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-05-28 14:50:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1073/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240528_115632:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240528_115634:cmsbot_crab_transferLogs - 0
activity-check.sh 240528_115637:cmsbot_crab_activity - 0
inputFiles-check.sh 240528_115639:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240528_115641:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240528_115646:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240528_115648:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240528_115650:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240528_115653:cmsbot_crab_numCores - 0
scriptExe-check.sh 240528_115655:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240528_115657:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240528_115700:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240528_115702:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240528_115704:cmsbot_crab_inputDBS - 0
useParent-check.sh 240528_115706:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240528_115709:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240528_115711:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240528_115713:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240528_115718:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240528_115720:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240528_115723:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240528_115725:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240528_115727:cmsbot_crab_whitelist - 0
blacklist-check.sh 240528_115730:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240528_115732:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240528_115734:cmsbot_crab_voRole - 0
voGroup-check.sh 240528_115737:cmsbot_crab_voGroup - 0
scheddName-check.sh 240528_115739:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240528_115744:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240528_115644:cmsbot_crab_outputFiles - 1
collector-check.sh 240528_115741:cmsbot_crab_collector - 1
```

## Comment (belforte, 2024-05-28T13:15:25Z)

I am puzzled that collector-check failed. I verified that the TW was using both CERN and FNAL ones, and FNAL is OK (CERN is not). :man_shrugging: :roll_eyes: 
outputFiles requires the new client in GH HEAD

## Comment (cmsdmwmbot, 2024-05-28T13:22:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-05-28 15:22:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/932/console

```
{'TN': '240528_115747:cmsbot_crab_20240528_135746', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 995, 'transferring': 2, 'failed': 3}, 'publication (fail/tdb/DBS)': '0/995/995'}
{'TN': '240528_115749:cmsbot_crab_20240528_135748', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115751:cmsbot_crab_20240528_135751', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115754:cmsbot_crab_20240528_135753', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240528_115756:cmsbot_crab_20240528_135756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240528_115820:cmsbot_crab_20240528_135758', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240528_115824:cmsbot_crab_rucio_transfers_20240528_135822', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115826:cmsbot_crab_rucio_transfers_group_20240528_135825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115829:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240528_135828', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115833:cmsbot_crab_rucio_transfers_nopublication_20240528_135831', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115837:cmsbot_crab_rucio_transfers_withnoneedm_20240528_135835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115840:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240528_135838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (novicecpp, 2024-05-28T13:26:13Z)

> outputFiles requires the new client in GH HEAD

@belforte Do we need to deploy client first?

## Comment (belforte, 2024-05-28T13:32:53Z)

no. it will work with current client. Simply getoutput logs an odd message on Jenkins nodes (only) which makes crab client exit with code=1. Actually we need new REST before we can update client ! 
https://github.com/dmwm/CRABClient/issues/5309#issuecomment-2112391604

Yeah.. .I should have documented this much better :-(

## Comment (cmsdmwmbot, 2024-05-28T14:54:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-05-28 16:54:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/933/console

```
{'TN': '240528_115747:cmsbot_crab_20240528_135746', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240528_115749:cmsbot_crab_20240528_135748', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115751:cmsbot_crab_20240528_135751', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115754:cmsbot_crab_20240528_135753', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240528_115756:cmsbot_crab_20240528_135756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240528_115820:cmsbot_crab_20240528_135758', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240528_115824:cmsbot_crab_rucio_transfers_20240528_135822', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115826:cmsbot_crab_rucio_transfers_group_20240528_135825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115829:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240528_135828', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115833:cmsbot_crab_rucio_transfers_nopublication_20240528_135831', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115837:cmsbot_crab_rucio_transfers_withnoneedm_20240528_135835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115840:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240528_135838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (novicecpp, 2024-05-28T15:04:13Z)

I remembered this but forgot which commit or which service you need to deploy first.

Maybe we can put some comments after PR is merged to remind the compatibility between service. So, when I create the release I can open all merged PRs again and look at that comments.

## Comment (belforte, 2024-05-28T15:14:17Z)

I am realising that I do not remember anymore the important details here :sob:

## Comment (cmsdmwmbot, 2024-05-28T16:57:45Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-05-28 18:57:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/934/console

```
{'TN': '240528_115747:cmsbot_crab_20240528_135746', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240528_115749:cmsbot_crab_20240528_135748', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115751:cmsbot_crab_20240528_135751', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115754:cmsbot_crab_20240528_135753', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240528_115756:cmsbot_crab_20240528_135756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240528_115820:cmsbot_crab_20240528_135758', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240528_115824:cmsbot_crab_rucio_transfers_20240528_135822', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115826:cmsbot_crab_rucio_transfers_group_20240528_135825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115829:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240528_135828', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115833:cmsbot_crab_rucio_transfers_nopublication_20240528_135831', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115837:cmsbot_crab_rucio_transfers_withnoneedm_20240528_135835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115840:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240528_135838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-05-28T17:19:26Z)

I find it worrying that only 1 file has been transferred by Rucio in hours. Although it is unlikely that it is due to changes in this tag

## Comment (cmsdmwmbot, 2024-05-28T19:00:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-05-28 21:00:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/935/console

```
{'TN': '240528_115747:cmsbot_crab_20240528_135746', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240528_115749:cmsbot_crab_20240528_135748', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115751:cmsbot_crab_20240528_135751', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240528_115754:cmsbot_crab_20240528_135753', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240528_115756:cmsbot_crab_20240528_135756', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240528_115820:cmsbot_crab_20240528_135758', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240528_115824:cmsbot_crab_rucio_transfers_20240528_135822', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115826:cmsbot_crab_rucio_transfers_group_20240528_135825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/34'}
{'TN': '240528_115829:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240528_135828', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115833:cmsbot_crab_rucio_transfers_nopublication_20240528_135831', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240528_115837:cmsbot_crab_rucio_transfers_withnoneedm_20240528_135835', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/31/28'}
{'TN': '240528_115840:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240528_135838', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 4, 'transferring': 36}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (novicecpp, 2024-05-29T07:15:28Z)

`240528_115824:cmsbot_crab_rucio_transfers_20240528_135822` also completed. 
[v3.240527](https://github.com/dmwm/CRABServer/releases/tag/v3.240527) is validated.

## Comment (belforte, 2024-05-29T07:18:59Z)

about previous discussion on CRABClient, all in all I had not been *so* bad. I had put a clear note in the new Client tag
https://github.com/dmwm/CRABClient/releases/tag/v3.240520
