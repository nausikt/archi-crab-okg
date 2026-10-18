# dmwm/CRABServer issue #9345: do not add walltime over resubmits for maxtime check

State: closed
Opened: 2026-07-13T15:06:19Z
Closed: 2026-07-27T13:11:50Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9345

## Opening post (belforte, 2026-07-13T15:06:19Z)

In the way that we do resubmissions and retries now, it makes no sense to add time spend in previous submissions in order to check for job having exceeded MAX_WALLTIME.
In particular we want to automatically increase walltime request in subsequent resubmissions.

This part must be reviewed
https://github.com/dmwm/CRABServer/blob/872622c977148a667e0cba9295f9d5951773e20b/src/python/TaskWorker/Actions/RetryJob.py#L375-L390

- [x] remove `integrated_job_time`
- [x] check whether it is worth to look at `Committed* ad`
- [x] improve logging so that PostJob log shows  actual usage and limit

## Comment (belforte, 2026-07-13T15:17:31Z)

current PostJonb log is like this
```
Wed, 01 Jul 2026 14:55:04 CEST(+0200):INFO:PostJob ====== Starting to analyze job exit status.
Wed, 01 Jul 2026 14:55:04 CEST(+0200):INFO:PostJob        -----> RetryJob log start -----
Wed, 01 Jul 2026 14:55:04 CEST(+0200):DEBUG:RetryJob Job ads already present. Will not use condor_q, but will load previous jobs ads.
Wed, 01 Jul 2026 14:55:04 CEST(+0200):INFO:RetryJob New job_fjr.2180.2.json file content: {"exitMsg": "Not retrying job due to wall clock limit (job automatically killed on the worker node)", "jobExitCode": 50664, "exitCode": 50664}
Wed, 01 Jul 2026 14:55:04 CEST(+0200):ERROR:RetryJob Original error: Job did not produce a usable framework job report.
Wed, 01 Jul 2026 14:55:04 CEST(+0200):ERROR:RetryJob Not retrying job due to wall clock limit (job automatically killed on the worker node)
Wed, 01 Jul 2026 14:55:04 CEST(+0200):INFO:PostJob        <----- RetryJob log finish ----
Wed, 01 Jul 2026 14:55:04 CEST(+0200):INFO:PostJob The retry handler indicated this was a fatal error.
```

## Comment (belforte, 2026-07-13T15:59:31Z)

can compute wall clock time using the ads `JobCurrentStartDate` and `EnteredCurrentStatus` (the latter is the time when job was removed)
**Note:** cannot use `CommittedTime` since when time limit is exceeded, job is evicted, so `CommittedTime` is reset to 0

Here's an example or relevant classAds from a job which hit the time limit from https://cmsweb.cern.ch/scheddmon/0121/nladams/260619_134211:nladams_crab_ScoutingPFRun3F/postjob.2180.2.txt

| Ad | Value | |
| --- | --- | --- |
|                RemoteWallClockTime |   217638.0 | seconds = 3627 min = 60.4 h|
|   LastRemoteWallClockTime    |144053.0 | seconds = 2400.88 min = 40.01 h|
| MaxWallTimeMinsRun  |  2400 | what is used in PeriodicRemove |
|                                LastMatchTime |  1782766448 | |
|       JobCurrentStartDate   |1782766448| |
|      JobCurrentStartExecutingDate | 1782766453| |
|    EnteredCurrentStatus|  1782910501| delta from JobCurrStartDate =  2400.88 min|
|                  CommittedTime   | 0 |
|   NumJobStarts   | 2 | 
| NumShadowStarts   | 2 |


**Note:** `RemoteWallCLockTime` includes previous attempts, indeed we not even have 60h pilots !
This means that this line is also wrong https://github.com/dmwm/cms-htcondor-es/blob/5fe8acbeaa03c73a8321a6570423857a870241d0/src/htcondor_es/convert_to_json.py#L698

**Note also** the description of `RemoteWallClockTime` vs. `LastRemoveWallClockTime` in https://htcondor.readthedocs.io/en/latest/classad-attributes/job-classad-attributes.html#RemoteWallClockTime and 
https://htcondor.readthedocs.io/en/latest/classad-attributes/job-classad-attributes.html#LastRemoteWallClockTime

## Comment (belforte, 2026-07-14T17:18:19Z)

Note that the job in the example above had two starts, the first time ran for about 20h,  then was killed for unknown reasons and restarted by the schedd)  is summed to the second start (which lasted 40h and was ended  by periodic remove).

## Comment (belforte, 2026-07-23T14:12:50Z)

The thing is that there is no need for a time check in PostJob ! If job runs too long, PeriodicRemove kills it and we know becasue of the RemoveReason. Period.
 So code can be removed and there's no need to look at `Committed*` ads
