# dmwm/CRABServer issue #8241: #711: Test prod CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2024-02-16T14:01:08Z
Closed: 2024-02-18T17:24:25Z
URL: https://github.com/dmwm/CRABServer/issues/8241

## Opening post (cmsdmwmbot, 2024-02-16T14:01:08Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [ ] Task_Submission_Status_Tracking

Started at: 2024-02-16 15:01:07
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/711/)

## Comment (cmsdmwmbot, 2024-02-16T14:02:35Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240216_140128:cmsbot_crab_20240216_150125
240216_140129:cmsbot_crab_20240216_150128
240216_140130:cmsbot_crab_20240216_150129
240216_140130:cmsbot_crab_20240216_150130
240216_140131:cmsbot_crab_20240216_150131
240216_140203:cmsbot_crab_20240216_150132
240216_140205:cmsbot_crab_rucio_transfers_20240216_150203
240216_140206:cmsbot_crab_rucio_transfers_group_20240216_150205
240216_140208:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150206
240216_140210:cmsbot_crab_rucio_transfers_nopublication_20240216_150208
240216_140212:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150210
240216_140214:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150212
```

Finished at: 2024-02-16 15:02:14
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/711/console)

## Comment (cmsdmwmbot, 2024-02-16T14:24:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-16 15:24:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/760/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140128:cmsbot_crab_20240216_150125', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140129:cmsbot_crab_20240216_150128', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150129', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150130', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140131:cmsbot_crab_20240216_150131', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140203:cmsbot_crab_20240216_150132', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140205:cmsbot_crab_rucio_transfers_20240216_150203', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140206:cmsbot_crab_rucio_transfers_group_20240216_150205', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140208:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150206', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140210:cmsbot_crab_rucio_transfers_nopublication_20240216_150208', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140212:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150210', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140214:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150212', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T14:40:02Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-02-16 15:40:01
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/762/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140128:cmsbot_crab_20240216_150125', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140129:cmsbot_crab_20240216_150128', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150129', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150130', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140131:cmsbot_crab_20240216_150131', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140203:cmsbot_crab_20240216_150132', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140205:cmsbot_crab_rucio_transfers_20240216_150203', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140206:cmsbot_crab_rucio_transfers_group_20240216_150205', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140208:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150206', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140210:cmsbot_crab_rucio_transfers_nopublication_20240216_150208', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140212:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150210', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140214:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150212', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T15:26:01Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-02-16 16:26:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/764/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140128:cmsbot_crab_20240216_150125', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140129:cmsbot_crab_20240216_150128', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150129', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150130', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140131:cmsbot_crab_20240216_150131', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140203:cmsbot_crab_20240216_150132', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140205:cmsbot_crab_rucio_transfers_20240216_150203', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140206:cmsbot_crab_rucio_transfers_group_20240216_150205', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140208:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150206', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140210:cmsbot_crab_rucio_transfers_nopublication_20240216_150208', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140212:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150210', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140214:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150212', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T16:57:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-02-16 17:56:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/766/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140128:cmsbot_crab_20240216_150125', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140129:cmsbot_crab_20240216_150128', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150129', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150130', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140131:cmsbot_crab_20240216_150131', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140203:cmsbot_crab_20240216_150132', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140205:cmsbot_crab_rucio_transfers_20240216_150203', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140206:cmsbot_crab_rucio_transfers_group_20240216_150205', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140208:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150206', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140210:cmsbot_crab_rucio_transfers_nopublication_20240216_150208', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140212:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150210', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140214:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150212', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T18:58:44Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-02-16 19:58:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/768/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140128:cmsbot_crab_20240216_150125', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140129:cmsbot_crab_20240216_150128', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150129', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150130', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140131:cmsbot_crab_20240216_150131', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140203:cmsbot_crab_20240216_150132', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140205:cmsbot_crab_rucio_transfers_20240216_150203', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140206:cmsbot_crab_rucio_transfers_group_20240216_150205', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140208:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150206', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140210:cmsbot_crab_rucio_transfers_nopublication_20240216_150208', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140212:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150210', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140214:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150212', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-02-16T21:00:57Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-02-16 22:00:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/770/console

```
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140128:cmsbot_crab_20240216_150125', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140129:cmsbot_crab_20240216_150128', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150129', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140130:cmsbot_crab_20240216_150130', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140131:cmsbot_crab_20240216_150131', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140203:cmsbot_crab_20240216_150132', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140205:cmsbot_crab_rucio_transfers_20240216_150203', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140206:cmsbot_crab_rucio_transfers_group_20240216_150205', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140208:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240216_150206', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140210:cmsbot_crab_rucio_transfers_nopublication_20240216_150208', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140212:cmsbot_crab_rucio_transfers_withnoneedm_20240216_150210', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
{'dbStatus': u'SUBMITFAILED', 'testResult': 'TestResubmitted', 'jobsPerStatus': {}, 'TN': '240216_140214:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240216_150212', 'combinedStatus': u'SUBMITFAILED', 'publication (fail/tdb/DBS)': 'None'}
```
