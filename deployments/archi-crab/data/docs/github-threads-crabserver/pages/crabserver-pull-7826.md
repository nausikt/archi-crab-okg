# dmwm/CRABServer pull request #7826: Publisher for aso via rucio fix #7770

State: closed
Opened: 2023-08-14T12:43:15Z
Closed: 2023-08-17T14:09:25Z
Merged: 2023-08-17T14:09:25Z
URL: https://github.com/dmwm/CRABServer/pull/7826

## Opening post (belforte, 2023-08-14T12:43:15Z)

Even if things are not final, I am merging into master to facilitate testing.
This only ADDS things, so it is totally harmless:
* Publisher/PublisherMasterRucio.py
* Publisher/TaskPublishRucio.py
* new method `getCrabserver` in `TaskWorker/WorkerUtilities.py`

Still requires manual work to start the Publisher_rucio, but that can come via further PR's

## Comment (cmsdmwmbot, 2023-08-14T12:49:51Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 24 warnings and errors that must be fixed
   * 5 warnings
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 46 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1651/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-17T13:50:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 21 warnings and errors that must be fixed
   * 4 warnings
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 46 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1654/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-17T14:06:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 4 warnings
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 46 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1655/artifact/artifacts/PullRequestReport.html
