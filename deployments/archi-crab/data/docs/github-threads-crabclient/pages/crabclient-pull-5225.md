# dmwm/CRABClient pull request #5225: make sure all commands return a dict. Fix #5224

State: closed
Opened: 2023-10-16T22:16:08Z
Closed: 2023-10-17T17:46:55Z
Merged: 2023-10-17T17:46:54Z
URL: https://github.com/dmwm/CRABClient/pull/5225

## Opening post (belforte, 2023-10-16T22:16:08Z)

(no text)

## Comment (belforte, 2023-10-16T22:17:37Z)

@mapellidario note that this assumes that https://github.com/dmwm/CRABClient/issues/5224#issuecomment-1765315793 is OK. I am still waiting yours and Wa's opinion on both the strategy and the  implementation.

## Comment (cmsdmwmbot, 2023-10-16T22:23:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 35 warnings and errors that must be fixed
   * 8 warnings
   * 614 comments to review
 * Pycodestyle check: succeeded
   * 446 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/944/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-17T15:34:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 33 warnings and errors that must be fixed
   * 8 warnings
   * 614 comments to review
 * Pycodestyle check: succeeded
   * 446 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/945/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-17T16:06:53Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 35 warnings and errors that must be fixed
   * 8 warnings
   * 606 comments to review
 * Pycodestyle check: succeeded
   * 458 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/946/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-17T16:58:41Z)

@novicecpp I believe that previous commits address all of your comments. Let me know.

## Comment (cmsdmwmbot, 2023-10-17T17:04:02Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 12 warnings
   * 719 comments to review
 * Pycodestyle check: succeeded
   * 528 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/947/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-10-17T17:13:00Z)

Yes.
Thanks Stefano.

## Comment (cmsdmwmbot, 2023-10-17T17:34:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 12 warnings
   * 719 comments to review
 * Pycodestyle check: succeeded
   * 528 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/948/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-17T17:46:44Z)

all those pylint errors are due to "old code which needs to run in python2 as well, did not follow naming conventions and is anyhow untouched and working'
