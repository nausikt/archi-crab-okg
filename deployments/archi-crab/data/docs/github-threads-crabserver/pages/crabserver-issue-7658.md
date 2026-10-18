# dmwm/CRABServer issue #7658: #393: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-10T14:43:33Z
Closed: 2023-06-29T20:27:19Z
URL: https://github.com/dmwm/CRABServer/issues/7658

## Opening post (cmsdmwmbot, 2023-06-10T14:43:33Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-06-10 16:43:32
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/393/)

## Comment (cmsdmwmbot, 2023-06-10T14:45:47Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230610_144518:cmsbot_crab_20230610_164517
230610_144519:cmsbot_crab_20230610_164518
230610_144520:cmsbot_crab_20230610_164520
230610_144522:cmsbot_crab_20230610_164521
230610_144523:cmsbot_crab_20230610_164522
230610_144526:cmsbot_crab_20230610_164524
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230610_144353:cmsbot_crab_transferOutputs
230610_144355:cmsbot_crab_transferLogs
230610_144356:cmsbot_crab_activity
230610_144357:cmsbot_crab_inputFiles
230610_144358:cmsbot_crab_disableAutomaticOutputCollection
230610_144400:cmsbot_crab_outputFiles
230610_144401:cmsbot_crab_allowUndistributedCMSSW
230610_144402:cmsbot_crab_maxMemoryMB
230610_144404:cmsbot_crab_maxJobRuntimeMin
230610_144405:cmsbot_crab_numCores
230610_144406:cmsbot_crab_scriptExe
230610_144408:cmsbot_crab_scriptArgs
230610_144409:cmsbot_crab_sendPythonFolder
230610_144450:cmsbot_crab_sendExternalFolder
230610_144452:cmsbot_crab_inputDBS
230610_144453:cmsbot_crab_useParent
230610_144454:cmsbot_crab_secondaryInputDataset
230610_144456:cmsbot_crab_lumiMaskFile
230610_144457:cmsbot_crab_lumiMaskUrl
230610_144459:cmsbot_crab_outLFNDirBase
230610_144501:cmsbot_crab_runRange
230610_144502:cmsbot_crab_ignoreLocality
230610_144504:cmsbot_crab_userInputFiles
230610_144505:cmsbot_crab_whitelist
230610_144507:cmsbot_crab_blacklist
230610_144508:cmsbot_crab_ignoreGlobalBlacklist
230610_144509:cmsbot_crab_voRole
230610_144511:cmsbot_crab_voGroup
230610_144513:cmsbot_crab_scheddName
230610_144514:cmsbot_crab_collector
230610_144515:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230610_144351:cmsbot_crab_20230610_164350
```

Finished at: 2023-06-10 16:45:26
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/393/console)

## Comment (cmsdmwmbot, 2023-06-10T15:07:54Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-10 17:07:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/345/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/345//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-10T15:09:07Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-10 17:09:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/608/console

```
RETRY TESTS:
numCores-check.sh 230610_144405:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230610_144457:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230610_144501:cmsbot_crab_runRange - 2
whitelist-check.sh 230610_144505:cmsbot_crab_whitelist - 2
blacklist-check.sh 230610_144507:cmsbot_crab_blacklist - 2
voGroup-check.sh 230610_144511:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230610_144353:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230610_144355:cmsbot_crab_transferLogs - 0
activity-check.sh 230610_144356:cmsbot_crab_activity - 0
inputFiles-check.sh 230610_144357:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230610_144358:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230610_144400:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230610_144401:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230610_144402:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230610_144404:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230610_144406:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230610_144408:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230610_144409:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230610_144450:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230610_144452:cmsbot_crab_inputDBS - 0
useParent-check.sh 230610_144453:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230610_144454:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230610_144456:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230610_144459:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230610_144502:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230610_144504:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230610_144508:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230610_144509:cmsbot_crab_voRole - 0
scheddName-check.sh 230610_144513:cmsbot_crab_scheddName - 0
collector-check.sh 230610_144514:cmsbot_crab_collector - 0
extraJDL-check.sh 230610_144515:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-10T15:31:07Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-10 17:31:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/609/console

```
RETRY TESTS:
numCores-check.sh 230610_144405:cmsbot_crab_numCores - 2
whitelist-check.sh 230610_144505:cmsbot_crab_whitelist - 2
blacklist-check.sh 230610_144507:cmsbot_crab_blacklist - 2
voGroup-check.sh 230610_144511:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230610_144353:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230610_144355:cmsbot_crab_transferLogs - 0
activity-check.sh 230610_144356:cmsbot_crab_activity - 0
inputFiles-check.sh 230610_144357:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230610_144358:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230610_144400:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230610_144401:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230610_144402:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230610_144404:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230610_144406:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230610_144408:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230610_144409:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230610_144450:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230610_144452:cmsbot_crab_inputDBS - 0
useParent-check.sh 230610_144453:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230610_144454:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230610_144456:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230610_144457:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230610_144459:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230610_144501:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230610_144502:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230610_144504:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230610_144508:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230610_144509:cmsbot_crab_voRole - 0
scheddName-check.sh 230610_144513:cmsbot_crab_scheddName - 0
collector-check.sh 230610_144514:cmsbot_crab_collector - 0
extraJDL-check.sh 230610_144515:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-10T15:48:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-10 17:48:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/457/console

```
{'TN': '230610_144518:cmsbot_crab_20230610_164517', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 970, 'transferring': 26, 'running': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230610_144519:cmsbot_crab_20230610_164518', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230610_144520:cmsbot_crab_20230610_164520', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230610_144522:cmsbot_crab_20230610_164521', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230610_144523:cmsbot_crab_20230610_164522', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230610_144526:cmsbot_crab_20230610_164524', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'finished': 9}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-06-10T15:53:11Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-10 17:53:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/610/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230610_144353:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230610_144355:cmsbot_crab_transferLogs - 0
activity-check.sh 230610_144356:cmsbot_crab_activity - 0
inputFiles-check.sh 230610_144357:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230610_144358:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230610_144400:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230610_144401:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230610_144402:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230610_144404:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230610_144406:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230610_144408:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230610_144409:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230610_144450:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230610_144452:cmsbot_crab_inputDBS - 0
useParent-check.sh 230610_144453:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230610_144454:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230610_144456:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230610_144457:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230610_144459:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230610_144501:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230610_144502:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230610_144504:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230610_144505:cmsbot_crab_whitelist - 0
blacklist-check.sh 230610_144507:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230610_144508:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230610_144509:cmsbot_crab_voRole - 0
voGroup-check.sh 230610_144511:cmsbot_crab_voGroup - 0
scheddName-check.sh 230610_144513:cmsbot_crab_scheddName - 0
collector-check.sh 230610_144514:cmsbot_crab_collector - 0
extraJDL-check.sh 230610_144515:cmsbot_crab_extraJDL - 0

FAILED TESTS:
numCores-check.sh 230610_144405:cmsbot_crab_numCores - 1
```

## Comment (cmsdmwmbot, 2023-06-10T16:52:16Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-10 18:52:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/458/console

```
{'TN': '230610_144518:cmsbot_crab_20230610_164517', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 3, 'finished': 997}, 'combinedStatus': 'FAILED'}
{'TN': '230610_144519:cmsbot_crab_20230610_164518', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230610_144520:cmsbot_crab_20230610_164520', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230610_144522:cmsbot_crab_20230610_164521', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230610_144523:cmsbot_crab_20230610_164522', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230610_144526:cmsbot_crab_20230610_164524', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 9}, 'combinedStatus': 'FAILED'}
```
