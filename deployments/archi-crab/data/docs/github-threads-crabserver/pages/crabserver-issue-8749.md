# dmwm/CRABServer issue #8749: #855: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-10-24T11:14:08Z
Closed: 2024-10-29T20:20:40Z
URL: https://github.com/dmwm/CRABServer/issues/8749

## Opening post (cmsdmwmbot, 2024-10-24T11:14:08Z)

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

Started at: 2024-10-24 12:54:05
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/855/)

## Comment (cmsdmwmbot, 2024-10-24T11:17:00Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
241024_111606:cmsbot_crab_20241024_131605
241024_111608:cmsbot_crab_20241024_131608
241024_111611:cmsbot_crab_20241024_131610
241024_111613:cmsbot_crab_20241024_131613
241024_111616:cmsbot_crab_20241024_131615
241024_111620:cmsbot_crab_20241024_131618
241024_111623:cmsbot_crab_rucio_transfers_20241024_131622
241024_111625:cmsbot_crab_rucio_transfers_group_20241024_131625
241024_111629:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131628
241024_111632:cmsbot_crab_rucio_transfers_nopublication_20241024_131631
241024_111635:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131634
241024_111639:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131637
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
241024_111436:cmsbot_crab_transferOutputs
241024_111439:cmsbot_crab_transferLogs
241024_111441:cmsbot_crab_activity
241024_111444:cmsbot_crab_inputFiles
241024_111447:cmsbot_crab_disableAutomaticOutputCollection
241024_111449:cmsbot_crab_outputFiles
241024_111452:cmsbot_crab_allowUndistributedCMSSW
241024_111455:cmsbot_crab_maxMemoryMB
241024_111458:cmsbot_crab_maxJobRuntimeMin
241024_111500:cmsbot_crab_numCores
241024_111503:cmsbot_crab_scriptExe
241024_111505:cmsbot_crab_scriptArgs
241024_111508:cmsbot_crab_sendVenvFolder
241024_111511:cmsbot_crab_sendExternalFolder
241024_111513:cmsbot_crab_inputDBS
241024_111516:cmsbot_crab_useParent
241024_111526:cmsbot_crab_secondaryInputDataset
241024_111529:cmsbot_crab_lumiMaskFile
241024_111532:cmsbot_crab_lumiMaskUrl
241024_111535:cmsbot_crab_outLFNDirBase
241024_111537:cmsbot_crab_runRange
241024_111540:cmsbot_crab_ignoreLocality
241024_111542:cmsbot_crab_userInputFiles
241024_111545:cmsbot_crab_whitelist
241024_111547:cmsbot_crab_blacklist
241024_111550:cmsbot_crab_ignoreGlobalBlacklist
241024_111552:cmsbot_crab_voRole
241024_111555:cmsbot_crab_voGroup
241024_111557:cmsbot_crab_scheddName
241024_111600:cmsbot_crab_collector
241024_111603:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241024_111433:cmsbot_crab_20241024_131432
```

Finished at: 2024-10-24 13:16:39
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/855/console)

## Comment (cmsdmwmbot, 2024-10-24T12:14:16Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-10-24 13:37:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1102/console

```
{'TN': '241024_111606:cmsbot_crab_20241024_131605', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111608:cmsbot_crab_20241024_131608', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111611:cmsbot_crab_20241024_131610', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111613:cmsbot_crab_20241024_131613', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111616:cmsbot_crab_20241024_131615', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111620:cmsbot_crab_20241024_131618', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111623:cmsbot_crab_rucio_transfers_20241024_131622', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111625:cmsbot_crab_rucio_transfers_group_20241024_131625', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111629:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131628', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111632:cmsbot_crab_rucio_transfers_nopublication_20241024_131631', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111635:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131634', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111639:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131637', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-10-24T12:14:16Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-10-24 13:40:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/551/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/551//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241024_131432  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Command recover failed


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241024_111433:cmsbot_crab_20241024_131432  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241024_131432/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
step kill - task already killed
Command recover failed
```

## Comment (cmsdmwmbot, 2024-10-24T12:18:41Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 0 out of 4. Test is done.
**Finished at:** 2024-10-24 14:18:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1208/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241024_111436:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241024_111439:cmsbot_crab_transferLogs - 0
activity-check.sh 241024_111441:cmsbot_crab_activity - 0
inputFiles-check.sh 241024_111444:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241024_111447:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241024_111449:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241024_111452:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241024_111455:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241024_111458:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241024_111500:cmsbot_crab_numCores - 0
scriptExe-check.sh 241024_111503:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241024_111505:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241024_111508:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241024_111511:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241024_111513:cmsbot_crab_inputDBS - 0
useParent-check.sh 241024_111516:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241024_111526:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241024_111529:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241024_111532:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241024_111535:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241024_111537:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241024_111540:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241024_111542:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241024_111545:cmsbot_crab_whitelist - 0
blacklist-check.sh 241024_111547:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241024_111550:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241024_111552:cmsbot_crab_voRole - 0
voGroup-check.sh 241024_111555:cmsbot_crab_voGroup - 0
scheddName-check.sh 241024_111557:cmsbot_crab_scheddName - 0
collector-check.sh 241024_111600:cmsbot_crab_collector - 0
extraJDL-check.sh 241024_111603:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-10-24T12:30:12Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 5. Test is done.
**Finished at:** 2024-10-24 14:30:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1105/console

```
{'TN': '241024_111606:cmsbot_crab_20241024_131605', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/0'}
{'TN': '241024_111608:cmsbot_crab_20241024_131608', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111611:cmsbot_crab_20241024_131610', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/0'}
{'TN': '241024_111613:cmsbot_crab_20241024_131613', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/0'}
{'TN': '241024_111616:cmsbot_crab_20241024_131615', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/0'}
{'TN': '241024_111620:cmsbot_crab_20241024_131618', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/0'}
{'TN': '241024_111623:cmsbot_crab_rucio_transfers_20241024_131622', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/0'}
{'TN': '241024_111625:cmsbot_crab_rucio_transfers_group_20241024_131625', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/0'}
{'TN': '241024_111629:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241024_131628', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111632:cmsbot_crab_rucio_transfers_nopublication_20241024_131631', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241024_111635:cmsbot_crab_rucio_transfers_withnoneedm_20241024_131634', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/0'}
{'TN': '241024_111639:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241024_131637', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
