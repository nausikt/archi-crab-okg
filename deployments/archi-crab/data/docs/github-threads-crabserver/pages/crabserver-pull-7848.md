# dmwm/CRABServer pull request #7848: Merge rucio_transfers to master

State: closed
Opened: 2023-08-22T15:18:44Z
Closed: 2023-08-24T12:55:38Z
Merged: 2023-08-24T12:55:38Z
URL: https://github.com/dmwm/CRABServer/pull/7848

## Opening post (novicecpp, 2023-08-22T15:18:44Z)

Merge `RUCIO_Transfers.py` to master.

Mostly add new files and replace Old Rucio ASO script with new one. [cmscp.py](https://github.com/dmwm/CRABServer/pull/7848/files#diff-0a2fdf079163a75156e42d7abc277ec76284debc5322fb6c2de68179350253c2) and [PostJob.py](https://github.com/dmwm/CRABServer/pull/7848/files#diff-a4cebbe1c32aa0a7d5b56a221d1ba9c0df06347759aab86886ac14f5c82cb3d6) have small changes in it that pretty safe to push on production.

## Comment (cmsdmwmbot, 2023-08-22T15:22:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 199 warnings and errors that must be fixed
   * 54 warnings
   * 902 comments to review
 * Pycodestyle check: succeeded
   * 1440 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1660/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-22T15:40:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 199 warnings and errors that must be fixed
   * 54 warnings
   * 902 comments to review
 * Pycodestyle check: succeeded
   * 1440 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1661/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-22T17:03:01Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 157 warnings and errors that must be fixed
   * 39 warnings
   * 791 comments to review
 * Pycodestyle check: succeeded
   * 1398 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1663/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-23T15:13:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 149 warnings and errors that must be fixed
   * 38 warnings
   * 768 comments to review
 * Pycodestyle check: succeeded
   * 1397 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1670/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-08-24T12:45:20Z)

@belforte I am squash merging this to master and release the new tag. Feel free to revert it anytime if you find any serious issue.
