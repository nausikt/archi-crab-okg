# dmwm/CRABServer issue #9399: Rucio ASO fails to flag a file as transferred in filetransfersdb

State: closed
Opened: 2026-08-25T15:44:50Z
Closed: 2026-08-26T15:09:19Z
Labels: Type: Bug, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9399

## Opening post (belforte, 2026-08-25T15:44:50Z)

I have hit this problem with task https://cmsweb-testbed.cern.ch/crabserver/ui/task/260819_222955%3Acrabint1_crab_rucio_transfers_group_20260820_002954

Task has 10 jobs, all completed quickly, 9 were also xferred soon, while one (`output_10.root`) took several days. Now it all done and rule is OK.

ASO-Rucio created 3 blocks
```
belforte@lxplus810/crabint1> rucio list-content  group.crab_test:/GenericTTbar/rucio-ruciotransfers-1787178594-94ba0e06145abd65ccb1d21786dc7e1d/USER 
+------------------------------------------------------------------------------------------------------------------------------------------+--------------+
| SCOPE:NAME                                                                                                                               | [DID TYPE]   |
|------------------------------------------------------------------------------------------------------------------------------------------+--------------|
| group.crab_test:/GenericTTbar/rucio-ruciotransfers-1787178594-94ba0e06145abd65ccb1d21786dc7e1d/USER#2f117cad-374b-40d6-9193-8e7cafbabef8 | DATASET      |
| group.crab_test:/GenericTTbar/rucio-ruciotransfers-1787178594-94ba0e06145abd65ccb1d21786dc7e1d/USER#b4ddcf27-fc10-48d7-8c43-4c9213578ecd | DATASET      |
| group.crab_test:/GenericTTbar/rucio-ruciotransfers-1787178594-94ba0e06145abd65ccb1d21786dc7e1d/USER#e12b70a6-6609-4f33-8bfe-7ff2aedb97be | DATASET      |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------+
belforte@lxplus810/crabint1> 
```
one (`b97be` ) has 8 files, one (`78ecd`) has just `output_3` and `babef8` has just `output_10`

Looking at bookkeeping files in   `/home/grid/crabint1/260819_222955:crabint1_crab_rucio_transfers_group_20260820_002954/SPOOL_DIR/task_process/transfers` everything seems done
```
              lfn2pfn_map.json       
[crabtw@vocms059 transfers]$ cat transfer_ok.txt 
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_1.root
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_2.root
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_4.root
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_5.root
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_6.root
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_7.root
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_8.root
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_9.root
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_3.root
/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_10.root
[crabtw@vocms059 transfers]$ 
```
```
13[crabtw@vocms059 transfers]$ cat block_complete.txt 
/GenericTTbar/rucio-ruciotransfers-1787178594-94ba0e06145abd65ccb1d21786dc7e1d/USER#e12b70a6-6609-4f33-8bfe-7ff2aedb97be
/GenericTTbar/rucio-ruciotransfers-1787178594-94ba0e06145abd65ccb1d21786dc7e1d/USER#b4ddcf27-fc10-48d7-8c43-4c9213578ecd
/GenericTTbar/rucio-ruciotransfers-1787178594-94ba0e06145abd65ccb1d21786dc7e1d/USER#2f117cad-374b-40d6-9193-8e7cafbabef8
[crabtw@vocms059 transfers]$ 
```
etc,
But in CRAB DB `filetranasfersdb` table the entry for job 10 is

<img width="1086" height="788" alt="Image" src="https://github.com/user-attachments/assets/430b511c-72d6-4bf6-91b2-cd7cb842b3cf" />

so the fille appears still in transfer

<img width="1053" height="554" alt="Image" src="https://github.com/user-attachments/assets/e00bce2f-b48b-46d7-b28c-4b7a2fff3c91" />

PostJob is still running, crab status show job 10 as still transferring etc.

**when ASO-Rucio detected the transfer OK for this last file, it failed to update Oracle DB** 😭 

From a first quick look at `/home/grid/crabint1/260819_222955:crabint1_crab_rucio_transfers_group_20260820_002954/SPOOL_DIR/task_process/transfer_rucio.log` I could not see where the problem was.  But this log is very verbose (240K lines !) and I am not familiar with it.

That log has this line
```
[2026-08-21 06:11:29,527] [RucioTransfer.Actions.MonitorLockStatus] [DEBUG] fileDocs to update block completion: [{'id': '89a9f44ea56d6766eded09df8f0e76d3ebdcdf608bb68be38dd9caf0', 'name': '/store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000/output_10.root', 'dataset': '/GenericTTbar/rucio-ruciotransfers-1787178594-94ba0e06145abd65ccb1d21786dc7e1d/USER#2f117cad-374b-40d6-9193-8e7cafbabef8', 'blockcomplete': 'OK', 'ruleid': '463bebb13c404322b644dd3610b4d32d'}]
```
which should be logger just before the call to CRAB REST
https://github.com/dmwm/CRABServer/blob/6c1e83e10af760bc2a62cc7b3c9a56d59fae3246/src/python/ASO/Rucio/Actions/MonitorLockStatus.py#L58-L59

No error is logged after that

OTOH the filetransfersdb record was last updated on `tm_last_update	1787569416` i.e. 
```
belforte@lxplus810/crabint1> date -d @1787569416
Mon Aug 24 13:03:36 CEST 2026
belforte@lxplus810/crabint1> 
```

??????

## Comment (belforte, 2026-08-25T15:50:02Z)

hmm... postjob for job 10 was executed 4 times !!
Apparently the first 2 times it stopped during the deferral loop !!
```
 Tue Aug 25 05:32:49 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
[crabtw@vocms059 SPOOL_DIR]$ for r in 0 1 2 3 4; do PJ=postjob.10.$r.txt; echo $PJ; tail -2 $PJ; done
postjob.10.0.txt
Fri Aug 21 10:22:43 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Fri Aug 21 10:52:45 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
postjob.10.1.txt
Sat Aug 22 06:27:02 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Sat Aug 22 06:57:05 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
postjob.10.2.txt
Mon Aug 24 03:32:24 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Mon Aug 24 04:02:27 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
postjob.10.3.txt
======== Finished post-job execution with status code 2  : NON-RECOVERABLE JOB FAIL. No retries
Ended TaskManagerBootstrap with code 2
postjob.10.4.txt
Ended TaskManagerBootstrap with code 4
Tue Aug 25 05:32:49 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
[crabtw@vocms059 SPOOL_DIR]$ 
```

Maybe ASO-Rucio is OK, and the problem is in those (automatic ??!!!!) resubmissions.

We have a design decision that no resubmission is possible when using ASO-Rucio, exactly because it will mess bookkeping !

## Comment (belforte, 2026-08-25T15:55:55Z)

cronology of POST steps in dagman log is indeed strange
```
[crabtw@vocms059 SPOOL_DIR]$ cat RunJobs.dag.dagman.out |grep "POST Script of node"
08/20/26 01:20:27 POST Script of node Job6 completed successfully.
08/20/26 01:23:24 POST Script of node Job9 completed successfully.
08/20/26 01:23:24 POST Script of node Job5 completed successfully.
08/20/26 01:23:29 POST Script of node Job4 completed successfully.
08/20/26 01:23:29 POST Script of node Job2 completed successfully.
08/20/26 01:23:34 POST Script of node Job1 completed successfully.
08/20/26 01:23:39 POST Script of node Job7 completed successfully.
08/20/26 01:24:09 POST Script of node Job8 completed successfully.
08/20/26 09:22:30 POST Script of node Job3 completed successfully.
08/21/26 11:22:52 POST Script of node Job10 failed with status 1
08/22/26 19:27:14 POST Script of node Job10 failed with status 1
08/24/26 04:32:34 POST Script of node Job10 failed with status 1
08/24/26 04:40:41 POST Script of node Job10 failed with status 2
08/24/26 12:57:24 POST Script of node Job6 completed successfully.
08/24/26 12:57:24 POST Script of node Job9 completed successfully.
08/24/26 12:57:24 POST Script of node Job5 completed successfully.
08/24/26 12:57:24 POST Script of node Job4 completed successfully.
08/24/26 12:57:24 POST Script of node Job2 completed successfully.
08/24/26 12:57:24 POST Script of node Job1 completed successfully.
08/24/26 12:57:24 POST Script of node Job7 completed successfully.
08/24/26 12:57:24 POST Script of node Job8 completed successfully.
08/24/26 12:57:24 POST Script of node Job3 completed successfully.
08/24/26 12:57:24 POST Script of node Job10 failed with status 1
08/24/26 12:57:24 POST Script of node Job10 failed with status 1
08/24/26 12:57:24 POST Script of node Job10 failed with status 1
08/24/26 12:57:24 POST Script of node Job10 failed with status 1
[crabtw@vocms059 SPOOL_DIR]$ 
```

## Comment (belforte, 2026-08-25T16:19:14Z)

something wrong with new resubmission code ?
was Job10 marked as failed at some point so that the CICD pipeline issued a resubmit ? But hopefully TW should refuse resubmit when ASO==Rucio .

pfff...

## Comment (belforte, 2026-08-25T16:22:20Z)

TW log is not on TW disk anymore (!!!)  but pulling it from S3 cache, there is nothing after the successful submit. No `crab resubmit` was issued.

## Comment (belforte, 2026-08-25T16:29:58Z)

clearly something bad happened on Aug 24 at 4:40 am
```
08/24/26 04:40:41 POST Script of node Job10 failed with status 2
08/24/26 04:40:41 POST for Node Job10 returned 2
08/24/26 04:40:41 DAG status: 2 (DAG_STATUS_NODE_FAILED)
08/24/26 04:40:41 Of 10 nodes total:
08/24/26 04:40:41  Done     Pre   Queued    Post   Ready   Un-Ready   Failed   Futile
08/24/26 04:40:41   ===     ===      ===     ===     ===        ===      ===      ===
08/24/26 04:40:41     9       0        0       0       0          0        1        0
08/24/26 04:40:41 0 job proc(s) currently held
08/24/26 04:40:41 Note: 224 total POST script deferrals because of -MaxPost limit (10) or DEFER
08/24/26 04:40:41 DAGMan Runtime Statistics: [EventCycleTimeAvg=0.000; EventCycleTimeMax=0.359; EventCycleTimeMin=0.000; EventCycleTimeStd=0.003; EventCycleTimeSum=30.474; SleepCycleTimeAvg=5.019; SleepCycleTimeMax=5.963; SleepCycleTimeMin=4.005; SleepCycleTimeStd=0.049; SleepCycleTimeSum=359469.955; SubmitCycleTimeAvg=0.000; SubmitCycleTimeMax=0.262; SubmitCycleTimeMin=0.000; SubmitCycleTimeStd=0.001; SubmitCycleTimeSum=1.606; EventCycleTimeCount=71621.000; SleepCycleTimeCount=71621.000; SubmitCycleTimeCount=71622.000; LogProcessCycleTimeAvg=0.002; LogProcessCycleTimeMax=0.007; LogProcessCycleTimeMin=0.000; LogProcessCycleTimeStd=0.002; LogProcessCycleTimeSum=0.058; LogProcessCycleTimeCount=30.000; ]
08/24/26 04:40:41 Updating node status file
08/24/26 04:40:41 ERROR: the following job(s) failed:
08/24/26 04:40:41 ---------------------- Node ----------------------
08/24/26 04:40:41       Node Name: Job10
08/24/26 04:40:41            Noop: false
08/24/26 04:40:41          NodeID: 9
08/24/26 04:40:41     Node Status: STATUS_ERROR
08/24/26 04:40:41 Node return val: 2
08/24/26 04:40:41           Error: Job exited with status 147 and POST Script failed with status 2 (after 3 node retries)
08/24/26 04:40:41 Job Submit File: Job.10.submit
08/24/26 04:40:41      PRE Script: dag_bootstrap.sh PREJOB $RETRY 10 260819_222955:crabint1_crab_rucio_transfers_group_20260820_002954 crab-preprod-tw01.cern.ch conventional
08/24/26 04:40:41     POST Script: dag_bootstrap.sh POSTJOB $JOBID $RETURN $RETRY $MAX_RETRIES 260819_222955:crabint1_crab_rucio_transfers_group_20260820_002954 10 /store/temp/user/crabint1.fc8da30b0c45665baadb7dd2e2b252177bdff657/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000 /store/group/rucio/crab_test/ruciotransfers-1787178594/GenericTTbar/ruciotransfers-1787178594/260819_222955/0000 cmsRun_10.log.tar.gz conventional output_10.root
08/24/26 04:40:41           Retry: 3
08/24/26 04:40:41  HTCondor Job ID: (10601666.0.0)
08/24/26 04:40:41 PARENTS:  WAITING: 0 CHILDREN:
08/24/26 04:40:41 ---------------------------------------       <END>
08/24/26 04:40:41 Aborting DAG...
```
Well.. maybe it is OK that DAG was aborting when last node failed. But.. why did it restart 8 hours later ?
```
meMin=0.000; LogProcessCycleTimeStd=0.002; LogProcessCycleTimeSum=0.058; LogProcessCycleTimeCount=30.000; ]
08/24/26 04:40:41 Dag(root)::~Dag()
08/24/26 04:40:41 **** condor_dagman (condor_DAGMAN) pid 2670825 EXITING WITH STATUS 1
08/24/26 12:57:24 Setting maximum file descriptors to 46080.
08/24/26 12:57:24 ******************************************************
08/24/26 12:57:24 ** condor_dagman (CONDOR_DAGMAN) STARTING UP
08/24/26 12:57:24 ** /usr/bin/condor_dagman
```

When it restarted it submitted Job 10 again, as expected and I think this is what drove ASO into a mess.

## Comment (belforte, 2026-08-25T16:37:05Z)

SUbmission record from Dagman. Indeed Job 10 was submitted 5 times
```[crabtw@vocms059 SPOOL_DIR]$ cat RunJobs.dag.dagman.out |grep "Submitting node"
08/20/26 00:49:06 Submitting node Job3 from file Job.3.submit using direct job submission
08/20/26 00:49:06 Submitting node Job9 from file Job.9.submit using direct job submission
08/20/26 00:49:06 Submitting node Job4 from file Job.4.submit using direct job submission
08/20/26 00:49:06 Submitting node Job1 from file Job.1.submit using direct job submission
08/20/26 00:49:06 Submitting node Job8 from file Job.8.submit using direct job submission
08/20/26 00:49:06 Submitting node Job5 from file Job.5.submit using direct job submission
08/20/26 00:49:06 Submitting node Job7 from file Job.7.submit using direct job submission
08/20/26 00:49:06 Submitting node Job2 from file Job.2.submit using direct job submission
08/20/26 00:49:06 Submitting node Job10 from file Job.10.submit using direct job submission
08/20/26 00:49:06 Submitting node Job6 from file Job.6.submit using direct job submission
08/21/26 11:22:57 Submitting node Job10 from file Job.10.submit using direct job submission
08/22/26 19:27:19 Submitting node Job10 from file Job.10.submit using direct job submission
08/24/26 04:32:39 Submitting node Job10 from file Job.10.submit using direct job submission
08/24/26 12:57:30 Submitting node Job10 from file Job.10.submit using direct job submission
[crabtw@vocms059 SPOOL_DIR]$ 
```

Looking at events for Job10
```[crabtw@vocms059 SPOOL_DIR]$ cat RunJobs.dag.dagman.out |grep ULOG|grep Job10
08/20/26 00:49:11 Event: ULOG_SUBMIT for HTCondor Node Job10 (10599745.0.0) {08/20/26 00:49:06}
08/20/26 00:49:16 Event: ULOG_EXECUTE for HTCondor Node Job10 (10599745.0.0) {08/20/26 00:49:11}
08/20/26 00:50:41 Event: ULOG_JOB_TERMINATED for HTCondor Node Job10 (10599745.0.0) {08/20/26 00:50:37}
08/21/26 11:22:52 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job10 (10599745.0.0) {08/21/26 11:22:47}
08/21/26 11:23:02 Event: ULOG_SUBMIT for HTCondor Node Job10 (10601201.0.0) {08/21/26 11:22:57}
```
and a few lines below
```
08/21/26 11:22:52 POST Script of node Job10 failed with status 1
08/21/26 11:22:52 POST for Node Job10 returned 1
08/21/26 11:22:52 Node(Job10)::_Status = STATUS_ERROR
08/21/26 11:22:52 Node(Job10)::SetStatus(STATUS_READY    )
08/21/26 11:22:52 Retrying node Job10 (retry #1 of 3)...
```
Why did PostJob prematurely terminate on 08/21/26 11:22:52 ?

## Comment (belforte, 2026-08-25T16:43:29Z)

last line of postjob.10.0.txt is from 30 min earlier
```
[crabtw@vocms059 SPOOL_DIR]$ tail -1 postjob.10.0.txt 
Fri Aug 21 10:52:45 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
[crabtw@vocms059 SPOOL_DIR]$ 
```
And apparently PostJob was running for 5 seconds before exiting
```
08/21/26 11:22:47 Running POST script of Node Job10...
08/21/26 11:22:52 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job10 (10599745.0.0) {08/21/26 11:22:47}
```

It could have been a problem in the wrapper `dagman_bootstrap.sh` but its log is overwritten every time ... so... no way to know.

## Comment (belforte, 2026-08-25T17:23:54Z)

well.. An odd failure in PostJob once in a blue moon is somethin I can accept to file as "user will do crab kill and crab recovery".
But the fact that dagman restarted really puzzles me.

## Comment (belforte, 2026-08-25T17:27:01Z)

I tried to verify that crab resubmit is  disabled, but now PJ is stuck in waiting for transfer, client immediately refuses.
```
Found no jobs to resubmit. Only jobs in status failed can be resubmitted. 
```

## Comment (belforte, 2026-08-25T17:40:44Z)

Oh DAMN !! I was looking in wrong TW, this was submitted to preprod, not crab-dev-tw01.
Here are the `Resubmit` lines from the log
```

[crab3@crab-preprod-tw01 crabint1]$ cat 260819_222955:crabint1_crab_rucio_transfers_group_20260820_002954.log|grep Resubmitter|cut -c 1-100
2026-08-24 12:56:23,280:DEBUG:Handler:Starting <TaskWorker.Actions.DagmanResubmitter.DagmanResubmitt
2026-08-24 12:56:23,281:INFO:DagmanResubmitter:About to resubmit failed jobs for workflow: 260819_22
2026-08-24 12:56:23,281:DEBUG:DagmanResubmitter:Task info: {'tm_taskname': '260819_222955:crabint1_c
2026-08-24 12:56:23,590:DEBUG:DagmanResubmitter:Resubmitting when JOBIDs were specified
2026-08-24 12:56:23,690:INFO:DagmanResubmitter:Setting CRAB_ResubmitRecord={"epoch": 1, "job_ids": [
2026-08-24 12:56:23,712:DEBUG:DagmanResubmitter:Setting the task as successfully resubmitted with {'
2026-08-24 12:56:24,970:INFO:Handler:Finished <TaskWorker.Actions.DagmanResubmitter.DagmanResubmitte
2026-08-25 19:32:15,241:DEBUG:Handler:Starting <TaskWorker.Actions.DagmanResubmitter.DagmanResubmitt
2026-08-25 19:32:15,241:INFO:DagmanResubmitter:About to resubmit failed jobs for workflow: 260819_22
2026-08-25 19:32:15,241:DEBUG:DagmanResubmitter:Task info: {'tm_taskname': '260819_222955:crabint1_c
2026-08-25 19:32:15,564:DEBUG:DagmanResubmitter:Resubmitting when JOBIDs were specified
2026-08-25 19:32:15,636:INFO:DagmanResubmitter:Setting CRAB_ResubmitRecord={"epoch": 2, "job_ids": [
2026-08-25 19:32:15,665:DEBUG:DagmanResubmitter:Setting the task as successfully resubmitted with {'
2026-08-25 19:32:16,953:INFO:Handler:Finished <TaskWorker.Actions.DagmanResubmitter.DagmanResubmitte
[crab3@crab-preprod-tw01 crabint1]$ 
```

So indeed a `crab resubmit` was issued at on `2026-08-24 12:56:23,280:` which caused `08/24/26 12:57:24 ** condor_dagman (CONDOR_DAGMAN) STARTING UP`

## Comment (belforte, 2026-08-25T17:43:10Z)

and it looks like we did talk about "making it impossible to use crab resubmit with Rucio ASO" but never implemented it. By the way resubmission **before** ASO is called, i.e. on job failure, is OK. Is resubmission during ASO or after ASO failure which must be prevented.

## Comment (belforte, 2026-08-25T17:46:15Z)

**Conclusion**
* no fault in ASO-Rucio code (so far)
* PostJob exited with status 1 during the deferral loop, multiple times!!! **to be understood**
* need to implement a way to **prevent resubmission of jobs which fail in ASO step** (e.g. reach the 7 days timeout)

* this task problem was caused by the PostJob odd failure. We never tested the case when ASO-Rucio gives up after 7 days :-(

## Comment (belforte, 2026-08-26T07:37:55Z)

The unepxected PJ exit could be explained by one bash command in `dagman_bootstrap.sh` exiting with 1.
I guess the only way to know more would be to save logs from that (now it goes to  `dag_bootstrap.out` which gets overwritten every time a PRE/POST runs) and wait for another occurrence.

I will created ad-hoc issue about resubmission after I dig out the original thread.

## Comment (belforte, 2026-08-26T07:48:20Z)

how to handle ASO-RUcio timeout and resubmission was covered in https://github.com/dmwm/CRABServer/issues/8429

The plan was to make sure that PostJob never exits with 1 during ASO step (made timeout 60 days) so that user has to kill. And now killed tasks can not be resubmitted anymore.

So we are stuck with: PostJob returned 1 during ASO step, which is not expected. And since it did it during the bash deferral step, which we introduced to avoid running python too much, the problem could have happened somehow inside this

https://github.com/dmwm/CRABServer/blob/6c1e83e10af760bc2a62cc7b3c9a56d59fae3246/scripts/dagman/dag_bootstrap.sh#L26-L46

Well.. the script could also have failed in one of the following lines which are executed to run the python PostJob.py, and indeed if this would happen for "normal ASO", making PostJob (or PreJob) exiting with 1 is not a problem, it simply triggers a new submission.

But in ASO-Rucio world we need to be sure that PostJob can only return 1 before it hands control to Rucio.

## Comment (belforte, 2026-08-26T14:30:44Z)

Anyhow, I think the "what happened" is understood now: at some point the task had a job in failed status, which made the test script in the pipeline issue a resubmit which was accepted, ending up in overwriting the filetransfersdb record. ASO-Rucio is not prepared for this and did not do anything since from its POV everything was done already. ASO-RUcio simply completed the processing of what was given to in in `postjob.10.0.txt` !

I will open a new issue about making dag_bootstrap.sh more robust or at least more debuggable.
