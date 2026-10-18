# dmwm/CRABServer pull request #9248: make atomicReplaceAcrossFS a py2 compatible.

State: closed
Opened: 2025-12-13T10:21:19Z
Closed: 2025-12-13T10:28:19Z
Merged: 2025-12-13T10:28:19Z
URL: https://github.com/dmwm/CRABServer/pull/9248

## Opening post (nausikt, 2025-12-13T10:21:19Z)

Follow up patches of #9243 regarding #9241 

I've tested on [test14, 13587395](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13587395), this will fix failures in old CMSSWs envs where py2 was used.

Failed emails from `crab-dev-tw02` last night [1] just came from corrupted image, there were nothing go wrong with the new code as you can see in [2]
[1]
```
[FATAL tini (7)] exec python3 failed: No such file or directory
```
[2] the image was premature fetched with size 273 MB instead of 1.x GB.
```
[crab3@crab-dev-tw02 ~]$ docker image ls
REPOSITORY                                TAG                                    IMAGE ID     
  CREATED        SIZE
registry.cern.ch/cmscrab/crabtwmonit      <none>                                 ceac8e90fecd   15 hours ago   273MB
```
AFAIR, we've noted somewhere in past issues, the failed come from **either** (*ordered by likelihood)
1. Inside cicd pipeline who trying to tag and push `v3.2512{13|14}` as `v3.latest` which somehow generated  corrupted image tag.
2. OR during periodically cron fetch, we somehow got corrupted local image as we seen in [2] 
```
# Puppet Name: monit -  get latest docker image for monit scripts
13 * * * * docker pull registry.cern.ch/cmscrab/crabtwmonit:v3.latest >/dev/null 2>&1
```

## Comment (cmsdmwmbot, 2025-12-13T10:26:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 14 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2708/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-12-13T11:25:25Z)

Hi @nausikt for next time a simpler solution could have been to put the new utility in a different place than the "too generic" ServerUtilities which is the only file shared with Client and hence needs to be py2 compatible.

If python2 was used to run the crontab, you could simply move to use py3 there. It makes no sense btw that our container does not have python3 since it is based on python3.8 debian image. Maybe you were simply seeing the effect of partially build image.

FInally, about "too much code in ServerUtility", please see https://github.com/dmwm/CRABServer/issues/7765

Bottom line: do not over-react, take it easy, and let's talk before you do too much

## Comment (nausikt, 2025-12-13T14:15:10Z)

> Hi @nausikt for next time a simpler solution could have been to put the new utility in a different place than the "too generic" ServerUtilities which is the only file shared with Client and hence needs to be py2 compatible.
> 
> If python2 was used to run the crontab, you could simply move to use py3 there. It makes no sense btw that our container does not have python3 since it is based on python3.8 debian image. Maybe you were simply seeing the effect of partially build image.
> 
> FInally, about "too much code in ServerUtility", please see #7765
> 
> Bottom line: do not over-react, take it easy, and let's talk before you do too much

Acknowledged Stefano, Thanks for rationales behind things!
