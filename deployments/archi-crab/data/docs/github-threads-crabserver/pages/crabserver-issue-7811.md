# dmwm/CRABServer issue #7811: #457: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-08-11T20:01:00Z
Closed: 2023-08-11T20:13:53Z
URL: https://github.com/dmwm/CRABServer/issues/7811

## Opening post (cmsdmwmbot, 2023-08-11T20:01:00Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-08-11 22:00:59
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/457/)

## Comment (cmsdmwmbot, 2023-08-11T20:01:48Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230811_200117:cmsbot_crab_20230811_220116
230811_200119:cmsbot_crab_20230811_220118
230811_200121:cmsbot_crab_20230811_220120
230811_200122:cmsbot_crab_20230811_220122
230811_200124:cmsbot_crab_20230811_220123
230811_200127:cmsbot_crab_20230811_220125
```

Finished at: 2023-08-11 22:01:27
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/457/console)

## Comment (cmsdmwmbot, 2023-08-11T20:09:03Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 0 out of 4. Something went wrong. Investigate manually.
**Finished at:** 2023-08-11 22:09:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/538/console

```

```

## Comment (belforte, 2023-08-11T20:13:53Z)

mea culpa

## Comment (cmsdmwmbot, 2023-08-11T20:17:59Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 0 out of 4. Something went wrong. Investigate manually.
**Finished at:** 2023-08-11 22:17:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/539/console

```

```

## Comment (cmsdmwmbot, 2023-08-11T20:28:00Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 0 out of 4. Something went wrong. Investigate manually.
**Finished at:** 2023-08-11 22:27:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/540/console

```

```

## Comment (cmsdmwmbot, 2023-08-11T21:53:11Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-11 23:53:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/541/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 978, 'transferring': 21}, 'TN': '230811_200117:cmsbot_crab_20230811_220116', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/978/978'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '230811_200119:cmsbot_crab_20230811_220118', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/5'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_200121:cmsbot_crab_20230811_220120', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'TN': '230811_200122:cmsbot_crab_20230811_220122', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/9/9'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 1, 'finished': 95, 'transferring': 4}, 'TN': '230811_200124:cmsbot_crab_20230811_220123', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/95/95'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200127:cmsbot_crab_20230811_220125', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '0/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-11T22:00:52Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 20. Will run again.
**Finished at:** 2023-08-12 00:00:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/542/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 997, 'transferring': 3}, 'TN': '230811_200117:cmsbot_crab_20230811_220116', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/978/997'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '230811_200119:cmsbot_crab_20230811_220118', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/5'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_200121:cmsbot_crab_20230811_220120', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'TN': '230811_200122:cmsbot_crab_20230811_220122', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/9/9'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 98, 'transferring': 1, 'running': 1}, 'TN': '230811_200124:cmsbot_crab_20230811_220123', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/95/98'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200127:cmsbot_crab_20230811_220125', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '0/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-11T22:13:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-12 00:13:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/544/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 997, 'transferring': 3}, 'TN': '230811_200117:cmsbot_crab_20230811_220116', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '997/997/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '230811_200119:cmsbot_crab_20230811_220118', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_200121:cmsbot_crab_20230811_220120', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200122:cmsbot_crab_20230811_220122', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 98, 'transferring': 2}, 'TN': '230811_200124:cmsbot_crab_20230811_220123', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '98/98/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200127:cmsbot_crab_20230811_220125', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T22:21:03Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 20. Will run again.
**Finished at:** 2023-08-12 00:21:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/545/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 997, 'transferring': 3}, 'TN': '230811_200117:cmsbot_crab_20230811_220116', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '997/997/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230811_200119:cmsbot_crab_20230811_220118', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '6/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_200121:cmsbot_crab_20230811_220120', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200122:cmsbot_crab_20230811_220122', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 98, 'transferring': 2}, 'TN': '230811_200124:cmsbot_crab_20230811_220123', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '98/98/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200127:cmsbot_crab_20230811_220125', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T22:28:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 20. Will run again.
**Finished at:** 2023-08-12 00:28:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/546/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 997, 'transferring': 3}, 'TN': '230811_200117:cmsbot_crab_20230811_220116', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '997/997/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230811_200119:cmsbot_crab_20230811_220118', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '6/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_200121:cmsbot_crab_20230811_220120', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200122:cmsbot_crab_20230811_220122', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'TN': '230811_200124:cmsbot_crab_20230811_220123', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '99/98/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200127:cmsbot_crab_20230811_220125', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T22:35:29Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 20. Test is done.
**Finished at:** 2023-08-12 00:35:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/547/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_200117:cmsbot_crab_20230811_220116', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/997/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230811_200119:cmsbot_crab_20230811_220118', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '6/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_200121:cmsbot_crab_20230811_220120', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200122:cmsbot_crab_20230811_220122', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_200124:cmsbot_crab_20230811_220123', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/98/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_200127:cmsbot_crab_20230811_220125', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```
