# dmwm/CRABServer pull request #9287: refactor test pipeline - version 2

State: closed
Opened: 2026-03-29T15:02:22Z
Closed: 2026-04-07T10:48:50Z
Merged: 2026-04-07T10:48:50Z
URL: https://github.com/dmwm/CRABServer/pull/9287

## Opening post (belforte, 2026-03-29T15:02:22Z)

Fixes #9213 
This collects changes from #9280 and #9284 plus fixes to make it all work consistently.
squashing a long and twisted story into a single commit. It also addresses Vijay's comment on #9280 

Here's recap of changes

this brings in extensive changes to test pipeline aimed to
* adapt to changes in CRAB (e.g. new status `Running`)
* ensure that test always and only fail when there's real errors (of course this is an open ended task)
* terse reports, yet allow for ` -o ci.variable="VERBOSE=0|1|2|3" 
* always wait for tasks to be completed even if sleep step was not long enough
* readable, synoptic, view of test status printed at the end of each iteration
* add CMSSW_15 to what we test
* always use CMSSW_15 (and python3) to run scripts which do not require `crab submit`
* refactoring of StatusTracking tests for clean log and full error catching
* reduced amount of testing for oldish CMSSW version
   * StatusTracking is only run for CMSSW>=13
   * CCV is not run for CMSSW < 10 (SL7 releases)
* allow to test release pipeline via tags like `pypi-test2-blah=v3.010101`

## Comment (cmsdmwmbot, 2026-03-29T15:05:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 240 comments to review
 * Pycodestyle check: succeeded
   * 178 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2762/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-29T15:11:16Z)

**IMPORTANT NOTE**
I did not remove the various `  allow_failure: true` in  [.gitlab-ci.yml](https://github.com/dmwm/CRABServer/blob/master/.gitlab-ci.yml) for the release pipeline because at times a test fail due to a glitch and a `retry` fixes it. But this means that all  exclamation points in (pipeline page)[https://gitlab.cern.ch/crab3/CRABServer/-/pipelines] need to be checked by operators before the new release is deployed.

A possible alternative would be to change logic so that every failing test is retried a few times, but at times a job failed on the grid or in the TW and no amount or retrying the check will do. A better way would be to rewrite everything to have a fully autonomous create/submit/check pipeline for each individual test and then combine. But that seems way more work than the above.

A lesson for future projects.

## Comment (cmsdmwmbot, 2026-03-29T15:17:29Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 240 comments to review
 * Pycodestyle check: succeeded
   * 177 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2763/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-30T15:09:32Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 240 comments to review
 * Pycodestyle check: succeeded
   * 177 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2767/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-30T15:19:32Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 240 comments to review
 * Pycodestyle check: succeeded
   * 177 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2768/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-31T08:34:55Z)

here's a pipeline running the new test code in "release" mode i.e. with the full CMSSW matrix
https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/14413065

## Comment (belforte, 2026-03-31T14:43:28Z)

One rucio_transfer test [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260330_160719%3Acrabint1_crab_rucio_transfers_20260330_180716) in that pipeline is hopelessly failing  because one output file was somehow lost on the T2 store/temp disk (gfal-ls lists 0 size and Rucio is stuck with FTS reporting `.TRANSFER_FAILED:User-defined and destination ADLER32 checksum do not match (d2625018 != 00000001)`
With current CRAB there is no way to fix this. The only way to complete the dataset is a new recovery task.

## Comment (cmsdmwmbot, 2026-04-02T15:51:32Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 240 comments to review
 * Pycodestyle check: succeeded
   * 177 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2778/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-04-07T10:48:45Z)

thank you @aspiringmind-code . Merging
