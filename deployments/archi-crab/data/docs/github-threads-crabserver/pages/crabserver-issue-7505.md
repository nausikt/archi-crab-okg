# dmwm/CRABServer issue #7505: #367: Test prod CRABClient using test2 REST instance and CMSSW_12_0_1 CMSSW release

State: closed
Opened: 2023-01-25T16:25:10Z
Closed: 2023-01-26T09:01:24Z
URL: https://github.com/dmwm/CRABServer/issues/7505

## Opening post (cmsdmwmbot, 2023-01-25T16:25:10Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_0_1**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-01-25 17:25:09
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/367/)

## Comment (belforte, 2023-01-25T16:31:15Z)

aim to validate v3.221205 i.e. latest tag

## Comment (cmsdmwmbot, 2023-01-25T16:31:19Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230125_162956:cmsbot_crab_20230125_172954
230125_163000:cmsbot_crab_20230125_172957
230125_163004:cmsbot_crab_20230125_173001
230125_163008:cmsbot_crab_20230125_173005
230125_163012:cmsbot_crab_20230125_173009
230125_163056:cmsbot_crab_20230125_173013
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230125_162751:cmsbot_crab_transferOutputs
230125_162755:cmsbot_crab_transferLogs
230125_162759:cmsbot_crab_activity
230125_162802:cmsbot_crab_inputFiles
230125_162806:cmsbot_crab_disableAutomaticOutputCollection
230125_162810:cmsbot_crab_outputFiles
230125_162814:cmsbot_crab_allowUndistributedCMSSW
230125_162818:cmsbot_crab_maxMemoryMB
230125_162821:cmsbot_crab_maxJobRuntimeMin
230125_162825:cmsbot_crab_numCores
230125_162829:cmsbot_crab_scriptExe
230125_162832:cmsbot_crab_scriptArgs
230125_162836:cmsbot_crab_sendPythonFolder
230125_162849:cmsbot_crab_sendExternalFolder
230125_162852:cmsbot_crab_inputDBS
230125_162856:cmsbot_crab_useParent
230125_162859:cmsbot_crab_secondaryInputDataset
230125_162903:cmsbot_crab_lumiMaskFile
230125_162907:cmsbot_crab_lumiMaskUrl
230125_162912:cmsbot_crab_outLFNDirBase
230125_162915:cmsbot_crab_runRange
230125_162919:cmsbot_crab_ignoreLocality
230125_162923:cmsbot_crab_userInputFiles
230125_162926:cmsbot_crab_whitelist
230125_162930:cmsbot_crab_blacklist
230125_162934:cmsbot_crab_ignoreGlobalBlacklist
230125_162938:cmsbot_crab_voRole
230125_162942:cmsbot_crab_voGroup
230125_162945:cmsbot_crab_scheddName
230125_162949:cmsbot_crab_collector
230125_162952:cmsbot_crab_extraJDL
```

Finished at: 2023-01-25 17:30:57
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/367/console)

## Comment (cmsdmwmbot, 2023-01-25T16:57:28Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-01-25 17:57:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/564/console

```
RETRY TESTS:
transferLogs-check.sh 230125_162755:cmsbot_crab_transferLogs - 2
activity-check.sh 230125_162759:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 230125_162818:cmsbot_crab_maxMemoryMB - 2
scriptExe-check.sh 230125_162829:cmsbot_crab_scriptExe - 2
useParent-check.sh 230125_162856:cmsbot_crab_useParent - 2
lumiMaskFile-check.sh 230125_162903:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230125_162907:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230125_162915:cmsbot_crab_runRange - 2
whitelist-check.sh 230125_162926:cmsbot_crab_whitelist - 2
blacklist-check.sh 230125_162930:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230125_162934:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230125_162938:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230125_162751:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 230125_162802:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230125_162806:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230125_162810:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230125_162814:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230125_162821:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230125_162825:cmsbot_crab_numCores - 0
scriptArgs-check.sh 230125_162832:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230125_162836:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230125_162849:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230125_162852:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230125_162859:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 230125_162912:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230125_162919:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230125_162923:cmsbot_crab_userInputFiles - 0
voGroup-check.sh 230125_162942:cmsbot_crab_voGroup - 0
scheddName-check.sh 230125_162945:cmsbot_crab_scheddName - 0
collector-check.sh 230125_162949:cmsbot_crab_collector - 0
extraJDL-check.sh 230125_162952:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-01-25T17:24:14Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-01-25 18:24:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/565/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230125_162751:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230125_162755:cmsbot_crab_transferLogs - 0
activity-check.sh 230125_162759:cmsbot_crab_activity - 0
inputFiles-check.sh 230125_162802:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230125_162806:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230125_162810:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230125_162814:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230125_162818:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230125_162821:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230125_162825:cmsbot_crab_numCores - 0
scriptExe-check.sh 230125_162829:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230125_162832:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230125_162836:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230125_162849:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230125_162852:cmsbot_crab_inputDBS - 0
useParent-check.sh 230125_162856:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230125_162859:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230125_162903:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230125_162907:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230125_162912:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230125_162915:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230125_162919:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230125_162923:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230125_162926:cmsbot_crab_whitelist - 0
blacklist-check.sh 230125_162930:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230125_162934:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230125_162938:cmsbot_crab_voRole - 0
voGroup-check.sh 230125_162942:cmsbot_crab_voGroup - 0
scheddName-check.sh 230125_162945:cmsbot_crab_scheddName - 0
collector-check.sh 230125_162949:cmsbot_crab_collector - 0
extraJDL-check.sh 230125_162952:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-01-25T17:33:51Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-01-25 18:33:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/416/console

```
{'TN': '230125_162956:cmsbot_crab_20230125_172954', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 999, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230125_163000:cmsbot_crab_20230125_172957', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230125_163004:cmsbot_crab_20230125_173001', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163008:cmsbot_crab_20230125_173005', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163012:cmsbot_crab_20230125_173009', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163056:cmsbot_crab_20230125_173013', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 8, 'transferring': 1, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-01-25T18:36:49Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-01-25 19:36:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/417/console

```
{'TN': '230125_162956:cmsbot_crab_20230125_172954', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230125_163000:cmsbot_crab_20230125_172957', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 7}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163004:cmsbot_crab_20230125_173001', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163008:cmsbot_crab_20230125_173005', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163012:cmsbot_crab_20230125_173009', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163056:cmsbot_crab_20230125_173013', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-01-25T19:39:42Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-01-25 20:39:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/418/console

```
{'TN': '230125_162956:cmsbot_crab_20230125_172954', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163000:cmsbot_crab_20230125_172957', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 7}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163004:cmsbot_crab_20230125_173001', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163008:cmsbot_crab_20230125_173005', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163012:cmsbot_crab_20230125_173009', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230125_163056:cmsbot_crab_20230125_173013', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-01-26T08:39:18Z)

all OK, including publication
