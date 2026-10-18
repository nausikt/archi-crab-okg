# dmwm/CRABServer pull request #7591: 30 days for recall and 30 days for processing. Fix #7590

State: closed
Opened: 2023-04-13T22:10:20Z
Closed: 2023-04-13T22:18:01Z
Merged: 2023-04-13T22:18:01Z
URL: https://github.com/dmwm/CRABServer/pull/7591

## Opening post (belforte, 2023-04-13T22:10:20Z)

(no text)

## Comment (belforte, 2023-04-13T22:14:10Z)

I tested the rule update by running those lines in python interpreter. We do not have any easy way to test in real life other than merging and deploying.

## Comment (cmsdmwmbot, 2023-04-13T22:15:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 4 warnings
   * 111 comments to review
 * Pycodestyle check: succeeded
   * 152 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1488/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-13T22:17:51Z)

jenkins complains are about untouched part of the code. Usual historically "imperfect" syntax
