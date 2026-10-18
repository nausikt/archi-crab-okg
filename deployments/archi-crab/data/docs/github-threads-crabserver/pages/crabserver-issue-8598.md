# dmwm/CRABServer issue #8598: after moving to v2 bindings PostJob is not re-run after 1st time

State: closed
Opened: 2024-08-08T21:54:43Z
Closed: 2024-08-12T13:57:03Z
Labels: Type: Enhancement, Priority: High, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8598

## Opening post (belforte, 2024-08-08T21:54:43Z)

e.g. https://cmsweb-test2.cern.ch/crabserver/ui/task/240808_165343%3Acrabint1_crab_20240808_185342

hints:

[1] LAST RUN AT 19:01 WHILE NOW IT IS 23.47
[2] POST SCRIPTS ARE (CORRECTLY) LABELED AS "TO RERUN" IN NODE-STATE
[3] RunJobs.dag.dagman.out IS FULL OF `Max POST scripts (20) already running`


[1]
```
belforte@vocms059/SPOOL_DIR> date
Thu Aug  8 11:47:12 PM CEST 2024
belforte@vocms059/SPOOL_DIR> tail  postjob.999.0.txt
 'start_time': '2024-08-08 19:01:26.536718',
 'state': 'new',
 'type': 'output',
 'user': 'crabint1',
 'workflow': '240808_165343:crabint1_crab_20240808_185342'}
Thu, 08 Aug 2024 19:01:26 CEST(+0200):INFO:PostJob ====== Finished to check uploads to ASO database.
Thu, 08 Aug 2024 19:01:26 CEST(+0200):INFO:PostJob Deferring the execution of the post-job.
Thu, 08 Aug 2024 19:01:26 CEST(+0200):INFO:PostJob ********************************************************************************
======== Finished post-job execution with status code 4  : DEFERRING. PostJob will run again after 30 min
Ended TaskManagerBootstrap with code 4
belforte@vocms059/SPOOL_DIR> 
```

[2]
```
belforte@vocms059/SPOOL_DIR> tail -50 node_state 
[
  Type = "NodeStatus";
  Node = "Job996";
  NodeStatus = 4; /* "STATUS_POSTRUN" */
  StatusDetails = "";
  RetryCount = 0;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job997";
  NodeStatus = 4; /* "STATUS_POSTRUN" */
  StatusDetails = "";
  RetryCount = 0;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job998";
  NodeStatus = 5; /* "STATUS_DONE" */
  StatusDetails = "";
  RetryCount = 0;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job999";
  NodeStatus = 4; /* "STATUS_POSTRUN" */
  StatusDetails = "";
  RetryCount = 0;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "NodeStatus";
  Node = "Job1000";
  NodeStatus = 4; /* "STATUS_POSTRUN" */
  StatusDetails = "";
  RetryCount = 0;
  JobProcsQueued = 0;
  JobProcsHeld = 0;
]
[
  Type = "StatusEnd";
  EndTime = 1723153742; /* "Thu Aug  8 23:49:02 2024" */
  NextUpdate = 1723153772; /* "Thu Aug  8 23:49:32 2024" */
]
belforte@vocms059/SPOOL_DIR> 
```

[3]
```
08/08/24 23:49:32 Max POST scripts (20) already running; deferring POST script of Job Job544
```

## Comment (belforte, 2024-08-08T21:59:45Z)

hmmm. the problem in #8597 makes PostJob spend 15 minutes in a sleep/retry loop.
That likely explains. PostJob usually runs in seconds.
