# dmwm/CRABServer issue #7794: #451: Test prod CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-08-04T07:27:46Z
Closed: 2023-08-14T12:33:22Z
URL: https://github.com/dmwm/CRABServer/issues/7794

## Opening post (cmsdmwmbot, 2023-08-04T07:27:46Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-08-04 09:27:44
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/451/)

## Comment (cmsdmwmbot, 2023-08-04T07:32:13Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230804_073113:cmsbot_crab_20230804_093111
230804_073116:cmsbot_crab_20230804_093114
230804_073120:cmsbot_crab_20230804_093117
230804_073122:cmsbot_crab_20230804_093120
230804_073126:cmsbot_crab_20230804_093123
230804_073151:cmsbot_crab_20230804_093126
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230804_072930:cmsbot_crab_transferOutputs
230804_072933:cmsbot_crab_transferLogs
230804_072935:cmsbot_crab_activity
230804_072939:cmsbot_crab_inputFiles
230804_072942:cmsbot_crab_disableAutomaticOutputCollection
230804_072945:cmsbot_crab_outputFiles
230804_072948:cmsbot_crab_allowUndistributedCMSSW
230804_072951:cmsbot_crab_maxMemoryMB
230804_072953:cmsbot_crab_maxJobRuntimeMin
230804_072957:cmsbot_crab_numCores
230804_073000:cmsbot_crab_scriptExe
230804_073003:cmsbot_crab_scriptArgs
230804_073006:cmsbot_crab_sendPythonFolder
230804_073018:cmsbot_crab_sendExternalFolder
230804_073021:cmsbot_crab_inputDBS
230804_073024:cmsbot_crab_useParent
230804_073027:cmsbot_crab_secondaryInputDataset
230804_073030:cmsbot_crab_lumiMaskFile
230804_073034:cmsbot_crab_lumiMaskUrl
230804_073038:cmsbot_crab_outLFNDirBase
230804_073041:cmsbot_crab_runRange
230804_073044:cmsbot_crab_ignoreLocality
230804_073047:cmsbot_crab_userInputFiles
230804_073049:cmsbot_crab_whitelist
230804_073052:cmsbot_crab_blacklist
230804_073055:cmsbot_crab_ignoreGlobalBlacklist
230804_073058:cmsbot_crab_voRole
230804_073101:cmsbot_crab_voGroup
230804_073104:cmsbot_crab_scheddName
230804_073107:cmsbot_crab_collector
230804_073110:cmsbot_crab_extraJDL
```

Finished at: 2023-08-04 09:31:51
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/451/console)

## Comment (cmsdmwmbot, 2023-08-04T07:57:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-04 09:57:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/771/console

```
RETRY TESTS:
scriptArgs-check.sh 230804_073003:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 230804_073034:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230804_073041:cmsbot_crab_runRange - 2
whitelist-check.sh 230804_073049:cmsbot_crab_whitelist - 2
blacklist-check.sh 230804_073052:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230804_072930:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230804_072933:cmsbot_crab_transferLogs - 0
activity-check.sh 230804_072935:cmsbot_crab_activity - 0
inputFiles-check.sh 230804_072939:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230804_072942:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230804_072945:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230804_072948:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230804_072951:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230804_072953:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230804_072957:cmsbot_crab_numCores - 0
scriptExe-check.sh 230804_073000:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230804_073006:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230804_073018:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230804_073021:cmsbot_crab_inputDBS - 0
useParent-check.sh 230804_073024:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230804_073027:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230804_073030:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230804_073038:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230804_073044:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230804_073047:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230804_073055:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230804_073058:cmsbot_crab_voRole - 0
voGroup-check.sh 230804_073101:cmsbot_crab_voGroup - 0
scheddName-check.sh 230804_073104:cmsbot_crab_scheddName - 0
collector-check.sh 230804_073107:cmsbot_crab_collector - 0
extraJDL-check.sh 230804_073110:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-04T08:23:13Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-08-04 10:23:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/773/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230804_072930:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230804_072933:cmsbot_crab_transferLogs - 0
activity-check.sh 230804_072935:cmsbot_crab_activity - 0
inputFiles-check.sh 230804_072939:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230804_072942:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230804_072945:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230804_072948:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230804_072951:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230804_072953:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230804_072957:cmsbot_crab_numCores - 0
scriptExe-check.sh 230804_073000:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230804_073003:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230804_073006:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230804_073018:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230804_073021:cmsbot_crab_inputDBS - 0
useParent-check.sh 230804_073024:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230804_073027:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230804_073030:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230804_073034:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230804_073038:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230804_073041:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230804_073044:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230804_073047:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230804_073049:cmsbot_crab_whitelist - 0
blacklist-check.sh 230804_073052:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230804_073055:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230804_073058:cmsbot_crab_voRole - 0
voGroup-check.sh 230804_073101:cmsbot_crab_voGroup - 0
scheddName-check.sh 230804_073104:cmsbot_crab_scheddName - 0
collector-check.sh 230804_073107:cmsbot_crab_collector - 0
extraJDL-check.sh 230804_073110:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-04T08:34:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-04 10:34:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/528/console

```
{'TN': '230804_073113:cmsbot_crab_20230804_093111', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 997, 'transferring': 1, 'running': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230804_073116:cmsbot_crab_20230804_093114', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230804_073120:cmsbot_crab_20230804_093117', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_073122:cmsbot_crab_20230804_093120', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_073126:cmsbot_crab_20230804_093123', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_073151:cmsbot_crab_20230804_093126', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-08-04T09:36:39Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-08-04 11:36:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/530/console

```
{'TN': '230804_073113:cmsbot_crab_20230804_093111', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 2, 'finished': 998}, 'combinedStatus': 'FAILED'}
{'TN': '230804_073116:cmsbot_crab_20230804_093114', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_073120:cmsbot_crab_20230804_093117', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_073122:cmsbot_crab_20230804_093120', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_073126:cmsbot_crab_20230804_093123', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230804_073151:cmsbot_crab_20230804_093126', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```
