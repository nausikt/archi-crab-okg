# dmwm/CRABClient pull request #5350: Python3.12 support: Use importlib instead of deprecated imp module

State: closed
Opened: 2024-11-21T10:40:26Z
Closed: 2024-11-21T11:17:16Z
Merged: 2024-11-21T11:17:16Z
URL: https://github.com/dmwm/CRABClient/pull/5350

## Opening post (smuzaffar, 2024-11-21T10:40:26Z)

`imp` module has been deprecated and removed in `python 3.12`. This PR proposes to uses `importlib` for `python 3.12` e.g in `CMSSW_14_2_PY3_12_X` IBs. It should not break crab client for CMSSW release with `python version < 3.12`.

This requires newer WMCore specially change in [WMCore/Configuration.py](https://github.com/dmwm/WMCore/pull/11530/files#diff-ae418221154baa0ba96bdcf0566fde2fccf43a95d289f435f28c45e2a0552f1b) . 

Note that using this I was able to submit crab job for CMSSW_14_2_PY312_X but they [fail on crab server side](https://cmsweb.cern.ch:8443/scheddmon/0195/cmsbot/241121_102531:cmsbot_crab_Jenkins_CMSSW_14_2_PY312_X_2024-11-20-2300_el8_amd64_gcc12_123400/job_out.1.0.txt) as due to usage of `imp` in crab server code. So in order to fully support python 3.12 crab jobs, one needs to update crab server code too

## Comment (cmsdmwmbot, 2024-11-21T10:42:01Z)

Can one of the admins verify this patch?

## Comment (belforte, 2024-11-21T11:05:12Z)

:bow: 
great work @smuzaffar . As always.
I did not know that we are moving toward python 3.12.  And will be very happy to future-proof server code as well, even if currently we run it in a python3.8 debian container.

But am very puzzled by the run-time error in y [fail on crab server side](https://cmsweb.cern.ch:8443/scheddmon/0195/cmsbot/241121_102531:cmsbot_crab_Jenkins_CMSSW_14_2_PY312_X_2024-11-20-2300_el8_amd64_gcc12_123400/job_out.1.0.txt) since at first sight the traceback indicates presence of WMCore's /cvmfs/cms.cern.ch/cc8_amd64_gcc9 environment inside cmsRun execution, which both WMCore and CRAB worked hard to separate.

That still needs to be understood.
Hopefully this is not super-urgent and I can look at it after I am done with current work ?
We can surely get this change into the client in the meanwhile and check other commands.

I will open issues in CRABServer repo for the work on that side.

## Comment (belforte, 2024-11-21T11:17:11Z)

LGTM

## Comment (smuzaffar, 2024-11-21T14:56:33Z)

thanks @belforte.
The failure [a] is due to the usage of `past.builtins` in [FWCore/ParameterSet/python/Types.py](https://github.com/cms-sw/cmssw/blob/master/FWCore/ParameterSet/python/Types.py#L6). `past.builtins` is provided via `future` package which is loaded from `/cvmfs/cms.cern.ch/cc8_amd64_gcc9/external/py3-future/0.18.2/lib/python3.8/site-packages` as something (crab or wmcore) sets `PYTHONPATH` to `/srv/WMCore.zip:/cvmfs/cms.cern.ch/cc8_amd64_gcc9/external/py3-future/0.18.2/lib/python3.8/site-packages`.

I will fix cmssw FW code to not use  `past.builtins`  which will allow us to run crab tests. I proper fix/workaround  might be to not source `py3-future` for python 3.12 and above

[a]
```
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
```

## Comment (belforte, 2024-11-21T15:26:06Z)

thanks @smuzaffar . But I still do not like that $PYTHONPATH has WMCore's py3.8 added in when it runs the user application. It should be "CMSSW in a pristine environment".  There's something which I do not understand there which may possibly cause other problems. Let's follow up on that in https://github.com/dmwm/CRABServer/issues/8805
There is of course no reason for WMCore to still use `future` and `past` since they run in python3 now. But changing all places where those have been put in for the transition is something they did not get to yet. We surely want WMCore and CMSSW to be able to use different python versions.

## Comment (belforte, 2024-11-26T22:29:18Z)

@smuzaffar I just deployed a new CRAB TaskWorker which fixes the PYTHONPATH conflict (cleanup PYTHONPATH before running the application e.g. cmsRun)
Now job submitted with  CMSSW_14_2_PY3_12_X (of course using crab client from IB which has your patch) run happily.
I tested on same release as in your report `CMSSW_14_2_PY312_X_2024-11-20-2300`

## Comment (smuzaffar, 2024-11-26T23:03:19Z)

thanks @belforte ,  this is really good.
