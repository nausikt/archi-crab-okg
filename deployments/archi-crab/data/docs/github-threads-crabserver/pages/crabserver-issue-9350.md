# dmwm/CRABServer issue #9350: Improve job stdout when job is removed

State: closed
Opened: 2026-07-16T17:04:01Z
Closed: 2026-07-21T16:02:00Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9350

## Opening post (belforte, 2026-07-16T17:04:01Z)

move here from #9346 

 I notice that when job is killed and partial stdout file ` cmsRun-stdout.log.tmp ` is printed, the final stdout is not "crisply clear".  I think a problem is
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

## Comment (belforte, 2026-07-16T17:14:27Z)

Let me try to work on this now that I am fresh of looking at it.

## Comment (belforte, 2026-07-17T09:28:57Z)

after getting hints from Google and Claude I have changed trap handling from
https://github.com/dmwm/CRABServer/blob/1038e05ebaf8cc0ae95906d385899d8344b1d460/scripts/job_wrapper/gWMS-CMSRunAnalysis.sh#L57-L59
https://github.com/dmwm/CRABServer/blob/1038e05ebaf8cc0ae95906d385899d8344b1d460/scripts/job_wrapper/gWMS-CMSRunAnalysis.sh#L75-L76
to
```python
function finish {
  if [ -n "$caught_signal" ]; then
    echo "Caught signal: $caught_signal"
    EXIT_STATUS=`kill -l $caught_signal`  # from signal name to signal number
    echo "set EXIT_STATUS to $EXIT_STATUS"
    unset caught_signal
  else
    echo "Normal exit"
  fi
  echo "Application exit status: $EXIT_STATUS"
  chirp_exit_code
[...]
  exit $EXIT_STATUS
}
# Trap all exits and execute finish function, while
# making sure that we detect signals meant to stop the job
caught_signal=""
trap 'caught_signal=SIGINT; finish'  SIGINT
trap 'caught_signal=SIGTERM; finish' SIGTERM
trap 'caught_signal=SIGHUP; finish'  SIGHUP
trap 'caught_signal=SIGKILL; finish'  SIGKILL
trap 'finish' EXIT
```

But after that job output is not returned to AP anymore !!

I had tested that change running interactively `gWMS-CMSRunAnalysis.sh` and it was all fine. So it seems that when running in the `startd` something else is going on.
I am trying to add the "extra trap" one at a time.

## Comment (belforte, 2026-07-17T13:14:23Z)

if I only leave
`trap 'caught_signal=SIGINT; finish'  SIGINT`
and comment out all other `trap` statements, output is returned and is truncated w/o the `finish()` being executed.
This indicates that SIGINT is not issued when job is removed

## Comment (belforte, 2026-07-17T13:33:30Z)

I believe that `condor_rm` results in SIGTERM, consistently with [the doc](https://htcondor.readthedocs.io/en/latest/users-manual/job-scheduling.html#how-jobs-are-vacated), so next I try
```
# making sure that we detect signals meant to stop the job
caught_signal=""
trap 'caught_signal=SIGINT; finish'  SIGINT
#trap 'caught_signal=SIGTERM; finish' SIGTERM
trap 'caught_signal=SIGHUP; finish'  SIGHUP
trap 'caught_signal=SIGKILL; finish'  SIGKILL
trap 'finish' EXIT
```
and I get
```
Now running the CMSRunAnalysis.py job in /srv...
+ python3 CMSRunAnalysis.py --jobId=1 --oneEventMode=0
Normal exit
Application exit status: 
======== Figuring out long exit code of the job for condor_chirp at Fri Jul 17 13:31:18 GMT 2026========
==== Failed to load the long exit code from jobReport.exitCode.txt. Falling back to short exit code ====
======== Short exit code also missing. Setting exit code to 80001 ========
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
======== Checking execution of user application (cmsRun and scriptExe) Fri Jul 17 13:31:18 GMT 2026========
the file cmsRun-stdout.log.tmp exists
[...]
Begin processing the 796th record. Run 1, Event 4775, LumiSection 24 on stream 0 at 17-Jul-2026 15:31:18.550 CEST

the file cmsRun-stdout.log does **NOT** exist
======== Checking execution of cmsRun Fri Jul 17 13:31:18 GMT 2026========
the file FrameworkJobReport.xml exists
the file FrameworkJobReport.xml is non-empty. wc (newlines, words, bytes):  3 5 111 FrameworkJobReport.xml
the file jobReport.json.1 exists
the file jobReport.exitCode.txt does **NOT** exist
======== Finished - Checking execution of user application Fri Jul 17 13:31:18 GMT 2026========
Job started:   1784294951 ,  Fri Jul 17 13:29:11 GMT 2026
Job finished:  1784295078 ,  Fri Jul 17 13:31:18 GMT 2026
Job Running time in seconds:  127
```
I.e. the script is terminated at 2min and goes through `trap 'finish' EXIT` like "before"

## Comment (belforte, 2026-07-17T13:49:08Z)

next test, enable `trap` on SIGTERM, but with a plain `finish`, same syntax as current `trap finish EXIT`
```text
trap 'caught_signal=SIGINT; finish'  SIGINT
#trap 'caught_signal=SIGTERM; finish' SIGTERM
trap finish SIGTERM
trap 'caught_signal=SIGHUP; finish'  SIGHUP
trap 'caught_signal=SIGKILL; finish'  SIGKILL
trap 'finish' EXIT
```
This time no output is retrieved.

**Conclusion: if I `trap SIGTERM` condor out retrieval is broken** !!??

## Comment (belforte, 2026-07-17T15:48:51Z)

Last test, with a simple
`trap /usr/bin/date SIGTERM`

still, no output.

Maybe we need to make sure that SIGTERM reaches the parent process of the wrapper ?
I tried to use in the trap a function which sends `kill SIGTERM $$` as per a hint which I found via google, but no change.

## Comment (belforte, 2026-07-20T19:58:52Z)

Since there is no way to trap SIGTERM, I fall back to the simplest and safest options of adding some lines to stdout to explain
the situation and will chirp back exit code *`50666 =  Job killed by condor for unknown reasons `* leaving it to PostJob to refine it based on PeriodicRemovalReason

## Comment (belforte, 2026-07-20T20:24:37Z)

new jobs stdout will have these "message lines":
```text
$ cat job_out.1.0.txt|grep ===
[...] more lines at the beginnning
======== CMSRunAnalysis.py STARTING at Mon Jul 20 20:14:05 GMT 2026 ========
======== Figuring out long exit code of the job for condor_chirp at Mon Jul 20 20:16:12 GMT 2026========
==== Failed to load the long exit code from jobReport.exitCode.txt. Falling back to short exit code ====
======== Short exit code also missing. Setting exit code to 80001 ========
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
======== Checking execution of user application (cmsRun or scriptExe) Mon Jul 20 20:16:12 GMT 2026========
========================================================================
======== User application did not complete due to an external signal ===
======== Most likely we got a SIGTERM from HTCondor             ========
======== Job execution stops here, and ExitCode is set to 50666 ========
======== available application log (if any) will be printed below ======
========================================================================
===== END OF FILE ==== 
======== Checking execution of cmsRun Mon Jul 20 20:16:12 GMT 2026========
======== Finished - Checking execution of user application Mon Jul 20 20:16:12 GMT 2026========
======== Figuring out long exit code of the job for condor_chirp at Mon Jul 20 20:16:12 GMT 2026========
==== Failed to load the long exit code from jobReport.exitCode.txt. Falling back to short exit code ====
==== Short exit code of the job is 50666 ====
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
```
and jobs completes with these classAds

```
           Chirp_CRAB3_Job_ExitCode    50666
                           ExitCode    143
```
Note that 143 = 128 + 15 and 15 is SIGTERM
Then PostJob sets (and chirps) the final exit code for e.g. `crab status`:
`1 jobs failed with exit code 50664`
