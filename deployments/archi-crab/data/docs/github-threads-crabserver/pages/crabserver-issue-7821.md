# dmwm/CRABServer issue #7821: #461: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-08-14T12:00:22Z
Closed: 2023-08-14T12:32:50Z
URL: https://github.com/dmwm/CRABServer/issues/7821

## Opening post (cmsdmwmbot, 2023-08-14T12:00:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-08-14 14:00:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/461/)

## Comment (cmsdmwmbot, 2023-08-14T12:01:15Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230814_120041:cmsbot_crab_20230814_140040
230814_120044:cmsbot_crab_20230814_140043
230814_120046:cmsbot_crab_20230814_140045
230814_120048:cmsbot_crab_20230814_140047
230814_120050:cmsbot_crab_20230814_140049
230814_120053:cmsbot_crab_20230814_140051
```

Finished at: 2023-08-14 14:00:54
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/461/console)

## Comment (cmsdmwmbot, 2023-08-14T12:15:09Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-14 14:15:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/600/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 45, 'transferring': 952, 'finished': 3}, 'TN': '230814_120041:cmsbot_crab_20230814_140040', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '3/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 5}, 'TN': '230814_120044:cmsbot_crab_20230814_140043', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230814_120046:cmsbot_crab_20230814_140045', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230814_120048:cmsbot_crab_20230814_140047', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 3, 'transferring': 97}, 'TN': '230814_120050:cmsbot_crab_20230814_140049', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 7, 'transferring': 3}, 'TN': '230814_120053:cmsbot_crab_20230814_140051', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-14T12:27:30Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 10. Something went wrong. Investigate manually.
**Finished at:** 2023-08-14 14:27:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/603/console

```

```

## Comment (belforte, 2023-08-14T12:32:50Z)

aborted intentionally
