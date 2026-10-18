# dmwm/CRABServer pull request #9062: chirp exit code of cmscp. Fix #8197

State: closed
Opened: 2025-05-02T13:05:40Z
Closed: 2025-05-05T14:34:22Z
Merged: 2025-05-05T14:34:22Z
URL: https://github.com/dmwm/CRABServer/pull/9062

## Opening post (belforte, 2025-05-02T13:05:40Z)

I could not make cmscp.py fail yet to test this. But at least it does not seem to cause any harm. Will test more.

## Comment (cmsdmwmbot, 2025-05-02T13:08:49Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2445/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-05T14:34:17Z)

Had to hack `cmscp.py` to test, but it works as desired.
