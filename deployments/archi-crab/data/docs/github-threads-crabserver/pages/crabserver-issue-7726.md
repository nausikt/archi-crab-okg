# dmwm/CRABServer issue #7726: #427: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2023-07-07T16:36:15Z
Closed: 2023-07-07T19:48:46Z
URL: https://github.com/dmwm/CRABServer/issues/7726

## Opening post (cmsdmwmbot, 2023-07-07T16:36:15Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-07-07 18:36:15
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/427/)

## Comment (cmsdmwmbot, 2023-07-07T16:40:08Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230707_163919:cmsbot_crab_20230707_183915
230707_163922:cmsbot_crab_20230707_183919
230707_163926:cmsbot_crab_20230707_183923
230707_163930:cmsbot_crab_20230707_183926
230707_163934:cmsbot_crab_20230707_183930
230707_163946:cmsbot_crab_20230707_183934
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230707_163743:cmsbot_crab_transferOutputs
230707_163745:cmsbot_crab_transferLogs
230707_163748:cmsbot_crab_activity
230707_163752:cmsbot_crab_inputFiles
230707_163755:cmsbot_crab_disableAutomaticOutputCollection
230707_163759:cmsbot_crab_outputFiles
230707_163801:cmsbot_crab_allowUndistributedCMSSW
230707_163804:cmsbot_crab_maxMemoryMB
230707_163807:cmsbot_crab_maxJobRuntimeMin
230707_163810:cmsbot_crab_numCores
230707_163813:cmsbot_crab_scriptExe
230707_163816:cmsbot_crab_scriptArgs
230707_163820:cmsbot_crab_sendPythonFolder
230707_163826:cmsbot_crab_sendExternalFolder
230707_163829:cmsbot_crab_inputDBS
230707_163831:cmsbot_crab_useParent
230707_163834:cmsbot_crab_secondaryInputDataset
230707_163837:cmsbot_crab_lumiMaskFile
230707_163840:cmsbot_crab_lumiMaskUrl
230707_163844:cmsbot_crab_outLFNDirBase
230707_163847:cmsbot_crab_runRange
230707_163850:cmsbot_crab_ignoreLocality
230707_163852:cmsbot_crab_userInputFiles
230707_163855:cmsbot_crab_whitelist
230707_163858:cmsbot_crab_blacklist
230707_163901:cmsbot_crab_ignoreGlobalBlacklist
230707_163903:cmsbot_crab_voRole
230707_163906:cmsbot_crab_voGroup
230707_163909:cmsbot_crab_scheddName
230707_163912:cmsbot_crab_collector
230707_163914:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230707_163740:cmsbot_crab_20230707_183734
```

Finished at: 2023-07-07 18:39:46
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/427/console)

## Comment (cmsdmwmbot, 2023-07-07T17:02:48Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-07 19:02:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/362/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/362//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-07T17:05:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 19:05:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/681/console

```
RETRY TESTS:
transferLogs-check.sh 230707_163745:cmsbot_crab_transferLogs - 2
lumiMaskUrl-check.sh 230707_163840:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230707_163847:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 230707_163850:cmsbot_crab_ignoreLocality - 2
whitelist-check.sh 230707_163855:cmsbot_crab_whitelist - 2
blacklist-check.sh 230707_163858:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230707_163901:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163743:cmsbot_crab_transferOutputs - 0
activity-check.sh 230707_163748:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163755:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163759:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163801:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163804:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163807:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163810:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163813:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163816:cmsbot_crab_scriptArgs - 0
sendExternalFolder-check.sh 230707_163826:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 230707_163831:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163834:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163837:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_163844:cmsbot_crab_outLFNDirBase - 0
userInputFiles-check.sh 230707_163852:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230707_163903:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163906:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163909:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163912:cmsbot_crab_collector - 0

FAILED TESTS:
sendPythonFolder-check.sh 230707_163820:cmsbot_crab_sendPythonFolder - 1
inputDBS-check.sh 230707_163829:cmsbot_crab_inputDBS - 1
extraJDL-check.sh 230707_163914:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-07-07T17:30:15Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-07 19:30:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/685/console

```
RETRY TESTS:
runRange-check.sh 230707_163847:cmsbot_crab_runRange - 2
ignoreGlobalBlacklist-check.sh 230707_163901:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163743:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163745:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163748:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163755:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163759:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163801:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163804:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163807:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163810:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163813:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163816:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163820:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163826:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163829:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163831:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163834:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163837:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_163840:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_163844:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_163850:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163852:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163855:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163858:cmsbot_crab_blacklist - 0
voRole-check.sh 230707_163903:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163906:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163909:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163912:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T17:42:13Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 19:42:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/472/console

```
{'TN': '230707_163919:cmsbot_crab_20230707_183915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 16, 'transferring': 979, 'running': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163922:cmsbot_crab_20230707_183919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163926:cmsbot_crab_20230707_183923', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163930:cmsbot_crab_20230707_183926', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163934:cmsbot_crab_20230707_183930', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163946:cmsbot_crab_20230707_183934', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-07-07T17:55:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-07 19:55:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/690/console

```
RETRY TESTS:
runRange-check.sh 230707_163847:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163743:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163745:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163748:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163755:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163759:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163801:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163804:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163807:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163810:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163813:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163816:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163820:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163826:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163829:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163831:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163834:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163837:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_163840:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_163844:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_163850:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163852:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163855:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163858:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163901:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163903:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163906:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163909:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163912:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T18:22:07Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-07 20:22:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/695/console

```
RETRY TESTS:
runRange-check.sh 230707_163847:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163743:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163745:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163748:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163755:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163759:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163801:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163804:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163807:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163810:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163813:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163816:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163820:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163826:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163829:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163831:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163834:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163837:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_163840:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_163844:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_163850:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163852:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163855:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163858:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163901:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163903:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163906:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163909:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163912:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T18:44:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-07 20:44:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/477/console

```
{'TN': '230707_163919:cmsbot_crab_20230707_183915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 995, 'transferring': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_163922:cmsbot_crab_20230707_183919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163926:cmsbot_crab_20230707_183923', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163930:cmsbot_crab_20230707_183926', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163934:cmsbot_crab_20230707_183930', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163946:cmsbot_crab_20230707_183934', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-07-07T18:47:13Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-07 20:47:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/698/console

```
RETRY TESTS:
runRange-check.sh 230707_163847:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163743:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163745:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163748:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163755:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163759:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163801:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163804:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163807:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163810:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163813:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163816:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163820:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163826:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163829:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163831:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163834:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163837:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_163840:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_163844:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_163850:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163852:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163855:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163858:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163901:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163903:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163906:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163909:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163912:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T19:42:38Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 4 out of 0. Test is done.
**Finished at:** 2023-07-07 21:42:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/700/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_163743:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_163745:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_163748:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_163752:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_163755:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_163759:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_163801:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_163804:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_163807:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_163810:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_163813:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_163816:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_163820:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_163826:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_163829:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_163831:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_163834:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_163837:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_163840:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_163844:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_163847:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_163850:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_163852:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_163855:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_163858:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_163901:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_163903:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_163906:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_163909:cmsbot_crab_scheddName - 0
collector-check.sh 230707_163912:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_163914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T19:46:28Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-07-07 21:46:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/480/console

```
{'TN': '230707_163919:cmsbot_crab_20230707_183915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163922:cmsbot_crab_20230707_183919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163926:cmsbot_crab_20230707_183923', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163930:cmsbot_crab_20230707_183926', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163934:cmsbot_crab_20230707_183930', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_163946:cmsbot_crab_20230707_183934', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-07-07T19:48:46Z)

all OK
