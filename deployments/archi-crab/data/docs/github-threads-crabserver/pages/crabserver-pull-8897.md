# dmwm/CRABServer pull request #8897: handle task kill in wrong state as 400 BadRequest instead of 500.

State: closed
Opened: 2025-01-29T03:53:09Z
Closed: 2025-01-29T15:38:50Z
Merged: 2025-01-29T15:38:50Z
URL: https://github.com/dmwm/CRABServer/pull/8897

## Opening post (nausikt, 2025-01-29T03:53:09Z)

Fixes #8878

## Comment (cmsdmwmbot, 2025-01-29T03:56:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 warnings
   * 48 comments to review
 * Pycodestyle check: succeeded
   * 311 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2352/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-29T04:26:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 47 comments to review
 * Pycodestyle check: succeeded
   * 309 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2353/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-29T08:05:06Z)

Thanks @sinonkt .
I would rather use a more generic exception, not introduce a new one ev, iery time we find a non-allowed operation. Please change the new exception name a bit .

There are other cases were current code returns HTTP 500 but a kinder exception would be better,  like asking for status of a non-existing task.

Then we should look into handing HTTP 400 in the client !

## Comment (belforte, 2025-01-29T20:32:03Z)

sorry @sinonkt I could not tell from the list of changes, are lines like this preserved ?
```
Server answered with: You cannot kill a task if it is in the SUBMITFAILED status
```
