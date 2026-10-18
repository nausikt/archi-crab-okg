# dmwm/CRABServer issue #7852: #470: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-08-24T13:44:55Z
Closed: 2023-08-25T09:04:34Z
URL: https://github.com/dmwm/CRABServer/issues/7852

## Opening post (cmsdmwmbot, 2023-08-24T13:44:55Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-08-24 15:44:54
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/470/)

## Comment (cmsdmwmbot, 2023-08-24T13:48:06Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230824_134721:cmsbot_crab_20230824_154720
230824_134722:cmsbot_crab_20230824_154721
230824_134724:cmsbot_crab_20230824_154723
230824_134725:cmsbot_crab_20230824_154724
230824_134727:cmsbot_crab_20230824_154726
230824_134745:cmsbot_crab_20230824_154727
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230824_134542:cmsbot_crab_transferOutputs
230824_134544:cmsbot_crab_transferLogs
230824_134546:cmsbot_crab_activity
230824_134547:cmsbot_crab_inputFiles
230824_134549:cmsbot_crab_disableAutomaticOutputCollection
230824_134551:cmsbot_crab_outputFiles
230824_134553:cmsbot_crab_allowUndistributedCMSSW
230824_134554:cmsbot_crab_maxMemoryMB
230824_134556:cmsbot_crab_maxJobRuntimeMin
230824_134557:cmsbot_crab_numCores
230824_134559:cmsbot_crab_scriptExe
230824_134601:cmsbot_crab_scriptArgs
230824_134602:cmsbot_crab_sendPythonFolder
230824_134651:cmsbot_crab_sendExternalFolder
230824_134653:cmsbot_crab_inputDBS
230824_134654:cmsbot_crab_useParent
230824_134656:cmsbot_crab_secondaryInputDataset
230824_134657:cmsbot_crab_lumiMaskFile
230824_134659:cmsbot_crab_lumiMaskUrl
230824_134701:cmsbot_crab_outLFNDirBase
230824_134703:cmsbot_crab_runRange
230824_134704:cmsbot_crab_ignoreLocality
230824_134706:cmsbot_crab_userInputFiles
230824_134707:cmsbot_crab_whitelist
230824_134709:cmsbot_crab_blacklist
230824_134711:cmsbot_crab_ignoreGlobalBlacklist
230824_134712:cmsbot_crab_voRole
230824_134714:cmsbot_crab_voGroup
230824_134715:cmsbot_crab_scheddName
230824_134717:cmsbot_crab_collector
230824_134718:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230824_134540:cmsbot_crab_20230824_154539
```

Finished at: 2023-08-24 15:47:45
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/470/console)

## Comment (cmsdmwmbot, 2023-08-24T14:09:05Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-08-24 16:09:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/371/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/371//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-08-24T14:10:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-24 16:10:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/627/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 57, 'transferring': 938, 'finished': 5}, 'TN': '230824_134721:cmsbot_crab_20230824_154720', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'finished': 4}, 'TN': '230824_134722:cmsbot_crab_20230824_154721', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230824_134724:cmsbot_crab_20230824_154723', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230824_134725:cmsbot_crab_20230824_154724', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 31, 'transferring': 69}, 'TN': '230824_134727:cmsbot_crab_20230824_154726', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230824_134745:cmsbot_crab_20230824_154727', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-24T14:10:58Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-24 16:10:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/779/console

```
RETRY TESTS:
outputFiles-check.sh 230824_134551:cmsbot_crab_outputFiles - 2
lumiMaskUrl-check.sh 230824_134659:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230824_134703:cmsbot_crab_runRange - 2
whitelist-check.sh 230824_134707:cmsbot_crab_whitelist - 2
blacklist-check.sh 230824_134709:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230824_134542:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230824_134544:cmsbot_crab_transferLogs - 0
activity-check.sh 230824_134546:cmsbot_crab_activity - 0
inputFiles-check.sh 230824_134547:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230824_134549:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230824_134553:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230824_134554:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230824_134556:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230824_134557:cmsbot_crab_numCores - 0
scriptExe-check.sh 230824_134559:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230824_134601:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230824_134602:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230824_134651:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230824_134653:cmsbot_crab_inputDBS - 0
useParent-check.sh 230824_134654:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230824_134656:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230824_134657:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230824_134701:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230824_134704:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230824_134706:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230824_134711:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230824_134712:cmsbot_crab_voRole - 0
voGroup-check.sh 230824_134714:cmsbot_crab_voGroup - 0
scheddName-check.sh 230824_134715:cmsbot_crab_scheddName - 0
collector-check.sh 230824_134717:cmsbot_crab_collector - 0
extraJDL-check.sh 230824_134718:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-24T14:27:40Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2023-08-24 16:27:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/628/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 478, 'transferring': 517, 'running': 5}, 'TN': '230824_134721:cmsbot_crab_20230824_154720', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/6/6'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230824_134722:cmsbot_crab_20230824_154721', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230824_134724:cmsbot_crab_20230824_154723', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'TN': '230824_134725:cmsbot_crab_20230824_154724', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 31, 'transferring': 69}, 'TN': '230824_134727:cmsbot_crab_20230824_154726', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/31/31'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230824_134745:cmsbot_crab_20230824_154727', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-24T14:33:18Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-08-24 16:33:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/780/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230824_134542:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230824_134544:cmsbot_crab_transferLogs - 0
activity-check.sh 230824_134546:cmsbot_crab_activity - 0
inputFiles-check.sh 230824_134547:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230824_134549:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230824_134551:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230824_134553:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230824_134554:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230824_134556:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230824_134557:cmsbot_crab_numCores - 0
scriptExe-check.sh 230824_134559:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230824_134601:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230824_134602:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230824_134651:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230824_134653:cmsbot_crab_inputDBS - 0
useParent-check.sh 230824_134654:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230824_134656:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230824_134657:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230824_134659:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230824_134701:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230824_134703:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230824_134704:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230824_134706:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230824_134707:cmsbot_crab_whitelist - 0
blacklist-check.sh 230824_134709:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230824_134711:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230824_134712:cmsbot_crab_voRole - 0
voGroup-check.sh 230824_134714:cmsbot_crab_voGroup - 0
scheddName-check.sh 230824_134715:cmsbot_crab_scheddName - 0
collector-check.sh 230824_134717:cmsbot_crab_collector - 0
extraJDL-check.sh 230824_134718:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-08-24T15:14:51Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2023-08-24 17:14:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/629/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 995, 'transferring': 4}, 'TN': '230824_134721:cmsbot_crab_20230824_154720', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/906/906'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '230824_134722:cmsbot_crab_20230824_154721', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230824_134724:cmsbot_crab_20230824_154723', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230824_134725:cmsbot_crab_20230824_154724', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230824_134727:cmsbot_crab_20230824_154726', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230824_134745:cmsbot_crab_20230824_154727', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-24T16:50:30Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2023-08-24 18:50:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/630/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230824_134721:cmsbot_crab_20230824_154720', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230824_134722:cmsbot_crab_20230824_154721', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230824_134724:cmsbot_crab_20230824_154723', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230824_134725:cmsbot_crab_20230824_154724', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230824_134727:cmsbot_crab_20230824_154726', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230824_134745:cmsbot_crab_20230824_154727', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```
