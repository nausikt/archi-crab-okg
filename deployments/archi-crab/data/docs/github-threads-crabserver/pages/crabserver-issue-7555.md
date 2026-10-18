# dmwm/CRABServer issue #7555: #378: Test prod CRABClient using test11 REST instance and CMSSW_12_6_0_pre4 CMSSW release

State: closed
Opened: 2023-02-27T12:34:16Z
Closed: 2023-03-29T10:41:18Z
URL: https://github.com/dmwm/CRABServer/issues/7555

## Opening post (cmsdmwmbot, 2023-02-27T12:34:16Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test11**
- CMSSW_release: **CMSSW_12_6_0_pre4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-02-27 13:34:15
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/378/)

## Comment (cmsdmwmbot, 2023-02-27T12:35:07Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230227_123436:cmsbot_crab_20230227_133435
230227_123438:cmsbot_crab_20230227_133438
230227_123439:cmsbot_crab_20230227_133439
230227_123441:cmsbot_crab_20230227_133440
230227_123442:cmsbot_crab_20230227_133442
230227_123446:cmsbot_crab_20230227_133443
```

Finished at: 2023-02-27 13:34:46
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/378/console)

## Comment (mapellidario, 2023-02-27T12:42:59Z)

I will use these tasks to check some changes to the jobwrapper

## Comment (cmsdmwmbot, 2023-02-27T13:37:30Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-27 14:37:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/439/console

```
{'TN': '230227_123436:cmsbot_crab_20230227_133435', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 997, 'transferring': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230227_123438:cmsbot_crab_20230227_133438', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230227_123439:cmsbot_crab_20230227_133439', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230227_123441:cmsbot_crab_20230227_133440', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230227_123442:cmsbot_crab_20230227_133442', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230227_123446:cmsbot_crab_20230227_133443', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-02-27T14:39:49Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2023-02-27 15:39:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/440/console

```
{'TN': '230227_123436:cmsbot_crab_20230227_133435', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'combinedStatus': 'COMPLETED'}
{'TN': '230227_123438:cmsbot_crab_20230227_133438', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 7}, 'combinedStatus': 'COMPLETED'}
{'TN': '230227_123439:cmsbot_crab_20230227_133439', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230227_123441:cmsbot_crab_20230227_133440', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
{'TN': '230227_123442:cmsbot_crab_20230227_133442', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'combinedStatus': 'COMPLETED'}
{'TN': '230227_123446:cmsbot_crab_20230227_133443', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (mapellidario, 2023-03-29T10:41:18Z)

succeded
