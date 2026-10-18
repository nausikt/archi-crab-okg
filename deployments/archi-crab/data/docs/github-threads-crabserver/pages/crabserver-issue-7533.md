# dmwm/CRABServer issue #7533: #373: Test GH CRABClient using preprod REST instance and CMSSW_12_6_0_pre4 CMSSW release

State: closed
Opened: 2023-02-15T14:50:04Z
Closed: 2023-02-16T17:58:40Z
URL: https://github.com/dmwm/CRABServer/issues/7533

## Opening post (cmsdmwmbot, 2023-02-15T14:50:04Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_0_pre4**
- SCRAM_ARCH: **el8_amd64_gcc10**
- CRABServer_tag: **HEAD**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-02-15 15:50:03
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/373/)

## Comment (cmsdmwmbot, 2023-02-15T14:52:40Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230215_145153:cmsbot_crab_20230215_155152
230215_145155:cmsbot_crab_20230215_155154
230215_145156:cmsbot_crab_20230215_155155
230215_145158:cmsbot_crab_20230215_155157
230215_145159:cmsbot_crab_20230215_155159
230215_145219:cmsbot_crab_20230215_155200
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230215_145055:cmsbot_crab_transferOutputs
230215_145057:cmsbot_crab_transferLogs
230215_145058:cmsbot_crab_activity
230215_145100:cmsbot_crab_inputFiles
230215_145101:cmsbot_crab_disableAutomaticOutputCollection
230215_145103:cmsbot_crab_outputFiles
230215_145104:cmsbot_crab_allowUndistributedCMSSW
230215_145106:cmsbot_crab_maxMemoryMB
230215_145107:cmsbot_crab_maxJobRuntimeMin
230215_145109:cmsbot_crab_numCores
230215_145111:cmsbot_crab_scriptExe
230215_145112:cmsbot_crab_scriptArgs
230215_145114:cmsbot_crab_sendPythonFolder
230215_145123:cmsbot_crab_sendExternalFolder
230215_145124:cmsbot_crab_inputDBS
230215_145126:cmsbot_crab_useParent
230215_145127:cmsbot_crab_secondaryInputDataset
230215_145129:cmsbot_crab_lumiMaskFile
230215_145131:cmsbot_crab_lumiMaskUrl
230215_145133:cmsbot_crab_outLFNDirBase
230215_145135:cmsbot_crab_runRange
230215_145136:cmsbot_crab_ignoreLocality
230215_145138:cmsbot_crab_userInputFiles
230215_145140:cmsbot_crab_whitelist
230215_145141:cmsbot_crab_blacklist
230215_145143:cmsbot_crab_ignoreGlobalBlacklist
230215_145144:cmsbot_crab_voRole
230215_145146:cmsbot_crab_voGroup
230215_145147:cmsbot_crab_scheddName
230215_145149:cmsbot_crab_collector
230215_145151:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230215_145053:cmsbot_crab_20230215_155052
```

Finished at: 2023-02-15 15:52:19
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/373/console)

## Comment (cmsdmwmbot, 2023-02-15T15:14:40Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-02-15 16:14:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/334/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/334//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-02-15T15:19:48Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-02-15 16:19:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/576/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 230215_145055:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230215_145057:cmsbot_crab_transferLogs - 1
activity-check.sh 230215_145058:cmsbot_crab_activity - 1
inputFiles-check.sh 230215_145100:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 230215_145101:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230215_145103:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 230215_145104:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 230215_145106:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230215_145107:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230215_145109:cmsbot_crab_numCores - 1
scriptExe-check.sh 230215_145111:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230215_145112:cmsbot_crab_scriptArgs - 1
sendPythonFolder-check.sh 230215_145114:cmsbot_crab_sendPythonFolder - 1
sendExternalFolder-check.sh 230215_145123:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 230215_145124:cmsbot_crab_inputDBS - 1
useParent-check.sh 230215_145126:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230215_145127:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230215_145129:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230215_145131:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230215_145133:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230215_145135:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230215_145136:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230215_145138:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230215_145140:cmsbot_crab_whitelist - 1
blacklist-check.sh 230215_145141:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230215_145143:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230215_145144:cmsbot_crab_voRole - 1
voGroup-check.sh 230215_145146:cmsbot_crab_voGroup - 1
scheddName-check.sh 230215_145147:cmsbot_crab_scheddName - 1
collector-check.sh 230215_145149:cmsbot_crab_collector - 1
extraJDL-check.sh 230215_145151:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-02-15T15:57:32Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-15 16:57:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/427/console

```
{'TN': '230215_145153:cmsbot_crab_20230215_155152', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145155:cmsbot_crab_20230215_155154', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145156:cmsbot_crab_20230215_155155', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145158:cmsbot_crab_20230215_155157', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145159:cmsbot_crab_20230215_155159', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145219:cmsbot_crab_20230215_155200', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
```

## Comment (cmsdmwmbot, 2023-02-15T17:00:28Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-02-15 18:00:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/429/console

```
{'TN': '230215_145153:cmsbot_crab_20230215_155152', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145155:cmsbot_crab_20230215_155154', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145156:cmsbot_crab_20230215_155155', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145158:cmsbot_crab_20230215_155157', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145159:cmsbot_crab_20230215_155159', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145219:cmsbot_crab_20230215_155200', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
```

## Comment (cmsdmwmbot, 2023-02-15T18:05:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-02-15 19:05:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/431/console

```
{'TN': '230215_145153:cmsbot_crab_20230215_155152', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145155:cmsbot_crab_20230215_155154', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145156:cmsbot_crab_20230215_155155', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145158:cmsbot_crab_20230215_155157', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145159:cmsbot_crab_20230215_155159', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
{'TN': '230215_145219:cmsbot_crab_20230215_155200', 'dbStatus': u'HOLDING', 'testResult': 'TestRunning', 'jobsPerStatus': {}, 'combinedStatus': u'HOLDING'}
```

## Comment (novicecpp, 2023-02-16T17:58:40Z)

This one had bug I found in wmcore. Closing.
