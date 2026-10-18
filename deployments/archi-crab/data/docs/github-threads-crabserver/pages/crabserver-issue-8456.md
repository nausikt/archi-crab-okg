# dmwm/CRABServer issue #8456: tasks with numCores>1 stays idle when using submit Object

State: closed
Opened: 2024-06-02T14:44:47Z
Closed: 2024-06-03T21:31:05Z
Labels: Type: Bug, Status: Done, Area: HTCondor, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8456

## Opening post (belforte, 2024-06-02T14:44:47Z)

with reference to #8336 

tasks submitted with e.g.
```
config.JobType.numCores = 8
```
stay idle in the scheduler universe and fail to bootstrap.

The problem is that using the old way, the `Requirements` for the dag_bootstrap job, i.e. the one submitted by the TW, is
```
Requirements = true || false && TARGET.OPSYS == "LINUX" && TARGET.ARCH == "X86_64" && TARGET.HasFileTransfer && TARGET.Disk >= RequestDisk && TARGET.Memory >= RequestMemory && TARGET.Cpus >= RequestCpus
```
note that TW only specifies the `true || false` and the rest is added automatically by  [HTCondor](https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit.html)
When the above expression is evaluated all the conditions added by HTC are ANDed with `false` to become irrelevant, and the result is simply `true`, which I guess explains this line which I always found very mysterious:
https://github.com/dmwm/CRABServer/blob/856d1efed8cba1f6c65d9b263ab8ffc20db9cd4d/src/python/TaskWorker/Actions/DagmanSubmitter.py#L482

When using a submit Object, instead of passing the classAds to `schedd.submit` (which is deprecated now), the final `Requirements` add is instead
```
Requirements = (true || false) && (TARGET.Arch == "X86_64") && (TARGET.OpSys == "LINUX") && (TARGET.Disk >= RequestDisk) && (TARGET.Memory >= RequestMemory) && (TARGET.Cpus >= RequestCpus)
```
this time HTCondor added parenthesis, which makes sense and is consistent with the [documentation](https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit.html)

But this time the requirements added by HTC "matter" and although I could not find what is the value for `TARGET.Cpus` (`condor_status -schedd -con 'machine=="vocms0122.cern.ch"' -l|grep -i cpu` returns nothing ), the last member is clearly what prevents the match, since other tasks have the same expression simply w/o the final` && (TARGET.Cpus >= RequestCpus)` and work finely.

Simply removing this line solves the problem
https://github.com/dmwm/CRABServer/blob/856d1efed8cba1f6c65d9b263ab8ffc20db9cd4d/src/python/TaskWorker/Actions/DagmanSubmitter.py#L73

In a way, it is not good to use those classAd to pass requirements for the grid jobs, the correct requirements are already in the `Jobs.submit` file prepared by DagmanCreator.

I presume that one reason to do in this way could have been to make it easier to change those requirements during `crab resubmit` by only sending new ads, w/o  touching the `Job.submit`.

I have not tested if after this change is is stll possible to change numCores in the resubmit, but it is a very bad idea IMHO, we should rather forbid it.

I can't remove other requirements passed as ads here like `RequestMemory` because they are used in PreJob, possibly to make it work with same code for submissions and resubmissions.

In the medium term, we need to rewrite the resubmission anyhow, and will avoid using dagman-job's classAd for this.

## Comment (belforte, 2024-06-03T13:58:57Z)

with the fix in https://github.com/belforte/CRABServer/commit/c73d3fdb90d75503822b67a6acadf1329f7301a4 tasks get submitted, but the gridjobs have `RequestCpus = 1`
A change in PreJob is needed.
Or a way for scheduler to start those in scheduler universe.
I will do some local tests and write to HTCondor, it may be the least effort path to a short term solution.

## Comment (belforte, 2024-06-03T16:30:18Z)

I wrote this to condor support
```

Dear experts,
can you explain why a JDL [1] with three lines in it stays idle forever ?
Universe   = scheduler
requirements = true
RequestCpus = 2

inspecting the job requirements with condor_q -l, I find
Requirements = (true) && (TARGET.Arch == "X86_64") && (TARGET.OpSys == "LINUX") && (TARGET.Disk >= RequestDisk) && (TARGET.Memory >= RequestMemory) && (TARGET.Cpus >= RequestCpus)

The same submission runs withing a few minutes if I put
RequestCpus = 2
and in that case the Requirements expression does not have the final
term  && (TARGET.Cpus >= RequestCpus)

My scheduler is 16-cpu machine, so regardless of whether the
requirement makes sense or not, I'd expect the job to run, no ?

Documentation in https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit.html says
<quote>
For scheduler and local universe jobs, the requirements expression is evaluated against the Scheduler ClassAd which represents the the condor_schedd daemon running on the access point, rather than a remote machine.
</quote>

But I did find a way to inspect those TARGET.* ads.
condor_status -sched -con 'machine=="vocms059.cern.ch"' -af Cpus Memory ...
simply returns "undefined". Same if I add TARGET.
Just lile "condor_q -af requirements" returns undefined


This is currently breaking CMS CRAB submission when moving to current
schedd.submit(submitObject,...) binding (we can go into details of how
it was working "before" if you care, but it is not relevant, IMHO).
I believe I can find a workaround by changing code in various places,
but if the above could be made to work, it would be the easiest.

Thanks
Stefano


[1] full JDL

Universe   = scheduler
Executable = sleep.sh
Arguments  = 1
Log        = sleep.PC.log
Output     = sleep.out.$(Cluster).$(Process)
Error      = sleep.err.$(Cluster).$(Process)
requirements = true
should_transfer_files = YES
RequestMemory = 2000
RequestCpus = 2
when_to_transfer_output = ON_EXIT
Queue 1

```

## Comment (belforte, 2024-06-03T18:43:39Z)

Reply from ToddM is here
https://www-auth.cs.wisc.edu/lists/htcondor-users/2024-June/msg00008.shtml

and "solution" is here
https://www-auth.cs.wisc.edu/lists/htcondor-users/2024-June/msg00011.shtml

I will test replacing
https://github.com/dmwm/CRABServer/blob/7ac2b90193632df3757bcf3bf7750ff27bf736a3/src/python/TaskWorker/Actions/DagmanSubmitter.py#L481
with
```python
    jobJDL["Requirements"] = "TARGET.Cpus==1"
```

## Comment (belforte, 2024-06-03T19:15:45Z)

testing latest fix in
 - [x] https://github.com/dmwm/CRABServer/issues/8465

## Comment (belforte, 2024-06-03T21:26:39Z)

fix validated.

## Comment (belforte, 2024-06-03T21:31:05Z)

fixed via #8466
