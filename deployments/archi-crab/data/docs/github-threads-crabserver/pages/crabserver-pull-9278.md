# dmwm/CRABServer pull request #9278: Use local disk to read groups info

State: closed
Opened: 2026-02-27T16:59:12Z
Closed: 2026-02-27T17:28:41Z
Merged: 2026-02-27T17:28:40Z
URL: https://github.com/dmwm/CRABServer/pull/9278

## Opening post (belforte, 2026-02-27T16:59:12Z)

for #9235

## Comment (cmsdmwmbot, 2026-02-27T17:02:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 74 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2746/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-02-27T17:07:11Z)

I will not fixpylint complains in CMSGroupMapper which mostly come from using globals for memory caching which is useless to us, but a cut example to keep around should anybody every want to replicate. Otherwise we could simply refactor keeping only the directory crawler part.

## Comment (belforte, 2026-02-27T17:28:08Z)

I tested on crab-dev-tw91 that my local group T2_US_FNALPC is added correctly and also that my job is submitted in highprio account group after I hacked
```
[crab3@crab-dev-tw01 ~]$ cat /data/container/TaskWorker/groups/highPriorityUsers.json
["belforte"]
[crab3@crab-dev-tw01 ~]$ 
```
