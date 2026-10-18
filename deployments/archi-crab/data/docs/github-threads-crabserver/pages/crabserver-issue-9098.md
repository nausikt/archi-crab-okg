# dmwm/CRABServer issue #9098: Wrong Dagman status for some tasks

State: closed
Opened: 2025-05-28T16:43:52Z
Closed: 2025-05-30T11:23:23Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/9098

## Opening post (belforte, 2025-05-28T16:43:52Z)

following up on user problem report

https://cms-talk.web.cern.ch/t/crab-jobs-stuck-in-toretry-state/125339

I have found that all the 3 tasks indicated suffer of same problem.

At some point all DAG nodes were completed of failed and Dagman exited


But some failed jobs were left in PRERUN status in the `node_status` file, making CRAB report them and ToRetry and preventing resubmission.

Indeed the `node_status` reports a running Dagman with 35 nodes in PRE
```
[crabtw@vocms0121 cluster123521780.proc0.subproc0]$ head -15 node_state 
[
  Type = "DagStatus";
  DagFiles = {
    "/data/srv/glidecondor/condor_local/spool/1780/0/cluster123521780.proc0.subproc0/RunJobs.dag"
  };
  Timestamp = 1748301015; /* "Tue May 27 01:10:15 2025" */
  DagStatus = 3; /* "STATUS_SUBMITTED ()" */
  NodesTotal = 2086;
  NodesDone = 2051;
  NodesPre = 35;
  NodesQueued = 0;
  NodesPost = 0;

```
looking at e.g. the metric file, it reports the Dagman as PRERUN (status 2, see  [HTC doc](https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-information-files.html#current-node-status-file))
```[crabtw@vocms0121 cluster123521780.proc0.subproc0]$ cat RunJobs.dag.metrics 
{
    "client":"condor_dagman",
    "version":"24.0.6",
    "type":"metrics",
    "start_time":1748301012.527,
    "end_time":1748301026.335,
    "duration":13.808,
    "exitcode":1,
    "dagman_id":"123521780",
    "parent_dagman_id":"",
    "rescue_dag_number":0,
    "jobs":2086,
    "jobs_failed":35,
    "jobs_succeeded":2051,
    "dag_jobs":0,
    "dag_jobs_failed":0,
    "dag_jobs_succeeded":0,
    "total_jobs":2086,
    "total_jobs_run":2086,
    "DagStatus":2
}

```

But Dagman exited and claimed it had nothing to do

```
05/27/25 01:10:25 Aborting DAG...
05/27/25 01:10:25 Writing Rescue DAG to /data/srv/glidecondor/condor_local/spool/1780/0/cluster123521780.proc0.subproc0/RunJobs.dag.rescue003...
05/27/25 01:10:25 We have 0 running nodes to remove
05/27/25 01:10:25 Removing submitted jobs...
05/27/25 01:10:25 Removing any/all submitted HTCondor jobs...
05/27/25 01:10:25 Running: /usr/bin/condor_rm -const DAGManJobId==123521780 -reason DAG' 'Abort:' 'DAG' 'is' 'exiting' 'and' 'writing' 'rescue' 'file.
05/27/25 01:10:26 Note: 0 total node deferrals because of -MaxJobs limit (0)
05/27/25 01:10:26 Note: 0 total node deferrals because of -MaxIdle limit (1000)
05/27/25 01:10:26 Note: 0 total node deferrals because of node category throttles
05/27/25 01:10:26 Note: 111 total PRE script deferrals because of -MaxPre limit (20) or DEFER
05/27/25 01:10:26 Note: 0 total POST script deferrals because of -MaxPost limit (10) or DEFER
05/27/25 01:10:26 Note: 0 total HOLD script deferrals because of -MaxHold limit (20) or DEFER
05/27/25 01:10:26 DAG status: 2 (DAG_STATUS_NODE_FAILED)
05/27/25 01:10:26 Of 2086 nodes total:
05/27/25 01:10:26  Done     Pre   Queued    Post   Ready   Un-Ready   Failed   Futile
05/27/25 01:10:26   ===     ===      ===     ===     ===        ===      ===      ===
05/27/25 01:10:26  2051       0        0       0       0          0       35        0
05/27/25 01:10:26 0 job proc(s) currently held
05/27/25 01:10:26 Note: 111 total PRE script deferrals because of -MaxPre limit (20) or DEFER
05/27/25 01:10:26 DAGMan Runtime Statistics: [EventCycleTimeAvg = 0.003715634346008301; EventCycleTimeCount = 2.0; EventCycleTimeMax = 0.006990194320678711; EventCycleTimeMin = 0.0004410743713378906; EventCycleTimeStd = 0.004630927126982993; EventCycleTimeSum = 0.007431268692016602; LogProcessCycleTimeAvg = 3.719329833984375E-05; LogProcessCycleTimeCount = 1.0; LogProcessCycleTimeMax = 3.719329833984375E-05; LogProcessCycleTimeMin = 3.719329833984375E-05; LogProcessCycleTimeStd = 3.719329833984375E-05; LogProcessCycleTimeSum = 3.719329833984375E-05; SleepCycleTimeAvg = 5.388615369796753; SleepCycleTimeCount = 2.0; SleepCycleTimeMax = 5.534433841705322; SleepCycleTimeMin = 5.242796897888184; SleepCycleTimeStd = 0.2062184606176189; SleepCycleTimeSum = 10.77723073959351; SubmitCycleTimeAvg = 2.137819925944011E-05; SubmitCycleTimeCount = 3.0; SubmitCycleTimeMax = 2.694129943847656E-05; SubmitCycleTimeMin = 1.811981201171875E-05; SubmitCycleTimeStd = 4.841325890387857E-06; SubmitCycleTimeSum = 6.413459777832031E-05; ]
05/27/25 01:10:26 Node status file not updated because it is not yet outdated
05/27/25 01:10:26 Wrote metrics file /data/srv/glidecondor/condor_local/spool/1780/0/cluster123521780.proc0.subproc0/RunJobs.dag.metrics.
05/27/25 01:10:26 DAGMan Runtime Statistics: [EventCycleTimeAvg = 0.003715634346008301; EventCycleTimeCount = 2.0; EventCycleTimeMax = 0.006990194320678711; EventCycleTimeMin = 0.0004410743713378906; EventCycleTimeStd = 0.004630927126982993; EventCycleTimeSum = 0.007431268692016602; LogProcessCycleTimeAvg = 3.719329833984375E-05; LogProcessCycleTimeCount = 1.0; LogProcessCycleTimeMax = 3.719329833984375E-05; LogProcessCycleTimeMin = 3.719329833984375E-05; LogProcessCycleTimeStd = 3.719329833984375E-05; LogProcessCycleTimeSum = 3.719329833984375E-05; SleepCycleTimeAvg = 5.388615369796753; SleepCycleTimeCount = 2.0; SleepCycleTimeMax = 5.534433841705322; SleepCycleTimeMin = 5.242796897888184; SleepCycleTimeStd = 0.2062184606176189; SleepCycleTimeSum = 10.77723073959351; SubmitCycleTimeAvg = 2.137819925944011E-05; SubmitCycleTimeCount = 3.0; SubmitCycleTimeMax = 2.694129943847656E-05; SubmitCycleTimeMin = 1.811981201171875E-05; SubmitCycleTimeStd = 4.841325890387857E-06; SubmitCycleTimeSum = 6.413459777832031E-05; ]
05/27/25 01:10:26 Dag(root)::~Dag()
05/27/25 01:10:26 **** condor_dagman (condor_DAGMAN) pid 2561844 EXITING WITH STATUS 1
[crabtw@vocms0121 cluster123521780.proc0.subproc0]$ 

```

There was more going on, since ultimately Dagman exited because the PreJob scripts failed for those jobs (to be investigated), but whatever the reason for Pre script failure, once the 3 retries are exhausted the node should move to FAILED, not be stuck in PRERUN !

FWIW, looking deeper, the thing was apparently triggered by a Dagman restart (a resubmit ?)
```
05/26/25 00:45:43 **** condor_dagman (condor_DAGMAN) pid 161763 EXITING WITH STATUS 1
05/27/25 01:10:12 Setting maximum file descriptors to 46080.
05/27/25 01:10:12 ******************************************************
05/27/25 01:10:12 ** condor_dagman (CONDOR_DAGMAN) STARTING UP
```
that triggered 35 PRE scriptds wjhich all failed.
PreJob log indicates the falure reason as
```
Tue, 27 May 2025 01:10:20 CEST(+0200):INFO:PreJob calculate_crab_retry returned the following message: 
	Loaded retry_info = {'pre': 10, 'post': 9}
	File job_out.455 already exists.
	It seems the job has already been submitted.
	Setting the pre-job exit code to 1.
```
which means that the previous retry PostJob had not moved the output to WEB_DIR, which it does at the very beginning.
Indeed there is no postjob log for job 455 since 2 days earlier
```
[crabtw@vocms0121 cluster123521780.proc0.subproc0]$ ls -ltr post*455*
-rw-r--r-- 1 crabtw zh 39988 May 23 09:09 postjob.455.0.txt
-rw-r--r-- 1 crabtw zh 39954 May 23 14:03 postjob.1455.0.txt
-rw-r--r-- 1 crabtw zh 33133 May 23 15:06 postjob.455.1.txt
-rw-r--r-- 1 crabtw zh 17879 May 23 20:24 postjob.1455.1.txt
-rw-r--r-- 1 crabtw zh    30 May 24 22:05 postjob.455.3.txt
-rw-r--r-- 1 crabtw zh 67336 May 25 04:12 postjob.455.2.txt
[crabtw@vocms0121 cluster123521780.proc0.subproc0]$ 
```
 
So PostJob did not run (to be understood) which made PreJob fail (by design), but
**why Dagman exited leaving nodes in PRERUN rather than FAILED ?**

## Comment (belforte, 2025-05-28T16:51:31Z)

about "PostJob failed w/o a log" dagman log only indicates that all happened within one second
```
05/27/25 01:10:14 Event: ULOG_JOB_TERMINATED for HTCondor Node Job455 (123709194.0.0) {05/25/25 04:11:55} [recovery mode]
05/27/25 01:10:14 Event is okay
05/27/25 01:10:14 Number of idle job procs: 1
05/27/25 01:10:14 Node Job455 job proc (123709194.0.0) completed successfully.
05/27/25 01:10:14 Node Job455 job completed
05/27/25 01:10:14 Node(Job455)::_Status = STATUS_SUBMITTED
05/27/25 01:10:14 Node(Job455)::SetStatus(STATUS_POSTRUN  )
05/27/25 01:10:14 Event: ULOG_POST_SCRIPT_TERMINATED for HTCondor Node Job455 (123709194.0.0) {05/25/25 04:12:01} [recovery mode]
05/27/25 01:10:14 Event is okay
05/27/25 01:10:14 Node(Job455)::_Status = STATUS_POSTRUN
05/27/25 01:10:14 Node(Job455)::SetStatus(STATUS_ERROR    )
05/27/25 01:10:14 POST Script of node Job455 failed with status 1
05/27/25 01:10:14 POST for Node Job455 returned 1
```

## Comment (belforte, 2025-05-28T16:53:29Z)

shall we start by rolling back #9012  ?  @mmascher

## Comment (belforte, 2025-05-28T16:57:04Z)

at the time Dagman exited, it wrote things very clearly in the Rescue dag
```
# Rescue DAG file, created after running
#   the /data/srv/glidecondor/condor_local/spool/1780/0/cluster123521780.proc0.subproc0/RunJobs.dag DAG file
# Created 5/26/2025 23:10:25 UTC
# Rescue DAG version: 2.0.1 (partial)
#
# Total number of Nodes: 2086
# Nodes premarked DONE: 2051
# Nodes that failed: 35
#   Job10,Job13,Job16,Job24,Job27,Job37,Job55,Job57,Job60,Job131,Job138,Job300,Job301,Job304,Job305,Job306,Job307,Job407,Job451,Job453,Job455,Job675,Job835,Job1052,Job1053,Job1054,Job1059,Job1061,Job1062,Job1079,Job1399,Job1400,Job1401,Job1654,Job2061,<ENDLIST>
```

The problem is that we rely on node status file  !
CRAB sees all those jobs as "beiing retried" (human transaltion of PRE) and refuses to resubmit.

## Comment (belforte, 2025-05-28T16:58:25Z)

all the above appears to go against what is written in [HTC doc](https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-information-files.html#current-node-status-file)

> The status file is also updated a final time when the DAG completes either successfully or not.

## Comment (belforte, 2025-05-29T10:22:26Z)

I wrote to HTCondor support https://www-auth.cs.wisc.edu/lists/htcondor-users/2025-May/msg00091.shtml
```text
Date: Thu, 29 May 2025 12:22:01 +0200
    From: Stefano Belforte <[stefano.belforte@xxxxxxx](mailto:stefano.belforte@DOMAIN.HIDDEN)>
    Subject: [HTCondor-users] problems with Dagman status files

Dear experts,

we have hit a few cases of an odd situation (for me at least) with Dagman status.
Can you kindly help me to understand correctly the information there ? Or is there by any chance an inconsistency in the way those are written, or documented ?

There are more details in https://github.com/dmwm/CRABServer/issues/9098 and more can be provided upon request, like full log files or access to the AP where things ran.

Summary is:

this is not the norm, usually things work finely (thanks !)

we had a bad day where for unknown reasons a lot POST scripts failed immediately, leading to nodes being retried (as per dagman description file, all fine there). Due the odd way in which POST failed the PRE script of the retries failed too. Once the max retry for the node was reached the node was failed, but still listed as in PRERUN (!?)

After all affected nodes ended like that, dagman debug file has (trimmed):

05/27/25 01:10:25 Aborting DAG...
[...]
05/27/25 01:10:26 DAG status: 2 (DAG_STATUS_NODE_FAILED)
[...]
05/27/25 01:10:26  Done     Pre   Queued    Post   Ready   Un-Ready   Failed   Futile
05/27/25 01:10:26   ===     ===      ===     ===     ===        ===      ===      ===
05/27/25 01:10:26  2051       0        0       0       0          0       35        0
[...]
05/27/25 01:10:26 Node status file not updated because it is not yet outdated
05/27/25 01:10:26 Wrote metrics file /data/srv/glidecondor/condor_local/spool/1780/0/cluster123521780.proc0.subproc0/RunJobs.dag.metrics.
[...]
05/27/25 01:10:26 **** condor_dagman (condor_DAGMAN) pid 2561844 EXITING WITH STATUS 1

Note the "Node status file not updated" which to me is in contradiction with
the documentation https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-information-files.html
which states " The status file is also updated a final time when the DAG completes either successfully or not."

Indeed in the status file I have [1] and in metrics file I have [2]

So my questions are:

1. Why was stats file not updated ? What can I do to ensure it is ?

2. Why DAG status is 3 in the status file, but 2 in the metric file ?

3. How do I reconcile "DAG status: 2 (DAG_STATUS_NODE_FAILED)"   with the list of status values in the Dagman documentation ?


As a final note, Dagman wrote a rescue file which looks just fine to me (thanks!) but so fare we have been relying on status file to decide that a dagman could be restarted (called resubmission in CRAB). As long as the node file says STATUS 3 (SUBMITTED) we prevent users from restarting the Dagman.

I apologise if this message is not clear, it is a new situation and I do not fully understand what's happening.

Thanks for you help

Stefano


[1]

[
  Type = "DagStatus";
  DagFiles = {
    "/data/srv/glidecondor/condor_local/spool/1780/0/cluster123521780.proc0.subproc0/RunJobs.dag"
  };
  Timestamp = 1748301015; /* ["Tue May 27 01:10:15 2025"](tuemay2701:10:152025) */
  DagStatus = 3; /* "STATUS_SUBMITTED ()" */
  NodesTotal = 2086;
  NodesDone = 2051;
  NodesPre = 35;
  NodesQueued = 0;
  NodesPost = 0;

[2]

{
    "client":"condor_dagman",
    "version":"24.0.6",
    "type":"metrics",
    "start_time":1748301012.527,
    "end_time":1748301026.335,
    "duration":13.808,
    "exitcode":1,
    "dagman_id":"123521780",
    "parent_dagman_id":"",
    "rescue_dag_number":0,
    "jobs":2086,
    "jobs_failed":35,
    "jobs_succeeded":2051,
    "dag_jobs":0,
    "dag_jobs_failed":0,
    "dag_jobs_succeeded":0,
    "total_jobs":2086,
    "total_jobs_run":2086,
    "DagStatus":2
}
```

## Comment (belforte, 2025-05-29T15:05:12Z)

here's the answer from expert

On 29/05/2025 16:28, Cole Bollig wrote:
> Hi Stefano,
>
>     When DAGMan goes to write the final node status on the way out the door, it checks if its state has changed
> before actually writing the node status file. In this case it appears that DAGMan has determined that its state
> had not changed since the prior writing of the DAG node status file.
> If you want to have DAGMan to re-write the node status file at exit regardless of state change,
> you can add the ALWAYS-UPDATE keyword to the declaration in your DAG file.
>
>     Points 2 & 3 are due to the fact that DagStatus means different things in the node status file
> and the metrics file.
>  This discrepancy is something that has sadly existed for a long time,
> and I don't know the best way to address it.
>
>         For the node status file, the DagStatus is equivalent to the value list you
>               provided from our documentation.
>         For the metrics file, the DagStatus is set to the value of the DAGMan jobs ClassAd attribute
 [DAG_Status](https://htcondor.readthedocs.io/en/latest/classad-attributes/job-classad-attributes.html#DAG_Status).
>
>
> I will update the documentation to better reflect attempting to write the node status file on exit and warn that DagStatus is different between the two files.
>
> Hope this helps,
> Cole Bollig

## Comment (belforte, 2025-05-29T15:18:38Z)

So the solution to the Dagman status problem should be to add back **ALWAYS-UPDATE** which I will do as hot patch

While the reason of the immediate PostJob failures remains a mistery and I have no idea how to address it. Maybe the best way is to modify `dag_bootstrap.sh` so that its stdout/err go to a different file every time so we look in there when the PostJob fails before activating Python logging. And go from there. Maybe also stop dumping env and classads in `dag_bootstrap.out`.

## Comment (belforte, 2025-05-30T08:54:31Z)

the patch for ALWAYS-UPDATE has been deployed.
I am keeping this open to think about improving logging from POST step

## Comment (belforte, 2025-05-30T09:51:01Z)

I suspect that the failures where due to this line at the end of dag_bootstrap.sh
`exec nice -n 19 python3 -m TaskWorker.TaskManagerBootstrap "$@"`
Becasue `TaskManagerBootstrap` does
```python
from TaskWorker.Actions import PreDAG, PreJob, PostJob
```
and PreDAG has calls to Rucio client, so the code is imported even if not used and most likely was triggering the
`ModuleNotFoundError: No module named 'rucio.db'` during import as per https://cms-talk.web.cern.ch/t/new-rucio-command-line-installed-on-cvmfs/119305/4?u=belforte

So indeed POST was failing before starting python3 and there was no postjob log.

Indeed:
```console
belforte@vocms059/SPOOL_DIR> export PYTHONPATH=$PYTHONPATH:/cvmfs/cms.cern.ch/rucio/x86_64/rhel9/py3/37.4.0/lib/python3.9/site-packages/
belforte@vocms059/SPOOL_DIR> python3 -m TaskWorker.TaskManagerBootstrap 
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/3509/0/cluster10233509.proc0.subproc0/Utils/TokenManager.py", line 23, in <module>
    import jwt
ModuleNotFoundError: No module named 'jwt'
Traceback (most recent call last):
  File "/usr/lib64/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib64/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/data/srv/glidecondor/condor_local/spool/3509/0/cluster10233509.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py", line 6, in <module>
    from TaskWorker.Actions import PreDAG, PreJob, PostJob
  File "/data/srv/glidecondor/condor_local/spool/3509/0/cluster10233509.proc0.subproc0/TaskWorker/Actions/PreDAG.py", line 41, in <module>
    from RucioUtils import getNativeRucioClient
  File "/data/srv/glidecondor/condor_local/spool/3509/0/cluster10233509.proc0.subproc0/RucioUtils.py", line 5, in <module>
    from rucio.client import Client
  File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel9/py3/37.4.0/lib/python3.9/site-packages/rucio/client/__init__.py", line 15, in <module>
    from .client import Client  # noqa: F401
  File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel9/py3/37.4.0/lib/python3.9/site-packages/rucio/client/client.py", line 32, in <module>
    from rucio.client.requestclient import RequestClient
  File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel9/py3/37.4.0/lib/python3.9/site-packages/rucio/client/requestclient.py", line 23, in <module>
    from rucio.db.sqla.constants import TransferLimitDirection
ModuleNotFoundError: No module named 'rucio.db'
belforte@vocms059/SPOOL_DIR> 
```

## Comment (belforte, 2025-05-30T11:23:23Z)

All in all, the problem is understood. And the reason I could not figure out initially is because when I tried PostJob manually it was working because Shahzad had already fixed Rucio client.
So maybe we can stay with "dag_boostrap.sh ~never fails so there's no reason to save a different log file every time". Our directories are cluttered already.
