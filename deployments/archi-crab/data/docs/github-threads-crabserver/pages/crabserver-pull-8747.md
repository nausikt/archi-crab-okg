# dmwm/CRABServer pull request #8747: remove debug_files handling in TW. Do it in scheduler

State: closed
Opened: 2024-10-21T19:22:10Z
Closed: 2024-10-22T07:17:01Z
Merged: 2024-10-22T07:17:01Z
URL: https://github.com/dmwm/CRABServer/pull/8747

## Opening post (belforte, 2024-10-21T19:22:10Z)

this is point 4.5 of https://github.com/dmwm/CRABServer/issues/6544
and completes handling S3 tarballs in the scheduler, w/o using TaskWorker and man in the middle and w/o shipping them using condor `transfer_input_files`

## Comment (cmsdmwmbot, 2024-10-21T19:24:01Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 161 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2214/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-10-21T21:06:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 154 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2215/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-10-21T22:10:02Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 7 comments to review
 * Pycodestyle check: succeeded
   * 149 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2216/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-10-21T22:11:32Z)

remaining pylint comments are in parts of the code which I do not fully understand and better not touch !

## Comment (cmsdmwmbot, 2024-10-21T22:12:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 7 comments to review
 * Pycodestyle check: succeeded
   * 149 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2217/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-10-21T22:14:05Z)

testing in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8363814  **ok**
