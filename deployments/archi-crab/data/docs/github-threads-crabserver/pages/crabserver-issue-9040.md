# dmwm/CRABServer issue #9040: Inability to pickle 'htcondor2_impl._handle' object with childWorker enabled

State: closed
Opened: 2025-04-09T15:20:49Z
Closed: 2025-04-10T11:12:00Z
URL: https://github.com/dmwm/CRABServer/issues/9040

## Opening post (aspiringmind-code, 2025-04-09T15:20:49Z)

```
[vchakrav@lxplus975 myfirstcrabtask]$ crab submit --dryrun -c HC-1kj.py
Will use CRAB configuration file HC-1kj.py
Contacting voms-cms-auth.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.cern.ch] "cms"...
Remote VOMS server contacted succesfully.


Created proxy in /tmp/x509up_u150799.

Your proxy is valid until Thu Apr 17 16:41:09 CEST 2025
Importing CMSSW configuration pset.py
Finished importing CMSSW configuration pset.py
Sending the request to the server at cmsweb-testbed.cern.ch
Success: Your task has been delivered to the preprod CRAB3 server.
Task name: 250409_144114:vchakrav_crab_20250409_164107
Project dir: ./crab_20250409_164107
Waiting for task to be processed
Checking task status
Task status: WAITING
Please wait...
Task status: SUBMITFAILED
Error: The submission of your task has failed.
Failure message:	Process-2: I just had a failure for cannot pickle 'htcondor2_impl._handle' object
				workid=0
				task=250409_144114:vchakrav_crab_20250409_164107
			concurrent.futures.process._RemoteTraceback: 
			"""
			Traceback (most recent call last):
			  File "/usr/local/lib/python3.8/concurrent/futures/process.py", line 204, in _sendback_result
			    result_queue.put(_ResultItem(work_id, result=result,
			  File "/usr/local/lib/python3.8/multiprocessing/queues.py", line 362, in put
			    obj = _ForkingPickler.dumps(obj)
			  File "/usr/local/lib/python3.8/multiprocessing/reduction.py", line 51, in dumps
			    cls(buf, protocol).dump(obj)
			TypeError: cannot pickle 'htcondor2_impl._handle' object
			"""
			
			The above exception was the direct cause of the following exception:
			
			Traceback (most recent call last):
			  File "/data/srv/current/lib/python/site-packages/TaskWorker/Worker.py", line 106, in processWorkerLoop
			    workOutput = startChildWorker(WORKER_CONFIG, work, args, logger)
			  File "/data/srv/current/lib/python/site-packages
			[... message truncated to the first 1000 chars ...]
```

## Comment (belforte, 2025-04-09T15:36:07Z)

it is possible that error comes from this line
https://github.com/dmwm/CRABServer/blob/a23e98a82d22e01724318cc344e5a4e92eda74f2/src/python/TaskWorker/ChildWorker.py#L60
where, as found in #9014 , the output of the "work" contains an `htcondor.Submit()` object when the work chain stops before DagmanSubmitter

should get full traceback from TW log
