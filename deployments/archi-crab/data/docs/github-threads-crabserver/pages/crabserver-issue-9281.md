# dmwm/CRABServer issue #9281: not all RUcio calls are retried

State: closed
Opened: 2026-03-21T11:24:13Z
Closed: 2026-03-26T13:26:54Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9281

## Opening post (belforte, 2026-03-21T11:24:13Z)

Something slipped through in past attempt to retry all calls to Rucio which failed due to HTTP error ( #9096  #9243 )
Here's one example (dev=tw01, running master branch)

```
2026-03-20 20:13:27,386:WARNING:RucioUtils:Try Rucio lfn2pn with operation write
2026-03-20 20:13:29,159:WARNING:RucioUtils:Rucio lfn2pfn resolution for write failed with:
An unknown exception occurred.
Details: no error information passed (http status code: 503)
Try next one.
2026-03-20 20:13:29,161:DEBUG:Handler:Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 97, in executeAction
    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanCreator.py", line 1304, in execute
    jobSubmit, params, inputFiles, splitterResult = self.executeInternal(*args, **kw)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanCreator.py", line 1265, in executeInternal
    jobSubmit, splitterResult, subdags = self.createSubdag(*args, **kw)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanCreator.py", line 1054, in createSubdag
    jobgroupDagSpecs, startjobid = self.makeDagSpecs(
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanCreator.py", line 649, in makeDagSpecs
    lastDirectPfn = getWritePFN(self.rucioClient, siteName=task['tm_asyncdest'], lfn=directDest,
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 166, in getWritePFN
    raise TaskWorkerException(msg)
TaskWorker.WorkerExceptions.TaskWorkerException: lfn2pfn resolution with Rucio failed for site: T2_CH_CERN  LFN: /store/user/crabint1/GenericTTbar/CrabAutoTest_whitelist/260320_185815/0000 with exception(s) :
operation: write, exception: An unknown exception occurred.
Details: no error information passed (http status code: 503)

```

## Comment (nausikt, 2026-03-26T12:08:15Z)

Ahh, sorry, i saw this but forgot to response.

## Comment (belforte, 2026-03-26T13:26:54Z)

Duplicate of #9285
