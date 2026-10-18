# dmwm/CRABServer pull request #9322: Remove unused panda(?) keyword since 2021, last use 2013

State: closed
Opened: 2026-06-08T09:23:54Z
Closed: 2026-06-08T10:18:41Z
Merged: 2026-06-08T10:18:41Z
URL: https://github.com/dmwm/CRABServer/pull/9322

## Opening post (oljemark, 2026-06-08T09:23:54Z)

See discussion in https://github.com/dmwm/CRABServer/pull/9321#issuecomment-4642367221 . Last used in CRAB2 https://github.com/dmwm/CRAB2/issues/901

## Comment (cmsdmwmbot, 2026-06-08T09:28:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 warnings
   * 11 comments to review
 * Pycodestyle check: succeeded
   * 24 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2832/artifact/artifacts/PullRequestReport.html

## Comment (oljemark, 2026-06-08T09:35:09Z)

Thanks, there were two more warnings now that I'm fixing.

## Comment (nausikt, 2026-06-08T09:38:38Z)

Thanks for the neat changes!

## Comment (cmsdmwmbot, 2026-06-08T09:54:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 10 comments to review
 * Pycodestyle check: succeeded
   * 22 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2833/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-06-08T10:10:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 10 comments to review
 * Pycodestyle check: succeeded
   * 22 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2834/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-06-08T10:20:08Z)

this will be tested in the next pre-release tag.

## Comment (belforte, 2026-06-09T13:59:38Z)

thanks for the cleanup, but I fail to see the connection with panda !

## Comment (oljemark, 2026-06-09T14:21:03Z)

Hi, @belforte . The removal of the use of this parameter seemed to be the part of the commit https://github.com/dmwm/CRABServer/commit/509b567ba03be54ec8c11489ef9017c1a4f7fe65 that was described by "removal of deprecated pandas code"? Although the separate obsolete parameter panda_resubmitted jobs elsewhere in the codebase may indicate it wasn't actually from panda.
