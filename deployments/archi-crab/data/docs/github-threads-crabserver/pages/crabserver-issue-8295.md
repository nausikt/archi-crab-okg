# dmwm/CRABServer issue #8295: #730: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-16T16:18:58Z
Closed: 2024-03-17T12:05:35Z
URL: https://github.com/dmwm/CRABServer/issues/8295

## Opening post (cmsdmwmbot, 2024-03-16T16:18:58Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2024-03-16 17:18:57
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/730/)

## Comment (cmsdmwmbot, 2024-03-16T16:21:07Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240316_161921:cmsbot_crab_20240316_171919
240316_161923:cmsbot_crab_20240316_171923
240316_161925:cmsbot_crab_20240316_171925
240316_161927:cmsbot_crab_20240316_171927
240316_161929:cmsbot_crab_20240316_171929
240316_161958:cmsbot_crab_20240316_171931
240316_162001:cmsbot_crab_rucio_transfers_20240316_171959
240316_162003:cmsbot_crab_rucio_transfers_group_20240316_172002
240316_162037:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240316_172004
240316_162040:cmsbot_crab_rucio_transfers_nopublication_20240316_172039
240316_162043:cmsbot_crab_rucio_transfers_withnoneedm_20240316_172042
240316_162046:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240316_172045
```

Finished at: 2024-03-16 17:20:46
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/730/console)

## Comment (cmsdmwmbot, 2024-03-16T16:42:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-16 17:41:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/806/console

```
{'TN': '240316_161921:cmsbot_crab_20240316_171919', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 992, 'running': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_161923:cmsbot_crab_20240316_171923', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_161925:cmsbot_crab_20240316_171925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_161927:cmsbot_crab_20240316_171927', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_161929:cmsbot_crab_20240316_171929', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_161958:cmsbot_crab_20240316_171931', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 4, 'running': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162001:cmsbot_crab_rucio_transfers_20240316_171959', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162003:cmsbot_crab_rucio_transfers_group_20240316_172002', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162037:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240316_172004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162040:cmsbot_crab_rucio_transfers_nopublication_20240316_172039', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162043:cmsbot_crab_rucio_transfers_withnoneedm_20240316_172042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162046:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240316_172045', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-16T16:57:51Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-16 17:57:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/807/console

```
{'TN': '240316_161921:cmsbot_crab_20240316_171919', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 353, 'finished': 640, 'running': 7}, 'publication (fail/tdb/DBS)': '0/500/500'}
{'TN': '240316_161923:cmsbot_crab_20240316_171923', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_161925:cmsbot_crab_20240316_171925', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_161927:cmsbot_crab_20240316_171927', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/3/3'}
{'TN': '240316_161929:cmsbot_crab_20240316_171929', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/23/23'}
{'TN': '240316_161958:cmsbot_crab_20240316_171931', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162001:cmsbot_crab_rucio_transfers_20240316_171959', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162003:cmsbot_crab_rucio_transfers_group_20240316_172002', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162037:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240316_172004', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162040:cmsbot_crab_rucio_transfers_nopublication_20240316_172039', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162043:cmsbot_crab_rucio_transfers_withnoneedm_20240316_172042', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162046:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240316_172045', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-16T17:46:56Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-16 18:46:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/808/console

```
{'TN': '240316_161921:cmsbot_crab_20240316_171919', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 993, 'failed': 6, 'running': 1}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240316_161923:cmsbot_crab_20240316_171923', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_161925:cmsbot_crab_20240316_171925', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240316_161927:cmsbot_crab_20240316_171927', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240316_161929:cmsbot_crab_20240316_171929', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240316_161958:cmsbot_crab_20240316_171931', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240316_162001:cmsbot_crab_rucio_transfers_20240316_171959', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240316_162003:cmsbot_crab_rucio_transfers_group_20240316_172002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240316_162037:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240316_172004', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162040:cmsbot_crab_rucio_transfers_nopublication_20240316_172039', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162043:cmsbot_crab_rucio_transfers_withnoneedm_20240316_172042', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240316_162046:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240316_172045', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-16T19:19:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-03-16 20:19:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/809/console

```
{'TN': '240316_161921:cmsbot_crab_20240316_171919', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'FAILED', 'jobsPerStatus': {'finished': 999, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/999/999'}
{'TN': '240316_161923:cmsbot_crab_20240316_171923', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240316_161925:cmsbot_crab_20240316_171925', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240316_161927:cmsbot_crab_20240316_171927', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240316_161929:cmsbot_crab_20240316_171929', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240316_161958:cmsbot_crab_20240316_171931', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240316_162001:cmsbot_crab_rucio_transfers_20240316_171959', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240316_162003:cmsbot_crab_rucio_transfers_group_20240316_172002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240316_162037:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240316_172004', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162040:cmsbot_crab_rucio_transfers_nopublication_20240316_172039', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162043:cmsbot_crab_rucio_transfers_withnoneedm_20240316_172042', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240316_162046:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240316_172045', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-16T21:21:02Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 4 out of 5. Test is done.
**Finished at:** 2024-03-16 22:21:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/810/console

```
{'TN': '240316_161921:cmsbot_crab_20240316_171919', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240316_161923:cmsbot_crab_20240316_171923', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240316_161925:cmsbot_crab_20240316_171925', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240316_161927:cmsbot_crab_20240316_171927', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240316_161929:cmsbot_crab_20240316_171929', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240316_161958:cmsbot_crab_20240316_171931', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240316_162001:cmsbot_crab_rucio_transfers_20240316_171959', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240316_162003:cmsbot_crab_rucio_transfers_group_20240316_172002', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240316_162037:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240316_172004', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162040:cmsbot_crab_rucio_transfers_nopublication_20240316_172039', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240316_162043:cmsbot_crab_rucio_transfers_withnoneedm_20240316_172042', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240316_162046:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240316_172045', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-03-17T12:05:35Z)

ALL OK
