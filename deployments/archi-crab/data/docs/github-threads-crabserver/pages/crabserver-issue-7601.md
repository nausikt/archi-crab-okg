# dmwm/CRABServer issue #7601: #384: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-04-17T15:28:31Z
Closed: 2023-05-04T16:39:30Z
URL: https://github.com/dmwm/CRABServer/issues/7601

## Opening post (cmsdmwmbot, 2023-04-17T15:28:31Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-04-17 17:28:30
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/384/)

## Comment (mapellidario, 2023-04-17T15:29:41Z)

just because I am paranoid, I started some tests on testbed to check the new robot certificate. everything looked ok on a simple hc task.

## Comment (cmsdmwmbot, 2023-04-17T15:31:44Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230417_153106:cmsbot_crab_20230417_173106
230417_153108:cmsbot_crab_20230417_173107
230417_153110:cmsbot_crab_20230417_173109
230417_153112:cmsbot_crab_20230417_173111
230417_153113:cmsbot_crab_20230417_173113
230417_153123:cmsbot_crab_20230417_173114
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230417_152921:cmsbot_crab_transferOutputs
230417_152923:cmsbot_crab_transferLogs
230417_152924:cmsbot_crab_activity
230417_152926:cmsbot_crab_inputFiles
230417_152928:cmsbot_crab_disableAutomaticOutputCollection
230417_152929:cmsbot_crab_outputFiles
230417_152931:cmsbot_crab_allowUndistributedCMSSW
230417_152933:cmsbot_crab_maxMemoryMB
230417_152934:cmsbot_crab_maxJobRuntimeMin
230417_152936:cmsbot_crab_numCores
230417_152937:cmsbot_crab_scriptExe
230417_152939:cmsbot_crab_scriptArgs
230417_152941:cmsbot_crab_sendPythonFolder
230417_153035:cmsbot_crab_sendExternalFolder
230417_153036:cmsbot_crab_inputDBS
230417_153038:cmsbot_crab_useParent
230417_153040:cmsbot_crab_secondaryInputDataset
230417_153041:cmsbot_crab_lumiMaskFile
230417_153043:cmsbot_crab_lumiMaskUrl
230417_153046:cmsbot_crab_outLFNDirBase
230417_153047:cmsbot_crab_runRange
230417_153049:cmsbot_crab_ignoreLocality
230417_153050:cmsbot_crab_userInputFiles
230417_153052:cmsbot_crab_whitelist
230417_153054:cmsbot_crab_blacklist
230417_153055:cmsbot_crab_ignoreGlobalBlacklist
230417_153057:cmsbot_crab_voRole
230417_153059:cmsbot_crab_voGroup
230417_153100:cmsbot_crab_scheddName
230417_153102:cmsbot_crab_collector
230417_153104:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230417_152919:cmsbot_crab_20230417_172918
```

Finished at: 2023-04-17 17:31:23
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/384/console)

## Comment (cmsdmwmbot, 2023-04-17T15:52:47Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-04-17 17:52:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/342/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/342//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-04-17T15:55:01Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-04-17 17:54:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/594/console

```
RETRY TESTS:
numCores-check.sh 230417_152936:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230417_153043:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230417_153047:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230417_153050:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230417_153052:cmsbot_crab_whitelist - 2
blacklist-check.sh 230417_153054:cmsbot_crab_blacklist - 2
voGroup-check.sh 230417_153059:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230417_152921:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230417_152923:cmsbot_crab_transferLogs - 0
activity-check.sh 230417_152924:cmsbot_crab_activity - 0
inputFiles-check.sh 230417_152926:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230417_152928:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230417_152929:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230417_152931:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230417_152933:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230417_152934:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230417_152937:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230417_152939:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230417_152941:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230417_153035:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230417_153036:cmsbot_crab_inputDBS - 0
useParent-check.sh 230417_153038:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230417_153040:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230417_153041:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230417_153046:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230417_153049:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230417_153055:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230417_153057:cmsbot_crab_voRole - 0
scheddName-check.sh 230417_153100:cmsbot_crab_scheddName - 0
collector-check.sh 230417_153102:cmsbot_crab_collector - 0
extraJDL-check.sh 230417_153104:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-04-17T16:17:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-04-17 18:17:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/595/console

```
RETRY TESTS:
numCores-check.sh 230417_152936:cmsbot_crab_numCores - 2
runRange-check.sh 230417_153047:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230417_152921:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230417_152923:cmsbot_crab_transferLogs - 0
activity-check.sh 230417_152924:cmsbot_crab_activity - 0
inputFiles-check.sh 230417_152926:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230417_152928:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230417_152929:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230417_152931:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230417_152933:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230417_152934:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230417_152937:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230417_152939:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230417_152941:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230417_153035:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230417_153036:cmsbot_crab_inputDBS - 0
useParent-check.sh 230417_153038:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230417_153040:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230417_153041:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230417_153043:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230417_153046:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230417_153049:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230417_153050:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230417_153052:cmsbot_crab_whitelist - 0
blacklist-check.sh 230417_153054:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230417_153055:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230417_153057:cmsbot_crab_voRole - 0
voGroup-check.sh 230417_153059:cmsbot_crab_voGroup - 0
scheddName-check.sh 230417_153100:cmsbot_crab_scheddName - 0
collector-check.sh 230417_153102:cmsbot_crab_collector - 0
extraJDL-check.sh 230417_153104:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-04-17T16:34:38Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-04-17 18:34:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/443/console

```
{'TN': '230417_153106:cmsbot_crab_20230417_173106', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 508, 'transferring': 488, 'running': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153108:cmsbot_crab_20230417_173107', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153110:cmsbot_crab_20230417_173109', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230417_153112:cmsbot_crab_20230417_173111', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153113:cmsbot_crab_20230417_173113', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 15, 'transferring': 85}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153123:cmsbot_crab_20230417_173114', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-04-17T16:39:41Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-04-17 18:39:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/596/console

```
RETRY TESTS:
numCores-check.sh 230417_152936:cmsbot_crab_numCores - 2
runRange-check.sh 230417_153047:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230417_152921:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230417_152923:cmsbot_crab_transferLogs - 0
activity-check.sh 230417_152924:cmsbot_crab_activity - 0
inputFiles-check.sh 230417_152926:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230417_152928:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230417_152929:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230417_152931:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230417_152933:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230417_152934:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230417_152937:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230417_152939:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230417_152941:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230417_153035:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230417_153036:cmsbot_crab_inputDBS - 0
useParent-check.sh 230417_153038:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230417_153040:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230417_153041:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230417_153043:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230417_153046:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230417_153049:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230417_153050:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230417_153052:cmsbot_crab_whitelist - 0
blacklist-check.sh 230417_153054:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230417_153055:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230417_153057:cmsbot_crab_voRole - 0
voGroup-check.sh 230417_153059:cmsbot_crab_voGroup - 0
scheddName-check.sh 230417_153100:cmsbot_crab_scheddName - 0
collector-check.sh 230417_153102:cmsbot_crab_collector - 0
extraJDL-check.sh 230417_153104:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-04-17T17:02:10Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-04-17 19:02:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/597/console

```
RETRY TESTS:
runRange-check.sh 230417_153047:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230417_152921:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230417_152923:cmsbot_crab_transferLogs - 0
activity-check.sh 230417_152924:cmsbot_crab_activity - 0
inputFiles-check.sh 230417_152926:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230417_152928:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230417_152929:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230417_152931:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230417_152933:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230417_152934:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230417_152936:cmsbot_crab_numCores - 0
scriptExe-check.sh 230417_152937:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230417_152939:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230417_152941:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230417_153035:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230417_153036:cmsbot_crab_inputDBS - 0
useParent-check.sh 230417_153038:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230417_153040:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230417_153041:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230417_153043:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230417_153046:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230417_153049:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230417_153050:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230417_153052:cmsbot_crab_whitelist - 0
blacklist-check.sh 230417_153054:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230417_153055:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230417_153057:cmsbot_crab_voRole - 0
voGroup-check.sh 230417_153059:cmsbot_crab_voGroup - 0
scheddName-check.sh 230417_153100:cmsbot_crab_scheddName - 0
collector-check.sh 230417_153102:cmsbot_crab_collector - 0
extraJDL-check.sh 230417_153104:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-04-17T17:24:37Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 4. Test is done.
**Finished at:** 2023-04-17 19:24:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/598/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230417_152921:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230417_152923:cmsbot_crab_transferLogs - 0
activity-check.sh 230417_152924:cmsbot_crab_activity - 0
inputFiles-check.sh 230417_152926:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230417_152928:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230417_152929:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230417_152931:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230417_152933:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230417_152934:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230417_152936:cmsbot_crab_numCores - 0
scriptExe-check.sh 230417_152937:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230417_152939:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230417_152941:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230417_153035:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230417_153036:cmsbot_crab_inputDBS - 0
useParent-check.sh 230417_153038:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230417_153040:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230417_153041:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230417_153043:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230417_153046:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230417_153047:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230417_153049:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230417_153050:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230417_153052:cmsbot_crab_whitelist - 0
blacklist-check.sh 230417_153054:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230417_153055:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230417_153057:cmsbot_crab_voRole - 0
voGroup-check.sh 230417_153059:cmsbot_crab_voGroup - 0
scheddName-check.sh 230417_153100:cmsbot_crab_scheddName - 0
collector-check.sh 230417_153102:cmsbot_crab_collector - 0
extraJDL-check.sh 230417_153104:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-04-17T17:37:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-04-17 19:36:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/444/console

```
{'TN': '230417_153106:cmsbot_crab_20230417_173106', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 3, 'finished': 771, 'transferring': 226}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153108:cmsbot_crab_20230417_173107', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230417_153110:cmsbot_crab_20230417_173109', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230417_153112:cmsbot_crab_20230417_173111', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153113:cmsbot_crab_20230417_173113', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 59, 'transferring': 41}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153123:cmsbot_crab_20230417_173114', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-04-17T18:41:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-04-17 20:41:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/445/console

```
{'TN': '230417_153106:cmsbot_crab_20230417_173106', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 3, 'finished': 867, 'transferring': 130}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153108:cmsbot_crab_20230417_173107', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230417_153110:cmsbot_crab_20230417_173109', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230417_153112:cmsbot_crab_20230417_173111', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153113:cmsbot_crab_20230417_173113', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 70, 'transferring': 30}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153123:cmsbot_crab_20230417_173114', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-04-17T19:43:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-04-17 21:43:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/446/console

```
{'TN': '230417_153106:cmsbot_crab_20230417_173106', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 3, 'finished': 868, 'transferring': 129}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153108:cmsbot_crab_20230417_173107', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230417_153110:cmsbot_crab_20230417_173109', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230417_153112:cmsbot_crab_20230417_173111', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153113:cmsbot_crab_20230417_173113', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 70, 'transferring': 30}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153123:cmsbot_crab_20230417_173114', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-04-17T20:46:39Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-04-17 22:46:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/447/console

```
{'TN': '230417_153106:cmsbot_crab_20230417_173106', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 3, 'finished': 976, 'transferring': 21}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153108:cmsbot_crab_20230417_173107', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230417_153110:cmsbot_crab_20230417_173109', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230417_153112:cmsbot_crab_20230417_173111', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153113:cmsbot_crab_20230417_173113', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 87, 'transferring': 13}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230417_153123:cmsbot_crab_20230417_173114', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (mapellidario, 2023-05-04T16:39:30Z)

All looks ok, closing
