# dmwm/CRABServer issue #8429: Rucio-ASO should properly handle job/task termination

State: closed
Opened: 2024-05-23T14:15:16Z
Closed: 2025-05-26T14:18:53Z
Labels: Status: Done, RUCIO
URL: https://github.com/dmwm/CRABServer/issues/8429

## Opening post (belforte, 2024-05-23T14:15:16Z)

properly handle things when
* PostJob fails a job after ASO timeout (7 days currently)
* crab kill command is sent

ASO should cleanup DID's in Rucio and make sure that open blocks are closed so that files properly transferred get published.


After quite some pondering and a little testing, I have settled on the following strategy:

- [x] do not allow anymore resubmission of killed tasks [CMSTalk1](https://cms-talk.web.cern.ch/t/coming-changes-to-crab-client/124722/1) [CMSTalk2](https://cms-talk.web.cern.ch/t/deprecating-resubmission-of-killed-crab-tasks/124723) #9075 
- [x] `crab kill` does a `condor_rm` of all task DAGs, instead of`condor_hold` #9076 
- [x] `cache_status.py` detects when DAG's have been killed or otherwise terminated and writes an `overallDagStatus` in `status_cache.json` 
- [x] ASO-Rucio reads `status_cache.json` and uses  `overallDagStatus` to decide if to close current dataset
    - [x]  that allows to increase number of files and elapsed time before closing a dataset, to be like Publisher_schedd
- [x] kill, not hold, DAGs when `CRAB_TaskEndTime` is reached #9077 
- [x] let PostJob run for as long as needed #9078 
- [x] look into a way to defer PostJob for a longer time when waiting on Rucio since days. #9079

## Comment (belforte, 2025-05-12T08:25:22Z)

trikier than I thought.

It is not possible to resubmit jobs once they reached the transfer status, once a file replica is inserted in Rucio a new file with same name can not be added anymore (reminder: Rucio stores permanently the checksum associated to a LFN and our files contain timestamps so checksum is different if same file is created again with same content).

I start to lean to let PJ wait on Rucio until task life time is expired or task is killed.
We can not fail them unless we have a way to prevent a resubmission.

## Comment (belforte, 2025-05-12T10:15:57Z)

So let's start with `crab kill`.
**We currently allow tasks to be resubmitted after `crab kill`. But in this case it must be forbidden. We can not risk that a job which had reached the `transferring` status is resubmitted.**

And then about PostJob
**since jobs in transferring can not be resubmitted, do not stop PostJob after 7 days, let it run until Task is terminated/completed, i.e. Rucio eventually succeeds or task is killed or task reaches end of life**

* I need to review what exactly happens when task reaches end of life. Dagman is going to be held[1] but..what does it mean in terms of dag status ? (well, same for kill, that also holds the dag). I see one example of Help dagman which reports FAILED status, but better be sure.
* I have asked HTCondor support https://www-auth.cs.wisc.edu/lists/htcondor-users/2025-May/msg00035.shtml


[1]
```console
belforte@vocms0106/~> condor_q 114458146.0


-- Schedd: crab3@vocms0106.cern.ch : <188.184.80.88:4080?... @ 05/13/25 23:19:37
 ID           OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD
114458146.0   crabtw          5/13 08:41   0+14:38:30 R  10   0.7 condor_dagman -p 0 -f -l . -Lockfile RunJobs1.su

Total for query: 0 jobs; 0 completed, 0 removed, 0 idle, 0 running, 0 held, 0 suspended 
Total for all users: 57740 jobs; 29631 completed, 2343 removed, 19220 idle, 6546 running, 0 held, 0 suspended

belforte@vocms0106/~> condor_q 114458146.0 -l|grep -i period
PeriodicHold = time() > CRAB_TaskEndTime
belforte@vocms0106/~> 
```

## Comment (belforte, 2025-05-12T13:18:35Z)

Best seems to disable resubmission of killed tasks in the REST, modifying
https://github.com/dmwm/CRABServer/blob/73a84b54d50a4c1fb11fdcf8212a2503618cb7d3/src/python/CRABInterface/DataWorkflow.py#L285-L286

Which will  make these redundant
https://github.com/dmwm/CRABServer/blob/73a84b54d50a4c1fb11fdcf8212a2503618cb7d3/src/python/CRABInterface/DataWorkflow.py#L296-L298

## Comment (belforte, 2025-05-12T14:26:53Z)

now about killing while ASO-Rucio is running.
DagmanKiller HOLD the DAG and kills all vanilla universe jobs
https://github.com/dmwm/CRABServer/blob/c64dc53f28f56a1022121b3680a757daf88f40ad/src/python/TaskWorker/Actions/DagmanKiller.py#L94-L95

Problem: DAG are also held when they completed with some failed jobs, to allow resubmission. How can ASO tell the 
difference ?

## Comment (belforte, 2025-05-12T17:01:53Z)

hmm... looks like current ASO-Rucio code has no knowledge of DAG status, and will simply wait 6 ours in order to close last block/dataset
https://github.com/dmwm/CRABServer/blob/c64dc53f28f56a1022121b3680a757daf88f40ad/src/python/ASO/Rucio/Actions/MonitorLockStatus.py#L188-L204

## Comment (belforte, 2025-05-12T17:05:45Z)

that comment is stale, default timeout is 1h
https://github.com/dmwm/CRABServer/blob/c64dc53f28f56a1022121b3680a757daf88f40ad/src/python/ASO/Rucio/Main.py#L66
I will send a task with a number of job which is not a multiple of 20 to check.
https://github.com/dmwm/CRABServer/blob/c64dc53f28f56a1022121b3680a757daf88f40ad/src/python/ASO/Rucio/Main.py#L40

## Comment (belforte, 2025-05-13T09:32:09Z)

IIUC the above means that if we kill a task by holding the DAGMAN, i.e. kill running jobs, running postjobs and halt the dagman, ASO-RUcio will wrap up things within 1 hour.
https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-interaction.html#suspending-a-running-dag

Should we remove the DAGMAN instead ? If we do not want to allow resubmission, why keep it around in Held status ?

## Comment (belforte, 2025-05-13T15:38:26Z)

thoughts:
* 1h timeout before closing a dataset is too short, just like 20 file per dataset is too little. It will create too many small blocks in DBS
* In view of making the timeout e.g. 4h, we need a way to close thing on ASO-Rucio side when task is killed. Since at that point no more PostJobs will run and no more files will be added to the list of transfers.
* all in all this is what Publsher does now to decide that a task is done and close current block: check if it is KILLED in DB or otherwise fetch status cache from WEBDIR and parse it using same code as in  Client (and new cache_status.py) https://github.com/dmwm/CRABServer/blob/c64dc53f28f56a1022121b3680a757daf88f40ad/src/python/Publisher/PublisherMaster.py#L332
* maybe "as simple as" in `task_proc_wrapper.sh` where we have the following loop, we can have `cache status` report the overall "collapsed DAG status" and pass it to `manage_transfers`
```
    cache_status
    manage_transfers
    sleep 300s
```

I went for adding `overallDagStatus`  key to `task_process/status_cache.json` and reading that file inside ASO-Rucio code

## Comment (belforte, 2025-05-13T19:41:06Z)

I have modified `cache_status.py` to add `overallDagStatus` key to the `cache_status.json` file.

Now that can be read amd used to set `shouldClose` in https://github.com/dmwm/CRABServer/blob/c64dc53f28f56a1022121b3680a757daf88f40ad/src/python/ASO/Rucio/Actions/MonitorLockStatus.py#L189-L196

## Comment (belforte, 2025-05-14T12:54:24Z)

`crab kill` or `task reached end of life` have same effect: dagbootstrap job is held.
When the job is held, it stops running, so the main dagman exits and in `node_status` we have
```
  Type = "DagStatus";
  DagFiles = {
    "/data/srv/glidecondor/condor_local/spool/4109/0/cluster10224109.proc0.subproc0/RunJobs.dag"
  };
  Timestamp = 1747226438; /* "Wed May 14 14:40:38 2025" */
  DagStatus = 6; /* "STATUS_ERROR (removed)" *
```
and all job nodes have
```
[
  Type = "NodeStatus";
  Node = "Job1";
  NodeStatus = 6; /* "STATUS_ERROR" */
```

so far so good. Now need to check subdags which are instead submitted not by running condor_dagman inside a script, but via `condor_submit_dag` command
https://github.com/dmwm/CRABServer/blob/c64dc53f28f56a1022121b3680a757daf88f40ad/src/python/TaskWorker/Actions/PreDAG.py#L335

## Comment (belforte, 2025-05-14T13:41:57Z)

the new code (as per last line in https://github.com/dmwm/CRABServer/issues/8429#issuecomment-2877010643 ) results in
```
  "overallDagStatus": "FAILED"
```
after a `crab kill` which is fine (again "standard splitting")

## Comment (belforte, 2025-05-14T14:08:47Z)

hmm.. I tried another `condor_hold` of a dagman bootstrap and DagStatus in `node_state` is not `DagStatus = 6; /* "STATUS_ERROR (removed)" *` but `  DagStatus = 3; /* "STATUS_SUBMITTED (held)" */` which `cache_status.py` translates into `RUNNING`, since status 3 is defined as STATUS_SUBMITTED by Dagman. The comment is not propagated in the classAd format when `node_state` is parsed.

## Comment (belforte, 2025-05-14T14:15:12Z)

well it looks like the first test was somehow flawed, and the expecte behavior is indeed 'STATUS_SUBMITTED` after the hold.
[This](https://www-auth.cs.wisc.edu/lists/htcondor-users/2025-May/msg00038.shtml) from HTCondor Dagman expert:

> Hi Stefano,
>
> Being held is not considered an error for DAGMan. When you run condor_hold on a running DAGMan job, the DagStatus
> attribute in the node status file should actually be 3 (submitted) with an inline comment saying "STATUS_SUBMITTED
> (held)". That being said when writing the node status file, DAGMan checks to see if the DAG is finished executing. This
 > would take precedence over the hold and set the status to done or error.
>
> -Cole Bollig

## Comment (belforte, 2025-05-14T14:35:56Z)

we already have code which checks the dagman jobs so can detect the HOLD status
https://github.com/dmwm/CRABServer/blob/c64dc53f28f56a1022121b3680a757daf88f40ad/scripts/task_process/task_proc_wrapper.sh#L91-L92

I'd need a way to catch this info inside `status_cache`.

OTOH `crab klll` will `condor_rm` all jobs so all actice dag nodes should fail and dag end in `FAILED`. But I am not sure in case there are unsubmitted nodes.

## Comment (belforte, 2025-05-14T14:39:50Z)

OTOH... does it really matter if when task reaches end of life we simply wait "timeout" hours from last successful postjob before closing last dataset ?

Better stay focused on crab kill.

Given that we deprecate resubmit after kill.. why holding the dagmans vs. simply doing a condor_rm ?

## Comment (belforte, 2025-05-14T15:10:48Z)

hm... after checking https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/files/crabschedd/JobCleanup.py , we need to make sure that dagman bootstrap jobs stay in the queue so that we can eventually cleanup SPOOL_DIR and WEB_DIR


anyhow JobCleanup.py above looks at all jobs in Scheduler universe and checks only that dag is not running and time since submission, so will clean up removed DAG's as well.

## Comment (belforte, 2025-05-15T12:26:37Z)

so we **may** use `condor_rm` on dagman's as well when `crab kill` is issued.

## Comment (belforte, 2025-05-16T10:07:55Z)

I am reluctant to add calls to condor_q inside `cache_status.py`, since that script is only parsing files so far, it has the virtue of being independent from schedd being temporarily busy (condo_q failes at times when duty cycle is high).

I have considered changing the frequency of calling `perform_condorq` in `task_proc_wrapper.sh` from 24h to to something shorter, but passing information from there to `cache_status.py` looks ugly.

And by the way I do not see the point of calling `perform_condorq` every 24h in the script while checking its output every 5min in `exit_now`. But as usual, let's try not to change what works w/o a good reason.

So, putting all together, I am pretty much inclined to `condor_rm`  dagman jobs at  `crab kill` time.
That will put DAG in FAILED status and kill all jobs in each DAG.

## Comment (belforte, 2025-05-16T12:38:44Z)

I am left with
* PostJob should not wait only 7 days, but until task expires, this means keep going until DAGMAN stops running them. Would be good to have some way to delay re-running from 30 min to hours as time goes.
* Currently DAGMANs are put in Hold when task expires (`PeriodicHold = time() > CRAB_TaskEndTime`) shall I remove them instead ? that's the case for vanilla universe jobs. Maybe kill dagman a few hours later, give condor time to run PostJobs ? Does it matter for removed jobs ?

## Comment (belforte, 2025-05-16T13:17:53Z)

PostJob takes less than a second to run when checking for output and finding that it has to wait [1]. Is really worth to worry about doing it too often? All in all PJ queries Transfersdb every 15 min, and otherwise reuses cached file on disk,  things happen pretty quickly then, most of the time likely goes in starting Python ! So changes to PJ code to e.g. exit immediatey to wait longer may not really help.

We currently allow 10 concurrent PostJobs, 10/sec means 18k in each 30min, so we can check status of a full 10k-job task even if Rucio is fully stuck. And otherwise PostJobs will be automatically delayed. Yet this may go on for weeks.

As long as we do not have tens of tasks in that situation, we should be OK. Main danger is that some largish T2 goes down making Rucio halt transfers there for a while.

All in all I am leaning toward "let it happen and see how it goes". If we run into problems, deal with them when they happen.

The best alternative I can imagine is to add a quick exit  in  `dag_bootstrap.sh` as a way to increase delays between PJ running. The available info there are what's in the arguments
`dag_bootstrap.sh POSTJOB $JOBID $RETURN $RETRY $MAX_RETRIES <task_name> <CRAB_ID> <tmp_LFN>  <final_LFN> ...`
see [DagmanMacros](https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-introduction.html#special-script-argument-macros) for the `$*` variables
Unfortunately no quick way to tell how long ago $JOBID was submitted or completed !

Yet, if disaster strikes, we can easily add a random "exit now with code 4" in dag_bootstrap.sh and delay PJ execution.

Or maybe... do it anyhow based on timestamp in task name ?

[1]
```
Mon, 28 Apr 2025 11:20:35 CEST(+0200):INFO:PostJob 
======== Starting execution again after deferral
Mon, 28 Apr 2025 11:20:35 CEST(+0200):DEBUG:PostJob (Parsed job ad.)
Mon, 28 Apr 2025 11:20:35 CEST(+0200):DEBUG:PostJob Output dataset should be already uploaded:
/FakeDataset/fakefile-FakePublish-93b9c6d427aa8d818d09d9e891838c1f/USER
Mon, 28 Apr 2025 11:20:35 CEST(+0200):INFO:PostJob Using the cache since it is up to date (last_query=1745831754.9439688) and it is after we submitted the transfer (aso_start_timestamp=1745830232)
Mon, 28 Apr 2025 11:20:35 CEST(+0200):DEBUG:PostJob Using cached ASO results.
Mon, 28 Apr 2025 11:20:35 CEST(+0200):INFO:PostJob Got statuses: submitted; 0.5 hours since transfer submit.
Mon, 28 Apr 2025 11:20:35 CEST(+0200):INFO:PostJob Deferring the execution of the post-job.
Mon, 28 Apr 2025 11:20:35 CEST(+0200):INFO:PostJob ********************************************************************************
======== Finished post-job execution with status code 4  : DEFERRING. PostJob will run again after 30 min
Ended TaskManagerBootstrap with code 4
```
also the "full process" as seen from Dagman side took < 1sec:
```
04/28/25 11:20:35 Running POST script of Node Job1069...
04/28/25 11:20:35 Deferring POST script of node Job1069 for 1800 seconds (exit status was 4)...
```
