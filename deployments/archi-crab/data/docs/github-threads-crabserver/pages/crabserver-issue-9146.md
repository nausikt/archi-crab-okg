# dmwm/CRABServer issue #9146: failed Rucio call is not retried ?

State: closed
Opened: 2025-08-06T21:01:45Z
Closed: 2026-08-12T07:42:42Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9146

## Opening post (belforte, 2025-08-06T21:01:45Z)

from this TW log https://s3.cern.ch/crabcache_dev/crabint1/250806_185658%3Acrabint1_crab_sendVenvFolder/twlog?AWSAccessKeyId=715203df6482458ba839e73e6dab634b&Signature=TML9cvIzjD1vwTvzVntR6lDHE1E%3D&Expires=1757105939

here are relevant lines
```
2025-08-06 21:01:21,410:DEBUG:Handler:Starting <TaskWorker.Actions.StageoutCheck.StageoutCheck object at 0x7f64c40d9ee0> on 250806_185658:crabint1_crab_sendVenvFolder
2025-08-06 21:01:21,420:INFO:ServerUtilities:Will use GFAL2 commands for checking write permissions
2025-08-06 21:01:21,420:INFO:StageoutCheck:Will check stageout at T2_CH_CERN
2025-08-06 21:01:21,421:WARNING:RucioUtils:Try Rucio lfn2pn with operation third_party_copy_write
2025-08-06 21:01:23,194:WARNING:RucioUtils:Rucio lfn2pfn resolution for third_party_copy_write failed with:
An unknown exception occurred.
Details: no error information passed (http status code: 503)
Try next one.
2025-08-06 21:01:23,195:INFO:ServerUtilities:Warning: Failed to delete file 250806185658crabint1crabsendenvolder_crab3check.tmp
2025-08-06 21:01:23,197:DEBUG:Handler:Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 97, in executeAction
    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/StageoutCheck.py", line 130, in execute
    pfn = getWritePFN(self.rucioClient, siteName=self.task['tm_asyncdest'], lfn=lfn, operations=['third_party_copy_write'], logger=self.logger)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 139, in getWritePFN
    raise TaskWorkerException(msg)
TaskWorker.WorkerExceptions.TaskWorkerException: lfn2pfn resolution with Rucio failed for site: T2_CH_CERN  LFN: /store/user/crabint1/250806185658crabint1crabsendenvolder_crab3check.tmp with exception(s) :
operation: third_party_copy_write, exception: An unknown exception occurred.
Details: no error information passed (http status code: 503)
```

after the log is uploaded.

## Comment (belforte, 2026-07-03T10:08:18Z)

possibly relates with #9136

## Comment (belforte, 2026-08-12T07:42:42Z)

should have been solved by now with #9296
