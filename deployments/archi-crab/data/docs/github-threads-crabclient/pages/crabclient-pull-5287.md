# dmwm/CRABClient pull request #5287: preparelocal creates one json file with args for job. Fix #5276

State: closed
Opened: 2024-01-30T17:10:51Z
Closed: 2024-01-30T17:23:38Z
Merged: 2024-01-30T17:23:38Z
URL: https://github.com/dmwm/CRABClient/pull/5287

## Opening post (belforte, 2024-01-30T17:10:51Z)

also a small change to the Hellp message for `--instance`

## Comment (cmsdmwmbot, 2024-01-30T17:13:03Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 39 comments to review
 * Pycodestyle check: succeeded
   * 139 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1050/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-01-30T17:23:26Z)

pylint complaints are the expected ones for py2 compatibility.
