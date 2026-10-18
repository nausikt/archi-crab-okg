# dmwm/CRABServer issue #7544: #376: Test prod CRABClient using preprod REST instance and CMSSW_12_6_0_pre4 CMSSW release

State: closed
Opened: 2023-02-20T16:45:13Z
Closed: 2023-02-22T17:31:05Z
URL: https://github.com/dmwm/CRABServer/issues/7544

## Opening post (cmsdmwmbot, 2023-02-20T16:45:13Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_0_pre4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-02-20 17:45:12
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/376/)

## Comment (cmsdmwmbot, 2023-02-20T16:47:37Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230220_164651:cmsbot_crab_20230220_174650
230220_164653:cmsbot_crab_20230220_174652
230220_164654:cmsbot_crab_20230220_174654
230220_164656:cmsbot_crab_20230220_174655
230220_164658:cmsbot_crab_20230220_174657
230220_164716:cmsbot_crab_20230220_174659
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230220_164554:cmsbot_crab_transferOutputs
230220_164555:cmsbot_crab_transferLogs
230220_164557:cmsbot_crab_activity
230220_164559:cmsbot_crab_inputFiles
230220_164600:cmsbot_crab_disableAutomaticOutputCollection
230220_164602:cmsbot_crab_outputFiles
230220_164604:cmsbot_crab_allowUndistributedCMSSW
230220_164605:cmsbot_crab_maxMemoryMB
230220_164607:cmsbot_crab_maxJobRuntimeMin
230220_164608:cmsbot_crab_numCores
230220_164610:cmsbot_crab_scriptExe
230220_164612:cmsbot_crab_scriptArgs
230220_164614:cmsbot_crab_sendPythonFolder
230220_164621:cmsbot_crab_sendExternalFolder
230220_164622:cmsbot_crab_inputDBS
230220_164624:cmsbot_crab_useParent
230220_164626:cmsbot_crab_secondaryInputDataset
230220_164627:cmsbot_crab_lumiMaskFile
230220_164629:cmsbot_crab_lumiMaskUrl
230220_164631:cmsbot_crab_outLFNDirBase
230220_164633:cmsbot_crab_runRange
230220_164635:cmsbot_crab_ignoreLocality
230220_164636:cmsbot_crab_userInputFiles
230220_164638:cmsbot_crab_whitelist
230220_164639:cmsbot_crab_blacklist
230220_164641:cmsbot_crab_ignoreGlobalBlacklist
230220_164642:cmsbot_crab_voRole
230220_164644:cmsbot_crab_voGroup
230220_164646:cmsbot_crab_scheddName
230220_164647:cmsbot_crab_collector
230220_164649:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230220_164552:cmsbot_crab_20230220_174551
```

Finished at: 2023-02-20 17:47:16
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/376/console)

## Comment (cmsdmwmbot, 2023-02-20T17:08:42Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-02-20 18:08:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/337/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/337//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-02-20T17:10:40Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-20 18:10:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/582/console

```
RETRY TESTS:
numCores-check.sh 230220_164608:cmsbot_crab_numCores - 2
scriptExe-check.sh 230220_164610:cmsbot_crab_scriptExe - 2
useParent-check.sh 230220_164624:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 230220_164629:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230220_164631:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230220_164633:cmsbot_crab_runRange - 2
whitelist-check.sh 230220_164638:cmsbot_crab_whitelist - 2
blacklist-check.sh 230220_164639:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230220_164554:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230220_164555:cmsbot_crab_transferLogs - 0
activity-check.sh 230220_164557:cmsbot_crab_activity - 0
inputFiles-check.sh 230220_164559:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230220_164600:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230220_164602:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230220_164604:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230220_164605:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230220_164607:cmsbot_crab_maxJobRuntimeMin - 0
sendPythonFolder-check.sh 230220_164614:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230220_164621:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230220_164622:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230220_164626:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230220_164627:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230220_164635:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230220_164641:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230220_164642:cmsbot_crab_voRole - 0
voGroup-check.sh 230220_164644:cmsbot_crab_voGroup - 0
scheddName-check.sh 230220_164646:cmsbot_crab_scheddName - 0
collector-check.sh 230220_164647:cmsbot_crab_collector - 0
extraJDL-check.sh 230220_164649:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptArgs-check.sh 230220_164612:cmsbot_crab_scriptArgs - 1
userInputFiles-check.sh 230220_164636:cmsbot_crab_userInputFiles - 1
```

## Comment (cmsdmwmbot, 2023-02-20T17:32:54Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-02-20 18:32:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/583/console

```
RETRY TESTS:
numCores-check.sh 230220_164608:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230220_164629:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230220_164631:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230220_164633:cmsbot_crab_runRange - 2
whitelist-check.sh 230220_164638:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230220_164554:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230220_164555:cmsbot_crab_transferLogs - 0
activity-check.sh 230220_164557:cmsbot_crab_activity - 0
inputFiles-check.sh 230220_164559:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230220_164600:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230220_164602:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230220_164604:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230220_164605:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230220_164607:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230220_164610:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230220_164614:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230220_164621:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230220_164622:cmsbot_crab_inputDBS - 0
useParent-check.sh 230220_164624:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230220_164626:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230220_164627:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230220_164635:cmsbot_crab_ignoreLocality - 0
blacklist-check.sh 230220_164639:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230220_164641:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230220_164642:cmsbot_crab_voRole - 0
voGroup-check.sh 230220_164644:cmsbot_crab_voGroup - 0
scheddName-check.sh 230220_164646:cmsbot_crab_scheddName - 0
collector-check.sh 230220_164647:cmsbot_crab_collector - 0
extraJDL-check.sh 230220_164649:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptArgs-check.sh 230220_164612:cmsbot_crab_scriptArgs - 1
userInputFiles-check.sh 230220_164636:cmsbot_crab_userInputFiles - 1
```

## Comment (cmsdmwmbot, 2023-02-20T17:50:09Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-20 18:50:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/437/console

```
{'TN': '230220_164651:cmsbot_crab_20230220_174650', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 27, 'finished': 535, 'transferring': 429, 'running': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230220_164653:cmsbot_crab_20230220_174652', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230220_164654:cmsbot_crab_20230220_174654', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230220_164656:cmsbot_crab_20230220_174655', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230220_164658:cmsbot_crab_20230220_174657', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 91, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230220_164716:cmsbot_crab_20230220_174659', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-02-20T17:55:02Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-02-20 18:55:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/584/console

```
RETRY TESTS:
numCores-check.sh 230220_164608:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230220_164629:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230220_164631:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230220_164633:cmsbot_crab_runRange - 2
whitelist-check.sh 230220_164638:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230220_164554:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230220_164555:cmsbot_crab_transferLogs - 0
activity-check.sh 230220_164557:cmsbot_crab_activity - 0
inputFiles-check.sh 230220_164559:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230220_164600:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230220_164602:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230220_164604:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230220_164605:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230220_164607:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230220_164610:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230220_164614:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230220_164621:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230220_164622:cmsbot_crab_inputDBS - 0
useParent-check.sh 230220_164624:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230220_164626:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230220_164627:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230220_164635:cmsbot_crab_ignoreLocality - 0
blacklist-check.sh 230220_164639:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230220_164641:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230220_164642:cmsbot_crab_voRole - 0
voGroup-check.sh 230220_164644:cmsbot_crab_voGroup - 0
scheddName-check.sh 230220_164646:cmsbot_crab_scheddName - 0
collector-check.sh 230220_164647:cmsbot_crab_collector - 0
extraJDL-check.sh 230220_164649:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptArgs-check.sh 230220_164612:cmsbot_crab_scriptArgs - 1
userInputFiles-check.sh 230220_164636:cmsbot_crab_userInputFiles - 1
```

## Comment (cmsdmwmbot, 2023-02-20T18:17:11Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-02-20 19:17:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/585/console

```
RETRY TESTS:
numCores-check.sh 230220_164608:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230220_164629:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230220_164631:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230220_164633:cmsbot_crab_runRange - 2
whitelist-check.sh 230220_164638:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230220_164554:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230220_164555:cmsbot_crab_transferLogs - 0
activity-check.sh 230220_164557:cmsbot_crab_activity - 0
inputFiles-check.sh 230220_164559:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230220_164600:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230220_164602:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230220_164604:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230220_164605:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230220_164607:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230220_164610:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230220_164614:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230220_164621:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230220_164622:cmsbot_crab_inputDBS - 0
useParent-check.sh 230220_164624:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230220_164626:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230220_164627:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230220_164635:cmsbot_crab_ignoreLocality - 0
blacklist-check.sh 230220_164639:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230220_164641:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230220_164642:cmsbot_crab_voRole - 0
voGroup-check.sh 230220_164644:cmsbot_crab_voGroup - 0
scheddName-check.sh 230220_164646:cmsbot_crab_scheddName - 0
collector-check.sh 230220_164647:cmsbot_crab_collector - 0
extraJDL-check.sh 230220_164649:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptArgs-check.sh 230220_164612:cmsbot_crab_scriptArgs - 1
userInputFiles-check.sh 230220_164636:cmsbot_crab_userInputFiles - 1
```

## Comment (cmsdmwmbot, 2023-02-20T18:39:15Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-02-20 19:39:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/586/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230220_164629:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230220_164631:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230220_164633:cmsbot_crab_runRange - 2
whitelist-check.sh 230220_164638:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230220_164554:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230220_164555:cmsbot_crab_transferLogs - 0
activity-check.sh 230220_164557:cmsbot_crab_activity - 0
inputFiles-check.sh 230220_164559:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230220_164600:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230220_164602:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230220_164604:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230220_164605:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230220_164607:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230220_164608:cmsbot_crab_numCores - 0
scriptExe-check.sh 230220_164610:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230220_164614:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230220_164621:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230220_164622:cmsbot_crab_inputDBS - 0
useParent-check.sh 230220_164624:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230220_164626:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230220_164627:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230220_164635:cmsbot_crab_ignoreLocality - 0
blacklist-check.sh 230220_164639:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230220_164641:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230220_164642:cmsbot_crab_voRole - 0
voGroup-check.sh 230220_164644:cmsbot_crab_voGroup - 0
scheddName-check.sh 230220_164646:cmsbot_crab_scheddName - 0
collector-check.sh 230220_164647:cmsbot_crab_collector - 0
extraJDL-check.sh 230220_164649:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptArgs-check.sh 230220_164612:cmsbot_crab_scriptArgs - 1
userInputFiles-check.sh 230220_164636:cmsbot_crab_userInputFiles - 1
```

## Comment (cmsdmwmbot, 2023-02-20T18:52:33Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-02-20 19:52:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/438/console

```
{'TN': '230220_164651:cmsbot_crab_20230220_174650', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 35, 'finished': 815, 'transferring': 150}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230220_164653:cmsbot_crab_20230220_174652', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 0, 'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230220_164654:cmsbot_crab_20230220_174654', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230220_164656:cmsbot_crab_20230220_174655', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230220_164658:cmsbot_crab_20230220_174657', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230220_164716:cmsbot_crab_20230220_174659', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (mapellidario, 2023-02-22T17:31:05Z)

These tests showed some issues that to not appear to be crab related, so I will close this issue

- [x] `230220_164651:cmsbot_crab_20230220_174650` has 35 jobs that failed, with a mixture of 8001, 50664 (max wall time) and 60317 (stuck stageout)
- [x] `230220_164653:cmsbot_crab_20230220_174652` has one job failing with 50664 (max wall time)
- [x] jobs from `230220_164612:cmsbot_crab_scriptArgs` and `230220_164636:cmsbot_crab_userInputFiles` failed with 8001 because they run at IRFU, site that was known to have file read errors in the last couple of days
