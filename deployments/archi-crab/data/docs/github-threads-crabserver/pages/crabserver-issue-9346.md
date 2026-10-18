# dmwm/CRABServer issue #9346: Return job stdout when job is removed (evicted)

State: closed
Opened: 2026-07-14T15:27:36Z
Closed: 2026-07-17T13:11:34Z
Labels: Type: Bug, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9346

## Opening post (belforte, 2026-07-14T15:27:36Z)

Long ago Brian introduced the nice feature that job stdout is returned also when job is e.g. terminated (condor_rm) due to excessice memory or time usage in commit  https://github.com/dmwm/CRABServer/commit/43d18053fbaf05650c3927d23dcf58f804c22b0a

But this does not appear to work anymore.

I broke that when reformatting DagmanCreate to use a jobSubmit object instead of JDL-as-a-string.
 According to current Condor documentation,  the correct attribute in the submission JDL is not `WhenToTransferOutput` but `when_to_transfer_output` see e.g.
https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit.html
and https://deepwiki.com/search/if-i-specify-whentotransferout_cffdbf73-b080-4906-a55c-ce3061276ace?mode=fast

After submission that resul in that the classAd  `WhenToTransferOutput`  but the way to set it in the JDL is via `when_to_transfer_output`  as it may be implied by [this](https://htcondor.readthedocs.io/en/latest/apis/python-bindings/tutorials/HTCondor-Introduction.html#Schedd) example.  Yet there is no mention of `WhenToTransferOutput` in current job classAd [documentation](https://htcondor.readthedocs.io/en/latest/classad-attributes/job-classad-attributes.html).
Anyhow I verified that having this in `JobSubmit``
```console
belforte@vocms059/SPOOL_DIR> grep -i when Job.submit 
when_to_transfer_output = ON_EXIT_OR_EVICT
```
results in
```console
belforte@vocms059/SPOOL_DIR> condor_q 10568464 -l|grep -i when
WhenToTransferOutput = "ON_EXIT_OR_EVICT"
```

I also notice that when refactoring DagmanCreator for v2 API, I commented out this line
https://github.com/dmwm/CRABServer/blob/872622c977148a667e0cba9295f9d5951773e20b/src/python/TaskWorker/Actions/DagmanCreator.py#L437-L438
but it is actually a documented feature https://htcondor.readthedocs.io/en/latest/classad-attributes/job-classad-attributes.html#SpoolOnEvict
and should indeed be `False`  !! Since we do not want to transfer back the sandbox on eviction, we want the job to restart cleanly from scratch.

## Comment (belforte, 2026-07-15T08:07:11Z)

the simple fix works ! But I notice that when job is killed and partial stdout file ` cmsRun-stdout.log.tmp ` is printed, the final stdout is not "crisply clear".  I think a problem is
https://github.com/dmwm/CRABServer/blob/872622c977148a667e0cba9295f9d5951773e20b/scripts/job_wrapper/gWMS-CMSRunAnalysis.sh#L273-L274
when condor kills the job while user app is running, a signal is sent while line 273 is being executed.
So 276 is not executed and $EXIT_STATUS stays undefined, execution jumps to  `finish{}` function because of 
https://github.com/dmwm/CRABServer/blob/872622c977148a667e0cba9295f9d5951773e20b/scripts/job_wrapper/gWMS-CMSRunAnalysis.sh#L76
and the call to `check_application_execution` in there results in these lines in job output
```text
======== Figuring out long exit code of the job for condor_chirp at Wed Jul 15 07:49:05 GMT 2026========
==== Failed to load the long exit code from jobReport.exitCode.txt. Falling back to short exit code ====
======== Short exit code also missing. Settint exit code to 80001 ========
```

## Comment (belforte, 2026-07-16T13:41:33Z)

Let's move "improving stdout when killed" to another issue. I am not able to reproduce anymore the "fix".
I.e. job output is not retrieved anymore in spite of `when_to_transfer_output = ON_EXIT_OR_EVICT` in JDL !!

I am puzzled.

## Comment (belforte, 2026-07-16T17:03:06Z)

I tested again w/o the changes to gWMS-CMSRunAnalysis and it works. So will push that in and create a new issue for a better `trap` handling
