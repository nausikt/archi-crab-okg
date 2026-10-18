# dmwm/CRABServer pull request #8807: fixing ruciousage logic

State: closed
Opened: 2024-11-22T08:46:19Z
Closed: 2024-11-22T10:20:10Z
Merged: 2024-11-22T10:20:10Z
URL: https://github.com/dmwm/CRABServer/pull/8807

## Opening post (aspiringmind-code, 2024-11-22T08:46:19Z)

Specifying how to calculate rucio usage in cases of different account and activity

## Comment (cmsdmwmbot, 2024-11-22T08:50:02Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2288/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-11-22T09:30:13Z)

Logic looks good. I have put a couple comments in the code.
Did you verify that no change is required in code which calls this ?

## Comment (aspiringmind-code, 2024-11-22T09:50:16Z)

@belforte Yes, no change is required on the side of code that calls getRucioUsage. I have added your requested changes. Thanks!

## Comment (cmsdmwmbot, 2024-11-22T09:51:04Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2289/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-11-22T10:06:03Z)

looks good.
