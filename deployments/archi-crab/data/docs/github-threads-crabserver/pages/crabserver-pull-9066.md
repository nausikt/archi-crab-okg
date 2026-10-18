# dmwm/CRABServer pull request #9066: add destination to TapeRecall table. Fix #9060

State: closed
Opened: 2025-05-08T08:42:30Z
Closed: 2025-05-08T15:46:06Z
Merged: 2025-05-08T15:46:06Z
URL: https://github.com/dmwm/CRABServer/pull/9066

## Opening post (belforte, 2025-05-08T08:42:30Z)

also fixes pylint warnings

new code is the `findDestForRule()` function

## Comment (belforte, 2025-05-08T08:45:48Z)

tested by running by hand in tw02 as per https://cmscrab.docs.cern.ch/crab-components/crab-monitoring/crab-crontabs.html#run-the-script-interactively-with-debugger 
Then had to edit grafana table to make new column visible.

## Comment (cmsdmwmbot, 2025-05-08T08:46:02Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 25 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2448/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-08T14:46:49Z)

this is all in all tested well enough, and I am eager to see the new column in the prod. dashboard. Merging. Sorry Vijay

## Comment (aspiringmind-code, 2025-05-08T15:02:25Z)

Sorry for the delay...I had taken a preliminary look and all looked good.

## Comment (aspiringmind-code, 2025-05-08T15:05:16Z)

The only question I have is why the timeout was felt necessary?

## Comment (belforte, 2025-05-08T15:45:47Z)

I added the timeout to please pylint :man_shrugging:  I guess it can't harm.
