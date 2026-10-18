# dmwm/CRABServer pull request #8883: use --jobId argument and input_args.json file for grid jobs

State: closed
Opened: 2025-01-17T12:56:25Z
Closed: 2025-01-20T14:54:55Z
Merged: 2025-01-20T14:54:55Z
URL: https://github.com/dmwm/CRABServer/pull/8883

## Opening post (belforte, 2025-01-17T12:56:25Z)

fix #8869

Code Cleanup still needed after this, time to get rid of things not used since long but left around which only create confusion. But will be better to test those changes separately once this is established to work.

## Comment (cmsdmwmbot, 2025-01-17T12:59:11Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 56 comments to review
 * Pycodestyle check: succeeded
   * 89 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2319/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-17T13:59:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 56 comments to review
 * Pycodestyle check: succeeded
   * 89 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2320/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-20T14:54:46Z)

tested in my sched, works as well as current production, see last coments in #8869
