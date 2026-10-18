# dmwm/CRABServer pull request #9296: Add awareness of Rucio HTTP exceptions and retry up to 10 times over ~20 minutes

State: closed
Opened: 2026-04-09T20:56:36Z
Closed: 2026-07-22T20:19:51Z
Merged: 2026-07-22T20:19:51Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/pull/9296

## Opening post (nausikt, 2026-04-09T20:56:36Z)

Resolve https://github.com/dmwm/CRABServer/issues/9285

I've released this patch to **crab-dev-tw02** via `v3.latest`, `v3-260409-tolerate-rucio-http-exceptions`.
See also [latest tag in harbour](https://registry.cern.ch/harbor/projects/1891/repositories/crabtwmonit/artifacts-tab)

## How to test
From now on, we should expect *one-sided reporting/emailing* from *only* `crab-prod-tw02` about **503 exceptions.**

*P.S. If its works well, we will promote it into prod with proper release tag.*

## Comment (cmsdmwmbot, 2026-04-09T20:59:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 10 comments to review
 * Pycodestyle check: succeeded
   * 13 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2782/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-04-10T14:35:59Z)

Acknowledged @belforte, will revise/add better docs!

> E.g it is not clear to me what will happen if we get an http exception other than the ones that you list explicitly. Is that fatal ? Ignored ? Retried using default policy ?

Put concretely, RucioException("http status code: 555" or whatever "....") will be treated as **Fatal** (raised right away with no retry), just like other native RucioExceptions.

Meanwhile, "http status code: {403|429|500|502|503}" are specifically trapped by predicate in retry loop earlier, not raised until the maximum number of retries is reached.

> On the substance, are you sure that all other http exceptions deserve a different treatment ? Do we have any evidence of an http exception which is not worth retrying, given that "remote serve is down or anyhow in total confusion" is a condition where retrying after delay is certainly good ?

I mostly follow the standard used on the CRAB REST side. That said, I'm still skeptical on only 403 shouldn't be here *P.S. other make sense to me na. e.g. 429: too many requests, 50X: server faults*, what do you think?
https://github.com/dmwm/CRABServer/blob/216d7f5d698a020104d72b1d354fbcfe906b721e/src/python/RESTInteractions.py#L29-L38

## Comment (belforte, 2026-04-10T14:58:20Z)

RESTInteraction is a bit special because it only talks to our server where our code is in control of what http code is returned, and was also based on experience, in practice we almost never see anything different. Server throttling never really worked (something which Valentin tried to add, but ... somehow he did not really finished and the main problem was DBS which was solved by rewrite in go and separating server for users and prod). So 429 never happens. But we have some http 304 e.g. in current grafana which I have no idea what it is, and http 400 which should not be there, because all queries come from our code and therefore should better be good ones. It is also true that those HTTP codes may come from cmsweb FrontEnd, not necessarily CRAB Server... 
There would be a lot to investigate there. SImly do not take that code as gold standard !

You have to choose between adding http errors from Rucio "as they pop up", possibly after having investigated and figured out what they are, or be proactive and say "retry them all". The former is more work. The latter may potentially obscure some issue worth reporting... But for CRAB Rest we felt we had a duty to fix our server, so preferred to call it fatal any "unknowns" error. For Rucio... what do we do if we get some odd errors at a low rate ?

## Comment (nausikt, 2026-04-10T15:13:55Z)

Thanks for extreme clarity & history!🙇‍♂️

Forgive me, for had switched off my brain, the former investigate & patch "as they pop up", make much more sense to me!

Will converge to only 503 for now then🫡

## Comment (cmsdmwmbot, 2026-04-17T15:45:15Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 10 comments to review
 * Pycodestyle check: succeeded
   * 13 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2798/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-05-11T17:22:13Z)

@nausikt forgive may failing memory. What is the status of this ?

## Comment (belforte, 2026-05-20T08:33:32Z)

@nausikt what is the status of this ? If you only retry 503, what will you do  if we get some odd errors at a low rate from Rucio ?  Set up an alarm to let you know when it happens and change the code ?

## Comment (belforte, 2026-07-22T14:39:38Z)

@nausikt ping. What is the status of this ? Pls do not forget your own PR !

## Comment (nausikt, 2026-07-22T14:53:03Z)

My patch on crab-dev-tw02 was overwritten for a while i guessed, thus we have reports from both {dev|prod}-tw02 cron this morning. [1]

I can't remembered the reasons why i've to hold this PR let's get it merged and propagated.

<img width="1186" height="459" alt="Screenshot 2026-07-22 at 16 48 38" src="https://github.com/user-attachments/assets/1e882519-65dd-4d0a-8972-9c4c5786f519" />

## Comment (nausikt, 2026-07-22T14:59:08Z)

> @nausikt what is the status of this ? If you only retry 503, what will you do if we get some odd errors at a low rate from Rucio ? Set up an alarm to let you know when it happens and change the code ?

I see, I'll move it to be configurable as well. like your https://github.com/dmwm/CRABServer/issues/9341#issue-4805906730

Let me take care both retryable config in one shot.

## Comment (belforte, 2026-07-22T15:49:39Z)

I like simple solutions. Why can't we simply retry ALL http exceptions 3 times ?

## Comment (cmsdmwmbot, 2026-07-22T17:10:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 10 comments to review
 * Pycodestyle check: succeeded
   * 15 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2866/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-07-22T17:12:14Z)

Agree, but i guessed you meant 5XX right? retry 4XXs may not helpful.

And can we not stick to 3 times? is 10 times exponentials backoff over 20 mins as we've now acceptable for you?  

P.S., rucio client already have built-in 3 times retrying mechanism over few seconds.

## Comment (belforte, 2026-07-22T17:26:42Z)

> Agree, but i guessed you meant 5XX right? retry 4XXs may not helpful.

In principle you are right. In practice we never make illegal requests or similar, why should we ever get 4XX if not because of a server error ? What do we gain by failing earlier ?

> And can we not stick to 3 times? is 10 times exponentials backoff over 20 mins as we've now acceptable for you?

I wrote w/lo looking.. do you mean that all retries happen within 20 minutes max ? That's fine for me. All in all all our queries should succeed, we sort out bugs in development. If something fails, it can only be network or server problem. So we retry

## Comment (belforte, 2026-07-22T17:27:34Z)

>  rucio client already have built-in 3 times retrying mechanism over few seconds.

yes, but it is clearly insufficient, so we had to add our own :-(

## Comment (nausikt, 2026-07-22T19:58:11Z)

@belforte I think current implementation was aligned with your comments, please, feel free to approve at your convenience.

## Comment (cmsdmwmbot, 2026-07-22T19:59:15Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 9 comments to review
 * Pycodestyle check: succeeded
   * 14 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2867/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-07-22T20:04:30Z)

thanks @nausikt . Sorry for my being lazy and commenting on your comment before reading the code !

## Comment (belforte, 2026-07-22T20:05:56Z)

Please take care of commit signature :-(

## Comment (nausikt, 2026-07-22T20:08:08Z)

No apologies! Thanks to you as always for thought provoking clarification.

Yeah.... old PR, I learned not to forget PR the hard way.

## Comment (cmsdmwmbot, 2026-07-22T20:20:13Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2869/artifact/artifacts/PullRequestReport.html
