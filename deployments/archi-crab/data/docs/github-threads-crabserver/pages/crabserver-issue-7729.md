# dmwm/CRABServer issue #7729: #430: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-07T20:27:34Z
Closed: 2023-07-07T22:38:54Z
URL: https://github.com/dmwm/CRABServer/issues/7729

## Opening post (cmsdmwmbot, 2023-07-07T20:27:34Z)

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

Started at: 2023-07-07 22:27:33
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/430/)

## Comment (cmsdmwmbot, 2023-07-07T20:29:43Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230707_202913:cmsbot_crab_20230707_222912
230707_202914:cmsbot_crab_20230707_222914
230707_202915:cmsbot_crab_20230707_222915
230707_202917:cmsbot_crab_20230707_222916
230707_202918:cmsbot_crab_20230707_222918
230707_202921:cmsbot_crab_20230707_222919
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230707_202749:cmsbot_crab_transferOutputs
230707_202751:cmsbot_crab_transferLogs
230707_202752:cmsbot_crab_activity
230707_202754:cmsbot_crab_inputFiles
230707_202756:cmsbot_crab_disableAutomaticOutputCollection
230707_202757:cmsbot_crab_outputFiles
230707_202759:cmsbot_crab_allowUndistributedCMSSW
230707_202801:cmsbot_crab_maxMemoryMB
230707_202802:cmsbot_crab_maxJobRuntimeMin
230707_202804:cmsbot_crab_numCores
230707_202805:cmsbot_crab_scriptExe
230707_202807:cmsbot_crab_scriptArgs
230707_202808:cmsbot_crab_sendPythonFolder
230707_202846:cmsbot_crab_sendExternalFolder
230707_202848:cmsbot_crab_inputDBS
230707_202849:cmsbot_crab_useParent
230707_202851:cmsbot_crab_secondaryInputDataset
230707_202852:cmsbot_crab_lumiMaskFile
230707_202854:cmsbot_crab_lumiMaskUrl
230707_202856:cmsbot_crab_outLFNDirBase
230707_202857:cmsbot_crab_runRange
230707_202859:cmsbot_crab_ignoreLocality
230707_202900:cmsbot_crab_userInputFiles
230707_202901:cmsbot_crab_whitelist
230707_202903:cmsbot_crab_blacklist
230707_202904:cmsbot_crab_ignoreGlobalBlacklist
230707_202905:cmsbot_crab_voRole
230707_202907:cmsbot_crab_voGroup
230707_202908:cmsbot_crab_scheddName
230707_202909:cmsbot_crab_collector
230707_202911:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230707_202747:cmsbot_crab_20230707_222747
```

Finished at: 2023-07-07 22:29:22
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/430/console)

## Comment (cmsdmwmbot, 2023-07-07T20:50:39Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-07 22:50:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/364/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/364//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-07-07T20:51:33Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 22:51:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/702/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230707_202854:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230707_202857:cmsbot_crab_runRange - 2
whitelist-check.sh 230707_202901:cmsbot_crab_whitelist - 2
blacklist-check.sh 230707_202903:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_202749:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_202751:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_202752:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_202754:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_202756:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_202757:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_202759:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_202801:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_202802:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_202804:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_202805:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_202807:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_202808:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_202846:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_202848:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_202849:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_202851:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_202852:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230707_202856:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230707_202859:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_202900:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230707_202904:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_202905:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_202907:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_202908:cmsbot_crab_scheddName - 0
collector-check.sh 230707_202909:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_202911:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T21:13:31Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-07-07 23:13:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/704/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230707_202749:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230707_202751:cmsbot_crab_transferLogs - 0
activity-check.sh 230707_202752:cmsbot_crab_activity - 0
inputFiles-check.sh 230707_202754:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230707_202756:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230707_202757:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230707_202759:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230707_202801:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230707_202802:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230707_202804:cmsbot_crab_numCores - 0
scriptExe-check.sh 230707_202805:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230707_202807:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230707_202808:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230707_202846:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230707_202848:cmsbot_crab_inputDBS - 0
useParent-check.sh 230707_202849:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230707_202851:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230707_202852:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230707_202854:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230707_202856:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230707_202857:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230707_202859:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230707_202900:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230707_202901:cmsbot_crab_whitelist - 0
blacklist-check.sh 230707_202903:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230707_202904:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230707_202905:cmsbot_crab_voRole - 0
voGroup-check.sh 230707_202907:cmsbot_crab_voGroup - 0
scheddName-check.sh 230707_202908:cmsbot_crab_scheddName - 0
collector-check.sh 230707_202909:cmsbot_crab_collector - 0
extraJDL-check.sh 230707_202911:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-07T21:31:55Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-07 23:31:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/485/console

```
{'TN': '230707_202913:cmsbot_crab_20230707_222912', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 998, 'transferring': 1, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_202914:cmsbot_crab_20230707_222914', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_202915:cmsbot_crab_20230707_222915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_202917:cmsbot_crab_20230707_222916', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_202918:cmsbot_crab_20230707_222918', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 99, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230707_202921:cmsbot_crab_20230707_222919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 9}, 'combinedStatus': 'FAILED'}
```

## Comment (cmsdmwmbot, 2023-07-07T22:34:07Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-07-08 00:34:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/487/console

```
{'TN': '230707_202913:cmsbot_crab_20230707_222912', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_202914:cmsbot_crab_20230707_222914', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_202915:cmsbot_crab_20230707_222915', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_202917:cmsbot_crab_20230707_222916', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_202918:cmsbot_crab_20230707_222918', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230707_202921:cmsbot_crab_20230707_222919', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```
