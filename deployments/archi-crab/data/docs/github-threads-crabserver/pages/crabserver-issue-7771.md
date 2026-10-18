# dmwm/CRABServer issue #7771: #444: Test prod CRABClient using test11 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-18T08:17:38Z
Closed: 2023-07-19T12:42:31Z
URL: https://github.com/dmwm/CRABServer/issues/7771

## Opening post (cmsdmwmbot, 2023-07-18T08:17:38Z)

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

Started at: 2023-07-18 10:17:37
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/444/)

## Comment (cmsdmwmbot, 2023-07-18T08:20:03Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230718_081916:cmsbot_crab_20230718_101915
230718_081917:cmsbot_crab_20230718_101917
230718_081918:cmsbot_crab_20230718_101918
230718_081919:cmsbot_crab_20230718_101919
230718_081921:cmsbot_crab_20230718_101920
230718_081941:cmsbot_crab_20230718_101922
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230718_081756:cmsbot_crab_transferOutputs
230718_081757:cmsbot_crab_transferLogs
230718_081758:cmsbot_crab_activity
230718_081800:cmsbot_crab_inputFiles
230718_081801:cmsbot_crab_disableAutomaticOutputCollection
230718_081802:cmsbot_crab_outputFiles
230718_081803:cmsbot_crab_allowUndistributedCMSSW
230718_081805:cmsbot_crab_maxMemoryMB
230718_081806:cmsbot_crab_maxJobRuntimeMin
230718_081808:cmsbot_crab_numCores
230718_081809:cmsbot_crab_scriptExe
230718_081810:cmsbot_crab_scriptArgs
230718_081812:cmsbot_crab_sendPythonFolder
230718_081851:cmsbot_crab_sendExternalFolder
230718_081852:cmsbot_crab_inputDBS
230718_081854:cmsbot_crab_useParent
230718_081855:cmsbot_crab_secondaryInputDataset
230718_081856:cmsbot_crab_lumiMaskFile
230718_081858:cmsbot_crab_lumiMaskUrl
230718_081900:cmsbot_crab_outLFNDirBase
230718_081901:cmsbot_crab_runRange
230718_081902:cmsbot_crab_ignoreLocality
230718_081904:cmsbot_crab_userInputFiles
230718_081905:cmsbot_crab_whitelist
230718_081906:cmsbot_crab_blacklist
230718_081907:cmsbot_crab_ignoreGlobalBlacklist
230718_081909:cmsbot_crab_voRole
230718_081910:cmsbot_crab_voGroup
230718_081911:cmsbot_crab_scheddName
230718_081912:cmsbot_crab_collector
230718_081914:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230718_081754:cmsbot_crab_20230718_101754
```

Finished at: 2023-07-18 10:19:41
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/444/console)

## Comment (mapellidario, 2023-07-18T08:23:33Z)

follow up to #7768 

running https://github.com/dmwm/CRABServer/compare/master...mapellidario:20230717_py3htc10 in a crabserver container without py3-htcondor, generated from the changes in https://github.com/cms-sw/cmsdist/pull/8600

## Comment (cmsdmwmbot, 2023-07-18T08:42:25Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-18 10:42:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/369/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/369//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-18T08:43:10Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-18 10:43:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/746/console

```
RETRY TESTS:
outputFiles-check.sh 230718_081802:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230718_081805:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230718_081806:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230718_081808:cmsbot_crab_numCores - 2
useParent-check.sh 230718_081854:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 230718_081858:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230718_081901:cmsbot_crab_runRange - 2
whitelist-check.sh 230718_081905:cmsbot_crab_whitelist - 2
blacklist-check.sh 230718_081906:cmsbot_crab_blacklist - 2
voGroup-check.sh 230718_081910:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_081756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_081757:cmsbot_crab_transferLogs - 0
activity-check.sh 230718_081758:cmsbot_crab_activity - 0
inputFiles-check.sh 230718_081800:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_081801:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230718_081803:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 230718_081809:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_081810:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_081812:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_081851:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_081852:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230718_081855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_081856:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230718_081900:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_081902:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_081904:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230718_081907:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230718_081909:cmsbot_crab_voRole - 0
scheddName-check.sh 230718_081911:cmsbot_crab_scheddName - 0
collector-check.sh 230718_081912:cmsbot_crab_collector - 0
extraJDL-check.sh 230718_081914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-18T09:05:32Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-18 11:05:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/747/console

```
RETRY TESTS:
runRange-check.sh 230718_081901:cmsbot_crab_runRange - 2
blacklist-check.sh 230718_081906:cmsbot_crab_blacklist - 2
voGroup-check.sh 230718_081910:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_081756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_081757:cmsbot_crab_transferLogs - 0
activity-check.sh 230718_081758:cmsbot_crab_activity - 0
inputFiles-check.sh 230718_081800:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_081801:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230718_081802:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230718_081803:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230718_081805:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230718_081806:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230718_081808:cmsbot_crab_numCores - 0
scriptExe-check.sh 230718_081809:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_081810:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_081812:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_081851:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_081852:cmsbot_crab_inputDBS - 0
useParent-check.sh 230718_081854:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230718_081855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_081856:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230718_081858:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230718_081900:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_081902:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_081904:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230718_081905:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 230718_081907:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230718_081909:cmsbot_crab_voRole - 0
scheddName-check.sh 230718_081911:cmsbot_crab_scheddName - 0
collector-check.sh 230718_081912:cmsbot_crab_collector - 0
extraJDL-check.sh 230718_081914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-18T09:23:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-18 11:23:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/505/console

```
{'TN': '230718_081916:cmsbot_crab_20230718_101915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 829, 'transferring': 166, 'running': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081917:cmsbot_crab_20230718_101917', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081918:cmsbot_crab_20230718_101918', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230718_081919:cmsbot_crab_20230718_101919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081921:cmsbot_crab_20230718_101920', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 79, 'transferring': 20, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081941:cmsbot_crab_20230718_101922', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-18T09:27:29Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-18 11:27:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/748/console

```
RETRY TESTS:
runRange-check.sh 230718_081901:cmsbot_crab_runRange - 2
voGroup-check.sh 230718_081910:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_081756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_081757:cmsbot_crab_transferLogs - 0
activity-check.sh 230718_081758:cmsbot_crab_activity - 0
inputFiles-check.sh 230718_081800:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_081801:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230718_081802:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230718_081803:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230718_081805:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230718_081806:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230718_081808:cmsbot_crab_numCores - 0
scriptExe-check.sh 230718_081809:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_081810:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_081812:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_081851:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_081852:cmsbot_crab_inputDBS - 0
useParent-check.sh 230718_081854:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230718_081855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_081856:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230718_081858:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230718_081900:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_081902:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_081904:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230718_081905:cmsbot_crab_whitelist - 0
blacklist-check.sh 230718_081906:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230718_081907:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230718_081909:cmsbot_crab_voRole - 0
scheddName-check.sh 230718_081911:cmsbot_crab_scheddName - 0
collector-check.sh 230718_081912:cmsbot_crab_collector - 0
extraJDL-check.sh 230718_081914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-18T09:51:30Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-18 11:51:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/749/console

```
RETRY TESTS:
runRange-check.sh 230718_081901:cmsbot_crab_runRange - 2
voGroup-check.sh 230718_081910:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_081756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_081757:cmsbot_crab_transferLogs - 0
activity-check.sh 230718_081758:cmsbot_crab_activity - 0
inputFiles-check.sh 230718_081800:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_081801:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230718_081802:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230718_081803:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230718_081805:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230718_081806:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230718_081808:cmsbot_crab_numCores - 0
scriptExe-check.sh 230718_081809:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_081810:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_081812:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_081851:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_081852:cmsbot_crab_inputDBS - 0
useParent-check.sh 230718_081854:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230718_081855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_081856:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230718_081858:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230718_081900:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_081902:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_081904:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230718_081905:cmsbot_crab_whitelist - 0
blacklist-check.sh 230718_081906:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230718_081907:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230718_081909:cmsbot_crab_voRole - 0
scheddName-check.sh 230718_081911:cmsbot_crab_scheddName - 0
collector-check.sh 230718_081912:cmsbot_crab_collector - 0
extraJDL-check.sh 230718_081914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-18T10:14:28Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-18 12:14:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/750/console

```
RETRY TESTS:
runRange-check.sh 230718_081901:cmsbot_crab_runRange - 2
voGroup-check.sh 230718_081910:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_081756:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_081757:cmsbot_crab_transferLogs - 0
activity-check.sh 230718_081758:cmsbot_crab_activity - 0
inputFiles-check.sh 230718_081800:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_081801:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230718_081802:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230718_081803:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230718_081805:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230718_081806:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230718_081808:cmsbot_crab_numCores - 0
scriptExe-check.sh 230718_081809:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_081810:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_081812:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_081851:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_081852:cmsbot_crab_inputDBS - 0
useParent-check.sh 230718_081854:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230718_081855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_081856:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230718_081858:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230718_081900:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_081902:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_081904:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230718_081905:cmsbot_crab_whitelist - 0
blacklist-check.sh 230718_081906:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230718_081907:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230718_081909:cmsbot_crab_voRole - 0
scheddName-check.sh 230718_081911:cmsbot_crab_scheddName - 0
collector-check.sh 230718_081912:cmsbot_crab_collector - 0
extraJDL-check.sh 230718_081914:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-18T10:27:29Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-18 12:27:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/506/console

```
{'TN': '230718_081916:cmsbot_crab_20230718_101915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 834, 'transferring': 165}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081917:cmsbot_crab_20230718_101917', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081918:cmsbot_crab_20230718_101918', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230718_081919:cmsbot_crab_20230718_101919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 5}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081921:cmsbot_crab_20230718_101920', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 80, 'transferring': 19}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081941:cmsbot_crab_20230718_101922', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-18T11:31:32Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-18 13:31:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/507/console

```
{'TN': '230718_081916:cmsbot_crab_20230718_101915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 865, 'transferring': 134}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081917:cmsbot_crab_20230718_101917', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081918:cmsbot_crab_20230718_101918', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230718_081919:cmsbot_crab_20230718_101919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081921:cmsbot_crab_20230718_101920', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 82, 'transferring': 17}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081941:cmsbot_crab_20230718_101922', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-18T12:35:32Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-18 14:35:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/508/console

```
{'TN': '230718_081916:cmsbot_crab_20230718_101915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 974, 'transferring': 25}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081917:cmsbot_crab_20230718_101917', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230718_081918:cmsbot_crab_20230718_101918', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230718_081919:cmsbot_crab_20230718_101919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081921:cmsbot_crab_20230718_101920', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 90, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081941:cmsbot_crab_20230718_101922', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-07-18T13:37:42Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 4 out of 4. Test failed. Investigate manually
**Finished at:** 2023-07-18 15:37:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/509/console

```
{'TN': '230718_081916:cmsbot_crab_20230718_101915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 989, 'transferring': 10}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_081917:cmsbot_crab_20230718_101917', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230718_081918:cmsbot_crab_20230718_101918', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230718_081919:cmsbot_crab_20230718_101919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230718_081921:cmsbot_crab_20230718_101920', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 99}, 'combinedStatus': 'FAILED'}
{'TN': '230718_081941:cmsbot_crab_20230718_101922', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (mapellidario, 2023-07-19T12:35:30Z)

> Test: Task Submission Status Tracking

all ok, spurious problems at mit and purdue. cmsRun did not write anything to console

> CCV

- 230718_081901:cmsbot_crab_runRange: one job had a weird problem with local stageout (the postjob reported the job as killed with too much wallclock time and mention a problem with FTS, FTS reports the transfer as failed, FTS logs do not mention any problem)
- 230718_081910:cmsbot_crab_voGroup : postjob declared the job failed with "too much wall clock time", mentioning "no fts server updated the transfer info for more than 900s"

The problems do not feel related to the changes at a first glance, they seems a transitory FTS problem. I will need to have a better look

## Comment (mapellidario, 2023-07-19T12:42:31Z)

Stefano confirmed having seen problems with FTS recently as well. We can assume that the problems are not related to these changes and move on
