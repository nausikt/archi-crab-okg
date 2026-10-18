# dmwm/CRABServer issue #8184: #680: Test dev CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-01-15T10:29:47Z
Closed: 2024-01-16T16:54:28Z
URL: https://github.com/dmwm/CRABServer/issues/8184

## Opening post (cmsdmwmbot, 2024-01-15T10:29:47Z)

**Tests started for following configuration:**

**This is used to validate use of Rucio group in test https://its.cern.ch/jira/projects/CMSTRANSF/issues/CMSTRANSF-802**

**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Validation
- [x] Task_Submission_Status_Tracking

Started at: 2024-01-15 11:29:46
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/680/)

## Comment (cmsdmwmbot, 2024-01-15T10:31:10Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240115_103007:cmsbot_crab_20240115_113005
240115_103009:cmsbot_crab_20240115_113007
240115_103011:cmsbot_crab_20240115_113009
240115_103013:cmsbot_crab_20240115_113011
240115_103015:cmsbot_crab_20240115_113014
240115_103029:cmsbot_crab_20240115_113016
240115_103032:cmsbot_crab_rucio_transfers_20240115_113029
240115_103034:cmsbot_crab_rucio_transfers_group_20240115_113033
240115_103038:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240115_113035
240115_103041:cmsbot_crab_rucio_transfers_nopublication_20240115_113039
240115_103045:cmsbot_crab_rucio_transfers_withnoneedm_20240115_113042
240115_103048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240115_113046
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240115_103004:cmsbot_crab_20240115_113002
```

Finished at: 2024-01-15 11:30:48
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/680/console)

## Comment (cmsdmwmbot, 2024-01-15T10:52:29Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-15 11:52:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/726/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 5, 'transferring': 995}, 'TN': '240115_103007:cmsbot_crab_20240115_113005', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '240115_103009:cmsbot_crab_20240115_113007', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '240115_103011:cmsbot_crab_20240115_113009', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240115_103013:cmsbot_crab_20240115_113011', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '240115_103015:cmsbot_crab_20240115_113014', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240115_103029:cmsbot_crab_20240115_113016', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240115_103032:cmsbot_crab_rucio_transfers_20240115_113029', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240115_103034:cmsbot_crab_rucio_transfers_group_20240115_113033', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240115_103038:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240115_113035', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 39}, 'TN': '240115_103041:cmsbot_crab_rucio_transfers_nopublication_20240115_113039', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240115_103045:cmsbot_crab_rucio_transfers_withnoneedm_20240115_113042', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '240115_103048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240115_113046', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-15T10:55:01Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-15 11:55:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/498/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/498//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-15T11:08:38Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-01-15 12:08:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/727/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 640, 'transferring': 359, 'running': 1}, 'TN': '240115_103007:cmsbot_crab_20240115_113005', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '240115_103009:cmsbot_crab_20240115_113007', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240115_103011:cmsbot_crab_20240115_113009', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240115_103013:cmsbot_crab_20240115_113011', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240115_103015:cmsbot_crab_20240115_113014', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '240115_103029:cmsbot_crab_20240115_113016', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103032:cmsbot_crab_rucio_transfers_20240115_113029', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'TN': '240115_103034:cmsbot_crab_rucio_transfers_group_20240115_113033', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103038:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240115_113035', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'TN': '240115_103041:cmsbot_crab_rucio_transfers_nopublication_20240115_113039', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103045:cmsbot_crab_rucio_transfers_withnoneedm_20240115_113042', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240115_113046', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-15T11:55:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-01-15 12:55:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/728/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 999, 'running': 1}, 'TN': '240115_103007:cmsbot_crab_20240115_113005', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/900/900'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '240115_103009:cmsbot_crab_20240115_113007', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240115_103011:cmsbot_crab_20240115_113009', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240115_103013:cmsbot_crab_20240115_113011', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240115_103015:cmsbot_crab_20240115_113014', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240115_103029:cmsbot_crab_20240115_113016', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103032:cmsbot_crab_rucio_transfers_20240115_113029', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'TN': '240115_103034:cmsbot_crab_rucio_transfers_group_20240115_113033', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103038:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240115_113035', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103041:cmsbot_crab_rucio_transfers_nopublication_20240115_113039', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103045:cmsbot_crab_rucio_transfers_withnoneedm_20240115_113042', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240115_113046', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-15T13:27:27Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-01-15 14:27:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/729/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 999}, 'TN': '240115_103007:cmsbot_crab_20240115_113005', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/999/999'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '240115_103009:cmsbot_crab_20240115_113007', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240115_103011:cmsbot_crab_20240115_113009', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240115_103013:cmsbot_crab_20240115_113011', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240115_103015:cmsbot_crab_20240115_113014', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240115_103029:cmsbot_crab_20240115_113016', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103032:cmsbot_crab_rucio_transfers_20240115_113029', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'TN': '240115_103034:cmsbot_crab_rucio_transfers_group_20240115_113033', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103038:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240115_113035', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103041:cmsbot_crab_rucio_transfers_nopublication_20240115_113039', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103045:cmsbot_crab_rucio_transfers_withnoneedm_20240115_113042', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240115_113046', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-15T15:29:30Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-01-15 16:29:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/730/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240115_103007:cmsbot_crab_20240115_113005', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '240115_103009:cmsbot_crab_20240115_113007', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240115_103011:cmsbot_crab_20240115_113009', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240115_103013:cmsbot_crab_20240115_113011', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240115_103015:cmsbot_crab_20240115_113014', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240115_103029:cmsbot_crab_20240115_113016', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103032:cmsbot_crab_rucio_transfers_20240115_113029', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'TN': '240115_103034:cmsbot_crab_rucio_transfers_group_20240115_113033', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103038:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240115_113035', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103041:cmsbot_crab_rucio_transfers_nopublication_20240115_113039', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103045:cmsbot_crab_rucio_transfers_withnoneedm_20240115_113042', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240115_113046', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2024-01-15T17:30:36Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-01-15 18:30:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/731/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '240115_103007:cmsbot_crab_20240115_113005', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '240115_103009:cmsbot_crab_20240115_113007', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '240115_103011:cmsbot_crab_20240115_113009', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240115_103013:cmsbot_crab_20240115_113011', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '240115_103015:cmsbot_crab_20240115_113014', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '240115_103029:cmsbot_crab_20240115_113016', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103032:cmsbot_crab_rucio_transfers_20240115_113029', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 39, 'transferring': 1}, 'TN': '240115_103034:cmsbot_crab_rucio_transfers_group_20240115_113033', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/39/39'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103038:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240115_113035', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103041:cmsbot_crab_rucio_transfers_nopublication_20240115_113039', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103045:cmsbot_crab_rucio_transfers_withnoneedm_20240115_113042', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/40/40'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 40}, 'TN': '240115_103048:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240115_113046', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2024-01-16T16:54:28Z)

the failed transfer was due to authorization having got lost in Rucio, see https://its.cern.ch/jira/projects/CMSTRANSF/issues/CMSTRANSF-802?filter=reportedbyme

It is (temporarely ?) fixed now, but retry of the test fails, possible work area was deleted by now.
Close as successful
