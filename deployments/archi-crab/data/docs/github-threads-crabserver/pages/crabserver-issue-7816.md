# dmwm/CRABServer issue #7816: #458: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2023-08-11T23:04:52Z
Closed: 2023-08-14T09:38:14Z
URL: https://github.com/dmwm/CRABServer/issues/7816

## Opening post (cmsdmwmbot, 2023-08-11T23:04:52Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2023-08-12 01:04:51
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/458/)

## Comment (cmsdmwmbot, 2023-08-11T23:07:16Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230811_230624:cmsbot_crab_20230812_010616
230811_230629:cmsbot_crab_20230812_010625
230811_230634:cmsbot_crab_20230812_010630
230811_230639:cmsbot_crab_20230812_010635
230811_230642:cmsbot_crab_20230812_010639
230811_230655:cmsbot_crab_20230812_010643
```

Finished at: 2023-08-12 01:06:55
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/458/console)

## Comment (cmsdmwmbot, 2023-08-11T23:14:27Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 0 out of 4. Something went wrong. Investigate manually.
**Finished at:** 2023-08-12 01:14:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/548/console

```

```

## Comment (cmsdmwmbot, 2023-08-11T23:28:26Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 0. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-08-12 01:28:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/549/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 1, 'transferring': 9}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T23:32:32Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-08-12 01:32:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/550/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T23:35:34Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 20. Will run again.
**Finished at:** 2023-08-12 01:35:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/551/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T23:39:44Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 20. Will run again.
**Finished at:** 2023-08-12 01:39:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/552/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T23:42:41Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 20. Will run again.
**Finished at:** 2023-08-12 01:42:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/553/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T23:46:53Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 20. Will run again.
**Finished at:** 2023-08-12 01:46:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/554/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 988, 'transferring': 12}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '988/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T23:49:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 20. Will run again.
**Finished at:** 2023-08-12 01:49:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/555/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 999, 'transferring': 1}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '999/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '7/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T23:54:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 20. Will run again.
**Finished at:** 2023-08-12 01:54:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/556/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 7, 'transferring': 3}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '7/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-11T23:57:06Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 20. Will run again.
**Finished at:** 2023-08-12 01:57:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/557/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 9, 'transferring': 1}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '9/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:01:14Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 20. Will run again.
**Finished at:** 2023-08-12 02:01:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/558/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:04:20Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 6 out of 20. Will run again.
**Finished at:** 2023-08-12 02:04:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/559/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/0/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:08:27Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 20. Will run again.
**Finished at:** 2023-08-12 02:08:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/560/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/0/500'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:11:31Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 7 out of 20. Will run again.
**Finished at:** 2023-08-12 02:11:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/561/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:15:44Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 6 out of 20. Will run again.
**Finished at:** 2023-08-12 02:15:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/562/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:18:44Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 8 out of 20. Will run again.
**Finished at:** 2023-08-12 02:18:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/563/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:22:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 7 out of 20. Will run again.
**Finished at:** 2023-08-12 02:22:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/564/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:25:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 9 out of 20. Will run again.
**Finished at:** 2023-08-12 02:25:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/565/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:30:13Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 8 out of 20. Will run again.
**Finished at:** 2023-08-12 02:30:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/566/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:33:19Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 10 out of 20. Will run again.
**Finished at:** 2023-08-12 02:33:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/567/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:37:25Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 9 out of 20. Will run again.
**Finished at:** 2023-08-12 02:37:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/568/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:40:28Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 11 out of 20. Will run again.
**Finished at:** 2023-08-12 02:40:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/569/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:44:39Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 10 out of 20. Will run again.
**Finished at:** 2023-08-12 02:44:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/570/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:47:38Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 12 out of 20. Will run again.
**Finished at:** 2023-08-12 02:47:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/571/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:51:50Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 11 out of 20. Will run again.
**Finished at:** 2023-08-12 02:51:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/572/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:54:53Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 13 out of 20. Will run again.
**Finished at:** 2023-08-12 02:54:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/573/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T00:59:01Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 12 out of 20. Will run again.
**Finished at:** 2023-08-12 02:59:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/574/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:02:04Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 14 out of 20. Will run again.
**Finished at:** 2023-08-12 03:02:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/575/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:06:16Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 13 out of 20. Will run again.
**Finished at:** 2023-08-12 03:06:15
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/576/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:09:15Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 15 out of 20. Will run again.
**Finished at:** 2023-08-12 03:09:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/577/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:13:23Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 14 out of 20. Will run again.
**Finished at:** 2023-08-12 03:13:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/578/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:16:30Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 16 out of 20. Will run again.
**Finished at:** 2023-08-12 03:16:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/579/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:20:35Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 15 out of 20. Will run again.
**Finished at:** 2023-08-12 03:20:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/580/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:23:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 17 out of 20. Will run again.
**Finished at:** 2023-08-12 03:23:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/581/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:27:46Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 16 out of 20. Will run again.
**Finished at:** 2023-08-12 03:27:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/582/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:30:52Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 18 out of 20. Will run again.
**Finished at:** 2023-08-12 03:30:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/583/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:34:59Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 17 out of 20. Will run again.
**Finished at:** 2023-08-12 03:34:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/584/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:38:01Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 19 out of 20. Will run again.
**Finished at:** 2023-08-12 03:37:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/585/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:42:11Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 18 out of 20. Will run again.
**Finished at:** 2023-08-12 03:42:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/586/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:45:10Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 20 out of 20. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-08-12 03:45:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/587/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/0'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:49:22Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 19 out of 20. Will run again.
**Finished at:** 2023-08-12 03:49:21
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/588/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T01:57:58Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 20 out of 20. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-08-12 03:57:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/589/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'SUBMITTED', 'publication (f/t/D)': '5/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```

## Comment (cmsdmwmbot, 2023-08-12T15:21:00Z)

**Test:** Task Submission Status Tracking
**Result:** SUCCEEDED
**Attempt:** 20 out of 0. Test is done.
**Finished at:** 2023-08-12 17:20:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/590/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230811_230624:cmsbot_crab_20230812_010616', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1000/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 6}, 'TN': '230811_230629:cmsbot_crab_20230812_010625', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '6/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230811_230634:cmsbot_crab_20230812_010630', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '1/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230639:cmsbot_crab_20230812_010635', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230811_230642:cmsbot_crab_20230812_010639', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '100/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230811_230655:cmsbot_crab_20230812_010643', 'combinedStatus': 'COMPLETED', 'publication (f/t/D)': '10/10/10'}
```
