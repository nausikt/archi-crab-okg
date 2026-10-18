# dmwm/CRABServer pull request #8557: add CRABUtils/TaskUtils.py

State: closed
Opened: 2024-07-24T09:18:27Z
Closed: 2024-07-24T12:20:01Z
Merged: 2024-07-24T12:20:01Z
URL: https://github.com/dmwm/CRABServer/pull/8557

## Opening post (belforte, 2024-07-24T09:18:27Z)

a step toward #7671 and #7765

At this time I am not changing existing code to use these instead. Leaving it to @aspiringmind-code as he completes #7671

## Comment (cmsdmwmbot, 2024-07-24T09:25:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2057/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-07-24T09:25:39Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2058/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-07-24T09:33:16Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2059/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-24T10:15:50Z)

pfff..  `CRABServer/src/python/Utils` clashes with `WMCore/src/python/Utils` since we put in the PYTHONPATH both ` `CRABServer/src/python` and `WMCore/src/python`

Shall we rename the directory to  `CRABServer/src/python/CRABUtils` ?
@novicecpp @aspiringmind-code @mapellidario  what do you think ?

## Comment (cmsdmwmbot, 2024-07-24T11:15:17Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2060/artifact/artifacts/PullRequestReport.html
