# dmwm/CRABClient pull request #5429: Fix #5427 handle case of incorrect file counting from FJR

State: closed
Opened: 2026-06-29T10:40:32Z
Closed: 2026-06-30T09:33:50Z
Merged: 2026-06-30T09:33:50Z
URL: https://github.com/dmwm/CRABClient/pull/5429

## Opening post (belforte, 2026-06-29T10:40:32Z)

Fixes #5427 
incorrect file (and event) counting happens when FJR contains wrong information due to bad input file naming or is simply faked by users.
If that happens, warn the user and avoid printing misleading information in `crab report`

## Comment (belforte, 2026-06-29T10:41:09Z)

Need to verify compatibility with older python and adapt if needed

## Comment (cmsdmwmbot, 2026-06-29T10:44:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 9 comments to review
 * Pycodestyle check: succeeded
   * 16 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1151/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-06-29T12:27:11Z)

tested with both python3 and python2.7

## Comment (cmsdmwmbot, 2026-06-29T12:28:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 15 comments to review
 * Pycodestyle check: succeeded
   * 16 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1152/artifact/artifacts/PullRequestReport.html
