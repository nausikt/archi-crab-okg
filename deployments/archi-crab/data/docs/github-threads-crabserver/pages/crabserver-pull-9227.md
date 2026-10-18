# dmwm/CRABServer pull request #9227: Remove cacheurl arg from submit

State: closed
Opened: 2025-11-10T14:30:24Z
Closed: 2025-11-11T14:12:29Z
Merged: 2025-11-11T14:12:29Z
URL: https://github.com/dmwm/CRABServer/pull/9227

## Opening post (belforte, 2025-11-10T14:30:24Z)

Now that we have crab client v3.251020 in production we can remove the
obsolete `cacheurl` argument from submit POST call. As per #9167

Take this chance also do do a bit more cleanup and fix pylint complaints

**Beware** this will make REST incompatible with older `crab-pre` client which is currently at `v3.250820`.

Can wait to deploy new REST until e.g. 2026 when new CRAB Client has been in production long enough to be confident that we do not need `crab-pre`

## Comment (cmsdmwmbot, 2025-11-10T14:31:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 10 comments to review
 * Pycodestyle check: succeeded
   * 166 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2664/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-11-10T19:42:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 10 comments to review
 * Pycodestyle check: succeeded
   * 166 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2665/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-11-10T19:46:39Z)

WOW. Amazingly fast review. Hope it was not a ChatGPT-generated one. Thanks

## Comment (nausikt, 2025-11-10T19:55:36Z)

> WOW. Amazingly fast review. Hope it was not a ChatGPT-generated one. Thanks

As a stalker, I've silently reviewed first 2 commits since afternoon. So, i just have a look on last commit one then DONE. LoL
