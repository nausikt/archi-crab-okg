# dmwm/CRABServer issue #7563: #379: Test prod CRABClient using test2 REST instance and CMSSW_12_0_1 CMSSW release

State: closed
Opened: 2023-03-11T16:43:51Z
Closed: 2023-03-11T21:08:10Z
URL: https://github.com/dmwm/CRABServer/issues/7563

## Opening post (cmsdmwmbot, 2023-03-11T16:43:51Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_0_1**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-03-11 17:43:50
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/379/)

## Comment (belforte, 2023-03-11T16:45:05Z)

this is to make sure that additions for processing a Rucio container did not break anything. Ref #7538 and #7556

## Comment (cmsdmwmbot, 2023-03-11T16:48:52Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230311_164755:cmsbot_crab_20230311_174752
230311_164758:cmsbot_crab_20230311_174756
230311_164802:cmsbot_crab_20230311_174759
230311_164805:cmsbot_crab_20230311_174803
230311_164809:cmsbot_crab_20230311_174806
230311_164830:cmsbot_crab_20230311_174810
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230311_164557:cmsbot_crab_transferOutputs
230311_164602:cmsbot_crab_transferLogs
230311_164605:cmsbot_crab_activity
230311_164610:cmsbot_crab_inputFiles
230311_164613:cmsbot_crab_disableAutomaticOutputCollection
230311_164616:cmsbot_crab_outputFiles
230311_164620:cmsbot_crab_allowUndistributedCMSSW
230311_164623:cmsbot_crab_maxMemoryMB
230311_164627:cmsbot_crab_maxJobRuntimeMin
230311_164630:cmsbot_crab_numCores
230311_164633:cmsbot_crab_scriptExe
230311_164637:cmsbot_crab_scriptArgs
230311_164640:cmsbot_crab_sendPythonFolder
230311_164652:cmsbot_crab_sendExternalFolder
230311_164656:cmsbot_crab_inputDBS
230311_164659:cmsbot_crab_useParent
230311_164703:cmsbot_crab_secondaryInputDataset
230311_164706:cmsbot_crab_lumiMaskFile
230311_164710:cmsbot_crab_lumiMaskUrl
230311_164714:cmsbot_crab_outLFNDirBase
230311_164717:cmsbot_crab_runRange
230311_164721:cmsbot_crab_ignoreLocality
230311_164724:cmsbot_crab_userInputFiles
230311_164727:cmsbot_crab_whitelist
230311_164731:cmsbot_crab_blacklist
230311_164734:cmsbot_crab_ignoreGlobalBlacklist
230311_164738:cmsbot_crab_voRole
230311_164741:cmsbot_crab_voGroup
230311_164744:cmsbot_crab_scheddName
230311_164747:cmsbot_crab_collector
230311_164751:cmsbot_crab_extraJDL
```

Finished at: 2023-03-11 17:48:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/379/console)

## Comment (cmsdmwmbot, 2023-03-11T17:15:06Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-03-11 18:15:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/590/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230311_164710:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230311_164717:cmsbot_crab_runRange - 2
whitelist-check.sh 230311_164727:cmsbot_crab_whitelist - 2
blacklist-check.sh 230311_164731:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230311_164734:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230311_164557:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230311_164602:cmsbot_crab_transferLogs - 0
activity-check.sh 230311_164605:cmsbot_crab_activity - 0
inputFiles-check.sh 230311_164610:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230311_164613:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230311_164616:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230311_164620:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230311_164623:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230311_164627:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230311_164630:cmsbot_crab_numCores - 0
scriptExe-check.sh 230311_164633:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230311_164637:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230311_164640:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230311_164652:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230311_164656:cmsbot_crab_inputDBS - 0
useParent-check.sh 230311_164659:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230311_164703:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230311_164706:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230311_164714:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230311_164721:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230311_164724:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230311_164738:cmsbot_crab_voRole - 0
voGroup-check.sh 230311_164741:cmsbot_crab_voGroup - 0
scheddName-check.sh 230311_164744:cmsbot_crab_scheddName - 0
collector-check.sh 230311_164747:cmsbot_crab_collector - 0
extraJDL-check.sh 230311_164751:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-03-11T17:41:28Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-03-11 18:41:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/591/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230311_164557:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230311_164602:cmsbot_crab_transferLogs - 0
activity-check.sh 230311_164605:cmsbot_crab_activity - 0
inputFiles-check.sh 230311_164610:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230311_164613:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230311_164616:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230311_164620:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230311_164623:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230311_164627:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230311_164630:cmsbot_crab_numCores - 0
scriptExe-check.sh 230311_164633:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230311_164637:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230311_164640:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230311_164652:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230311_164656:cmsbot_crab_inputDBS - 0
useParent-check.sh 230311_164659:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230311_164703:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230311_164706:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230311_164710:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230311_164714:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230311_164717:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230311_164721:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230311_164724:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230311_164727:cmsbot_crab_whitelist - 0
blacklist-check.sh 230311_164731:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230311_164734:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230311_164738:cmsbot_crab_voRole - 0
voGroup-check.sh 230311_164741:cmsbot_crab_voGroup - 0
scheddName-check.sh 230311_164744:cmsbot_crab_scheddName - 0
collector-check.sh 230311_164747:cmsbot_crab_collector - 0
extraJDL-check.sh 230311_164751:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-03-11T17:51:14Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-03-11 18:51:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/441/console

```
{'TN': '230311_164755:cmsbot_crab_20230311_174752', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 974, 'transferring': 11, 'running': 15}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230311_164758:cmsbot_crab_20230311_174756', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230311_164802:cmsbot_crab_20230311_174759', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230311_164805:cmsbot_crab_20230311_174803', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230311_164809:cmsbot_crab_20230311_174806', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 93, 'transferring': 5, 'running': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230311_164830:cmsbot_crab_20230311_174810', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-03-11T18:55:49Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-03-11 19:55:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/442/console

```
{'TN': '230311_164755:cmsbot_crab_20230311_174752', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 14, 'finished': 984, 'transferring': 1, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230311_164758:cmsbot_crab_20230311_174756', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 7}, 'combinedStatus': 'COMPLETED'}
{'TN': '230311_164802:cmsbot_crab_20230311_174759', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230311_164805:cmsbot_crab_20230311_174803', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230311_164809:cmsbot_crab_20230311_174806', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 98}, 'combinedStatus': 'FAILED'}
{'TN': '230311_164830:cmsbot_crab_20230311_174810', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-03-11T21:08:10Z)

the 2 failed out of 98 in `230311_164809:cmsbot_crab_20230311_174806` are a clear site problem
of the 15 failed out of 1000 in `230311_164755:cmsbot_crab_20230311_174752` , 10 were at same site as the 2 above, anyhow all hit the 1h running time timeout which indicates data read problems at the site.
ALL OK
