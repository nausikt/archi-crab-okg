# dmwm/CRABServer pull request #8800: Add variables to pipeline for flexibility

State: closed
Opened: 2024-11-18T16:56:56Z
Closed: 2024-11-19T09:52:44Z
Merged: 2024-11-19T09:52:44Z
URL: https://github.com/dmwm/CRABServer/pull/8800

## Opening post (aspiringmind-code, 2024-11-18T16:56:56Z)

We add variables like SKIP_BUILD, SKIP_DEPLOY and SKIP_SUBMIT in respective rules to make skipping steps flexible. 
We make use of explicit checks
And add a check to ensure file exists to avoid failure in statusTracking.py

## Comment (cmsdmwmbot, 2024-11-18T16:59:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2282/artifact/artifacts/PullRequestReport.html
