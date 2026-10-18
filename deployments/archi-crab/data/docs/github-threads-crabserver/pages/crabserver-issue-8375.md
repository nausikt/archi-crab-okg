# dmwm/CRABServer issue #8375: #768: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-03T08:46:35Z
Closed: 2024-05-06T22:34:13Z
URL: https://github.com/dmwm/CRABServer/issues/8375

## Opening post (cmsdmwmbot, 2024-05-03T08:46:35Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2024-05-03 10:46:34
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/768/)

## Comment (cmsdmwmbot, 2024-05-03T08:47:45Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240503_084654:cmsbot_crab_20240503_104653
240503_084656:cmsbot_crab_20240503_104656
240503_084658:cmsbot_crab_20240503_104658
240503_084700:cmsbot_crab_20240503_104700
240503_084702:cmsbot_crab_20240503_104702
240503_084706:cmsbot_crab_20240503_104704
240503_084709:cmsbot_crab_rucio_transfers_20240503_104707
240503_084711:cmsbot_crab_rucio_transfers_group_20240503_104710
240503_084714:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240503_104713
240503_084718:cmsbot_crab_rucio_transfers_nopublication_20240503_104716
240503_084721:cmsbot_crab_rucio_transfers_withnoneedm_20240503_104719
240503_084724:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240503_104722
```

Finished at: 2024-05-03 10:47:24
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/768/console)

## Comment (cmsdmwmbot, 2024-05-03T09:08:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-03 11:08:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/887/console

```
{'TN': '240503_084654:cmsbot_crab_20240503_104653', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 989, 'finished': 1, 'running': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084656:cmsbot_crab_20240503_104656', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 1, 'finished': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084658:cmsbot_crab_20240503_104658', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084700:cmsbot_crab_20240503_104700', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084702:cmsbot_crab_20240503_104702', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084706:cmsbot_crab_20240503_104704', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 2, 'running': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084709:cmsbot_crab_rucio_transfers_20240503_104707', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084711:cmsbot_crab_rucio_transfers_group_20240503_104710', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084714:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240503_104713', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084718:cmsbot_crab_rucio_transfers_nopublication_20240503_104716', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084721:cmsbot_crab_rucio_transfers_withnoneedm_20240503_104719', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084724:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240503_104722', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-03T09:26:29Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-05-03 11:26:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/888/console

```
{'TN': '240503_084654:cmsbot_crab_20240503_104653', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 105, 'finished': 889, 'running': 6}, 'publication (fail/tdb/DBS)': '0/400/400'}
{'TN': '240503_084656:cmsbot_crab_20240503_104656', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084658:cmsbot_crab_20240503_104658', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240503_084700:cmsbot_crab_20240503_104700', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240503_084702:cmsbot_crab_20240503_104702', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 71, 'finished': 29}, 'publication (fail/tdb/DBS)': '0/8/8'}
{'TN': '240503_084706:cmsbot_crab_20240503_104704', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084709:cmsbot_crab_rucio_transfers_20240503_104707', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 31, 'finished': 9}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084711:cmsbot_crab_rucio_transfers_group_20240503_104710', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 19, 'finished': 21}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084714:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240503_104713', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 14, 'transferring': 26}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084718:cmsbot_crab_rucio_transfers_nopublication_20240503_104716', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 23, 'finished': 17}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084721:cmsbot_crab_rucio_transfers_withnoneedm_20240503_104719', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 24, 'transferring': 16}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084724:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240503_104722', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 23, 'finished': 17}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-03T10:13:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-05-03 12:13:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/890/console

```
{'TN': '240503_084654:cmsbot_crab_20240503_104653', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 993, 'failed': 5, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240503_084656:cmsbot_crab_20240503_104656', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084658:cmsbot_crab_20240503_104658', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240503_084700:cmsbot_crab_20240503_104700', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240503_084702:cmsbot_crab_20240503_104702', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240503_084706:cmsbot_crab_20240503_104704', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240503_084709:cmsbot_crab_rucio_transfers_20240503_104707', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084711:cmsbot_crab_rucio_transfers_group_20240503_104710', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084714:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240503_104713', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084718:cmsbot_crab_rucio_transfers_nopublication_20240503_104716', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084721:cmsbot_crab_rucio_transfers_withnoneedm_20240503_104719', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084724:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240503_104722', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-03T11:45:28Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-05-03 13:45:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/893/console

```
{'TN': '240503_084654:cmsbot_crab_20240503_104653', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240503_084656:cmsbot_crab_20240503_104656', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240503_084658:cmsbot_crab_20240503_104658', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240503_084700:cmsbot_crab_20240503_104700', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240503_084702:cmsbot_crab_20240503_104702', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240503_084706:cmsbot_crab_20240503_104704', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240503_084709:cmsbot_crab_rucio_transfers_20240503_104707', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240503_084711:cmsbot_crab_rucio_transfers_group_20240503_104710', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240503_084714:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240503_104713', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084718:cmsbot_crab_rucio_transfers_nopublication_20240503_104716', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240503_084721:cmsbot_crab_rucio_transfers_withnoneedm_20240503_104719', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240503_084724:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240503_104722', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
