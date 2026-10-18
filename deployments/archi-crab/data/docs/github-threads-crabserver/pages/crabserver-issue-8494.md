# dmwm/CRABServer issue #8494: #804: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-14T13:28:57Z
Closed: 2024-06-14T16:29:11Z
URL: https://github.com/dmwm/CRABServer/issues/8494

## Opening post (cmsdmwmbot, 2024-06-14T13:28:57Z)

**This is meant to test modernizehtc-0614**
**Also tests new AuthProxyServer in cmsweb-testbed FrontEnd**

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-06-14 15:28:56
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/804/)

## Comment (cmsdmwmbot, 2024-06-14T13:31:06Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240614_133012:cmsbot_crab_20240614_153012
240614_133013:cmsbot_crab_20240614_153013
240614_133015:cmsbot_crab_20240614_153014
240614_133016:cmsbot_crab_20240614_153016
240614_133018:cmsbot_crab_20240614_153017
240614_133033:cmsbot_crab_20240614_153019
240614_133035:cmsbot_crab_rucio_transfers_20240614_153034
240614_133037:cmsbot_crab_rucio_transfers_group_20240614_153036
240614_133039:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240614_153038
240614_133041:cmsbot_crab_rucio_transfers_nopublication_20240614_153040
240614_133043:cmsbot_crab_rucio_transfers_withnoneedm_20240614_153042
240614_133045:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240614_153044
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240614_132927:cmsbot_crab_transferOutputs
240614_132929:cmsbot_crab_transferLogs
240614_132931:cmsbot_crab_activity
240614_132932:cmsbot_crab_inputFiles
240614_132933:cmsbot_crab_disableAutomaticOutputCollection
240614_132935:cmsbot_crab_outputFiles
240614_132936:cmsbot_crab_allowUndistributedCMSSW
240614_132938:cmsbot_crab_maxMemoryMB
240614_132939:cmsbot_crab_maxJobRuntimeMin
240614_132940:cmsbot_crab_numCores
240614_132942:cmsbot_crab_scriptExe
240614_132943:cmsbot_crab_scriptArgs
240614_132944:cmsbot_crab_sendVenvFolder
240614_132946:cmsbot_crab_sendExternalFolder
240614_132947:cmsbot_crab_inputDBS
240614_132949:cmsbot_crab_useParent
240614_132950:cmsbot_crab_secondaryInputDataset
240614_132951:cmsbot_crab_lumiMaskFile
240614_132953:cmsbot_crab_lumiMaskUrl
240614_132955:cmsbot_crab_outLFNDirBase
240614_132956:cmsbot_crab_runRange
240614_132958:cmsbot_crab_ignoreLocality
240614_132959:cmsbot_crab_userInputFiles
240614_133000:cmsbot_crab_whitelist
240614_133002:cmsbot_crab_blacklist
240614_133003:cmsbot_crab_ignoreGlobalBlacklist
240614_133005:cmsbot_crab_voRole
240614_133006:cmsbot_crab_voGroup
240614_133007:cmsbot_crab_scheddName
240614_133009:cmsbot_crab_collector
240614_133010:cmsbot_crab_extraJDL
```

Finished at: 2024-06-14 15:30:45
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/804/console)

## Comment (cmsdmwmbot, 2024-06-14T13:52:11Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-14 15:52:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/992/console

```
{'TN': '240614_133012:cmsbot_crab_20240614_153012', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 1, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133013:cmsbot_crab_20240614_153013', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133015:cmsbot_crab_20240614_153014', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133016:cmsbot_crab_20240614_153016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133018:cmsbot_crab_20240614_153017', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133033:cmsbot_crab_20240614_153019', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133035:cmsbot_crab_rucio_transfers_20240614_153034', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133037:cmsbot_crab_rucio_transfers_group_20240614_153036', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133039:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240614_153038', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133041:cmsbot_crab_rucio_transfers_nopublication_20240614_153040', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133043:cmsbot_crab_rucio_transfers_withnoneedm_20240614_153042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133045:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240614_153044', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-14T13:55:01Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-14 15:55:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1116/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240614_132939:cmsbot_crab_maxJobRuntimeMin - 2
whitelist-check.sh 240614_133000:cmsbot_crab_whitelist - 2
blacklist-check.sh 240614_133002:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240614_133003:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240614_132927:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240614_132929:cmsbot_crab_transferLogs - 0
activity-check.sh 240614_132931:cmsbot_crab_activity - 0
inputFiles-check.sh 240614_132932:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240614_132933:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240614_132935:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240614_132936:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240614_132938:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 240614_132940:cmsbot_crab_numCores - 0
scriptExe-check.sh 240614_132942:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240614_132943:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240614_132944:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240614_132946:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240614_132947:cmsbot_crab_inputDBS - 0
useParent-check.sh 240614_132949:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240614_132950:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240614_132951:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240614_132955:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240614_132959:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240614_133005:cmsbot_crab_voRole - 0
voGroup-check.sh 240614_133006:cmsbot_crab_voGroup - 0
scheddName-check.sh 240614_133007:cmsbot_crab_scheddName - 0
collector-check.sh 240614_133009:cmsbot_crab_collector - 0
extraJDL-check.sh 240614_133010:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240614_132953:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 240614_132956:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240614_132958:cmsbot_crab_ignoreLocality - 1
```

## Comment (cmsdmwmbot, 2024-06-14T14:08:10Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-14 16:08:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/993/console

```
{'TN': '240614_133012:cmsbot_crab_20240614_153012', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 1, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133013:cmsbot_crab_20240614_153013', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133015:cmsbot_crab_20240614_153014', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133016:cmsbot_crab_20240614_153016', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133018:cmsbot_crab_20240614_153017', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133033:cmsbot_crab_20240614_153019', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133035:cmsbot_crab_rucio_transfers_20240614_153034', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133037:cmsbot_crab_rucio_transfers_group_20240614_153036', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133039:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240614_153038', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133041:cmsbot_crab_rucio_transfers_nopublication_20240614_153040', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133043:cmsbot_crab_rucio_transfers_withnoneedm_20240614_153042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133045:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240614_153044', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-14T14:19:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-06-14 16:19:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1117/console

```
RETRY TESTS:
ignoreGlobalBlacklist-check.sh 240614_133003:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240614_132927:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240614_132929:cmsbot_crab_transferLogs - 0
activity-check.sh 240614_132931:cmsbot_crab_activity - 0
inputFiles-check.sh 240614_132932:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240614_132933:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240614_132935:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240614_132936:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240614_132938:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240614_132939:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240614_132940:cmsbot_crab_numCores - 0
scriptExe-check.sh 240614_132942:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240614_132943:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240614_132944:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240614_132946:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240614_132947:cmsbot_crab_inputDBS - 0
useParent-check.sh 240614_132949:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240614_132950:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240614_132951:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240614_132955:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240614_132959:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240614_133000:cmsbot_crab_whitelist - 0
blacklist-check.sh 240614_133002:cmsbot_crab_blacklist - 0
voRole-check.sh 240614_133005:cmsbot_crab_voRole - 0
voGroup-check.sh 240614_133006:cmsbot_crab_voGroup - 0
scheddName-check.sh 240614_133007:cmsbot_crab_scheddName - 0
collector-check.sh 240614_133009:cmsbot_crab_collector - 0
extraJDL-check.sh 240614_133010:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240614_132953:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 240614_132956:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240614_132958:cmsbot_crab_ignoreLocality - 1
```

## Comment (cmsdmwmbot, 2024-06-14T14:43:12Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-06-14 16:43:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1118/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240614_132953:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240614_132956:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240614_132958:cmsbot_crab_ignoreLocality - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240614_132927:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240614_132929:cmsbot_crab_transferLogs - 0
activity-check.sh 240614_132931:cmsbot_crab_activity - 0
inputFiles-check.sh 240614_132932:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240614_132933:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240614_132935:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240614_132936:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240614_132938:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240614_132939:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240614_132940:cmsbot_crab_numCores - 0
scriptExe-check.sh 240614_132942:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240614_132943:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240614_132944:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240614_132946:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240614_132947:cmsbot_crab_inputDBS - 0
useParent-check.sh 240614_132949:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240614_132950:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240614_132951:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240614_132955:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240614_132959:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240614_133000:cmsbot_crab_whitelist - 0
blacklist-check.sh 240614_133002:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240614_133003:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240614_133005:cmsbot_crab_voRole - 0
voGroup-check.sh 240614_133006:cmsbot_crab_voGroup - 0
scheddName-check.sh 240614_133007:cmsbot_crab_scheddName - 0
collector-check.sh 240614_133009:cmsbot_crab_collector - 0
extraJDL-check.sh 240614_133010:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-14T14:54:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-14 16:54:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/994/console

```
{'TN': '240614_133012:cmsbot_crab_20240614_153012', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240614_133013:cmsbot_crab_20240614_153013', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240614_133015:cmsbot_crab_20240614_153014', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240614_133016:cmsbot_crab_20240614_153016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240614_133018:cmsbot_crab_20240614_153017', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240614_133033:cmsbot_crab_20240614_153019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240614_133035:cmsbot_crab_rucio_transfers_20240614_153034', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240614_133037:cmsbot_crab_rucio_transfers_group_20240614_153036', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240614_133039:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240614_153038', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133041:cmsbot_crab_rucio_transfers_nopublication_20240614_153040', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133043:cmsbot_crab_rucio_transfers_withnoneedm_20240614_153042', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240614_133045:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240614_153044', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-06-14T15:07:36Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-14 17:07:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1119/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240614_132927:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240614_132929:cmsbot_crab_transferLogs - 0
activity-check.sh 240614_132931:cmsbot_crab_activity - 0
inputFiles-check.sh 240614_132932:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240614_132933:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240614_132935:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240614_132936:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240614_132938:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240614_132939:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240614_132940:cmsbot_crab_numCores - 0
scriptExe-check.sh 240614_132942:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240614_132943:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240614_132944:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240614_132946:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240614_132947:cmsbot_crab_inputDBS - 0
useParent-check.sh 240614_132949:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240614_132950:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240614_132951:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240614_132955:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 240614_132959:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240614_133000:cmsbot_crab_whitelist - 0
blacklist-check.sh 240614_133002:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240614_133003:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240614_133005:cmsbot_crab_voRole - 0
voGroup-check.sh 240614_133006:cmsbot_crab_voGroup - 0
scheddName-check.sh 240614_133007:cmsbot_crab_scheddName - 0
collector-check.sh 240614_133009:cmsbot_crab_collector - 0
extraJDL-check.sh 240614_133010:cmsbot_crab_extraJDL - 0

FAILED TESTS:
lumiMaskUrl-check.sh 240614_132953:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 240614_132956:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240614_132958:cmsbot_crab_ignoreLocality - 1
```

## Comment (cmsdmwmbot, 2024-06-14T16:27:24Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-06-14 18:27:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/995/console

```
{'TN': '240614_133012:cmsbot_crab_20240614_153012', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240614_133013:cmsbot_crab_20240614_153013', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240614_133015:cmsbot_crab_20240614_153014', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240614_133016:cmsbot_crab_20240614_153016', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240614_133018:cmsbot_crab_20240614_153017', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240614_133033:cmsbot_crab_20240614_153019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240614_133035:cmsbot_crab_rucio_transfers_20240614_153034', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240614_133037:cmsbot_crab_rucio_transfers_group_20240614_153036', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240614_133039:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240614_153038', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133041:cmsbot_crab_rucio_transfers_nopublication_20240614_153040', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240614_133043:cmsbot_crab_rucio_transfers_withnoneedm_20240614_153042', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240614_133045:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240614_153044', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-06-14T16:29:11Z)

the 3 failed tasks in CCV are due to a problem with dCache at DESY
