# dmwm/CRABServer issue #7818: #459: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2023-08-12T15:15:40Z
Closed: 2023-08-14T09:38:35Z
URL: https://github.com/dmwm/CRABServer/issues/7818

## Opening post (cmsdmwmbot, 2023-08-12T15:15:40Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-08-12 17:15:39
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/459/)

## Comment (cmsdmwmbot, 2023-08-12T15:17:59Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230812_151712:cmsbot_crab_20230812_171705
230812_151717:cmsbot_crab_20230812_171713
230812_151721:cmsbot_crab_20230812_171717
230812_151726:cmsbot_crab_20230812_171722
230812_151731:cmsbot_crab_20230812_171727
230812_151738:cmsbot_crab_20230812_171731
```

Finished at: 2023-08-12 17:17:38
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/459/console)

## Comment (cmsdmwmbot, 2023-08-12T15:30:15Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-12 17:30:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/591/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '230812_151712:cmsbot_crab_20230812_171705', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 4, 'running': 1}, 'TN': '230812_151717:cmsbot_crab_20230812_171713', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '4/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230812_151721:cmsbot_crab_20230812_171717', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230812_151726:cmsbot_crab_20230812_171722', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '230812_151731:cmsbot_crab_20230812_171727', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 9}, 'TN': '230812_151738:cmsbot_crab_20230812_171731', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T15:42:32Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 10. Will run again.
**Finished at:** 2023-08-12 17:42:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/593/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '230812_151712:cmsbot_crab_20230812_171705', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'TN': '230812_151717:cmsbot_crab_20230812_171713', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230812_151721:cmsbot_crab_20230812_171717', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230812_151726:cmsbot_crab_20230812_171722', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '230812_151731:cmsbot_crab_20230812_171727', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230812_151738:cmsbot_crab_20230812_171731', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T16:14:49Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 10. Will run again.
**Finished at:** 2023-08-12 18:14:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/595/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230812_151712:cmsbot_crab_20230812_171705', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230812_151717:cmsbot_crab_20230812_171713', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230812_151721:cmsbot_crab_20230812_171717', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151726:cmsbot_crab_20230812_171722', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230812_151731:cmsbot_crab_20230812_171727', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151738:cmsbot_crab_20230812_171731', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T17:19:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 10. Will run again.
**Finished at:** 2023-08-12 19:19:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/597/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230812_151712:cmsbot_crab_20230812_171705', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '230812_151717:cmsbot_crab_20230812_171713', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230812_151721:cmsbot_crab_20230812_171717', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151726:cmsbot_crab_20230812_171722', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230812_151731:cmsbot_crab_20230812_171727', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151738:cmsbot_crab_20230812_171731', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T19:03:06Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 4 out of 10. Test is done.
**Finished at:** 2023-08-12 21:03:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/599/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230812_151712:cmsbot_crab_20230812_171705', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230812_151717:cmsbot_crab_20230812_171713', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '6/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230812_151721:cmsbot_crab_20230812_171717', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151726:cmsbot_crab_20230812_171722', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230812_151731:cmsbot_crab_20230812_171727', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151738:cmsbot_crab_20230812_171731', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```
