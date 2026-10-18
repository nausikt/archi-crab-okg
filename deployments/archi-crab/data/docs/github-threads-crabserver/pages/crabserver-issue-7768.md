# dmwm/CRABServer issue #7768: #443: Test prod CRABClient using test11 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-17T20:55:40Z
Closed: 2023-07-19T12:38:40Z
URL: https://github.com/dmwm/CRABServer/issues/7768

## Opening post (cmsdmwmbot, 2023-07-17T20:55:40Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test11**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-07-17 22:55:40
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/443/)

## Comment (cmsdmwmbot, 2023-07-17T20:57:51Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230717_205722:cmsbot_crab_20230717_225721
230717_205723:cmsbot_crab_20230717_225722
230717_205724:cmsbot_crab_20230717_225724
230717_205726:cmsbot_crab_20230717_225725
230717_205727:cmsbot_crab_20230717_225726
230717_205730:cmsbot_crab_20230717_225728
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230717_205559:cmsbot_crab_transferOutputs
230717_205601:cmsbot_crab_transferLogs
230717_205602:cmsbot_crab_activity
230717_205604:cmsbot_crab_inputFiles
230717_205605:cmsbot_crab_disableAutomaticOutputCollection
230717_205606:cmsbot_crab_outputFiles
230717_205608:cmsbot_crab_allowUndistributedCMSSW
230717_205609:cmsbot_crab_maxMemoryMB
230717_205610:cmsbot_crab_maxJobRuntimeMin
230717_205611:cmsbot_crab_numCores
230717_205613:cmsbot_crab_scriptExe
230717_205614:cmsbot_crab_scriptArgs
230717_205615:cmsbot_crab_sendPythonFolder
230717_205656:cmsbot_crab_sendExternalFolder
230717_205657:cmsbot_crab_inputDBS
230717_205659:cmsbot_crab_useParent
230717_205700:cmsbot_crab_secondaryInputDataset
230717_205701:cmsbot_crab_lumiMaskFile
230717_205703:cmsbot_crab_lumiMaskUrl
230717_205705:cmsbot_crab_outLFNDirBase
230717_205706:cmsbot_crab_runRange
230717_205708:cmsbot_crab_ignoreLocality
230717_205709:cmsbot_crab_userInputFiles
230717_205710:cmsbot_crab_whitelist
230717_205712:cmsbot_crab_blacklist
230717_205713:cmsbot_crab_ignoreGlobalBlacklist
230717_205714:cmsbot_crab_voRole
230717_205715:cmsbot_crab_voGroup
230717_205717:cmsbot_crab_scheddName
230717_205718:cmsbot_crab_collector
230717_205719:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230717_205558:cmsbot_crab_20230717_225557
```

Finished at: 2023-07-17 22:57:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/443/console)

## Comment (mapellidario, 2023-07-17T20:59:07Z)

testing https://github.com/dmwm/CRABServer/compare/master...mapellidario:20230717_py3htc10 on an image with htcondor

I wanted to run some tests, after a simple submissions worked fine. Next step: remove htcondor from that container and try again.

## Comment (cmsdmwmbot, 2023-07-17T21:20:15Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-17 23:20:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/368/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/368//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-17T21:21:12Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-17 23:21:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/741/console

```
RETRY TESTS:
disableAutomaticOutputCollection-check.sh 230717_205605:cmsbot_crab_disableAutomaticOutputCollection - 2
maxMemoryMB-check.sh 230717_205609:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 230717_205611:cmsbot_crab_numCores - 2
useParent-check.sh 230717_205659:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 230717_205703:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230717_205706:cmsbot_crab_runRange - 2
whitelist-check.sh 230717_205710:cmsbot_crab_whitelist - 2
blacklist-check.sh 230717_205712:cmsbot_crab_blacklist - 2
voGroup-check.sh 230717_205715:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230717_205559:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230717_205601:cmsbot_crab_transferLogs - 0
activity-check.sh 230717_205602:cmsbot_crab_activity - 0
inputFiles-check.sh 230717_205604:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 230717_205606:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230717_205608:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230717_205610:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230717_205613:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230717_205614:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230717_205615:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230717_205656:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230717_205657:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230717_205700:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230717_205701:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230717_205705:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230717_205708:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230717_205709:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230717_205713:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230717_205714:cmsbot_crab_voRole - 0
scheddName-check.sh 230717_205717:cmsbot_crab_scheddName - 0
collector-check.sh 230717_205718:cmsbot_crab_collector - 0
extraJDL-check.sh 230717_205719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-17T21:43:18Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-17 23:43:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/742/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230717_205609:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 230717_205611:cmsbot_crab_numCores - 2
useParent-check.sh 230717_205659:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 230717_205703:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230717_205706:cmsbot_crab_runRange - 2
whitelist-check.sh 230717_205710:cmsbot_crab_whitelist - 2
voGroup-check.sh 230717_205715:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230717_205559:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230717_205601:cmsbot_crab_transferLogs - 0
activity-check.sh 230717_205602:cmsbot_crab_activity - 0
inputFiles-check.sh 230717_205604:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230717_205605:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230717_205606:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230717_205608:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230717_205610:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230717_205613:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230717_205614:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230717_205615:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230717_205656:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230717_205657:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230717_205700:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230717_205701:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230717_205705:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230717_205708:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230717_205709:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230717_205712:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230717_205713:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230717_205714:cmsbot_crab_voRole - 0
scheddName-check.sh 230717_205717:cmsbot_crab_scheddName - 0
collector-check.sh 230717_205718:cmsbot_crab_collector - 0
extraJDL-check.sh 230717_205719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-17T22:01:37Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-18 00:01:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/500/console

```
{'TN': '230717_205722:cmsbot_crab_20230717_225721', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 327, 'transferring': 661}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205723:cmsbot_crab_20230717_225722', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205724:cmsbot_crab_20230717_225724', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230717_205726:cmsbot_crab_20230717_225725', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 3, 'transferring': 7}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205727:cmsbot_crab_20230717_225726', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 25, 'transferring': 75}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205730:cmsbot_crab_20230717_225728', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 3, 'transferring': 7}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-17T22:05:17Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-18 00:05:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/743/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230717_205609:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 230717_205611:cmsbot_crab_numCores - 2
useParent-check.sh 230717_205659:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 230717_205703:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230717_205706:cmsbot_crab_runRange - 2
whitelist-check.sh 230717_205710:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230717_205559:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230717_205601:cmsbot_crab_transferLogs - 0
activity-check.sh 230717_205602:cmsbot_crab_activity - 0
inputFiles-check.sh 230717_205604:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230717_205605:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230717_205606:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230717_205608:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230717_205610:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230717_205613:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230717_205614:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230717_205615:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230717_205656:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230717_205657:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230717_205700:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230717_205701:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230717_205705:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230717_205708:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230717_205709:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230717_205712:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230717_205713:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230717_205714:cmsbot_crab_voRole - 0
voGroup-check.sh 230717_205715:cmsbot_crab_voGroup - 0
scheddName-check.sh 230717_205717:cmsbot_crab_scheddName - 0
collector-check.sh 230717_205718:cmsbot_crab_collector - 0
extraJDL-check.sh 230717_205719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-17T22:27:08Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-18 00:27:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/744/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230717_205609:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 230717_205611:cmsbot_crab_numCores - 2
useParent-check.sh 230717_205659:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 230717_205703:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230717_205706:cmsbot_crab_runRange - 2
whitelist-check.sh 230717_205710:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230717_205559:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230717_205601:cmsbot_crab_transferLogs - 0
activity-check.sh 230717_205602:cmsbot_crab_activity - 0
inputFiles-check.sh 230717_205604:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230717_205605:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230717_205606:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230717_205608:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230717_205610:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230717_205613:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230717_205614:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230717_205615:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230717_205656:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230717_205657:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230717_205700:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230717_205701:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230717_205705:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230717_205708:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230717_205709:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230717_205712:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230717_205713:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230717_205714:cmsbot_crab_voRole - 0
voGroup-check.sh 230717_205715:cmsbot_crab_voGroup - 0
scheddName-check.sh 230717_205717:cmsbot_crab_scheddName - 0
collector-check.sh 230717_205718:cmsbot_crab_collector - 0
extraJDL-check.sh 230717_205719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-17T22:48:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-18 00:48:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/745/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230717_205609:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 230717_205611:cmsbot_crab_numCores - 2
useParent-check.sh 230717_205659:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 230717_205703:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230717_205706:cmsbot_crab_runRange - 2
whitelist-check.sh 230717_205710:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230717_205559:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230717_205601:cmsbot_crab_transferLogs - 0
activity-check.sh 230717_205602:cmsbot_crab_activity - 0
inputFiles-check.sh 230717_205604:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230717_205605:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230717_205606:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230717_205608:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230717_205610:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230717_205613:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230717_205614:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230717_205615:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230717_205656:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230717_205657:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230717_205700:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230717_205701:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230717_205705:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230717_205708:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230717_205709:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230717_205712:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230717_205713:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230717_205714:cmsbot_crab_voRole - 0
voGroup-check.sh 230717_205715:cmsbot_crab_voGroup - 0
scheddName-check.sh 230717_205717:cmsbot_crab_scheddName - 0
collector-check.sh 230717_205718:cmsbot_crab_collector - 0
extraJDL-check.sh 230717_205719:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-17T23:03:49Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-18 01:03:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/501/console

```
{'TN': '230717_205722:cmsbot_crab_20230717_225721', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 412, 'transferring': 576}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205723:cmsbot_crab_20230717_225722', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205724:cmsbot_crab_20230717_225724', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230717_205726:cmsbot_crab_20230717_225725', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205727:cmsbot_crab_20230717_225726', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 44, 'transferring': 56}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205730:cmsbot_crab_20230717_225728', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-18T00:07:30Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-18 02:07:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/502/console

```
{'TN': '230717_205722:cmsbot_crab_20230717_225721', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 510, 'transferring': 478}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205723:cmsbot_crab_20230717_225722', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205724:cmsbot_crab_20230717_225724', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230717_205726:cmsbot_crab_20230717_225725', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205727:cmsbot_crab_20230717_225726', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 48, 'transferring': 52}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205730:cmsbot_crab_20230717_225728', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-18T01:10:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-18 03:10:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/503/console

```
{'TN': '230717_205722:cmsbot_crab_20230717_225721', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 763, 'transferring': 225}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205723:cmsbot_crab_20230717_225722', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205724:cmsbot_crab_20230717_225724', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230717_205726:cmsbot_crab_20230717_225725', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205727:cmsbot_crab_20230717_225726', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 68, 'transferring': 32}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205730:cmsbot_crab_20230717_225728', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-18T02:13:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-18 04:13:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/504/console

```
{'TN': '230717_205722:cmsbot_crab_20230717_225721', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 12, 'finished': 787, 'transferring': 201}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205723:cmsbot_crab_20230717_225722', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205724:cmsbot_crab_20230717_225724', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230717_205726:cmsbot_crab_20230717_225725', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205727:cmsbot_crab_20230717_225726', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 70, 'transferring': 30}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230717_205730:cmsbot_crab_20230717_225728', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (mapellidario, 2023-07-18T08:21:00Z)

looks ok, but i will have a better look later

## Comment (mapellidario, 2023-07-19T12:38:40Z)

Status tracking

- 230717_205722:cmsbot_crab_20230717_225721 : 12 jobs failed at irfu, 8001, not related to the changes

CCV: all ok.

problems not related to these changes. We can close this
