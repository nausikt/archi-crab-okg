# dmwm/CRABServer issue #9392: odd error in RenewRemoteProxies

State: open
Opened: 2026-08-24T07:49:38Z
URL: https://github.com/dmwm/CRABServer/issues/9392

## Opening post (belforte, 2026-08-24T07:49:38Z)

from  ` /data/srv/TaskManager/logs/tasks/recurring/RenewRemoteProxies.260823_192059.log` on `crab-prod-tw02`

Process-2: I just had a failure for 
	workid=0
	task=RenewRemoteProxies.260823_192059
Traceback (most recent call last):
  File "/data/repos/CRABServer/src/python/TaskWorker/Worker.py", line 106, in processWorkerLoop
    workOutput = startChildWorker(WORKER_CONFIG, work, args, logger)
  File "/data/repos/CRABServer/src/python/TaskWorker/ChildWorker.py", line 60, in startChildWorker
    raise e
  File "/data/repos/CRABServer/src/python/TaskWorker/ChildWorker.py", line 54, in startChildWorker
    outputs = future.result(timeout=procTimeout + 1)
  File "/usr/lib64/python3.9/concurrent/futures/_base.py", line 448, in result
    raise TimeoutError()
concurrent.futures._base.TimeoutError


2026-08-23 23:08:30,074:ERROR:RESTInteractions:Rejected request when connecting to https://cmsweb.cern.ch:8443/crabserver/prod/workflowdb using workflow=RenewRemoteProxies.260823_192059&status=FAILED&subresource=failure&failure=Process-2%3A+I+just+had+a+failure+for+%0A%09workid%3D0%0A%09task%3DRenewRemoteProxies.260823_192059%0ATraceback+%28most+recent+call+last%29%3A%0A++File+%22%2Fdata%2Frepos%2FCRABServer%2Fsrc%2Fpython%2FTaskWorker%2FWorker.py%22%2C+line+106%2C+in+processWorkerLoop%0A++++workOutput+%3D+startChildWorker%28WORKER_CONFIG%2C+work%2C+args%2C+logger%29%0A++File+%22%2Fdata%2Frepos%2FCRABServer%2Fsrc%2Fpython%2FTaskWorker%2FChildWorker.py%22%2C+line+60%2C+in+startChildWorker%0A++++raise+e%0A++File+%22%2Fdata%2Frepos%2FCRABServer%2Fsrc%2Fpython%2FTaskWorker%2FChildWorker.py%22%2C+line+54%2C+in+startChildWorker%0A++++outputs+%3D+future.result%28timeout%3DprocTimeout+%2B+1%29%0A++File+%22%2Fusr%2Flib64%2Fpython3.9%2Fconcurrent%2Ffutures%2F_base.py%22%2C+line+448%2C+in+result%0A++++raise+TimeoutError%28%29%0Aconcurrent.futures._base.TimeoutError%0A. Error details: {'content-type': 'text/html;charset=utf-8', 'date': 'Sun, 23 Aug 2026 21:08:30 GMT', 'response-proto': 'HTTP/1.1', 'response-status': '400 Bad Request', 'response-status-code': '400', 'response-time': '3.278902ms', 'response-time-seconds': '0.003279662', 'x-content-type-options': 'bla', 'x-error-detail': 'Invalid input parameter', 'x-error-http': '400', 'x-error-id': '281934be19ff9c7a8ff24516820cab5e', 'x-error-info': "Incorrect 'workflow' parameter <class 'str'> RenewRemoteProxies.260823_192059", 'x-rest-status': '302', 'x-rest-time': '794.649 us', 'content-length': '734'}


why ` 'Invalid input parameter' ?
maybe we can't upload messages from RenewRemoteProxies ?

## Comment (oljemark, 2026-08-26T10:46:25Z)

Hi @belforte . Is the period in "RenewRemoteProxies.260823_192059" an allowed character in RX_TASKNAME? I see it specifically added in RX_LFN, but it seems like only alphanumerics, dash, underscore and colon are allowed in workflow parameter?

## Comment (belforte, 2026-08-26T12:44:13Z)

Hi @oljemark , yes, I believe that the unusual format of the workflow name is reason. And I was leaving to @nausikt to confirm and propose a solution. It is also to be noted that recurring actions are injected in the TW queue w/o ever being "workflow" in the database, so there is no place where to upload such messages !
Simply it is better to keep our log w/o fake error.

## Comment (nausikt, 2026-08-26T14:41:53Z)

Thank you @oljemark! @belforte  We will neither allow the dot in `RX_TASKNAME` nor trying to make local recurring action taskname `RenewRemoteProxies_260823_192059` comply with RX_TASKNAME.

We may simply skip uploading via `failTask` if `task['tm_taskname']` start with `RenewRemoteProxies` Since we don't have recurring action kept in db anyhow as Stefano said. (skipping all REST calls for certain Actions?)
https://github.com/dmwm/CRABServer/blob/6c1e83e10af760bc2a62cc7b3c9a56d59fae3246/src/python/TaskWorker/Worker.py#L137-L142

Will this solution acceptable? though i don't like patching if-else this way but its seems to be the simplest one. Let me hear your thoughts! 🙇🏻

## Comment (belforte, 2026-08-26T15:33:30Z)

I would rather figure out what RenewRemoteProxies was trying to do, and prevent it from doing it, if possible. The piece of traceback which I pasted in the initial comment says very little. And I do not like mysteries !

## Comment (belforte, 2026-08-26T15:51:25Z)

I just got the scary thought that maybe RenewRemoteProxies always times out in the worker and we never renew all proxies ? 😨

## Comment (nausikt, 2026-08-26T16:07:15Z)

It started to be scary to me too, At first i thought that it just occasionally time out due temporary overloaded of myproxy server.

## Comment (belforte, 2026-08-26T17:02:47Z)

I expect that errors in communication with myproxy are currently handled, original developers hopefully thought of that. But yeah... we need to investigate before we hide the error under the carpet !
