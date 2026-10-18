# dmwm/CRABClient pull request #5422: use --jobId as arg for CMSRunAnalysis. Fix #5241

State: closed
Opened: 2025-10-17T21:41:30Z
Closed: 2025-10-20T09:33:11Z
Merged: 2025-10-20T09:33:10Z
URL: https://github.com/dmwm/CRABClient/pull/5422

## Opening post (belforte, 2025-10-17T21:41:30Z)

typo in commit message !! This fixes #5421 !!!

## Comment (cmsdmwmbot, 2025-10-17T21:45:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 1 warnings
   * 56 comments to review
 * Pycodestyle check: succeeded
   * 72 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1143/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-10-17T22:42:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 1 warnings
   * 56 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1144/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-10-17T22:56:35Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 56 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1145/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-10-20T09:15:50Z)

thanks for review @nausikt . Do you care to check that it works for you too ? We do not have a test for this in our pipeline

## Comment (cmsdmwmbot, 2025-10-20T09:22:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 56 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1146/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-10-20T09:25:03Z)

> thanks for review @nausikt . Do you care to check that it works for you too ? We do not have a test for this in our pipeline

tested, It looks good on my side too.
```bash
Dry run
Getting input files into tmp dir /tmp/kphornsi/tmp70z418am
Copying and preparing files for local execution in /tmp/crabStatusTracking/crab_test14-dryrun-20251020-2/local
go to that directory IN A CLEAN SHELL and use  'sh run_job.sh NUMJOB' to execute the job
Execute test run in local sub-directory of /tmp/crabStatusTracking/crab_test14-dryrun-20251020-2
Executing test, please wait...
Last trial took only 16.0 seconds. We are trying now with 29201 events
Last trial took only 8.7 seconds. We are trying now with 57162 events
Last trial took only 8.0 seconds. We are trying now with 122318 events
Last trial took only 8.2 seconds. We are trying now with 195810 events
```

## Comment (belforte, 2025-10-20T09:33:06Z)

thanks Krittin for cross-checking
