# dmwm/CRABServer pull request #9383: Kill tasks after too many aso errors 9355

State: closed
Opened: 2026-08-10T21:43:35Z
Closed: 2026-08-19T15:27:02Z
Merged: 2026-08-19T15:27:02Z
URL: https://github.com/dmwm/CRABServer/pull/9383

## Opening post (belforte, 2026-08-10T21:43:35Z)

(no text)

## Comment (cmsdmwmbot, 2026-08-10T21:48:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 305 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2880/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-08-10T22:19:49Z)

@nausikt this is not a simple change !
Please do not hurry too much and take your time. Again, since it should almost only kick-in when there are many errors, it is not obvious how to test.
I forced failure in a test task and it appears OK.

But critical review of the aim (see the issue) is important.
Hopefully if we deploy w/o changing TaskWorkerConfig.py only the part which propagates ASO error code to `crab status` should be executed. That's a bit easier to test and one may hope that it is harmless.

## Comment (cmsdmwmbot, 2026-08-10T22:24:36Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 305 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2881/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-08-12T14:20:09Z)

on HOLD. I am adding dry run and mail to operators

## Comment (cmsdmwmbot, 2026-08-12T14:20:12Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 310 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2882/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-12T19:58:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 310 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2883/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-12T20:03:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 310 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2884/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-13T09:06:12Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 310 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2885/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-13T09:11:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 310 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2886/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-08-13T09:11:46Z)

This is ready for review now.  Mail it is only sent  to me currently, that helps more testings, we will change when deploy. I still need to fix for using correct total number of job in automatic splitting, where number of jobs changes during task processing. Will open an ad hoc issue and change after this is finalized, since that requires changes beyond PostJob.

## Comment (belforte, 2026-08-13T13:53:13Z)

Thanks Krittin,
great idea to mark tasks/jobs via  a classAd as well. 
Indeed getting  mails is OK for commissioning, but we do not want to get hundreds of them in a day.
Let me make another commit with that !

If we want to prevent more jobs from running, doing it in PostJob is the fastest and easiest. Also I'd rather not add more scripts. Could add functions in task_process, which currently prepares status summary for CRAB client and handles ASO, but that means distributing around "high level" decisions (do I retry or not ?) which are currently taken in PostJob, this seems to make more confusion.

## Comment (belforte, 2026-08-13T14:33:52Z)

I think I need to add also a config. switch to turn off mail sending

## Comment (belforte, 2026-08-13T17:13:15Z)

as I started to look where to add a classAd, I realized that it is easy to add it to the job which is causing the kill. But it is not easy to do for "all jobs killed afterwards, but not those which just completed or will complete between now and when DagmanKiller does a condor_rm of everything'.
Oh well...

## Comment (cmsdmwmbot, 2026-08-13T17:52:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 310 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2887/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-14T08:26:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 312 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2888/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-14T08:28:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 312 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2889/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-15T17:32:11Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 16 warnings and errors that must be fixed
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 313 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2891/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-15T19:53:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 312 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2892/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-17T14:19:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 312 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2894/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-17T14:20:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 312 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2893/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-18T15:02:54Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 312 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2895/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-18T16:04:54Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 312 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2896/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-18T16:06:18Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 312 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2897/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-08-18T16:11:36Z)

@nausikt sorry for long and twisted history of this PR. I am now reasonally happy with it and would like to merge and start testing. Current version sends mail like this. The mail subject clarifies if DryRun or real kill. 
You can look at changes again, or say you trust me and I will merge.
The important thing is be confident that nothing changes with respect to current situation if we keep `DryRun= True`

```
Killing 260818_145929:belforte_crab_20260818_165927 in PostJob for crabId 1.0 on vocms059.cern.ch
Jobs in task : 10
Kill Thresholds: nErrors 2  relFraction 0.5  absFraction 0.1
ASO summary:
 Relative
   OK    0/3 = 0%
   FAIL  3/3 = 100%
 Absolute
   OK    0/10 = 0%
   FAIL  3/10 = 30%
```
