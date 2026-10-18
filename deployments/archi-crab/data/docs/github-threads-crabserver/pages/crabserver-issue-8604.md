# dmwm/CRABServer issue #8604: resubmiting with v2 bindings fails

State: closed
Opened: 2024-08-09T17:13:20Z
Closed: 2024-08-12T19:26:21Z
Labels: Type: Bug, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8604

## Opening post (belforte, 2024-08-09T17:13:20Z)

Initially discovered when resubmitting with V2 a task submitted with V1 bindings:

in https://cmsweb-test2.cern.ch/crabserver/ui/task/240809_150303%3Acmsbot_crab_scriptExe

```
2024-08-09 19:02:55,905:DEBUG:DagmanResubmitter:Resubmitting when JOBIDs were specified
2024-08-09 19:02:56,212:DEBUG:Handler:Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanResubmitter.py", line 103, in executeInternal
    schedd.edit(rootConst, adparam, ad.lookup(taskparam))
  File "/usr/local/lib/python3.8/site-packages/htcondor2/_schedd.py", line 215, in edit
    match_count = job_spec_hack(self._addr, job_spec,
  File "/usr/local/lib/python3.8/site-packages/htcondor2/_schedd.py", line 65, in job_spec_hack
    return f_constraint(addr, job_constraint, *args)
OSError: Unable to edit jobs matching constraint

```

But later found the same on a tast submitted with V2 bindings https://cmsweb-test2.cern.ch/crabserver/ui/task/240812_101636%3Abelforte_crab_20240812_121634
```
2024-08-12 13:58:16,451:DEBUG:DagmanResubmitter:Resubmitting when JOBIDs were specified
2024-08-12 13:58:16,472:DEBUG:Handler:Traceback (most recent call last):
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/DagmanResubmitter.py", line 103, in executeInternal
    schedd.edit(rootConst, adparam, ad.lookup(taskparam))
  File "/usr/local/lib/python3.8/site-packages/htcondor2/_schedd.py", line 215, in edit
    match_count = job_spec_hack(self._addr, job_spec,
  File "/usr/local/lib/python3.8/site-packages/htcondor2/_schedd.py", line 65, in job_spec_hack
    return f_constraint(addr, job_constraint, *args)
OSError: Unable to edit jobs matching constraint

```

## Comment (belforte, 2024-08-09T17:17:47Z)

relevant code appears perfectly "v2 compliant"
https://github.com/belforte/CRABServer/blob/9e531c1c61e9122a9a9ddcd69e48e5a120dca95b/src/python/TaskWorker/Actions/DagmanResubmitter.py#L95-L109
```python
        try:
                schedd.edit(rootConst, "HoldKillSig", 'SIGKILL')
                # Overwrite parameters in the os.environ[_CONDOR_JOB_AD] file. This will affect
                # all the jobs, not only the ones we want to resubmit. That's why the pre-job
                # is saving the values of the parameters for each job retry in text files (the
                # files are in the directory resubmit_info in the schedd).
                for adparam, taskparam in params.items():
                    if taskparam in ad:
                        schedd.edit(rootConst, adparam, ad.lookup(taskparam))
                    elif task['resubmit_' + taskparam] is not None:
                        schedd.edit(rootConst, adparam, str(task['resubmit_' + taskparam]))
                schedd.act(htcondor.JobAction.Hold, rootConst)
                schedd.edit(rootConst, "HoldKillSig", 'SIGUSR1')
                schedd.act(htcondor.JobAction.Release, rootConst)
            except Exception as hte:
```
but the fact that line 96 (edit of `HoldKillSig`) did not raise, suggest that some adparam has a non-v2 compiant format.

detailed debugging needed

## Comment (belforte, 2024-08-09T17:22:37Z)

I issued a new `crab resubmit` after switching TW to HTC bindings V1, and it worked

## Comment (belforte, 2024-08-12T13:30:06Z)

there is a problem with sending a list as value for `schedd.edit`.

This is a replica of what DagmanResubmitter does, in the python3 shell on vocms059

```text
Python 3.9.18 (main, Jul  3 2024, 00:00:00) 
[GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor
>>> import classad
>>> schedd=htcondor.Schedd()
>>> schedd.query("clusterid==9718033", ["CRAB_ResubmitList"])
[[ ServerTime = 1723467283; CRAB_ResubmitList = { "1","2","3" } ]]
>>> myAd = classad.ClassAd()
>>> myAd['myList']=["10","11","12"]
>>> expT=myAd.lookup('myList')
>>> expT
{ "10","11","12" }
>>> r=schedd.edit("clusterid==9718033", "CRAB_ResubmitList", expT)
>>> print(r)
edited 1 jobs
>>> schedd.query("clusterid==9718033", ["CRAB_ResubmitList"])
[[ ServerTime = 1723467447; CRAB_ResubmitList = { "10","11","12" } ]]
>>> 
```
All good.
Now try with V2
```text
>>> import htcondor2
>>> import classad2
>>> schedd2=htcondor2.Schedd()
>>> schedd2.query("clusterid==9718033", ["CRAB_ResubmitList"])
[[ ServerTime = 1723467596; CRAB_ResubmitList = { "10","11","12" } ]]
>>> myAd2=classad2.ClassAd()
>>> myAd2['myList']=["20","30","40"]
>>> expT2=myAd2.lookup('myList')
>>> expT2
{ "20","30","40" }
>>> schedd2.query("clusterid==9718033", ["CRAB_ResubmitList"])
[[ ServerTime = 1723467714; CRAB_ResubmitList = { "10","11","12" } ]]
>>> r=schedd.edit("clusterid==9718033", "CRAB_ResubmitList", expT2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/grid/crabtw/.local/lib/python3.9/site-packages/htcondor/_lock.py", line 70, in wrapper
    rv = func(*args, **kwargs)
TypeError: No registered converter was able to produce a C++ rvalue of type std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > from this Python object of type ExprTree
>>> r=schedd2.edit("clusterid==9718033", "CRAB_ResubmitList", expT2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/grid/crabtw/.local/lib/python3.9/site-packages/htcondor2/_schedd.py", line 215, in edit
    match_count = job_spec_hack(self._addr, job_spec,
  File "/home/grid/crabtw/.local/lib/python3.9/site-packages/htcondor2/_schedd.py", line 65, in job_spec_hack
    return f_constraint(addr, job_constraint, *args)
OSError: Unable to edit jobs matching constraint
>>> 
```

I have prepared a "reproducer" for Jamie
```text
[crabtw@vocms059 ~]$ condor_qedit -con 'clusterid==9718033' CRAB_ResubmitList "888"
Set attribute "CRAB_ResubmitList" for 1 matching jobs.
[crabtw@vocms059 ~]$ condor_q -con 'clusterid==9718033' -af CRAB_ResubmitList
888
[crabtw@vocms059 ~]$ python3 testEdit.py 
Condor version: $CondorVersion: 23.9.6 2024-08-08 BuildID: UW_Python_Wheel_Build $
Condor2 version: $CondorVersion: 23.9.6 2024-08-08 BuildID: UW_Python_Wheel_Build $
query job ad with V1
[[ ServerTime = 1723469322; CRAB_ResubmitList = 888 ]]
Now use V1 to set to 
   {
      "10",
      "11",
      "12"
   }
edited 1 jobs
query again:
[[ ServerTime = 1723469322; CRAB_ResubmitList = { "10","11","12" } ]]
query job ad with V2
[[ ServerTime = 1723469322; CRAB_ResubmitList = { "10","11","12" } ]]
Now use V2 to set to 
   {
      "20",
      "30",
      "40"
   }
Traceback (most recent call last):
  File "/home/grid/crabtw/testEdit.py", line 37, in <module>
    r = sched2.edit("clusterid==9718033", "CRAB_ResubmitList", expT2)
  File "/home/grid/crabtw/.local/lib/python3.9/site-packages/htcondor2/_schedd.py", line 215, in edit
    match_count = job_spec_hack(self._addr, job_spec,
  File "/home/grid/crabtw/.local/lib/python3.9/site-packages/htcondor2/_schedd.py", line 65, in job_spec_hack
    return f_constraint(addr, job_constraint, *args)
OSError: Unable to edit jobs matching constraint
[crabtw@vocms059 ~]$ 
```

with 
```text
[crabtw@vocms059 ~]$ cat testEdit.py 
#!/usr/bin/python3

import htcondor
import classad
import htcondor2
import classad2
print(f"Condor version: {htcondor.version()}")
print(f"Condor2 version: {htcondor2.version()}")

schedd = htcondor.Schedd()
sched2 = htcondor2.Schedd()

print("query job ad with V1")
info = schedd.query("clusterid==9718033", ["CRAB_ResubmitList"])
print(info)

# create a classAd exprTree with a new value
myAd = classad.ClassAd()
myAd['myList'] = ["10","11","12"]
expT = myAd.lookup('myList')
print(f"Now use V1 to set to {expT}")
r = schedd.edit("clusterid==9718033", "CRAB_ResubmitList", expT)
print(r)
info = schedd.query("clusterid==9718033", ["CRAB_ResubmitList"])
print("query again:")
print(info)

print("query job ad with V2")
info = sched2.query("clusterid==9718033", ["CRAB_ResubmitList"])
print(info)

# create a new (V2) ad with a new value
myAd2 = classad2.ClassAd()
myAd2['myList2'] = ["20", "30", "40"]
expT2 = myAd2.lookup('myList2')
print(f"Now use V2 to set to {expT2}")
r = sched2.edit("clusterid==9718033", "CRAB_ResubmitList", expT2)
print(r)
```

## Comment (Todd-L-Miller, 2024-08-12T15:54:55Z)

Try
```
r = sched2.edit("clusterid==9718033", "CRAB_ResubmitList", repr(expT2))
```
as a work-around.

## Comment (belforte, 2024-08-12T16:11:00Z)

it works ! Great. I can progress in testing :-)
indeed this works as well
```
sched2.edit("clusterid==9718033", "CRAB_ResubmitList", '{"888","999"}')
```
just that our current code uses the exprTree, and when I tried to construct the explicit list myself I could not find the correct quoting.

Thanks !!

## Comment (belforte, 2024-08-12T16:30:47Z)

I verified that it works on v1 as well. Can use same code.

## Comment (Todd-L-Miller, 2024-08-12T17:26:27Z)

Good.  I've pushed that fix into my "small fixes to the v2 bindings" branch, which I'll be sure to merge for 24.0.
