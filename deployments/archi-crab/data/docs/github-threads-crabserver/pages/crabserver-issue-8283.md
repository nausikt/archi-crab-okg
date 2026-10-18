# dmwm/CRABServer issue #8283: #723: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-14T13:01:34Z
Closed: 2024-03-14T19:18:38Z
URL: https://github.com/dmwm/CRABServer/issues/8283

## Opening post (cmsdmwmbot, 2024-03-14T13:01:34Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2024-03-14 14:01:33
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/723/)

## Comment (cmsdmwmbot, 2024-03-14T13:03:40Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240314_130225:cmsbot_crab_20240314_140223
240314_130227:cmsbot_crab_20240314_140226
240314_130229:cmsbot_crab_20240314_140229
240314_130232:cmsbot_crab_20240314_140231
240314_130234:cmsbot_crab_20240314_140233
240314_130300:cmsbot_crab_20240314_140235
240314_130303:cmsbot_crab_rucio_transfers_20240314_140302
240314_130306:cmsbot_crab_rucio_transfers_group_20240314_140305
240314_130309:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240314_140307
240314_130313:cmsbot_crab_rucio_transfers_nopublication_20240314_140311
240314_130316:cmsbot_crab_rucio_transfers_withnoneedm_20240314_140314
240314_130319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240314_140317
```

Finished at: 2024-03-14 14:03:19
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/723/console)

## Comment (cmsdmwmbot, 2024-03-14T13:25:48Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-14 14:25:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/795/console

```
{'TN': '240314_130225:cmsbot_crab_20240314_140223', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1000}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130227:cmsbot_crab_20240314_140226', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130229:cmsbot_crab_20240314_140229', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130232:cmsbot_crab_20240314_140231', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130234:cmsbot_crab_20240314_140233', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 100}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130300:cmsbot_crab_20240314_140235', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130303:cmsbot_crab_rucio_transfers_20240314_140302', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130306:cmsbot_crab_rucio_transfers_group_20240314_140305', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130309:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240314_140307', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130313:cmsbot_crab_rucio_transfers_nopublication_20240314_140311', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130316:cmsbot_crab_rucio_transfers_withnoneedm_20240314_140314', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240314_140317', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-14T13:42:44Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-14 14:42:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/796/console

```
{'TN': '240314_130225:cmsbot_crab_20240314_140223', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 852, 'transferring': 148}, 'publication (fail/tdb/DBS)': '0/200/200'}
{'TN': '240314_130227:cmsbot_crab_20240314_140226', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130229:cmsbot_crab_20240314_140229', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130232:cmsbot_crab_20240314_140231', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 8, 'running': 1, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240314_130234:cmsbot_crab_20240314_140233', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 85, 'transferring': 15}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130300:cmsbot_crab_20240314_140235', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 8, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130303:cmsbot_crab_rucio_transfers_20240314_140302', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 34, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130306:cmsbot_crab_rucio_transfers_group_20240314_140305', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 4, 'finished': 36}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130309:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240314_140307', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 29, 'transferring': 11}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130313:cmsbot_crab_rucio_transfers_nopublication_20240314_140311', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 32, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130316:cmsbot_crab_rucio_transfers_withnoneedm_20240314_140314', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 33, 'transferring': 7}, 'publication (fail/tdb/DBS)': '0/3/3'}
{'TN': '240314_130319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240314_140317', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 32, 'transferring': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-14T14:28:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-14 15:28:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/797/console

```
{'TN': '240314_130225:cmsbot_crab_20240314_140223', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240314_130227:cmsbot_crab_20240314_140226', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130229:cmsbot_crab_20240314_140229', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240314_130232:cmsbot_crab_20240314_140231', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 9, 'running': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240314_130234:cmsbot_crab_20240314_140233', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240314_130300:cmsbot_crab_20240314_140235', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240314_130303:cmsbot_crab_rucio_transfers_20240314_140302', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240314_130306:cmsbot_crab_rucio_transfers_group_20240314_140305', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240314_130309:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240314_140307', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130313:cmsbot_crab_rucio_transfers_nopublication_20240314_140311', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130316:cmsbot_crab_rucio_transfers_withnoneedm_20240314_140314', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '17/23/23'}
{'TN': '240314_130319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240314_140317', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-14T16:00:50Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2024-03-14 17:00:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/798/console

```
{'TN': '240314_130225:cmsbot_crab_20240314_140223', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240314_130227:cmsbot_crab_20240314_140226', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240314_130229:cmsbot_crab_20240314_140229', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240314_130232:cmsbot_crab_20240314_140231', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240314_130234:cmsbot_crab_20240314_140233', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240314_130300:cmsbot_crab_20240314_140235', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240314_130303:cmsbot_crab_rucio_transfers_20240314_140302', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240314_130306:cmsbot_crab_rucio_transfers_group_20240314_140305', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240314_130309:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240314_140307', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130313:cmsbot_crab_rucio_transfers_nopublication_20240314_140311', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240314_130316:cmsbot_crab_rucio_transfers_withnoneedm_20240314_140314', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '17/23/23'}
{'TN': '240314_130319:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240314_140317', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (novicecpp, 2024-03-14T19:18:38Z)

The latest tag [v3.240313](https://github.com/dmwm/CRABServer/releases/tag/v3.240313).
