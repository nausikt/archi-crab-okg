# dmwm/CRABServer issue #9378: protect PostJob against being run on old job

State: closed
Opened: 2026-08-07T10:29:45Z
Closed: 2026-08-10T19:32:52Z
Labels: Type: Bug, Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9378

## Opening post (belforte, 2026-08-07T10:29:45Z)

At times Dagman can "loose' the fact that a PostJob process it spawned is completed, and submit the PJ again with same retry number [1]
Currently this make PostJob  to think it is being restart after deferral and plow on, but it fails to update classAd since job left the queue. So it spends O(10) minutes in retrying and eventually crashes w/o any proper logging. This
* slows down Dagman and schedd
* can eat a lot of memory
* creates logs very confusing


[1] here's my analysis of one such event where [postjob.377.4](https://cmsweb.cern.ch/scheddmon/0122/fernance/260806_115656:fernance_crab_GluGluHToDarkShowers-ScenarioA_Par-ctau-0p6-mA-1p67-mpi-5_GENSIM_RAWSIM_HLT2025/postjob.337.4.txt) shows
```text
Thu, 06 Aug 2026 16:06:42 CEST(+0200):INFO:PostJob ********************************************************************************
======== Finished post-job execution with status code 1  : RECOVERABLE JOB FAIL. This jobs will be retried
Ended TaskManagerBootstrap with code 1
Thu, 06 Aug 2026 16:12:00 CEST(+0200):INFO:PostJob 
======== Starting execution again after deferral
Thu, 06 Aug 2026 16:12:00 CEST(+0200):DEBUG:PostJob (Parsed job ad.)
Thu, 06 Aug 2026 16:12:00 CEST(+0200):ERROR:PostJob Invalid job report: missing 'steps'
Thu, 06 Aug 2026 16:12:14 CEST(+0200):ERROR:PostJob Exception in setting job ClassAd attributes:
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/160/0/cluster160730160.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 2908, in set_state_ClassAds
    self.schedd.edit([self.dag_jobid], param, str(params[param]))
[... more errors and tracebacks...]
then it looks like process was killed
Thu, 06 Aug 2026 16:21:37 CEST(+0200):INFO:PostJob 
======== Starting execution again after deferral
Thu, 06 Aug 2026 16:21:37 CEST(+0200):DEBUG:PostJob (Parsed job ad.)
Thu, 06 Aug 2026 16:21:37 CEST(+0200):ERROR:PostJob Invalid job report: missing 'steps'
Thu, 06 Aug 2026 16:21:38 CEST(+0200):ERROR:PostJob Exception in setting job ClassAd attributes:
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/160/0/cluster160730160.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 2908, in set_state_ClassAds
    self.schedd.edit([self.dag_jobid], param, str(params[param]))
[...more errors and tracebaks...]
Thu, 06 Aug 2026 16:32:55 CEST(+0200):ERROR:PostJob Failed to set job ClassAd attributes for 5 times, will not retry. Dashboard may report stale job status/exit-code.
Ended TaskManagerBootstrap with code 2
```

I derived the following timelene(s) and observations from `RunJobs.dag.dagman.out` and PostJob logs.
**Note:** every time dagman restarts it replays old events in the log.
"Spurious" lines from that in the log are like
```
08/06/26 16:08:10 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160732540.0.0) {08/06/26 14:16:56} [recovery mode]
```
which indicates that at 16:08 Dagman notices an event happened 2 hours earlier at 16:16. for job 160732540.0
In order to make sense of things one must ignore `ULOG*` lines which end with `[recovery mode]` **and** the lines which immediately follows with same time stamps which AFAIU report details of that old event while alas have a simpler format like the following which do not indicated e.g. to what condor JobId they refer.
```
08/06/26 16:08:10 Event is okay
08/06/26 16:08:10 Node(Job337)::_Status = STATUS_POSTRUN  
08/06/26 16:08:10 Node(Job337)::SetStatus(STATUS_ERROR    )
```

### Timeline

 ```text
TIMELINE Job337
===================== R 0 ======
13:59:11 PRE spawn
14:08:50 Running POST script of Node Job337...
14:08:50 POST spawn
14:08:57 PJ-0 end
===================== R 1 =======
14:09:45 PRE spawn
14:16:49 Running POST script of Node Job337...
14:16:49 POST spawn
14:16:55 PJ-1 end
===================== R 2 =============
14:19:04 PRE spawn
14:19:20 Event: ULOG_SUBMIT for HTCondor Node Job337 (160734204.0.0)
14:26:17 Running POST script of Node Job337...
14:26:17 POST spawn
14:26:18 PJ-2 DEBUG:PostJob This post-job corresponds to job with Condor ID 160734204.
14:26:21 PJ-2 end
==================== R 3 =============
15:24:39 PRE spawn
15:42:21 Running POST script of Node Job337...
15:42:21 POST spawn
15:42:42 PJ-3 end
====================== R 4 ==========
15:45:56 PRE spawn
15:55:34 Event: ULOG_SUBMIT for HTCondor Node Job337 (160750473.0.0)
15:57:55 Event: ULOG_JOB_TERMINATED for HTCondor Node Job337 (160750473.0.0) {08/06/26 15:57:50}
16:06:27 Running POST script of Node Job337...
16:06:27       spawned pid 1975436: dag_bootstrap.sh
16:06:32 PJ-4 starts for job with Condor ID 160750473.
16:06:42 Finished post-job execution with status code 1  : RECOVERABLE JOB FAIL.
================= DAGMAN RESTART ==================
*******************************************************************************************************
08/06/26 16:06:55 Daemon exiting before all child processes gone; killing 1975436
*** Dagman killed the process which it spawned for PostJob even if it completed 7 seconds earlier !!!
*** this must be why it decided to start the PostJob again at 16:11:56
*** Alas Dagman logs when it spawns processes, but not when it logs their conclusion
********************************************************************************************************
16:06:55 **** condor_dagman (condor_DAGMAN) pid 1400098 EXITING WITH STATUS 3
16:07:59 ** condor_dagman (CONDOR_DAGMAN) STARTING UP
16:08:13 Event: ULOG_JOB_TERMINATED for HTCondor Node Job337 (160750473.0.0) {08/06/26 15:57:50} [recovery mode]
16:08:13 Node Job337 job proc (160750473.0.0) failed with status 195.
16:08:13 Node(Job337)::SetStatus(STATUS_POSTRUN  )
16:11:56 Running POST script of Node Job337...
16:11:56 POST spawn
16:12:00 PJ-4 Starting execution again after deferral
16:12:15 Unable to commit transaction:Modifying attribute CRAB_PostJobStatus in nonexistent job 160750473.0
================= DAGMAN RESTART ==================
16:20:23 **** condor_dagman (condor_DAGMAN) pid 1981527 EXITING WITH STATUS 3
16:21:34 Running POST script of Node Job337...
16:21:34 POST spawn
16:21:37 PJ-4 Starting execution again after deferral
16:21:38 PJ-4 ERROR:PostJob Exception in setting job ClassAd attributes:
16:32:55 PJ-4 ERROR:PostJob Failed to set job ClassAd attributes for 5 times
         Ended TaskManagerBootstrap with code 2
16:32:55 PJ-4 end with code 2 (= DO NOT RETRY ME ANYMORE)
================= DAGMAN RESTART ==================
16:34:07 **** condor_dagman (condor_DAGMAN) pid 2152255 EXITING WITH STATUS 3
================= DAGMAN RESTART ==================
16:48:34 **** condor_dagman (condor_DAGMAN) pid 2284446 EXITING WITH STATUS 3
====================== R 5 =========
16:49:40 PRE spawn
16:49:47 Event: ULOG_SUBMIT for HTCondor Node Job337 (160757211.0.0)
17:03:40 **** condor_dagman (condor_DAGMAN) pid 2380758 EXITING WITH STATUS 3
17:16:11 **** condor_dagman (condor_DAGMAN) pid 2492841 EXITING WITH STATUS 3
17:27:39 **** condor_dagman (condor_DAGMAN) pid 2616192 EXITING WITH STATUS 3
17:39:18 **** condor_dagman (condor_DAGMAN) pid 2704328 EXITING WITH STATUS 3
18:02:05 **** condor_dagman (condor_DAGMAN) pid 2805027 EXITING WITH STATUS 3
18:03:08 ** condor_dagman (CONDOR_DAGMAN) STARTING UP
20:08:09 Node Job337 job proc (160757211.0.0) completed successfully
20:08:09 Running POST script of Node Job337...
20:08:09 POST spawn
20:08:10 PJ-5 starts
20:08:10 DEBUG:PostJob This post-job corresponds to job with Condor ID 160757211.
20:08:13 Deferring POST script of node Job337 for 1800 seconds (exit status was 4)...
================= DAGMAN RESTART ==================
20:09:43 **** condor_dagman (condor_DAGMAN) pid 3002601 EXITING WITH STATUS 3
20:11:01 Deferring POST script of node Job337 for 1800 seconds (exit status was 4)...
================= DAGMAN RESTART ==================
20:20:54 **** condor_dagman (condor_DAGMAN) pid 4037328 EXITING WITH STATUS 3
20:22:03 Running POST script of Node Job337...
20:22:07 Finished post-job execution with status code 0
20:22:07 PJ-5 end
20:22:11 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160757211.0.0)
20:22:11 POST Script of node Job337 completed successfully.
20:22:11 Node(Job337)::SetStatus(STATUS_DONE     )

====  DAGAMAN ENDS SUCCESSFULLY ===========
23:53:26 **** condor_dagman (condor_DAGMAN) pid 4114354 EXITING WITH STATUS 0



SUBMISSIONS TIMELINE EXCLUDING recovery mode
[crabtw@vocms0122 cluster160730160.proc0.subproc0]$ grep Job337  RunJobs.dag.dagman.out |grep ULOG_SUBMIT|grep -v recovery
08/06/26 13:59:40 Event: ULOG_SUBMIT for HTCondor Node Job337 (160730501.0.0) {08/06/26 13:59:34}
08/06/26 14:10:11 Event: ULOG_SUBMIT for HTCondor Node Job337 (160732540.0.0) {08/06/26 14:10:08}
08/06/26 14:19:20 Event: ULOG_SUBMIT for HTCondor Node Job337 (160734204.0.0) {08/06/26 14:19:19}
08/06/26 15:24:49 Event: ULOG_SUBMIT for HTCondor Node Job337 (160745387.0.0) {08/06/26 15:24:49}
08/06/26 15:55:34 Event: ULOG_SUBMIT for HTCondor Node Job337 (160750473.0.0) {08/06/26 15:55:26}
08/06/26 16:49:47 Event: ULOG_SUBMIT for HTCondor Node Job337 (160757211.0.0) {08/06/26 16:49:46}

POST JOB TERMINATION EXCLUDING recovery mode
[crabtw@vocms0122 cluster160730160.proc0.subproc0]$ grep Job337  RunJobs.dag.dagman.out |grep "_POST_SCRIPT_TERMINATED for HTCondor Node Job337"|grep -v recovery
08/06/26 14:09:05 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160730501.0.0) {08/06/26 14:08:57}
08/06/26 14:17:03 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160732540.0.0) {08/06/26 14:16:56}
08/06/26 14:26:23 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160734204.0.0) {08/06/26 14:26:21}
08/06/26 15:43:02 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160745387.0.0) {08/06/26 15:42:49}
08/06/26 16:32:56 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160750473.0.0) {08/06/26 16:32:55}
08/06/26 16:32:56 POST Script of node Job337 failed with status 2
08/06/26 20:22:11 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160757211.0.0) {08/06/26 20:22:07}

INCLUDING PJ STATUS
[crabtw@vocms0122 cluster160730160.proc0.subproc0]$ grep Job337  RunJobs.dag.dagman.out |grep -v recovery|grep "_POST_SCRIPT_TERMINATED for HTCondor Node Job337" -A5
-- R 0
08/06/26 14:09:05 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160730501.0.0) {08/06/26 14:08:57}
08/06/26 14:09:05 Node(Job337)::_Status = STATUS_POSTRUN
08/06/26 14:09:05 Node(Job337)::SetStatus(STATUS_ERROR    )
08/06/26 14:09:05 POST Script of node Job337 failed with status 1
08/06/26 14:09:05 POST for Node Job337 returned 1
08/06/26 14:09:05 Node(Job337)::_Status = STATUS_ERROR
-- R 1
08/06/26 14:17:03 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160732540.0.0) {08/06/26 14:16:56}
08/06/26 14:17:03 Node(Job337)::_Status = STATUS_POSTRUN
08/06/26 14:17:03 Node(Job337)::SetStatus(STATUS_ERROR    )
08/06/26 14:17:03 POST Script of node Job337 failed with status 1
08/06/26 14:17:03 POST for Node Job337 returned 1
08/06/26 14:17:03 Node(Job337)::_Status = STATUS_ERROR
-- R 2
08/06/26 14:26:23 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160734204.0.0) {08/06/26 14:26:21}
08/06/26 14:26:23 Node(Job337)::_Status = STATUS_POSTRUN
08/06/26 14:26:23 Node(Job337)::SetStatus(STATUS_ERROR    )
08/06/26 14:26:23 POST Script of node Job337 failed with status 2
08/06/26 14:26:23 POST for Node Job337 returned 2
08/06/26 14:26:23 Aborting further retries of node Job337 (last attempt returned 2)
-- R 3
08/06/26 15:43:02 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160745387.0.0) {08/06/26 15:42:49}
08/06/26 15:43:02 Node(Job337)::_Status = STATUS_POSTRUN
08/06/26 15:43:02 Node(Job337)::SetStatus(STATUS_ERROR    )
08/06/26 15:43:02 POST Script of node Job337 failed with status 1
08/06/26 15:43:02 POST for Node Job337 returned 1
08/06/26 15:43:02 Node(Job337)::_Status = STATUS_ERROR
-- R 4
08/06/26 16:32:56 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160750473.0.0) {08/06/26 16:32:55}
08/06/26 16:32:56 Node(Job337)::_Status = STATUS_POSTRUN
08/06/26 16:32:56 Node(Job337)::SetStatus(STATUS_ERROR    )
08/06/26 16:32:56 POST Script of node Job337 failed with status 2
08/06/26 16:32:56 POST for Node Job337 returned 2
08/06/26 16:32:56 Aborting further retries of node Job337 (last attempt returned 2)
-- R 5
08/06/26 20:22:11 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job337 (160757211.0.0) {08/06/26 20:22:07}
08/06/26 20:22:11 POST Script of node Job337 completed successfully.
08/06/26 20:22:11 Node(Job337)::_Status = STATUS_POSTRUN
08/06/26 20:22:11 Node(Job337)::SetStatus(STATUS_DONE     )
[crabtw@vocms0122 cluster160730160.proc0.subproc0]$
```

## Comment (belforte, 2026-08-07T10:55:25Z)

PJ should detect the situation and exit with code 2. Telling Dagman to submit a new job.

## Comment (belforte, 2026-08-07T12:57:25Z)

the failing classAd update happens in 
https://github.com/dmwm/CRABServer/blob/cd03a20b880425c44f5140b44be5f10462439367/src/python/TaskWorker/Actions/PostJob.py#L2907-L2931

## Comment (belforte, 2026-08-07T13:03:06Z)

easiest and safest seems to check that `dag_jobid`
https://github.com/dmwm/CRABServer/blob/cd03a20b880425c44f5140b44be5f10462439367/src/python/TaskWorker/Actions/PostJob.py#L1589
is still in the condor queue early on, like here
https://github.com/dmwm/CRABServer/blob/cd03a20b880425c44f5140b44be5f10462439367/src/python/TaskWorker/Actions/PostJob.py#L1620-L1624
with a query like
```python
ads=schedd.query(constraint=f"clusterid=={self.dag_clusterid}")
```
