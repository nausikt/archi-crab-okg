# dmwm/CRABServer issue #8222: #703: Test prod CRABClient using preprod REST instance and CMSSW_8_0_36 CMSSW release

State: closed
Opened: 2024-02-02T11:45:16Z
Closed: 2024-02-02T14:47:45Z
URL: https://github.com/dmwm/CRABServer/issues/8222

## Opening post (cmsdmwmbot, 2024-02-02T11:45:16Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_8_0_36**
- SCRAM_ARCH: **slc7_amd64_gcc530**

**Tests started:**

- [x] Client_Configuration_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-02-02 12:45:15
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/703/)

## Comment (cmsdmwmbot, 2024-02-02T11:48:20Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240202_114658:cmsbot_crab_20240202_124656
240202_114700:cmsbot_crab_20240202_124658
240202_114702:cmsbot_crab_20240202_124700
240202_114704:cmsbot_crab_20240202_124702
240202_114706:cmsbot_crab_20240202_124705
240202_114738:cmsbot_crab_20240202_124707
240202_114742:cmsbot_crab_rucio_transfers_20240202_124740
240202_114745:cmsbot_crab_rucio_transfers_group_20240202_124743
240202_114749:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124745
240202_114752:cmsbot_crab_rucio_transfers_nopublication_20240202_124749
240202_114756:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124752
240202_114759:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124756
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_114546:cmsbot_crab_transferOutputs
240202_114548:cmsbot_crab_transferLogs
240202_114550:cmsbot_crab_activity
240202_114554:cmsbot_crab_inputFiles
240202_114556:cmsbot_crab_disableAutomaticOutputCollection
240202_114559:cmsbot_crab_outputFiles
240202_114601:cmsbot_crab_allowUndistributedCMSSW
240202_114603:cmsbot_crab_maxMemoryMB
240202_114605:cmsbot_crab_maxJobRuntimeMin
240202_114608:cmsbot_crab_numCores
240202_114610:cmsbot_crab_scriptExe
240202_114613:cmsbot_crab_scriptArgs
240202_114616:cmsbot_crab_sendVenvFolder
240202_114623:cmsbot_crab_sendExternalFolder
240202_114624:cmsbot_crab_inputDBS
240202_114626:cmsbot_crab_useParent
240202_114628:cmsbot_crab_secondaryInputDataset
240202_114630:cmsbot_crab_lumiMaskFile
240202_114631:cmsbot_crab_lumiMaskUrl
240202_114634:cmsbot_crab_outLFNDirBase
240202_114636:cmsbot_crab_runRange
240202_114637:cmsbot_crab_ignoreLocality
240202_114638:cmsbot_crab_userInputFiles
240202_114640:cmsbot_crab_whitelist
240202_114642:cmsbot_crab_blacklist
240202_114644:cmsbot_crab_ignoreGlobalBlacklist
240202_114647:cmsbot_crab_voRole
240202_114649:cmsbot_crab_voGroup
240202_114651:cmsbot_crab_scheddName
240202_114653:cmsbot_crab_collector
240202_114655:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 12:47:59
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/703/console)

## Comment (cmsdmwmbot, 2024-02-02T12:09:16Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 13:09:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/741/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 10, 'running': 149, 'transferring': 833, 'cooloff': 8}, 'TN': '240202_114658:cmsbot_crab_20240202_124656', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 5}, 'TN': '240202_114700:cmsbot_crab_20240202_124658', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240202_114702:cmsbot_crab_20240202_124700', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'transferring': 8}, 'TN': '240202_114704:cmsbot_crab_20240202_124702', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 2, 'running': 10, 'transferring': 87, 'unsubmitted': 1}, 'TN': '240202_114706:cmsbot_crab_20240202_124705', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 2, 'transferring': 8}, 'TN': '240202_114738:cmsbot_crab_20240202_124707', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 39}, 'TN': '240202_114742:cmsbot_crab_rucio_transfers_20240202_124740', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 5, 'transferring': 35}, 'TN': '240202_114745:cmsbot_crab_rucio_transfers_group_20240202_124743', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 39}, 'TN': '240202_114749:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124745', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_114752:cmsbot_crab_rucio_transfers_nopublication_20240202_124749', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_114756:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124752', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'running': 2, 'transferring': 37}, 'TN': '240202_114759:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124756', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T12:11:44Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 13:11:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/930/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240202_114631:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240202_114636:cmsbot_crab_runRange - 2
whitelist-check.sh 240202_114640:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_114642:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240202_114644:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240202_114647:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114546:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_114548:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_114550:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_114554:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114556:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_114559:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_114601:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_114603:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_114605:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_114608:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_114610:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_114613:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_114616:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114623:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114624:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_114626:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_114628:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114630:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240202_114634:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240202_114637:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_114638:cmsbot_crab_userInputFiles - 0
voGroup-check.sh 240202_114649:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_114651:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114653:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_114655:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T12:25:35Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-02-02 13:25:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/743/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 239, 'transferring': 761}, 'TN': '240202_114658:cmsbot_crab_20240202_124656', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 0, 'finished': 2, 'idle': 1}, 'TN': '240202_114700:cmsbot_crab_20240202_124658', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240202_114702:cmsbot_crab_20240202_124700', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240202_114704:cmsbot_crab_20240202_124702', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '240202_114706:cmsbot_crab_20240202_124705', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240202_114738:cmsbot_crab_20240202_124707', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_114742:cmsbot_crab_rucio_transfers_20240202_124740', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_114745:cmsbot_crab_rucio_transfers_group_20240202_124743', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_114749:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124745', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_114752:cmsbot_crab_rucio_transfers_nopublication_20240202_124749', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240202_114756:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124752', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 19, 'finished': 20}, 'TN': '240202_114759:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124756', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T12:36:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-02-02 13:36:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/935/console

```
RETRY TESTS:
ignoreGlobalBlacklist-check.sh 240202_114644:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114546:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_114548:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_114550:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_114554:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114556:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_114559:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_114601:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_114603:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_114605:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_114608:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_114610:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_114613:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_114616:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114623:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114624:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_114626:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_114628:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114630:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_114631:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_114634:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_114636:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_114637:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_114638:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_114640:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_114642:cmsbot_crab_blacklist - 0
voRole-check.sh 240202_114647:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_114649:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_114651:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114653:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_114655:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T12:57:59Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-02-02 13:57:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/937/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114546:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_114548:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_114550:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_114554:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114556:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_114559:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_114601:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_114603:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_114605:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_114608:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_114610:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_114613:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_114616:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114623:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114624:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_114626:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_114628:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114630:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_114631:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_114634:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_114636:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_114637:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_114638:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_114640:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_114642:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_114644:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_114647:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_114649:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_114651:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114653:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_114655:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T13:13:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-02-02 14:13:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/745/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 806, 'transferring': 194}, 'TN': '240202_114658:cmsbot_crab_20240202_124656', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/800/800'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 0, 'finished': 2, 'transferring': 1}, 'TN': '240202_114700:cmsbot_crab_20240202_124658', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240202_114702:cmsbot_crab_20240202_124700', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_114704:cmsbot_crab_20240202_124702', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/7/7'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240202_114706:cmsbot_crab_20240202_124705', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/66/66'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_114738:cmsbot_crab_20240202_124707', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114742:cmsbot_crab_rucio_transfers_20240202_124740', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114745:cmsbot_crab_rucio_transfers_group_20240202_124743', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '1/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114749:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124745', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114752:cmsbot_crab_rucio_transfers_nopublication_20240202_124749', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114756:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124752', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '1/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 32, 'transferring': 8}, 'TN': '240202_114759:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124756', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-02-02T14:44:34Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-02-02 15:44:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/747/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240202_114658:cmsbot_crab_20240202_124656', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'failed': 0, 'finished': 3}, 'TN': '240202_114700:cmsbot_crab_20240202_124658', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240202_114702:cmsbot_crab_20240202_124700', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_114704:cmsbot_crab_20240202_124702', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240202_114706:cmsbot_crab_20240202_124705', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240202_114738:cmsbot_crab_20240202_124707', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114742:cmsbot_crab_rucio_transfers_20240202_124740', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114745:cmsbot_crab_rucio_transfers_group_20240202_124743', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '1/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114749:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240202_124745', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114752:cmsbot_crab_rucio_transfers_nopublication_20240202_124749', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114756:cmsbot_crab_rucio_transfers_withnoneedm_20240202_124752', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '1/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240202_114759:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240202_124756', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-02-02T14:47:45Z)

all OK
