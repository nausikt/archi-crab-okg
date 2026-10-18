# dmwm/CRABServer issue #9238: last PR #9236 breaks AS

State: closed
Opened: 2025-12-03T10:57:32Z
Closed: 2026-03-31T15:16:59Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9238

## Opening post (belforte, 2025-12-03T10:57:32Z)

I did not test automatic splitting in #9236 :-(

Currently AS tasks fail after probe jobs ran with
```
  File "/data/srv/glidecondor/condor_local/spool/504/0/cluster131710504.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PreDAG.py", line 133, in execute
  File "/data/srv/glidecondor/condor_local/spool/504/0/cluster131710504.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PreDAG.py", line 317, in executeInternal
  File "/data/srv/glidecondor/condor_local/spool/504/0/cluster131710504.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/DagmanCreator.py", line 1144, in createSubdag
UnboundLocalError: local variable 'dagConfigFileName' referenced before assignment
```

TW master is broken until this is fixed. Anyhow we also need to roll back https://github.com/dmwm/CRABServer/pull/9228 :-(

FYI @nausikt

## Comment (belforte, 2026-03-31T15:16:59Z)

fixed via #9240
