# dmwm/CRABServer pull request #9360: build in the code list of short exit codes. Fix #9340

State: closed
Opened: 2026-07-20T22:49:39Z
Closed: 2026-07-22T14:25:33Z
Merged: 2026-07-22T14:25:33Z
URL: https://github.com/dmwm/CRABServer/pull/9360

## Opening post (belforte, 2026-07-20T22:49:39Z)

(no text)

## Comment (cmsdmwmbot, 2026-07-20T22:53:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 110 comments to review
 * Pycodestyle check: succeeded
   * 16 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2861/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-07-21T16:25:55Z)

@nausikt I have added a caution comment and used `shortCode` as suggested by AI.
I still need to start with `newERP[code] = policy` because the original dictionary may contain both long and short codes, who knows. 
But when looking harder I think that there was a mistake. So I made another commit.
What do you think ?

## Comment (cmsdmwmbot, 2026-07-21T16:27:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 110 comments to review
 * Pycodestyle check: succeeded
   * 16 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2864/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-07-21T16:28:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 110 comments to review
 * Pycodestyle check: succeeded
   * 16 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2865/artifact/artifacts/PullRequestReport.html
