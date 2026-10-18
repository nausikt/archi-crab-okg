# dmwm/CRABServer issue #7784: #448: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-21T11:23:05Z
Closed: 2023-08-02T12:15:50Z
URL: https://github.com/dmwm/CRABServer/issues/7784

## Opening post (cmsdmwmbot, 2023-07-21T11:23:05Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-07-21 13:23:04
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/448/)

## Comment (cmsdmwmbot, 2023-07-21T11:23:52Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230721_112321:cmsbot_crab_20230721_132320
230721_112324:cmsbot_crab_20230721_132323
230721_112325:cmsbot_crab_20230721_132324
230721_112326:cmsbot_crab_20230721_132326
230721_112328:cmsbot_crab_20230721_132327
230721_112331:cmsbot_crab_20230721_132329
```

Finished at: 2023-07-21 13:23:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/448/console)

## Comment (cmsdmwmbot, 2023-07-21T12:27:06Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-21 14:27:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/520/console

```
{'TN': '230721_112321:cmsbot_crab_20230721_132320', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 31, 'finished': 302, 'transferring': 667}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112324:cmsbot_crab_20230721_132323', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112325:cmsbot_crab_20230721_132324', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112326:cmsbot_crab_20230721_132326', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112328:cmsbot_crab_20230721_132327', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 10, 'transferring': 89}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112331:cmsbot_crab_20230721_132329', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-21T13:30:51Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-21 15:30:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/521/console

```
{'TN': '230721_112321:cmsbot_crab_20230721_132320', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 31, 'finished': 377, 'transferring': 592}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112324:cmsbot_crab_20230721_132323', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112325:cmsbot_crab_20230721_132324', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112326:cmsbot_crab_20230721_132326', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112328:cmsbot_crab_20230721_132327', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 16, 'transferring': 83}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112331:cmsbot_crab_20230721_132329', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 2, 'transferring': 8}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-21T14:33:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-21 16:33:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/522/console

```
{'TN': '230721_112321:cmsbot_crab_20230721_132320', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 392, 'transferring': 607, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112324:cmsbot_crab_20230721_132323', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112325:cmsbot_crab_20230721_132324', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112326:cmsbot_crab_20230721_132326', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112328:cmsbot_crab_20230721_132327', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 16, 'transferring': 84}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112331:cmsbot_crab_20230721_132329', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 2, 'transferring': 8}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-21T15:37:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-21 17:37:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/523/console

```
{'TN': '230721_112321:cmsbot_crab_20230721_132320', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 397, 'transferring': 603}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112324:cmsbot_crab_20230721_132323', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112325:cmsbot_crab_20230721_132324', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230721_112326:cmsbot_crab_20230721_132326', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112328:cmsbot_crab_20230721_132327', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 18, 'transferring': 82}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112331:cmsbot_crab_20230721_132329', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (cmsdmwmbot, 2023-07-21T16:42:55Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-21 18:42:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/524/console

```
{'TN': '230721_112321:cmsbot_crab_20230721_132320', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 399, 'transferring': 601}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112324:cmsbot_crab_20230721_132323', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112325:cmsbot_crab_20230721_132324', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230721_112326:cmsbot_crab_20230721_132326', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112328:cmsbot_crab_20230721_132327', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 18, 'transferring': 82}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230721_112331:cmsbot_crab_20230721_132329', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'transferring': 6}, 'combinedStatus': 'SUBMITTED'}
```

## Comment (belforte, 2023-08-02T12:15:50Z)

gave up
