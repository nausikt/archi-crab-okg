# dmwm/CRABServer issue #7871: #472: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-09-12T15:26:53Z
Closed: 2023-09-13T08:11:36Z
URL: https://github.com/dmwm/CRABServer/issues/7871

## Opening post (cmsdmwmbot, 2023-09-12T15:26:53Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-09-12 17:26:53
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/472/)

## Comment (cmsdmwmbot, 2023-09-12T15:29:36Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230912_152858:cmsbot_crab_20230912_172857
230912_152859:cmsbot_crab_20230912_172859
230912_152901:cmsbot_crab_20230912_172900
230912_152902:cmsbot_crab_20230912_172901
230912_152903:cmsbot_crab_20230912_172903
230912_152914:cmsbot_crab_20230912_172904
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230912_152724:cmsbot_crab_transferOutputs
230912_152727:cmsbot_crab_transferLogs
230912_152730:cmsbot_crab_activity
230912_152732:cmsbot_crab_inputFiles
230912_152733:cmsbot_crab_disableAutomaticOutputCollection
230912_152735:cmsbot_crab_outputFiles
230912_152737:cmsbot_crab_allowUndistributedCMSSW
230912_152739:cmsbot_crab_maxMemoryMB
230912_152741:cmsbot_crab_maxJobRuntimeMin
230912_152743:cmsbot_crab_numCores
230912_152744:cmsbot_crab_scriptExe
230912_152746:cmsbot_crab_scriptArgs
230912_152748:cmsbot_crab_sendPythonFolder
230912_152830:cmsbot_crab_sendExternalFolder
230912_152831:cmsbot_crab_inputDBS
230912_152833:cmsbot_crab_useParent
230912_152834:cmsbot_crab_secondaryInputDataset
230912_152835:cmsbot_crab_lumiMaskFile
230912_152837:cmsbot_crab_lumiMaskUrl
230912_152839:cmsbot_crab_outLFNDirBase
230912_152841:cmsbot_crab_runRange
230912_152843:cmsbot_crab_ignoreLocality
230912_152845:cmsbot_crab_userInputFiles
230912_152846:cmsbot_crab_whitelist
230912_152847:cmsbot_crab_blacklist
230912_152849:cmsbot_crab_ignoreGlobalBlacklist
230912_152850:cmsbot_crab_voRole
230912_152851:cmsbot_crab_voGroup
230912_152853:cmsbot_crab_scheddName
230912_152854:cmsbot_crab_collector
230912_152856:cmsbot_crab_extraJDL
```

Finished at: 2023-09-12 17:29:15
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/472/console)

## Comment (cmsdmwmbot, 2023-09-12T15:51:47Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-09-12 17:51:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/635/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 372, 'transferring': 615, 'running': 13}, 'TN': '230912_152858:cmsbot_crab_20230912_172857', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'TN': '230912_152859:cmsbot_crab_20230912_172859', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230912_152901:cmsbot_crab_20230912_172900', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230912_152902:cmsbot_crab_20230912_172901', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 34, 'transferring': 66}, 'TN': '230912_152903:cmsbot_crab_20230912_172903', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 3, 'running': 1}, 'TN': '230912_152914:cmsbot_crab_20230912_172904', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-09-12T15:52:52Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-09-12 17:52:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/782/console

```
RETRY TESTS:
activity-check.sh 230912_152730:cmsbot_crab_activity - 2
lumiMaskUrl-check.sh 230912_152837:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230912_152841:cmsbot_crab_runRange - 2
whitelist-check.sh 230912_152846:cmsbot_crab_whitelist - 2
blacklist-check.sh 230912_152847:cmsbot_crab_blacklist - 2
voGroup-check.sh 230912_152851:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230912_152724:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230912_152727:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230912_152732:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230912_152733:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230912_152735:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230912_152737:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230912_152739:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230912_152741:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230912_152743:cmsbot_crab_numCores - 0
scriptExe-check.sh 230912_152744:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230912_152746:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230912_152748:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230912_152830:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230912_152831:cmsbot_crab_inputDBS - 0
useParent-check.sh 230912_152833:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230912_152834:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230912_152835:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230912_152839:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230912_152843:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230912_152845:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230912_152849:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230912_152850:cmsbot_crab_voRole - 0
scheddName-check.sh 230912_152853:cmsbot_crab_scheddName - 0
collector-check.sh 230912_152854:cmsbot_crab_collector - 0
extraJDL-check.sh 230912_152856:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-09-12T16:09:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2023-09-12 18:09:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/636/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 954, 'transferring': 37, 'running': 9}, 'TN': '230912_152858:cmsbot_crab_20230912_172857', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/300/300'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230912_152859:cmsbot_crab_20230912_172859', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230912_152901:cmsbot_crab_20230912_172900', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'TN': '230912_152902:cmsbot_crab_20230912_172901', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'TN': '230912_152903:cmsbot_crab_20230912_172903', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/34/34'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'TN': '230912_152914:cmsbot_crab_20230912_172904', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/6/6'}
```

## Comment (cmsdmwmbot, 2023-09-12T16:15:02Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-09-12 18:15:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/783/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230912_152724:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230912_152727:cmsbot_crab_transferLogs - 0
activity-check.sh 230912_152730:cmsbot_crab_activity - 0
inputFiles-check.sh 230912_152732:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230912_152733:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230912_152735:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230912_152737:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230912_152739:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230912_152741:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230912_152743:cmsbot_crab_numCores - 0
scriptExe-check.sh 230912_152744:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230912_152746:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230912_152748:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230912_152830:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230912_152831:cmsbot_crab_inputDBS - 0
useParent-check.sh 230912_152833:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230912_152834:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230912_152835:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230912_152837:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230912_152839:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230912_152841:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230912_152843:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230912_152845:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230912_152846:cmsbot_crab_whitelist - 0
blacklist-check.sh 230912_152847:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230912_152849:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230912_152850:cmsbot_crab_voRole - 0
voGroup-check.sh 230912_152851:cmsbot_crab_voGroup - 0
scheddName-check.sh 230912_152853:cmsbot_crab_scheddName - 0
collector-check.sh 230912_152854:cmsbot_crab_collector - 0
extraJDL-check.sh 230912_152856:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-09-12T16:56:34Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2023-09-12 18:56:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/638/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 5, 'finished': 991, 'transferring': 4}, 'TN': '230912_152858:cmsbot_crab_20230912_172857', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/991/991'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '230912_152859:cmsbot_crab_20230912_172859', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230912_152901:cmsbot_crab_20230912_172900', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230912_152902:cmsbot_crab_20230912_172901', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230912_152903:cmsbot_crab_20230912_172903', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230912_152914:cmsbot_crab_20230912_172904', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```

## Comment (cmsdmwmbot, 2023-09-12T18:29:01Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2023-09-12 20:29:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/639/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230912_152858:cmsbot_crab_20230912_172857', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230912_152859:cmsbot_crab_20230912_172859', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230912_152901:cmsbot_crab_20230912_172900', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230912_152902:cmsbot_crab_20230912_172901', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230912_152903:cmsbot_crab_20230912_172903', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230912_152914:cmsbot_crab_20230912_172904', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```

## Comment (novicecpp, 2023-09-13T08:11:36Z)

Nice. Thanks @belforte for auto resubmission.
