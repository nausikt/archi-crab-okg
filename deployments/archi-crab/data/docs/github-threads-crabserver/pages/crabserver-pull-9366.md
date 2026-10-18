# dmwm/CRABServer pull request #9366: correct handling of too much wall clock. Fix #9345

State: closed
Opened: 2026-07-27T09:10:51Z
Closed: 2026-07-27T13:11:49Z
Merged: 2026-07-27T13:11:49Z
URL: https://github.com/dmwm/CRABServer/pull/9366

## Opening post (belforte, 2026-07-27T09:10:51Z)

also improves message in PostJob. When job hit maximum wall time it will print
```text
Mon, 27 Jul 2026 11:04:56 CEST(+0200):INFO:PostJob        -----> RetryJob log start -----
Mon, 27 Jul 2026 11:04:56 CEST(+0200):DEBUG:RetryJob Job ads already present. Will not use condor_q, but will load previous jobs ads.
Mon, 27 Jul 2026 11:04:56 CEST(+0200):INFO:RetryJob This is job retry number 0. Will not try to search and load previous job ads.
Mon, 27 Jul 2026 11:04:56 CEST(+0200):INFO:RetryJob New job_fjr.1.0.json file content: {"exitMsg": "Not retrying job due to wall clock limit (job automatically killed on the worker node)\nJobs lasted 131.0 seconds (0:02:11) vs. 120 (0:02:00) MAX", "jobExitCode": 50664, "exitCode": 50664}
Mon, 27 Jul 2026 11:04:56 CEST(+0200):ERROR:RetryJob Original error: Job did not produce a usable framework job report.
Mon, 27 Jul 2026 11:04:56 CEST(+0200):ERROR:RetryJob Not retrying job due to wall clock limit (job automatically killed on the worker node)
Jobs lasted 131.0 seconds (0:02:11) vs. 120 (0:02:00) MAX
Mon, 27 Jul 2026 11:04:56 CEST(+0200):INFO:PostJob        <----- RetryJob log finish ----
```
and `crab status --verboseErrors` prints
```text

1 jobs failed with exit code 50664:

	1 jobs failed with following error message: (for example, job 1)

		Not retrying job due to wall clock limit (job automatically killed on the worker node)
		Jobs lasted 131.0 seconds (0:02:11) vs. 120 (0:02:00) MAX

```

## Comment (cmsdmwmbot, 2026-07-27T09:14:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 18 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2870/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-07-27T10:15:22Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 18 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2871/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-07-27T13:07:15Z)

report for memory should have a nice message already
https://github.com/dmwm/CRABServer/blob/ea2f8c0bfa80ac2c0d9b2d2065f6f0130f9a39d7/src/python/TaskWorker/Actions/RetryJob.py#L424-L426

But I do not see that in [PostJob log](https://cmsweb.cern.ch/scheddmon/0196/qinju/260726_124537:qinju_crab_7_2025Cv1/postjob.149.0.txt)
```text
Mon, 27 Jul 2026 11:05:34 CEST(+0200):INFO:PostJob        -----> RetryJob log start -----
Mon, 27 Jul 2026 11:05:34 CEST(+0200):DEBUG:RetryJob Job ads already present. Will not use condor_q, but will load previous jobs ads.
Mon, 27 Jul 2026 11:05:34 CEST(+0200):INFO:RetryJob This is job retry number 0. Will not try to search and load previous job ads.
Mon, 27 Jul 2026 11:05:34 CEST(+0200):INFO:RetryJob New job_fjr.149.0.json file content: {"exitMsg": "Job killed by HTCondor due to excessive memory use (RSS=2250 MB). Will not retry it.", "jobExitCode": 50660, "exitCode": 50660}
Mon, 27 Jul 2026 11:05:34 CEST(+0200):ERROR:RetryJob Original error: Job did not produce a usable framework job report.
Mon, 27 Jul 2026 11:05:34 CEST(+0200):ERROR:RetryJob Job killed by HTCondor due to excessive memory use (RSS=2250 MB). Will not retry it.
Mon, 27 Jul 2026 11:05:34 CEST(+0200):INFO:PostJob        <----- RetryJob log finish ----
```

will investigate

## Comment (belforte, 2026-07-27T13:11:26Z)

indeed the "nice message" is in a part of code which does not get executed, similar to what happened to max time. I'll make a new issue and PR

## Comment (belforte, 2026-07-27T13:11:43Z)

thanks @nausikt  !!!
