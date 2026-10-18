# dmwm/CRABServer issue #7682: #395: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-27T23:00:32Z
Closed: 2023-06-29T20:16:17Z
URL: https://github.com/dmwm/CRABServer/issues/7682

## Opening post (cmsdmwmbot, 2023-06-27T23:00:32Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-06-28 01:00:31
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/395/)

## Comment (cmsdmwmbot, 2023-06-27T23:03:38Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230627_230251:cmsbot_crab_20230628_010251
230627_230252:cmsbot_crab_20230628_010252
230627_230254:cmsbot_crab_20230628_010253
230627_230255:cmsbot_crab_20230628_010255
230627_230256:cmsbot_crab_20230628_010256
230627_230317:cmsbot_crab_20230628_010257
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230627_230125:cmsbot_crab_transferOutputs
230627_230126:cmsbot_crab_transferLogs
230627_230127:cmsbot_crab_activity
230627_230129:cmsbot_crab_inputFiles
230627_230130:cmsbot_crab_disableAutomaticOutputCollection
230627_230131:cmsbot_crab_outputFiles
230627_230133:cmsbot_crab_allowUndistributedCMSSW
230627_230134:cmsbot_crab_maxMemoryMB
230627_230136:cmsbot_crab_maxJobRuntimeMin
230627_230137:cmsbot_crab_numCores
230627_230139:cmsbot_crab_scriptExe
230627_230140:cmsbot_crab_scriptArgs
230627_230141:cmsbot_crab_sendPythonFolder
230627_230225:cmsbot_crab_sendExternalFolder
230627_230226:cmsbot_crab_inputDBS
230627_230228:cmsbot_crab_useParent
230627_230229:cmsbot_crab_secondaryInputDataset
230627_230230:cmsbot_crab_lumiMaskFile
230627_230232:cmsbot_crab_lumiMaskUrl
230627_230234:cmsbot_crab_outLFNDirBase
230627_230235:cmsbot_crab_runRange
230627_230237:cmsbot_crab_ignoreLocality
230627_230238:cmsbot_crab_userInputFiles
230627_230239:cmsbot_crab_whitelist
230627_230241:cmsbot_crab_blacklist
230627_230242:cmsbot_crab_ignoreGlobalBlacklist
230627_230243:cmsbot_crab_voRole
230627_230245:cmsbot_crab_voGroup
230627_230246:cmsbot_crab_scheddName
230627_230247:cmsbot_crab_collector
230627_230249:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230627_230123:cmsbot_crab_20230628_010122
```

Finished at: 2023-06-28 01:03:17
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/395/console)

## Comment (cmsdmwmbot, 2023-06-27T23:24:36Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-28 01:24:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/347/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/347//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-27T23:25:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-28 01:25:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/615/console

```
RETRY TESTS:
useParent-check.sh 230627_230228:cmsbot_crab_useParent - 2
runRange-check.sh 230627_230235:cmsbot_crab_runRange - 2
whitelist-check.sh 230627_230239:cmsbot_crab_whitelist - 2
blacklist-check.sh 230627_230241:cmsbot_crab_blacklist - 2
extraJDL-check.sh 230627_230249:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 230627_230129:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230627_230133:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230627_230141:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_230225:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_230226:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230627_230246:cmsbot_crab_scheddName - 0
collector-check.sh 230627_230247:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 230627_230125:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230627_230126:cmsbot_crab_transferLogs - 1
activity-check.sh 230627_230127:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230627_230130:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230627_230131:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230627_230134:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230627_230136:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230627_230137:cmsbot_crab_numCores - 1
scriptExe-check.sh 230627_230139:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230627_230140:cmsbot_crab_scriptArgs - 1
secondaryInputDataset-check.sh 230627_230229:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230627_230230:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230627_230232:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230627_230234:cmsbot_crab_outLFNDirBase - 1
ignoreLocality-check.sh 230627_230237:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230627_230238:cmsbot_crab_userInputFiles - 1
ignoreGlobalBlacklist-check.sh 230627_230242:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230627_230243:cmsbot_crab_voRole - 1
voGroup-check.sh 230627_230245:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2023-06-27T23:46:36Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-28 01:46:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/619/console

```
RETRY TESTS:
useParent-check.sh 230627_230228:cmsbot_crab_useParent - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 230627_230129:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230627_230133:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230627_230141:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_230225:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_230226:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230627_230246:cmsbot_crab_scheddName - 0
collector-check.sh 230627_230247:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 230627_230125:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230627_230126:cmsbot_crab_transferLogs - 1
activity-check.sh 230627_230127:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230627_230130:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230627_230131:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230627_230134:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230627_230136:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230627_230137:cmsbot_crab_numCores - 1
scriptExe-check.sh 230627_230139:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230627_230140:cmsbot_crab_scriptArgs - 1
secondaryInputDataset-check.sh 230627_230229:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230627_230230:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230627_230232:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230627_230234:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230627_230235:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230627_230237:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230627_230238:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230627_230239:cmsbot_crab_whitelist - 1
blacklist-check.sh 230627_230241:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230627_230242:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230627_230243:cmsbot_crab_voRole - 1
voGroup-check.sh 230627_230245:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230627_230249:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-06-28T00:05:37Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-28 02:05:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/459/console

```
{'TN': '230627_230251:cmsbot_crab_20230628_010251', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 999, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230627_230252:cmsbot_crab_20230628_010252', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 5}, 'combinedStatus': 'FAILED'}
{'TN': '230627_230254:cmsbot_crab_20230628_010253', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1}, 'combinedStatus': 'FAILED'}
{'TN': '230627_230255:cmsbot_crab_20230628_010255', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 10}, 'combinedStatus': 'FAILED'}
{'TN': '230627_230256:cmsbot_crab_20230628_010256', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 100}, 'combinedStatus': 'FAILED'}
{'TN': '230627_230317:cmsbot_crab_20230628_010257', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 10}, 'combinedStatus': 'FAILED'}
```

## Comment (cmsdmwmbot, 2023-06-28T00:08:22Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-28 02:08:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/623/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
inputFiles-check.sh 230627_230129:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230627_230133:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230627_230141:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_230225:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_230226:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230627_230246:cmsbot_crab_scheddName - 0
collector-check.sh 230627_230247:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 230627_230125:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230627_230126:cmsbot_crab_transferLogs - 1
activity-check.sh 230627_230127:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230627_230130:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230627_230131:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230627_230134:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230627_230136:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230627_230137:cmsbot_crab_numCores - 1
scriptExe-check.sh 230627_230139:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230627_230140:cmsbot_crab_scriptArgs - 1
useParent-check.sh 230627_230228:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230627_230229:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230627_230230:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230627_230232:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230627_230234:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230627_230235:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230627_230237:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230627_230238:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230627_230239:cmsbot_crab_whitelist - 1
blacklist-check.sh 230627_230241:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230627_230242:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230627_230243:cmsbot_crab_voRole - 1
voGroup-check.sh 230627_230245:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230627_230249:cmsbot_crab_extraJDL - 1
```
