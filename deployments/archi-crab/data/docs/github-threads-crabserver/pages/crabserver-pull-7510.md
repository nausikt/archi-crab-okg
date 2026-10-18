# dmwm/CRABServer pull request #7510: Use python3 for every command inside the jobwrapper

State: closed
Opened: 2023-01-27T13:44:02Z
Closed: 2023-02-20T14:41:12Z
Merged: 2023-02-20T14:41:12Z
URL: https://github.com/dmwm/CRABServer/pull/7510

## Opening post (mapellidario, 2023-01-27T13:44:02Z)

Fixes #7509

### status

condor_chirp is broken when running slc6 jobs: still work in progress

### description

I noticed a problem with the python used to retrieve the exit code in #7509 . It's caused by the new jobwrapper, since it does not load into the path any executable called "python", but only `python3`. 

I also looked around and fixed all the instances that I could find of ambiguous `python` instead of `python3`.

### future work

We still have many `#!/usr/bin/python` and `#!/usr/bin/env python` that should become `#!/usr/bin/env python3`. I will do it at a later time. They are likely not causing any problem because we are not calling directly the `.py` files, but always using `python3 <myfile>.py`. Still, it's better to be consistent.

## Comment (belforte, 2023-01-27T13:47:40Z)

are we sure that python3 is always availble to the wrapper ? even when using CMSSW_6 ?

## Comment (cmsdmwmbot, 2023-01-27T13:48:02Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1406/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-01-27T13:58:04Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1407/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-01-27T14:39:18Z)

> are we sure that python3 is always availble to the wrapper ? even when using CMSSW_6 ?

Mh, I will make some more tests. However, I thought that we were aiming for:

- the container on the woker node starts with whatever env it wants
- we source comp environment, in py3, and we run jobwrapper scripts inside it
- we source cmssw python (this can be py2)

I sort of assumed that we were able to fix py3 for the jobwrapper environment. But you are right, i need to explicitely test it with some older cmssw version, like cmssw_7 (i am not wure whether we need to support cmssw_6)

## Comment (belforte, 2023-01-27T14:49:59Z)

my fear is that for older CMSSW glidein may start an SL6 pilot w/o python3.
You are right, we support down to CMSSW_7. But no 6. pfff... will CMSSW_7 ever go away ?

## Comment (mapellidario, 2023-02-09T18:30:30Z)

I still have problems with `condor_chirp` when running tasks with scram_arch slc6:

```plaintext
======== Figuring out long exit code of the job for condor_chirp ========
==== Long exit code of the job is 0 ====
/usr/bin/python: htchirp is a package and cannot be directly executed
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 1 ========
```

from: https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230209_155558:dmapelli_crab_20230209_165552/job_out.3.0.txt

I will have a look tomorrow. It is possible I am "leaking" a python2 PATH from the cmsRun env back to the jobwrapper.

## Comment (belforte, 2023-02-09T23:09:31Z)

or maybe a conflict between 
== ENV: GWMS_SINGULARITY_IMAGE_HUMAN=/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel6
and the way the pilot makes condor_chirp available
we call condor_chirp from the outermost shell, which is a bash script
https://github.com/dmwm/CRABServer/blob/c484c2377476c3eeca32207fc4d2117bfdf714e2/scripts/gWMS-CMSRunAnalysis.sh#L48

## Comment (cmsdmwmbot, 2023-02-15T15:17:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1422/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-15T19:17:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1425/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-02-16T10:01:51Z)

Eventually, I needed to have a more in-depth look at how environments
change inside the JobWrapper and I have not answered all the questions I have yet.
I will post this comment anyways not to keep the rest of the team in the dark.

Jobs that require cc7 or el8 work just fine. I may need to give them another look in the next few days, but I do not recall I found anything wrong. Some problems emerge with the new jobwrapper when we run slc6 jobs.

In the next sections, I will compare the two following tasks

- `task1` https://cmsweb-test11.cern.ch/crabserver/ui/task/230216_093031%3Admapelli_crab_20230216_103029 . Task requiring slc6, TW that we have in production now with the following debug changes https://github.com/dmwm/CRABServer/compare/v3.221124...mapellidario:20230215_jobwr_dbg_1
- `task2` https://cmsweb-test11.cern.ch/crabserver/ui/task/230216_093555%3Admapelli_crab_20230216_103554 . Task requiring slc6, TW from https://github.com/dmwm/CRABServer/pull/7510 with the same debug changes as above (https://github.com/mapellidario/CRABServer/compare/20230127_jobwr_2...mapellidario:CRABServer:20230215_jobwr_dbg_2)

####  `condor_chirp`. still open question

The condor_chirp command is a bash script [1] that uses a python version found by the gWMS script `gwms-python` [2].

This scripts are shipped to the container by glidein [3]. Nikos showed me an xml config where based 
on the singularity container version (let's say rhel6), they decide which version of condor 
(9.11 if i remember correctly) to use and which tarball to ship to the container (a condor 8 if I 
remember correctly. yes, i know, they dont match, doesnt matter too much apparently).

Currently in production, when we run an slc6 job, `/srv/.gwms.d/bin/gwms-python` 
selects python 2.7.13 and everything looks good. [4]

However, when we run an slc6 job with the new jobwrapper, `/srv/.gwms.d/bin/gwms-python` 
selects python 2.6.6 and it breaks [5]

I need some more time to understand how `gwms-python` works and make sure that we provide a proper environment when it runs. Maybe I can just throw everything away and let it use the startup environment.

If I understand correctly, we may need to fix the environment for condor_chirp only when we need to use it to compute the exit code [6].

#### task_proc_wrapper. ok

we need to select which python version we should use for populating the `DEST_LFN` variable. The python that we use here is the default schedd one if I understand correctly, so using both py2 and py3 gives the proper result in both [7] 

When we use py3 we have the usual TokenManager complaining that it can not find `import jwt`, but it does not seem to affect the outcome. 

I would chose to use python3, as we do in this PR.

#### CMSRunAnalysis.sh, "import CMSRunAnalysis; CMSRunAnalysis.logCMSSW()". ok

The python that we use here depends on the COMP environment, so we need to switch to python3, which is what we do in this PR. [8] 

---

Addendum, for future me who will wonder how i debugged things:

When we submit an job with a scram arch that requires slc6, 
SI spins up an slc6 container where we run all our scripts into. 
As stefano mentioned, the container that we run in is 
`GWMS_SINGULARITY_IMAGE_HUMAN=/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel6`

and can be explored on lxplus with

```
/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel6/singularity -- bash
```

I still dont know how to replicate in lxplus what gwms does in the worken nodes, maybe we can just run https://github.com/glideinWMS/glideinwms/blob/master/creation/web_base/glidein_startup.sh, but i am ready to bet that a single script is not enough and that we need to access some tarballs that are on the frontend machine only.

---

[1] path inside the worker node container: `/srv/.gwms.d/bin/condor_chirp`, https://github.com/glideinWMS/glideinwms/blob/master/creation/web_base/condor_chirp

[2] path: `/srv/.gwms.d/bin/gwms-python`, https://github.com/glideinWMS/glideinwms/blob/master/creation/web_base/gwms-python 

[3] https://github.com/glideinWMS/glideinwms/blob/8cedeaff71e692d53c6a27e8c63dfc334432371b/creation/web_base/glidein_startup.sh#L2023 somewhere around here

[4]

a job from `task1`, for example: https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230216_093031:dmapelli_crab_20230216_103029/job_out.1.0.txt

```planitext
+ /srv/.gwms.d/bin/gwms-python --version
Python 2.7.13+
+ file /srv/.gwms.d/bin/gwms-python
/srv/.gwms.d/bin/gwms-python: POSIX shell script text executable
+ command -v condor_chirp
/srv/.gwms.d/bin/condor_chirp
+ /srv/.gwms.d/bin/gwms-python -c 'import htchirp; print(htchirp.__file__)'
/srv/.gwms.d/lib/python/htchirp/__init__.py
+ set +x
======== Figuring out long exit code of the job for condor_chirp ========
==== Long exit code of the job is 0 ====
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
```

[5] 
a job from `task2`, for example https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230216_093555:dmapelli_crab_20230216_103554/job_out.1.0.txt

```plaintext
+ /srv/.gwms.d/bin/gwms-python --version
Python 2.6.6
+ file /srv/.gwms.d/bin/gwms-python
/srv/.gwms.d/bin/gwms-python: POSIX shell script text executable
+ command -v condor_chirp
/srv/.gwms.d/bin/condor_chirp
+ /srv/.gwms.d/bin/gwms-python -c 'import htchirp; print(htchirp.__file__)'
/srv/.gwms.d/lib/python/htchirp/__init__.py
+ set +x
======== Figuring out long exit code of the job for condor_chirp ========
==== Long exit code of the job is 0 ====
/usr/bin/python: htchirp is a package and cannot be directly executed
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 1 ========
```

[6] https://github.com/dmwm/CRABServer/blob/master/scripts/gWMS-CMSRunAnalysis.sh#L66

[7] 

- `task1`: https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230216_093031:dmapelli_crab_20230216_103029/SPOOL_DIR/task_process/daemon.out.9247650.0
- `task2`: https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230216_093555:dmapelli_crab_20230216_103554/SPOOL_DIR/task_process/daemon.out.9247657.0

[8]

`task1`: 

<details>
```plaintext
======== CMSRunAnalysis.py FINISHING at Thu Feb 16 09:32:38 GMT 2023 ========
+ echo dariodebug
dariodebug
+ echo python3
python3
+ python3 -c 'import CMSRunAnalysis; print("dariodebug", CMSRunAnalysis.EC_MissingArg)'
Failed to import the site module
Traceback (most recent call last):
  File "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.4/3.4.57/el6-x86_64/usr/lib/python2.6/site-packages/site.py", line 73, in <module>
    __boot()
  File "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.4/3.4.57/el6-x86_64/usr/lib/python2.6/site-packages/site.py", line 2, in __boot
    import sys, imp, os, os.path   
  File "/usr/lib64/python3.4/imp.py", line 22, in <module>
    from importlib import util
  File "/usr/lib64/python3.4/importlib/util.py", line 12, in <module>
    from contextlib import contextmanager
  File "/usr/lib64/python3.4/contextlib.py", line 4, in <module>
    from collections import deque
  File "/usr/lib64/python3.4/collections/__init__.py", line 17, in <module>
    from reprlib import recursive_repr as _recursive_repr
  File "/cvmfs/cms.cern.ch/COMP/slc6_amd64_gcc493/external/py2-future/0.18.2/lib/python2.7/site-packages/reprlib/__init__.py", line 7, in <module>
    raise ImportError('This package should not be accessible on Python 3. '
ImportError: This package should not be accessible on Python 3. Either you are trying to run from the python-future src folder or your installation of python-future is corrupted.
+ echo python
python
+ python -c 'import CMSRunAnalysis; print("dariodebug", CMSRunAnalysis.EC_MissingArg)'
('dariodebug', 50113)
+ set +x
```
</details>

`task2`

<details>
```plaintext
======== CMSRunAnalysis.py FINISHING at Thu Feb 16 09:37:46 GMT 2023 ========
+ echo dariodebug
dariodebug
+ echo python3
python3
+ python3 -c 'import CMSRunAnalysis; print("dariodebug", CMSRunAnalysis.EC_MissingArg)'
dariodebug 50113
+ echo python
python
+ python -c 'import CMSRunAnalysis; print("dariodebug", CMSRunAnalysis.EC_MissingArg)'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "CMSRunAnalysis.py", line 23, in <module>
    import WMCore.Storage.SiteLocalConfig as SiteLocalConfig
  File "/srv/WMCore.zip/WMCore/Storage/SiteLocalConfig.py", line 11, in <module>
ImportError: No module named builtins
+ set +x
```
</details>

## Comment (cmsdmwmbot, 2023-02-16T17:59:53Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1426/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-02-17T13:19:48Z)

As Stefano mentioned in https://github.com/dmwm/CRABServer/issues/7536#issuecomment-1434435897

> ... we should not call python in there but only execute condor_chirp and let gWMS wrapper do the work ...

Since we do not have `jq`, unless someone has a nice idea on how to parse a json file inside the worker node, we need to use some python for https://github.com/dmwm/CRABServer/blob/ba11632d45e42512addcfaac681c1adbc1a5b870/scripts/gWMS-CMSRunAnalysis.sh#L56

The point is: which python? 

- I thought we always had COMP `python3` , but that can cause weird errors when a job fails likely due to python version mismatch [1]
- Yesterday I experimented with `gwms-python` in this commit https://github.com/dmwm/CRABServer/pull/7510/commits/1a4d80d610b6f9cab65580946e3bf0cb5fa07920 , which makes condor_chirp work as intended :) [2]

---

[1] this [job](https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230216_155957:dmapelli_crab_20230216_165956/job_out.1.0.txt) from https://cmsweb-test11.cern.ch/crabserver/ui/task/230216_155957:dmapelli_crab_20230216_165956

<details>

```plaintext
======== Figuring out long exit code of the job for condor_chirp ========
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.5/3.5.63-1/el7-x86_64/usr/lib64/python3.6/json/__init__.py", line 299, in load
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.5/3.5.63-1/el7-x86_64/usr/lib64/python3.6/json/__init__.py", line 354, in loads
    return _default_decoder.decode(s)
  File "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.5/3.5.63-1/el7-x86_64/usr/lib64/python3.6/json/decoder.py", line 339, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.5/3.5.63-1/el7-x86_64/usr/lib64/python3.6/json/decoder.py", line 357, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
==== Failed to load the long exit code from jobReport.json.1. Falling back to short exit code ====
======== Short exit code also missing. Settint exit code to 80001 ========
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "CMSRunAnalysis.py", line 23, in <module>
    import WMCore.Storage.SiteLocalConfig as SiteLocalConfig
  File "/srv/WMCore.zip/WMCore/Storage/SiteLocalConfig.py", line 11, in <module>
ImportError: No module named builtins
+ set +x
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
```
</details>

[2] this [job](https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230216_180013:dmapelli_crab_20230216_190012/job_out.1.0.txt) from https://cmsweb-test11.cern.ch/crabserver/ui/task/230216_180013:dmapelli_crab_20230216_190012

<details>

```plaintext
======== Figuring out long exit code of the job for condor_chirp ========
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "/usr/lib64/python2.7/json/__init__.py", line 290, in load
    **kw)
  File "/usr/lib64/python2.7/json/__init__.py", line 338, in loads
    return _default_decoder.decode(s)
  File "/usr/lib64/python2.7/json/decoder.py", line 366, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib64/python2.7/json/decoder.py", line 384, in raw_decode
    raise ValueError("No JSON object could be decoded")
ValueError: No JSON object could be decoded
==== Failed to load the long exit code from jobReport.json.1. Falling back to short exit code ====
======== Short exit code also missing. Settint exit code to 80001 ========
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
```

</details>

## Comment (belforte, 2023-02-17T13:30:20Z)

@mapellidario wow. very thorough investigation and surely I can't follow all details, but am puzzled that you worry about the env. I would think that the `finish` in gWMS-CMSRunAnalysis.sh is executed in the startup environment (plus a few exports). Since this line
https://github.com/dmwm/CRABServer/blob/ba11632d45e42512addcfaac681c1adbc1a5b870/scripts/gWMS-CMSRunAnalysis.sh#L138
forks another process where all env. setup is done. Is that process is terminated by condor (too much time e.g.) the env. for the `finish` is correct. Am I simply confused ?

Unless the problem is that jobs get killed by condor when doing stageout, so that we have gone through
https://github.com/dmwm/CRABServer/blob/ba11632d45e42512addcfaac681c1adbc1a5b870/scripts/gWMS-CMSRunAnalysis.sh#L166-L172
which may indeed leave us in a bad status.
Shall we wrap statageout in its own `bash` subprocess like done for the main application ?

## Comment (belforte, 2023-02-17T13:49:51Z)

sorry Dario, I only read now the comment which you posted before mine.
My immediate reaction is "why do we do that stuff inside chirp_exit_code" ?
Let's move the python to where we have python and keep that function as something which can be run when things failed badly and control is bumped back to the top wrapper.

## Comment (belforte, 2023-02-17T13:53:40Z)

it is also possible that long exit code can be `grep`ped from the fjr json file. Ugly, but... all in all that's a parser too

## Comment (mapellidario, 2023-02-20T12:32:53Z)

After spending a couple of more days on the `condor_chirp` problem and having opened and ad hoc issue https://github.com/dmwm/CRABServer/issues/7542 , I think this PR can be merged.

Long story short:

- `condor_chirp` is a wrapper around `gwms-python`, so it makes sense to use `gwms-python` inside it
- `condor_chirp` gives problems with slc6. However, the solution has a scope way broader than this PR. I would postpone it

So: I would merge this PR as is and move all the rest to a later stage :)

## Comment (belforte, 2023-02-20T13:43:10Z)

we should not call `gwms-python`. Please change to `python` and let's worry later about fixing for the edge cases.

## Comment (cmsdmwmbot, 2023-02-20T14:09:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1433/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-20T14:14:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1434/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-02-20T14:16:36Z)

> we should not call gwms-python. Please change to python and let's worry later about fixing for the edge cases.

I disagree.

- using `python` there breaks chirp for every job running in el8, [here](https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230127_122119:dmapelli_crab_20230127_132116/job_out.1.0.txt)
- using `python3` there breaks chirp for every job running in slc7, [here](https://cmsweb-test11.cern.ch/crabserver/ui/task/230216_155957:dmapelli_crab_20230216_165956)

since that script is executed by `condor_chirp`, which is a wrapper of `gwms-python -m htchirp`, i think that sticking to `gwms-python` is the cleanest option

## Comment (mapellidario, 2023-02-20T14:40:25Z)

After private discussion, we are sticking to `python`, we will think about condor_chirp at a later stage

## Comment (mapellidario, 2023-02-20T14:41:01Z)

Since we agreed on the details of this PR, I will merge it
