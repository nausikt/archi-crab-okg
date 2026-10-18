# dmwm/CRABServer pull request #8936: remove "if useHtcV2". Always use V2. Fix #8935

State: closed
Opened: 2025-02-18T17:22:28Z
Closed: 2025-02-20T12:05:48Z
Merged: 2025-02-20T12:05:48Z
URL: https://github.com/dmwm/CRABServer/pull/8936

## Opening post (belforte, 2025-02-18T17:22:28Z)

(no text)

## Comment (cmsdmwmbot, 2025-02-18T17:28:44Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 46 warnings and errors that must be fixed
   * 195 comments to review
 * Pycodestyle check: succeeded
   * 777 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2378/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-02-18T17:42:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 195 comments to review
 * Pycodestyle check: succeeded
   * 777 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2379/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-02-18T18:08:48Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 195 comments to review
 * Pycodestyle check: succeeded
   * 777 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2380/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-02-19T09:09:36Z)

fixing the last pylint complain requires rewriting logic inside PostJob. Too much danger and too much work. Simply bad coding practice but current code is safe.

validation pipeline: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/10465098 **OK**

## Comment (belforte, 2025-02-20T12:05:41Z)

thanks @sinonkt for having found the time to look at this.
