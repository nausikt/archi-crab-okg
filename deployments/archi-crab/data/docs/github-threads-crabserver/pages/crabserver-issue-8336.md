# dmwm/CRABServer issue #8336: use a Submit object, not a classAd (dagAd) as argument to schedd.submit

State: closed
Opened: 2024-04-15T21:26:55Z
Closed: 2024-05-31T14:36:54Z
Labels: Status: Done, Priority: High, Area: Code Cleanup, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8336

## Opening post (belforte, 2024-04-15T21:26:55Z)

an [htcondor.Submit](https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/htcondor.html#submitting-jobs) object should be used as first argument to `schedd.submit` in
https://github.com/dmwm/CRABServer/blob/6f65ad6a5dd413d6f4aa078aae86dd5ceb63edf5/src/python/TaskWorker/Actions/DagmanSubmitter.py#L543
as documented in the `submit` paragraph of [interacting with schedulers](https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/htcondor.html#interacting-with-schedulers)
see also https://github.com/dmwm/CRABServer/issues/8333#issue-2239797786

Use the [syntax  of submission file](https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit.html#submit-description-file-commands) so that description is simpler and more clear and conversion to classAd is [done](https://htcondor.readthedocs.io/en/latest/users-manual/submitting-a-job.html#submitting-a-job) by HTCondor

This is a bit non trivial since we need to make sure that all submission ads are properly handled, submitting a few test tasks is not enough to validate.

Hopefully DagmanSubmitter will be easier to read after this.

## Comment (belforte, 2024-05-29T17:11:45Z)

harder than I thought :-(

After some struggle I got to the point of submitting a dagman to the scheduler which as by design is in HOLD waiting for spool() command as in the current code
https://github.com/dmwm/CRABServer/blob/f499fd55e4a762ada09ae07e53a78fba034cd804/src/python/TaskWorker/Actions/DagmanSubmitter.py#L548-L549

But I can't find a way to make `schedd.spool()` work. Documentation appears inconsistent with reality.
I have sent a mail to support
<details>
<summary>mail text</summary>

Hi. I am trying to move to new way of submitting in python bindings
https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/htcondor.html#interacting-with-schedulers

But am facing an unexpected obstacle which I do not know how to solve.
Can you help ?

I am using bindings from HTCondor 23.7.2

Since in context of CMS CRAB we submit to remote schedulers,
I have to use

submitResult = schedd.submit(submit_object,...)
schedd.spool(the correct arg !)

So far we have been using the old format
clusterId = schedd.submit(classAd, returnAd)
schedd.spool(returnAd)

I have converted my code which used to pass a classAd object
to create a submit object and I think I getting there since
I get a SubmitResult object with the expected content
(Pdb) type(submitResult)
<class 'htcondor.htcondor.SubmitResult'>
(Pdb) submitResult.cluster()
104893441
(Pdb) submitResult.first_proc()
0
(Pdb) submitResult.num_procs()
1
Pdb) type(submitResult.clusterad())
<class 'classad.classad.ClassAd'>

But I can't find a proper argument for schedd.spool()
the documentation says:

spool(ad_list) → None :

    Spools the files specified in a list of job ClassAds to the condor_schedd.

    Parameters

        ad_list (list[ClassAds]) – A list of job descriptions; typically, this is the list returned by the jobs() method on the submit result object.
    Raises

        RuntimeError – if there are any errors.


Note the :
typically, this is the list returned by the jobs() method on the submit result object.

But the submit result object does not have a jobs() method !!

I tried
schedd.spool(submitResult.clusterad()) , but (abbreviated)
Boost error:  did not match C++ signature:

I tried with a list, but
(Pdb) schedd.spool([submitResult.clusterad()])
*** htcondor.HTCondorIOError: DCSchedd::spoolJobFiles:1:Job ad 0 did not have a proc id
(Pdb)

submitResult.clusterad() has a 'ClusterId' attribute but indeed not a ProcId nor Proc not "proc id"
(Pdb) submitResult.clusterad()['clusterid']
104893441
(Pdb) submitResult.clusterad()['procid']
*** KeyError: 'procid'
(Pdb) submitResult.clusterad()['proc']
*** KeyError: 'proc'
(Pdb) submitResult.clusterad()['proc id']
*** KeyError: 'proc id'
(Pdb)


I am out of ideas

Thanks
Stefano

</details>

Here's ToddM's answer
```
> But submitResult object does not have a jobs() method

    I'd always assumed that the documentation meant "the Submit object's jobs() method", but I'd never actually tested it; it turns out to be just a little more complicated than that.  Full example that seems to work for me follows.  (Job will go on hold because it doesn't produce the
specified output, but that makes it easier to check if everything got spooled correctly.)  Let me know if this works for you.

-- ToddM


#!/usr/env/env python3

import htcondor

collector = htcondor.Collector()
location = collector.locate(htcondor.DaemonTypes.Schedd, "azaphrael.org" )
schedd = htcondor.Schedd(location)

submit = htcondor.Submit("""
    universe = vanilla
    executable = /bin/sleep
    arguments = 1
    transfer_executable = false
    should_transfer_files = true

    transfer_input_files = /tmp/input.txt
    transfer_output_files = output.txt

    queue 1
""")


result = schedd.submit(
    submit,
    spool=True
)

wtaf = submit.jobs(
    count=result.num_procs(),
    clusterid=result.cluster(),
)
schedd.spool(list(wtaf))
_______________________________________________
HTCondor-users mailing list
To unsubscribe, send a message to [htcondor-users-request@cs.wisc.edu](mailto:htcondor-users-request@cs.wisc.edu) with a
subject: Unsubscribe
You can also unsubscribe by visiting
https://lists.cs.wisc.edu/mailman/listinfo/htcondor-users

The archives can be found at:
https://lists.cs.wisc.edu/archive/htcondor-users/
```

## Comment (belforte, 2024-05-29T17:43:26Z)

current state of the art is https://github.com/belforte/CRABServer/tree/add-user-policy-to-tape-recall-8354

By the way #8333 needs to be done at same time as this

## Comment (belforte, 2024-05-29T19:58:43Z)

back to mundane things, there's bunch of things which have different name in JDL vs classAd (e.g. TransferInput vs transfer_input_files) and custom ads which I did not add the `+` initially becasue lack the telling initial `CRAB_` (e.g. MaxWallTimeMinsProbe  and similar used for automatic splitting)

HTC ads which needs a different name in JDL
```
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'TransferInput = InputFiles.tar.gz, subdag.ad' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'Err = /data/srv/tmp/_240529_160122:belforte_crab_20240529_18011856z6jrw8/request.err' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'Out = /data/srv/tmp/_240529_160122:belforte_crab_20240529_18011856z6jrw8/request.out' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'OtherJobRemoveRequirements = DAGManJobId =?= ClusterId' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'TransferOutput = RunJobs.dag.dagman.out, RunJobs.dag.rescue.001' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)
```
CRAB private ads which need the leading `+` sign. The first is a schedd ad coming from collector via HTCondorLocator, but it is not a job Ad ! (and by the way it is always null for us.. maybe it was needed once upon a time....)
```
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'RemoteCondorSetup = ' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'MaxWallTimeMinsTail = 225' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'MaxWallTimeMinsProbe = 60' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'MaxWallTimeMinsRun = 30' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)
/usr/local/lib/python3.8/site-packages/htcondor/_lock.py:70: UserWarning: the line 'MaxWallTimeMins = 30' was unused by Submit object. Is it a typo?
  rv = func(*args, **kwargs)

```

## Comment (belforte, 2024-05-31T08:44:02Z)

submission works now. But Automatic splitting fails to submit the subdag with
```
Submitting job(s)ERROR: unable to read proxy file
ERROR: condor_submit failed; aborting.
```
fixed.
