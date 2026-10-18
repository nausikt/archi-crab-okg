# dmwm/CRABServer pull request #9338: lock migration account file when updating

State: closed
Opened: 2026-07-01T15:14:04Z
Closed: 2026-07-01T15:35:53Z
Merged: 2026-07-01T15:35:53Z
URL: https://github.com/dmwm/CRABServer/pull/9338

## Opening post (belforte, 2026-07-01T15:14:04Z)

I have seen that times the file gets re-written. I do not see how it could happen, but clearly it does not fulfill the goal of storing information on failures over time.
So let's try with a lock.

## Comment (cmsdmwmbot, 2026-07-01T15:17:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 2 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2850/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-07-01T15:35:44Z)

thanks Krittin !
