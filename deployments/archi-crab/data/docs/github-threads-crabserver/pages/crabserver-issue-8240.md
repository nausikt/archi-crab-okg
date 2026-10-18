# dmwm/CRABServer issue #8240: #710: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-02-16T13:57:02Z
Closed: 2024-02-18T17:24:25Z
URL: https://github.com/dmwm/CRABServer/issues/8240

## Opening post (cmsdmwmbot, 2024-02-16T13:57:02Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-02-16 14:57:01
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/710/)

## Comment (cmsdmwmbot, 2024-02-16T14:00:57Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240216_135923:cmsbot_crab_20240216_145922
240216_135925:cmsbot_crab_20240216_145924
240216_135927:cmsbot_crab_20240216_145926
240216_135929:cmsbot_crab_20240216_145929
240216_135931:cmsbot_crab_20240216_145931
240216_135958:cmsbot_crab_20240216_145933
240216_140001:cmsbot_crab_rucio_transfers_20240216_145959
240216_140003:cmsbot_crab_rucio_transfers_group_20240216_150002
240216_140019:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150005
240216_140029:cmsbot_crab_rucio_transfers_nopublication_20240216_150021
240216_140033:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150031
240216_140036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150034
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240216_135723:cmsbot_crab_transferOutputs
240216_135727:cmsbot_crab_transferLogs
240216_135729:cmsbot_crab_activity
240216_135731:cmsbot_crab_inputFiles
240216_135733:cmsbot_crab_disableAutomaticOutputCollection
240216_135735:cmsbot_crab_outputFiles
240216_135737:cmsbot_crab_allowUndistributedCMSSW
240216_135739:cmsbot_crab_maxMemoryMB
240216_135741:cmsbot_crab_maxJobRuntimeMin
240216_135743:cmsbot_crab_numCores
240216_135746:cmsbot_crab_scriptExe
240216_135748:cmsbot_crab_scriptArgs
240216_135750:cmsbot_crab_sendVenvFolder
240216_135841:cmsbot_crab_sendExternalFolder
240216_135843:cmsbot_crab_inputDBS
240216_135845:cmsbot_crab_useParent
240216_135847:cmsbot_crab_secondaryInputDataset
240216_135850:cmsbot_crab_lumiMaskFile
240216_135853:cmsbot_crab_lumiMaskUrl
240216_135856:cmsbot_crab_outLFNDirBase
240216_135858:cmsbot_crab_runRange
240216_135900:cmsbot_crab_ignoreLocality
240216_135902:cmsbot_crab_userInputFiles
240216_135904:cmsbot_crab_whitelist
240216_135907:cmsbot_crab_blacklist
240216_135909:cmsbot_crab_ignoreGlobalBlacklist
240216_135911:cmsbot_crab_voRole
240216_135913:cmsbot_crab_voGroup
240216_135915:cmsbot_crab_scheddName
240216_135917:cmsbot_crab_collector
240216_135920:cmsbot_crab_extraJDL
```

Finished at: 2024-02-16 15:00:36
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/710/console)

## Comment (cmsdmwmbot, 2024-02-16T14:22:46Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-16 15:22:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/759/console

```
{'TN': '240216_135923:cmsbot_crab_20240216_145922', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135925:cmsbot_crab_20240216_145924', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135927:cmsbot_crab_20240216_145926', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135929:cmsbot_crab_20240216_145929', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135931:cmsbot_crab_20240216_145931', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135958:cmsbot_crab_20240216_145933', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140001:cmsbot_crab_rucio_transfers_20240216_145959', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140003:cmsbot_crab_rucio_transfers_group_20240216_150002', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140019:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150005', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140029:cmsbot_crab_rucio_transfers_nopublication_20240216_150021', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140033:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150031', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150034', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T14:24:59Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-16 15:24:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/950/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 240216_135723:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240216_135727:cmsbot_crab_transferLogs - 1
activity-check.sh 240216_135729:cmsbot_crab_activity - 1
inputFiles-check.sh 240216_135731:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240216_135733:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240216_135735:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240216_135737:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240216_135739:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240216_135741:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240216_135743:cmsbot_crab_numCores - 1
scriptExe-check.sh 240216_135746:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240216_135748:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240216_135750:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240216_135841:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240216_135843:cmsbot_crab_inputDBS - 1
useParent-check.sh 240216_135845:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240216_135847:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240216_135850:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240216_135853:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240216_135856:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240216_135858:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240216_135900:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240216_135902:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240216_135904:cmsbot_crab_whitelist - 1
blacklist-check.sh 240216_135907:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240216_135909:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240216_135911:cmsbot_crab_voRole - 1
voGroup-check.sh 240216_135913:cmsbot_crab_voGroup - 1
scheddName-check.sh 240216_135915:cmsbot_crab_scheddName - 1
collector-check.sh 240216_135917:cmsbot_crab_collector - 1
extraJDL-check.sh 240216_135920:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-02-16T14:38:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-02-16 15:38:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/761/console

```
{'TN': '240216_135923:cmsbot_crab_20240216_145922', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135925:cmsbot_crab_20240216_145924', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135927:cmsbot_crab_20240216_145926', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135929:cmsbot_crab_20240216_145929', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135931:cmsbot_crab_20240216_145931', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135958:cmsbot_crab_20240216_145933', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140001:cmsbot_crab_rucio_transfers_20240216_145959', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140003:cmsbot_crab_rucio_transfers_group_20240216_150002', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140019:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150005', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140029:cmsbot_crab_rucio_transfers_nopublication_20240216_150021', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140033:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150031', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150034', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T15:25:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-02-16 16:24:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/763/console

```
{'TN': '240216_135923:cmsbot_crab_20240216_145922', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135925:cmsbot_crab_20240216_145924', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135927:cmsbot_crab_20240216_145926', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135929:cmsbot_crab_20240216_145929', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135931:cmsbot_crab_20240216_145931', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135958:cmsbot_crab_20240216_145933', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140001:cmsbot_crab_rucio_transfers_20240216_145959', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140003:cmsbot_crab_rucio_transfers_group_20240216_150002', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140019:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150005', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140029:cmsbot_crab_rucio_transfers_nopublication_20240216_150021', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140033:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150031', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150034', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T16:56:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-02-16 17:56:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/765/console

```
{'TN': '240216_135923:cmsbot_crab_20240216_145922', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135925:cmsbot_crab_20240216_145924', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135927:cmsbot_crab_20240216_145926', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135929:cmsbot_crab_20240216_145929', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135931:cmsbot_crab_20240216_145931', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135958:cmsbot_crab_20240216_145933', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140001:cmsbot_crab_rucio_transfers_20240216_145959', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140003:cmsbot_crab_rucio_transfers_group_20240216_150002', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140019:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150005', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140029:cmsbot_crab_rucio_transfers_nopublication_20240216_150021', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140033:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150031', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150034', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T18:57:49Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-02-16 19:57:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/767/console

```
{'TN': '240216_135923:cmsbot_crab_20240216_145922', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135925:cmsbot_crab_20240216_145924', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135927:cmsbot_crab_20240216_145926', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135929:cmsbot_crab_20240216_145929', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135931:cmsbot_crab_20240216_145931', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135958:cmsbot_crab_20240216_145933', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140001:cmsbot_crab_rucio_transfers_20240216_145959', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140003:cmsbot_crab_rucio_transfers_group_20240216_150002', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140019:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150005', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140029:cmsbot_crab_rucio_transfers_nopublication_20240216_150021', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140033:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150031', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150034', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T20:59:47Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-02-16 21:59:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/769/console

```
{'TN': '240216_135923:cmsbot_crab_20240216_145922', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135925:cmsbot_crab_20240216_145924', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135927:cmsbot_crab_20240216_145926', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135929:cmsbot_crab_20240216_145929', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135931:cmsbot_crab_20240216_145931', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_135958:cmsbot_crab_20240216_145933', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140001:cmsbot_crab_rucio_transfers_20240216_145959', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140003:cmsbot_crab_rucio_transfers_group_20240216_150002', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140019:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150005', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140029:cmsbot_crab_rucio_transfers_nopublication_20240216_150021', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140033:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150031', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240216_140036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150034', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```
