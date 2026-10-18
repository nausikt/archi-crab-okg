# dmwm/CRABServer pull request #9276: add exit code dependent retry policy

State: closed
Opened: 2026-02-24T13:35:55Z
Closed: 2026-06-01T06:58:31Z
URL: https://github.com/dmwm/CRABServer/pull/9276

## Opening post (aspiringmind-code, 2026-02-24T13:35:55Z)

Fix #9264 

Salient Features of the New ExitCode Dependent Resubmission and Retry Policy:

- Automatic calculation of job id specific `resubmit_counter` based on lastExitCode dependent max_retries and crab_retry
- `retries_consumed_for_ec` resets to 0 when exitCode changes
- We start with 100 retries limit. But it increases with every resubmit. By how much is ExitCode dependent. Most popular case would be the limit becoming 103, 106,... with each resubmit. So effectively the user does not hit an upperbound as long as they wish to resubmit. This preserves current behaviour
- In the case of no parameters specified with resubmission, if exit code suggests that increasing maxmemory or maxjobruntime can help, automatic increase by 30% tried until hitting the upperbounds of 7500 MB and 47 hours respectively
- retry delay of 900 s is added for each recoverable error exit code. This delay can be changed for each exit Code
- If exitcode shows that changing site will help, the site of the last retry run is dropped from the availableSet for the current retry. Note that the site is not blacklisted and will be available for subsequent retries. Also note that this feature happens even in the retries of simple submit (i.e. not only for crab resubmit but also for retries of simple crab submit)
- The source of truth is EXIT_RETRY_POLICY dictionary in RetryJob. It has every recoverable exit code with keys like `type, max_retries, delay, msg, change_site, increase_memory, memory_factor, runtime_factor, increase_runtime and handler`
- effective_max_retries will be exit code dependent calculated by the formula `(base_max + 1)*(resubmit_counter + 1) - 1` where `base_max` is specified in the policy dict. So for an exit code like 8020 every resubmit will give additional 3 retries. For exitcode 8028 every resubmit will give additional 10 retries.
- When effective_max_retries for a recoverable error is reached FatalError is raised. User can do resubmit.
- Only recoverable errors specified in the policy are retried. Fatal errors will pass through the default route and won't be retried.
- ToDos for subsequent improvement:
   Make files inside resubmit_info json instead of txt
   Avoid short and long exit code redundancy in the EXIT_RETRY_POLICY

## Comment (cmsdmwmbot, 2026-02-24T13:40:41Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2738/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-02-24T15:58:16Z)

more on the "substance", it is not good to use `sleep` inside RetryJob i.e. inside PostJob (which calls this).
We are limited by the how many PostJob can run concurrently, due to memory constrain. The preferred implementation would be what is done when waiting for ASO, exit with a proper exit code which tells Dagman to rerun the Post (or Pre ?) step after a delay (example of delay in PreJob is the use of `deferTime` in there).

Notice that delaying the PostJob also delays the status reporting, the DAG node is still not completed. Rather once we introduce re-submission delays of several hours (days ?) we should worry about properly reporting this to user.
I think that currently jobs are reported in "toRetry" or "cooloff" (unfortunately there is some  inconsistency) when the DAG node is completed with error but not resubmitted yet. At least that's a status that appears at times, but I have
not done a careful study of the current implementation.

## Comment (cmsdmwmbot, 2026-02-24T17:30:37Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 185 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2739/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-02-24T18:43:56Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 110 comments to review
 * Pycodestyle check: succeeded
   * 191 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2740/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-30T15:01:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 223 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2766/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-31T08:18:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 222 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2769/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-31T09:59:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 221 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2770/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-31T11:33:25Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 122 comments to review
 * Pycodestyle check: succeeded
   * 264 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2771/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-31T13:30:37Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 114 comments to review
 * Pycodestyle check: succeeded
   * 266 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2772/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-31T14:41:27Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 115 comments to review
 * Pycodestyle check: succeeded
   * 266 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2773/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-01T11:24:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 117 comments to review
 * Pycodestyle check: succeeded
   * 267 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2776/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-01T14:01:27Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 117 comments to review
 * Pycodestyle check: succeeded
   * 267 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2777/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-10T08:40:35Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 117 comments to review
 * Pycodestyle check: succeeded
   * 267 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2784/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-10T10:23:38Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 138 comments to review
 * Pycodestyle check: succeeded
   * 273 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2785/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-13T09:10:38Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 138 comments to review
 * Pycodestyle check: succeeded
   * 273 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2788/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-13T11:48:53Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 169 comments to review
 * Pycodestyle check: succeeded
   * 287 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2790/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2026-04-13T12:39:20Z)

Salient Features of the New Resubmission and Retry Policy:

- `CRAB_ResubmitCounter` job ad incremented every time user does crab resubmit
- The upperbound on retries across all possible resubmissions for a job is set at 103.
- In the case of no parameters specified with resubmission, if exit code suggests that increasing maxmemory or maxjobruntime can help, automatic increase by 30% tried until hitting the upperbounds of 7500 MB and 47 hrs respectively
- retry delay of 900 s added for each recoverable error exit code
- If exitcode shows that changing site will help, the site of the last retry run is dropped from the availableSet for the current retry. Note that the site is not blacklisted and will be available for subsequent retries. Also note that this feature happens even in the retries of simple submit (i.e. not only for crab resubmit but also for retries of simple crab submit)
- The source of truth is EXIT_RETRY_POLICY dictionary in PreJob. It has every recoverable exit code with keys like `type, max_retries, delay, msg, change_site, increase_memory, memory_factor, runtime_factor, increase_runtime and handler`
- effective_max_retries will be exit code dependent calculated by the formula `(base_max + 1)*(resubmit_counter + 1) - 1` where `base_max` is specified in the policy dict. So for an exit code like 8020 every resubmit will give additional 3 retries. For exitcode 8028 every resubmit will give additional 10 retries.
- When effective_max_retries for a recoverable error is reached FatalError is raised. User can do resubmit.
- Only recoverable errors specified in the policy are retried. Fatal errors will pass through the default route and won't be retried.
- ABORT-DAG-ON command removed from DAG_FRAGMENT

## Comment (belforte, 2026-04-14T08:41:55Z)

Once this is stable, better move the salient features summary at the top "description" (and add the units to 900).
Or even make a clean PR with all commits squashed and just the description !

## Comment (belforte, 2026-04-16T16:22:43Z)

thanks @aspiringmind-code  I believe that this is good, yet I have some comments here and there.

Also, as discussed in the meeting, let's make sure that we start by deploying a new code which should behave identically to current one. Keep it in use for a couple of weeks, and then start changing retry policies.
Feel free to propose a different plan, of course. I like to change one thing at a time, but am open to being convinced otherwise.

## Comment (cmsdmwmbot, 2026-04-17T10:33:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 169 comments to review
 * Pycodestyle check: succeeded
   * 287 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2796/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-17T11:48:57Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 169 comments to review
 * Pycodestyle check: succeeded
   * 294 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2797/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-20T13:08:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 169 comments to review
 * Pycodestyle check: succeeded
   * 294 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2800/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-20T14:18:03Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 169 comments to review
 * Pycodestyle check: succeeded
   * 294 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2801/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-20T14:22:52Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 169 comments to review
 * Pycodestyle check: succeeded
   * 294 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2802/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-04-20T15:02:42Z)

about `Tried as integer, doesn't work. Causes Submit Failed. makeJobSubmit expects integers to be passed as strings`
The constrain actually comes from `htcondor2.Submit()` class which requires strings on the RHS of assignments [1]
But I was expecting to see it to become an `int` internally[2]

e.g. these lines
```python
        retry_aso = "1" if getattr(self.config.TaskWorker, 'retryOnASOFailures', True) else "0"
        jobSubmit['My.CRAB_RetryOnASOFailures'] = retry_aso
```
result in
```
belforte@vocms059/SPOOL_DIR> condor_q 10486848.0 -af  CRAB_RetryOnASOFailures
1
```
This is also confirmed by a small python test [3]

Of course one `int()` too many will not hurt, but I am puzzled. Something else is going on.

[1]
```
>>> j=htcondor2.Submit()
>>> j['a']=2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib64/python3.9/site-packages/htcondor2/_submit.py", line 139, in __setitem__
    raise TypeError("value must be a string")
TypeError: value must be a string
>>> 
```
[2]
```
>>> j['a']="2"
>>> j
Submit(a = 2
queue
)
>>> 
```

[3]
```
belforte@vocms059/SPOOL_DIR> python3
Python 3.9.25 (main, Mar 26 2026, 00:00:00) 
[GCC 11.5.0 20240719 (Red Hat 11.5.0-11)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor2
>>> sched=htcondor2.Schedd()
>>> ad=sched.query('clusterid==10486848')
>>> ad[0,'CRAB_RetryOnASOFailures']
1
>>> type(ad[0,'CRAB_RetryOnASOFailures'])
<class 'int'>
>>> 
```

## Comment (cmsdmwmbot, 2026-04-22T09:57:01Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 169 comments to review
 * Pycodestyle check: succeeded
   * 294 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2804/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-22T11:46:04Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 170 comments to review
 * Pycodestyle check: succeeded
   * 293 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2805/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-22T13:36:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 170 comments to review
 * Pycodestyle check: succeeded
   * 293 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2806/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-22T15:50:05Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 170 comments to review
 * Pycodestyle check: succeeded
   * 293 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2807/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-22T17:29:02Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 170 comments to review
 * Pycodestyle check: succeeded
   * 293 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2808/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-22T17:51:56Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 167 comments to review
 * Pycodestyle check: succeeded
   * 250 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2810/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-22T18:05:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 167 comments to review
 * Pycodestyle check: succeeded
   * 250 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2811/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-24T10:46:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 167 comments to review
 * Pycodestyle check: succeeded
   * 250 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2812/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-24T11:28:01Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 179 comments to review
 * Pycodestyle check: succeeded
   * 253 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2813/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-24T11:38:02Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 179 comments to review
 * Pycodestyle check: succeeded
   * 253 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2814/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-04-24T13:32:18Z)

I have read all the code now and completed my review. Looks to me that all is clear, with exception of ongoing discussion on how to handle max_retry: error-dependent or fixed ? Which is a sort of major design decision and deserves some thinking.

## Comment (cmsdmwmbot, 2026-04-28T11:28:42Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 179 comments to review
 * Pycodestyle check: succeeded
   * 253 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2816/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-28T13:07:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 161 comments to review
 * Pycodestyle check: succeeded
   * 243 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2817/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-28T15:25:44Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 161 comments to review
 * Pycodestyle check: succeeded
   * 243 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2819/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-29T08:58:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 161 comments to review
 * Pycodestyle check: succeeded
   * 243 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2820/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-29T09:02:39Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 161 comments to review
 * Pycodestyle check: succeeded
   * 243 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2821/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-04-29T16:23:51Z)

In today's (29/04/2026) meeting we discussed how to count/limit retries and resubmissions.
Here's summary
* we agree that `maxRetry` can not be exit-code dependend. Each job which completes with recoverable error is retried, up to a maximum. A fatal error terminates automatic retries. We start with `maxRetry=10`
* There are 3 things which one may want to count (and keep track of)
   * `retryNumber` like now, the number of times a job is submitted for a given crabId, from to max in DagMan (100 currently). This is needed to uniquely identify the condor job, pre/post-job logs, records in OpenSearch etc. LIke now. 
      *  Its Semantics is not changing. 
   * `resubmitNumber` the number of times a user has issued a `crab resubmit` for this crabId. Easy to define. Hard to compute and track.
      * Its usefulness is not clear, other than as possibly having a role in computing next counter `retryInThisResubmissionCycleNumber`
   *  `retryInThisResubmissionCycleNumber`, let's shorten to RRN : Retry in (Re)submission Number
      * Semantics: this counter is what must be compared with maxRetry (i.e. 10) to decide if a new automatic retry (i.e. a new condor_submit) should be done or the job set to `failed` due to max reached. 
      * It is not immediately obvious how to determine this. We discussed two ways:
         1.  guess the resubmission cycle by using `mod(retryNumber,10)` and set RRN as `retryNumber-resubmitNumber*10` (maybe +1 or -1 ... a detail). Pros: easy and simple . Cons: in case of fatal errors next resubmit may have <10 retries, down to possible just one, such undefined max_retry may be confusing for ops and users.
         2. increment RRN at every job submission, but reset to 0 when `crab resubmit` is processed.  Pros: this is exactly what we want. Cons: more code is needed and it is difficult (impossible) to avoid that a Dagman restart (schedd failure or whatever) looks like a `resubmit`

Of course we need to track (i.e. persist on disk) the counters which we will be using, currently this is being done via DAG retry counter inside dagman log and node_status files, and crabId specific files in `SPOOL_DIR/retry_info/job.<crabId>.txt` . New code in this PR also introduces `resubmit_info/job.<crabId>.txt`. We discussed changing to JSON.  If RRN is not coomputed in PreJob (1. above) it will need to be persisted on disk too.
 
Stefano (who proposed 2.) has some ideas on its implementation:

**Idea1. not good**: Use classAd `CRAB_ResubmitList` in PreJob.py to know that current crabId is being resubmitted. Along the lines of how it is used in PreJob to set `use_resubmit_info`. It does not work because that classAd "sticks" and the PreJob has no way to know if this is a resubmission or not. Also code will get confused if another resubmit arrives while dagman was still starting, possibly with a different jobId list, so the previous list gets lost before it was fully used. We saw during tests that some jobs could "not be resubmitted".

**Idea2. not clearly wrong**: Leverage `adjustSites.py` inside `dag_bootstrap_startup.sh`. It runs when dagman is not running, so we know that nothing changes in DAG status. Persist RRN in for each Job in some file (one per task will suffice). Increment the jobId value in each PreJob (need a lock due to concurrency, or go for thousand small files again)  and compare with `maxRetry` in PostJob (like now) to decide whether to submit again or not. Inside `adjustSites.py` i.e. at each dagman restart, use classAd `CRAB_ResubmitList` to reset RRN for those jobs.
   * In a way this reproduces current (Brian's) implementation where RRN is the Dagman Retry counter and adjust sites hacks Dagman log and status files to do the resetting. By letting Dag node retry counter run free and moving the RRN counter in our scope, we gain robustness, clarity and flexibility. Hopefully all the places in the code where DAG_RETRY was used have been changed already in this PR.
  * About resubmission vs. dagman restarts, since `CRAB_ResubmitList` sticks, every Dagman restart will look to the code like a new `crab resubmit` with same list of jobs to resubmit as last one. This should have no effect on crabIds which have completed by "now", but for those which were being retried it will reset the RRN counter, basically giving them a higher max_retry. Having more retries is not as bad as having less (does not decrease chances for success!) and, since such unintended dagman restarts are rare, chances for confusions are much fewer. An idea to tell resbumits from restarts, could be to inroduce a `thisIsResumit' classAd to be used as a boolean flag: DagmanResubmitter sets it to True, adjustSites  checks it in order to decide if to reset RRN's, then sets it to False after the reset id done. So in case of a restart, RRN's will not be touched.

## Comment (cmsdmwmbot, 2026-05-28T11:12:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 161 comments to review
 * Pycodestyle check: succeeded
   * 243 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2825/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2026-06-01T06:58:31Z)

Closing with follow up in #9318
