# dmwm/CRABServer issue #8192: #682: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-22T15:44:56Z
Closed: 2024-01-23T08:52:17Z
URL: https://github.com/dmwm/CRABServer/issues/8192

## Opening post (cmsdmwmbot, 2024-01-22T15:44:56Z)

**TEST TW v3.240122 and that Publication check in ST now works**

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-01-22 16:44:55
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/682/)

## Comment (cmsdmwmbot, 2024-01-22T15:48:09Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240122_154716:cmsbot_crab_20240122_164715
240122_154718:cmsbot_crab_20240122_164717
240122_154720:cmsbot_crab_20240122_164720
240122_154723:cmsbot_crab_20240122_164722
240122_154725:cmsbot_crab_20240122_164724
240122_154730:cmsbot_crab_20240122_164727
240122_154733:cmsbot_crab_rucio_transfers_20240122_164731
240122_154735:cmsbot_crab_rucio_transfers_group_20240122_164734
240122_154738:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240122_164737
240122_154741:cmsbot_crab_rucio_transfers_nopublication_20240122_164740
240122_154745:cmsbot_crab_rucio_transfers_withnoneedm_20240122_164743
240122_154748:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240122_164746
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240122_154519:cmsbot_crab_transferOutputs
240122_154522:cmsbot_crab_transferLogs
240122_154524:cmsbot_crab_activity
240122_154526:cmsbot_crab_inputFiles
240122_154529:cmsbot_crab_disableAutomaticOutputCollection
240122_154531:cmsbot_crab_outputFiles
240122_154533:cmsbot_crab_allowUndistributedCMSSW
240122_154536:cmsbot_crab_maxMemoryMB
240122_154538:cmsbot_crab_maxJobRuntimeMin
240122_154540:cmsbot_crab_numCores
240122_154542:cmsbot_crab_scriptExe
240122_154545:cmsbot_crab_scriptArgs
240122_154547:cmsbot_crab_sendVenvFolder
240122_154633:cmsbot_crab_sendExternalFolder
240122_154635:cmsbot_crab_inputDBS
240122_154637:cmsbot_crab_useParent
240122_154639:cmsbot_crab_secondaryInputDataset
240122_154641:cmsbot_crab_lumiMaskFile
240122_154644:cmsbot_crab_lumiMaskUrl
240122_154647:cmsbot_crab_outLFNDirBase
240122_154649:cmsbot_crab_runRange
240122_154652:cmsbot_crab_ignoreLocality
240122_154654:cmsbot_crab_userInputFiles
240122_154656:cmsbot_crab_whitelist
240122_154659:cmsbot_crab_blacklist
240122_154701:cmsbot_crab_ignoreGlobalBlacklist
240122_154703:cmsbot_crab_voRole
240122_154706:cmsbot_crab_voGroup
240122_154708:cmsbot_crab_scheddName
240122_154710:cmsbot_crab_collector
240122_154712:cmsbot_crab_extraJDL
```

Finished at: 2024-01-22 16:47:48
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/682/console)

## Comment (cmsdmwmbot, 2024-01-22T16:09:04Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-22 17:09:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/737/console

```
{'TN': '240122_154716:cmsbot_crab_20240122_164715', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 957, 'running': 43}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154718:cmsbot_crab_20240122_164717', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154720:cmsbot_crab_20240122_164720', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154723:cmsbot_crab_20240122_164722', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154725:cmsbot_crab_20240122_164724', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154730:cmsbot_crab_20240122_164727', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 3, 'transferring': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154733:cmsbot_crab_rucio_transfers_20240122_164731', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154735:cmsbot_crab_rucio_transfers_group_20240122_164734', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154738:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240122_164737', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154741:cmsbot_crab_rucio_transfers_nopublication_20240122_164740', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154745:cmsbot_crab_rucio_transfers_withnoneedm_20240122_164743', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154748:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240122_164746', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-22T16:11:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-22 17:11:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/891/console

```
RETRY TESTS:
transferLogs-check.sh 240122_154522:cmsbot_crab_transferLogs - 2
maxMemoryMB-check.sh 240122_154536:cmsbot_crab_maxMemoryMB - 2
scriptExe-check.sh 240122_154542:cmsbot_crab_scriptExe - 2
lumiMaskFile-check.sh 240122_154641:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240122_154644:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240122_154649:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240122_154654:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240122_154656:cmsbot_crab_whitelist - 2
blacklist-check.sh 240122_154659:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240122_154701:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240122_154519:cmsbot_crab_transferOutputs - 0
activity-check.sh 240122_154524:cmsbot_crab_activity - 0
inputFiles-check.sh 240122_154526:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240122_154529:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240122_154531:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240122_154533:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240122_154538:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240122_154540:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240122_154545:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240122_154547:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240122_154633:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240122_154635:cmsbot_crab_inputDBS - 0
useParent-check.sh 240122_154637:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240122_154639:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 240122_154647:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240122_154652:cmsbot_crab_ignoreLocality - 0
voRole-check.sh 240122_154703:cmsbot_crab_voRole - 0
voGroup-check.sh 240122_154706:cmsbot_crab_voGroup - 0
scheddName-check.sh 240122_154708:cmsbot_crab_scheddName - 0
collector-check.sh 240122_154710:cmsbot_crab_collector - 0
extraJDL-check.sh 240122_154712:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-22T16:25:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-01-22 17:24:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/738/console

```
{'TN': '240122_154716:cmsbot_crab_20240122_164715', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154718:cmsbot_crab_20240122_164717', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154720:cmsbot_crab_20240122_164720', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154723:cmsbot_crab_20240122_164722', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154725:cmsbot_crab_20240122_164724', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154730:cmsbot_crab_20240122_164727', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154733:cmsbot_crab_rucio_transfers_20240122_164731', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154735:cmsbot_crab_rucio_transfers_group_20240122_164734', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154738:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240122_164737', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1, 'finished': 39}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154741:cmsbot_crab_rucio_transfers_nopublication_20240122_164740', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1, 'finished': 39}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154745:cmsbot_crab_rucio_transfers_withnoneedm_20240122_164743', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154748:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240122_164746', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-22T16:35:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-22 17:35:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/892/console

```
RETRY TESTS:
userInputFiles-check.sh 240122_154654:cmsbot_crab_userInputFiles - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240122_154519:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240122_154522:cmsbot_crab_transferLogs - 0
activity-check.sh 240122_154524:cmsbot_crab_activity - 0
inputFiles-check.sh 240122_154526:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240122_154529:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240122_154531:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240122_154533:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240122_154536:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240122_154538:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240122_154540:cmsbot_crab_numCores - 0
scriptExe-check.sh 240122_154542:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240122_154545:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240122_154547:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240122_154633:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240122_154635:cmsbot_crab_inputDBS - 0
useParent-check.sh 240122_154637:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240122_154639:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240122_154641:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240122_154644:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240122_154647:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240122_154649:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240122_154652:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 240122_154656:cmsbot_crab_whitelist - 0
blacklist-check.sh 240122_154659:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240122_154701:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240122_154703:cmsbot_crab_voRole - 0
voGroup-check.sh 240122_154706:cmsbot_crab_voGroup - 0
scheddName-check.sh 240122_154708:cmsbot_crab_scheddName - 0
collector-check.sh 240122_154710:cmsbot_crab_collector - 0
extraJDL-check.sh 240122_154712:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-22T16:59:31Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-01-22 17:59:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/893/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240122_154519:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240122_154522:cmsbot_crab_transferLogs - 0
activity-check.sh 240122_154524:cmsbot_crab_activity - 0
inputFiles-check.sh 240122_154526:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240122_154529:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240122_154531:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240122_154533:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240122_154536:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240122_154538:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240122_154540:cmsbot_crab_numCores - 0
scriptExe-check.sh 240122_154542:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240122_154545:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240122_154547:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240122_154633:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240122_154635:cmsbot_crab_inputDBS - 0
useParent-check.sh 240122_154637:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240122_154639:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240122_154641:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240122_154644:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240122_154647:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240122_154649:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240122_154652:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240122_154654:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240122_154656:cmsbot_crab_whitelist - 0
blacklist-check.sh 240122_154659:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240122_154701:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240122_154703:cmsbot_crab_voRole - 0
voGroup-check.sh 240122_154706:cmsbot_crab_voGroup - 0
scheddName-check.sh 240122_154708:cmsbot_crab_scheddName - 0
collector-check.sh 240122_154710:cmsbot_crab_collector - 0
extraJDL-check.sh 240122_154712:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-22T17:10:51Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 2 out of 5. Test is done.
**Finished at:** 2024-01-22 18:10:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/739/console

```
{'TN': '240122_154716:cmsbot_crab_20240122_164715', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240122_154718:cmsbot_crab_20240122_164717', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240122_154720:cmsbot_crab_20240122_164720', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240122_154723:cmsbot_crab_20240122_164722', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240122_154725:cmsbot_crab_20240122_164724', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240122_154730:cmsbot_crab_20240122_164727', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240122_154733:cmsbot_crab_rucio_transfers_20240122_164731', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240122_154735:cmsbot_crab_rucio_transfers_group_20240122_164734', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240122_154738:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240122_164737', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154741:cmsbot_crab_rucio_transfers_nopublication_20240122_164740', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240122_154745:cmsbot_crab_rucio_transfers_withnoneedm_20240122_164743', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240122_154748:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240122_164746', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-01-23T08:52:17Z)

At last all of StatusTracking tests succeed, including Publication test
