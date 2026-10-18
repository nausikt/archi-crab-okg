# dmwm/CRABServer issue #7947: #515: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-10-13T23:07:12Z
Closed: 2023-10-14T08:48:17Z
URL: https://github.com/dmwm/CRABServer/issues/7947

## Opening post (cmsdmwmbot, 2023-10-13T23:07:12Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2023-10-14 01:07:11
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/515/)

## Comment (cmsdmwmbot, 2023-10-13T23:08:22Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
231013_230731:cmsbot_crab_20231014_010730
231013_230733:cmsbot_crab_20231014_010732
231013_230735:cmsbot_crab_20231014_010734
231013_230737:cmsbot_crab_20231014_010736
231013_230739:cmsbot_crab_20231014_010738
231013_230801:cmsbot_crab_20231014_010740
```

Finished at: 2023-10-14 01:08:01
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/515/console)

## Comment (cmsdmwmbot, 2023-10-13T23:31:16Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-10-14 01:31:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/661/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 26, 'transferring': 974}, 'TN': '231013_230731:cmsbot_crab_20231014_010730', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '231013_230733:cmsbot_crab_20231014_010732', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '231013_230735:cmsbot_crab_20231014_010734', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231013_230737:cmsbot_crab_20231014_010736', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 2, 'transferring': 98}, 'TN': '231013_230739:cmsbot_crab_20231014_010738', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231013_230801:cmsbot_crab_20231014_010740', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-10-13T23:48:56Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2023-10-14 01:48:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/662/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 921, 'transferring': 79}, 'TN': '231013_230731:cmsbot_crab_20231014_010730', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/26/26'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '231013_230733:cmsbot_crab_20231014_010732', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1}, 'TN': '231013_230735:cmsbot_crab_20231014_010734', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 10}, 'TN': '231013_230737:cmsbot_crab_20231014_010736', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 91, 'transferring': 9}, 'TN': '231013_230739:cmsbot_crab_20231014_010738', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/2/2'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1, 'transferring': 9}, 'TN': '231013_230801:cmsbot_crab_20231014_010740', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-10-14T00:36:32Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2023-10-14 02:36:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/663/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 1000}, 'TN': '231013_230731:cmsbot_crab_20231014_010730', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/926/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'transferring': 1}, 'TN': '231013_230733:cmsbot_crab_20231014_010732', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '231013_230735:cmsbot_crab_20231014_010734', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231013_230737:cmsbot_crab_20231014_010736', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231013_230739:cmsbot_crab_20231014_010738', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231013_230801:cmsbot_crab_20231014_010740', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```

## Comment (cmsdmwmbot, 2023-10-14T02:09:03Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 3 out of 5. Test is done.
**Finished at:** 2023-10-14 04:09:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/664/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '231013_230731:cmsbot_crab_20231014_010730', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '231013_230733:cmsbot_crab_20231014_010732', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '231013_230735:cmsbot_crab_20231014_010734', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231013_230737:cmsbot_crab_20231014_010736', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '231013_230739:cmsbot_crab_20231014_010738', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '231013_230801:cmsbot_crab_20231014_010740', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
```
