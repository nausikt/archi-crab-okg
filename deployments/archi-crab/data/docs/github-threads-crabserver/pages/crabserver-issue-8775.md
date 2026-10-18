# dmwm/CRABServer issue #8775: #873: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-07T17:24:50Z
Closed: 2024-11-08T08:22:30Z
URL: https://github.com/dmwm/CRABServer/issues/8775

## Opening post (cmsdmwmbot, 2024-11-07T17:24:50Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2024-11-07 18:24:49
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/873/)

## Comment (cmsdmwmbot, 2024-11-07T17:26:24Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
241107_172511:cmsbot_crab_20241107_182510
241107_172514:cmsbot_crab_20241107_182513
241107_172516:cmsbot_crab_20241107_182516
241107_172519:cmsbot_crab_20241107_182518
241107_172521:cmsbot_crab_20241107_182521
241107_172544:cmsbot_crab_20241107_182523
241107_172547:cmsbot_crab_rucio_transfers_20241107_182546
241107_172549:cmsbot_crab_rucio_transfers_group_20241107_182549
241107_172553:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241107_182551
241107_172555:cmsbot_crab_rucio_transfers_nopublication_20241107_182554
241107_172559:cmsbot_crab_rucio_transfers_withnoneedm_20241107_182557
241107_172602:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241107_182601
```

Finished at: 2024-11-07 18:26:02
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/873/console)

## Comment (cmsdmwmbot, 2024-11-07T17:47:35Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-07 18:47:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1112/console

```
{'TN': '241107_172511:cmsbot_crab_20241107_182510', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 993, 'cooloff': 1, 'running': 3, 'idle': 2, 'unsubmitted': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172514:cmsbot_crab_20241107_182513', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172516:cmsbot_crab_20241107_182516', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172519:cmsbot_crab_20241107_182518', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172521:cmsbot_crab_20241107_182521', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172544:cmsbot_crab_20241107_182523', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172547:cmsbot_crab_rucio_transfers_20241107_182546', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172549:cmsbot_crab_rucio_transfers_group_20241107_182549', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172553:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241107_182551', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'cooloff': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172555:cmsbot_crab_rucio_transfers_nopublication_20241107_182554', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172559:cmsbot_crab_rucio_transfers_withnoneedm_20241107_182557', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172602:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241107_182601', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-11-07T18:04:37Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-11-07 19:04:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1113/console

```
{'TN': '241107_172511:cmsbot_crab_20241107_182510', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 331, 'finished': 668, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172514:cmsbot_crab_20241107_182513', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172516:cmsbot_crab_20241107_182516', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172519:cmsbot_crab_20241107_182518', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 3, 'finished': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172521:cmsbot_crab_20241107_182521', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172544:cmsbot_crab_20241107_182523', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172547:cmsbot_crab_rucio_transfers_20241107_182546', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172549:cmsbot_crab_rucio_transfers_group_20241107_182549', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172553:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241107_182551', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172555:cmsbot_crab_rucio_transfers_nopublication_20241107_182554', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172559:cmsbot_crab_rucio_transfers_withnoneedm_20241107_182557', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172602:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241107_182601', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-11-07T18:51:40Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-11-07 19:51:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1114/console

```
{'TN': '241107_172511:cmsbot_crab_20241107_182510', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'failed': 1, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/995/995'}
{'TN': '241107_172514:cmsbot_crab_20241107_182513', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241107_172516:cmsbot_crab_20241107_182516', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241107_172519:cmsbot_crab_20241107_182518', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241107_172521:cmsbot_crab_20241107_182521', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241107_172544:cmsbot_crab_20241107_182523', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241107_172547:cmsbot_crab_rucio_transfers_20241107_182546', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '241107_172549:cmsbot_crab_rucio_transfers_group_20241107_182549', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 29, 'transferring': 11}, 'publication (fail/tdb/DBS)': '0/29/29'}
{'TN': '241107_172553:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241107_182551', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172555:cmsbot_crab_rucio_transfers_nopublication_20241107_182554', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172559:cmsbot_crab_rucio_transfers_withnoneedm_20241107_182557', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '241107_172602:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241107_182601', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-11-07T20:23:36Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-11-07 21:23:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1115/console

```
{'TN': '241107_172511:cmsbot_crab_20241107_182510', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241107_172514:cmsbot_crab_20241107_182513', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241107_172516:cmsbot_crab_20241107_182516', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241107_172519:cmsbot_crab_20241107_182518', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241107_172521:cmsbot_crab_20241107_182521', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241107_172544:cmsbot_crab_20241107_182523', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241107_172547:cmsbot_crab_rucio_transfers_20241107_182546', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241107_172549:cmsbot_crab_rucio_transfers_group_20241107_182549', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '241107_172553:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241107_182551', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172555:cmsbot_crab_rucio_transfers_nopublication_20241107_182554', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172559:cmsbot_crab_rucio_transfers_withnoneedm_20241107_182557', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241107_172602:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241107_182601', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-11-07T22:25:35Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 4 out of 5. Test is done.
**Finished at:** 2024-11-07 23:25:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1116/console

```
{'TN': '241107_172511:cmsbot_crab_20241107_182510', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '241107_172514:cmsbot_crab_20241107_182513', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241107_172516:cmsbot_crab_20241107_182516', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '241107_172519:cmsbot_crab_20241107_182518', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241107_172521:cmsbot_crab_20241107_182521', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '241107_172544:cmsbot_crab_20241107_182523', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '241107_172547:cmsbot_crab_rucio_transfers_20241107_182546', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241107_172549:cmsbot_crab_rucio_transfers_group_20241107_182549', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241107_172553:cmsbot_crab_rucio_transfers_manyedm_nopublication_20241107_182551', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172555:cmsbot_crab_rucio_transfers_nopublication_20241107_182554', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '241107_172559:cmsbot_crab_rucio_transfers_withnoneedm_20241107_182557', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '241107_172602:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20241107_182601', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-11-08T08:22:30Z)

OK
