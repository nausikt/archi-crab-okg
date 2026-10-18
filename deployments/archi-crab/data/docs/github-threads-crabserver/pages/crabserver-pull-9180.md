# dmwm/CRABServer pull request #9180: Stop using external config part1

State: closed
Opened: 2025-09-08T14:33:16Z
Closed: 2025-09-25T08:27:41Z
Merged: 2025-09-25T08:27:41Z
URL: https://github.com/dmwm/CRABServer/pull/9180

## Opening post (belforte, 2025-09-08T14:33:16Z)

Address initial part of the "PLAN" in #9167 

This requires  that  CRABServer's `config.py` is modified first by adding
* `data.s3_bucket = 'crabcache_dev'` or `crabcache_preprod` or `crabcache_prod` as appropriate for each cluster
* `data.compatibleClientVersions = ["v3", "development"]`

those changes are compatible with current code and can be done at any time

other simplifications can be done after this is deployed:
* remove from CRABServer `config.py`
   * `data.credpath`, `data.phedexurl`,` data.dbsurl`, `data.defaultBlacklist`, `data.mode`
* remove from [cmsweb-rest-config.json](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config.json)
   * "compatible-versions", "banned-out-destinations", "delegate-dn", all "modes"
      * so that it becomes like  https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config-test.json

A successive last cleanup will eliminate all references to external config and get rid of CRAB3ServerConfig once htcondor configuration is moved to TW
 

I have verified that the new code works both with  [current]( https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config.json) and [new]( https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config-test.json) `cmsweb-rest-config-test.json`

And that it works with both [current](https://github.com/sinonkt/CMSKubernetes/blob/migrate-to-argocd/argocd/apps/crab/crabserver/base/config/config.py) config (with the changes indicated above) and the new, leaner one as in [test2](https://gitlab.cern.ch/crab3/crab-k8s-overlays/-/blob/master/argocd/apps/crab/crabserver/overlays/test2/config/config.py)

More testing e.g. in preprod is of course important.

## Comment (cmsdmwmbot, 2025-09-08T14:38:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 12 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 435 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2613/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-08T15:51:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 11 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 435 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2614/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-08T15:54:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 11 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 435 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2615/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-08T16:01:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 11 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 435 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2616/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-08T16:55:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 11 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 435 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2617/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-08T21:27:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 11 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 435 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2618/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-09-09T19:31:44Z)

I believe this is ready to go, but it needs changes to `config.py` first. We should converge in where to make them. But review can be done

## Comment (belforte, 2025-09-25T08:26:44Z)

Thanks Krittin and Vijay for your review.

Congrats Krittin for your new avatar. Cool image. 
I can't resist inserting my own small contribute to Nausicaa's legend using a different alphabet, from the Odyssey, beginning of book 6. (about 800 BC) :

 ἔνι κούρη [...] ' ἀθανάτῃσι φυὴν καὶ εἶδος ὁμοίη, [...], ‘Ναυσικάα θύγατερ μεγαλήτορος Ἀλκινόοιο,
 
(yeah.. it's Greek to me..) here's a hopefully passable translation
a young girl [...] similar to immortals in spirit and likeness [...] Nausicaa, daughter of greathearted Alcinous

you can of course find English (Thai ? Hindy ?) translation of the Odyssey and read the whole story, but I do not recommend it, it is very long and likely boring.  I never did. But my high school studies had ancient Greek language class and we went through some pieces of their literature

## Comment (nausikt, 2025-09-25T08:43:30Z)

> Thanks Krittin and Vijay for your review.
> 
> Congrats Krittin for your new avatar. Cool image. I can't resist inserting my own small contribute to Nausicaa's legend using a different alphabet, from the Odyssey, beginning of book 6. (about 800 BC) :
> 
> ἔνι κούρη [...] ' ἀθανάτῃσι φυὴν καὶ εἶδος ὁμοίη, [...], ‘Ναυσικάα θύγατερ μεγαλήτορος Ἀλκινόοιο,
> 
> (yeah.. it's Greek to me..) here's a hopefully passable translation a young girl [...] similar to immortals in spirit and likeness [...] Nausicaa, daughter of greathearted Alcinous
> 
> you can of course find English (Thai ? Hindy ?) translation of the Odyssey and read the whole story, but I do not recommend it, it is very long and likely boring. I never did. But my high school studies had ancient Greek language class and we went through some pieces of their literature

Thank you man!, Wowww

Glad that you share this hobbyist side too! Didn’t aware that Nausicaä has her origins in The Odyssey (I have to look into that!).

I’m just a Studio Ghibli fanboy—especially of Nausicaä of the Valley of the Wind which we (Vijay and me) watched together on Netflix a few months ago, I hard sale him, LoL!. Highly recommended, very philosophical! I love how big-hearted she is and how tirelessly, relentlessly she works to resolve conflicts with understanding—swimming against the current of a desperate world, yet still managing to get things done. Truly inspiring!

## Comment (belforte, 2025-09-25T08:51:57Z)

May daughter is a fan of Studio Ghibli too. We watched almost all of their movies. Indeed most anime rotate around struggle, perseverance and final victory. She also likes Saint Seya a lot ,called Cavalieri dello Zodiaco (Knights of the Zodiac) in Italy, I am not sure what the original name is.

## Comment (nausikt, 2025-09-25T09:02:21Z)

Ohhh, Woww, you guys sound like a Top fans, nice to meet you companions! I just watched 80% of their movies...

Having to keep turning Vijay into Hayao Miyazaki's crew then, LoL. Last time, i've recommended him "The Boy and the Heron", mixtures vibes & nuances of many Studio Ghibli movies into one.
