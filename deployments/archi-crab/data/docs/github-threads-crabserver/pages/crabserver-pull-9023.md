# dmwm/CRABServer pull request #9023: add logging of slaves queue. Fix #9022

State: closed
Opened: 2025-03-31T09:02:57Z
Closed: 2025-04-01T07:26:56Z
Merged: 2025-04-01T07:26:56Z
Labels: Status: On Hold
URL: https://github.com/dmwm/CRABServer/pull/9023

## Opening post (belforte, 2025-03-31T09:02:57Z)

these are changes that I have been using in my [branch](https://github.com/belforte/CRABServer/tree/add-diagnostic-to-Worker), and which are running currently in canary.
In that branch I have also modified code so that `./start.sh -d` option runs only MasterWorker in debug mode, while keeping the subprocesses pool for the slaves, but adding another option for that seems too much complexity which we may never use, so have left it out and that's why I am not merging that branch.

I think the additional logging is good to have anyhow and allows us to progress with new code like the [add info to TaskTable](https://github.com/dmwm/CRABServer/tree/addInfoToTasks-03-25).

All in all since the problem in #9014 is not easily reproducible, we may want to  move to new code anyhow and simply investigate when it happens.

## Comment (cmsdmwmbot, 2025-03-31T09:06:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 3 warnings
   * 89 comments to review
 * Pycodestyle check: succeeded
   * 121 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2414/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-03-31T09:45:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 84 comments to review
 * Pycodestyle check: succeeded
   * 121 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2415/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-31T12:55:27Z)

let's sit on this a bit, I may need to add logging see https://github.com/dmwm/CRABServer/issues/9014#issuecomment-2766069719

## Comment (belforte, 2025-04-01T07:26:44Z)

logging is sufficient
