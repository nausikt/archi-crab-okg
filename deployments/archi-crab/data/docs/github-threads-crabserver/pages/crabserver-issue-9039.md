# dmwm/CRABServer issue #9039: crab submit --dryrun failed got KeyError: 'CRAB_AdditionalOutputFiles'

State: closed
Opened: 2025-04-09T13:09:52Z
Closed: 2025-04-09T13:56:15Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9039

## Opening post (nausikt, 2025-04-09T13:09:52Z)

Issue still there even after 1st April patches. Regarding User's report in [CMS-Talk](https://cms-talk.web.cern.ch/t/crab-error-keyerror-crab-additionaloutputfiles/122751)
Log:
```
[kphornsi@lxplus945 workspace]$ crab submit --dryrun -c HC-1kj.py
Will use CRAB configuration file HC-1kj.py
Importing CMSSW configuration pset.py
Finished importing CMSSW configuration pset.py
Sending the request to the server at cmsweb.cern.ch
Success: Your task has been delivered to the prod CRAB3 server.
Task name: 250409_130229:kphornsi_crab_20250409_150224
Project dir: /tmp/crabStatusTracking/crab_20250409_150224
Waiting for task to be processed
Checking task status
Task status: WAITING
Please wait...
Task status: WAITING
Please wait...
Task status: QUEUED
Please wait...
Task status: UPLOADED

Dry run
Getting input files into tmp dir /tmp/kphornsi/tmpf2o44qct
Copying and preparing files for local execution in /tmp/crabStatusTracking/crab_20250409_150224/local
ERROR: KeyError: 'CRAB_AdditionalOutputFiles'

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /tmp/crabStatusTracking/crab_20250409_150224/crab.log to the CRAB cache.
```

## Comment (belforte, 2025-04-09T13:21:30Z)

oddily I get a different error:
```
Getting input files into tmp dir /tmp/belforte/tmpgsfz43sw
Copying and preparing files for local execution in /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250409_142311/local
go to that directory IN A CLEAN SHELL and use  'sh run_job.sh NUMJOB' to execute the job
Execute rest run in local sub-directory of ./crab_20250409_142311
Executing test, please wait...
ERROR: FileNotFoundError: [Errno 2] No such file or directory: 'JobArgs-1.json'
```

## Comment (belforte, 2025-04-09T13:25:16Z)

seems like for user and Krittin the `KeyError: 'CRAB_AdditionalOutputFiles'` strikes before the local subdir is ready

## Comment (belforte, 2025-04-09T13:32:36Z)

client log for Krittin's test above has
```text
INFO 2025-04-09 13:04:02.145 UTC: 	 Copying and preparing files for local execution in /tmp/crabStatusTracking/crab_20250409_150224/local
DEBUG 2025-04-09 13:04:02.145 UTC: 	 Creating InputArgs.txt file
ERROR 2025-04-09 13:04:02.149 UTC: 	 Unhandled Exception!
ERROR 2025-04-09 13:04:02.149 UTC: 	 'CRAB_AdditionalOutputFiles'
Traceback (most recent call last):
  File "/eos/user/k/kphornsi/WORK/CRABClient/bin/crab.py", line 157, in <module>
    client()
  File "/eos/user/k/kphornsi/WORK/CRABClient/bin/crab.py", line 142, in __call__
    returnDict = self.cmd()
  File "/eos/user/k/kphornsi/WORK/CRABClient/src/python/CRABClient/Commands/submit.py", line 167, in __call__
    self.runPrepareLocal(projDir)
  File "/eos/user/k/kphornsi/WORK/CRABClient/src/python/CRABClient/Commands/submit.py", line 194, in runPrepareLocal
    retval = preparelocalCmd()
  File "/eos/user/k/kphornsi/WORK/CRABClient/src/python/CRABClient/Commands/preparelocal.py", line 50, in __call__
    self.prepareDir(inputArgs, self.options.destdir)
  File "/eos/user/k/kphornsi/WORK/CRABClient/src/python/CRABClient/Commands/preparelocal.py", line 153, in prepareDir
    inputArgsForScript[key] = jobArgs[value]
KeyError: 'CRAB_AdditionalOutputFiles'
ERROR 2025-04-09 13:04:02.179 UTC: 	 ERROR: KeyError: 'CRAB_AdditionalOutputFiles'
ERROR 2025-04-09 13:04:02.180 UTC: 	
```

## Comment (belforte, 2025-04-09T13:33:17Z)

@sinonkt see log above. Seems that you are using a local version of client. Please verify `crab --version`

## Comment (nausikt, 2025-04-09T13:35:58Z)

> [@sinonkt](https://github.com/sinonkt) see log above. Seems that you are using a local version of client. Please verify `crab --version`

it does, i confusing myself with my alias when doing the development on client!
```
[kphornsi@lxplus945 workspace]$ crab --version
CRAB client development
```

## Comment (belforte, 2025-04-09T13:45:10Z)

I can reproduce the 
```
ERROR: KeyError: 'CRAB_AdditionalOutputFiles'
```
with `crab-pre`. 
So the fix for that is in `crab-prod already :-) . But we need a fix for
``` 
No such file or directory: 'JobArgs-1.json'
```

Most likely that was due to an attempt not to break crab preparelocal on what is now old TW. I suspect that we need a new client version here.

## Comment (nausikt, 2025-04-09T13:50:12Z)

I can confirm on `crab-pre` too, its still strikes before local sub dir in my case.
BUT, can't on `prod`.
```
[kphornsi@lxplus804 WORKSPACE]$ which crab
/cvmfs/cms.cern.ch/common/crab
[kphornsi@lxplus804 WORKSPACE]$ crab --version
CRAB client v3.250318
```
I got totally diferent error.
```
[kphornsi@lxplus804 WORKSPACE]$ crab submit --dryrun -c HC-10j.py
Will use CRAB configuration file HC-10j.py
Importing CMSSW configuration pset.py
Finished importing CMSSW configuration pset.py
Sending the request to the server at cmsweb.cern.ch
Success: Your task has been delivered to the prod CRAB3 server.
Task name: 250409_134348:kphornsi_crab_20250409_154341
Project dir: /tmp/crabStatusTracking/crab_20250409_154341
Waiting for task to be processed
Checking task status
Task status: WAITING
Please wait...
Task status: HOLDING
Please wait...
Task status: SUBMITFAILED
Error: The submission of your task has failed.
Failure message:	Process-1: I just had a failure for cannot pickle 'htcondor2_impl._handle' object
				workid=1
				task=250409_134348:kphornsi_crab_20250409_154341
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

Dry run
Getting input files into tmp dir /tmp/kphornsi/tmpuxd_Pz
Thic only works for tasks submitted to or uploaded. Current status is SUBMITFAILED
```

## Comment (belforte, 2025-04-09T13:50:25Z)

anyhow this is a CRABClient problem. WIll move to that repo.

## Comment (belforte, 2025-04-09T13:56:15Z)

moved to https://github.com/dmwm/CRABClient/issues/5383

## Comment (belforte, 2025-04-09T14:25:30Z)

@sinonkt the error in https://github.com/dmwm/CRABServer/issues/9039#issuecomment-2789808874 is **really** worrying. That happens with the TW version before the fix for "do not push un-pickleable objects to multiprocessing Queue()".

Unless there is a problem with what we run in canary :-(

@aspiringmind-code please configure crab-preprod-tw01 the same way as canary and test `submit --dryrun` there. If it is reproducible it means that the fix which I put is not sufficient. Ref: https://github.com/dmwm/CRABServer/pull/9026
In that case up to you if to fix it yourself or hand it to me.

## Comment (belforte, 2025-04-09T14:26:37Z)

@sinonkt can you tell if in your case the task was processed by prod or canary TW ? `crab status` should do.

## Comment (nausikt, 2025-04-09T14:29:34Z)

> [@sinonkt](https://github.com/sinonkt) can you tell if in your case the task was processed by prod or canary TW ? `crab status` should do.

I can confirm. it's processed on crab-prod-tw02
```
[kphornsi@lxplus804 WORKSPACE]$ crab status --task=250409_134348:kphornsi_crab_20250409_154341
crab status requires a projdir. Since you passed a taskname, we will run crab remake
Remaking crab_20250409_154341 folder.
Remaking .requestcache file.
Success: Finished remaking project directory crab_20250409_154341
/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-requests/2.21.0-pafccj2/lib/python3.6/site-packages/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.25.2) or chardet (3.0.4) doesn't match a supported version!
  RequestsDependencyWarning)
Rucio client intialized for account kphornsi
CRAB project directory:		/eos/home-k/kphornsi/WORK/CMSSW_10_6_26/WORKSPACE/crab_20250409_154341
Task name:			250409_134348:kphornsi_crab_20250409_154341
Grid scheduler - Task Worker:	N/A yet - crab-prod-tw02
Status on the CRAB server:	SUBMITFAILED
```

## Comment (nausikt, 2025-04-09T14:39:01Z)

> [@sinonkt](https://github.com/sinonkt) the error in [#9039 (comment)](https://github.com/dmwm/CRABServer/issues/9039#issuecomment-2789808874) is **really** worrying. That happens with the TW version before the fix for "do not push un-pickleable objects to multiprocessing Queue()".
> 
> Unless there is a problem with what we run in canary :-(
> 
> [@aspiringmind-code](https://github.com/aspiringmind-code) please configure crab-preprod-tw01 the same way as canary and test `submit --dryrun` there. If it is reproducible it means that the fix which I put is not sufficient. Ref: [#9026](https://github.com/dmwm/CRABServer/pull/9026) In that case up to you if to fix it yourself or hand it to me.

@belforte and can also confirm that when task landed on `crab-prod-tw01` it converged to different `ERROR: KeyError: CRAB_AdditionalOutputFiles` error from `crab-prod-tw02` pickle error.

```
[kphornsi@lxplus804 WORKSPACE]$ crab status --task=250409_143314:kphornsi_crab_20250409_163310
crab status requires a projdir. Since you passed a taskname, we will run crab remake
Remaking crab_20250409_163310 folder.
Remaking .requestcache file.
Success: Finished remaking project directory crab_20250409_163310
/cvmfs/cms.cern.ch/slc7_amd64_gcc700/external/py2-requests/2.21.0-pafccj2/lib/python3.6/site-packages/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.25.2) or chardet (3.0.4) doesn't match a supported version!
  RequestsDependencyWarning)
Rucio client intialized for account kphornsi
CRAB project directory:		/eos/home-k/kphornsi/WORK/CMSSW_10_6_26/WORKSPACE/crab_20250409_163310
Task name:			250409_143314:kphornsi_crab_20250409_163310
Grid scheduler - Task Worker:	N/A yet - crab-prod-tw01
Status on the CRAB server:	UPLOADED
```

```
[kphornsi@lxplus804 WORKSPACE]$ crab-pre submit --dryrun -c HC-10j.py
Will use CRAB configuration file HC-10j.py
Importing CMSSW configuration pset.py
Finished importing CMSSW configuration pset.py
Sending the request to the server at cmsweb.cern.ch
Success: Your task has been delivered to the prod CRAB3 server.
Task name: 250409_143021:kphornsi_crab_20250409_163016
Project dir: /tmp/crabStatusTracking/crab_20250409_163016
Waiting for task to be processed
Checking task status
Task status: WAITING
Please wait...
Task status: WAITING
Please wait...
Task status: NEW
Please wait...
Task status: HOLDING
Please wait...
Task status: UPLOADED

Dry run
Getting input files into tmp dir /tmp/kphornsi/tmpedMjSG
Copying and preparing files for local execution in /tmp/crabStatusTracking/crab_20250409_163016/local
ERROR: KeyError: 'CRAB_AdditionalOutputFiles'
```

## Comment (aspiringmind-code, 2025-04-09T15:00:01Z)

@belforte preprod already runs the same version v3.250401-stable as canary and the error is due to inability to pickle 'htcondor2_impl._handle' object. [#9026](https://github.com/dmwm/CRABServer/pull/9026) didn't resolve the unpickling problem.
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

## Comment (belforte, 2025-04-10T07:25:41Z)

summary:
1. problem reported by user was due to using `crab-pre`
2. when using `crab-prod` there is still an error, which requires a new CRABClient https://github.com/dmwm/CRABClient/issues/5383
3. when ChildWorker is enabled in TW the problem with picking surfaces again #9040
