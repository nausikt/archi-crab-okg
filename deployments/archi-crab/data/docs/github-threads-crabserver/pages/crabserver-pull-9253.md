# dmwm/CRABServer pull request #9253: Use timeless importlib for module importing

State: closed
Opened: 2025-12-19T14:32:02Z
Closed: 2026-03-03T18:51:40Z
Merged: 2026-03-03T18:51:40Z
URL: https://github.com/dmwm/CRABServer/pull/9253

## Opening post (nausikt, 2025-12-19T14:32:02Z)

Resolve #8804 

We have *no* explicit ***import imp*** in our codebase, So basically mostly **imp** deprecations have been addressed by us, bumping WMCore to the py3.12 compliant version, #9254.

This PR was tested via #9251, when env was *lift* to ***py3.12***.
*P.S The PR actually is cherry-picked(s) commits (https://github.com/dmwm/CRABServer/pull/9251/commits/2c6e5990a54160ecc4540645f33c2897a1f8e9dd, https://github.com/dmwm/CRABServer/pull/9251/commits/768bf20a59d202eb7fc68893489f3645567392f8) from https://github.com/dmwm/CRABServer/pull/9251*

## Comment (cmsdmwmbot, 2025-12-19T14:34:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 5 warnings
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 116 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2710/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-03-03T16:38:27Z)

@belforte I think this PR is also ready for merge and testing alongside https://github.com/dmwm/CRABServer/pull/9265, Could you please have a final review? Thanks!
