# dmwm/CRABServer issue #7804: #453: Test prod CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-08-10T20:56:38Z
Closed: 2023-08-11T11:08:44Z
URL: https://github.com/dmwm/CRABServer/issues/7804

## Opening post (cmsdmwmbot, 2023-08-10T20:56:38Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-08-10 22:56:37
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/453/)

## Comment (cmsdmwmbot, 2023-08-10T21:00:27Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230810_205948:cmsbot_crab_20230810_225945
230810_205950:cmsbot_crab_20230810_225948
230810_205953:cmsbot_crab_20230810_225951
230810_205956:cmsbot_crab_20230810_225954
230810_205959:cmsbot_crab_20230810_225957
230810_210005:cmsbot_crab_20230810_230000
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230810_205808:cmsbot_crab_transferOutputs
230810_205811:cmsbot_crab_transferLogs
230810_205814:cmsbot_crab_activity
230810_205817:cmsbot_crab_inputFiles
230810_205820:cmsbot_crab_disableAutomaticOutputCollection
230810_205823:cmsbot_crab_outputFiles
230810_205826:cmsbot_crab_allowUndistributedCMSSW
230810_205829:cmsbot_crab_maxMemoryMB
230810_205832:cmsbot_crab_maxJobRuntimeMin
230810_205835:cmsbot_crab_numCores
230810_205838:cmsbot_crab_scriptExe
230810_205841:cmsbot_crab_scriptArgs
230810_205844:cmsbot_crab_sendPythonFolder
230810_205851:cmsbot_crab_sendExternalFolder
230810_205855:cmsbot_crab_inputDBS
230810_205858:cmsbot_crab_useParent
230810_205901:cmsbot_crab_secondaryInputDataset
230810_205904:cmsbot_crab_lumiMaskFile
230810_205907:cmsbot_crab_lumiMaskUrl
230810_205911:cmsbot_crab_outLFNDirBase
230810_205914:cmsbot_crab_runRange
230810_205917:cmsbot_crab_ignoreLocality
230810_205920:cmsbot_crab_userInputFiles
230810_205923:cmsbot_crab_whitelist
230810_205926:cmsbot_crab_blacklist
230810_205929:cmsbot_crab_ignoreGlobalBlacklist
230810_205932:cmsbot_crab_voRole
230810_205935:cmsbot_crab_voGroup
230810_205938:cmsbot_crab_scheddName
230810_205941:cmsbot_crab_collector
230810_205944:cmsbot_crab_extraJDL
```

Finished at: 2023-08-10 23:00:06
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/453/console)

## Comment (cmsdmwmbot, 2023-08-10T21:25:35Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-10 23:25:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/776/console

```
RETRY TESTS:
activity-check.sh 230810_205814:cmsbot_crab_activity - 2
outputFiles-check.sh 230810_205823:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230810_205829:cmsbot_crab_maxMemoryMB - 2
scriptExe-check.sh 230810_205838:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 230810_205907:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230810_205914:cmsbot_crab_runRange - 2
blacklist-check.sh 230810_205926:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230810_205929:cmsbot_crab_ignoreGlobalBlacklist - 2
voGroup-check.sh 230810_205935:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230810_205808:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230810_205811:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230810_205817:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230810_205820:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230810_205826:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230810_205832:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230810_205835:cmsbot_crab_numCores - 0
scriptArgs-check.sh 230810_205841:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230810_205844:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230810_205851:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230810_205855:cmsbot_crab_inputDBS - 0
useParent-check.sh 230810_205858:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230810_205901:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230810_205904:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230810_205911:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230810_205917:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230810_205920:cmsbot_crab_userInputFiles - 0
voRole-check.sh 230810_205932:cmsbot_crab_voRole - 0
scheddName-check.sh 230810_205938:cmsbot_crab_scheddName - 0
extraJDL-check.sh 230810_205944:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230810_205923:cmsbot_crab_whitelist - 1
collector-check.sh 230810_205941:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2023-08-10T21:51:02Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-08-10 23:51:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/778/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230810_205808:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230810_205811:cmsbot_crab_transferLogs - 0
activity-check.sh 230810_205814:cmsbot_crab_activity - 0
inputFiles-check.sh 230810_205817:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230810_205820:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230810_205823:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230810_205826:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230810_205829:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230810_205832:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230810_205835:cmsbot_crab_numCores - 0
scriptExe-check.sh 230810_205838:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230810_205841:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230810_205844:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230810_205851:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230810_205855:cmsbot_crab_inputDBS - 0
useParent-check.sh 230810_205858:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230810_205901:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230810_205904:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230810_205907:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230810_205911:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230810_205914:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230810_205917:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230810_205920:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230810_205926:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230810_205929:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230810_205932:cmsbot_crab_voRole - 0
voGroup-check.sh 230810_205935:cmsbot_crab_voGroup - 0
scheddName-check.sh 230810_205938:cmsbot_crab_scheddName - 0
extraJDL-check.sh 230810_205944:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230810_205923:cmsbot_crab_whitelist - 1
collector-check.sh 230810_205941:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2023-08-10T22:02:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-11 00:02:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/532/console

```
{'TN': '230810_205948:cmsbot_crab_20230810_225945', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 996, 'transferring': 4}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230810_205950:cmsbot_crab_20230810_225948', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230810_205953:cmsbot_crab_20230810_225951', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205956:cmsbot_crab_20230810_225954', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205959:cmsbot_crab_20230810_225957', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_210005:cmsbot_crab_20230810_230000', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-08-10T22:43:35Z)

CCV failed due to a couple `Cannot connect to the Rucio server.` in DataDiscovery. pff...

## Comment (cmsdmwmbot, 2023-08-10T23:04:57Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-08-11 01:04:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/534/console

```
{'TN': '230810_205948:cmsbot_crab_20230810_225945', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205950:cmsbot_crab_20230810_225948', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205953:cmsbot_crab_20230810_225951', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205956:cmsbot_crab_20230810_225954', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_205959:cmsbot_crab_20230810_225957', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230810_210005:cmsbot_crab_20230810_230000', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (belforte, 2023-08-11T11:08:44Z)

all OK
