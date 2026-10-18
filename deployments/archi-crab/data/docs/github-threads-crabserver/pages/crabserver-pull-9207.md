# dmwm/CRABServer pull request #9207: only 3GB max mem for 1core at initial sub. Fix #9206

State: closed
Opened: 2025-10-09T12:00:35Z
Closed: 2025-10-10T07:55:25Z
Merged: 2025-10-10T07:55:25Z
URL: https://github.com/dmwm/CRABServer/pull/9207

## Opening post (belforte, 2025-10-09T12:00:35Z)

(no text)

## Comment (cmsdmwmbot, 2025-10-09T12:03:21Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 58 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2654/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-10-09T12:13:21Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 58 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2655/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-10-09T13:21:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 58 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2656/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-10-09T13:26:15Z)

Krittin, Vijay,  last change at line 310 is an unrelated pylint fix

## Comment (belforte, 2025-10-09T13:29:30Z)

tested on crab-dev-tw01. I am also running [pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13069318), but it will not exercise the new functionality, it never submits with > 2500 MB requested memory

## Comment (belforte, 2025-10-09T16:40:41Z)

pipeline was all OK https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13069318

## Comment (belforte, 2025-10-10T07:55:17Z)

thanks all for quick review
