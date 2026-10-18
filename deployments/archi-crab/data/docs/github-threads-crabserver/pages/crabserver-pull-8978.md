# dmwm/CRABServer pull request #8978: Add columns to task db 8973

State: closed
Opened: 2025-03-11T23:16:28Z
Closed: 2025-03-12T21:14:00Z
URL: https://github.com/dmwm/CRABServer/pull/8978

## Opening post (belforte, 2025-03-11T23:16:28Z)

see https://github.com/dmwm/CRABServer/issues/8973#issuecomment-2715918092

this adds a new subresource to task API to edit one column table for one task

also adds visualisation of numJobs and DAGstatus in MAIN tab of crabserver UI

## Comment (cmsdmwmbot, 2025-03-11T23:19:02Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 37 comments to review
 * Pycodestyle check: succeeded
   * 219 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2398/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-11T23:19:23Z)

@aspiringmind-code at this point I am not interested as much in a code review (feel free though) as to your opinion on adding such a wide-scope, error-prone API which breaks with CRAB original idea to have one API for each action with very precise validation.
OTOH this is likely more similar to what many applications  do, you get an ORA-xxx error if you try to do something wrong, and then it is for you to figure out.

## Comment (belforte, 2025-03-11T23:20:48Z)

the new REST code is currently running on cmsweb-test2. I did some testing making calls from python shell

## Comment (belforte, 2025-03-12T21:14:00Z)

further work on this moved to https://github.com/dmwm/CRABServer/tree/addInfoToTasks-03-25
