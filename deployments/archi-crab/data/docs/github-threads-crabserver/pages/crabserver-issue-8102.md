# dmwm/CRABServer issue #8102: #620: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-12-15T15:31:31Z
Closed: 2023-12-19T21:16:13Z
URL: https://github.com/dmwm/CRABServer/issues/8102

## Opening post (cmsdmwmbot, 2023-12-15T15:31:31Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2023-12-15 16:31:30
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/620/)

## Comment (cmsdmwmbot, 2023-12-15T15:32:52Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
231215_153150:cmsbot_crab_20231215_163149
231215_153201:cmsbot_crab_20231215_163201
231215_153204:cmsbot_crab_20231215_163203
231215_153206:cmsbot_crab_20231215_163205
231215_153208:cmsbot_crab_20231215_163207
231215_153212:cmsbot_crab_20231215_163209
231215_153215:cmsbot_crab_rucio_transfers_20231215_163213
231215_153217:cmsbot_crab_rucio_transfers_group_20231215_163217
231215_153220:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231215_163219
231215_153224:cmsbot_crab_rucio_transfers_nopublication_20231215_163222
231215_153227:cmsbot_crab_rucio_transfers_withnoneedm_20231215_163225
231215_153230:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231215_163228
```

Finished at: 2023-12-15 16:32:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/620/console)

## Comment (cmsdmwmbot, 2023-12-15T15:57:08Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-12-15 16:57:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/689/console

```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1000}, 'TN': '231215_153150:cmsbot_crab_20231215_163149', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'TN': '231215_153201:cmsbot_crab_20231215_163201', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 1}, 'TN': '231215_153204:cmsbot_crab_20231215_163203', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231215_153206:cmsbot_crab_20231215_163205', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 100}, 'TN': '231215_153208:cmsbot_crab_20231215_163207', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 10}, 'TN': '231215_153212:cmsbot_crab_20231215_163209', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231215_153215:cmsbot_crab_rucio_transfers_20231215_163213', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231215_153217:cmsbot_crab_rucio_transfers_group_20231215_163217', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231215_153220:cmsbot_crab_rucio_transfers_manyedm_nopublication_20231215_163219', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231215_153224:cmsbot_crab_rucio_transfers_nopublication_20231215_163222', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231215_153227:cmsbot_crab_rucio_transfers_withnoneedm_20231215_163225', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'transferring': 40}, 'TN': '231215_153230:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20231215_163228', 'combinedStatus': 'SUBMITTED', 'publication (fail/tdb/DBS)': '0/0/0'}
```
