# dmwm/CRABServer issue #8935: latest DagmanCreator code only works with HTC v2 API

State: closed
Opened: 2025-02-18T16:41:16Z
Closed: 2025-02-20T12:05:49Z
URL: https://github.com/dmwm/CRABServer/issues/8935

## Opening post (belforte, 2025-02-18T16:41:16Z)

recent Dagamn* restructuring in https://github.com/belforte/CRABServer/commit/367e5692451b821683af7404cece63eed280d6ce introduced the use of `htcondor.Submit` object  in DagmanCreator . 
Code is "HTC v2 only" [*], but we have already set HTC API to v2 in all TaskWorkers.

But for "obscure" reasons the env. var. ` useHtcV2` is not propagated to PreDag when starting the tail subdags, only the processing subdag is OK. So submission of tail dagmans (e.g. in DagLog1.txt is failing with
```
  File "/data/srv/glidecondor/condor_local/spool/6407/0/cluster116926407.proc0.subproc0/TaskWorker/Actions/DagmanCreator.py", line 1158, in createSubdag
    if not 'My.CRAB_FailedNodeLimit' in jobSubmit:
TypeError: argument of type 'Submit' is not iterable
```

since processing DAG submission was OK, it was not easy to notice the problem.

Fixing the env. passing is not useful at this point. I will simply force usage of v2 API
I tested this on a task which had exhibited that failure: https://cmsweb.cern.ch/crabserver/ui/task/250217_154906%3Acerminar_crab_DoublePhoton_FlatPt-1To100_PU200

and it worked finely.


[*]
Down to technicalities , the semantycs of the HTCondor Submit() object is different in v1 [1] and v2[2].
v2 API is easier to work with and I had ended up in writing code which only works in v2 !


[1]
```text
[crabtw@vocms059 ~]$ python3
Python 3.9.21 (main, Dec  5 2024, 00:00:00) 
[GCC 11.5.0 20240719 (Red Hat 11.5.0-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor
>>> htcondor.version()
'$CondorVersion: 24.0.3 2025-01-03 BuildID: 777902 PackageID: 24.0.3-1 GitSHA: ef02b46e $'
>>> js=htcondor.Submit()
>>> js['a']='33'
>>> js
'a = 33\n'
>>> 'a' in js
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: argument of type 'Submit' is not iterable
>>> 
```

[2]
```text
[crabtw@vocms059 ~]$ python3
Python 3.9.21 (main, Dec  5 2024, 00:00:00) 
[GCC 11.5.0 20240719 (Red Hat 11.5.0-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor2
>>> htcondor2.version()
'$CondorVersion: 24.0.3 2025-01-03 BuildID: 777902 PackageID: 24.0.3-1 GitSHA: ef02b46e $'
>>> js=htcondor2.Submit()
>>> js['a']='33'
>>> js
Submit(a = 33
queue
)
>>> 'a' in js
True
>>> 
```

## Comment (belforte, 2025-02-18T16:46:14Z)

at this point I will simply enforce usage of Htcondor V2 API everywhere.
