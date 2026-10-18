# dmwm/CRABServer issue #7898: #476: Test GH CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-10-06T16:49:02Z
Closed: 2023-10-09T14:30:27Z
URL: https://github.com/dmwm/CRABServer/issues/7898

## Opening post (cmsdmwmbot, 2023-10-06T16:49:02Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2023-10-06 18:49:01
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/476/)

## Comment (cmsdmwmbot, 2023-10-06T16:49:53Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
231006_164921:cmsbot_crab_20231006_184921
231006_164923:cmsbot_crab_20231006_184923
231006_164925:cmsbot_crab_20231006_184924
231006_164927:cmsbot_crab_20231006_184926
231006_164928:cmsbot_crab_20231006_184928
231006_164932:cmsbot_crab_20231006_184929
```

Finished at: 2023-10-06 18:49:32
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/476/console)

## Comment (cmsdmwmbot, 2023-10-06T17:14:16Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-10-06 19:14:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/653/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 62, 'transferring': 827, 'finished': 111}, 'TN': '231006_164921:cmsbot_crab_20231006_184921', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '231006_164923:cmsbot_crab_20231006_184923', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1}, 'TN': '231006_164925:cmsbot_crab_20231006_184924', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 9}, 'TN': '231006_164927:cmsbot_crab_20231006_184926', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 13, 'transferring': 87}, 'TN': '231006_164928:cmsbot_crab_20231006_184928', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/8/8'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 9}, 'TN': '231006_164932:cmsbot_crab_20231006_184929', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-10-06T17:32:33Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2023-10-06 19:32:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/654/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 902, 'transferring': 97, 'running': 1}, 'TN': '231006_164921:cmsbot_crab_20231006_184921', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/900/900'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '231006_164923:cmsbot_crab_20231006_184923', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '231006_164925:cmsbot_crab_20231006_184924', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'TN': '231006_164927:cmsbot_crab_20231006_184926', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/9/9'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231006_164928:cmsbot_crab_20231006_184928', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/98/98'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'TN': '231006_164932:cmsbot_crab_20231006_184929', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/7/7'}
```

## Comment (cmsdmwmbot, 2023-10-06T18:20:28Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2023-10-06 20:20:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/655/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'TN': '231006_164921:cmsbot_crab_20231006_184921', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/998/998'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '231006_164923:cmsbot_crab_20231006_184923', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '231006_164925:cmsbot_crab_20231006_184924', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231006_164927:cmsbot_crab_20231006_184926', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231006_164928:cmsbot_crab_20231006_184928', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231006_164932:cmsbot_crab_20231006_184929', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/9/9'}
```

## Comment (cmsdmwmbot, 2023-10-06T19:53:21Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2023-10-06 21:53:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/656/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '231006_164921:cmsbot_crab_20231006_184921', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '231006_164923:cmsbot_crab_20231006_184923', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '231006_164925:cmsbot_crab_20231006_184924', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231006_164927:cmsbot_crab_20231006_184926', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231006_164928:cmsbot_crab_20231006_184928', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231006_164932:cmsbot_crab_20231006_184929', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```
