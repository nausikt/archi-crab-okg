# dmwm/CRABServer issue #7790: #449: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-08-01T15:20:10Z
Closed: 2023-08-01T17:09:00Z
URL: https://github.com/dmwm/CRABServer/issues/7790

## Opening post (cmsdmwmbot, 2023-08-01T15:20:10Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

**This will be used to verify #7777 by checkin publication**

Started at: 2023-08-01 17:20:09
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/449/)

## Comment (cmsdmwmbot, 2023-08-01T15:22:17Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230801_152148:cmsbot_crab_20230801_172147
230801_152149:cmsbot_crab_20230801_172149
230801_152150:cmsbot_crab_20230801_172150
230801_152152:cmsbot_crab_20230801_172151
230801_152153:cmsbot_crab_20230801_172152
230801_152155:cmsbot_crab_20230801_172154
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230801_152029:cmsbot_crab_transferOutputs
230801_152031:cmsbot_crab_transferLogs
230801_152032:cmsbot_crab_activity
230801_152033:cmsbot_crab_inputFiles
230801_152035:cmsbot_crab_disableAutomaticOutputCollection
230801_152036:cmsbot_crab_outputFiles
230801_152037:cmsbot_crab_allowUndistributedCMSSW
230801_152039:cmsbot_crab_maxMemoryMB
230801_152040:cmsbot_crab_maxJobRuntimeMin
230801_152041:cmsbot_crab_numCores
230801_152042:cmsbot_crab_scriptExe
230801_152044:cmsbot_crab_scriptArgs
230801_152045:cmsbot_crab_sendPythonFolder
230801_152123:cmsbot_crab_sendExternalFolder
230801_152124:cmsbot_crab_inputDBS
230801_152126:cmsbot_crab_useParent
230801_152127:cmsbot_crab_secondaryInputDataset
230801_152128:cmsbot_crab_lumiMaskFile
230801_152130:cmsbot_crab_lumiMaskUrl
230801_152132:cmsbot_crab_outLFNDirBase
230801_152133:cmsbot_crab_runRange
230801_152135:cmsbot_crab_ignoreLocality
230801_152136:cmsbot_crab_userInputFiles
230801_152137:cmsbot_crab_whitelist
230801_152138:cmsbot_crab_blacklist
230801_152140:cmsbot_crab_ignoreGlobalBlacklist
230801_152141:cmsbot_crab_voRole
230801_152142:cmsbot_crab_voGroup
230801_152143:cmsbot_crab_scheddName
230801_152145:cmsbot_crab_collector
230801_152146:cmsbot_crab_extraJDL
```

Finished at: 2023-08-01 17:21:56
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/449/console)

## Comment (cmsdmwmbot, 2023-08-01T15:44:13Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-01 17:44:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/767/console

```
RETRY TESTS:
activity-check.sh 230801_152032:cmsbot_crab_activity - 2
lumiMaskUrl-check.sh 230801_152130:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230801_152133:cmsbot_crab_runRange - 2
whitelist-check.sh 230801_152137:cmsbot_crab_whitelist - 2
blacklist-check.sh 230801_152138:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230801_152029:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230801_152031:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230801_152033:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230801_152035:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230801_152036:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230801_152037:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230801_152039:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230801_152040:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230801_152041:cmsbot_crab_numCores - 0
scriptExe-check.sh 230801_152042:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230801_152044:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230801_152045:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230801_152123:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230801_152124:cmsbot_crab_inputDBS - 0
useParent-check.sh 230801_152126:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230801_152127:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230801_152128:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230801_152132:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230801_152135:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230801_152136:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230801_152140:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230801_152141:cmsbot_crab_voRole - 0
voGroup-check.sh 230801_152142:cmsbot_crab_voGroup - 0
scheddName-check.sh 230801_152143:cmsbot_crab_scheddName - 0
collector-check.sh 230801_152145:cmsbot_crab_collector - 0
extraJDL-check.sh 230801_152146:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-01T16:06:09Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-08-01 18:06:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/768/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230801_152130:cmsbot_crab_lumiMaskUrl - 2
whitelist-check.sh 230801_152137:cmsbot_crab_whitelist - 2
blacklist-check.sh 230801_152138:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230801_152029:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230801_152031:cmsbot_crab_transferLogs - 0
activity-check.sh 230801_152032:cmsbot_crab_activity - 0
inputFiles-check.sh 230801_152033:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230801_152035:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230801_152036:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230801_152037:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230801_152039:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230801_152040:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230801_152041:cmsbot_crab_numCores - 0
scriptExe-check.sh 230801_152042:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230801_152044:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230801_152045:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230801_152123:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230801_152124:cmsbot_crab_inputDBS - 0
useParent-check.sh 230801_152126:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230801_152127:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230801_152128:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230801_152132:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230801_152133:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230801_152135:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230801_152136:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230801_152140:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230801_152141:cmsbot_crab_voRole - 0
voGroup-check.sh 230801_152142:cmsbot_crab_voGroup - 0
scheddName-check.sh 230801_152143:cmsbot_crab_scheddName - 0
collector-check.sh 230801_152145:cmsbot_crab_collector - 0
extraJDL-check.sh 230801_152146:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-01T16:24:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-01 18:24:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/525/console

```
{'TN': '230801_152148:cmsbot_crab_20230801_172147', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 987, 'transferring': 9, 'running': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230801_152149:cmsbot_crab_20230801_172149', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230801_152150:cmsbot_crab_20230801_172150', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230801_152152:cmsbot_crab_20230801_172151', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230801_152153:cmsbot_crab_20230801_172152', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230801_152155:cmsbot_crab_20230801_172154', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'transferring': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-08-01T16:28:07Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-08-01 18:28:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/769/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230801_152029:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230801_152031:cmsbot_crab_transferLogs - 0
activity-check.sh 230801_152032:cmsbot_crab_activity - 0
inputFiles-check.sh 230801_152033:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230801_152035:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230801_152036:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230801_152037:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230801_152039:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230801_152040:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230801_152041:cmsbot_crab_numCores - 0
scriptExe-check.sh 230801_152042:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230801_152044:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230801_152045:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230801_152123:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230801_152124:cmsbot_crab_inputDBS - 0
useParent-check.sh 230801_152126:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230801_152127:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230801_152128:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230801_152130:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230801_152132:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230801_152133:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230801_152135:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230801_152136:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230801_152137:cmsbot_crab_whitelist - 0
blacklist-check.sh 230801_152138:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230801_152140:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230801_152141:cmsbot_crab_voRole - 0
voGroup-check.sh 230801_152142:cmsbot_crab_voGroup - 0
scheddName-check.sh 230801_152143:cmsbot_crab_scheddName - 0
collector-check.sh 230801_152145:cmsbot_crab_collector - 0
extraJDL-check.sh 230801_152146:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-08-01T16:53:33Z)

So far so good, all StatusTracking tasks are almost done and number of files in phys03 properly matches number of successful jobs

## Comment (belforte, 2023-08-01T17:09:00Z)

all jobs successful and successfully published !

## Comment (cmsdmwmbot, 2023-08-01T17:27:06Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-08-01 19:27:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/526/console

```
{'TN': '230801_152148:cmsbot_crab_20230801_172147', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230801_152149:cmsbot_crab_20230801_172149', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230801_152150:cmsbot_crab_20230801_172150', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230801_152152:cmsbot_crab_20230801_172151', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230801_152153:cmsbot_crab_20230801_172152', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230801_152155:cmsbot_crab_20230801_172154', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```
