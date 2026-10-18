# dmwm/CRABServer issue #7889: #474: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-09-21T15:55:04Z
Closed: 2023-09-21T21:58:50Z
URL: https://github.com/dmwm/CRABServer/issues/7889

## Opening post (cmsdmwmbot, 2023-09-21T15:55:04Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2023-09-21 17:55:03
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/474/)

## Comment (cmsdmwmbot, 2023-09-21T15:57:51Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230921_155709:cmsbot_crab_20230921_175708
230921_155710:cmsbot_crab_20230921_175709
230921_155711:cmsbot_crab_20230921_175711
230921_155713:cmsbot_crab_20230921_175712
230921_155715:cmsbot_crab_20230921_175714
230921_155730:cmsbot_crab_20230921_175715
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230921_155528:cmsbot_crab_transferOutputs
230921_155530:cmsbot_crab_transferLogs
230921_155533:cmsbot_crab_activity
230921_155535:cmsbot_crab_inputFiles
230921_155537:cmsbot_crab_disableAutomaticOutputCollection
230921_155539:cmsbot_crab_outputFiles
230921_155541:cmsbot_crab_allowUndistributedCMSSW
230921_155542:cmsbot_crab_maxMemoryMB
230921_155544:cmsbot_crab_maxJobRuntimeMin
230921_155546:cmsbot_crab_numCores
230921_155548:cmsbot_crab_scriptExe
230921_155550:cmsbot_crab_scriptArgs
230921_155551:cmsbot_crab_sendPythonFolder
230921_155639:cmsbot_crab_sendExternalFolder
230921_155641:cmsbot_crab_inputDBS
230921_155643:cmsbot_crab_useParent
230921_155645:cmsbot_crab_secondaryInputDataset
230921_155646:cmsbot_crab_lumiMaskFile
230921_155648:cmsbot_crab_lumiMaskUrl
230921_155651:cmsbot_crab_outLFNDirBase
230921_155652:cmsbot_crab_runRange
230921_155653:cmsbot_crab_ignoreLocality
230921_155655:cmsbot_crab_userInputFiles
230921_155656:cmsbot_crab_whitelist
230921_155658:cmsbot_crab_blacklist
230921_155659:cmsbot_crab_ignoreGlobalBlacklist
230921_155701:cmsbot_crab_voRole
230921_155702:cmsbot_crab_voGroup
230921_155703:cmsbot_crab_scheddName
230921_155705:cmsbot_crab_collector
230921_155706:cmsbot_crab_extraJDL
```

Finished at: 2023-09-21 17:57:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/474/console)

## Comment (cmsdmwmbot, 2023-09-21T16:22:33Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-09-21 18:22:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/784/console

```
RETRY TESTS:
maxMemoryMB-check.sh 230921_155542:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 230921_155546:cmsbot_crab_numCores - 2
useParent-check.sh 230921_155643:cmsbot_crab_useParent - 2
lumiMaskFile-check.sh 230921_155646:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230921_155648:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230921_155651:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230921_155652:cmsbot_crab_runRange - 2
whitelist-check.sh 230921_155656:cmsbot_crab_whitelist - 2
blacklist-check.sh 230921_155658:cmsbot_crab_blacklist - 2
voGroup-check.sh 230921_155702:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230921_155528:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230921_155530:cmsbot_crab_transferLogs - 0
activity-check.sh 230921_155533:cmsbot_crab_activity - 0
inputFiles-check.sh 230921_155535:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230921_155537:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230921_155539:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230921_155541:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 230921_155544:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230921_155548:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230921_155550:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230921_155551:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230921_155639:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230921_155641:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230921_155645:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 230921_155653:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230921_155655:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230921_155659:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230921_155701:cmsbot_crab_voRole - 0
scheddName-check.sh 230921_155703:cmsbot_crab_scheddName - 0
collector-check.sh 230921_155705:cmsbot_crab_collector - 0
extraJDL-check.sh 230921_155706:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-09-21T16:22:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-09-21 18:22:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/645/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 504, 'transferring': 494, 'running': 2}, 'TN': '230921_155709:cmsbot_crab_20230921_175708', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/500/500'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'TN': '230921_155710:cmsbot_crab_20230921_175709', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230921_155711:cmsbot_crab_20230921_175711', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230921_155713:cmsbot_crab_20230921_175712', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '230921_155715:cmsbot_crab_20230921_175714', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230921_155730:cmsbot_crab_20230921_175715', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-09-21T16:41:06Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2023-09-21 18:41:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/646/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 988, 'transferring': 11, 'running': 1}, 'TN': '230921_155709:cmsbot_crab_20230921_175708', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/500/500'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230921_155710:cmsbot_crab_20230921_175709', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1}, 'TN': '230921_155711:cmsbot_crab_20230921_175711', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 10}, 'TN': '230921_155713:cmsbot_crab_20230921_175712', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 98, 'transferring': 2}, 'TN': '230921_155715:cmsbot_crab_20230921_175714', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 2, 'transferring': 8}, 'TN': '230921_155730:cmsbot_crab_20230921_175715', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-09-21T16:44:51Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-09-21 18:44:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/785/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230921_155528:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230921_155530:cmsbot_crab_transferLogs - 0
activity-check.sh 230921_155533:cmsbot_crab_activity - 0
inputFiles-check.sh 230921_155535:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230921_155537:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230921_155539:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230921_155541:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230921_155542:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230921_155544:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230921_155546:cmsbot_crab_numCores - 0
scriptExe-check.sh 230921_155548:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230921_155550:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230921_155551:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230921_155639:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230921_155641:cmsbot_crab_inputDBS - 0
useParent-check.sh 230921_155643:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230921_155645:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230921_155646:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230921_155648:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230921_155651:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230921_155652:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230921_155653:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230921_155655:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230921_155656:cmsbot_crab_whitelist - 0
blacklist-check.sh 230921_155658:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230921_155659:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230921_155701:cmsbot_crab_voRole - 0
voGroup-check.sh 230921_155702:cmsbot_crab_voGroup - 0
scheddName-check.sh 230921_155703:cmsbot_crab_scheddName - 0
collector-check.sh 230921_155705:cmsbot_crab_collector - 0
extraJDL-check.sh 230921_155706:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-09-21T17:29:04Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2023-09-21 19:29:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/647/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1000}, 'TN': '230921_155709:cmsbot_crab_20230921_175708', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/999/999'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '230921_155710:cmsbot_crab_20230921_175709', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230921_155711:cmsbot_crab_20230921_175711', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230921_155713:cmsbot_crab_20230921_175712', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230921_155715:cmsbot_crab_20230921_175714', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230921_155730:cmsbot_crab_20230921_175715', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```

## Comment (cmsdmwmbot, 2023-09-21T19:03:05Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2023-09-21 21:03:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/648/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230921_155709:cmsbot_crab_20230921_175708', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230921_155710:cmsbot_crab_20230921_175709', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230921_155711:cmsbot_crab_20230921_175711', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230921_155713:cmsbot_crab_20230921_175712', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230921_155715:cmsbot_crab_20230921_175714', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230921_155730:cmsbot_crab_20230921_175715', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```

## Comment (belforte, 2023-09-21T21:58:50Z)

all OK
