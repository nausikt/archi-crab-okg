# dmwm/CRABServer issue #8571: introduce a software switch for using HTC bindings v2

State: closed
Opened: 2024-07-29T16:36:01Z
Closed: 2024-08-09T23:14:12Z
Labels: Status: Done, Priority: High, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8571

## Opening post (belforte, 2024-07-29T16:36:01Z)

- [x] a switch in TaskWorkerConfig.py
- [x] pass this info to Scheduler via a file in the spool directory. Each python script will check that file presence at the beginning before doing `import htcondor` or `import htcondor2 as htcondor`
  * Changed to use an env.variable defined in the submit JDL of the job submitted by DagmanSubmitter

## Comment (mapellidario, 2024-07-30T09:30:00Z)

is creating a file in the spool directory the best we can do? do we dislike so much adding an argument in the calls from TW to the schedd?

## Comment (belforte, 2024-07-30T09:39:58Z)

There no "free arguments". In the call we pass am HTCondor JDL. We could use an env.variable which will be part of the env. where the dag_bootstrap_startup.sh runs. Let's try that

## Comment (belforte, 2024-07-30T22:11:38Z)

the pro side of using a file is that it makes it easy to tell if a task is/was using new bindings, but I can still create the file in the dag_bootstrap_startup.sh. An env var  may be more elegant to test in the various python scripts

## Comment (mapellidario, 2024-07-31T10:16:47Z)

Well, env variables are printed in the job stdout, it is not that different from checking that a file is in the spool directory

## Comment (belforte, 2024-07-31T10:40:40Z)

matter of taste, you need `sudo crabtw` to read `_condor.stdout` and it is too long for my taste

## Comment (belforte, 2024-08-01T18:44:52Z)

https://github.com/belforte/CRABServer/tree/allow-v2-bindings-8571 now has a solution for TW
* `config.TaskWorker.useHtcV2 = True` in TaskWorkerConfig.py (if missing, means False)
* managed via Hiera in puppet, can be set in the host.cern.ch.yaml file
* parsed inside `manage.sh` to set an env. variable which is used in TW code to decide whch version to import

@novicecpp @mapellidario feel free to look at [comparison with master](https://github.com/dmwm/CRABServer/compare/master...belforte:CRABServer:allow-v2-bindings-8571?expand=1) and comment

Now I need to pass the env. variable to the dagman startup job in the scheduler and use it in all scripts there.

## Comment (belforte, 2024-08-01T19:07:52Z)

automatic splitting is failing in an odd way. Let's  use consistently v1 or v2 before worrying more

08/01/24 16:11:23 ERROR: node Job1: job ID in userlog submit event (9693669.0.0) doesn't match ID reported earlier by submit command (9693668.0.0)!  Aborting DAG; set DAGMAN_ABORT_ON_SCARY_SUBMIT to false if you are *sure* this shouldn't cause an abort.

## Comment (belforte, 2024-08-02T17:51:18Z)

the problem persists when using v2 also in scheduler scripts and comes from DagmanSubmitter, it is due to a chance in HTCondor:   https://github.com/dmwm/CRABServer/issues/8272#issuecomment-2265870173

I will look into a fix. But for the scope of this issue, I think I am OK. Anyhow it is fixed in master branch now ! 
https://github.com/dmwm/CRABServer/pull/8586

## Comment (belforte, 2024-08-07T17:01:05Z)

after some trial and error and a discussion among Dario/Stefano/Wa described in #8584 we have settled on the following strategy (a simpler variant of https://github.com/dmwm/CRABServer/issues/8571#issuecomment-2263734339 ) 

 *  config.TaskWorker.useHtcV2 = True in TaskWorkerConfig.py (if missing, means False)
 *  managed via Hiera in puppet, can be set in the host.cern.ch.yaml file
 *  used inside TaskWorkerConfig.py itself to set `$useHtcV2` in the environment, which in turn is used in TW code to decide what to import
 *  pass  `$useHtcV2` env.var. to scripts which run in the scheduler via `environment` directive in jobJDL

## Comment (belforte, 2024-08-08T21:34:47Z)

Possibley unrelated to changes here, I have identied problems with PostJob https://github.com/dmwm/CRABServer/issues/8598
1. it does not run again after detecting transfer in progres, so job is stuck in transferring forever
2. it uses the deprecated Transation method which was removed in v2 https://github.com/dmwm/CRABServer/issues/8597
```text
Thu, 08 Aug 2024 20:19:19 CEST(+0200):ERROR:PostJob Exception in setting job ClassAd attributes:
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/3155/0/cluster9703155.proc0.subproc0/TaskWorker/Actions/PostJob.py", line 2917, in set_state_ClassAds
    with self.schedd.transaction(htcondor.TransactionFlags.NonDurable):
AttributeError: 'Schedd' object has no attribute 'transaction'
```

## Comment (belforte, 2024-08-08T21:35:26Z)

I will simply make sure that things still work for v1 and them we can integrate this to keep debuggin v2
