# dmwm/CRABServer issue #7778: #445: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-18T22:38:42Z
Closed: 2023-07-20T14:29:05Z
URL: https://github.com/dmwm/CRABServer/issues/7778

## Opening post (cmsdmwmbot, 2023-07-18T22:38:42Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-07-19 00:38:41
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/445/)

## Comment (cmsdmwmbot, 2023-07-18T22:41:01Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230718_224031:cmsbot_crab_20230719_004031
230718_224033:cmsbot_crab_20230719_004032
230718_224034:cmsbot_crab_20230719_004034
230718_224035:cmsbot_crab_20230719_004035
230718_224037:cmsbot_crab_20230719_004036
230718_224040:cmsbot_crab_20230719_004038
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230718_223859:cmsbot_crab_transferOutputs
230718_223901:cmsbot_crab_transferLogs
230718_223902:cmsbot_crab_activity
230718_223904:cmsbot_crab_inputFiles
230718_223905:cmsbot_crab_disableAutomaticOutputCollection
230718_223906:cmsbot_crab_outputFiles
230718_223908:cmsbot_crab_allowUndistributedCMSSW
230718_223909:cmsbot_crab_maxMemoryMB
230718_223910:cmsbot_crab_maxJobRuntimeMin
230718_223912:cmsbot_crab_numCores
230718_223913:cmsbot_crab_scriptExe
230718_223914:cmsbot_crab_scriptArgs
230718_223916:cmsbot_crab_sendPythonFolder
230718_223957:cmsbot_crab_sendExternalFolder
230718_223959:cmsbot_crab_inputDBS
230718_224000:cmsbot_crab_useParent
230718_224002:cmsbot_crab_secondaryInputDataset
230718_224003:cmsbot_crab_lumiMaskFile
230718_224006:cmsbot_crab_lumiMaskUrl
230718_224015:cmsbot_crab_outLFNDirBase
230718_224016:cmsbot_crab_runRange
230718_224017:cmsbot_crab_ignoreLocality
230718_224019:cmsbot_crab_userInputFiles
230718_224020:cmsbot_crab_whitelist
230718_224021:cmsbot_crab_blacklist
230718_224023:cmsbot_crab_ignoreGlobalBlacklist
230718_224024:cmsbot_crab_voRole
230718_224025:cmsbot_crab_voGroup
230718_224027:cmsbot_crab_scheddName
230718_224028:cmsbot_crab_collector
230718_224029:cmsbot_crab_extraJDL
```

Finished at: 2023-07-19 00:40:40
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/445/console)

## Comment (cmsdmwmbot, 2023-07-18T23:03:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-19 01:03:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/751/console

```
RETRY TESTS:
activity-check.sh 230718_223902:cmsbot_crab_activity - 2
maxJobRuntimeMin-check.sh 230718_223910:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230718_223912:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230718_224006:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230718_224016:cmsbot_crab_runRange - 2
whitelist-check.sh 230718_224020:cmsbot_crab_whitelist - 2
blacklist-check.sh 230718_224021:cmsbot_crab_blacklist - 2
voRole-check.sh 230718_224024:cmsbot_crab_voRole - 2
voGroup-check.sh 230718_224025:cmsbot_crab_voGroup - 2
extraJDL-check.sh 230718_224029:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_223859:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_223901:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230718_223904:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_223905:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230718_223906:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230718_223908:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230718_223909:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 230718_223913:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_223914:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_223916:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_223957:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_223959:cmsbot_crab_inputDBS - 0
useParent-check.sh 230718_224000:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230718_224002:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_224003:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230718_224015:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_224017:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_224019:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230718_224023:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 230718_224027:cmsbot_crab_scheddName - 0
collector-check.sh 230718_224028:cmsbot_crab_collector - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-18T23:27:17Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-19 01:27:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/752/console

```
RETRY TESTS:
activity-check.sh 230718_223902:cmsbot_crab_activity - 2
maxJobRuntimeMin-check.sh 230718_223910:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230718_223912:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230718_224006:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230718_224016:cmsbot_crab_runRange - 2
whitelist-check.sh 230718_224020:cmsbot_crab_whitelist - 2
blacklist-check.sh 230718_224021:cmsbot_crab_blacklist - 2
voRole-check.sh 230718_224024:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_223859:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_223901:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230718_223904:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_223905:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230718_223906:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230718_223908:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230718_223909:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 230718_223913:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_223914:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_223916:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_223957:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_223959:cmsbot_crab_inputDBS - 0
useParent-check.sh 230718_224000:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230718_224002:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_224003:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230718_224015:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_224017:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_224019:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230718_224023:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230718_224025:cmsbot_crab_voGroup - 0
scheddName-check.sh 230718_224027:cmsbot_crab_scheddName - 0
collector-check.sh 230718_224028:cmsbot_crab_collector - 0
extraJDL-check.sh 230718_224029:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-18T23:43:41Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-19 01:43:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/510/console

```
{'TN': '230718_224031:cmsbot_crab_20230719_004031', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 15, 'finished': 126, 'transferring': 859}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224033:cmsbot_crab_20230719_004032', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224034:cmsbot_crab_20230719_004034', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224035:cmsbot_crab_20230719_004035', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224037:cmsbot_crab_20230719_004036', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 6, 'finished': 5, 'transferring': 89}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224040:cmsbot_crab_20230719_004038', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-18T23:51:16Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-19 01:51:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/753/console

```
RETRY TESTS:
activity-check.sh 230718_223902:cmsbot_crab_activity - 2
maxJobRuntimeMin-check.sh 230718_223910:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230718_223912:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230718_224006:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230718_224016:cmsbot_crab_runRange - 2
whitelist-check.sh 230718_224020:cmsbot_crab_whitelist - 2
blacklist-check.sh 230718_224021:cmsbot_crab_blacklist - 2
voRole-check.sh 230718_224024:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_223859:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_223901:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230718_223904:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_223905:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230718_223906:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230718_223908:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230718_223909:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 230718_223913:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_223914:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_223916:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_223957:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_223959:cmsbot_crab_inputDBS - 0
useParent-check.sh 230718_224000:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230718_224002:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_224003:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230718_224015:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_224017:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_224019:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230718_224023:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230718_224025:cmsbot_crab_voGroup - 0
scheddName-check.sh 230718_224027:cmsbot_crab_scheddName - 0
collector-check.sh 230718_224028:cmsbot_crab_collector - 0
extraJDL-check.sh 230718_224029:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-19T00:14:19Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-19 02:14:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/754/console

```
RETRY TESTS:
activity-check.sh 230718_223902:cmsbot_crab_activity - 2
maxJobRuntimeMin-check.sh 230718_223910:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230718_223912:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230718_224006:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230718_224016:cmsbot_crab_runRange - 2
whitelist-check.sh 230718_224020:cmsbot_crab_whitelist - 2
blacklist-check.sh 230718_224021:cmsbot_crab_blacklist - 2
voRole-check.sh 230718_224024:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_223859:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_223901:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230718_223904:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_223905:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230718_223906:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230718_223908:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230718_223909:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 230718_223913:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_223914:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_223916:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_223957:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_223959:cmsbot_crab_inputDBS - 0
useParent-check.sh 230718_224000:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230718_224002:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_224003:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230718_224015:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_224017:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_224019:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230718_224023:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230718_224025:cmsbot_crab_voGroup - 0
scheddName-check.sh 230718_224027:cmsbot_crab_scheddName - 0
collector-check.sh 230718_224028:cmsbot_crab_collector - 0
extraJDL-check.sh 230718_224029:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-19T00:36:09Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-19 02:36:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/755/console

```
RETRY TESTS:
activity-check.sh 230718_223902:cmsbot_crab_activity - 2
maxJobRuntimeMin-check.sh 230718_223910:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230718_223912:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230718_224006:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230718_224016:cmsbot_crab_runRange - 2
whitelist-check.sh 230718_224020:cmsbot_crab_whitelist - 2
blacklist-check.sh 230718_224021:cmsbot_crab_blacklist - 2
voRole-check.sh 230718_224024:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230718_223859:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230718_223901:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230718_223904:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230718_223905:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230718_223906:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230718_223908:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230718_223909:cmsbot_crab_maxMemoryMB - 0
scriptExe-check.sh 230718_223913:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230718_223914:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230718_223916:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230718_223957:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230718_223959:cmsbot_crab_inputDBS - 0
useParent-check.sh 230718_224000:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230718_224002:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230718_224003:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230718_224015:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230718_224017:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230718_224019:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230718_224023:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230718_224025:cmsbot_crab_voGroup - 0
scheddName-check.sh 230718_224027:cmsbot_crab_scheddName - 0
collector-check.sh 230718_224028:cmsbot_crab_collector - 0
extraJDL-check.sh 230718_224029:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-19T00:45:52Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-19 02:45:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/511/console

```
{'TN': '230718_224031:cmsbot_crab_20230719_004031', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 15, 'finished': 128, 'transferring': 857}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224033:cmsbot_crab_20230719_004032', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224034:cmsbot_crab_20230719_004034', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224035:cmsbot_crab_20230719_004035', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224037:cmsbot_crab_20230719_004036', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 6, 'finished': 5, 'transferring': 89}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224040:cmsbot_crab_20230719_004038', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-19T01:49:30Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-19 03:49:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/512/console

```
{'TN': '230718_224031:cmsbot_crab_20230719_004031', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 15, 'finished': 129, 'transferring': 856}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224033:cmsbot_crab_20230719_004032', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224034:cmsbot_crab_20230719_004034', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224035:cmsbot_crab_20230719_004035', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224037:cmsbot_crab_20230719_004036', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 6, 'finished': 8, 'transferring': 86}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224040:cmsbot_crab_20230719_004038', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-19T02:51:40Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-19 04:51:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/513/console

```
{'TN': '230718_224031:cmsbot_crab_20230719_004031', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 15, 'finished': 142, 'transferring': 843}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224033:cmsbot_crab_20230719_004032', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224034:cmsbot_crab_20230719_004034', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224035:cmsbot_crab_20230719_004035', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 1, 'transferring': 8}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224037:cmsbot_crab_20230719_004036', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 6, 'finished': 14, 'transferring': 80}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224040:cmsbot_crab_20230719_004038', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-19T03:55:31Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-19 05:55:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/514/console

```
{'TN': '230718_224031:cmsbot_crab_20230719_004031', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 15, 'finished': 142, 'transferring': 843}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224033:cmsbot_crab_20230719_004032', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224034:cmsbot_crab_20230719_004034', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224035:cmsbot_crab_20230719_004035', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 1, 'transferring': 8}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224037:cmsbot_crab_20230719_004036', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 6, 'finished': 14, 'transferring': 80}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230718_224040:cmsbot_crab_20230719_004038', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (belforte, 2023-07-20T14:29:04Z)

FTS was so slow everything times out
