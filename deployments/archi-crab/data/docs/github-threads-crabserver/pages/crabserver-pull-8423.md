# dmwm/CRABServer pull request #8423: sanitize extraJDL. See #8420

State: closed
Opened: 2024-05-22T09:14:25Z
Closed: 2024-05-22T10:04:07Z
Merged: 2024-05-22T10:04:07Z
URL: https://github.com/dmwm/CRABServer/pull/8423

## Opening post (belforte, 2024-05-22T09:14:25Z)

(no text)

## Comment (cmsdmwmbot, 2024-05-22T09:20:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 50 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1995/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-22T09:50:36Z)

pylint complains refer to "tricky" strings in the submission dagAd part which shoud better not be touched. May go away with #8336
