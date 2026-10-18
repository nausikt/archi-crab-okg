# dmwm/CRABServer issue #8792: automatic splitting fails on missing throughput file

State: closed
Opened: 2024-11-14T09:12:09Z
Closed: 2024-11-15T10:21:57Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/8792

## Opening post (belforte, 2024-11-14T09:12:09Z)

I found this while looking at stuck automatic task in the CI pipeline
https://cmsweb-testbed.cern.ch/crabserver/ui/task/241113_203248%3Acrabint1_crab_20241113_213248
```text
[crabtw@vocms059 SPOOL_DIR]$ cat prejob_logs/predag.1.txt 
Wed, 13 Nov 2024 21:59:30 CET(+0100):INFO:PreDAG Pre-DAG started with output redirected to /data/srv/glidecondor/condor_local/spool/6837/0/cluster9976837.proc0.subproc0/prejob_logs/predag.1.txt
Wed, 13 Nov 2024 21:59:30 CET(+0100):INFO:PreDAG found 1 completed jobs
Wed, 13 Nov 2024 21:59:30 CET(+0100):INFO:PreDAG jobs remaining to process: 1
Wed, 13 Nov 2024 21:59:30 CET(+0100):INFO:PreDAG found 5 completed jobs
Wed, 13 Nov 2024 21:59:30 CET(+0100):INFO:PreDAG jobs remaining to process: 1
Got a fatal exception: [Errno 2] No such file or directory: 'automatic_splitting/throughputs/0-4'
Traceback (most recent call last):
  File "/usr/lib64/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib64/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/data/srv/glidecondor/condor_local/spool/6837/0/cluster9976837.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py", line 24, in <module>
    retval = bootstrap()
  File "/data/srv/glidecondor/condor_local/spool/6837/0/cluster9976837.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py", line 18, in bootstrap
    return PreDAG.PreDAG().execute(*sys.argv[2:])
  File "/data/srv/glidecondor/condor_local/spool/6837/0/cluster9976837.proc0.subproc0/TaskWorker/Actions/PreDAG.py", line 135, in execute
    retval = self.executeInternal(*args)
  File "/data/srv/glidecondor/condor_local/spool/6837/0/cluster9976837.proc0.subproc0/TaskWorker/Actions/PreDAG.py", line 244, in executeInternal
    with open(fn, 'r', encoding='utf-8') as fd:
FileNotFoundError: [Errno 2] No such file or directory: 'automatic_splitting/throughputs/0-4'
[crabtw@vocms059 SPOOL_DIR]$ ls automatic_splitting/
processed  throughputs
[crabtw@vocms059 SPOOL_DIR]$ ls automatic_splitting/throughputs/
0-1  0-2  0-3  0-5
[crabtw@vocms059 SPOOL_DIR]$ 


```

## Comment (belforte, 2024-11-14T09:17:06Z)

probe #4 failed, but that's "normal". Usually it does not result in error.
Also main processing was submitted, in spite of the error message. But it failed and tails jobs were not submitted.
![image](https://github.com/user-attachments/assets/34e9333d-4aa3-439d-b07d-a7bd1f6291f9)

## Comment (belforte, 2024-11-14T09:57:22Z)

looks like the problem is to run a tail step w/o info on the main one. The file `automatic_splitting/processed` only has info from the probe jobs
```text
>>> f=open('automatic_splitting/processed','rb')
>>> r=pickle.load(f)
>>> r
{'0-1', '0-3', '0-4', '0-5', '0-2'}
>>> 
```
which may have something to do with the odd log
```text
Wed, 13 Nov 2024 21:59:30 CET(+0100):INFO:PreDAG found 1 completed jobs
Wed, 13 Nov 2024 21:59:30 CET(+0100):INFO:PreDAG jobs remaining to process: 1
Wed, 13 Nov 2024 21:59:30 CET(+0100):INFO:PreDAG found 5 completed jobs
Wed, 13 Nov 2024 21:59:30 CET(+0100):INFO:PreDAG jobs remaining to process: 1
```

## Comment (belforte, 2024-11-14T10:08:31Z)

last lines of `dag_bootstrap.out`
```text
Entering TaskManagerBootstrap with args: ['/data/srv/glidecondor/condor_local/spool/6837/0/cluster9976837.proc0.subproc0/TaskWorker/TaskManagerBootstrap.py', 'PREDAG', 'tail', '1', '1']
Wed, 13 Nov 2024 21:59:30 CET(+0100):DEBUG:PreDAG Acquiring PreDAG lock
Wed, 13 Nov 2024 21:59:30 CET(+0100):DEBUG:PreDAG PreDAGlock acquired
```

## Comment (belforte, 2024-11-14T12:01:30Z)

after some debugging I believe that in here
https://github.com/dmwm/CRABServer/blob/3b2e705c8c5458135c57dfe88d1107aea075c26f/src/python/TaskWorker/Actions/PreDAG.py#L112-L127
Line 123 is wrong, it should be instead
```
if state == 'failed' and not processFailed: 
```
That will make the error in this issue go away. But since things are usually working, there may be something more.

## Comment (belforte, 2024-11-14T12:45:29Z)

I believe this problem only happens when all `processing` jobs fail (in our test there is only one such job ! so chances of this increase) and some probe failed.
This lines tell PreDag to use probe jobs for the new splitting estimate since processing jobs failed
https://github.com/dmwm/CRABServer/blob/3b2e705c8c5458135c57dfe88d1107aea075c26f/src/python/TaskWorker/Actions/PreDAG.py#L200-L201
but for reasons obscure to me `processFailed` is set to `False` which makes failed jobs NOT skipped (!!)
https://github.com/dmwm/CRABServer/blob/3b2e705c8c5458135c57dfe88d1107aea075c26f/src/python/TaskWorker/Actions/PreDAG.py#L123-L124
while "normally" the default `processFailed=True` is used
https://github.com/dmwm/CRABServer/blob/3b2e705c8c5458135c57dfe88d1107aea075c26f/src/python/TaskWorker/Actions/PreDAG.py#L174

Surely variable naming is confusing !
Also the fact that the `completedJobs()` method looks for completed jobs in the stage preceding the one indicated as argument
https://github.com/dmwm/CRABServer/blob/3b2e705c8c5458135c57dfe88d1107aea075c26f/src/python/TaskWorker/Actions/PreDAG.py#L117-L118

At this point I have no idea why the `processFailed` argument was introduced. Seems like the original implementor wanted to say:
_"if all jobs in this stage failed, go back to previous stage to generate splitting parameters, but take into account also failed jobs which were skipped before."_

But failed jobs have no throughput report, so can't be used !

## Comment (belforte, 2024-11-14T12:55:41Z)

I made that task DAG complete successfully by [rerunning PreDag manually](https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3OperatorDebugging#To_run_the_preDag_on_the_schedd) after changing
https://github.com/dmwm/CRABServer/blob/3b2e705c8c5458135c57dfe88d1107aea075c26f/src/python/TaskWorker/Actions/PreDAG.py#L201 to
```python
         estimates = set(self.completedJobs(stage='processing', processFailed=True))
```
which basically forces submission of a tail job with same config. as the processing one (OK, since the failure was an accidental 8028). 

But I am still worried that making the change in the code for everybody may trigger problems in different situations which I can not imagine/test no.

## Comment (belforte, 2024-11-14T12:58:34Z)

Maybe there are situations where processing jobs fail, but still produce a report ? E.g. if they hit the time limit ?
https://github.com/dmwm/CRABServer/blob/3b2e705c8c5458135c57dfe88d1107aea075c26f/scripts/TweakPSet.py#L209-L212

Or will they count as successful ?

## Comment (belforte, 2024-11-14T13:20:01Z)

that `processFailed` argument was introduced in https://github.com/dmwm/CRABServer/commit/90c08419c59254464a10699415aba61419cb244e

No comments. no issue.

I am still unsure what to do.

## Comment (belforte, 2024-11-14T13:55:44Z)

some (but not all) probe jobs failing and all processing jobs failing is all in all a very rare case.
Also fixing this does not help the CI pipeline to complete becasue current code still sees one failed job (the processing one) and keeps trying to resubmit.
Will have to fix the pipeline first to properly deal with automatic splitting: https://github.com/dmwm/CRABServer/issues/8794

## Comment (belforte, 2024-11-14T16:38:41Z)

I have prepared PR #8795   with that fix. But need to think more about possible side effects

## Comment (belforte, 2024-11-15T10:19:21Z)

I am now convinced that the problematic line
https://github.com/dmwm/CRABServer/blob/3b2e705c8c5458135c57dfe88d1107aea075c26f/src/python/TaskWorker/Actions/PreDAG.py#L201
is only relevant when all processing jobs fail. And therefore it is correct to change. If the problem never surfaces it must be because all processing jobs failing is very rare and never happened together with some probes also failing.
