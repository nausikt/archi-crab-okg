# dmwm/CRABServer issue #7654: #392: Test dev CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-06-05T09:57:30Z
Closed: 2023-06-05T14:24:54Z
URL: https://github.com/dmwm/CRABServer/issues/7654

## Opening post (cmsdmwmbot, 2023-06-05T09:57:30Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-06-05 11:57:29
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/392/)

## Comment (cmsdmwmbot, 2023-06-05T09:59:56Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230605_095904:cmsbot_crab_20230605_115904
230605_095906:cmsbot_crab_20230605_115905
230605_095907:cmsbot_crab_20230605_115907
230605_095909:cmsbot_crab_20230605_115908
230605_095910:cmsbot_crab_20230605_115910
230605_095934:cmsbot_crab_20230605_115911
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230605_095807:cmsbot_crab_transferOutputs
230605_095808:cmsbot_crab_transferLogs
230605_095810:cmsbot_crab_activity
230605_095811:cmsbot_crab_inputFiles
230605_095813:cmsbot_crab_disableAutomaticOutputCollection
230605_095815:cmsbot_crab_outputFiles
230605_095816:cmsbot_crab_allowUndistributedCMSSW
230605_095818:cmsbot_crab_maxMemoryMB
230605_095819:cmsbot_crab_maxJobRuntimeMin
230605_095821:cmsbot_crab_numCores
230605_095822:cmsbot_crab_scriptExe
230605_095824:cmsbot_crab_scriptArgs
230605_095825:cmsbot_crab_sendPythonFolder
230605_095834:cmsbot_crab_sendExternalFolder
230605_095836:cmsbot_crab_inputDBS
230605_095838:cmsbot_crab_useParent
230605_095839:cmsbot_crab_secondaryInputDataset
230605_095841:cmsbot_crab_lumiMaskFile
230605_095843:cmsbot_crab_lumiMaskUrl
230605_095845:cmsbot_crab_outLFNDirBase
230605_095847:cmsbot_crab_runRange
230605_095848:cmsbot_crab_ignoreLocality
230605_095850:cmsbot_crab_userInputFiles
230605_095851:cmsbot_crab_whitelist
230605_095853:cmsbot_crab_blacklist
230605_095854:cmsbot_crab_ignoreGlobalBlacklist
230605_095856:cmsbot_crab_voRole
230605_095857:cmsbot_crab_voGroup
230605_095859:cmsbot_crab_scheddName
230605_095901:cmsbot_crab_collector
230605_095902:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230605_095805:cmsbot_crab_20230605_115803
```

Finished at: 2023-06-05 11:59:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/392/console)

## Comment (cmsdmwmbot, 2023-06-05T10:22:26Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-06-05 12:22:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/344/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/344//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-05T10:23:36Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-05 12:23:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/605/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230605_095818:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230605_095819:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230605_095821:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 230605_095843:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230605_095847:cmsbot_crab_runRange - 2
whitelist-check.sh 230605_095851:cmsbot_crab_whitelist - 2
blacklist-check.sh 230605_095853:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230605_095807:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230605_095808:cmsbot_crab_transferLogs - 0
activity-check.sh 230605_095810:cmsbot_crab_activity - 0
inputFiles-check.sh 230605_095811:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230605_095813:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230605_095815:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230605_095816:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 230605_095822:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230605_095824:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230605_095825:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230605_095834:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230605_095836:cmsbot_crab_inputDBS - 0
useParent-check.sh 230605_095838:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230605_095839:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230605_095841:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230605_095845:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230605_095848:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230605_095850:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230605_095854:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230605_095856:cmsbot_crab_voRole - 0
voGroup-check.sh 230605_095857:cmsbot_crab_voGroup - 0
scheddName-check.sh 230605_095859:cmsbot_crab_scheddName - 0
collector-check.sh 230605_095901:cmsbot_crab_collector - 0
extraJDL-check.sh 230605_095902:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-05T10:47:24Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-05 12:47:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/606/console

```
RETRY TESTS:
numCores-check.sh 230605_095821:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230605_095807:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230605_095808:cmsbot_crab_transferLogs - 0
activity-check.sh 230605_095810:cmsbot_crab_activity - 0
inputFiles-check.sh 230605_095811:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230605_095813:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230605_095815:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230605_095816:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230605_095818:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230605_095819:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230605_095822:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230605_095824:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230605_095825:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230605_095834:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230605_095836:cmsbot_crab_inputDBS - 0
useParent-check.sh 230605_095838:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230605_095839:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230605_095841:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230605_095843:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230605_095845:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230605_095847:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230605_095848:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230605_095850:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230605_095851:cmsbot_crab_whitelist - 0
blacklist-check.sh 230605_095853:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230605_095854:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230605_095856:cmsbot_crab_voRole - 0
voGroup-check.sh 230605_095857:cmsbot_crab_voGroup - 0
scheddName-check.sh 230605_095859:cmsbot_crab_scheddName - 0
collector-check.sh 230605_095901:cmsbot_crab_collector - 0
extraJDL-check.sh 230605_095902:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-05T11:03:35Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-05 13:03:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/455/console

```
{'TN': '230605_095904:cmsbot_crab_20230605_115904', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 22, 'finished': 978}, 'combinedStatus': 'FAILED'}
{'TN': '230605_095906:cmsbot_crab_20230605_115905', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230605_095907:cmsbot_crab_20230605_115907', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230605_095909:cmsbot_crab_20230605_115908', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230605_095910:cmsbot_crab_20230605_115910', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230605_095934:cmsbot_crab_20230605_115911', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-06-05T11:11:34Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-06-05 13:11:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/607/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230605_095807:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230605_095808:cmsbot_crab_transferLogs - 0
activity-check.sh 230605_095810:cmsbot_crab_activity - 0
inputFiles-check.sh 230605_095811:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230605_095813:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230605_095815:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230605_095816:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230605_095818:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230605_095819:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230605_095821:cmsbot_crab_numCores - 0
scriptExe-check.sh 230605_095822:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230605_095824:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230605_095825:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230605_095834:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230605_095836:cmsbot_crab_inputDBS - 0
useParent-check.sh 230605_095838:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230605_095839:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230605_095841:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230605_095843:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230605_095845:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230605_095847:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230605_095848:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230605_095850:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230605_095851:cmsbot_crab_whitelist - 0
blacklist-check.sh 230605_095853:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230605_095854:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230605_095856:cmsbot_crab_voRole - 0
voGroup-check.sh 230605_095857:cmsbot_crab_voGroup - 0
scheddName-check.sh 230605_095859:cmsbot_crab_scheddName - 0
collector-check.sh 230605_095901:cmsbot_crab_collector - 0
extraJDL-check.sh 230605_095902:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-05T12:07:25Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-05 14:07:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/456/console

```
{'TN': '230605_095904:cmsbot_crab_20230605_115904', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 22, 'finished': 978}, 'combinedStatus': 'FAILED'}
{'TN': '230605_095906:cmsbot_crab_20230605_115905', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'combinedStatus': 'COMPLETED'}
{'TN': '230605_095907:cmsbot_crab_20230605_115907', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230605_095909:cmsbot_crab_20230605_115908', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230605_095910:cmsbot_crab_20230605_115910', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230605_095934:cmsbot_crab_20230605_115911', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (mapellidario, 2023-06-05T14:24:54Z)

all the failures in the task `230605_095904:cmsbot_crab_20230605_115904` are from 8001 at GRIF_LLR. It is very likely that this is a site problem and that crab itself is ok. I will close this issue, all good here! :)
