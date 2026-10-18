# dmwm/CRABServer pull request #8595: use TaskWorkerConfig to enable use of V2 bindings

State: closed
Opened: 2024-08-07T20:59:36Z
Closed: 2024-08-09T23:14:11Z
Merged: 2024-08-09T23:14:11Z
Labels: To be tested, PR: do not merge
URL: https://github.com/dmwm/CRABServer/pull/8595

## Opening post (belforte, 2024-08-07T20:59:36Z)

fix #8571 
#### Summary:
* switch v1/v2 works
* Running with v1 is OK.
* Testing highlighted another problem in using v2, will fix that separately.

## Comment (cmsdmwmbot, 2024-08-07T21:07:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 18 warnings
   * 513 comments to review
 * Pycodestyle check: succeeded
   * 908 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2095/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-08T15:19:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 369 comments to review
 * Pycodestyle check: succeeded
   * 904 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2097/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-08T16:21:05Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 369 comments to review
 * Pycodestyle check: succeeded
   * 904 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2098/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-08T16:26:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 370 comments to review
 * Pycodestyle check: succeeded
   * 904 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2099/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-09T07:54:53Z)

validation with v1 bindings passed
- [x] https://github.com/dmwm/CRABServer/issues/8599

## Comment (belforte, 2024-08-09T10:01:48Z)

WOW. What a careful review. Thanks Wa. I will address the minor comments.
As to testing v2 version, I did and it works at first sight, but I have found one more issue to fix https://github.com/dmwm/CRABServer/issues/8597
I'd rather like to close the "a switch for v2" chapter and do more changes and testing on the master branch.

## Comment (cmsdmwmbot, 2024-08-09T14:08:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 371 comments to review
 * Pycodestyle check: succeeded
   * 903 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2100/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-09T14:29:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 370 comments to review
 * Pycodestyle check: succeeded
   * 903 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2101/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-09T15:15:46Z)

one last round of validation after the changes..
### pipeline (here it uses v1)
- [x] https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7908895  pipelined timed out because Rucio is taking time, but otherwise all OK

### Jenkins
#### v1
- [x] CCV https://github.com/dmwm/CRABServer/issues/8600
- [x] SST https://github.com/dmwm/CRABServer/issues/8601

#### v2
- [ ]  :no_entry:  CCV https://github.com/dmwm/CRABServer/issues/8602 (doomed, was running on schedd w/o v2)
- [x] SST https://github.com/dmwm/CRABServer/issues/8603
- [x] CCV on vocms059 https://github.com/dmwm/CRABServer/issues/8606

## Comment (belforte, 2024-08-09T23:13:57Z)

OK. Let's go
