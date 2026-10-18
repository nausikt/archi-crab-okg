# dmwm/CRABServer issue #9402: kill early  failing tasks

State: open
Opened: 2026-08-26T15:56:27Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9402

## Opening post (belforte, 2026-08-26T15:56:27Z)

We have situations where some task is misconfigured and all jobs fail. Yet users may not notice/not care and we waste resources.
So as noted (in **bold**) in https://cms-talk.web.cern.ch/t/wasted-cpu-time-corehours-in-crab/147739 we could

* kill task if success rate is e.g. < 80% after 100 jobs. No matter what.

This should be implemented along the lines of what done for excessive ASO failures, with dryRun mode, mail to operators, configurable threshold, and appropriate value for the CRAB_ForcefullyTerminated classAd

## Comment (belforte, 2026-08-26T16:04:00Z)

this is very similar to what current code is already supposed to do
https://github.com/dmwm/CRABServer/blob/6c1e83e10af760bc2a62cc7b3c9a56d59fae3246/src/python/TaskWorker/Actions/PostJob.py#L1761-L1764

But
* that has not been used in a very long time and I am not sure it would still wrok
* I never read that code with care and I do not understand it enough to say if it fits the need
* we want to add the kill step (like done for ASO) so that task is nor revived by a "crab resubmit"
* I think that failure/error fraction is a more useful threshold than absolute number of failures

OTOH, if we reuse existing code, so much the better, and otherwise may consider removing it. It was originally meant to give control to the users by specifying the max amount of failures deemed acceptable in a task, but in practice no user ever used the `failureLimit` configuration parameter and we indeed [marked](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile) it as "very dangerous".

## Comment (nausikt, 2026-09-07T12:15:01Z)

For clarity, could it possibly be that
 
You mean "kill task if **error rate** is e.g. **>** 80% after 100 jobs. No matter what." since this is much safer and well covered wasted tasks use-cases. 

P.S. For example, tasks experienced transient issues may have success rate drop below 80% which will eventually completed most of the time.

## Comment (nausikt, 2026-09-07T12:19:12Z)

Or, in other words, should we instead state: "kill task if **success rate** < **20%**"?

## Comment (belforte, 2026-09-07T14:01:04Z)

success rate < 20% (or any other percentage) would kick in at 4 failed, 1 OK in the first five jobs. Too much aggressive IMHO.

There is no good way to deal with transient issues, once task is killed, is killed. The only way is to let enough jobs complete to stay clear of random fluctuations and apply a cut. That's why we need configurable thresholds:
After at least N jobs have completed, kill if at least X have failed (or less than Y succeeded).

## Comment (belforte, 2026-10-14T14:58:07Z)

Given what we have learnt so far, best is to identify tasks where first 20 jobs all fail, send a mail to operator, and investigate.
I suspect that "everything fails" is less frequent than people think.

## Comment (belforte, 2026-10-14T15:09:23Z)

question: do we count jobs including retries, or excluding retries ? is one of the two much easier to implement ?
