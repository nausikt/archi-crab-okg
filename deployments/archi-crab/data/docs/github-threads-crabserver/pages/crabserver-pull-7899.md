# dmwm/CRABServer pull request #7899: make sure that test is COMPLETED in the scheduler. Fix #7896

State: closed
Opened: 2023-10-06T19:30:52Z
Closed: 2023-10-09T14:08:30Z
Merged: 2023-10-09T14:08:30Z
URL: https://github.com/dmwm/CRABServer/pull/7899

## Opening post (belforte, 2023-10-06T19:30:52Z)

see discussion in #7896 about the rational for this change

## Comment (cmsdmwmbot, 2023-10-06T19:33:20Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 29 comments to review
 * Pycodestyle check: succeeded
   * 7 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1716/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-06T19:43:39Z)

this needs to run in python2 too,  so we keep those pylint warnings

## Comment (belforte, 2023-10-09T14:22:26Z)

I have built test image version 231009 to pickup this change
