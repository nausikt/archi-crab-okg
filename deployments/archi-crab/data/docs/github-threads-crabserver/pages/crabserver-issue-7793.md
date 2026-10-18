# dmwm/CRABServer issue #7793: #450: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-08-04T07:25:12Z
Closed: 2023-08-14T12:33:22Z
URL: https://github.com/dmwm/CRABServer/issues/7793

## Opening post (cmsdmwmbot, 2023-08-04T07:25:12Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-08-04 09:25:11
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/450/)

## Comment (cmsdmwmbot, 2023-08-04T07:27:37Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230804_072706:cmsbot_crab_20230804_092705
230804_072708:cmsbot_crab_20230804_092707
230804_072709:cmsbot_crab_20230804_092709
230804_072711:cmsbot_crab_20230804_092710
230804_072712:cmsbot_crab_20230804_092712
230804_072715:cmsbot_crab_20230804_092713
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230804_072533:cmsbot_crab_transferOutputs
230804_072535:cmsbot_crab_transferLogs
230804_072536:cmsbot_crab_activity
230804_072538:cmsbot_crab_inputFiles
230804_072540:cmsbot_crab_disableAutomaticOutputCollection
230804_072541:cmsbot_crab_outputFiles
230804_072543:cmsbot_crab_allowUndistributedCMSSW
230804_072544:cmsbot_crab_maxMemoryMB
230804_072546:cmsbot_crab_maxJobRuntimeMin
230804_072548:cmsbot_crab_numCores
230804_072549:cmsbot_crab_scriptExe
230804_072551:cmsbot_crab_scriptArgs
230804_072552:cmsbot_crab_sendPythonFolder
230804_072637:cmsbot_crab_sendExternalFolder
230804_072639:cmsbot_crab_inputDBS
230804_072640:cmsbot_crab_useParent
230804_072641:cmsbot_crab_secondaryInputDataset
230804_072643:cmsbot_crab_lumiMaskFile
230804_072645:cmsbot_crab_lumiMaskUrl
230804_072647:cmsbot_crab_outLFNDirBase
230804_072649:cmsbot_crab_runRange
230804_072650:cmsbot_crab_ignoreLocality
230804_072651:cmsbot_crab_userInputFiles
230804_072653:cmsbot_crab_whitelist
230804_072654:cmsbot_crab_blacklist
230804_072656:cmsbot_crab_ignoreGlobalBlacklist
230804_072658:cmsbot_crab_voRole
230804_072659:cmsbot_crab_voGroup
230804_072701:cmsbot_crab_scheddName
230804_072702:cmsbot_crab_collector
230804_072704:cmsbot_crab_extraJDL
```

Finished at: 2023-08-04 09:27:16
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/450/console)

## Comment (cmsdmwmbot, 2023-08-04T07:50:55Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-04 09:50:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/770/console

```
RETRY TESTS:
activity-check.sh 230804_072536:cmsbot_crab_activity - 2
maxJobRuntimeMin-check.sh 230804_072546:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 230804_072549:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 230804_072645:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230804_072649:cmsbot_crab_runRange - 2
whitelist-check.sh 230804_072653:cmsbot_crab_whitelist - 2
blacklist-check.sh 230804_072654:cmsbot_crab_blacklist - 2
voRole-check.sh 230804_072658:cmsbot_crab_voRole - 2
voGroup-check.sh 230804_072659:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230804_072533:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230804_072535:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230804_072538:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230804_072540:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230804_072541:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230804_072543:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230804_072544:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230804_072548:cmsbot_crab_numCores - 0
scriptArgs-check.sh 230804_072551:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230804_072552:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230804_072637:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230804_072639:cmsbot_crab_inputDBS - 0
useParent-check.sh 230804_072640:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230804_072641:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230804_072643:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230804_072647:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230804_072650:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230804_072651:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230804_072656:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 230804_072701:cmsbot_crab_scheddName - 0
collector-check.sh 230804_072702:cmsbot_crab_collector - 0
extraJDL-check.sh 230804_072704:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-04T08:14:01Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-08-04 10:14:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/772/console

```
RETRY TESTS:
runRange-check.sh 230804_072649:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230804_072533:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230804_072535:cmsbot_crab_transferLogs - 0
activity-check.sh 230804_072536:cmsbot_crab_activity - 0
inputFiles-check.sh 230804_072538:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230804_072540:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230804_072541:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230804_072543:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230804_072544:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230804_072546:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230804_072548:cmsbot_crab_numCores - 0
scriptExe-check.sh 230804_072549:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230804_072551:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230804_072552:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230804_072637:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230804_072639:cmsbot_crab_inputDBS - 0
useParent-check.sh 230804_072640:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230804_072641:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230804_072643:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230804_072645:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230804_072647:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230804_072650:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230804_072651:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230804_072653:cmsbot_crab_whitelist - 0
blacklist-check.sh 230804_072654:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230804_072656:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230804_072658:cmsbot_crab_voRole - 0
voGroup-check.sh 230804_072659:cmsbot_crab_voGroup - 0
scheddName-check.sh 230804_072701:cmsbot_crab_scheddName - 0
collector-check.sh 230804_072702:cmsbot_crab_collector - 0
extraJDL-check.sh 230804_072704:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-04T08:29:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-04 10:29:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/527/console

```
{'TN': '230804_072706:cmsbot_crab_20230804_092705', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 997, 'transferring': 1, 'running': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230804_072708:cmsbot_crab_20230804_092707', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230804_072709:cmsbot_crab_20230804_092709', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_072711:cmsbot_crab_20230804_092710', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_072712:cmsbot_crab_20230804_092712', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_072715:cmsbot_crab_20230804_092713', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-08-04T08:36:35Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-08-04 10:36:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/774/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230804_072533:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230804_072535:cmsbot_crab_transferLogs - 0
activity-check.sh 230804_072536:cmsbot_crab_activity - 0
inputFiles-check.sh 230804_072538:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230804_072540:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230804_072541:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230804_072543:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230804_072544:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230804_072546:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230804_072548:cmsbot_crab_numCores - 0
scriptExe-check.sh 230804_072549:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230804_072551:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230804_072552:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230804_072637:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230804_072639:cmsbot_crab_inputDBS - 0
useParent-check.sh 230804_072640:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230804_072641:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230804_072643:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230804_072645:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230804_072647:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230804_072649:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230804_072650:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230804_072651:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230804_072653:cmsbot_crab_whitelist - 0
blacklist-check.sh 230804_072654:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230804_072656:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230804_072658:cmsbot_crab_voRole - 0
voGroup-check.sh 230804_072659:cmsbot_crab_voGroup - 0
scheddName-check.sh 230804_072701:cmsbot_crab_scheddName - 0
collector-check.sh 230804_072702:cmsbot_crab_collector - 0
extraJDL-check.sh 230804_072704:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-04T09:33:04Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-08-04 11:33:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/529/console

```
{'TN': '230804_072706:cmsbot_crab_20230804_092705', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 998}, 'combinedStatus': 'FAILED'}
{'TN': '230804_072708:cmsbot_crab_20230804_092707', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_072709:cmsbot_crab_20230804_092709', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_072711:cmsbot_crab_20230804_092710', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_072712:cmsbot_crab_20230804_092712', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_072715:cmsbot_crab_20230804_092713', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```
