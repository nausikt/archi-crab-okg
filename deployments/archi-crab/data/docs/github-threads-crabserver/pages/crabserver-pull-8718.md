# dmwm/CRABServer pull request #8718: Remove extra files from TW tarballs

State: closed
Opened: 2024-09-25T16:26:30Z
Closed: 2024-09-30T13:02:30Z
Merged: 2024-09-30T13:02:30Z
URL: https://github.com/dmwm/CRABServer/pull/8718

## Opening post (belforte, 2024-09-25T16:26:30Z)

initial step to simplify TW tarballs handling as per #8699

## Comment (cmsdmwmbot, 2024-09-25T16:31:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 36 warnings and errors that must be fixed
   * 1 warnings
   * 403 comments to review
 * Pycodestyle check: succeeded
   * 580 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2178/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-25T16:35:34Z)

about pylint: all the errors come from `cmscp.py`. I am not going to touch it until/unless we have a need to change or decide to rewrite !!
