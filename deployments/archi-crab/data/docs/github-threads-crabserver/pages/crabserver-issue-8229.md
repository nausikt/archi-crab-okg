# dmwm/CRABServer issue #8229: #709: Test prod CRABClient using test2 REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2024-02-02T17:36:54Z
Closed: 2024-02-03T18:20:59Z
URL: https://github.com/dmwm/CRABServer/issues/8229

## Opening post (cmsdmwmbot, 2024-02-02T17:36:54Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-02-02 18:36:53
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/709/)

## Comment (cmsdmwmbot, 2024-02-02T17:39:10Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240202_173759:cmsbot_crab_20240202_183758
240202_173800:cmsbot_crab_20240202_183759
240202_173801:cmsbot_crab_20240202_183800
240202_173802:cmsbot_crab_20240202_183801
240202_173802:cmsbot_crab_20240202_183802
240202_173838:cmsbot_crab_20240202_183803
240202_173840:cmsbot_crab_rucio_transfers_20240202_183839
240202_173841:cmsbot_crab_rucio_transfers_group_20240202_183841
240202_173843:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_183842
240202_173845:cmsbot_crab_rucio_transfers_nopublication_20240202_183843
240202_173847:cmsbot_crab_rucio_transfers_withnoneedm_20240202_183845
240202_173848:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_183847
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_173726:cmsbot_crab_transferOutputs
240202_173727:cmsbot_crab_transferLogs
240202_173728:cmsbot_crab_activity
240202_173729:cmsbot_crab_inputFiles
240202_173730:cmsbot_crab_disableAutomaticOutputCollection
240202_173731:cmsbot_crab_outputFiles
240202_173731:cmsbot_crab_allowUndistributedCMSSW
240202_173732:cmsbot_crab_maxMemoryMB
240202_173733:cmsbot_crab_maxJobRuntimeMin
240202_173734:cmsbot_crab_numCores
240202_173735:cmsbot_crab_scriptExe
240202_173735:cmsbot_crab_scriptArgs
240202_173736:cmsbot_crab_sendVenvFolder
240202_173742:cmsbot_crab_sendExternalFolder
240202_173743:cmsbot_crab_inputDBS
240202_173744:cmsbot_crab_useParent
240202_173745:cmsbot_crab_secondaryInputDataset
240202_173746:cmsbot_crab_lumiMaskFile
240202_173747:cmsbot_crab_lumiMaskUrl
240202_173748:cmsbot_crab_outLFNDirBase
240202_173749:cmsbot_crab_runRange
240202_173750:cmsbot_crab_ignoreLocality
240202_173751:cmsbot_crab_userInputFiles
240202_173752:cmsbot_crab_whitelist
240202_173752:cmsbot_crab_blacklist
240202_173753:cmsbot_crab_ignoreGlobalBlacklist
240202_173754:cmsbot_crab_voRole
240202_173755:cmsbot_crab_voGroup
240202_173756:cmsbot_crab_scheddName
240202_173757:cmsbot_crab_collector
240202_173758:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 18:38:49
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/709/console)

## Comment (cmsdmwmbot, 2024-02-02T18:00:09Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 19:00:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/750/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 999}, 'TN': '240202_173759:cmsbot_crab_20240202_183758', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 5}, 'TN': '240202_173800:cmsbot_crab_20240202_183759', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240202_173801:cmsbot_crab_20240202_183800', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240202_173802:cmsbot_crab_20240202_183801', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 12, 'transferring': 88}, 'TN': '240202_173802:cmsbot_crab_20240202_183802', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 10}, 'TN': '240202_173838:cmsbot_crab_20240202_183803', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_173840:cmsbot_crab_rucio_transfers_20240202_183839', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 39}, 'TN': '240202_173841:cmsbot_crab_rucio_transfers_group_20240202_183841', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 39}, 'TN': '240202_173843:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_183842', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_173845:cmsbot_crab_rucio_transfers_nopublication_20240202_183843', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'transferring': 38}, 'TN': '240202_173847:cmsbot_crab_rucio_transfers_withnoneedm_20240202_183845', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'transferring': 38}, 'TN': '240202_173848:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_183847', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T18:03:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 19:03:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/945/console

```
RETRY TESTS:
outputFiles-check.sh 240202_173731:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240202_173733:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskUrl-check.sh 240202_173747:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240202_173748:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240202_173749:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240202_173751:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240202_173752:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_173752:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_173726:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_173727:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_173728:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_173729:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_173730:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240202_173731:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_173732:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 240202_173734:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_173735:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_173735:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_173736:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_173742:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_173743:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_173744:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_173745:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_173746:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240202_173750:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240202_173753:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_173754:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_173755:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_173756:cmsbot_crab_scheddName - 0
collector-check.sh 240202_173757:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_173758:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T18:16:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-02-02 19:16:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/751/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '240202_173759:cmsbot_crab_20240202_183758', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'TN': '240202_173800:cmsbot_crab_20240202_183759', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240202_173801:cmsbot_crab_20240202_183800', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240202_173802:cmsbot_crab_20240202_183801', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 99}, 'TN': '240202_173802:cmsbot_crab_20240202_183802', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'transferring': 9}, 'TN': '240202_173838:cmsbot_crab_20240202_183803', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'TN': '240202_173840:cmsbot_crab_rucio_transfers_20240202_183839', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'TN': '240202_173841:cmsbot_crab_rucio_transfers_group_20240202_183841', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'TN': '240202_173843:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_183842', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 35, 'transferring': 5}, 'TN': '240202_173845:cmsbot_crab_rucio_transfers_nopublication_20240202_183843', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'transferring': 38}, 'TN': '240202_173847:cmsbot_crab_rucio_transfers_withnoneedm_20240202_183845', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_173848:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_183847', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T18:28:50Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-02-02 19:28:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/949/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_173726:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_173727:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_173728:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_173729:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_173730:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_173731:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_173731:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_173732:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_173733:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_173734:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_173735:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_173735:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_173736:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_173742:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_173743:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_173744:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_173745:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_173746:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_173747:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_173748:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_173749:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_173750:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_173751:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_173752:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_173752:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_173753:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_173754:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_173755:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_173756:cmsbot_crab_scheddName - 0
collector-check.sh 240202_173757:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_173758:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T19:02:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-02-02 20:01:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/753/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240202_173759:cmsbot_crab_20240202_183758', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/900/900'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '240202_173800:cmsbot_crab_20240202_183759', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240202_173801:cmsbot_crab_20240202_183800', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_173802:cmsbot_crab_20240202_183801', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 99}, 'TN': '240202_173802:cmsbot_crab_20240202_183802', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/99/99'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'TN': '240202_173838:cmsbot_crab_20240202_183803', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/9/9'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173840:cmsbot_crab_rucio_transfers_20240202_183839', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173841:cmsbot_crab_rucio_transfers_group_20240202_183841', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173843:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_183842', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173845:cmsbot_crab_rucio_transfers_nopublication_20240202_183843', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173847:cmsbot_crab_rucio_transfers_withnoneedm_20240202_183845', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'TN': '240202_173848:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_183847', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T20:33:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-02-02 21:33:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/755/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240202_173759:cmsbot_crab_20240202_183758', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '240202_173800:cmsbot_crab_20240202_183759', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240202_173801:cmsbot_crab_20240202_183800', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_173802:cmsbot_crab_20240202_183801', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240202_173802:cmsbot_crab_20240202_183802', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_173838:cmsbot_crab_20240202_183803', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173840:cmsbot_crab_rucio_transfers_20240202_183839', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173841:cmsbot_crab_rucio_transfers_group_20240202_183841', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173843:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_183842', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173845:cmsbot_crab_rucio_transfers_nopublication_20240202_183843', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173847:cmsbot_crab_rucio_transfers_withnoneedm_20240202_183845', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173848:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_183847', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T22:35:43Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-02-02 23:35:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/756/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240202_173759:cmsbot_crab_20240202_183758', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '240202_173800:cmsbot_crab_20240202_183759', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240202_173801:cmsbot_crab_20240202_183800', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_173802:cmsbot_crab_20240202_183801', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240202_173802:cmsbot_crab_20240202_183802', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_173838:cmsbot_crab_20240202_183803', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173840:cmsbot_crab_rucio_transfers_20240202_183839', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173841:cmsbot_crab_rucio_transfers_group_20240202_183841', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173843:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_183842', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173845:cmsbot_crab_rucio_transfers_nopublication_20240202_183843', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173847:cmsbot_crab_rucio_transfers_withnoneedm_20240202_183845', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173848:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_183847', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-03T00:37:41Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-02-03 01:37:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/757/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240202_173759:cmsbot_crab_20240202_183758', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '240202_173800:cmsbot_crab_20240202_183759', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240202_173801:cmsbot_crab_20240202_183800', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_173802:cmsbot_crab_20240202_183801', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240202_173802:cmsbot_crab_20240202_183802', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_173838:cmsbot_crab_20240202_183803', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173840:cmsbot_crab_rucio_transfers_20240202_183839', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173841:cmsbot_crab_rucio_transfers_group_20240202_183841', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173843:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_183842', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173845:cmsbot_crab_rucio_transfers_nopublication_20240202_183843', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173847:cmsbot_crab_rucio_transfers_withnoneedm_20240202_183845', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173848:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_183847', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-03T18:12:11Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2024-02-03 19:12:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/758/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240202_173759:cmsbot_crab_20240202_183758', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '240202_173800:cmsbot_crab_20240202_183759', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240202_173801:cmsbot_crab_20240202_183800', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_173802:cmsbot_crab_20240202_183801', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240202_173802:cmsbot_crab_20240202_183802', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_173838:cmsbot_crab_20240202_183803', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173840:cmsbot_crab_rucio_transfers_20240202_183839', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173841:cmsbot_crab_rucio_transfers_group_20240202_183841', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173843:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_183842', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173845:cmsbot_crab_rucio_transfers_nopublication_20240202_183843', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173847:cmsbot_crab_rucio_transfers_withnoneedm_20240202_183845', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_173848:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_183847', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```
