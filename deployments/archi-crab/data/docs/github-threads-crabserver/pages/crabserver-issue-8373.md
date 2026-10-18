# dmwm/CRABServer issue #8373: #766: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-02T17:54:32Z
Closed: 2024-05-06T22:34:12Z
URL: https://github.com/dmwm/CRABServer/issues/8373

## Opening post (cmsdmwmbot, 2024-05-02T17:54:32Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2024-05-02 19:54:31
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/766/)

## Comment (cmsdmwmbot, 2024-05-02T17:55:53Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240502_175448:cmsbot_crab_20240502_195447
240502_175450:cmsbot_crab_20240502_195450
240502_175452:cmsbot_crab_20240502_195452
240502_175455:cmsbot_crab_20240502_195454
240502_175457:cmsbot_crab_20240502_195456
240502_175514:cmsbot_crab_20240502_195458
240502_175517:cmsbot_crab_rucio_transfers_20240502_195516
240502_175519:cmsbot_crab_rucio_transfers_group_20240502_195519
240502_175523:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_195521
240502_175526:cmsbot_crab_rucio_transfers_nopublication_20240502_195524
240502_175529:cmsbot_crab_rucio_transfers_withnoneedm_20240502_195528
240502_175532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_195531
```

Finished at: 2024-05-02 19:55:32
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/766/console)

## Comment (cmsdmwmbot, 2024-05-02T18:18:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-02 20:18:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/881/console

```
{'TN': '240502_175448:cmsbot_crab_20240502_195447', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 999, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175450:cmsbot_crab_20240502_195450', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175452:cmsbot_crab_20240502_195452', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175455:cmsbot_crab_20240502_195454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175457:cmsbot_crab_20240502_195456', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175514:cmsbot_crab_20240502_195458', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175517:cmsbot_crab_rucio_transfers_20240502_195516', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175519:cmsbot_crab_rucio_transfers_group_20240502_195519', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175523:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_195521', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175526:cmsbot_crab_rucio_transfers_nopublication_20240502_195524', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175529:cmsbot_crab_rucio_transfers_withnoneedm_20240502_195528', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_195531', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-02T18:35:35Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-05-02 20:35:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/882/console

```
{'TN': '240502_175448:cmsbot_crab_20240502_195447', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 729, 'transferring': 252, 'idle': 1, 'cooloff': 18}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175450:cmsbot_crab_20240502_195450', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175452:cmsbot_crab_20240502_195452', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175455:cmsbot_crab_20240502_195454', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175457:cmsbot_crab_20240502_195456', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175514:cmsbot_crab_20240502_195458', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175517:cmsbot_crab_rucio_transfers_20240502_195516', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/19/19'}
{'TN': '240502_175519:cmsbot_crab_rucio_transfers_group_20240502_195519', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/28/28'}
{'TN': '240502_175523:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_195521', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175526:cmsbot_crab_rucio_transfers_nopublication_20240502_195524', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175529:cmsbot_crab_rucio_transfers_withnoneedm_20240502_195528', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '240502_175532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_195531', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-02T19:22:28Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-05-02 21:22:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/883/console

```
{'TN': '240502_175448:cmsbot_crab_20240502_195447', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 994, 'running': 1, 'transferring': 5}, 'publication (fail/tdb/DBS)': '0/994/994'}
{'TN': '240502_175450:cmsbot_crab_20240502_195450', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175452:cmsbot_crab_20240502_195452', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240502_175455:cmsbot_crab_20240502_195454', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240502_175457:cmsbot_crab_20240502_195456', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240502_175514:cmsbot_crab_20240502_195458', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240502_175517:cmsbot_crab_rucio_transfers_20240502_195516', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '20/20/20'}
{'TN': '240502_175519:cmsbot_crab_rucio_transfers_group_20240502_195519', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/35/28'}
{'TN': '240502_175523:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_195521', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175526:cmsbot_crab_rucio_transfers_nopublication_20240502_195524', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_175529:cmsbot_crab_rucio_transfers_withnoneedm_20240502_195528', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '1/39/39'}
{'TN': '240502_175532:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_195531', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
