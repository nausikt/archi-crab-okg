# dmwm/CRABServer issue #8094: #617: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-12-11T21:36:17Z
Closed: 2023-12-19T21:16:13Z
URL: https://github.com/dmwm/CRABServer/issues/8094

## Opening post (cmsdmwmbot, 2023-12-11T21:36:17Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-12-11 22:36:17
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/617/)

## Comment (cmsdmwmbot, 2023-12-11T21:37:55Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
231211_213645:cmsbot_crab_20231211_223643
231211_213647:cmsbot_crab_20231211_223646
231211_213649:cmsbot_crab_20231211_223648
231211_213651:cmsbot_crab_20231211_223650
231211_213653:cmsbot_crab_20231211_223652
231211_213715:cmsbot_crab_20231211_223654
231211_213718:cmsbot_crab_rucio_transfers_20231211_223717
231211_213720:cmsbot_crab_rucio_transfers_group_20231211_223720
231211_213724:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231211_223722
231211_213727:cmsbot_crab_rucio_transfers_nopublication_20231211_223725
231211_213730:cmsbot_crab_rucio_transfers_withnoneedm_20231211_223728
231211_213733:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231211_223732
```

Finished at: 2023-12-11 22:37:34
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/617/console)

## Comment (cmsdmwmbot, 2023-12-11T22:00:32Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-11 23:00:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/683/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '231211_213645:cmsbot_crab_20231211_223643', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '231211_213647:cmsbot_crab_20231211_223646', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '231211_213649:cmsbot_crab_20231211_223648', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231211_213651:cmsbot_crab_20231211_223650', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '231211_213653:cmsbot_crab_20231211_223652', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231211_213715:cmsbot_crab_20231211_223654', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231211_213718:cmsbot_crab_rucio_transfers_20231211_223717', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231211_213720:cmsbot_crab_rucio_transfers_group_20231211_223720', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231211_213724:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231211_223722', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231211_213727:cmsbot_crab_rucio_transfers_nopublication_20231211_223725', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231211_213730:cmsbot_crab_rucio_transfers_withnoneedm_20231211_223728', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231211_213733:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231211_223732', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-12-11T22:18:06Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2023-12-11 23:18:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/684/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 916, 'transferring': 84}, 'TN': '231211_213645:cmsbot_crab_20231211_223643', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '231211_213647:cmsbot_crab_20231211_223646', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1}, 'TN': '231211_213649:cmsbot_crab_20231211_223648', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 10}, 'TN': '231211_213651:cmsbot_crab_20231211_223650', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 100}, 'TN': '231211_213653:cmsbot_crab_20231211_223652', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231211_213715:cmsbot_crab_20231211_223654', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213718:cmsbot_crab_rucio_transfers_20231211_223717', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231211_213720:cmsbot_crab_rucio_transfers_group_20231211_223720', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213724:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231211_223722', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213727:cmsbot_crab_rucio_transfers_nopublication_20231211_223725', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213730:cmsbot_crab_rucio_transfers_withnoneedm_20231211_223728', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213733:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231211_223732', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-12-11T23:06:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2023-12-12 00:06:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/685/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '231211_213645:cmsbot_crab_20231211_223643', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '231211_213647:cmsbot_crab_20231211_223646', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '231211_213649:cmsbot_crab_20231211_223648', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231211_213651:cmsbot_crab_20231211_223650', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231211_213653:cmsbot_crab_20231211_223652', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231211_213715:cmsbot_crab_20231211_223654', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213718:cmsbot_crab_rucio_transfers_20231211_223717', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231211_213720:cmsbot_crab_rucio_transfers_group_20231211_223720', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213724:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231211_223722', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213727:cmsbot_crab_rucio_transfers_nopublication_20231211_223725', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213730:cmsbot_crab_rucio_transfers_withnoneedm_20231211_223728', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213733:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231211_223732', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-12-12T00:40:06Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2023-12-12 01:40:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/686/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '231211_213645:cmsbot_crab_20231211_223643', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '231211_213647:cmsbot_crab_20231211_223646', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '231211_213649:cmsbot_crab_20231211_223648', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231211_213651:cmsbot_crab_20231211_223650', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231211_213653:cmsbot_crab_20231211_223652', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231211_213715:cmsbot_crab_20231211_223654', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213718:cmsbot_crab_rucio_transfers_20231211_223717', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231211_213720:cmsbot_crab_rucio_transfers_group_20231211_223720', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213724:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231211_223722', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213727:cmsbot_crab_rucio_transfers_nopublication_20231211_223725', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213730:cmsbot_crab_rucio_transfers_withnoneedm_20231211_223728', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213733:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231211_223732', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-12-12T02:45:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2023-12-12 03:45:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/687/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '231211_213645:cmsbot_crab_20231211_223643', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '231211_213647:cmsbot_crab_20231211_223646', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '231211_213649:cmsbot_crab_20231211_223648', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231211_213651:cmsbot_crab_20231211_223650', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231211_213653:cmsbot_crab_20231211_223652', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231211_213715:cmsbot_crab_20231211_223654', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213718:cmsbot_crab_rucio_transfers_20231211_223717', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213720:cmsbot_crab_rucio_transfers_group_20231211_223720', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213724:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231211_223722', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213727:cmsbot_crab_rucio_transfers_nopublication_20231211_223725', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213730:cmsbot_crab_rucio_transfers_withnoneedm_20231211_223728', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213733:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231211_223732', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-12-12T04:49:13Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-12-12 05:49:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/688/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '231211_213645:cmsbot_crab_20231211_223643', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '231211_213647:cmsbot_crab_20231211_223646', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '231211_213649:cmsbot_crab_20231211_223648', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231211_213651:cmsbot_crab_20231211_223650', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231211_213653:cmsbot_crab_20231211_223652', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231211_213715:cmsbot_crab_20231211_223654', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213718:cmsbot_crab_rucio_transfers_20231211_223717', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213720:cmsbot_crab_rucio_transfers_group_20231211_223720', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213724:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231211_223722', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213727:cmsbot_crab_rucio_transfers_nopublication_20231211_223725', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213730:cmsbot_crab_rucio_transfers_withnoneedm_20231211_223728', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 40}, 'TN': '231211_213733:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231211_223732', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```
