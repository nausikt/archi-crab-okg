# dmwm/CRABServer issue #8506: #807: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-17T13:17:44Z
Closed: 2024-06-18T16:03:03Z
URL: https://github.com/dmwm/CRABServer/issues/8506

## Opening post (cmsdmwmbot, 2024-06-17T13:17:44Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-06-17 15:17:43
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/807/)

## Comment (cmsdmwmbot, 2024-06-17T13:19:57Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240617_131909:cmsbot_crab_20240617_151909
240617_131911:cmsbot_crab_20240617_151911
240617_131913:cmsbot_crab_20240617_151913
240617_131915:cmsbot_crab_20240617_151915
240617_131917:cmsbot_crab_20240617_151917
240617_131921:cmsbot_crab_20240617_151919
240617_131923:cmsbot_crab_rucio_transfers_20240617_151922
240617_131925:cmsbot_crab_rucio_transfers_group_20240617_151925
240617_131928:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240617_151927
240617_131931:cmsbot_crab_rucio_transfers_nopublication_20240617_151930
240617_131933:cmsbot_crab_rucio_transfers_withnoneedm_20240617_151932
240617_131936:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240617_151935
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240617_131805:cmsbot_crab_transferOutputs
240617_131807:cmsbot_crab_transferLogs
240617_131809:cmsbot_crab_activity
240617_131811:cmsbot_crab_inputFiles
240617_131813:cmsbot_crab_disableAutomaticOutputCollection
240617_131815:cmsbot_crab_outputFiles
240617_131818:cmsbot_crab_allowUndistributedCMSSW
240617_131820:cmsbot_crab_maxMemoryMB
240617_131822:cmsbot_crab_maxJobRuntimeMin
240617_131824:cmsbot_crab_numCores
240617_131826:cmsbot_crab_scriptExe
240617_131828:cmsbot_crab_scriptArgs
240617_131830:cmsbot_crab_sendVenvFolder
240617_131832:cmsbot_crab_sendExternalFolder
240617_131834:cmsbot_crab_inputDBS
240617_131836:cmsbot_crab_useParent
240617_131838:cmsbot_crab_secondaryInputDataset
240617_131840:cmsbot_crab_lumiMaskFile
240617_131842:cmsbot_crab_lumiMaskUrl
240617_131845:cmsbot_crab_outLFNDirBase
240617_131847:cmsbot_crab_runRange
240617_131849:cmsbot_crab_ignoreLocality
240617_131851:cmsbot_crab_userInputFiles
240617_131853:cmsbot_crab_whitelist
240617_131855:cmsbot_crab_blacklist
240617_131857:cmsbot_crab_ignoreGlobalBlacklist
240617_131859:cmsbot_crab_voRole
240617_131901:cmsbot_crab_voGroup
240617_131903:cmsbot_crab_scheddName
240617_131905:cmsbot_crab_collector
240617_131907:cmsbot_crab_extraJDL
```

Finished at: 2024-06-17 15:19:36
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/807/console)

## Comment (cmsdmwmbot, 2024-06-17T13:40:52Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-17 15:40:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1000/console

```
{'TN': '240617_131909:cmsbot_crab_20240617_151909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131911:cmsbot_crab_20240617_151911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131913:cmsbot_crab_20240617_151913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131915:cmsbot_crab_20240617_151915', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131917:cmsbot_crab_20240617_151917', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131921:cmsbot_crab_20240617_151919', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131923:cmsbot_crab_rucio_transfers_20240617_151922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131925:cmsbot_crab_rucio_transfers_group_20240617_151925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131928:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240617_151927', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131931:cmsbot_crab_rucio_transfers_nopublication_20240617_151930', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131933:cmsbot_crab_rucio_transfers_withnoneedm_20240617_151932', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131936:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240617_151935', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-17T13:42:54Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-17 15:42:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1125/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 240617_131805:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240617_131807:cmsbot_crab_transferLogs - 1
activity-check.sh 240617_131809:cmsbot_crab_activity - 1
inputFiles-check.sh 240617_131811:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240617_131813:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240617_131815:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240617_131818:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240617_131820:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240617_131822:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240617_131824:cmsbot_crab_numCores - 1
scriptExe-check.sh 240617_131826:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240617_131828:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240617_131830:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240617_131832:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240617_131834:cmsbot_crab_inputDBS - 1
useParent-check.sh 240617_131836:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240617_131838:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240617_131840:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240617_131842:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240617_131845:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240617_131847:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240617_131849:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240617_131851:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240617_131853:cmsbot_crab_whitelist - 1
blacklist-check.sh 240617_131855:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240617_131857:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240617_131859:cmsbot_crab_voRole - 1
voGroup-check.sh 240617_131901:cmsbot_crab_voGroup - 1
scheddName-check.sh 240617_131903:cmsbot_crab_scheddName - 1
collector-check.sh 240617_131905:cmsbot_crab_collector - 1
extraJDL-check.sh 240617_131907:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-06-17T13:56:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-17 15:56:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1001/console

```
{'TN': '240617_131909:cmsbot_crab_20240617_151909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131911:cmsbot_crab_20240617_151911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131913:cmsbot_crab_20240617_151913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131915:cmsbot_crab_20240617_151915', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131917:cmsbot_crab_20240617_151917', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131921:cmsbot_crab_20240617_151919', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131923:cmsbot_crab_rucio_transfers_20240617_151922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131925:cmsbot_crab_rucio_transfers_group_20240617_151925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131928:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240617_151927', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131931:cmsbot_crab_rucio_transfers_nopublication_20240617_151930', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131933:cmsbot_crab_rucio_transfers_withnoneedm_20240617_151932', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131936:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240617_151935', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-17T14:17:03Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-17 16:17:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1126/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 240617_131805:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240617_131807:cmsbot_crab_transferLogs - 1
activity-check.sh 240617_131809:cmsbot_crab_activity - 1
inputFiles-check.sh 240617_131811:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240617_131813:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240617_131815:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240617_131818:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240617_131820:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240617_131822:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240617_131824:cmsbot_crab_numCores - 1
scriptExe-check.sh 240617_131826:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240617_131828:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240617_131830:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240617_131832:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240617_131834:cmsbot_crab_inputDBS - 1
useParent-check.sh 240617_131836:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240617_131838:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240617_131840:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240617_131842:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240617_131845:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240617_131847:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240617_131849:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240617_131851:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240617_131853:cmsbot_crab_whitelist - 1
blacklist-check.sh 240617_131855:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240617_131857:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240617_131859:cmsbot_crab_voRole - 1
voGroup-check.sh 240617_131901:cmsbot_crab_voGroup - 1
scheddName-check.sh 240617_131903:cmsbot_crab_scheddName - 1
collector-check.sh 240617_131905:cmsbot_crab_collector - 1
extraJDL-check.sh 240617_131907:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-06-17T14:42:39Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-17 16:42:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1002/console

```
{'TN': '240617_131909:cmsbot_crab_20240617_151909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131911:cmsbot_crab_20240617_151911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131913:cmsbot_crab_20240617_151913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131915:cmsbot_crab_20240617_151915', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131917:cmsbot_crab_20240617_151917', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131921:cmsbot_crab_20240617_151919', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131923:cmsbot_crab_rucio_transfers_20240617_151922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131925:cmsbot_crab_rucio_transfers_group_20240617_151925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131928:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240617_151927', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131931:cmsbot_crab_rucio_transfers_nopublication_20240617_151930', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131933:cmsbot_crab_rucio_transfers_withnoneedm_20240617_151932', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131936:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240617_151935', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-17T16:16:09Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-06-17 18:16:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1003/console

```
{'TN': '240617_131909:cmsbot_crab_20240617_151909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131911:cmsbot_crab_20240617_151911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131913:cmsbot_crab_20240617_151913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131915:cmsbot_crab_20240617_151915', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131917:cmsbot_crab_20240617_151917', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131921:cmsbot_crab_20240617_151919', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131923:cmsbot_crab_rucio_transfers_20240617_151922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131925:cmsbot_crab_rucio_transfers_group_20240617_151925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131928:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240617_151927', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131931:cmsbot_crab_rucio_transfers_nopublication_20240617_151930', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131933:cmsbot_crab_rucio_transfers_withnoneedm_20240617_151932', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131936:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240617_151935', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-17T18:17:14Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-06-17 20:17:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1004/console

```
{'TN': '240617_131909:cmsbot_crab_20240617_151909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131911:cmsbot_crab_20240617_151911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131913:cmsbot_crab_20240617_151913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131915:cmsbot_crab_20240617_151915', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131917:cmsbot_crab_20240617_151917', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131921:cmsbot_crab_20240617_151919', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131923:cmsbot_crab_rucio_transfers_20240617_151922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131925:cmsbot_crab_rucio_transfers_group_20240617_151925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131928:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240617_151927', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131931:cmsbot_crab_rucio_transfers_nopublication_20240617_151930', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131933:cmsbot_crab_rucio_transfers_withnoneedm_20240617_151932', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131936:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240617_151935', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-17T20:18:15Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-17 22:18:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1005/console

```
{'TN': '240617_131909:cmsbot_crab_20240617_151909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131911:cmsbot_crab_20240617_151911', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131913:cmsbot_crab_20240617_151913', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131915:cmsbot_crab_20240617_151915', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131917:cmsbot_crab_20240617_151917', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131921:cmsbot_crab_20240617_151919', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131923:cmsbot_crab_rucio_transfers_20240617_151922', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131925:cmsbot_crab_rucio_transfers_group_20240617_151925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131928:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240617_151927', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131931:cmsbot_crab_rucio_transfers_nopublication_20240617_151930', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131933:cmsbot_crab_rucio_transfers_withnoneedm_20240617_151932', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240617_131936:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240617_151935', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-18T16:03:03Z)

my bad
