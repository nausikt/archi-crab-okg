# dmwm/CRABServer pull request #9128: Remove old cache status code 

State: closed
Opened: 2025-07-09T08:39:28Z
Closed: 2025-07-23T19:09:04Z
Merged: 2025-07-23T19:09:04Z
URL: https://github.com/dmwm/CRABServer/pull/9128

## Opening post (belforte, 2025-07-09T08:39:28Z)

fix #9051

## Comment (belforte, 2025-07-09T08:40:55Z)

Let's wait for master to be usable again (fix Rucio retries) so that pipeline can be used, before merging.

## Comment (cmsdmwmbot, 2025-07-09T08:42:48Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2528/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-07-22T13:47:55Z)

rebased to current master. Now test

## Comment (cmsdmwmbot, 2025-07-22T13:50:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2535/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-22T19:40:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2540/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-07-23T19:08:55Z)

validation in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12499918
(one Rucio rule got stuck on an odd FTS error, but things are fine otherwise).
