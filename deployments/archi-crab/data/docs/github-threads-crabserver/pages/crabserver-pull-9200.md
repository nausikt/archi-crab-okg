# dmwm/CRABServer pull request #9200: add anySchedd submission test

State: closed
Opened: 2025-10-01T19:13:32Z
Closed: 2025-10-02T06:59:00Z
Merged: 2025-10-02T06:59:00Z
URL: https://github.com/dmwm/CRABServer/pull/9200

## Opening post (belforte, 2025-10-01T19:13:32Z)

(no text)

## Comment (belforte, 2025-10-01T19:14:41Z)

I have verified that this fails when using `preprod` (which has the broken v3.250929) and succeeds using the new "fix" currently deployed in test as per #9199

## Comment (belforte, 2025-10-01T19:16:37Z)

@nausikt @aspiringmind-code this is mostly FYI, but also to give you a starting point in case you want to add or modify tests. We still lack tests for configuration params introduced in last 2~3 years, like GPU-related things.

## Comment (cmsdmwmbot, 2025-10-01T19:16:53Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 108 comments to review
 * Pycodestyle check: succeeded
   * 26 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2648/artifact/artifacts/PullRequestReport.html
