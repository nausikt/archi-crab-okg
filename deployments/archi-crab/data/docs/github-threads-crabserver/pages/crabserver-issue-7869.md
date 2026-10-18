# dmwm/CRABServer issue #7869: #471: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-09-12T11:23:52Z
Closed: 2023-09-13T08:12:32Z
URL: https://github.com/dmwm/CRABServer/issues/7869

## Opening post (cmsdmwmbot, 2023-09-12T11:23:52Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-09-12 13:23:50
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/471/)

## Comment (cmsdmwmbot, 2023-09-12T11:28:02Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230912_112715:cmsbot_crab_20230912_132715
230912_112716:cmsbot_crab_20230912_132716
230912_112718:cmsbot_crab_20230912_132717
230912_112719:cmsbot_crab_20230912_132718
230912_112721:cmsbot_crab_20230912_132720
230912_112741:cmsbot_crab_20230912_132721
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230912_112552:cmsbot_crab_transferOutputs
230912_112554:cmsbot_crab_transferLogs
230912_112555:cmsbot_crab_activity
230912_112557:cmsbot_crab_inputFiles
230912_112558:cmsbot_crab_disableAutomaticOutputCollection
230912_112600:cmsbot_crab_outputFiles
230912_112601:cmsbot_crab_allowUndistributedCMSSW
230912_112602:cmsbot_crab_maxMemoryMB
230912_112603:cmsbot_crab_maxJobRuntimeMin
230912_112604:cmsbot_crab_numCores
230912_112605:cmsbot_crab_scriptExe
230912_112606:cmsbot_crab_scriptArgs
230912_112607:cmsbot_crab_sendPythonFolder
230912_112651:cmsbot_crab_sendExternalFolder
230912_112652:cmsbot_crab_inputDBS
230912_112653:cmsbot_crab_useParent
230912_112654:cmsbot_crab_secondaryInputDataset
230912_112656:cmsbot_crab_lumiMaskFile
230912_112658:cmsbot_crab_lumiMaskUrl
230912_112700:cmsbot_crab_outLFNDirBase
230912_112701:cmsbot_crab_runRange
230912_112703:cmsbot_crab_ignoreLocality
230912_112704:cmsbot_crab_userInputFiles
230912_112705:cmsbot_crab_whitelist
230912_112706:cmsbot_crab_blacklist
230912_112707:cmsbot_crab_ignoreGlobalBlacklist
230912_112709:cmsbot_crab_voRole
230912_112710:cmsbot_crab_voGroup
230912_112711:cmsbot_crab_scheddName
230912_112712:cmsbot_crab_collector
230912_112714:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230912_112550:cmsbot_crab_20230912_132548
```

Finished at: 2023-09-12 13:27:41
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/471/console)

## Comment (cmsdmwmbot, 2023-09-12T11:50:47Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-09-12 13:50:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/372/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/372//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-09-12T11:51:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-09-12 13:51:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/631/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112715:cmsbot_crab_20230912_132715', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112716:cmsbot_crab_20230912_132716', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112718:cmsbot_crab_20230912_132717', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112719:cmsbot_crab_20230912_132718', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112721:cmsbot_crab_20230912_132720', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112741:cmsbot_crab_20230912_132721', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2023-09-12T11:51:30Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-09-12 13:51:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/781/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230912_112552:cmsbot_crab_transferOutputs - 0

FAILED TESTS:
transferLogs-check.sh 230912_112554:cmsbot_crab_transferLogs - 1
activity-check.sh 230912_112555:cmsbot_crab_activity - 1
inputFiles-check.sh 230912_112557:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 230912_112558:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230912_112600:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 230912_112601:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 230912_112602:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230912_112603:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230912_112604:cmsbot_crab_numCores - 1
scriptExe-check.sh 230912_112605:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230912_112606:cmsbot_crab_scriptArgs - 1
sendPythonFolder-check.sh 230912_112607:cmsbot_crab_sendPythonFolder - 1
sendExternalFolder-check.sh 230912_112651:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 230912_112652:cmsbot_crab_inputDBS - 1
useParent-check.sh 230912_112653:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230912_112654:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230912_112656:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230912_112658:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230912_112700:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230912_112701:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230912_112703:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230912_112704:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230912_112705:cmsbot_crab_whitelist - 1
blacklist-check.sh 230912_112706:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230912_112707:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230912_112709:cmsbot_crab_voRole - 1
voGroup-check.sh 230912_112710:cmsbot_crab_voGroup - 1
scheddName-check.sh 230912_112711:cmsbot_crab_scheddName - 1
collector-check.sh 230912_112712:cmsbot_crab_collector - 1
extraJDL-check.sh 230912_112714:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-09-12T12:09:24Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2023-09-12 14:09:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/632/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112715:cmsbot_crab_20230912_132715', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112716:cmsbot_crab_20230912_132716', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112718:cmsbot_crab_20230912_132717', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112719:cmsbot_crab_20230912_132718', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112721:cmsbot_crab_20230912_132720', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112741:cmsbot_crab_20230912_132721', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2023-09-12T12:57:48Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2023-09-12 14:57:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/633/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112715:cmsbot_crab_20230912_132715', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112716:cmsbot_crab_20230912_132716', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112718:cmsbot_crab_20230912_132717', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112719:cmsbot_crab_20230912_132718', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112721:cmsbot_crab_20230912_132720', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112741:cmsbot_crab_20230912_132721', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2023-09-12T14:31:28Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2023-09-12 16:31:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/634/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112715:cmsbot_crab_20230912_132715', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112716:cmsbot_crab_20230912_132716', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112718:cmsbot_crab_20230912_132717', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112719:cmsbot_crab_20230912_132718', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112721:cmsbot_crab_20230912_132720', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112741:cmsbot_crab_20230912_132721', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2023-09-12T16:33:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2023-09-12 18:33:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/637/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112715:cmsbot_crab_20230912_132715', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112716:cmsbot_crab_20230912_132716', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112718:cmsbot_crab_20230912_132717', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112719:cmsbot_crab_20230912_132718', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112721:cmsbot_crab_20230912_132720', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112741:cmsbot_crab_20230912_132721', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2023-09-12T18:37:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-09-12 20:37:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/640/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112715:cmsbot_crab_20230912_132715', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112716:cmsbot_crab_20230912_132716', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112718:cmsbot_crab_20230912_132717', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112719:cmsbot_crab_20230912_132718', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112721:cmsbot_crab_20230912_132720', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '230912_112741:cmsbot_crab_20230912_132721', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (novicecpp, 2023-09-13T08:12:32Z)

Ignore it due to error in EOS.
