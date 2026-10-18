# dmwm/CRABServer issue #7895: #475: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-10-06T09:34:15Z
Closed: 2023-10-09T14:30:26Z
URL: https://github.com/dmwm/CRABServer/issues/7895

## Opening post (cmsdmwmbot, 2023-10-06T09:34:15Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2023-10-06 11:34:14
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/475/)

## Comment (cmsdmwmbot, 2023-10-06T09:35:45Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
231006_093455:cmsbot_crab_20231006_113453
231006_093458:cmsbot_crab_20231006_113457
231006_093500:cmsbot_crab_20231006_113458
231006_093502:cmsbot_crab_20231006_113501
231006_093504:cmsbot_crab_20231006_113503
231006_093524:cmsbot_crab_20231006_113504
```

Finished at: 2023-10-06 11:35:24
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/475/console)

## Comment (cmsdmwmbot, 2023-10-06T09:59:20Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-10-06 11:59:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/649/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 54, 'transferring': 874, 'finished': 72}, 'TN': '231006_093455:cmsbot_crab_20231006_113453', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/72/72'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 5}, 'TN': '231006_093458:cmsbot_crab_20231006_113457', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1}, 'TN': '231006_093500:cmsbot_crab_20231006_113458', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231006_093502:cmsbot_crab_20231006_113501', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 94, 'finished': 5}, 'TN': '231006_093504:cmsbot_crab_20231006_113503', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/5/5'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231006_093524:cmsbot_crab_20231006_113504', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-10-06T10:17:15Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2023-10-06 12:17:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/650/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 709, 'transferring': 285, 'running': 6}, 'TN': '231006_093455:cmsbot_crab_20231006_113453', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/72/72'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 5}, 'TN': '231006_093458:cmsbot_crab_20231006_113457', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1}, 'TN': '231006_093500:cmsbot_crab_20231006_113458', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231006_093502:cmsbot_crab_20231006_113501', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 94, 'transferring': 5, 'running': 1}, 'TN': '231006_093504:cmsbot_crab_20231006_113503', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/5/5'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'TN': '231006_093524:cmsbot_crab_20231006_113504', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-10-06T11:05:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2023-10-06 13:05:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/651/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 2, 'finished': 998}, 'TN': '231006_093455:cmsbot_crab_20231006_113453', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/972/972'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 5}, 'TN': '231006_093458:cmsbot_crab_20231006_113457', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1}, 'TN': '231006_093500:cmsbot_crab_20231006_113458', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231006_093502:cmsbot_crab_20231006_113501', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 99}, 'TN': '231006_093504:cmsbot_crab_20231006_113503', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/99/99'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231006_093524:cmsbot_crab_20231006_113504', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```

## Comment (cmsdmwmbot, 2023-10-06T12:38:19Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2023-10-06 14:38:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/652/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '231006_093455:cmsbot_crab_20231006_113453', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 5}, 'TN': '231006_093458:cmsbot_crab_20231006_113457', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '231006_093500:cmsbot_crab_20231006_113458', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231006_093502:cmsbot_crab_20231006_113501', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231006_093504:cmsbot_crab_20231006_113503', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231006_093524:cmsbot_crab_20231006_113504', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```
