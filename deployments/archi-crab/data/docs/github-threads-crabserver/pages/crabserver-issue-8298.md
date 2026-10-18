# dmwm/CRABServer issue #8298: #731: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-18T18:48:20Z
Closed: 2024-03-19T21:25:20Z
URL: https://github.com/dmwm/CRABServer/issues/8298

## Opening post (cmsdmwmbot, 2024-03-18T18:48:20Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2024-03-18 19:48:20
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/731/)

## Comment (cmsdmwmbot, 2024-03-18T18:49:31Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240318_184840:cmsbot_crab_20240318_194839
240318_184843:cmsbot_crab_20240318_194842
240318_184845:cmsbot_crab_20240318_194844
240318_184847:cmsbot_crab_20240318_194846
240318_184849:cmsbot_crab_20240318_194849
240318_184853:cmsbot_crab_20240318_194851
240318_184856:cmsbot_crab_rucio_transfers_20240318_194854
240318_184858:cmsbot_crab_rucio_transfers_group_20240318_194857
240318_184901:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_194859
240318_184904:cmsbot_crab_rucio_transfers_nopublication_20240318_194902
240318_184907:cmsbot_crab_rucio_transfers_withnoneedm_20240318_194906
240318_184910:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_194909
```

Finished at: 2024-03-18 19:49:10
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/731/console)

## Comment (cmsdmwmbot, 2024-03-18T19:11:04Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-18 20:11:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/811/console

```
{'TN': '240318_184840:cmsbot_crab_20240318_194839', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 992, 'running': 8}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184843:cmsbot_crab_20240318_194842', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184845:cmsbot_crab_20240318_194844', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184847:cmsbot_crab_20240318_194846', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184849:cmsbot_crab_20240318_194849', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184853:cmsbot_crab_20240318_194851', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 8, 'running': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184856:cmsbot_crab_rucio_transfers_20240318_194854', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184858:cmsbot_crab_rucio_transfers_group_20240318_194857', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184901:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_194859', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184904:cmsbot_crab_rucio_transfers_nopublication_20240318_194902', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184907:cmsbot_crab_rucio_transfers_withnoneedm_20240318_194906', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 3, 'transferring': 37}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184910:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_194909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 34, 'running': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-18T19:28:09Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-03-18 20:28:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/812/console

```
{'TN': '240318_184840:cmsbot_crab_20240318_194839', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 361, 'running': 8, 'finished': 631}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184843:cmsbot_crab_20240318_194842', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184845:cmsbot_crab_20240318_194844', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184847:cmsbot_crab_20240318_194846', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 9, 'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184849:cmsbot_crab_20240318_194849', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 41, 'finished': 58, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184853:cmsbot_crab_20240318_194851', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184856:cmsbot_crab_rucio_transfers_20240318_194854', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 23, 'finished': 17}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184858:cmsbot_crab_rucio_transfers_group_20240318_194857', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 20, 'transferring': 20}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184901:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_194859', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 19, 'transferring': 21}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184904:cmsbot_crab_rucio_transfers_nopublication_20240318_194902', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 29, 'transferring': 11}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184907:cmsbot_crab_rucio_transfers_withnoneedm_20240318_194906', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'running': 2, 'transferring': 11, 'finished': 27}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184910:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_194909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 24, 'running': 1, 'transferring': 15}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-18T20:15:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-03-18 21:15:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/813/console

```
{'TN': '240318_184840:cmsbot_crab_20240318_194839', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 995, 'transferring': 3, 'failed': 2}, 'publication (fail/tdb/DBS)': '0/900/900'}
{'TN': '240318_184843:cmsbot_crab_20240318_194842', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_184845:cmsbot_crab_20240318_194844', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_184847:cmsbot_crab_20240318_194846', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_184849:cmsbot_crab_20240318_194849', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 97, 'transferring': 3}, 'publication (fail/tdb/DBS)': '0/94/94'}
{'TN': '240318_184853:cmsbot_crab_20240318_194851', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_184856:cmsbot_crab_rucio_transfers_20240318_194854', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/39/39'}
{'TN': '240318_184858:cmsbot_crab_rucio_transfers_group_20240318_194857', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 35, 'transferring': 5}, 'publication (fail/tdb/DBS)': '0/35/35'}
{'TN': '240318_184901:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_194859', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 34, 'transferring': 6}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184904:cmsbot_crab_rucio_transfers_nopublication_20240318_194902', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184907:cmsbot_crab_rucio_transfers_withnoneedm_20240318_194906', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 2, 'finished': 38}, 'publication (fail/tdb/DBS)': '0/38/38'}
{'TN': '240318_184910:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_194909', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'running': 1, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-18T21:47:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-03-18 22:47:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/816/console

```
{'TN': '240318_184840:cmsbot_crab_20240318_194839', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240318_184843:cmsbot_crab_20240318_194842', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_184845:cmsbot_crab_20240318_194844', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_184847:cmsbot_crab_20240318_194846', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_184849:cmsbot_crab_20240318_194849', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240318_184853:cmsbot_crab_20240318_194851', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_184856:cmsbot_crab_rucio_transfers_20240318_194854', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240318_184858:cmsbot_crab_rucio_transfers_group_20240318_194857', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 36, 'transferring': 4}, 'publication (fail/tdb/DBS)': '0/36/36'}
{'TN': '240318_184901:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_194859', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184904:cmsbot_crab_rucio_transfers_nopublication_20240318_194902', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184907:cmsbot_crab_rucio_transfers_withnoneedm_20240318_194906', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240318_184910:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_194909', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-03-18T23:47:50Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 4 out of 5. Test is done.
**Finished at:** 2024-03-19 00:47:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/819/console

```
{'TN': '240318_184840:cmsbot_crab_20240318_194839', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '240318_184843:cmsbot_crab_20240318_194842', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_184845:cmsbot_crab_20240318_194844', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '240318_184847:cmsbot_crab_20240318_194846', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_184849:cmsbot_crab_20240318_194849', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '240318_184853:cmsbot_crab_20240318_194851', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '240318_184856:cmsbot_crab_rucio_transfers_20240318_194854', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240318_184858:cmsbot_crab_rucio_transfers_group_20240318_194857', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240318_184901:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240318_194859', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184904:cmsbot_crab_rucio_transfers_nopublication_20240318_194902', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '240318_184907:cmsbot_crab_rucio_transfers_withnoneedm_20240318_194906', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '240318_184910:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240318_194909', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-03-19T21:25:21Z)

OK
