# dmwm/CRABServer issue #9367: improve reporting for out of memory jobs

State: closed
Opened: 2026-07-27T13:50:38Z
Closed: 2026-07-27T16:08:53Z
URL: https://github.com/dmwm/CRABServer/issues/9367

## Opening post (belforte, 2026-07-27T13:50:38Z)

currently PostJob log prints
```text
Mon, 27 Jul 2026 11:05:34 CEST(+0200):INFO:PostJob        -----> RetryJob log start -----
Mon, 27 Jul 2026 11:05:34 CEST(+0200):DEBUG:RetryJob Job ads already present. Will not use condor_q, but will load previous jobs ads.
Mon, 27 Jul 2026 11:05:34 CEST(+0200):INFO:RetryJob This is job retry number 0. Will not try to search and load previous job ads.
Mon, 27 Jul 2026 11:05:34 CEST(+0200):INFO:RetryJob New job_fjr.149.0.json file content: {"exitMsg": "Job killed by HTCondor due to excessive memory use (RSS=2250 MB). Will not retry it.", "jobExitCode": 50660, "exitCode": 50660}
Mon, 27 Jul 2026 11:05:34 CEST(+0200):ERROR:RetryJob Original error: Job did not produce a usable framework job report.
Mon, 27 Jul 2026 11:05:34 CEST(+0200):ERROR:RetryJob Job killed by HTCondor due to excessive memory use (RSS=2250 MB). Will not retry it.
Mon, 27 Jul 2026 11:05:34 CEST(+0200):INFO:PostJob        <----- RetryJob log finish ----
```

Should print (more clearly) both used and max memory.
This is similar to #9366 where the "correct message" is in a part of the code which is never executed because out of memory is catched by PeriodicRemove, not looking at usage in FJR !

Thanks @nausikt for pointing out
(if I misunderstood, please add in here)

## Comment (belforte, 2026-07-27T14:31:40Z)

new code prints
```
Mon, 27 Jul 2026 16:23:29 CEST(+0200):INFO:PostJob        -----> RetryJob log start -----
Mon, 27 Jul 2026 16:23:29 CEST(+0200):DEBUG:RetryJob Job ads already present. Will not use condor_q, but will load previous jobs ads.
Mon, 27 Jul 2026 16:23:29 CEST(+0200):INFO:RetryJob This is job retry number 0. Will not try to search and load previous job ads.
Mon, 27 Jul 2026 16:23:29 CEST(+0200):INFO:RetryJob New job_fjr.1.0.json file content: {"exitMsg": "Job killed by HTCondor due to excessive memory use (2000 used vs. 500 requested) Will not retry it.", "jobExitCode": 50660, "exitCode": 50660}
Mon, 27 Jul 2026 16:23:29 CEST(+0200):ERROR:RetryJob Original error: Job did not produce a usable framework job report.
Mon, 27 Jul 2026 16:23:29 CEST(+0200):ERROR:RetryJob Job killed by HTCondor due to excessive memory use (2000 used vs. 500 requested) Will not retry it.
Mon, 27 Jul 2026 16:23:29 CEST(+0200):INFO:PostJob        <----- RetryJob log finish ----
```
and `crab status --verboseErrors` has
```text
Error Summary:

1 jobs failed with exit code 50660:

	1 jobs failed with following error message: (for example, job 1)

		Job killed by HTCondor due to excessive memory use (2000 used vs. 500 requested) Will not retry it.


```
