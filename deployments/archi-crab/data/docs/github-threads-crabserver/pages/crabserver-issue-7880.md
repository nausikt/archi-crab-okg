# dmwm/CRABServer issue #7880: #473: Test prod CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-09-15T09:28:06Z
Closed: 2023-09-15T13:01:47Z
URL: https://github.com/dmwm/CRABServer/issues/7880

## Opening post (cmsdmwmbot, 2023-09-15T09:28:06Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-09-15 11:28:04
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/473/)

## Comment (cmsdmwmbot, 2023-09-15T09:30:14Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230915_092924:cmsbot_crab_20230915_112922
230915_092926:cmsbot_crab_20230915_112925
230915_092927:cmsbot_crab_20230915_112927
230915_092929:cmsbot_crab_20230915_112929
230915_092931:cmsbot_crab_20230915_112930
230915_092952:cmsbot_crab_20230915_112932
```

Finished at: 2023-09-15 11:29:53
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/473/console)

## Comment (cmsdmwmbot, 2023-09-15T09:52:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-09-15 11:52:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/641/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 155, 'transferring': 833, 'running': 12}, 'TN': '230915_092924:cmsbot_crab_20230915_112922', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'TN': '230915_092926:cmsbot_crab_20230915_112925', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230915_092927:cmsbot_crab_20230915_112927', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'TN': '230915_092929:cmsbot_crab_20230915_112929', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 34, 'transferring': 64, 'running': 2}, 'TN': '230915_092931:cmsbot_crab_20230915_112930', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/34/34'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 5}, 'TN': '230915_092952:cmsbot_crab_20230915_112932', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/5/5'}
```

## Comment (cmsdmwmbot, 2023-09-15T10:10:21Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2023-09-15 12:10:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/642/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 849, 'transferring': 139, 'running': 12}, 'TN': '230915_092924:cmsbot_crab_20230915_112922', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230915_092926:cmsbot_crab_20230915_112925', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1}, 'TN': '230915_092927:cmsbot_crab_20230915_112927', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 10}, 'TN': '230915_092929:cmsbot_crab_20230915_112929', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 90, 'transferring': 8, 'running': 2}, 'TN': '230915_092931:cmsbot_crab_20230915_112930', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/34/34'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'transferring': 4}, 'TN': '230915_092952:cmsbot_crab_20230915_112932', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/5/5'}
```

## Comment (cmsdmwmbot, 2023-09-15T10:58:08Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2023-09-15 12:58:07
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/643/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 12, 'finished': 988}, 'TN': '230915_092924:cmsbot_crab_20230915_112922', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/988/988'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230915_092926:cmsbot_crab_20230915_112925', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230915_092927:cmsbot_crab_20230915_112927', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230915_092929:cmsbot_crab_20230915_112929', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {'failed': 2, 'finished': 98}, 'TN': '230915_092931:cmsbot_crab_20230915_112930', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/98/98'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230915_092952:cmsbot_crab_20230915_112932', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```

## Comment (cmsdmwmbot, 2023-09-15T12:31:02Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2023-09-15 14:31:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/644/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230915_092924:cmsbot_crab_20230915_112922', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230915_092926:cmsbot_crab_20230915_112925', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230915_092927:cmsbot_crab_20230915_112927', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230915_092929:cmsbot_crab_20230915_112929', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230915_092931:cmsbot_crab_20230915_112930', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230915_092952:cmsbot_crab_20230915_112932', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```

## Comment (novicecpp, 2023-09-15T13:01:47Z)

Nice.
