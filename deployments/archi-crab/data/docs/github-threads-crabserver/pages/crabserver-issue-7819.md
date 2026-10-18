# dmwm/CRABServer issue #7819: #460: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-08-12T15:18:10Z
Closed: 2023-08-14T09:38:35Z
URL: https://github.com/dmwm/CRABServer/issues/7819

## Opening post (cmsdmwmbot, 2023-08-12T15:18:10Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-08-12 17:18:09
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/460/)

## Comment (cmsdmwmbot, 2023-08-12T15:20:06Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230812_151916:cmsbot_crab_20230812_171914
230812_151917:cmsbot_crab_20230812_171917
230812_151919:cmsbot_crab_20230812_171918
230812_151921:cmsbot_crab_20230812_171921
230812_151923:cmsbot_crab_20230812_171922
230812_151945:cmsbot_crab_20230812_171924
```

Finished at: 2023-08-12 17:19:45
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/460/console)

## Comment (cmsdmwmbot, 2023-08-12T15:32:21Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-12 17:32:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/592/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 60, 'transferring': 926, 'running': 14}, 'TN': '230812_151916:cmsbot_crab_20230812_171914', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '60/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 5}, 'TN': '230812_151917:cmsbot_crab_20230812_171917', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230812_151919:cmsbot_crab_20230812_171918', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230812_151921:cmsbot_crab_20230812_171921', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 93}, 'TN': '230812_151923:cmsbot_crab_20230812_171922', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '7/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 4, 'transferring': 6}, 'TN': '230812_151945:cmsbot_crab_20230812_171924', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T15:44:46Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 10. Will run again.
**Finished at:** 2023-08-12 17:44:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/594/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 69, 'transferring': 931}, 'TN': '230812_151916:cmsbot_crab_20230812_171914', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '69/69/69'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230812_151917:cmsbot_crab_20230812_171917', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230812_151919:cmsbot_crab_20230812_171918', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230812_151921:cmsbot_crab_20230812_171921', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 93}, 'TN': '230812_151923:cmsbot_crab_20230812_171922', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '7/7/7'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230812_151945:cmsbot_crab_20230812_171924', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T16:17:04Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 10. Will run again.
**Finished at:** 2023-08-12 18:17:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/596/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230812_151916:cmsbot_crab_20230812_171914', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/969/969'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '230812_151917:cmsbot_crab_20230812_171917', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230812_151919:cmsbot_crab_20230812_171918', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151921:cmsbot_crab_20230812_171921', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230812_151923:cmsbot_crab_20230812_171922', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151945:cmsbot_crab_20230812_171924', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T17:21:10Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 10. Test is done.
**Finished at:** 2023-08-12 19:21:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/598/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230812_151916:cmsbot_crab_20230812_171914', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230812_151917:cmsbot_crab_20230812_171917', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '6/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230812_151919:cmsbot_crab_20230812_171918', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151921:cmsbot_crab_20230812_171921', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230812_151923:cmsbot_crab_20230812_171922', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230812_151945:cmsbot_crab_20230812_171924', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```
