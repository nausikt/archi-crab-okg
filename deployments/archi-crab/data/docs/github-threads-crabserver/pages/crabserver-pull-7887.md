# dmwm/CRABServer pull request #7887: Process corruption reports fix 7883

State: closed
Opened: 2023-09-18T20:51:23Z
Closed: 2023-09-21T14:07:29Z
Merged: 2023-09-21T14:07:29Z
URL: https://github.com/dmwm/CRABServer/pull/7887

## Opening post (belforte, 2023-09-18T20:51:23Z)

initial implementation.
No calls to Rucio. Only daily totals are collected. Waiting to see how it goes.

## Comment (cmsdmwmbot, 2023-09-18T20:57:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 6 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1705/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-18T21:07:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 6 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1706/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-18T21:09:50Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1707/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-09-18T21:16:45Z)

@mapellidario @novicecpp this is a standalone script which I will initially run by hand, so does not need reviewing in a way, but since it looks to me already too long and intricated for the task, feel free to suggest a different design before it grows more.

Of course there's still the chance that in the end we get just a handful of corrupted files a month, so this will all sort of evaporate.

## Comment (belforte, 2023-09-19T16:28:23Z)

>  I am OK if it for POC (and we need to run on production). But for the long term we should move to ES.

I see. Ambitious (esp. for my skill level) but surely nice. Let's wait to see how many times this happens !

## Comment (cmsdmwmbot, 2023-09-19T17:25:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 8 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 75 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1708/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-20T21:35:11Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 8 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 74 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1709/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-20T21:35:35Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 8 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 74 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1710/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-20T21:51:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 8 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 74 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1711/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-09-20T21:53:56Z)

@novicecpp I found that some change I had made had broken the reporting of corrupted files. On the good side we have some proof that if new code which checks for corruption fails (an undef variable here), things still work.
So unless you have further comments, we can put this next release and see how it goes.
