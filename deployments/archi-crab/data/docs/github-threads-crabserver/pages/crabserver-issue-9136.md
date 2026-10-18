# dmwm/CRABServer issue #9136: problems with Rucio retries

State: open
Opened: 2025-07-22T16:33:56Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9136

## Opening post (belforte, 2025-07-22T16:33:56Z)

I had a storm of submission failures while submitting CCV tests with logs like the following.
Clearly RUcio had a glitch, but.. shouldn't we be better protected ?
Can something be done ?

I am running from https://github.com/belforte/CRABServer/tree/remove-old-cache-status-code-9051 which should include your latest fixes for Rucio retries.

Logs for tasks which failed to submit are not available via web UI, anyhow they can be found on crab-dev-tw01 in
the TW logs/tasks/crabint1 directory looking for files with "small size" (3K vs. 30~50k)

Of course, if this was a user, we'd tell: submit again. My problem is that this is part of the pipeline where everything has to succeed and in a case like this thousands of jobs are submitted anyhow which will not be used for anything :-(


```text
crab3@crab-dev-tw01:/data/srv/TaskManager/logs/tasks/crabint1$ cat  250722_155937:crabint1_crab_activity.log
2025-07-22 18:00:33,505:DEBUG:Worker:Process-1: Starting <function handleNewTask at 0x7f9f7588e1f0> on 250722_155937:crabint1_crab_activity
2025-07-22 18:00:33,505:DEBUG:Worker:Run handleNewTask in childWorker.
2025-07-22 18:00:33,512:DEBUG:ChildWorker:Installing SIGALARM with timeout 3600 seconds.
2025-07-22 18:00:33,513:INFO:RucioUtils:Initializing native Rucio client
2025-07-22 18:00:33,513:DEBUG:RucioUtils:Using cert [/data/certs/robotcert.pem]
 and key [/data/certs/robotkey.pem] for rucio client.
2025-07-22 18:00:35,304:INFO:Worker:Uploading failure message to the REST:
Process-1: I just had a failure for An unknown exception occurred.
Details: no error information passed (http status code: 503)
	workid=0
	task=250722_155937:crabint1_crab_activity
concurrent.futures.process._RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/concurrent/futures/process.py", line 239, in _process_worker
    r = call_item.fn(*call_item.args, **call_item.kwargs)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/ChildWorker.py", line 95, in _runChildWorker
    outputs = work(*workArgs) # Run but don't return result (to avoid pickling issues); outputs variable helps debugging/inspection
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 174, in handleNewTask
    rucioClient = getNativeRucioClient(config=config, logger=handler.logger)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 93, in getNativeRucioClient
    ret = client.ping()
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 24, in wrapper
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/pingclient.py", line 44, in ping
    raise exc_cls(exc_msg)
rucio.common.exception.RucioException: An unknown exception occurred.
Details: no error information passed (http status code: 503)
"""

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Worker.py", line 106, in processWorkerLoop
    workOutput = startChildWorker(WORKER_CONFIG, work, args, logger)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/ChildWorker.py", line 60, in startChildWorker
    raise e
  File "/data/srv/current/lib/python/site-packages/TaskWorker/ChildWorker.py", line 54, in startChildWorker
    outputs = future.result(timeout=procTimeout + 1)
  File "/usr/local/lib/python3.8/concurrent/futures/_base.py", line 444, in result
    return self.__get_result()
  File "/usr/local/lib/python3.8/concurrent/futures/_base.py", line 389, in __get_result
    raise self._exception
rucio.common.exception.RucioException: An unknown exception occurred.
Details: no error information passed (http status code: 503)

2025-07-22 18:00:35,366:INFO:Worker:Failure message successfully uploaded to the REST
2025-07-22 18:00:35,366:DEBUG:Worker:Process-1: SUBMIT work on 250722_155937:crabint1_crab_activity completed in 1 seconds: Status: ERROR
Error = An unknown exception occurred.
Details: no error information passed (http status code: 503)

2025-07-22 18:00:35,377:DEBUG:Worker:RSS after finishing 250722_155937:crabint1_crab_activity: b'37.7812' MB
crab3@crab-dev-tw01:/data/srv/TaskManager/logs/tasks/crabint1$ 

```
