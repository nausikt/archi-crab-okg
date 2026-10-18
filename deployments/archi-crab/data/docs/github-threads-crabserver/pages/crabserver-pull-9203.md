# dmwm/CRABServer pull request #9203: TW no longer query backendurls, solely relied on propagates values in TaskWorkerConfig via puppet

State: closed
Opened: 2025-10-07T12:17:36Z
Closed: 2025-10-13T20:52:58Z
Merged: 2025-10-13T20:52:58Z
URL: https://github.com/dmwm/CRABServer/pull/9203

## Opening post (nausikt, 2025-10-07T12:17:36Z)

Regarding #9201 

I've tested on test14 as you can see [here](https://cmsweb-test14.cern.ch/crabserver/ui/task/251007_114139%3Akphornsi_crab_test14-20251007-2), also more coverage tests in pipeline [there](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13051463).

## Comment (cmsdmwmbot, 2025-10-07T12:21:13Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 7 comments to review
 * Pycodestyle check: succeeded
   * 25 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2650/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-10-07T13:40:36Z)

I looked at the indicated task URL, but surprisingley TW log can not be loaded. Is this something in my browser ? Or do you have same problem meaning there's something to fix ?

## Comment (nausikt, 2025-10-07T13:43:01Z)

> I looked at the indicated task URL, but surprisingley TW log can not be loaded. Is this something in my browser ? Or do you have same problem meaning there's something to fix ?

Thank you Stefano will have a look now.

## Comment (belforte, 2025-10-07T13:45:55Z)

THanks for superfast implementation. Very nice, just a little bit more ...

## Comment (belforte, 2025-10-07T13:52:15Z)

>>    I looked at the indicated task URL, but surprisingley TW log can not be loaded. Is this something in my browser ? Or do you have same problem meaning there's something to fix ?

> Thank you Stefano will have a look now.

hmm.. same happens on my TW. URL seems OK, but it does not work e.g.

https://cmsweb-test2.cern.ch/crabserver/ui/task/crabserver/dev/cache?subresource=download&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348

I have to fear that I broke something... let's see if it works in production

## Comment (cmsdmwmbot, 2025-10-07T13:55:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 7 comments to review
 * Pycodestyle check: succeeded
   * 25 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2651/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-10-07T13:59:58Z)

> > > I looked at the indicated task URL, but surprisingley TW log can not be loaded. Is this something in my browser ? Or do you have same problem meaning there's something to fix ?
> 
> > Thank you Stefano will have a look now.
> 
> hmm.. same happens on my TW. URL seems OK, but it does not work e.g.
> 
> https://cmsweb-test2.cern.ch/crabserver/ui/task/crabserver/dev/cache?subresource=download&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348
> 
> I have to fear that I broke something... let's see if it works in production

Same here on my browser inside CERN network.

## Comment (cmsdmwmbot, 2025-10-13T19:51:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 7 comments to review
 * Pycodestyle check: succeeded
   * 26 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2659/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-10-13T20:02:54Z)

Please fix pylint errors

## Comment (cmsdmwmbot, 2025-10-13T20:32:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 7 comments to review
 * Pycodestyle check: succeeded
   * 26 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2660/artifact/artifacts/PullRequestReport.html
