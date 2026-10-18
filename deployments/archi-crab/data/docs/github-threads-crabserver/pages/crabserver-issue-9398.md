# dmwm/CRABServer issue #9398: improve detection of removed (out of bound) jobs in PostJob

State: closed
Opened: 2026-08-24T16:24:11Z
Closed: 2026-09-23T13:32:43Z
URL: https://github.com/dmwm/CRABServer/issues/9398

## Opening post (belforte, 2026-08-24T16:24:11Z)

sometimes jobs are removed by hitting wall or memory limit, bt a FJR is reported to the schedd.
This makes PostJob set a confusing exit code = 80001

Should always check job status, and if it was removed, check reason ads and cross check used from ads vs. limits etc.

Also introduce new ExitCode for "killed by user", when user issues crab kill, jobs get
`RemoveReason = "Python-initiated action (by user crabtw)"`

## Comment (belforte, 2026-08-24T21:35:33Z)

It is also likely that PostJob does not get executed after a `crab kill`, so we will have to stick with 80001 from the job wrapper.
We can possibly edit this in the spider when pushing to OpenSearch, but it may be confusing to get a value there different form the classAd recorded in condor !

## Comment (belforte, 2026-09-15T14:57:09Z)

The best and only way is to add a `JobeExitCode` classAd to all jobs before sending `condor_rm`.
I will introduce ExitCode 50667 for this.

## Comment (belforte, 2026-09-22T14:24:58Z)

Some jobs are condor-rm'ed by Dagman when the DAG itself stops. I have not found any way to flag them
They have `RemoveReason` like
```	DAG Removed: User removed scheduler job from queue. (by user crabtw) ```
or
```   DAG Abort: DAG is exiting and writing rescue file. (by user crabtw) ```

## Comment (belforte, 2026-09-23T13:32:43Z)

after reviewing the code
https://github.com/dmwm/CRABServer/blob/be37a0af0873e3612a646c22ef0a4a3509bc1fd4/src/python/TaskWorker/Actions/RetryJob.py#L671-L687
I got convinced that it already will go through CPU and Memory check if FJR is missing 

Indeed the evidence is that sometimes the classAd update done in the PostJob is not picked up in the monitoring, as I already saw when checking CRAB_TerminationFailure 

Overall there is a low rate of jobs with an inconsistent set of classAds (e.g. have different `RemoveReason` and `PeriodicRemoveReasons`) which popup when looking in fine details. Here's exit code for all jobs removed due to `RemoveReason"Removed due to wall clock limit` in last 30 days. There is all sort of exit codes (including 0) other than 50664,
but those with exit code 80001 are less than 1 in 10^5

<img width="690" height="565" alt="Image" src="https://github.com/user-attachments/assets/a85f6b82-7313-4cff-b775-2e7eba30c45d" />

In conclusion, we have to live with the current situation.
