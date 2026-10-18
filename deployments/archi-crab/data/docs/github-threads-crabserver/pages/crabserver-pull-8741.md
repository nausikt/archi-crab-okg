# dmwm/CRABServer pull request #8741: Adding all the rule states in getTapRecallUsage and a bug fix

State: closed
Opened: 2024-10-14T09:04:16Z
Closed: 2024-11-21T14:00:39Z
Merged: 2024-11-21T14:00:39Z
URL: https://github.com/dmwm/CRABServer/pull/8741

## Opening post (aspiringmind-code, 2024-10-14T09:04:16Z)

Fix #8736

## Comment (cmsdmwmbot, 2024-10-14T09:39:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 8 comments to review
 * Pycodestyle check: succeeded
   * 17 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2200/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-10-14T10:40:40Z)

Aside the minor comment above, there is a fundamental problem here.

* for tape recall we do not want to count rules in OK status, since we want to know what is being asked, not what is on disk. True that now we remove OK rules after 4 days, but still it is better to avoid it
* for input lock almost everything should be OK

I am still puzzled that code could find  a sensible value for input lock while ignoring OK rules. That needs to be understood.
Can you look at it, or do I need to do it ?

## Comment (aspiringmind-code, 2024-10-14T10:48:00Z)

I will look at it.

## Comment (aspiringmind-code, 2024-10-14T11:23:21Z)

@belforte The use of getTapeRecallUsage was merged by me on 17th Sept in https://github.com/dmwm/CRABServer/pull/8697 and the release we are running is that of v3.240904 (4th September). Hence the changes are not yet in production and therefore we have the correct thing from using rucioClient.get_local_account_usage in the 4th Sept version.

## Comment (belforte, 2024-10-14T11:59:56Z)

thanks. So may be we stick with get_local_account_usage for crab_input ? Why bother to sum all rules when we have the total with a single call ?
Maybe I forgetting something ?

## Comment (aspiringmind-code, 2024-10-14T14:06:23Z)

We did the change to address https://github.com/dmwm/CRABServer/issues/8661 as we wanted to filter by activity=AnalysisTapeRecall instead of user, and use user argument only if provided.

## Comment (belforte, 2024-10-14T14:10:07Z)

thanks for fixing my confusion ! and sorry for noise.

## Comment (cmsdmwmbot, 2024-10-17T09:48:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 8 comments to review
 * Pycodestyle check: succeeded
   * 17 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2204/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-10-17T10:51:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 6 comments to review
 * Pycodestyle check: succeeded
   * 33 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2205/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-10-17T10:55:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 33 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2206/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-10-17T11:02:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 31 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2207/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-10-17T12:49:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 31 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2208/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-11-18T10:34:16Z)

@aspiringmind-code I am a bit lost here, sorry. Are you waiting for my feedback ?

## Comment (aspiringmind-code, 2024-11-18T10:49:32Z)

@belforte Ah, no...this is not complete. I'll fix it and tag you for your feedback when done.

## Comment (cmsdmwmbot, 2024-11-19T11:24:02Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 31 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2284/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-20T09:10:07Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 31 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2285/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-20T09:49:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 14 comments to review
 * Pycodestyle check: succeeded
   * 99 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2286/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2024-11-20T09:55:49Z)

@belforte This is ready for review now. Thanks!

## Comment (cmsdmwmbot, 2024-11-20T09:57:15Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 14 comments to review
 * Pycodestyle check: succeeded
   * 99 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2287/artifact/artifacts/PullRequestReport.html
