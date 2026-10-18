# dmwm/CRABClient pull request #5260: Move checkdataset to crab client repo fix 5233

State: closed
Opened: 2023-11-27T22:04:39Z
Closed: 2023-11-29T18:45:09Z
Merged: 2023-11-29T18:45:09Z
URL: https://github.com/dmwm/CRABClient/pull/5260

## Opening post (belforte, 2023-11-27T22:04:39Z)

also introduce `commandUsedInsideCrab()` function in `ClientUtilities` so that we can decide if/when to use `print()` in a command for extra-verbosity of "progress report in same line" which only applies when using `crab` command, not the python Client API

## Comment (cmsdmwmbot, 2023-11-27T22:10:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 5 warnings
   * 126 comments to review
 * Pycodestyle check: succeeded
   * 143 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1028/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-28T07:35:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 5 warnings
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 143 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1029/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-28T08:16:18Z)

**HOLD**
this PR is broken somewhere
something has gone wrong in one of last commits. Since now
```
belforte@lxplus808/TC3> crab status 
Traceback (most recent call last):
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/bin/crab.py", line 22, in <module>
    from CRABClient.ClientUtilities import getAvailCommands, initLoggers, setConsoleLogLevelVar, StopExecution, flushMemoryLogger, LOGFORMATTER
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/ClientUtilities.py", line 32, in <module>
    from CRABClient.UserUtilities import getUsernameFromCRIC
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/UserUtilities.py", line 17, in <module>
    from CRABClient.ClientUtilities import DBSURLS, LOGLEVEL_MUTE, colors
ImportError: cannot import name 'DBSURLS' from partially initialized module 'CRABClient.ClientUtilities' (most likely due to a circular import) (/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/ClientUtilities.py)
belforte@lxplus808/TC3> 
```

## Comment (belforte, 2023-11-28T08:47:45Z)

I think cleanest solution is to more `getUsernameFromCRIC` from `UserUtilities` to `ClientUtilities` since users are satisfied with the "technology independent" `getUsername`.
I guess when I switched from SiteDB to CRIC I did not dare to change too much.
The error was triggered when moving the import from "inside the code" to top of file, but this way it is better.

## Comment (cmsdmwmbot, 2023-11-28T08:50:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 5 warnings
   * 80 comments to review
 * Pycodestyle check: succeeded
   * 167 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1030/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-28T09:19:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 warnings
   * 78 comments to review
 * Pycodestyle check: succeeded
   * 167 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1031/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-28T09:20:32Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 warnings
   * 78 comments to review
 * Pycodestyle check: succeeded
   * 167 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1032/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-28T09:39:21Z)

ready for review. Unfortunately we need to commit to a branch in main repo in order to test with Jenkins.

## Comment (belforte, 2023-11-28T14:05:57Z)

Jenkins OK for CMSSW 13 and 7 
* https://github.com/dmwm/CRABServer/issues/8021
* https://github.com/dmwm/CRABServer/issues/8024

for other release need to fix Jenkins first https://github.com/dmwm/CRABServer/issues/8025

after moving Jenkins to use singularity CMSSW_10 is also OK
* https://github.com/dmwm/CRABServer/issues/8027

## Comment (cmsdmwmbot, 2023-11-29T16:43:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 warnings
   * 77 comments to review
 * Pycodestyle check: succeeded
   * 167 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1033/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-29T16:48:10Z)

@novicecpp the problems with Jenkins have been understood and this file now "compliles" in python2 too. Ready for review. Let me know if you prefer to call you out of this, then I merge and "since it is a new funcitonality, we can surely find and fix bugs later on"

## Comment (belforte, 2023-11-29T18:13:21Z)

yes it is done in there. I did in two PR to avoid having to wait for this to be merged before doing the other.

## Comment (belforte, 2023-11-29T18:13:47Z)

a bit of a mess :-( My fault

## Comment (belforte, 2023-11-29T18:44:49Z)

thanks for spotting this !!
But I do not feel comfortable at changing a file in two PR's like this.
Let me merge, and then address checkfile in #5262
