# dmwm/CRABServer issue #7652: automatic splitting does not send tail jobs

State: closed
Opened: 2023-06-02T15:29:31Z
Closed: 2023-06-09T08:39:49Z
Labels: Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/7652

## Opening post (belforte, 2023-06-02T15:29:31Z)

the user task in [this thread](https://cms-talk.web.cern.ch/t/many-jobs-failing-with-code-8028/24974) did not have tail jobs.
Looking around I found that dagman_bootstrap.sh failed [1] in the step of preparing tails with a worrying 
```
  TaskWorker/Actions/PreJob.py", line 502, in execute
    self.stage = args[4]
IndexError: tuple index out of range
```

This led to the dagman for the tail to be kicked off without the submit files [2]
and all tail jobs fail in the PRE step [3] of the dag

To be derbugged. Bu mostly.. was this some odd glitch, or do all of our automatic splitting task lack tail jobs ?

[1]
tail of `dag_bootstrap.out`
<details><summary>Details</summary>

```
+ echo 'Now running the job in /data/srv/glidecondor/condor_local/spool/1363/0/cluster92631363.proc0.subproc0...'
Now running the job in /data/srv/glidecondor/condor_local/spool/1363/0/cluster92631363.proc0.subproc0...
+ exec nice -n 19 python3 -m TaskWorker.TaskManagerBootstrap PREJOB 2 1-17 230519_144756:jdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter tailTTraceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/1363/0/cluster92631363.proc0.subproc0/Utils/TokenManager.py", line 23, in <module>
    import jwt
ModuleNotFoundError: No module named 'jwt'
Cannot import ldap
Entering TaskManagerBootstrap with args: ['/data/srv/glidecondor/condor_local/spool/1363/0/cluster92631363.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py', 'PREJOB', '2', '1-16', '230519_144756:jdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter', 'tail']
Got a fatal exception: tuple index out of range
Traceback (most recent call last):
  File "/usr/lib64/python3.6/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib64/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/data/srv/glidecondor/condor_local/spool/1363/0/cluster92631363.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py", line 85, in <module>
    retval = bootstrap()
  File "/data/srv/glidecondor/condor_local/spool/1363/0/cluster92631363.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py", line 26, in bootstrap
    return PreJob.PreJob().execute(*sys.argv[2:])
  File "/data/srv/glidecondor/condor_local/spool/1363/0/cluster92631363.proc0.subproc0/TaskWorker/Actions/PreJob.py", line 502, in execute
    self.stage = args[4]
IndexError: tuple index out of range
[crabtw@vocms0120 cluster92631363.proc0.subproc0]$ 
```
</details>

[2]

[crabtw@vocms0120 cluster92631363.proc0.subproc0]$ ls *submit
<details><summary>Details</summary>

```
Job.0-1.submit  Job.0-4.submit  Job.11.submit  Job.2.submit  Job.5.submit  Job.8.submit
Job.0-2.submit  Job.0-5.submit  Job.12.submit  Job.3.submit  Job.6.submit  Job.9.submit
Job.0-3.submit  Job.10.submit   Job.1.submit   Job.4.submit  Job.7.submit  Job.submit
[crabtw@vocms0120 cluster92631363.proc0.subproc0]$ 
```
</details>

[3]
[crabtw@vocms0120 cluster92631363.proc0.subproc0]$ cat node_state.1
<details><summary>Details</summary>

```
[
  Type = "DagStatus";
  DagFiles = {
    "RunJobs1.subdag"
  };
  Timestamp = 1684575668; /* "Sat May 20 11:41:08 2023" */
  DagStatus = 6; /* "STATUS_ERROR (failed)" */
  NodesTotal = 17;
  NodesDone = 0;
  NodesPre = 0;
  NodesQueued = 0;
  NodesPost = 0;
  NodesReady = 0;
  NodesUnready = 0;
  NodesFailed = 17;
  JobProcsHeld = 0;
  JobProcsIdle = 0; /* includes held */
]
[
  Type = "NodeStatus";
  Node = "Job1-1";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-2";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-3";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-4";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-5";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-6";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-7";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-8";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-9";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-10";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-11";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-12";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-13";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-14";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-15";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-16";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1-17";
  NodeStatus = 6; /* "STATUS_ERROR" */
  StatusDetails = "PRE Script failed with status 1 (after 2 node retries)";
  RetryCount = 2;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "StatusEnd";
  EndTime = 1684575668; /* "Sat May 20 11:41:08 2023" */
  NextUpdate = 0; /* "none" */
]
[crabtw@vocms0120 cluster92631363.proc0.subproc0]$ 
```
</details>

## Comment (belforte, 2023-06-02T19:16:06Z)

rerunning with pdb the line from `dag_bootrap.sh` as per the above log `dag_bootstrap.out` (need to setup env. first, just copy/paste from the script)

PreJob is called with these args:
```
args = ('2', '1-16', '230519_144756:jdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter', 'tail')
```
and then it looks for
https://github.com/dmwm/CRABServer/blob/23074811b67f2d7cad77d64270a2bae0679f2054/src/python/TaskWorker/Actions/PreJob.py#L494-L503
so clearly the `backend` is missing and the code fails to assign `"tail"` to `self.stage`

Now look at caller
https://github.com/dmwm/CRABServer/blob/23074811b67f2d7cad77d64270a2bae0679f2054/src/python/TaskWorker/TaskManagerBootstrap.py#L25-L26
and note from `dagman.out` 

Entering TaskManagerBootstrap with args: ['/data/srv/glidecondor/condor_local/spool/1363/0/cluster92631363.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py', 'PREJOB', '2', '1-16', '230519_144756:jdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter', 'tail']

I do not see anything which can do as `backend`, all args after `"PREJOB"` string are properly passed to the PreJob 

Need more digging.

## Comment (belforte, 2023-06-02T20:56:05Z)

args to `TaskManagerBootstrap ` come from
https://github.com/dmwm/CRABServer/blob/23074811b67f2d7cad77d64270a2bae0679f2054/scripts/dag_bootstrap.sh#L110
i.e. are the same as passed to `dag_bootstrap.sh` 
Those args come from the definition of the PRE step in the dagman itself.
In our case in `RunJobs1.subdag` (where tail jobs are defined):
```
SCRIPT  PRE  Job1-16 dag_bootstrap.sh PREJOB $RETRY 1-16 230519_144756:jdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter  tail
```
which does not have the `backend` argument.
To be compared with the (successful) "main" subdag where we have lines like:
```
SCRIPT  PRE  Job12 dag_bootstrap.sh PREJOB $RETRY 12 230519_144756:jdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter vocms0120.cern.ch processing
```
and `backend` is `vocms0120.cern.ch `, while for the main (initial) DAG the PRE step for probe jobs has
```
SCRIPT  PRE  Job0-1 dag_bootstrap.sh PREJOB $RETRY 0-1 230519_144756:jdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter crab-prod-tw01.cern.ch probe
```
and `backend` is crab-prod-tw01

Now, looking at the code this `backend` thing is a VERY obsolete thing which together with other VERY obsolete stuff like `bossId` is used in the obsolete code which prepares records to be sent to the obsolete MonAlisa based old dashboard... but that's a different story. Of course cleanup is long due here.

**So when `RunJobs1.subdag` was created, something went wrong.**

## Comment (belforte, 2023-06-02T21:23:25Z)

AFAIU lines like
```
SCRIPT  PRE  Job1 dag_bootstrap.sh PREJOB $RETRY 1 230519_144756:jdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter vocms0120.cern.ch processing
```
which is OK, or
```
SCRIPT  PRE  Job1-16 dag_bootstrap.sh PREJOB $RETRY 1-16 230519_144756:jdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter  tail
```
which is bad (no value for `backend` arg)
come from
https://github.com/dmwm/CRABServer/blob/23074811b67f2d7cad77d64270a2bae0679f2054/src/python/TaskWorker/Actions/DagmanCreator.py#L44-L52
and the `{backend}` value is assigned in
https://github.com/dmwm/CRABServer/blob/23074811b67f2d7cad77d64270a2bae0679f2054/src/python/TaskWorker/Actions/DagmanCreator.py#L645

Hard to fathom how `$HOSTNAME` could have been a null string !!!!

Hopefully an isolated glitch ?

## Comment (belforte, 2023-06-02T21:28:58Z)

On hold waiting for more evidence whether this was really an isolated incident.

## Comment (belforte, 2023-06-05T15:57:11Z)

I have run some tests, [including](https://cmsweb.cern.ch/crabserver/ui/task/230605_151708%3Abelforte_crab_20230605_171703) same input dataset as the [failed task](https://cmsweb.cern.ch/crabserver/ui/task/230519_144756%3Ajdickins_crab_pfnano_v2_3_2016APV_QCD_HT2000toInf_BGenFilter) but main jobs always completed OK so I got no chance to see tails in action.

## Comment (belforte, 2023-06-06T14:08:05Z)

more reports of same problem :-(
https://cms-talk.web.cern.ch/t/crab-resubmit-not-restarting-failed-jobs/24085/1

I guess I can start by removing that `backend` argument.

## Comment (belforte, 2023-06-07T13:43:41Z)

escalatint to "clearly broken" :-(

## Comment (mapellidario, 2023-06-07T14:31:41Z)

I know that this is bad practice and that we should aim for a proper refactor and remove the "backend" arguments, but what if we deploy a quickfix in which we change dagmancreator with

```diff
-  'backend': os.environ.get('HOSTNAME', ''), 
+  'backend': os.environ.get('HOSTNAME', 'dummy-backend'), 
``` 

?

If I understand correctly this should only cause the wrong value to be passed around, but at least our code should not fail because it finds an empty value.

Or did I miss anything?

## Comment (belforte, 2023-06-07T14:35:14Z)

that would solve, like setting backend='arbitrarystring'. But I have to fear that the real problem is elsewhere since this makes no sense. At the very least I need to reproduce the problem so that I can test the fix !

## Comment (belforte, 2023-06-08T00:41:16Z)

I was able to reproduce the problem after hacking things so that processing jobs fails by hitting a 2min maxWall time
```
belforte@lxplus814/automatic> crab status --long 
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/automatic/crab_20230607_232520
Task name:			230607_212524:belforte_crab_20230607_232520
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/230607_212524%3Abelforte_crab_20230607_232520
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=230607_212524%3Abelforte_crab_20230607_232520&from=1686169525000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_FR_GRIF', 'T2_FR_IPHC']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	FAILED

The job splitting of this task is 'Automatic', please refer to this FAQ for a description of the jobs status summary:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_is_the_Automatic_splitting
More details of Automatic Splitting process for this task (including possible failures) are in the Dagman Log files in:
https://cmsweb.cern.ch:8443/scheddmon/059/belforte/230607_212524:belforte_crab_20230607_232520/AutomaticSplitting/

Probe jobs status:              no output    		100.0% (5/5)

Main jobs status:               finished     		 33.3% (2/6)
				rescheduled as tail jobs		 66.7% (4/6)

Tail jobs status:               failed       		100.0% (4/4)

No publication information (publication has been disabled in the CRAB configuration file)

Error Summary: (use crab status --verboseErrors for details about the errors)

 2 jobs failed in postprocessing step

 1 jobs failed with exit code 50664

 1 jobs failed with exit code -1

Could not find exit code details for 4 jobs.

Have a look at https://twiki.cern.ch/twiki/bin/viewauth/CMSPublic/JobExitCodes for a description of the exit codes.

Extended Job Status Table:

 Job State        Most Recent Site        Runtime   Mem (MB)      CPU %    Retries   Restarts      Waste       Exit Code
 0-1 no output    T2_US_Wisconsin         0:03:31        330         20          0          0    0:02:08               0
 0-2 no output    T2_US_Wisconsin         0:02:43         61          6          0          0    0:02:08               0
 0-3 no output    T2_US_Wisconsin         0:02:00         51          7          0          0    0:03:02               0
 0-4 no output    T2_US_Wisconsin         0:02:36         61          5          0          0    0:02:08               0
 0-5 no output    T1_US_FNAL              0:03:09        555         16          1          0    0:10:58               0
   1 rescheduled  T1_US_FNAL              0:04:59        150         19          0          0    0:07:06  Postprocessing failed
   2 finished     T1_US_FNAL              0:04:54        508          3          0          0    0:01:22               0
   3 finished     T1_US_FNAL              0:05:00        543          4          0          0    0:01:06               0
   4 rescheduled  T1_US_FNAL              0:03:39        127          3          0          0    0:06:44           50664
   5 rescheduled  T1_US_FNAL              0:02:01        498         50          0          0    0:00:00  Postprocessing failed
   6 rescheduled  T1_US_FNAL              0:00:00          0    Unknown          0          1    0:01:04              -1
 1-1 failed                               0:00:00    Unknown          0          0          0    0:00:00         Unknown
 1-2 failed                               0:00:00    Unknown          0          0          0    0:00:00         Unknown
 1-3 failed                               0:00:00    Unknown          0          0          0    0:00:00         Unknown
 1-4 failed                               0:00:00    Unknown          0          0          0    0:00:00         Unknown

Warning: the max jobs runtime is less than 30% of the task requested value (1250 min), please consider to request a lower value for failed jobs (allowed through crab resubmit) and/or improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task.

Warning: the average jobs CPU efficiency is less than 50%, please consider to improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task

Summary of run jobs:
 * Memory: 0MB min, 543MB max, 305MB ave
 * Runtime: 0:00:00 min, 0:05:00 max, 0:02:03 ave
 * CPU eff: 0% min, 50% max, 12% ave
 * Waste: 0:17:23 (46% of total)

Log file is /afs/cern.ch/work/b/
```

Problem is clearly "persistent", so I doubt that the reason is `$HOSTNAME` not defined.  But I still have not found the proper way to follow the code

## Comment (belforte, 2023-06-08T07:11:55Z)

amazingly the dumb hack from
https://github.com/dmwm/CRABServer/blob/88b6f1160ba7a3f0271e03048bfef59bfad26a18/src/python/TaskWorker/Actions/DagmanCreator.py#L645
to
```python
'backend': 'DummyBackend',
```
has solved
```
belforte@lxplus814/automatic> crab status --long
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/automatic/crab_20230608_024042
Task name:			230608_004046:belforte_crab_20230608_024042
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/230608_004046%3Abelforte_crab_20230608_024042
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=230608_004046%3Abelforte_crab_20230608_024042&from=1686181246000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_FR_IPHC', 'T2_FR_GRIF']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	COMPLETED

The job splitting of this task is 'Automatic', please refer to this FAQ for a description of the jobs status summary:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_is_the_Automatic_splitting
More details of Automatic Splitting process for this task (including possible failures) are in the Dagman Log files in:
https://cmsweb.cern.ch:8443/scheddmon/059/belforte/230608_004046:belforte_crab_20230608_024042/AutomaticSplitting/

Probe jobs status:              no output    		100.0% (5/5)

Main jobs status:               finished     		 50.0% (3/6)
				rescheduled as tail jobs		 50.0% (3/6)

Tail jobs status:               finished     		100.0% (3/3)

No publication information (publication has been disabled in the CRAB configuration file)

Error Summary: (use crab status --verboseErrors for details about the errors)

 2 jobs failed with exit code 50664

 1 jobs failed in postprocessing step

Have a look at https://twiki.cern.ch/twiki/bin/viewauth/CMSPublic/JobExitCodes for a description of the exit codes.

Extended Job Status Table:

 Job State        Most Recent Site        Runtime   Mem (MB)      CPU %    Retries   Restarts      Waste       Exit Code
 0-1 no output    T1_US_FNAL              0:04:18        516         28          0          0    0:02:14               0
 0-2 no output    T2_US_Wisconsin         0:01:49         49          7          0          0    0:02:52               0
 0-3 no output    T2_US_Wisconsin         0:03:51         29         16          0          0    0:01:57               0
 0-4 no output    T2_US_MIT               0:01:51         23         18          0          0    0:03:16               0
 0-5 no output    T2_US_Wisconsin         0:01:50        633         16          0          0    0:03:20               0
   1 finished     T2_US_Wisconsin         0:04:22        636          4          0          0    0:05:35               0
   2 finished     T2_US_Wisconsin         0:04:18        277          4          0          0    0:05:22               0
   3 rescheduled  T2_US_Wisconsin         0:04:22        541          2          0          0    0:06:37           50664
   4 finished     T2_US_MIT               0:04:23         34          9          0          0    0:06:22               0
   5 rescheduled  T2_US_Wisconsin         0:04:22         82          3          0          0    0:06:28  Postprocessing failed
   6 rescheduled  T2_US_Wisconsin         0:04:21        606          3          0          0    0:06:31           50664
 1-1 finished     T2_US_Florida           0:02:48        554         15          0          0    0:03:56               0
 1-2 finished     T2_US_Wisconsin         0:02:47         38          4          0          0    0:04:41               0
 1-3 finished     T2_US_Wisconsin         0:03:30        664         48          0          0    0:02:56               0

Warning: the max jobs runtime is less than 30% of the task requested value (1250 min), please consider to request a lower value for failed jobs (allowed through crab resubmit) and/or improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task.

Warning: the average jobs CPU efficiency is less than 50%, please consider to improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task

Summary of run jobs:
 * Memory: 49MB min, 664MB max, 382MB ave
 * Runtime: 0:01:49 min, 0:04:23 max, 0:03:55 ave
 * CPU eff: 2% min, 48% max, 9% ave
 * Waste: 0:48:31 (58% of total)

Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/automatic/crab_20230608_024042/crab.log
belforte@lxplus814/automatic> 
```

I need to understand what is going on here.

## Comment (belforte, 2023-06-08T18:16:34Z)

` os.environ.get('HOSTNAME')` is already empty at the beginning ot PreDAG.py as started by
```
[crabtw@vocms059 SPOOL_DIR]$ tail -4 RunJobs0.subdag
ABORT-DAG-ON Job6 3

SUBDAG EXTERNAL Job1SubJobs RunJobs1.subdag NOOP
SCRIPT DEFER 4 300 PRE Job1SubJobs dag_bootstrap.sh PREDAG tail 6 1
[crabtw@vocms059 SPOOL_DIR]$ 
```

## Comment (belforte, 2023-06-08T18:27:02Z)

the problem is somehow inside/around dag_bootstrap.sh
For some reason when it is called for the tail PreDAG the env only contains CONDOR vars, even if
`echo $HOSTNAME` works, sort of it is set but not exported ?

Maybe something with new version of condor ?

## Comment (belforte, 2023-06-08T19:00:31Z)

the script is called in same way in the dag which works
```
[crabtw@vocms059 cluster9270919.proc0.subproc0]$ tail -4 RunJobs.dag
ABORT-DAG-ON Job0-5 3

SUBDAG EXTERNAL Job0SubJobs RunJobs0.subdag NOOP
SCRIPT DEFER 4 300 PRE Job0SubJobs dag_bootstrap.sh PREDAG processing 5 0
[crabtw@vocms059 cluster9270919.proc0.subproc0]$ 
```
and the one which does not
```
[crabtw@vocms059 cluster9270919.proc0.subproc0]$ tail -4 RunJobs0.subdag
ABORT-DAG-ON Job6 3

SUBDAG EXTERNAL Job1SubJobs RunJobs1.subdag NOOP
SCRIPT DEFER 4 300 PRE Job1SubJobs dag_bootstrap.sh PREDAG tail 6 1
[crabtw@vocms059 cluster9270919.proc0.subproc0]$ 

```

## Comment (belforte, 2023-06-08T19:07:22Z)

My best guess at this point is that the fact of being a subdag called from another subdag is what makes condor reset the environment

At the moment bottom line is therefore:
**HTCondor resets the environment when running a subdag, if we need any env. var. in our scripts, we have to export it explicitely in dag_bootstrap.sh**

## Comment (belforte, 2023-06-08T19:29:18Z)

to test this I am going to run original code, with the simple addition of
export HOSTNAME
in dag_bootstrap.sh

In a way it makes a lot of sense that condor_dagman runs in a new env. what is puzzling is that the subag for the processing jobs is OK, only the ones for the tail step has the cleaned env.

## Comment (belforte, 2023-06-08T21:35:54Z)

test confirmed that `export HOSTNAME` in `dag_bootstrap.sh` solves.

For the record, for debugging I found it useful to modify these two lines
https://github.com/dmwm/CRABServer/blob/88b6f1160ba7a3f0271e03048bfef59bfad26a18/scripts/dag_bootstrap.sh#L102
https://github.com/dmwm/CRABServer/blob/88b6f1160ba7a3f0271e03048bfef59bfad26a18/scripts/dag_bootstrap.sh#L111
adding .\`date +%s\` so that the `dag_bootstrap.env` and `dag_bootstrap.out` files are not overwritten everytime
 
In addition to a bunch of calls to logger.info in PreDAG.py, DagmanCreator.py and TaskManagerBootstrap.py

## Comment (belforte, 2023-06-08T21:42:36Z)

The hack needed to make processing jobs fail and thus force tail creating in reproducible ways is this change in PreJob.py
```diff
diff --git a/src/python/TaskWorker/Actions/PreJob.py b/src/python/TaskWorker/Actions/PreJob.py
index 6d10d96b..57f65bc7 100644
--- a/src/python/TaskWorker/Actions/PreJob.py
+++ b/src/python/TaskWorker/Actions/PreJob.py
@@ -287,6 +287,9 @@ class PreJob:
                 maxjobruntime = int(str(self.task_ad.lookup('MaxWallTimeMinsTail')))
             elif 'MaxWallTimeMinsRun' in self.task_ad:
                 maxjobruntime = int(str(self.task_ad.lookup('MaxWallTimeMinsRun')))
+                ##SB make processing jobs hit wall clock limit
+                maxjobruntime = 2
+                ##SB END
             if 'RequestMemory' in self.task_ad:
                 maxmemory = int(str(self.task_ad.lookup('RequestMemory')))
             if 'RequestCpus' in self.task_ad:
```
