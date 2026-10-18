# dmwm/CRABServer issue #8567: #817: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-07-29T14:57:58Z
Closed: 2024-10-10T22:43:00Z
URL: https://github.com/dmwm/CRABServer/issues/8567

## Opening post (cmsdmwmbot, 2024-07-29T14:57:58Z)

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

Started at: 2024-07-29 16:57:57
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/817/)

## Comment (cmsdmwmbot, 2024-07-29T15:00:44Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240729_145939:cmsbot_crab_20240729_165939
240729_145941:cmsbot_crab_20240729_165941
240729_145943:cmsbot_crab_20240729_165943
240729_145945:cmsbot_crab_20240729_165945
240729_145948:cmsbot_crab_20240729_165947
240729_150006:cmsbot_crab_20240729_165949
240729_150009:cmsbot_crab_rucio_transfers_20240729_170008
240729_150011:cmsbot_crab_rucio_transfers_group_20240729_170011
240729_150014:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240729_170013
240729_150017:cmsbot_crab_rucio_transfers_nopublication_20240729_170016
240729_150020:cmsbot_crab_rucio_transfers_withnoneedm_20240729_170019
240729_150022:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240729_170021
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240729_145825:cmsbot_crab_transferOutputs
240729_145827:cmsbot_crab_transferLogs
240729_145830:cmsbot_crab_activity
240729_145832:cmsbot_crab_inputFiles
240729_145836:cmsbot_crab_disableAutomaticOutputCollection
240729_145838:cmsbot_crab_outputFiles
240729_145840:cmsbot_crab_allowUndistributedCMSSW
240729_145843:cmsbot_crab_maxMemoryMB
240729_145845:cmsbot_crab_maxJobRuntimeMin
240729_145847:cmsbot_crab_numCores
240729_145849:cmsbot_crab_scriptExe
240729_145852:cmsbot_crab_scriptArgs
240729_145855:cmsbot_crab_sendVenvFolder
240729_145857:cmsbot_crab_sendExternalFolder
240729_145859:cmsbot_crab_inputDBS
240729_145901:cmsbot_crab_useParent
240729_145903:cmsbot_crab_secondaryInputDataset
240729_145906:cmsbot_crab_lumiMaskFile
240729_145908:cmsbot_crab_lumiMaskUrl
240729_145910:cmsbot_crab_outLFNDirBase
240729_145913:cmsbot_crab_runRange
240729_145915:cmsbot_crab_ignoreLocality
240729_145917:cmsbot_crab_userInputFiles
240729_145921:cmsbot_crab_whitelist
240729_145923:cmsbot_crab_blacklist
240729_145925:cmsbot_crab_ignoreGlobalBlacklist
240729_145927:cmsbot_crab_voRole
240729_145929:cmsbot_crab_voGroup
240729_145931:cmsbot_crab_scheddName
240729_145934:cmsbot_crab_collector
240729_145936:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240729_145823:cmsbot_crab_20240729_165822
```

Finished at: 2024-07-29 17:00:23
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/817/console)

## Comment (cmsdmwmbot, 2024-07-29T15:49:46Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-07-29 17:49:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1040/console

```
{'TN': '240729_145939:cmsbot_crab_20240729_165939', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240729_145941:cmsbot_crab_20240729_165941', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_145943:cmsbot_crab_20240729_165943', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240729_145945:cmsbot_crab_20240729_165945', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240729_145948:cmsbot_crab_20240729_165947', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240729_150006:cmsbot_crab_20240729_165949', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240729_150009:cmsbot_crab_rucio_transfers_20240729_170008', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150011:cmsbot_crab_rucio_transfers_group_20240729_170011', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150014:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240729_170013', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150017:cmsbot_crab_rucio_transfers_nopublication_20240729_170016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150020:cmsbot_crab_rucio_transfers_withnoneedm_20240729_170019', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150022:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240729_170021', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-07-29T15:52:28Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-07-29 17:52:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/544/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/544//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-07-29T15:53:24Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2024-07-29 17:53:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1141/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240729_145825:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240729_145827:cmsbot_crab_transferLogs - 0
activity-check.sh 240729_145830:cmsbot_crab_activity - 0
inputFiles-check.sh 240729_145832:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240729_145836:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240729_145838:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240729_145840:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240729_145843:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240729_145845:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240729_145847:cmsbot_crab_numCores - 0
scriptExe-check.sh 240729_145849:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240729_145852:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240729_145855:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240729_145857:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240729_145859:cmsbot_crab_inputDBS - 0
useParent-check.sh 240729_145901:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240729_145903:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240729_145906:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240729_145908:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240729_145910:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240729_145913:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240729_145915:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240729_145917:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240729_145921:cmsbot_crab_whitelist - 0
blacklist-check.sh 240729_145923:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240729_145925:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240729_145927:cmsbot_crab_voRole - 0
voGroup-check.sh 240729_145929:cmsbot_crab_voGroup - 0
scheddName-check.sh 240729_145931:cmsbot_crab_scheddName - 0
collector-check.sh 240729_145934:cmsbot_crab_collector - 0
extraJDL-check.sh 240729_145936:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-07-29T16:06:50Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-07-29 18:06:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1041/console

```
{'TN': '240729_145939:cmsbot_crab_20240729_165939', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240729_145941:cmsbot_crab_20240729_165941', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_145943:cmsbot_crab_20240729_165943', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240729_145945:cmsbot_crab_20240729_165945', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240729_145948:cmsbot_crab_20240729_165947', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240729_150006:cmsbot_crab_20240729_165949', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/9/9'}
{'TN': '240729_150009:cmsbot_crab_rucio_transfers_20240729_170008', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150011:cmsbot_crab_rucio_transfers_group_20240729_170011', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150014:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240729_170013', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150017:cmsbot_crab_rucio_transfers_nopublication_20240729_170016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150020:cmsbot_crab_rucio_transfers_withnoneedm_20240729_170019', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240729_150022:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240729_170021', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
