# dmwm/CRABServer pull request #8979: DagmanCreator updates num_jobs in taks. Fix #7766

State: closed
Opened: 2025-03-12T11:12:14Z
Closed: 2025-03-12T20:14:11Z
Labels: Status: On Hold
URL: https://github.com/dmwm/CRABServer/pull/8979

## Opening post (belforte, 2025-03-12T11:12:14Z)

a bit ugly for my test. Pisses me off that we have a `task` dictionary which does not have all columns from DB. But let's make sure it work first, and beautify later.

**Note: needs a REST built with changes from https://github.com/dmwm/CRABServer/pull/8978**

## Comment (cmsdmwmbot, 2025-03-12T11:15:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 75 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2399/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-03-12T11:16:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 75 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2400/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-12T11:23:37Z)

@aspiringmind-code let me know how much disgusting does the new code look to you. vs. having available `kw['task','tm_num_jobs']` . Yeah.. we should also set "way up" `self.taskDict=kw['task']` and use it consistently in all those actions :-(

## Comment (belforte, 2025-03-12T20:13:19Z)

@aspiringmind-code this could not work. Sorry, No need to review. Will let you know when it is ready

## Comment (belforte, 2025-03-12T20:14:11Z)

actually better close this. i will work in the new branch `addInfoToTasks-03-25`

## Comment (aspiringmind-code, 2025-03-13T09:28:56Z)

Ok, understood.
