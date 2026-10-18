# dmwm/CRABServer issue #8384: #770: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-08T14:27:39Z
Closed: 2024-05-08T16:24:29Z
URL: https://github.com/dmwm/CRABServer/issues/8384

## Opening post (cmsdmwmbot, 2024-05-08T14:27:39Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-05-08 16:27:38
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/770/)

## Comment (cmsdmwmbot, 2024-05-08T14:29:58Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240508_142907:cmsbot_crab_20240508_162907
240508_142909:cmsbot_crab_20240508_162909
240508_142911:cmsbot_crab_20240508_162911
240508_142913:cmsbot_crab_20240508_162913
240508_142915:cmsbot_crab_20240508_162915
240508_142919:cmsbot_crab_20240508_162917
240508_142923:cmsbot_crab_rucio_transfers_20240508_162920
240508_142925:cmsbot_crab_rucio_transfers_group_20240508_162924
240508_142927:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240508_162926
240508_142930:cmsbot_crab_rucio_transfers_nopublication_20240508_162929
240508_142933:cmsbot_crab_rucio_transfers_withnoneedm_20240508_162932
240508_142937:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240508_162935
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240508_142802:cmsbot_crab_transferOutputs
240508_142804:cmsbot_crab_transferLogs
240508_142806:cmsbot_crab_activity
240508_142808:cmsbot_crab_inputFiles
240508_142810:cmsbot_crab_disableAutomaticOutputCollection
240508_142812:cmsbot_crab_outputFiles
240508_142814:cmsbot_crab_allowUndistributedCMSSW
240508_142816:cmsbot_crab_maxMemoryMB
240508_142818:cmsbot_crab_maxJobRuntimeMin
240508_142820:cmsbot_crab_numCores
240508_142822:cmsbot_crab_scriptExe
240508_142825:cmsbot_crab_scriptArgs
240508_142827:cmsbot_crab_sendVenvFolder
240508_142829:cmsbot_crab_sendExternalFolder
240508_142831:cmsbot_crab_inputDBS
240508_142833:cmsbot_crab_useParent
240508_142835:cmsbot_crab_secondaryInputDataset
240508_142837:cmsbot_crab_lumiMaskFile
240508_142839:cmsbot_crab_lumiMaskUrl
240508_142843:cmsbot_crab_outLFNDirBase
240508_142845:cmsbot_crab_runRange
240508_142847:cmsbot_crab_ignoreLocality
240508_142849:cmsbot_crab_userInputFiles
240508_142851:cmsbot_crab_whitelist
240508_142853:cmsbot_crab_blacklist
240508_142855:cmsbot_crab_ignoreGlobalBlacklist
240508_142857:cmsbot_crab_voRole
240508_142859:cmsbot_crab_voGroup
240508_142901:cmsbot_crab_scheddName
240508_142903:cmsbot_crab_collector
240508_142905:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240508_142758:cmsbot_crab_20240508_162757
```

Finished at: 2024-05-08 16:29:37
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/770/console)

## Comment (mapellidario, 2024-05-08T14:43:56Z)

testing #8383 

- [x] https://cmsweb-testbed.cern.ch/crabserver/ui/task/240508_153304%3Admapelli_crab_wmcore233_20240508_173303 -> yeah, broken submission on vocms068, despite the problem reported is no location found for dataset.
    - [x] retry: https://cmsweb-testbed.cern.ch/crabserver/ui/task/240508_160655%3Admapelli_crab_wmcore233_20240508_180653 -> no ok vocms068 seem to have a real problem, `. Message from the scheduler: Unable to contact the collector and cached results does not exist for crab3@vocms068.cern.ch`
- [x] https://cmsweb-testbed.cern.ch/crabserver/ui/task/240508_154738%3Admapelli_crab_wmcore233_20240508_174737 (submitted on vocms059). some jobs failed with 8020, but overall rest can submit properly a dataset with `L1SCOUT` datatier
- [x] on prod the submissio fails with `Server answered with: Invalid input parameter. Reason is: Incorrect 'Data.inputDataset' parameter <class 'str'> /L1Scouting/Run2024B-v1/L1SCOUT`

## Comment (cmsdmwmbot, 2024-05-08T14:52:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-08 16:52:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/900/console

```
{'TN': '240508_142907:cmsbot_crab_20240508_162907', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 996, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142909:cmsbot_crab_20240508_162909', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142911:cmsbot_crab_20240508_162911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142913:cmsbot_crab_20240508_162913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142915:cmsbot_crab_20240508_162915', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142919:cmsbot_crab_20240508_162917', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142923:cmsbot_crab_rucio_transfers_20240508_162920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142925:cmsbot_crab_rucio_transfers_group_20240508_162924', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142927:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240508_162926', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142930:cmsbot_crab_rucio_transfers_nopublication_20240508_162929', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142933:cmsbot_crab_rucio_transfers_withnoneedm_20240508_162932', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142937:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240508_162935', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-08T14:54:45Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-05-08 16:54:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/536/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/536//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-05-08T14:56:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-08 16:56:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1050/console

```
RETRY TESTS:
transferLogs-check.sh 240508_142804:cmsbot_crab_transferLogs - 2
activity-check.sh 240508_142806:cmsbot_crab_activity - 2
outputFiles-check.sh 240508_142812:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240508_142818:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 240508_142822:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240508_142825:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240508_142837:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240508_142839:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240508_142843:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240508_142845:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240508_142849:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240508_142851:cmsbot_crab_whitelist - 2
blacklist-check.sh 240508_142853:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240508_142855:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240508_142857:cmsbot_crab_voRole - 2
voGroup-check.sh 240508_142859:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240508_142802:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240508_142808:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240508_142810:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240508_142814:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240508_142816:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 240508_142820:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240508_142827:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240508_142829:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240508_142831:cmsbot_crab_inputDBS - 0
useParent-check.sh 240508_142833:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240508_142835:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240508_142847:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 240508_142901:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240508_142905:cmsbot_crab_extraJDL - 0

FAILED TESTS:
collector-check.sh 240508_142903:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-05-08T15:09:11Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-05-08 17:09:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/901/console

```
{'TN': '240508_142907:cmsbot_crab_20240508_162907', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 997, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142909:cmsbot_crab_20240508_162909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142911:cmsbot_crab_20240508_162911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142913:cmsbot_crab_20240508_162913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142915:cmsbot_crab_20240508_162915', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142919:cmsbot_crab_20240508_162917', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142923:cmsbot_crab_rucio_transfers_20240508_162920', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142925:cmsbot_crab_rucio_transfers_group_20240508_162924', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 36, 'transferring': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142927:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240508_162926', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 33, 'transferring': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142930:cmsbot_crab_rucio_transfers_nopublication_20240508_162929', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 36, 'transferring': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142933:cmsbot_crab_rucio_transfers_withnoneedm_20240508_162932', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142937:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240508_162935', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-08T15:21:09Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-05-08 17:21:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1051/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240508_142802:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240508_142804:cmsbot_crab_transferLogs - 0
activity-check.sh 240508_142806:cmsbot_crab_activity - 0
inputFiles-check.sh 240508_142808:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240508_142810:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240508_142814:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240508_142816:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240508_142818:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240508_142820:cmsbot_crab_numCores - 0
scriptExe-check.sh 240508_142822:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240508_142825:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240508_142827:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240508_142829:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240508_142831:cmsbot_crab_inputDBS - 0
useParent-check.sh 240508_142833:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240508_142835:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240508_142837:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240508_142839:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240508_142843:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240508_142845:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240508_142847:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240508_142849:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240508_142851:cmsbot_crab_whitelist - 0
blacklist-check.sh 240508_142853:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240508_142855:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240508_142857:cmsbot_crab_voRole - 0
voGroup-check.sh 240508_142859:cmsbot_crab_voGroup - 0
scheddName-check.sh 240508_142901:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240508_142905:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240508_142812:cmsbot_crab_outputFiles - 1
collector-check.sh 240508_142903:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-05-08T15:55:12Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-05-08 17:55:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/902/console

```
{'TN': '240508_142907:cmsbot_crab_20240508_162907', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/998/998'}
{'TN': '240508_142909:cmsbot_crab_20240508_162909', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142911:cmsbot_crab_20240508_162911', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240508_142913:cmsbot_crab_20240508_162913', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240508_142915:cmsbot_crab_20240508_162915', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240508_142919:cmsbot_crab_20240508_162917', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240508_142923:cmsbot_crab_rucio_transfers_20240508_162920', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/39'}
{'TN': '240508_142925:cmsbot_crab_rucio_transfers_group_20240508_162924', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/39'}
{'TN': '240508_142927:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240508_162926', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142930:cmsbot_crab_rucio_transfers_nopublication_20240508_162929', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142933:cmsbot_crab_rucio_transfers_withnoneedm_20240508_162932', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240508_142937:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240508_162935', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (mapellidario, 2024-05-08T16:24:29Z)

everything in the rest looks ok

## Comment (cmsdmwmbot, 2024-05-08T17:26:24Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-05-08 19:26:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/903/console

```
{'TN': '240508_142907:cmsbot_crab_20240508_162907', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240508_142909:cmsbot_crab_20240508_162909', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240508_142911:cmsbot_crab_20240508_162911', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240508_142913:cmsbot_crab_20240508_162913', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240508_142915:cmsbot_crab_20240508_162915', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240508_142919:cmsbot_crab_20240508_162917', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240508_142923:cmsbot_crab_rucio_transfers_20240508_162920', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/39'}
{'TN': '240508_142925:cmsbot_crab_rucio_transfers_group_20240508_162924', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/39'}
{'TN': '240508_142927:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240508_162926', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142930:cmsbot_crab_rucio_transfers_nopublication_20240508_162929', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240508_142933:cmsbot_crab_rucio_transfers_withnoneedm_20240508_162932', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240508_142937:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240508_162935', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
