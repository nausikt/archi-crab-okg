# dmwm/CRABServer issue #7535: #374: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2023-02-15T19:44:55Z
Closed: 2023-02-17T11:47:27Z
URL: https://github.com/dmwm/CRABServer/issues/7535

## Opening post (cmsdmwmbot, 2023-02-15T19:44:55Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-02-15 20:44:54
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/374/)

## Comment (cmsdmwmbot, 2023-02-15T19:49:05Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230215_194819:cmsbot_crab_20230215_204815
230215_194823:cmsbot_crab_20230215_204819
230215_194827:cmsbot_crab_20230215_204823
230215_194832:cmsbot_crab_20230215_204828
230215_194836:cmsbot_crab_20230215_204832
230215_194843:cmsbot_crab_20230215_204836
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230215_194635:cmsbot_crab_transferOutputs
230215_194638:cmsbot_crab_transferLogs
230215_194641:cmsbot_crab_activity
230215_194644:cmsbot_crab_inputFiles
230215_194648:cmsbot_crab_disableAutomaticOutputCollection
230215_194651:cmsbot_crab_outputFiles
230215_194654:cmsbot_crab_allowUndistributedCMSSW
230215_194657:cmsbot_crab_maxMemoryMB
230215_194700:cmsbot_crab_maxJobRuntimeMin
230215_194704:cmsbot_crab_numCores
230215_194707:cmsbot_crab_scriptExe
230215_194710:cmsbot_crab_scriptArgs
230215_194713:cmsbot_crab_sendPythonFolder
230215_194719:cmsbot_crab_sendExternalFolder
230215_194722:cmsbot_crab_inputDBS
230215_194725:cmsbot_crab_useParent
230215_194728:cmsbot_crab_secondaryInputDataset
230215_194732:cmsbot_crab_lumiMaskFile
230215_194735:cmsbot_crab_lumiMaskUrl
230215_194739:cmsbot_crab_outLFNDirBase
230215_194742:cmsbot_crab_runRange
230215_194745:cmsbot_crab_ignoreLocality
230215_194748:cmsbot_crab_userInputFiles
230215_194751:cmsbot_crab_whitelist
230215_194755:cmsbot_crab_blacklist
230215_194758:cmsbot_crab_ignoreGlobalBlacklist
230215_194801:cmsbot_crab_voRole
230215_194804:cmsbot_crab_voGroup
230215_194808:cmsbot_crab_scheddName
230215_194811:cmsbot_crab_collector
230215_194814:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230215_194631:cmsbot_crab_20230215_204626
```

Finished at: 2023-02-15 20:48:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/374/console)

## Comment (cmsdmwmbot, 2023-02-15T20:13:46Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-02-15 21:13:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/335/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/335//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-02-15T20:15:13Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-15 21:15:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/577/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230215_194657:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230215_194700:cmsbot_crab_maxJobRuntimeMin - 2
scriptArgs-check.sh 230215_194710:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 230215_194735:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230215_194739:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230215_194742:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230215_194748:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230215_194751:cmsbot_crab_whitelist - 2
blacklist-check.sh 230215_194755:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230215_194635:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230215_194638:cmsbot_crab_transferLogs - 0
activity-check.sh 230215_194641:cmsbot_crab_activity - 0
inputFiles-check.sh 230215_194644:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230215_194648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230215_194651:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230215_194654:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 230215_194704:cmsbot_crab_numCores - 0
scriptExe-check.sh 230215_194707:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230215_194713:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230215_194719:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230215_194722:cmsbot_crab_inputDBS - 0
useParent-check.sh 230215_194725:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230215_194728:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230215_194732:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230215_194745:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230215_194758:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230215_194801:cmsbot_crab_voRole - 0
voGroup-check.sh 230215_194804:cmsbot_crab_voGroup - 0
scheddName-check.sh 230215_194808:cmsbot_crab_scheddName - 0
collector-check.sh 230215_194811:cmsbot_crab_collector - 0
extraJDL-check.sh 230215_194814:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-02-15T20:43:13Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-02-15 21:43:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/578/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230215_194635:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230215_194638:cmsbot_crab_transferLogs - 0
activity-check.sh 230215_194641:cmsbot_crab_activity - 0
inputFiles-check.sh 230215_194644:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230215_194648:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230215_194651:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230215_194654:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230215_194657:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230215_194700:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230215_194704:cmsbot_crab_numCores - 0
scriptExe-check.sh 230215_194707:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230215_194710:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230215_194713:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230215_194719:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230215_194722:cmsbot_crab_inputDBS - 0
useParent-check.sh 230215_194725:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230215_194728:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230215_194732:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230215_194735:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230215_194739:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230215_194742:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230215_194745:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230215_194748:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230215_194751:cmsbot_crab_whitelist - 0
blacklist-check.sh 230215_194755:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230215_194758:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230215_194801:cmsbot_crab_voRole - 0
voGroup-check.sh 230215_194804:cmsbot_crab_voGroup - 0
scheddName-check.sh 230215_194808:cmsbot_crab_scheddName - 0
collector-check.sh 230215_194811:cmsbot_crab_collector - 0
extraJDL-check.sh 230215_194814:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-02-15T20:53:39Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-15 21:53:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/432/console

```
{'TN': '230215_194819:cmsbot_crab_20230215_204815', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 999, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230215_194823:cmsbot_crab_20230215_204819', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230215_194827:cmsbot_crab_20230215_204823', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_194832:cmsbot_crab_20230215_204828', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_194836:cmsbot_crab_20230215_204832', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_194843:cmsbot_crab_20230215_204836', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-02-15T21:57:26Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-02-15 22:57:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/434/console

```
{'TN': '230215_194819:cmsbot_crab_20230215_204815', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 999}, 'combinedStatus': 'FAILED'}
{'TN': '230215_194823:cmsbot_crab_20230215_204819', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 7}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_194827:cmsbot_crab_20230215_204823', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_194832:cmsbot_crab_20230215_204828', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_194836:cmsbot_crab_20230215_204832', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_194843:cmsbot_crab_20230215_204836', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (novicecpp, 2023-02-17T11:47:27Z)

Everything is working fine. Closing.
