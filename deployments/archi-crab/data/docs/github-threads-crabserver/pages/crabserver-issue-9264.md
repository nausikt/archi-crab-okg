# dmwm/CRABServer issue #9264: improve resubmission policies

State: closed
Opened: 2026-01-20T17:05:53Z
Closed: 2026-07-03T19:29:12Z
Labels: Type: Enhancement, Type: Support
URL: https://github.com/dmwm/CRABServer/issues/9264

## Opening post (belforte, 2026-01-20T17:05:53Z)

We have evidence that more jobs will complete successfully if resubmitted more than the current 3 times (1 + 2 retries).

As clear in the [dashboard](https://monit-grafana.cern.ch/d/d07e49f1-7779-42ad-a9ff-d54dd4b9b829/crab-usage-spark?orgId=11&from=now-90d&to=now) created by our summer student last summer
Shown here for the most common exit codes

<img width="1353" height="643" alt="Image" src="https://github.com/user-attachments/assets/6be29dbd-c6a5-4c88-90a2-ff7f4a3629da" />

There is also a very long tail with many jobs succeeding after 20 attempts or more

<img width="1315" height="277" alt="Image" src="https://github.com/user-attachments/assets/a1d27761-10de-43dc-9490-e4332d927d85" />
I have excluded exit code 8028 (fail to open after fallback to xrootd) since that is likely dominated by automatic, immediate, user-initiated retries for files missing or corrupted or located at unavailable sites which usually get OK after a few days.

Since most user run wrapper scripts around CRAB which aggressively resubmit failed jobs, the number of retries is not that important IMHO.

What we lack here is the fraction of the times that jobs are NOT fixed by retry, e.g. 50115 could often be a CMSSW segfault which can very well be persistent.

Overall I think we have these main categories:
1. file open error, which requires retry with delay and/or run at different site
2. jobs which hit memory or wall clock limit, which require increasing it (which users usually do in their resubmissions, see below)
3. jobs which fail during ASO, where I believe that we can not improve on current policy, unless we add a 1 day delay on all ASO failures
4. jobs which failed with various possible exit codes, but due to local problems at the WN where we currently do not retry or retry too soon (I have seen cases where CRAB resubmissions are done so quickly that land on same WN due to HTCondor claim lease and of course suffer same problem)
5. there are errors which are almost never fixed (e.g. CMSSW configuration problem 8006) and we should avoid to retry ten times !

In view of increasing the retry count, and somehow having in mind WMA policy of "10 retries" I looked at which exit codes require more than 10 retries before becoming success (linear and log scale).  I do not understand the bin at exit code = 0, hopefully picture is still correct.

<img width="1312" height="421" alt="Image" src="https://github.com/user-attachments/assets/69a03c76-918f-4a4c-80e2-8bf15ebb3d1a" />

The clear outlier is 8028. Which is "expected" and well understood. I do not know what to exactly make of 50115 which as said above is a times a sort of catch-all, but we can start by simply retrying that 10 times as well, and in case make an ad-hoc study.


Finally I looked at how much users use resubmissions and how much they change requirements (time, memory, sites) see [e-log](https://cms-talk.web.cern.ch/t/how-much-are-users-resubmitting/140275?u=belforte)
Summarizing the tables in there I conclude that approximately:
* 20% of tasks get resubmitted by users
* half of those tasks get some change in requirements !!
* mostly users change the running time limit, when they ask for more memory, they also ask for more time
   * I can not say if those changes are done in a "meditated way", or some people have scripts that always ask for more time when they resubmit
*  only 6% of resubmitted tasks got a change in site black or white list, clearly only done after human decision and possibly suggestion by us





All of this is based on data from last 3 months, so picture may not be fully representative, but that's what we have and surely it is "not too wrong" all in all use patterns are quite constant.

## Comment (belforte, 2026-01-20T17:15:26Z)

Now that we hopefully understand what's going on, we can try to make a plan for improving things, i.e. move work from users to CRAB.

1. Introduce in automatic resubmission the possibility to:
   1. have a delay
   2. have an error code dependent number of retries
   3. change site(s)
   4. change memory or time requirement2. Review the classification of exit codes in [RetryJob](https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/RetryJob.py) (rewrite it ?) and define the more flexible policies above for each
3. make all resubmission have a minimum delay (10min ? 30min?) to avoid the "re-run on same broken WN" effect ?

## Comment (belforte, 2026-02-11T09:27:14Z)

@aspiringmind-code do I understand it correctly that you volunteered to work on this ? If so, please change assignment.

## Comment (aspiringmind-code, 2026-02-11T09:56:12Z)

Yes, thanks!

## Comment (belforte, 2026-07-03T19:29:12Z)

closed via #9319
