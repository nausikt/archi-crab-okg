# dmwm/CRABServer issue #7643: #391: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-05-24T14:55:44Z
Closed: 2023-05-25T08:30:39Z
URL: https://github.com/dmwm/CRABServer/issues/7643

## Opening post (cmsdmwmbot, 2023-05-24T14:55:44Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-05-24 16:55:43
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/391/)

## Comment (belforte, 2023-05-24T14:56:28Z)

basic test of new DBSDataDiscovery from https://github.com/belforte/CRABServer/tree/improve-rule-handling-for-7603

## Comment (cmsdmwmbot, 2023-05-24T14:58:42Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230524_145809:cmsbot_crab_20230524_165808
230524_145811:cmsbot_crab_20230524_165810
230524_145812:cmsbot_crab_20230524_165812
230524_145814:cmsbot_crab_20230524_165813
230524_145816:cmsbot_crab_20230524_165815
230524_145820:cmsbot_crab_20230524_165817
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230524_145617:cmsbot_crab_transferOutputs
230524_145619:cmsbot_crab_transferLogs
230524_145620:cmsbot_crab_activity
230524_145622:cmsbot_crab_inputFiles
230524_145624:cmsbot_crab_disableAutomaticOutputCollection
230524_145625:cmsbot_crab_outputFiles
230524_145627:cmsbot_crab_allowUndistributedCMSSW
230524_145629:cmsbot_crab_maxMemoryMB
230524_145630:cmsbot_crab_maxJobRuntimeMin
230524_145632:cmsbot_crab_numCores
230524_145634:cmsbot_crab_scriptExe
230524_145635:cmsbot_crab_scriptArgs
230524_145637:cmsbot_crab_sendPythonFolder
230524_145736:cmsbot_crab_sendExternalFolder
230524_145738:cmsbot_crab_inputDBS
230524_145739:cmsbot_crab_useParent
230524_145741:cmsbot_crab_secondaryInputDataset
230524_145743:cmsbot_crab_lumiMaskFile
230524_145745:cmsbot_crab_lumiMaskUrl
230524_145748:cmsbot_crab_outLFNDirBase
230524_145749:cmsbot_crab_runRange
230524_145751:cmsbot_crab_ignoreLocality
230524_145753:cmsbot_crab_userInputFiles
230524_145754:cmsbot_crab_whitelist
230524_145756:cmsbot_crab_blacklist
230524_145758:cmsbot_crab_ignoreGlobalBlacklist
230524_145759:cmsbot_crab_voRole
230524_145801:cmsbot_crab_voGroup
230524_145803:cmsbot_crab_scheddName
230524_145804:cmsbot_crab_collector
230524_145806:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230524_145615:cmsbot_crab_20230524_165605
```

Finished at: 2023-05-24 16:58:20
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/391/console)

## Comment (cmsdmwmbot, 2023-05-24T15:20:02Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-05-24 17:20:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/343/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/343//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-05-24T15:21:29Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-05-24 17:21:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/599/console

```
RETRY TESTS:
transferLogs-check.sh 230524_145619:cmsbot_crab_transferLogs - 2
activity-check.sh 230524_145620:cmsbot_crab_activity - 2
outputFiles-check.sh 230524_145625:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230524_145629:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 230524_145632:cmsbot_crab_numCores - 2
scriptArgs-check.sh 230524_145635:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 230524_145745:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230524_145748:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230524_145749:cmsbot_crab_runRange - 2
whitelist-check.sh 230524_145754:cmsbot_crab_whitelist - 2
blacklist-check.sh 230524_145756:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230524_145758:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230524_145617:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230524_145622:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230524_145624:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230524_145627:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230524_145630:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230524_145634:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230524_145637:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230524_145736:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230524_145738:cmsbot_crab_inputDBS - 0
useParent-check.sh 230524_145739:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230524_145741:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230524_145743:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230524_145751:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230524_145753:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 230524_145803:cmsbot_crab_scheddName - 0
collector-check.sh 230524_145804:cmsbot_crab_collector - 0
extraJDL-check.sh 230524_145806:cmsbot_crab_extraJDL - 0

FAILED TESTS:
voRole-check.sh 230524_145759:cmsbot_crab_voRole - 1
voGroup-check.sh 230524_145801:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2023-05-24T15:43:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-05-24 17:43:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/600/console

```
RETRY TESTS:
transferLogs-check.sh 230524_145619:cmsbot_crab_transferLogs - 2
activity-check.sh 230524_145620:cmsbot_crab_activity - 2
outputFiles-check.sh 230524_145625:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230524_145629:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 230524_145632:cmsbot_crab_numCores - 2
scriptArgs-check.sh 230524_145635:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 230524_145745:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230524_145749:cmsbot_crab_runRange - 2
whitelist-check.sh 230524_145754:cmsbot_crab_whitelist - 2
blacklist-check.sh 230524_145756:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230524_145758:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230524_145617:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230524_145622:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230524_145624:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230524_145627:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230524_145630:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230524_145634:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230524_145637:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230524_145736:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230524_145738:cmsbot_crab_inputDBS - 0
useParent-check.sh 230524_145739:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230524_145741:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230524_145743:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230524_145748:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230524_145751:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230524_145753:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 230524_145803:cmsbot_crab_scheddName - 0
collector-check.sh 230524_145804:cmsbot_crab_collector - 0
extraJDL-check.sh 230524_145806:cmsbot_crab_extraJDL - 0

FAILED TESTS:
voRole-check.sh 230524_145759:cmsbot_crab_voRole - 1
voGroup-check.sh 230524_145801:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2023-05-24T16:01:12Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-05-24 18:01:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/450/console

```
{'TN': '230524_145809:cmsbot_crab_20230524_165808', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 264, 'transferring': 724}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145811:cmsbot_crab_20230524_165810', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145812:cmsbot_crab_20230524_165812', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145814:cmsbot_crab_20230524_165813', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 4, 'transferring': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145816:cmsbot_crab_20230524_165815', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 11, 'finished': 28, 'transferring': 61}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145820:cmsbot_crab_20230524_165817', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-05-24T16:05:55Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-05-24 18:05:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/601/console

```
RETRY TESTS:
transferLogs-check.sh 230524_145619:cmsbot_crab_transferLogs - 2
activity-check.sh 230524_145620:cmsbot_crab_activity - 2
numCores-check.sh 230524_145632:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230524_145745:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230524_145749:cmsbot_crab_runRange - 2
whitelist-check.sh 230524_145754:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230524_145617:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230524_145622:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230524_145624:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230524_145625:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230524_145627:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230524_145629:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230524_145630:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230524_145634:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230524_145635:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230524_145637:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230524_145736:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230524_145738:cmsbot_crab_inputDBS - 0
useParent-check.sh 230524_145739:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230524_145741:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230524_145743:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230524_145748:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230524_145751:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230524_145753:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230524_145756:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230524_145758:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 230524_145803:cmsbot_crab_scheddName - 0
collector-check.sh 230524_145804:cmsbot_crab_collector - 0
extraJDL-check.sh 230524_145806:cmsbot_crab_extraJDL - 0

FAILED TESTS:
voRole-check.sh 230524_145759:cmsbot_crab_voRole - 1
voGroup-check.sh 230524_145801:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2023-05-24T16:28:12Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-05-24 18:28:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/602/console

```
RETRY TESTS:
transferLogs-check.sh 230524_145619:cmsbot_crab_transferLogs - 2
activity-check.sh 230524_145620:cmsbot_crab_activity - 2
lumiMaskUrl-check.sh 230524_145745:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230524_145749:cmsbot_crab_runRange - 2
whitelist-check.sh 230524_145754:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230524_145617:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230524_145622:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230524_145624:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230524_145625:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230524_145627:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230524_145629:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230524_145630:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230524_145634:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230524_145635:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230524_145637:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230524_145736:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230524_145738:cmsbot_crab_inputDBS - 0
useParent-check.sh 230524_145739:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230524_145741:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230524_145743:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230524_145748:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230524_145751:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230524_145753:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230524_145756:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230524_145758:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 230524_145803:cmsbot_crab_scheddName - 0
collector-check.sh 230524_145804:cmsbot_crab_collector - 0
extraJDL-check.sh 230524_145806:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 230524_145632:cmsbot_crab_numCores - 1
voRole-check.sh 230524_145759:cmsbot_crab_voRole - 1
voGroup-check.sh 230524_145801:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2023-05-24T16:50:30Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-05-24 18:50:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/603/console

```
RETRY TESTS:
transferLogs-check.sh 230524_145619:cmsbot_crab_transferLogs - 2
activity-check.sh 230524_145620:cmsbot_crab_activity - 2
lumiMaskUrl-check.sh 230524_145745:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230524_145749:cmsbot_crab_runRange - 2
whitelist-check.sh 230524_145754:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230524_145617:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230524_145622:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230524_145624:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230524_145625:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230524_145627:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230524_145629:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230524_145630:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230524_145634:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230524_145635:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230524_145637:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230524_145736:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230524_145738:cmsbot_crab_inputDBS - 0
useParent-check.sh 230524_145739:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230524_145741:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230524_145743:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230524_145748:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230524_145751:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230524_145753:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230524_145756:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230524_145758:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 230524_145803:cmsbot_crab_scheddName - 0
collector-check.sh 230524_145804:cmsbot_crab_collector - 0
extraJDL-check.sh 230524_145806:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 230524_145632:cmsbot_crab_numCores - 1
voRole-check.sh 230524_145759:cmsbot_crab_voRole - 1
voGroup-check.sh 230524_145801:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2023-05-24T17:03:52Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-05-24 19:03:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/451/console

```
{'TN': '230524_145809:cmsbot_crab_20230524_165808', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 315, 'transferring': 673}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145811:cmsbot_crab_20230524_165810', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145812:cmsbot_crab_20230524_165812', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145814:cmsbot_crab_20230524_165813', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 4, 'transferring': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145816:cmsbot_crab_20230524_165815', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 11, 'finished': 30, 'transferring': 59}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145820:cmsbot_crab_20230524_165817', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-05-24T18:09:37Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-05-24 20:09:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/452/console

```
{'TN': '230524_145809:cmsbot_crab_20230524_165808', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 318, 'transferring': 670}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145811:cmsbot_crab_20230524_165810', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145812:cmsbot_crab_20230524_165812', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145814:cmsbot_crab_20230524_165813', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 5, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145816:cmsbot_crab_20230524_165815', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 11, 'finished': 32, 'transferring': 57}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145820:cmsbot_crab_20230524_165817', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-05-24T19:13:51Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-05-24 21:13:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/453/console

```
{'TN': '230524_145809:cmsbot_crab_20230524_165808', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 336, 'transferring': 652}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145811:cmsbot_crab_20230524_165810', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145812:cmsbot_crab_20230524_165812', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145814:cmsbot_crab_20230524_165813', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 5, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145816:cmsbot_crab_20230524_165815', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 11, 'finished': 34, 'transferring': 55}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145820:cmsbot_crab_20230524_165817', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-05-24T20:17:50Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-05-24 22:17:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/454/console

```
{'TN': '230524_145809:cmsbot_crab_20230524_165808', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 349, 'transferring': 639}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145811:cmsbot_crab_20230524_165810', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145812:cmsbot_crab_20230524_165812', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145814:cmsbot_crab_20230524_165813', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 5, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145816:cmsbot_crab_20230524_165815', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 11, 'finished': 34, 'transferring': 55}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230524_145820:cmsbot_crab_20230524_165817', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-05-25T08:26:12Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2023-05-25 10:26:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/604/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230524_145617:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230524_145619:cmsbot_crab_transferLogs - 0
activity-check.sh 230524_145620:cmsbot_crab_activity - 0
inputFiles-check.sh 230524_145622:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230524_145624:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230524_145625:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230524_145627:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230524_145629:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230524_145630:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230524_145632:cmsbot_crab_numCores - 0
scriptExe-check.sh 230524_145634:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230524_145635:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230524_145637:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230524_145736:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230524_145738:cmsbot_crab_inputDBS - 0
useParent-check.sh 230524_145739:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230524_145741:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230524_145743:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230524_145745:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230524_145748:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230524_145749:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230524_145751:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230524_145753:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230524_145754:cmsbot_crab_whitelist - 0
blacklist-check.sh 230524_145756:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230524_145758:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230524_145759:cmsbot_crab_voRole - 0
voGroup-check.sh 230524_145801:cmsbot_crab_voGroup - 0
scheddName-check.sh 230524_145803:cmsbot_crab_scheddName - 0
collector-check.sh 230524_145804:cmsbot_crab_collector - 0
extraJDL-check.sh 230524_145806:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-05-25T08:30:39Z)

Tests OK
