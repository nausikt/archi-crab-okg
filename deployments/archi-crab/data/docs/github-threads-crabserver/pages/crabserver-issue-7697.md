# dmwm/CRABServer issue #7697: #406: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-29T20:28:09Z
Closed: 2023-06-30T09:07:09Z
URL: https://github.com/dmwm/CRABServer/issues/7697

## Opening post (cmsdmwmbot, 2023-06-29T20:28:09Z)

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

Started at: 2023-06-29 22:28:08
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/406/)

## Comment (cmsdmwmbot, 2023-06-29T20:30:20Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230629_202951:cmsbot_crab_20230629_222950
230629_202952:cmsbot_crab_20230629_222951
230629_202953:cmsbot_crab_20230629_222953
230629_202955:cmsbot_crab_20230629_222954
230629_202956:cmsbot_crab_20230629_222956
230629_202959:cmsbot_crab_20230629_222957
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_202825:cmsbot_crab_transferOutputs
230629_202826:cmsbot_crab_transferLogs
230629_202828:cmsbot_crab_activity
230629_202829:cmsbot_crab_inputFiles
230629_202830:cmsbot_crab_disableAutomaticOutputCollection
230629_202832:cmsbot_crab_outputFiles
230629_202833:cmsbot_crab_allowUndistributedCMSSW
230629_202835:cmsbot_crab_maxMemoryMB
230629_202836:cmsbot_crab_maxJobRuntimeMin
230629_202837:cmsbot_crab_numCores
230629_202839:cmsbot_crab_scriptExe
230629_202841:cmsbot_crab_scriptArgs
230629_202842:cmsbot_crab_sendPythonFolder
230629_202924:cmsbot_crab_sendExternalFolder
230629_202925:cmsbot_crab_inputDBS
230629_202927:cmsbot_crab_useParent
230629_202928:cmsbot_crab_secondaryInputDataset
230629_202929:cmsbot_crab_lumiMaskFile
230629_202931:cmsbot_crab_lumiMaskUrl
230629_202933:cmsbot_crab_outLFNDirBase
230629_202935:cmsbot_crab_runRange
230629_202936:cmsbot_crab_ignoreLocality
230629_202937:cmsbot_crab_userInputFiles
230629_202939:cmsbot_crab_whitelist
230629_202940:cmsbot_crab_blacklist
230629_202941:cmsbot_crab_ignoreGlobalBlacklist
230629_202943:cmsbot_crab_voRole
230629_202944:cmsbot_crab_voGroup
230629_202946:cmsbot_crab_scheddName
230629_202947:cmsbot_crab_collector
230629_202948:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230629_202824:cmsbot_crab_20230629_222823
```

Finished at: 2023-06-29 22:29:59
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/406/console)

## Comment (cmsdmwmbot, 2023-06-29T20:52:14Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-29 22:52:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/349/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/349//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-29T20:53:17Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 22:53:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/634/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 230629_202836:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230629_202837:cmsbot_crab_numCores - 2
useParent-check.sh 230629_202927:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230629_202928:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 230629_202929:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230629_202931:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230629_202933:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230629_202935:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 230629_202936:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 230629_202937:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230629_202939:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_202940:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230629_202941:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230629_202943:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_202825:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_202826:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_202828:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_202829:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_202830:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_202832:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_202833:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_202835:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 230629_202839:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_202841:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_202842:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_202924:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_202925:cmsbot_crab_inputDBS - 0

FAILED TESTS:
voGroup-check.sh 230629_202944:cmsbot_crab_voGroup - 1
scheddName-check.sh 230629_202946:cmsbot_crab_scheddName - 1
collector-check.sh 230629_202947:cmsbot_crab_collector - 1
extraJDL-check.sh 230629_202948:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-06-29T21:15:01Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-29 23:15:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/641/console

```
RETRY TESTS:
numCores-check.sh 230629_202837:cmsbot_crab_numCores - 2
useParent-check.sh 230629_202927:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230629_202928:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 230629_202929:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230629_202931:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230629_202933:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230629_202935:cmsbot_crab_runRange - 2
whitelist-check.sh 230629_202939:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_202940:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_202825:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_202826:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_202828:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_202829:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_202830:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_202832:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_202833:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_202835:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_202836:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230629_202839:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_202841:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_202842:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_202924:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_202925:cmsbot_crab_inputDBS - 0
ignoreLocality-check.sh 230629_202936:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_202937:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230629_202941:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_202943:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_202944:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_202946:cmsbot_crab_scheddName - 0
collector-check.sh 230629_202947:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_202948:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T21:34:29Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 23:34:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/460/console

```
{'TN': '230629_202951:cmsbot_crab_20230629_222950', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 868, 'transferring': 132}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_202952:cmsbot_crab_20230629_222951', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_202953:cmsbot_crab_20230629_222953', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_202955:cmsbot_crab_20230629_222954', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_202956:cmsbot_crab_20230629_222956', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230629_202959:cmsbot_crab_20230629_222957', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-06-29T21:36:54Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-06-29 23:36:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/647/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_202825:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_202826:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_202828:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_202829:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_202830:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_202832:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_202833:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_202835:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_202836:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_202837:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_202839:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230629_202841:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230629_202842:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_202924:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_202925:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_202927:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_202928:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_202929:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_202931:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_202933:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_202935:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_202936:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_202937:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_202939:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_202940:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_202941:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_202943:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_202944:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_202946:cmsbot_crab_scheddName - 0
collector-check.sh 230629_202947:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_202948:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-29T22:36:42Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-06-30 00:36:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/462/console

```
{'TN': '230629_202951:cmsbot_crab_20230629_222950', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_202952:cmsbot_crab_20230629_222951', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_202953:cmsbot_crab_20230629_222953', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_202955:cmsbot_crab_20230629_222954', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_202956:cmsbot_crab_20230629_222956', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230629_202959:cmsbot_crab_20230629_222957', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```
