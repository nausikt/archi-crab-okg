# dmwm/CRABServer pull request #9132: squashed commit from longstanding PR#9082, w/o changes on REST.

State: closed
Opened: 2025-07-11T09:41:26Z
Closed: 2025-07-24T14:49:51Z
Merged: 2025-07-24T14:49:51Z
URL: https://github.com/dmwm/CRABServer/pull/9132

## Opening post (nausikt, 2025-07-11T09:41:26Z)

This PR is forked from #9082 to resolve #6917.

### **Changes on REST (was _EXCLUDED_ from this PR):**
- [ ] [turn-on _expandSites, _checkASODestination at TW, turn-off on REST.](https://github.com/dmwm/CRABServer/pull/9082/commits/750b0ca464947cceb5b58d3114d29646d0ad8fc2)

### **Changes on TaskWorkers:**
_migrating CRIC, Site resolving fns, enabling WMCore cache and some refactoring_
- [x] [add debug logging suppressed CRIC Service.](https://github.com/dmwm/CRABServer/pull/9082/commits/a94bd9244647a0cee8b815b50f3432e80b5b35da)
- [x] [dependency injection, CRICService (resourceCatalog).](https://github.com/dmwm/CRABServer/pull/9082/commits/2ff130a01cfde8b0ef64b371dc6da2bd9fd7984d)
[sinonkt](https://github.com/dmwm/CRABServer/commits?author=sinonkt)
- [x] [refactor the ChildClass inherited from DataDiscovery to use a generic constructor signature.](https://github.com/dmwm/CRABServer/pull/9082/commits/12e92d5b5ca0c4f5c044e126f86c1662befba573)
- [x] [migrate _checkSite, _expandSites and _checkASODestination fns, tested.](https://github.com/dmwm/CRABServer/pull/9082/commits/89e9e6ca881d1cb7c6155e3bc1378699efb2cd66)
- [x] [enable WMCore's usestalecache.](https://github.com/dmwm/CRABServer/pull/9082/commits/575880ec8ff708808fc6eaec4917b3f9cff17a2b)
- [x] [fix return type from list to set.](https://github.com/dmwm/CRABServer/pull/9082/commits/42e91b93366bf7774601e14fd741c736074d9b90)
- [x] [all tm_site_{whitelist|blacklist} have to be expanded.](https://github.com/dmwm/CRABServer/pull/9082/commits/d19cb1a51e13bed36ba91aa87f5bd7c426bc72fb)
- [x] [fixes having to convert to list before JSON-serialize to ClassADs compatible string.](https://github.com/dmwm/CRABServer/pull/9082/commits/1605be17c20251b00db0e4557e60a11ee7cb6060)

_Introducing SiteInfoResolver TaskAction (a more elegance approach suggested by Stefano, also other responses to his review)_
- [x] [introduce SiteInfoResolver Action.](https://github.com/dmwm/CRABServer/pull/9082/commits/d75f1edeb9b3b134a4f36fb5e6d0da4371e6d39c)
- [x] [fixes typos bug, missing global_blaclist/locations var.](https://github.com/dmwm/CRABServer/pull/9082/commits/3d7b9add437d608c82512f5f48e0dae83c6c35ce)
- [x] [missing private fn, clear cut scope of SiteInfoResolver utility.](https://github.com/dmwm/CRABServer/pull/9082/commits/9760561a0c6d3dbbc48e1cab65e969f8796dcee8)
- [x] [passed along expanded site white/black list.](https://github.com/dmwm/CRABServer/pull/9082/commits/4acb9051b3789aad21cd08962091b1daa7174c57)
- [x] [introduce all_possible_processing_sites in task.](https://github.com/dmwm/CRABServer/pull/9082/commits/61dfa9398446d5506caaa930588e1e6343588101)
- [x] [removed redundant site white/black expanding and checking.](https://github.com/dmwm/CRABServer/pull/9082/commits/b11d804a31669aded78e07f99024786eeed5789f)
- [x] [use all_possible_processing_sites in DagmanCreator, move retry CRIC fail into SiteInfoResolver.](https://github.com/dmwm/CRABServer/pull/9082/commits/60b77f4ab86e04ddce1c2a564dc4c15a4a578411)
- [x] [remove unused site checking logic. use resolved site white/black list.](https://github.com/dmwm/CRABServer/pull/9082/commits/bcbcb2dfc14c29166d33843665a04e439962585c)
- [x] [DagmanCreator no longer needed resourceCatalog.](https://github.com/dmwm/CRABServer/pull/9082/commits/36f007c2b57b3835d469ace93801d27ec6a704cf)
- [x] [resourceCatalog is no longer needed in PreDAG as well.](https://github.com/dmwm/CRABServer/pull/9082/commits/298a15d99513fde1279d9bb0a24cdf585ddb4a79)
- [x] [fix formating, typos.](https://github.com/dmwm/CRABServer/pull/9082/commits/cfc2add8c1ea601b677df1ec5e5fd72894caa4ea)
- [x] [[1] PreDag clean up could be later, [2] no more passing down resourceCatalog](https://github.com/dmwm/CRABServer/pull/9082/commits/4e5f87ecf0ac4d0b5ed35c67bf5c644ff6dd1b4f)

## Comment (cmsdmwmbot, 2025-07-11T09:46:20Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 17 warnings and errors that must be fixed
   * 1 warnings
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 215 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2531/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-07-11T15:22:33Z)

> looks much much better now. Thanks. Besides the extra import (hint: run `pylint` on your local version of files). it seems that now `resourceCatalog` is only used inside `SiteInfoResolver`, so why not instantiate it in there, instead of doing it in the Handler and then passing it down ? It will make things more clean and readable, IMHO.
> 
> I am not happy that you introduced changes "for taste" like replacing explicit lists of arguments (which I can understand) with a `*kwargs` which is always very obscure to me. Am I missing a good technical reason for the change ? I have the prejudice that I may still need to be looking at this code further in the future than you will have to. So there is some benefit in making things easy for me.

Roger that Stefano, That's True, I thought about instantiate once just there but forgot to do it. 
and will make sure you are happy by not overdo things for taste! will undo it.

## Comment (cmsdmwmbot, 2025-07-11T15:33:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 1 warnings
   * 36 comments to review
 * Pycodestyle check: succeeded
   * 147 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2532/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-07-11T15:42:19Z)

@belforte It's still not obvious to me how can we release as 2-PRs. 

IMHO, we should do it in 1 PR. Since, right now changes in this PR are expanding/resolving SiteInfo twice, (both on REST, TW)

In my PoV, our current PR will test almost *nothing* regarding migrated functionalities on TW. the way we didn't turn-off functionalities on REST give us False sense of security that everything works but actually it was done on REST.

_In Short_: we should turn-off expanding/resolving site in same PR. So that we resolved just once on TW. then let it test through time in canary.

Could you please show me the way what i might have overlooked? Thanks for your patience!

## Comment (cmsdmwmbot, 2025-07-22T09:58:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 137 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2534/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-07-22T14:26:23Z)

Looks to me that all pylint warning in bold in https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2534/artifact/artifacts/PullRequestReport.html could be resolved. Please aim for score 10 on new code.

## Comment (nausikt, 2025-07-22T14:27:24Z)

> Looks to me that all pylint warning in bold in https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2534/artifact/artifacts/PullRequestReport.html could be resolved. Please aim for score 10 on new code.

Acknowledge Stefano!

## Comment (cmsdmwmbot, 2025-07-22T15:19:28Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 36 comments to review
 * Pycodestyle check: succeeded
   * 145 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2536/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-22T15:27:30Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 45 comments to review
 * Pycodestyle check: succeeded
   * 153 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2537/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-22T15:35:27Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 144 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2538/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-22T17:02:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 144 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2539/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-23T18:44:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 145 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2542/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-07-24T14:20:52Z)

@belforte Hi Stefano, I've tested this PR as following.

- [x] coverage tests were done on *test14* as you can see [here](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12508621)

some more specific tests on *preprod*
- [x] Automatic splitting [250724_132958:kphornsi_crab_testCRICAutomaticSplitting4](https://cmsweb-testbed.cern.ch/crabserver/ui/task/250724_132958%3Akphornsi_crab_testCRICAutomaticSplitting4)
- [x] single wildcard, whitelist = ['T2_IT_*'] [250724_135541:kphornsi_crab_testCRICSingleWildCardWhitelist](https://cmsweb-testbed.cern.ch/crabserver/ui/task/250724_135541%3Akphornsi_crab_testCRICSingleWildCardWhitelist)
- [ ] star wildcard, both '\*', ['\*'] was refused with Incorrect 'Site.whitelist' parameter <class 'str'> *
(P.S. not sure whether * error was expected)

## Comment (belforte, 2025-07-24T14:34:14Z)

OK. Sounds like this is not harmful. Let's merge and we'll run on it more. I am not sure what exactly happens with a site list `['*']` but I am surely happy to refuse it :-)

## Comment (nausikt, 2025-07-24T14:50:47Z)

Thank you Stefano! Finally....😭

## Comment (belforte, 2025-07-24T14:56:29Z)

now you will have to text against a modified REST :-) The pipeline does not exercise wild card expansion
