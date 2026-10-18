# dmwm/CRABServer issue #8370: #765: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-02T14:52:47Z
Closed: 2024-05-06T22:34:12Z
URL: https://github.com/dmwm/CRABServer/issues/8370

## Opening post (cmsdmwmbot, 2024-05-02T14:52:47Z)

**Tests started for following configuration:**

**Using this to validate (a bit) https://github.com/belforte/CRABServer/tree/deal-with-failed-migrations-8244**

**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2024-05-02 16:52:46
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/765/)

## Comment (cmsdmwmbot, 2024-05-02T14:54:52Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240502_145310:cmsbot_crab_20240502_165307
240502_145315:cmsbot_crab_20240502_165314
240502_145317:cmsbot_crab_20240502_165316
240502_145319:cmsbot_crab_20240502_165319
240502_145321:cmsbot_crab_20240502_165321
240502_145411:cmsbot_crab_20240502_165323
240502_145415:cmsbot_crab_rucio_transfers_20240502_165413
240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417
240502_145421:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_165419
240502_145424:cmsbot_crab_rucio_transfers_nopublication_20240502_165423
240502_145427:cmsbot_crab_rucio_transfers_withnoneedm_20240502_165426
240502_145431:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_165429
```

Finished at: 2024-05-02 16:54:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/765/console)

## Comment (cmsdmwmbot, 2024-05-02T15:15:51Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-02 17:15:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/877/console

```
{'TN': '240502_145310:cmsbot_crab_20240502_165307', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145315:cmsbot_crab_20240502_165314', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145317:cmsbot_crab_20240502_165316', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145319:cmsbot_crab_20240502_165319', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145321:cmsbot_crab_20240502_165321', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 97, 'running': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145411:cmsbot_crab_20240502_165323', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 2, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145415:cmsbot_crab_rucio_transfers_20240502_165413', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145421:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_165419', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145424:cmsbot_crab_rucio_transfers_nopublication_20240502_165423', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145427:cmsbot_crab_rucio_transfers_withnoneedm_20240502_165426', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145431:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_165429', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-02T15:31:50Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-05-02 17:31:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/878/console

```
{'TN': '240502_145310:cmsbot_crab_20240502_165307', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145315:cmsbot_crab_20240502_165314', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145317:cmsbot_crab_20240502_165316', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145319:cmsbot_crab_20240502_165319', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145321:cmsbot_crab_20240502_165321', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 88, 'transferring': 12}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145411:cmsbot_crab_20240502_165323', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145415:cmsbot_crab_rucio_transfers_20240502_165413', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/30/30'}
{'TN': '240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/35/35'}
{'TN': '240502_145421:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_165419', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 35, 'transferring': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145424:cmsbot_crab_rucio_transfers_nopublication_20240502_165423', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145427:cmsbot_crab_rucio_transfers_withnoneedm_20240502_165426', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/35/35'}
{'TN': '240502_145431:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_165429', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-02T16:21:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-05-02 18:21:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/879/console

```
{'TN': '240502_145310:cmsbot_crab_20240502_165307', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145315:cmsbot_crab_20240502_165314', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145317:cmsbot_crab_20240502_165316', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240502_145319:cmsbot_crab_20240502_165319', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240502_145321:cmsbot_crab_20240502_165321', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240502_145411:cmsbot_crab_20240502_165323', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240502_145415:cmsbot_crab_rucio_transfers_20240502_165413', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '8/32/32'}
{'TN': '240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '4/36/36'}
{'TN': '240502_145421:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_165419', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145424:cmsbot_crab_rucio_transfers_nopublication_20240502_165423', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145427:cmsbot_crab_rucio_transfers_withnoneedm_20240502_165426', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '4/36/36'}
{'TN': '240502_145431:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_165429', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-02T17:54:24Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-05-02 19:54:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/880/console

```
{'TN': '240502_145310:cmsbot_crab_20240502_165307', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145315:cmsbot_crab_20240502_165314', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145317:cmsbot_crab_20240502_165316', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240502_145319:cmsbot_crab_20240502_165319', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240502_145321:cmsbot_crab_20240502_165321', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240502_145411:cmsbot_crab_20240502_165323', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240502_145415:cmsbot_crab_rucio_transfers_20240502_165413', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '8/32/32'}
{'TN': '240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '4/36/36'}
{'TN': '240502_145421:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_165419', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145424:cmsbot_crab_rucio_transfers_nopublication_20240502_165423', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145427:cmsbot_crab_rucio_transfers_withnoneedm_20240502_165426', 'testResult': 'TestFailed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '4/36/36'}
{'TN': '240502_145431:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_165429', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-02T19:57:24Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-05-02 21:57:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/884/console

```
{'TN': '240502_145310:cmsbot_crab_20240502_165307', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145315:cmsbot_crab_20240502_165314', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145317:cmsbot_crab_20240502_165316', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240502_145319:cmsbot_crab_20240502_165319', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240502_145321:cmsbot_crab_20240502_165321', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240502_145411:cmsbot_crab_20240502_165323', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240502_145415:cmsbot_crab_rucio_transfers_20240502_165413', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/32'}
{'TN': '240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/38/36'}
{'TN': '240502_145421:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240502_165419', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145424:cmsbot_crab_rucio_transfers_nopublication_20240502_165423', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240502_145427:cmsbot_crab_rucio_transfers_withnoneedm_20240502_165426', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/36'}
{'TN': '240502_145431:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240502_165429', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
