# dmwm/CRABServer pull request #9148: Fix unexpanded site White/Black list when we do resubmission.

State: closed
Opened: 2025-08-07T12:33:55Z
Closed: 2025-08-11T16:27:55Z
Merged: 2025-08-11T16:27:55Z
URL: https://github.com/dmwm/CRABServer/pull/9148

## Opening post (nausikt, 2025-08-07T12:33:55Z)

Resolve #9147

## Comment (cmsdmwmbot, 2025-08-07T12:38:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 17 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2548/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-07T12:46:52Z)

this will not be enough, of course

## Comment (nausikt, 2025-08-07T12:48:48Z)

Sorry...man, didn't pushed yet.

## Comment (cmsdmwmbot, 2025-08-07T13:11:10Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 19 comments to review
 * Pycodestyle check: succeeded
   * 41 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2549/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-07T13:35:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 119 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2550/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-07T13:39:56Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 119 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2551/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-07T13:59:20Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 6 comments to review
 * Pycodestyle check: succeeded
   * 190 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2552/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-07T14:07:21Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 22 comments to review
 * Pycodestyle check: succeeded
   * 115 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2553/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-07T16:27:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 22 comments to review
 * Pycodestyle check: succeeded
   * 115 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2554/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-08-07T17:44:58Z)

I've tested normal submissions its works as expected as you can see [here](https://gitlab.cern.ch/crab3/CRABServer/-/commit/deba7861549de92f88a707f1aad3af10b5b2dd8b).

Will proceeding to test resubmitting -> deploy on preprod -> test it again ->  then back to you for final review, merge and release to put both MINIAOD locking & TW talks to CRIC back to canary.

## Comment (belforte, 2025-08-07T20:41:44Z)

thanks @sinonkt , I really appreciate how quickly you got the hang of this code and found your way around it. It looks to me that it will work. But surely more tests is much better.

## Comment (nausikt, 2025-08-11T15:05:50Z)

#9147 Sure Stefano!, Thanks for your kind encouragement, could you please re-review when you most convenience please?

## Comment (belforte, 2025-08-11T15:13:30Z)

please address the comments, then I will review again.

## Comment (cmsdmwmbot, 2025-08-11T16:01:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 21 comments to review
 * Pycodestyle check: succeeded
   * 114 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2555/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-11T16:04:13Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 21 comments to review
 * Pycodestyle check: succeeded
   * 112 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2556/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-08-11T16:27:42Z)

Thank you! please get some rest!
