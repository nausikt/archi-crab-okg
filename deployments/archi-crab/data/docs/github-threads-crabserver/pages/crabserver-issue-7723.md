# dmwm/CRABServer issue #7723: #423: Test prod CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-07-07T16:27:34Z
Closed: 2023-07-07T20:29:17Z
URL: https://github.com/dmwm/CRABServer/issues/7723

## Opening post (cmsdmwmbot, 2023-07-07T16:27:34Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-07-07 18:27:33
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/423/)

## Comment (cmsdmwmbot, 2023-07-07T16:29:24Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230707_162854:cmsbot_crab_20230707_182854
230707_162855:cmsbot_crab_20230707_182855
230707_162857:cmsbot_crab_20230707_182856
230707_162858:cmsbot_crab_20230707_182858
230707_162900:cmsbot_crab_20230707_182859
230707_162902:cmsbot_crab_20230707_182900
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230707_162756:cmsbot_crab_transferOutputs
230707_162759:cmsbot_crab_transferLogs
230707_162800:cmsbot_crab_activity
230707_162806:cmsbot_crab_inputFiles
230707_162810:cmsbot_crab_disableAutomaticOutputCollection
230707_162811:cmsbot_crab_outputFiles
230707_162814:cmsbot_crab_allowUndistributedCMSSW
230707_162815:cmsbot_crab_maxMemoryMB
230707_162816:cmsbot_crab_maxJobRuntimeMin
230707_162818:cmsbot_crab_numCores
230707_162820:cmsbot_crab_scriptExe
230707_162821:cmsbot_crab_scriptArgs
230707_162823:cmsbot_crab_sendPythonFolder
230707_162828:cmsbot_crab_sendExternalFolder
230707_162829:cmsbot_crab_inputDBS
230707_162830:cmsbot_crab_useParent
230707_162832:cmsbot_crab_secondaryInputDataset
230707_162833:cmsbot_crab_lumiMaskFile
230707_162835:cmsbot_crab_lumiMaskUrl
230707_162837:cmsbot_crab_outLFNDirBase
230707_162839:cmsbot_crab_runRange
230707_162840:cmsbot_crab_ignoreLocality
230707_162841:cmsbot_crab_userInputFiles
230707_162843:cmsbot_crab_whitelist
230707_162844:cmsbot_crab_blacklist
230707_162845:cmsbot_crab_ignoreGlobalBlacklist
230707_162847:cmsbot_crab_voRole
230707_162848:cmsbot_crab_voGroup
230707_162849:cmsbot_crab_scheddName
230707_162851:cmsbot_crab_collector
230707_162852:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230707_162753:cmsbot_crab_20230707_182752
```

Finished at: 2023-07-07 18:29:03
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/423/console)

## Comment (cmsdmwmbot, 2023-07-07T16:50:22Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-07 18:50:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/359/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/359//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-07T16:51:12Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 18:51:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/678/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 230707_162832:cmsbot_crab_secondaryInputDataset - 2
runRange-check.sh 230707_162839:cmsbot_crab_runRange - 2
whitelist-check.sh 230707_162843:cmsbot_crab_whitelist - 2
blacklist-check.sh 230707_162844:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_162756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_162759:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_162800:cmsbot_crab_activity - 0
disableAutomaticOutputCollection-check.sh 230707_162810:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230707_162814:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_162815:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230707_162818:cmsbot_crab_numCores - 0
scriptArgs-check.sh 230707_162821:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_162823:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_162828:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 230707_162830:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230707_162833:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230707_162840:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_162841:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230707_162847:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_162848:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_162849:cmsbot_crab_scheddName - 0
extraJDL-check.sh 230707_162852:cmsbot_crab_extraJDL - 0

FAILED TESTS:
inputFiles-check.sh 230707_162806:cmsbot_crab_inputFiles - 1
outputFiles-check.sh 230707_162811:cmsbot_crab_outputFiles - 1
maxJobRuntimeMin-check.sh 230707_162816:cmsbot_crab_maxJobRuntimeMin - 1
scriptExe-check.sh 230707_162820:cmsbot_crab_scriptExe - 1
inputDBS-check.sh 230707_162829:cmsbot_crab_inputDBS - 1
lumiMaskUrl-check.sh 230707_162835:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230707_162837:cmsbot_crab_outLFNDirBase - 1
ignoreGlobalBlacklist-check.sh 230707_162845:cmsbot_crab_ignoreGlobalBlacklist - 1
collector-check.sh 230707_162851:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2023-07-07T17:13:13Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-07 19:13:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/682/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 230707_162816:cmsbot_crab_maxJobRuntimeMin - 2
secondaryInputDataset-check.sh 230707_162832:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230707_162835:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230707_162839:cmsbot_crab_runRange - 2
whitelist-check.sh 230707_162843:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_162756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_162759:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_162800:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_162806:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_162810:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_162811:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_162814:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_162815:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230707_162818:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_162820:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_162821:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_162823:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_162828:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_162829:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_162830:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230707_162833:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_162837:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_162840:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_162841:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230707_162844:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_162845:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_162847:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_162848:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_162849:cmsbot_crab_scheddName - 0
collector-check.sh 230707_162851:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_162852:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T17:31:36Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 19:31:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/469/console

```
{'TN': '230707_162854:cmsbot_crab_20230707_182854', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 3, 'finished': 952, 'transferring': 4, 'running': 41}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_162855:cmsbot_crab_20230707_182855', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_162857:cmsbot_crab_20230707_182856', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162858:cmsbot_crab_20230707_182858', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162900:cmsbot_crab_20230707_182859', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162902:cmsbot_crab_20230707_182900', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-07T17:35:17Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-07 19:35:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/686/console

```
RETRY TESTS:
runRange-check.sh 230707_162839:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_162756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_162759:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_162800:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_162806:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_162810:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_162811:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_162814:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_162815:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_162816:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_162818:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_162820:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_162821:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_162823:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_162828:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_162829:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_162830:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_162832:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_162833:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_162835:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_162837:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_162840:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_162841:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_162843:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_162844:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_162845:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_162847:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_162848:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_162849:cmsbot_crab_scheddName - 0
collector-check.sh 230707_162851:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_162852:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T17:57:19Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-07 19:57:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/691/console

```
RETRY TESTS:
runRange-check.sh 230707_162839:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_162756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_162759:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_162800:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_162806:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_162810:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_162811:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_162814:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_162815:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_162816:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_162818:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_162820:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_162821:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_162823:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_162828:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_162829:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_162830:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_162832:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_162833:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_162835:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_162837:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_162840:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_162841:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_162843:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_162844:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_162845:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_162847:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_162848:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_162849:cmsbot_crab_scheddName - 0
collector-check.sh 230707_162851:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_162852:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T18:24:06Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 4. Test is done.
**Finished at:** 2023-07-07 20:24:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/696/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_162756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_162759:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_162800:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_162806:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_162810:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_162811:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_162814:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_162815:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_162816:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_162818:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_162820:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_162821:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_162823:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_162828:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_162829:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_162830:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_162832:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_162833:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_162835:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_162837:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_162839:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_162840:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_162841:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_162843:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_162844:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_162845:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_162847:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_162848:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_162849:cmsbot_crab_scheddName - 0
collector-check.sh 230707_162851:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_162852:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T18:33:42Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-07 20:33:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/474/console

```
{'TN': '230707_162854:cmsbot_crab_20230707_182854', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 3, 'finished': 997}, 'combinedStatus': 'FAILED'}
{'TN': '230707_162855:cmsbot_crab_20230707_182855', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162857:cmsbot_crab_20230707_182856', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162858:cmsbot_crab_20230707_182858', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162900:cmsbot_crab_20230707_182859', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162902:cmsbot_crab_20230707_182900', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-07-07T19:37:35Z)

resubmitted the 3 failed in 230707_162854:cmsbot_crab_20230707_182854

## Comment (cmsdmwmbot, 2023-07-07T20:26:11Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 0. Test is done.
**Finished at:** 2023-07-07 22:26:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/482/console

```
{'TN': '230707_162854:cmsbot_crab_20230707_182854', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162855:cmsbot_crab_20230707_182855', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162857:cmsbot_crab_20230707_182856', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162858:cmsbot_crab_20230707_182858', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162900:cmsbot_crab_20230707_182859', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_162902:cmsbot_crab_20230707_182900', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```
