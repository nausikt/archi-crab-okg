# dmwm/CRABServer pull request #9199: fix #9197

State: closed
Opened: 2025-10-01T16:07:39Z
Closed: 2025-10-02T07:02:39Z
Merged: 2025-10-02T07:02:39Z
URL: https://github.com/dmwm/CRABServer/pull/9199

## Opening post (belforte, 2025-10-01T16:07:39Z)

add back collector and list of schedds from external config

## Comment (cmsdmwmbot, 2025-10-01T16:12:50Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 warnings
   * 6 comments to review
 * Pycodestyle check: succeeded
   * 12 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2647/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-10-01T19:19:31Z)

I verified that this works on test2 when removing the line
```
config.Debug.scheddName = 'crab3@vocms059.cern.ch'
```
from crabConfig.py

Please review, then we can build a new tag and put in preprod again.

## Comment (belforte, 2025-10-02T07:02:36Z)

thanks for quick review !
