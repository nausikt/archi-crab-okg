# dmwm/CRABServer issue #8861: #920: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-12-12T10:37:43Z
Closed: 2024-12-13T17:58:05Z
URL: https://github.com/dmwm/CRABServer/issues/8861

## Opening post (cmsdmwmbot, 2024-12-12T10:37:43Z)

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

Started at: 2024-12-12 11:37:42
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/920/)

## Comment (cmsdmwmbot, 2024-12-12T10:41:10Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
241212_104003:cmsbot_crab_20241212_114002
241212_104007:cmsbot_crab_20241212_114005
241212_104010:cmsbot_crab_20241212_114009
241212_104014:cmsbot_crab_20241212_114013
241212_104018:cmsbot_crab_20241212_114016
241212_104023:cmsbot_crab_20241212_114020
241212_104027:cmsbot_crab_rucio_transfers_20241212_114025
241212_104031:cmsbot_crab_rucio_transfers_group_20241212_114029
241212_104035:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241212_114033
241212_104039:cmsbot_crab_rucio_transfers_nopublication_20241212_114037
241212_104044:cmsbot_crab_rucio_transfers_withnoneedm_20241212_114041
241212_104048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241212_114046
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
241212_103814:cmsbot_crab_transferOutputs
241212_103817:cmsbot_crab_transferLogs
241212_103821:cmsbot_crab_activity
241212_103824:cmsbot_crab_inputFiles
241212_103828:cmsbot_crab_disableAutomaticOutputCollection
241212_103831:cmsbot_crab_outputFiles
241212_103834:cmsbot_crab_allowUndistributedCMSSW
241212_103838:cmsbot_crab_maxMemoryMB
241212_103841:cmsbot_crab_maxJobRuntimeMin
241212_103845:cmsbot_crab_numCores
241212_103848:cmsbot_crab_scriptExe
241212_103852:cmsbot_crab_scriptArgs
241212_103855:cmsbot_crab_sendVenvFolder
241212_103859:cmsbot_crab_sendExternalFolder
241212_103902:cmsbot_crab_inputDBS
241212_103906:cmsbot_crab_useParent
241212_103909:cmsbot_crab_secondaryInputDataset
241212_103913:cmsbot_crab_lumiMaskFile
241212_103916:cmsbot_crab_lumiMaskUrl
241212_103921:cmsbot_crab_outLFNDirBase
241212_103924:cmsbot_crab_runRange
241212_103928:cmsbot_crab_ignoreLocality
241212_103931:cmsbot_crab_userInputFiles
241212_103934:cmsbot_crab_whitelist
241212_103938:cmsbot_crab_blacklist
241212_103942:cmsbot_crab_ignoreGlobalBlacklist
241212_103945:cmsbot_crab_voRole
241212_103949:cmsbot_crab_voGroup
241212_103952:cmsbot_crab_scheddName
241212_103956:cmsbot_crab_collector
241212_103959:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241212_103807:cmsbot_crab_20241212_113805
```

Finished at: 2024-12-12 11:40:48
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/920/console)

## Comment (cmsdmwmbot, 2024-12-12T11:02:24Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-12-12 12:02:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1134/console

```
{'TN': '241212_104003:cmsbot_crab_20241212_114002', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 997, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104007:cmsbot_crab_20241212_114005', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104010:cmsbot_crab_20241212_114009', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104014:cmsbot_crab_20241212_114013', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104018:cmsbot_crab_20241212_114016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104023:cmsbot_crab_20241212_114020', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 7, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104027:cmsbot_crab_rucio_transfers_20241212_114025', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104031:cmsbot_crab_rucio_transfers_group_20241212_114029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104035:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241212_114033', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104039:cmsbot_crab_rucio_transfers_nopublication_20241212_114037', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104044:cmsbot_crab_rucio_transfers_withnoneedm_20241212_114041', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241212_114046', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-12-12T11:05:12Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-12-12 12:05:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/594/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/594//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-12-12T11:06:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-12-12 12:06:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1262/console

```
RETRY TESTS:
transferLogs-check.sh 241212_103817:cmsbot_crab_transferLogs - 2
maxMemoryMB-check.sh 241212_103838:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 241212_103841:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241212_103845:cmsbot_crab_numCores - 2
scriptExe-check.sh 241212_103848:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 241212_103852:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 241212_103913:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241212_103916:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241212_103921:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241212_103924:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241212_103931:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241212_103934:cmsbot_crab_whitelist - 2
blacklist-check.sh 241212_103938:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241212_103942:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241212_103945:cmsbot_crab_voRole - 2
voGroup-check.sh 241212_103949:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241212_103814:cmsbot_crab_transferOutputs - 0
activity-check.sh 241212_103821:cmsbot_crab_activity - 0
inputFiles-check.sh 241212_103824:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241212_103828:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241212_103831:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241212_103834:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 241212_103855:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241212_103859:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241212_103902:cmsbot_crab_inputDBS - 0
useParent-check.sh 241212_103906:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241212_103909:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 241212_103928:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 241212_103952:cmsbot_crab_scheddName - 0
collector-check.sh 241212_103956:cmsbot_crab_collector - 0
extraJDL-check.sh 241212_103959:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-12-12T11:19:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-12-12 12:19:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1135/console

```
{'TN': '241212_104003:cmsbot_crab_20241212_114002', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104007:cmsbot_crab_20241212_114005', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104010:cmsbot_crab_20241212_114009', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104014:cmsbot_crab_20241212_114013', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104018:cmsbot_crab_20241212_114016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104023:cmsbot_crab_20241212_114020', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104027:cmsbot_crab_rucio_transfers_20241212_114025', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104031:cmsbot_crab_rucio_transfers_group_20241212_114029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104035:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241212_114033', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104039:cmsbot_crab_rucio_transfers_nopublication_20241212_114037', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104044:cmsbot_crab_rucio_transfers_withnoneedm_20241212_114041', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241212_114046', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-12-12T11:30:34Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-12-12 12:30:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1263/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241212_103814:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241212_103817:cmsbot_crab_transferLogs - 0
activity-check.sh 241212_103821:cmsbot_crab_activity - 0
inputFiles-check.sh 241212_103824:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241212_103828:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241212_103831:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241212_103834:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241212_103838:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241212_103841:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241212_103845:cmsbot_crab_numCores - 0
scriptExe-check.sh 241212_103848:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241212_103852:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241212_103855:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241212_103859:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241212_103902:cmsbot_crab_inputDBS - 0
useParent-check.sh 241212_103906:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241212_103909:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241212_103913:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241212_103916:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241212_103921:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241212_103924:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241212_103928:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241212_103931:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241212_103934:cmsbot_crab_whitelist - 0
blacklist-check.sh 241212_103938:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241212_103942:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241212_103945:cmsbot_crab_voRole - 0
voGroup-check.sh 241212_103949:cmsbot_crab_voGroup - 0
scheddName-check.sh 241212_103952:cmsbot_crab_scheddName - 0
collector-check.sh 241212_103956:cmsbot_crab_collector - 0
extraJDL-check.sh 241212_103959:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-12-12T12:06:26Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-12-12 13:06:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1136/console

```
{'TN': '241212_104003:cmsbot_crab_20241212_114002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241212_104007:cmsbot_crab_20241212_114005', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104010:cmsbot_crab_20241212_114009', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241212_104014:cmsbot_crab_20241212_114013', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241212_104018:cmsbot_crab_20241212_114016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241212_104023:cmsbot_crab_20241212_114020', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241212_104027:cmsbot_crab_rucio_transfers_20241212_114025', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241212_104031:cmsbot_crab_rucio_transfers_group_20241212_114029', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '241212_104035:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241212_114033', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104039:cmsbot_crab_rucio_transfers_nopublication_20241212_114037', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104044:cmsbot_crab_rucio_transfers_withnoneedm_20241212_114041', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '241212_104048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241212_114046', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-12-12T13:38:26Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-12-12 14:38:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1137/console

```
{'TN': '241212_104003:cmsbot_crab_20241212_114002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241212_104007:cmsbot_crab_20241212_114005', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241212_104010:cmsbot_crab_20241212_114009', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241212_104014:cmsbot_crab_20241212_114013', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241212_104018:cmsbot_crab_20241212_114016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241212_104023:cmsbot_crab_20241212_114020', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241212_104027:cmsbot_crab_rucio_transfers_20241212_114025', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241212_104031:cmsbot_crab_rucio_transfers_group_20241212_114029', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241212_104035:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241212_114033', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104039:cmsbot_crab_rucio_transfers_nopublication_20241212_114037', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241212_104044:cmsbot_crab_rucio_transfers_withnoneedm_20241212_114041', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241212_104048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241212_114046', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
