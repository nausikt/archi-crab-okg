# dmwm/CRABServer pull request #9155: always report truncated files. Fix #9154

State: closed
Opened: 2025-08-18T21:02:51Z
Closed: 2025-08-18T21:42:43Z
Merged: 2025-08-18T21:42:43Z
URL: https://github.com/dmwm/CRABServer/pull/9155

## Opening post (belforte, 2025-08-18T21:02:51Z)

(no text)

## Comment (cmsdmwmbot, 2025-08-18T21:05:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 7 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2568/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-18T21:31:21Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 8 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2569/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-18T21:42:38Z)

this is pretty safe since it is called inside `try..except..pass`. Let's put it in and see if it works
