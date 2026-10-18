# dmwm/CRABServer issue #8876: #922: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2025-01-09T14:45:20Z
Closed: 2025-01-09T17:03:40Z
URL: https://github.com/dmwm/CRABServer/issues/8876

## Opening post (cmsdmwmbot, 2025-01-09T14:45:20Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Task_Submission_Status_Tracking

Started at: 2025-01-09 15:45:19
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/922/)

## Comment (cmsdmwmbot, 2025-01-09T14:49:05Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
250109_144722:cmsbot_crab_20250109_154718
250109_144734:cmsbot_crab_20250109_154724
250109_144738:cmsbot_crab_20250109_154736
250109_144741:cmsbot_crab_20250109_154739
250109_144744:cmsbot_crab_20250109_154743
250109_144819:cmsbot_crab_20250109_154746
250109_144823:cmsbot_crab_rucio_transfers_20250109_154821
250109_144827:cmsbot_crab_rucio_transfers_group_20250109_154825
250109_144831:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250109_154829
250109_144835:cmsbot_crab_rucio_transfers_nopublication_20250109_154833
250109_144839:cmsbot_crab_rucio_transfers_withnoneedm_20250109_154837
250109_144843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250109_154841
```

Finished at: 2025-01-09 15:48:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/922/console)

## Comment (cmsdmwmbot, 2025-01-09T15:11:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2025-01-09 16:11:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1138/console

```
{'TN': '250109_144722:cmsbot_crab_20250109_154718', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 977, 'finished': 14, 'running': 9}, 'publication (fail/tdb/DBS)': '0/14/14'}
{'TN': '250109_144734:cmsbot_crab_20250109_154724', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144738:cmsbot_crab_20250109_154736', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144741:cmsbot_crab_20250109_154739', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144744:cmsbot_crab_20250109_154743', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 99, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144819:cmsbot_crab_20250109_154746', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144823:cmsbot_crab_rucio_transfers_20250109_154821', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144827:cmsbot_crab_rucio_transfers_group_20250109_154825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 40}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144831:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250109_154829', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144835:cmsbot_crab_rucio_transfers_nopublication_20250109_154833', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144839:cmsbot_crab_rucio_transfers_withnoneedm_20250109_154837', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250109_154841', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2025-01-09T15:28:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2025-01-09 16:28:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1139/console

```
{'TN': '250109_144722:cmsbot_crab_20250109_154718', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 959, 'transferring': 39, 'running': 2}, 'publication (fail/tdb/DBS)': '0/14/14'}
{'TN': '250109_144734:cmsbot_crab_20250109_154724', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144738:cmsbot_crab_20250109_154736', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144741:cmsbot_crab_20250109_154739', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144744:cmsbot_crab_20250109_154743', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 95, 'transferring': 4, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144819:cmsbot_crab_20250109_154746', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'transferring': 6, 'finished': 4}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144823:cmsbot_crab_rucio_transfers_20250109_154821', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144827:cmsbot_crab_rucio_transfers_group_20250109_154825', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 38, 'transferring': 2}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144831:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250109_154829', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144835:cmsbot_crab_rucio_transfers_nopublication_20250109_154833', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144839:cmsbot_crab_rucio_transfers_withnoneedm_20250109_154837', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250109_154841', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2025-01-09T16:14:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2025-01-09 17:14:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1140/console

```
{'TN': '250109_144722:cmsbot_crab_20250109_154718', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 998, 'transferring': 1, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/998/998'}
{'TN': '250109_144734:cmsbot_crab_20250109_154724', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 5, 'failed': 1, 'running': 1}, 'publication (fail/tdb/DBS)': '0/0/0'}
{'TN': '250109_144738:cmsbot_crab_20250109_154736', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250109_144741:cmsbot_crab_20250109_154739', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250109_144744:cmsbot_crab_20250109_154743', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'SUBMITTED', 'jobsPerStatus': {'finished': 99, 'transferring': 1}, 'publication (fail/tdb/DBS)': '0/99/99'}
{'TN': '250109_144819:cmsbot_crab_20250109_154746', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250109_144823:cmsbot_crab_rucio_transfers_20250109_154821', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144827:cmsbot_crab_rucio_transfers_group_20250109_154825', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '250109_144831:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250109_154829', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144835:cmsbot_crab_rucio_transfers_nopublication_20250109_154833', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144839:cmsbot_crab_rucio_transfers_withnoneedm_20250109_154837', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250109_154841', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (belforte, 2025-01-09T16:36:36Z)

pff... we ran out of Rucio quota at CERN
		Not enough Rucio quota at T2_CH_CERN:/store/user/rucio/cmsbot/ruciotransfers-1736434117. Remain quota: 0.8747176099568605 GB.

## Comment (belforte, 2025-01-09T16:57:05Z)

I can not authenticate as `cmsbot` but `crab_tape_recall` Rucio account has superpowers and can delete those rules.

## Comment (belforte, 2025-01-09T17:03:27Z)

anyhow this is fine as test of HTC 24.3.0 on TW

## Comment (cmsdmwmbot, 2025-01-09T17:47:00Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2025-01-09 18:46:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1141/console

```
{'TN': '250109_144722:cmsbot_crab_20250109_154718', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '250109_144734:cmsbot_crab_20250109_154724', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250109_144738:cmsbot_crab_20250109_154736', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250109_144741:cmsbot_crab_20250109_154739', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250109_144744:cmsbot_crab_20250109_154743', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250109_144819:cmsbot_crab_20250109_154746', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250109_144823:cmsbot_crab_rucio_transfers_20250109_154821', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144827:cmsbot_crab_rucio_transfers_group_20250109_154825', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '250109_144831:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250109_154829', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144835:cmsbot_crab_rucio_transfers_nopublication_20250109_154833', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144839:cmsbot_crab_rucio_transfers_withnoneedm_20250109_154837', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250109_154841', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2025-01-09T19:49:04Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2025-01-09 20:49:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1142/console

```
{'TN': '250109_144722:cmsbot_crab_20250109_154718', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '250109_144734:cmsbot_crab_20250109_154724', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250109_144738:cmsbot_crab_20250109_154736', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250109_144741:cmsbot_crab_20250109_154739', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250109_144744:cmsbot_crab_20250109_154743', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250109_144819:cmsbot_crab_20250109_154746', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250109_144823:cmsbot_crab_rucio_transfers_20250109_154821', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144827:cmsbot_crab_rucio_transfers_group_20250109_154825', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '250109_144831:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250109_154829', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144835:cmsbot_crab_rucio_transfers_nopublication_20250109_154833', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144839:cmsbot_crab_rucio_transfers_withnoneedm_20250109_154837', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250109_154841', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2025-01-09T21:51:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2025-01-09 22:51:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/1143/console

```
{'TN': '250109_144722:cmsbot_crab_20250109_154718', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1000}, 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'TN': '250109_144734:cmsbot_crab_20250109_154724', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 6, 'failed': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250109_144738:cmsbot_crab_20250109_154736', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1}, 'publication (fail/tdb/DBS)': '0/1/1'}
{'TN': '250109_144741:cmsbot_crab_20250109_154739', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250109_144744:cmsbot_crab_20250109_154743', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 100}, 'publication (fail/tdb/DBS)': '0/100/100'}
{'TN': '250109_144819:cmsbot_crab_20250109_154746', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 10}, 'publication (fail/tdb/DBS)': '0/10/10'}
{'TN': '250109_144823:cmsbot_crab_rucio_transfers_20250109_154821', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144827:cmsbot_crab_rucio_transfers_group_20250109_154825', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 40}, 'publication (fail/tdb/DBS)': '0/40/40'}
{'TN': '250109_144831:cmsbot_crab_rucio_transfers_manyedm_nopublication_20250109_154829', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144835:cmsbot_crab_rucio_transfers_nopublication_20250109_154833', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144839:cmsbot_crab_rucio_transfers_withnoneedm_20250109_154837', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '250109_144843:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20250109_154841', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITREFUSED', 'combinedStatus': 'SUBMITREFUSED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```
