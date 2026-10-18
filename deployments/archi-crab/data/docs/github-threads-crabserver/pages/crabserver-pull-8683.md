# dmwm/CRABServer pull request #8683: Enable install WMCore from private repository

State: closed
Opened: 2024-09-03T15:16:32Z
Closed: 2024-09-04T19:14:52Z
Merged: 2024-09-04T19:14:52Z
URL: https://github.com/dmwm/CRABServer/pull/8683

## Opening post (novicecpp, 2024-09-03T15:16:32Z)

Fix https://github.com/dmwm/CRABServer/issues/8582

In summary, put the conditional check into a new `installWMCore.sh` script. 
If repository specify in [wmcore_requirements.txt](https://github.com/dmwm/CRABServer/blob/f5687adbf5fddeb21526c33b623b2f5025e17945/cicd/crabserver_pypi/wmcore_requirements.txt) is `dmwm/WMCore`, always install wmcore from PyPI packages. 
Otherwise, clone it and copy whole `src/python` to install directory.

## Comment (cmsdmwmbot, 2024-09-03T15:18:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2157/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-03T20:07:28Z)

Looks very cool and quite likely my doubts only come from ignorance, so I beg you to describe things a little more. Instructions for different ways of installing could e.g. be part of the initial comments in `/wmcore_requirements.txt`. But let's not have the description of this PR as documentation !

## Comment (cmsdmwmbot, 2024-09-04T18:57:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2164/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-04T19:14:11Z)

very good, thanks !

## Comment (novicecpp, 2024-09-04T19:14:43Z)

Thanks!
