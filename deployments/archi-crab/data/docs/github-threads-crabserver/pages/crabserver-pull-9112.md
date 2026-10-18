# dmwm/CRABServer pull request #9112: Fix in out metdata handling for asorucio

State: closed
Opened: 2025-06-16T12:53:51Z
Closed: 2025-06-16T14:52:26Z
Merged: 2025-06-16T14:52:26Z
URL: https://github.com/dmwm/CRABServer/pull/9112

## Opening post (belforte, 2025-06-16T12:53:51Z)

fix #9094
this PR does:

*   always upload input metadata before handing control to ASO
*   introduce self.useAsoRucio and when true
    * upload output metadata  right after triggering ASO work (in first PJ iteration)
    *  do not and set publish flag to True in PostJob
*   keep the PJ running also for ASO-Rucio so that job status is reported the same way as it is now.
*  in ASO/Rucio/Actions/MonitorLockStatus/updateREESTFileDocsBlockCompletionInfo also set  publish flag to True 
*   no changes to Publisher

there are also minor changes for `pylint`

## Comment (cmsdmwmbot, 2025-06-16T12:57:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 319 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2503/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-16T14:42:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 319 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2505/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-16T14:50:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 319 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2506/artifact/artifacts/PullRequestReport.html
