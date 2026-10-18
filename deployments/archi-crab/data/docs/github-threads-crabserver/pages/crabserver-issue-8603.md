# dmwm/CRABServer issue #8603: #826: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-08-09T15:23:12Z
Closed: 2024-08-09T23:12:48Z
URL: https://github.com/dmwm/CRABServer/issues/8603

## Opening post (cmsdmwmbot, 2024-08-09T15:23:12Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2024-08-09 17:23:11
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/826/)

## Comment (cmsdmwmbot, 2024-08-09T15:24:28Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240809_152329:cmsbot_crab_20240809_172328
240809_152331:cmsbot_crab_20240809_172330
240809_152333:cmsbot_crab_20240809_172332
240809_152336:cmsbot_crab_20240809_172335
240809_152338:cmsbot_crab_20240809_172337
240809_152348:cmsbot_crab_20240809_172339
240809_152351:cmsbot_crab_rucio_transfers_20240809_172350
240809_152353:cmsbot_crab_rucio_transfers_group_20240809_172352
240809_152356:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_172355
240809_152359:cmsbot_crab_rucio_transfers_nopublication_20240809_172358
240809_152402:cmsbot_crab_rucio_transfers_withnoneedm_20240809_172401
240809_152407:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_172404
```

Finished at: 2024-08-09 17:24:07
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/826/console)

## Comment (cmsdmwmbot, 2024-08-09T15:46:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-08-09 17:46:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1062/console

```
{'TN': '240809_152329:cmsbot_crab_20240809_172328', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 996, 'running': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152331:cmsbot_crab_20240809_172330', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152333:cmsbot_crab_20240809_172332', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152336:cmsbot_crab_20240809_172335', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152338:cmsbot_crab_20240809_172337', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 94, 'running': 5, 'cooloff': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152348:cmsbot_crab_20240809_172339', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 8, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152351:cmsbot_crab_rucio_transfers_20240809_172350', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152353:cmsbot_crab_rucio_transfers_group_20240809_172352', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 30, 'running': 9, 'cooloff': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152356:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_172355', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'cooloff': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152359:cmsbot_crab_rucio_transfers_nopublication_20240809_172358', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152402:cmsbot_crab_rucio_transfers_withnoneedm_20240809_172401', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152407:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_172404', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'cooloff': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-09T16:02:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-08-09 18:02:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1063/console

```
{'TN': '240809_152329:cmsbot_crab_20240809_172328', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152331:cmsbot_crab_20240809_172330', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152333:cmsbot_crab_20240809_172332', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152336:cmsbot_crab_20240809_172335', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152338:cmsbot_crab_20240809_172337', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 97, 'running': 2, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152348:cmsbot_crab_20240809_172339', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152351:cmsbot_crab_rucio_transfers_20240809_172350', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152353:cmsbot_crab_rucio_transfers_group_20240809_172352', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 38, 'failed': 1, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152356:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_172355', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152359:cmsbot_crab_rucio_transfers_nopublication_20240809_172358', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152402:cmsbot_crab_rucio_transfers_withnoneedm_20240809_172401', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152407:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_172404', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-09T16:48:06Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-08-09 18:48:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1065/console

```
{'TN': '240809_152329:cmsbot_crab_20240809_172328', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 933, 'finished': 67}, 'publication (fail/tdb/DBS)': '0/79/79'}
{'TN': '240809_152331:cmsbot_crab_20240809_172330', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152333:cmsbot_crab_20240809_172332', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240809_152336:cmsbot_crab_20240809_172335', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240809_152338:cmsbot_crab_20240809_172337', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 52, 'transferring': 47, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240809_152348:cmsbot_crab_20240809_172339', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240809_152351:cmsbot_crab_rucio_transfers_20240809_172350', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152353:cmsbot_crab_rucio_transfers_group_20240809_172352', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240809_152356:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_172355', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240809_152359:cmsbot_crab_rucio_transfers_nopublication_20240809_172358', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152402:cmsbot_crab_rucio_transfers_withnoneedm_20240809_172401', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152407:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_172404', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-08-09T18:20:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-08-09 20:20:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1067/console

```
{'TN': '240809_152329:cmsbot_crab_20240809_172328', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 219, 'transferring': 781}, 'publication (fail/tdb/DBS)': '0/230/230'}
{'TN': '240809_152331:cmsbot_crab_20240809_172330', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240809_152333:cmsbot_crab_20240809_172332', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240809_152336:cmsbot_crab_20240809_172335', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240809_152338:cmsbot_crab_20240809_172337', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 99, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240809_152348:cmsbot_crab_20240809_172339', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240809_152351:cmsbot_crab_rucio_transfers_20240809_172350', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152353:cmsbot_crab_rucio_transfers_group_20240809_172352', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240809_152356:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_172355', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240809_152359:cmsbot_crab_rucio_transfers_nopublication_20240809_172358', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152402:cmsbot_crab_rucio_transfers_withnoneedm_20240809_172401', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152407:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_172404', 'testResult': 'TestResubmitted', 'dbStatus': 'RESUBMITFAILED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 39, 'failed': 1}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-08-09T20:22:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-08-09 22:22:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1069/console

```
{'TN': '240809_152329:cmsbot_crab_20240809_172328', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 418, 'transferring': 582}, 'publication (fail/tdb/DBS)': '0/429/429'}
{'TN': '240809_152331:cmsbot_crab_20240809_172330', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240809_152333:cmsbot_crab_20240809_172332', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240809_152336:cmsbot_crab_20240809_172335', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240809_152338:cmsbot_crab_20240809_172337', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240809_152348:cmsbot_crab_20240809_172339', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240809_152351:cmsbot_crab_rucio_transfers_20240809_172350', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/18/18'}
{'TN': '240809_152353:cmsbot_crab_rucio_transfers_group_20240809_172352', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 19, 'transferring': 21}, 'publication (fail/tdb/DBS)': '0/19/19'}
{'TN': '240809_152356:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_172355', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 30, 'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152359:cmsbot_crab_rucio_transfers_nopublication_20240809_172358', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 7, 'finished': 33}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152402:cmsbot_crab_rucio_transfers_withnoneedm_20240809_172401', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 15, 'finished': 25}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152407:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_172404', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 13, 'transferring': 27}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-09T22:23:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-08-10 00:23:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1071/console

```
{'TN': '240809_152329:cmsbot_crab_20240809_172328', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 618, 'transferring': 382}, 'publication (fail/tdb/DBS)': '0/628/0'}
{'TN': '240809_152331:cmsbot_crab_20240809_172330', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/0'}
{'TN': '240809_152333:cmsbot_crab_20240809_172332', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/0'}
{'TN': '240809_152336:cmsbot_crab_20240809_172335', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/0'}
{'TN': '240809_152338:cmsbot_crab_20240809_172337', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/0'}
{'TN': '240809_152348:cmsbot_crab_20240809_172339', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/0'}
{'TN': '240809_152351:cmsbot_crab_rucio_transfers_20240809_172350', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/0'}
{'TN': '240809_152353:cmsbot_crab_rucio_transfers_group_20240809_172352', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/0'}
{'TN': '240809_152356:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_172355', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152359:cmsbot_crab_rucio_transfers_nopublication_20240809_172358', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152402:cmsbot_crab_rucio_transfers_withnoneedm_20240809_172401', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/0'}
{'TN': '240809_152407:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_172404', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-08-09T23:10:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 0. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-08-10 01:10:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1072/console

```
{'TN': '240809_152329:cmsbot_crab_20240809_172328', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 702, 'transferring': 298}, 'publication (fail/tdb/DBS)': '0/683/683'}
{'TN': '240809_152331:cmsbot_crab_20240809_172330', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240809_152333:cmsbot_crab_20240809_172332', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240809_152336:cmsbot_crab_20240809_172335', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240809_152338:cmsbot_crab_20240809_172337', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240809_152348:cmsbot_crab_20240809_172339', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240809_152351:cmsbot_crab_rucio_transfers_20240809_172350', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240809_152353:cmsbot_crab_rucio_transfers_group_20240809_172352', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240809_152356:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240809_172355', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152359:cmsbot_crab_rucio_transfers_nopublication_20240809_172358', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240809_152402:cmsbot_crab_rucio_transfers_withnoneedm_20240809_172401', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240809_152407:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240809_172404', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-08-09T23:12:35Z)

OK. The 1K job task is stuck in transferring due to https://github.com/dmwm/CRABServer/issues/8597
