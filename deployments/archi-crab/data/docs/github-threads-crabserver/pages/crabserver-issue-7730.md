# dmwm/CRABServer issue #7730: #431: Test dev CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-07-07T22:46:24Z
Closed: 2023-07-08T13:16:05Z
URL: https://github.com/dmwm/CRABServer/issues/7730

## Opening post (cmsdmwmbot, 2023-07-07T22:46:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-07-08 00:46:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/431/)

## Comment (cmsdmwmbot, 2023-07-07T22:47:56Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230707_224727:cmsbot_crab_20230708_004726
230707_224728:cmsbot_crab_20230708_004727
230707_224729:cmsbot_crab_20230708_004729
230707_224731:cmsbot_crab_20230708_004730
230707_224732:cmsbot_crab_20230708_004731
230707_224735:cmsbot_crab_20230708_004733
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230707_224643:cmsbot_crab_transferOutputs
230707_224645:cmsbot_crab_transferLogs
230707_224646:cmsbot_crab_activity
230707_224647:cmsbot_crab_inputFiles
230707_224648:cmsbot_crab_disableAutomaticOutputCollection
230707_224650:cmsbot_crab_outputFiles
230707_224651:cmsbot_crab_allowUndistributedCMSSW
230707_224652:cmsbot_crab_maxMemoryMB
230707_224653:cmsbot_crab_maxJobRuntimeMin
230707_224655:cmsbot_crab_numCores
230707_224656:cmsbot_crab_scriptExe
230707_224657:cmsbot_crab_scriptArgs
230707_224658:cmsbot_crab_sendPythonFolder
230707_224703:cmsbot_crab_sendExternalFolder
230707_224704:cmsbot_crab_inputDBS
230707_224705:cmsbot_crab_useParent
230707_224706:cmsbot_crab_secondaryInputDataset
230707_224708:cmsbot_crab_lumiMaskFile
230707_224709:cmsbot_crab_lumiMaskUrl
230707_224711:cmsbot_crab_outLFNDirBase
230707_224712:cmsbot_crab_runRange
230707_224714:cmsbot_crab_ignoreLocality
230707_224715:cmsbot_crab_userInputFiles
230707_224716:cmsbot_crab_whitelist
230707_224717:cmsbot_crab_blacklist
230707_224719:cmsbot_crab_ignoreGlobalBlacklist
230707_224720:cmsbot_crab_voRole
230707_224721:cmsbot_crab_voGroup
230707_224722:cmsbot_crab_scheddName
230707_224724:cmsbot_crab_collector
230707_224725:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230707_224642:cmsbot_crab_20230708_004641
```

Finished at: 2023-07-08 00:47:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/431/console)

## Comment (cmsdmwmbot, 2023-07-07T23:08:44Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-08 01:08:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/365/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/365//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-07T23:10:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-08 01:10:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/706/console

```
RETRY TESTS:
numCores-check.sh 230707_224655:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230707_224709:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230707_224712:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230707_224715:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230707_224716:cmsbot_crab_whitelist - 2
blacklist-check.sh 230707_224717:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_224643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_224645:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_224646:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_224647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_224648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_224650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_224651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_224652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_224653:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230707_224656:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_224657:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_224658:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_224703:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_224704:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_224705:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_224706:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_224708:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_224711:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_224714:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230707_224719:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_224720:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_224721:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_224722:cmsbot_crab_scheddName - 0
collector-check.sh 230707_224724:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_224725:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T23:32:21Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-08 01:32:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/707/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230707_224709:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230707_224712:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230707_224715:cmsbot_crab_userInputFiles - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_224643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_224645:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_224646:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_224647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_224648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_224650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_224651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_224652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_224653:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_224655:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_224656:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_224657:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_224658:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_224703:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_224704:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_224705:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_224706:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_224708:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_224711:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_224714:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 230707_224716:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_224717:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_224719:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_224720:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_224721:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_224722:cmsbot_crab_scheddName - 0
collector-check.sh 230707_224724:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_224725:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T23:49:55Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-08 01:49:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/488/console

```
{'TN': '230707_224727:cmsbot_crab_20230708_004726', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 7, 'finished': 984, 'transferring': 2, 'running': 7}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_224728:cmsbot_crab_20230708_004727', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_224729:cmsbot_crab_20230708_004729', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_224731:cmsbot_crab_20230708_004730', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_224732:cmsbot_crab_20230708_004731', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_224735:cmsbot_crab_20230708_004733', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-07T23:54:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-08 01:54:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/708/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230707_224709:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_224643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_224645:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_224646:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_224647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_224648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_224650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_224651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_224652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_224653:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_224655:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_224656:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_224657:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_224658:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_224703:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_224704:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_224705:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_224706:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_224708:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_224711:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_224712:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_224714:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_224715:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_224716:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_224717:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_224719:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_224720:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_224721:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_224722:cmsbot_crab_scheddName - 0
collector-check.sh 230707_224724:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_224725:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-08T00:16:08Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-08 02:16:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/709/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230707_224709:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_224643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_224645:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_224646:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_224647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_224648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_224650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_224651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_224652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_224653:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_224655:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_224656:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_224657:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_224658:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_224703:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_224704:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_224705:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_224706:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_224708:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_224711:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_224712:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_224714:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_224715:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_224716:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_224717:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_224719:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_224720:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_224721:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_224722:cmsbot_crab_scheddName - 0
collector-check.sh 230707_224724:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_224725:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-08T00:38:02Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-08 02:38:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/710/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230707_224709:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_224643:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_224645:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_224646:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_224647:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_224648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_224650:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_224651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_224652:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_224653:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_224655:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_224656:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_224657:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_224658:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_224703:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_224704:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_224705:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_224706:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_224708:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_224711:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_224712:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_224714:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_224715:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_224716:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_224717:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_224719:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_224720:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_224721:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_224722:cmsbot_crab_scheddName - 0
collector-check.sh 230707_224724:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_224725:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-08T00:52:05Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-08 02:52:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/489/console

```
{'TN': '230707_224727:cmsbot_crab_20230708_004726', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 7, 'finished': 993}, 'combinedStatus': 'FAILED'}
{'TN': '230707_224728:cmsbot_crab_20230708_004727', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_224729:cmsbot_crab_20230708_004729', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_224731:cmsbot_crab_20230708_004730', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_224732:cmsbot_crab_20230708_004731', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_224735:cmsbot_crab_20230708_004733', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-07-08T13:16:05Z)

all tests are OK in the end, but can't make Jenkins rerun after so much time.
