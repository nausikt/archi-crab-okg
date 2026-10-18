# dmwm/CRABServer issue #9197: new REST v3.250929 is broken

State: closed
Opened: 2025-10-01T14:43:04Z
Closed: 2025-10-02T07:02:41Z
Labels: Type: Bug, Priority: Critical, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9197

## Opening post (belforte, 2025-10-01T14:43:04Z)

in spite of my thinking otherwise, it fails to pass the list of available schedds to the TW.
Every submission fails with
```text
2025-10-01 16:20:38,448:DEBUG:Handler,132:Starting <TaskWorker.Actions.DagmanSubmitter.DagmanSubmitter object at 0x7feb1e2a2550> on 251001_141955:belforte_crab_20251001_161953
2025-10-01 16:20:38,448:DEBUG:DagmanSubmitter,222:Picking up the scheduler using <function capacityMetricsChoicesHybrid at 0x7feb236fd940>
2025-10-01 16:20:38,451:ERROR:Handler,111:Problem handling 251001_141955:belforte_crab_20251001_161953 because of 'list' object has no attribute 'items' failure, traceback follows
Traceback (most recent call last):
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/Handler.py", line 97, in executeAction
    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/DagmanSubmitter.py", line 264, in execute
    self.pickAndSetSchedd(task)
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/DagmanSubmitter.py", line 228, in pickAndSetSchedd
    currentBackendurls['htcondorSchedds'] = { k:v for (k,v) in restSchedulers.items() if k not in alreadyTriedSchedds}
AttributeError: 'list' object has no attribute 'items'

```

Something is clearly not good with  `restSchedulers`

since we did not touch TW, the problem with  `restSchedulers` is likely due to the list received from REST

## Comment (belforte, 2025-10-01T15:05:18Z)

at first sight this is totallly wrong
https://github.com/dmwm/CRABServer/blob/e0dbc19825477c1f4a1efa27abf37557e4fd4cc3/src/python/CRABInterface/RESTServerInfo.py#L44-L50

1) `htcondorSchedds` must be a dictionary, not a list
2) this will return an empty object to the TW when called via
https://github.com/dmwm/CRABServer/blob/e0dbc19825477c1f4a1efa27abf37557e4fd4cc3/src/python/TaskWorker/Actions/TaskAction.py#L31

I do not understand how could I do something so stupid

## Comment (belforte, 2025-10-01T15:27:04Z)

fixed that. Now the problem is with the collector.

## Comment (belforte, 2025-10-01T16:09:51Z)

testing via https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13011862 (will test by hand the full schedd list)  was OK. So this does not break things.
