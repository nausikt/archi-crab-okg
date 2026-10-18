# dmwm/CRABServer issue #8805: Avoid mixing PYTHONPATH from WMCore and CMSSW 

State: closed
Opened: 2024-11-21T11:41:45Z
Closed: 2024-11-27T20:13:44Z
Labels: Type: Bug, Status: In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8805

## Opening post (belforte, 2024-11-21T11:41:45Z)

see https://github.com/dmwm/CRABClient/pull/5350


the job stdout for a job submitted with CMSSW_14_2_PY312_X_2024-11-20-2300 has the following. Is WMCore python env. leaking  into CMSSW ?

```text

==== CMSSW JOB Execution started at Thu Nov 21 10:30:36 2024 UTC ====
==== Will execute stdbuf -oL -eL cmsRun -j FrameworkJobReport.xml PSet.py > cmsRun-stdout.log.tmp 2>&1
Error executing application in CMSSW environment.
	See stdout log
==== Execution FAILED at Thu Nov 21 10:30:38 2024 UTC ====
==== CMSSW JOB Execution completed at Thu Nov 21 10:30:38 2024 UTC ====
Application exit code: 5
==== Execution FINISHED at Thu Nov 21 10:30:38 2024 UTC ====
======== CMSSW OUTPUT STARTING ========
NOTICE: lines longer than 3000 characters will be truncated
== CMSSW: /cvmfs/cms.cern.ch/cc8_amd64_gcc9/external/py3-future/0.18.2/lib/python3.8/site-packages/past/types/oldstr.py:23: SyntaxWarning: invalid escape sequence '\d'
== CMSSW:   """
== CMSSW: ----- Begin Fatal Exception 21-Nov-2024 05:30:38 EST-----------------------
== CMSSW: An exception of category 'ConfigFileReadError' occurred while
== CMSSW:    [0] Processing the python configuration file named PSet.py
== CMSSW: Exception Message:
== CMSSW:  unknown python problem occurred.
== CMSSW: ModuleNotFoundError: No module named 'imp'
== CMSSW:
== CMSSW: At:
== CMSSW:   /cvmfs/cms.cern.ch/cc8_amd64_gcc9/external/py3-future/0.18.2/lib/python3.8/site-packages/past/builtins/misc.py(45): <module>
== CMSSW:   <frozen importlib._bootstrap>(488): _call_with_frames_removed
== CMSSW:   <frozen importlib._bootstrap_external>(995): exec_module
== CMSSW:   <frozen importlib._bootstrap>(950): _load_unlocked
== CMSSW:   <frozen importlib._bootstrap>(1334): _find_and_load_unlocked
== CMSSW:   <frozen importlib._bootstrap>(1360): _find_and_load
== CMSSW:   /cvmfs/cms.cern.ch/cc8_amd64_gcc9/external/py3-future/0.18.2/lib/python3.8/site-packages/past/builtins/__init__.py(54): <module>
== CMSSW:   <frozen importlib._bootstrap>(488): _call_with_frames_removed
== CMSSW:   <frozen importlib._bootstrap_external>(995): exec_module
== CMSSW:   <frozen importlib._bootstrap>(950): _load_unlocked
== CMSSW:   <frozen importlib._bootstrap>(1334): _find_and_load_unlocked
== CMSSW:   <frozen importlib._bootstrap>(1360): _find_and_load
== CMSSW:   /cvmfs/cms-ib.cern.ch/sw/x86_64/week0/el8_amd64_gcc12/cms/cmssw/CMSSW_14_2_PY312_X_2024-11-20-2300/src/FWCore/ParameterSet/python/Types.py(6): <module>
== CMSSW:   <frozen importlib._bootstrap>(488): _call_with_frames_removed
== CMSSW:   <frozen importlib._bootstrap_external>(995): exec_module
== CMSSW:   <frozen importlib._bootstrap>(950): _load_unlocked
== CMSSW:   <frozen importlib._bootstrap>(1334): _find_and_load_unlocked
== CMSSW:   <frozen importlib._bootstrap>(1360): _find_and_load
== CMSSW:   /cvmfs/cms-ib.cern.ch/sw/x86_64/week0/el8_amd64_gcc12/cms/cmssw/CMSSW_14_2_PY312_X_2024-11-20-2300/src/FWCore/ParameterSet/python/Config.py(16): <module>
== CMSSW:   <frozen importlib._bootstrap>(488): _call_with_frames_removed
== CMSSW:   <frozen importlib._bootstrap_external>(995): exec_module
== CMSSW:   <frozen importlib._bootstrap>(950): _load_unlocked
== CMSSW:   <frozen importlib._bootstrap>(1334): _find_and_load_unlocked
== CMSSW:   <frozen importlib._bootstrap>(1360): _find_and_load
== CMSSW:   PSet.py(1): <module>
== CMSSW:
== CMSSW: ----- End Fatal Exception -------------------------------------------------
== CMSSW:
```

## Comment (belforte, 2024-11-21T16:55:20Z)

I do not like lack of environment control. Moving to top of list

## Comment (belforte, 2024-11-22T10:07:10Z)

So the problem is that we do no clean the environment  before executing e.g. cmsRun
https://github.com/dmwm/CRABServer/blob/99fe41a9b5a2ef0222827c32bff41ec45084a4f7/scripts/CMSRunAnalysis.py#L702

The `False` in there was introduced in https://github.com/dmwm/CRABServer/commit/a43a10d461cee1bd58ee36ebadb43b5a7909c5df
which indeed had this in the commets:
```
When we launch cmsRun, we should imitate what WMCore is
doing: do not clean the env, to preserve all the env
variables set for us by the workern node / pilot
and by cmsset_default.sh

Just a (small ?) difference with respect to WMCore:
we do not remove the COMP's python from the pythonpath.
This can be dangerous and should be thoroughly tested.
```

I am trying to remember why we decided not to cleanup PYTHONPATH :-(

## Comment (belforte, 2024-11-25T10:32:01Z)

After chat with @mapellidario 
* we can not use `cleanEnv=False` because it cleans too much. We need to preserve what site adds via `cmssetup_local.sh` or the pilot does
* we simply need the equivalent of `scram unsetenv` for the COMP python which we setup to run the wrapper
* Since such script does not exits, we will go for the small hack already used in WMCore https://github.com/dmwm/WMCore/blob/d3852da7cedd8be489c4d1b980beca7310ce149c/src/python/WMCore/WMSpec/Steps/Executors/CMSSW.py#L267
```python

        envOverride = {}
        # Do not pass WM PYTHONPATH to CMSSW environment
        pythonPath = os.environ.get('PYTHONPATH', '')
        envOverride['PYTHONPATH'] = ""
        # some libraries linked with CMSSW need HOME in the environment
        if 'HOME' not in os.environ:
            envOverride['HOME'] = os.environ.get('PWD', "/")

        os.environ.update(envOverride)
 ```

## Comment (belforte, 2024-11-27T16:10:25Z)

fix in https://github.com/belforte/CRABServer/commit/20b4abef5c8277931418096702bb12f3a4fd75d5 does not work on CMSSW_9 (and any other oldish CMSSW which relies on its $PYTHONPATH)

## Comment (belforte, 2024-11-27T16:40:33Z)

the problem is that CMSSW_9 needs its own PYTHONPATH which is setup e.g. by `cmsenv`.
But the way `scramTool`, i.e. [Scram()](https://github.com/dmwm/WMCore/blob/d3852da7cedd8be489c4d1b980beca7310ce149c/src/python/WMCore/WMRuntime/Tools/Scram.py#L368-L432) works in https://github.com/dmwm/CRABServer/blob/8d59c1bd133a504169ddf8614909de8059e144fe/scripts/CMSRunAnalysis.py#L411
is by forking a process and passing to its `stdin` via [procWriter](https://github.com/dmwm/WMCore/blob/d3852da7cedd8be489c4d1b980beca7310ce149c/src/python/WMCore/WMRuntime/Tools/Scram.py#L379-L384) all env. vars. which make up the CMSSW env before communicating the actual `unset PYTHONPATH; cmsRun` command which `CMSRunAnalysis.py` prepares.

And now I understand why in WMCore they used the apparently convoluted strategy to remove PYTHONPATH from the running process env before calling `scramTool` and add it back afterwards, as indicated above.
