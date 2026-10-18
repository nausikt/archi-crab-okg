# dmwm/CRABServer issue #8440: #783: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-29T08:50:00Z
Closed: 2024-05-29T12:10:46Z
URL: https://github.com/dmwm/CRABServer/issues/8440

## Opening post (cmsdmwmbot, 2024-05-29T08:50:00Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2024-05-29 10:49:59
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/783/)

## Comment (cmsdmwmbot, 2024-05-29T08:51:39Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240529_085020:cmsbot_crab_20240529_105019
240529_085022:cmsbot_crab_20240529_105021
240529_085024:cmsbot_crab_20240529_105024
240529_085026:cmsbot_crab_20240529_105026
240529_085029:cmsbot_crab_20240529_105028
240529_085058:cmsbot_crab_20240529_105031
240529_085101:cmsbot_crab_rucio_transfers_20240529_105100
240529_085103:cmsbot_crab_rucio_transfers_group_20240529_105103
240529_085107:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_105105
240529_085110:cmsbot_crab_rucio_transfers_nopublication_20240529_105109
240529_085114:cmsbot_crab_rucio_transfers_withnoneedm_20240529_105112
240529_085117:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_105116
```

Finished at: 2024-05-29 10:51:18
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/783/console)

## Comment (cmsdmwmbot, 2024-05-29T09:14:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-29 11:14:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/936/console

```
{'TN': '240529_085020:cmsbot_crab_20240529_105019', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 998, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085022:cmsbot_crab_20240529_105021', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085024:cmsbot_crab_20240529_105024', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085026:cmsbot_crab_20240529_105026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085029:cmsbot_crab_20240529_105028', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085058:cmsbot_crab_20240529_105031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085101:cmsbot_crab_rucio_transfers_20240529_105100', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085103:cmsbot_crab_rucio_transfers_group_20240529_105103', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085107:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_105105', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085110:cmsbot_crab_rucio_transfers_nopublication_20240529_105109', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085114:cmsbot_crab_rucio_transfers_withnoneedm_20240529_105112', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085117:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_105116', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-29T09:31:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-05-29 11:31:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/937/console

```
{'TN': '240529_085020:cmsbot_crab_20240529_105019', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 630, 'finished': 368, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085022:cmsbot_crab_20240529_105021', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085024:cmsbot_crab_20240529_105024', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085026:cmsbot_crab_20240529_105026', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 2, 'finished': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085029:cmsbot_crab_20240529_105028', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 83, 'transferring': 17}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085058:cmsbot_crab_20240529_105031', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085101:cmsbot_crab_rucio_transfers_20240529_105100', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 37, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085103:cmsbot_crab_rucio_transfers_group_20240529_105103', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 5, 'finished': 35}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085107:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_105105', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 27, 'transferring': 13}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085110:cmsbot_crab_rucio_transfers_nopublication_20240529_105109', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 30, 'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085114:cmsbot_crab_rucio_transfers_withnoneedm_20240529_105112', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 12, 'finished': 28}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085117:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_105116', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 33, 'transferring': 7}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-29T10:18:22Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-05-29 12:18:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/938/console

```
{'TN': '240529_085020:cmsbot_crab_20240529_105019', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240529_085022:cmsbot_crab_20240529_105021', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085024:cmsbot_crab_20240529_105024', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240529_085026:cmsbot_crab_20240529_105026', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240529_085029:cmsbot_crab_20240529_105028', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/99/99'}
{'TN': '240529_085058:cmsbot_crab_20240529_105031', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240529_085101:cmsbot_crab_rucio_transfers_20240529_105100', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_085103:cmsbot_crab_rucio_transfers_group_20240529_105103', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_085107:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_105105', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085110:cmsbot_crab_rucio_transfers_nopublication_20240529_105109', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085114:cmsbot_crab_rucio_transfers_withnoneedm_20240529_105112', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_085117:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_105116', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-05-29T11:50:19Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-05-29 13:50:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/939/console

```
{'TN': '240529_085020:cmsbot_crab_20240529_105019', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240529_085022:cmsbot_crab_20240529_105021', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240529_085024:cmsbot_crab_20240529_105024', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240529_085026:cmsbot_crab_20240529_105026', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240529_085029:cmsbot_crab_20240529_105028', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240529_085058:cmsbot_crab_20240529_105031', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240529_085101:cmsbot_crab_rucio_transfers_20240529_105100', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_085103:cmsbot_crab_rucio_transfers_group_20240529_105103', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_085107:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240529_105105', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085110:cmsbot_crab_rucio_transfers_nopublication_20240529_105109', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240529_085114:cmsbot_crab_rucio_transfers_withnoneedm_20240529_105112', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240529_085117:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240529_105116', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```
