# dmwm/CRABServer pull request #9159: use BEARER_TOKEN if available on AP. Fix #9140

State: closed
Opened: 2025-08-20T13:16:17Z
Closed: 2025-08-22T18:11:32Z
Merged: 2025-08-22T18:11:31Z
URL: https://github.com/dmwm/CRABServer/pull/9159

## Opening post (belforte, 2025-08-20T13:16:17Z)

(no text)

## Comment (cmsdmwmbot, 2025-08-20T13:19:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 112 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2576/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-21T11:29:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 112 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2577/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-21T18:43:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 112 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2578/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-21T18:50:20Z)

Thanks @aspiringmind-code 
I have added code to only enable token use in the job if CMSSW version and Site are "OK". I would like you to review again and especially look at how I handled the list of good sited and think whether there could be a better way in view of this being expanded and possibly end up in a short black list instead.
But hopefully still transient so we do not want to replicate the work done in TW for user-specified B/W lists with wildchar expansion and all those bells and whistles.

I have given a thought about a white list in the TaskWorkerConfig.py, but that already seems too much work. Maybe  I simply got lazy ?

## Comment (belforte, 2025-08-21T18:53:08Z)

Anyhow I tested this by submitting to CERN or to US and it behave as expected, Did not use token at CERN (and worked), used token at FLorida, WIsconsin and Nebraska (and worked).

## Comment (cmsdmwmbot, 2025-08-22T09:01:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 112 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2579/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-22T09:30:25Z)

please have a final look, eventually I will squash commits before merging. anyhow will give it another round of testing

## Comment (cmsdmwmbot, 2025-08-22T09:32:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 112 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2580/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-22T13:53:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 112 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2581/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-22T17:05:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 112 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2582/artifact/artifacts/PullRequestReport.html
