# dmwm/CRABServer pull request #8698: Fix #8663 adding getsubmitrefusedtasks api

State: closed
Opened: 2024-09-17T13:11:59Z
Closed: 2024-09-19T11:57:39Z
Merged: 2024-09-19T11:57:39Z
URL: https://github.com/dmwm/CRABServer/pull/8698

## Opening post (aspiringmind-code, 2024-09-17T13:11:59Z)

Adding the api for getsubmitrefusedtasks
See https://github.com/dmwm/CRABServer/issues/8663

## Comment (cmsdmwmbot, 2024-09-17T13:15:40Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 34 comments to review
 * Pycodestyle check: succeeded
   * 209 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2170/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-17T14:36:40Z)

Looks good, thanks. Did you test it ?

Please add to top of RESTTask
```
# pylint: disable=unused-argument
```
so to get rid of remaining pylint warning. Ideally one should put such a statement next to each line were it is triggered, to signal that we know that in that line there is an unused arg, but we can't do w/o it. But when it happens in many places, I guess we can excuse us from being a bit lazy

## Comment (cmsdmwmbot, 2024-09-19T11:55:41Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 34 comments to review
 * Pycodestyle check: succeeded
   * 209 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2171/artifact/artifacts/PullRequestReport.html
