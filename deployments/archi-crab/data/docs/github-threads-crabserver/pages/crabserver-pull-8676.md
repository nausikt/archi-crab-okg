# dmwm/CRABServer pull request #8676: Task scheduling

State: closed
Opened: 2024-08-30T10:09:05Z
Closed: 2024-09-04T14:22:33Z
Merged: 2024-09-04T14:22:33Z
URL: https://github.com/dmwm/CRABServer/pull/8676

## Opening post (aspiringmind-code, 2024-08-30T10:09:05Z)

Adding task scheduling functionality in TaskWorker based on roundrobin shuffle on users.
Gitlab pipeline runs on preprod: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8028184
See https://github.com/dmwm/CRABServer/wiki/Task-scheduling

## Comment (cmsdmwmbot, 2024-08-30T10:14:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 429 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2136/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-30T11:55:18Z)

@aspiringmind-code please do not close issues "by hand" they will be closed automatically when the PR is merged. 

You should refer the issues in one of the commits or in the PR with the magic words "fix #8676" (some variants are possible.. fixes, solve..) Which is good to do anyhow so that there is a link from the issue to the commit which was meant to solve and viceversa.

In that way the issue will have a link to the PR.
And it will not be closed in case the PR review is negative.

Thanks

## Comment (belforte, 2024-08-30T11:57:21Z)

hu... this was a PR. not an issue. Even worse ! Why did you close ?
PR's flow is from OPEN to MERGED.
CLOSE means that this PR is invalid and must be forgotten, not merged.

I am very confused ! Sorry

## Comment (cmsdmwmbot, 2024-08-30T11:59:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 429 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2137/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-30T12:00:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 429 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2138/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-30T12:13:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 1 warnings
   * 65 comments to review
 * Pycodestyle check: succeeded
   * 429 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2139/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-30T12:21:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 2 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 429 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2140/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-30T12:32:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 429 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2141/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2024-08-30T12:39:12Z)

Fixed the pylint errors and added the wiki page for task scheduling in the initial description. Will squash commits and merge once approved by @belforte

## Comment (belforte, 2024-08-30T15:37:31Z)

My comments are not major things, so this is almost ready to to in production as well. But for that we need to to add things, better via ad -hoc new issues
1. a dry-run option in the configuration (maybe a mode ? on/off/dry )
2. logging so that when it runs in dry mode we know what it would have done. Like print a table with two columns: user/#tasks and say how many for which users would have gone in NEW

## Comment (belforte, 2024-08-30T15:41:16Z)

I notices that we do not have a GH issue to drive this !
PLease make one like "add Task Scheduling capability"

So that you can keep there list of open actions etc.

## Comment (cmsdmwmbot, 2024-09-03T10:17:34Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 429 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2145/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-03T11:49:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 429 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2147/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-03T11:50:31Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 429 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2148/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-03T12:24:22Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 106 comments to review
 * Pycodestyle check: succeeded
   * 435 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2149/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-03T13:02:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 106 comments to review
 * Pycodestyle check: succeeded
   * 439 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2150/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-03T14:57:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 439 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2154/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-03T14:58:49Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 439 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2155/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-03T15:17:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 108 comments to review
 * Pycodestyle check: succeeded
   * 441 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2156/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2024-09-04T08:04:09Z)

Pipeline runs on preprod after the requested changes. See https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8051136 I'm not sure if I understood the dry run thing correctly...see last commit. Requesting @belforte for further comments.

## Comment (belforte, 2024-09-04T08:29:30Z)

>  I'm not sure if I understood the dry run thing correctly

That's where it helps to write down specifications before the code !
"dry run" usually means : show what you would be doing, but do not do it.  https://en.wikipedia.org/wiki/Dry_run_(testing)

## Comment (cmsdmwmbot, 2024-09-04T11:51:31Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 108 comments to review
 * Pycodestyle check: succeeded
   * 441 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2159/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-04T12:15:21Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 109 comments to review
 * Pycodestyle check: succeeded
   * 444 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2160/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2024-09-04T12:23:19Z)

@belforte I am ready to merge. Is it ok?

## Comment (cmsdmwmbot, 2024-09-04T14:06:36Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 114 comments to review
 * Pycodestyle check: succeeded
   * 443 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2161/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-04T14:13:55Z)

WOW. Extra-fancy table. I was thinking of something like "%20s %6d %6d" !

I noticed one thing though. Is dry-run going to be hardcoded to False ?
I may be wrong, but it seems to me that you do not read this from the config file.

This PR has got too long and confused. Make sure that dry_run defaults to True, and merge. Open a new issue about picking TaskScheduler params from config. file, which will require also changes in puppet.

## Comment (aspiringmind-code, 2024-09-04T14:19:33Z)

I thought  we were being safe by putting dry_run as False by default. Yes, you are write this hard codes it to false and we load the config file before that..I will change and merge and open a new issue for that. Thanks! Sorry for the long PR.
