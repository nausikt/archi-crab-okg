# dmwm/CRABServer issue #8092: #615: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-12-08T19:29:23Z
Closed: 2023-12-11T19:18:58Z
URL: https://github.com/dmwm/CRABServer/issues/8092

## Opening post (cmsdmwmbot, 2023-12-08T19:29:23Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-12-08 20:29:22
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/615/)

## Comment (cmsdmwmbot, 2023-12-08T19:31:11Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
231208_193004:cmsbot_crab_20231208_203001
231208_193006:cmsbot_crab_20231208_203006
231208_193009:cmsbot_crab_20231208_203008
231208_193011:cmsbot_crab_20231208_203010
231208_193013:cmsbot_crab_20231208_203012
231208_193031:cmsbot_crab_20231208_203015
231208_193035:cmsbot_crab_rucio_transfers_20231208_203033
231208_193037:cmsbot_crab_rucio_transfers_group_20231208_203037
231208_193040:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231208_203039
231208_193044:cmsbot_crab_rucio_transfers_nopublication_20231208_203042
231208_193047:cmsbot_crab_rucio_transfers_withnoneedm_20231208_203045
231208_193050:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231208_203048
```

Finished at: 2023-12-08 20:30:50
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/615/console)

## Comment (cmsdmwmbot, 2023-12-08T19:54:54Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-08 20:54:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/680/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '231208_193004:cmsbot_crab_20231208_203001', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'idle': 1}, 'TN': '231208_193006:cmsbot_crab_20231208_203006', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '231208_193009:cmsbot_crab_20231208_203008', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231208_193011:cmsbot_crab_20231208_203010', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '231208_193013:cmsbot_crab_20231208_203012', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'running': 3, 'transferring': 7}, 'TN': '231208_193031:cmsbot_crab_20231208_203015', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231208_193035:cmsbot_crab_rucio_transfers_20231208_203033', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231208_193037:cmsbot_crab_rucio_transfers_group_20231208_203037', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231208_193040:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231208_203039', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231208_193044:cmsbot_crab_rucio_transfers_nopublication_20231208_203042', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231208_193047:cmsbot_crab_rucio_transfers_withnoneedm_20231208_203045', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231208_193050:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231208_203048', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (cmsdmwmbot, 2023-12-08T20:12:02Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 1 out of 5. Something went wrong. Investigate manually.
**Finished at:** 2023-12-08 21:12:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/681/console

```

```
