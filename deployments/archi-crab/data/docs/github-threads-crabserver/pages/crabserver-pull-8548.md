# dmwm/CRABServer pull request #8548: Limiting Tape recall days to now+4 days

State: closed
Opened: 2024-07-05T15:40:16Z
Closed: 2024-07-11T10:47:40Z
Merged: 2024-07-11T10:47:40Z
URL: https://github.com/dmwm/CRABServer/pull/8548

## Opening post (aspiringmind-code, 2024-07-05T15:40:16Z)

See Issue https://github.com/dmwm/CRABServer/issues/8546

## Comment (cmsdmwmbot, 2024-07-05T15:43:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 5 warnings
 * Pycodestyle check: succeeded
   * 2 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2044/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-06T17:28:42Z)

Hi @aspiringmind-code 
are you sure that `lifetime` argument can be an absolute time from epoch like in your `time.time()+4days` ? Just from "the surface" it is not consistent with previous `lifetime=32days`

the goal of assigning this to you is to give you an entry point to look at Rucio. Before we wrap it up I want to be sure that you understand what this piece of code is doing, why we change, what a replication rule does etc.

Also please fix pylint "warnings and errors that must be fixed"

## Comment (cmsdmwmbot, 2024-07-10T11:52:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 5 warnings
 * Pycodestyle check: succeeded
   * 2 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2050/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-07-10T11:54:04Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 5 warnings
 * Pycodestyle check: succeeded
   * 2 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2051/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-10T13:28:20Z)

please fix the pylint error (unused import)

## Comment (cmsdmwmbot, 2024-07-11T07:45:39Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 warnings
 * Pycodestyle check: succeeded
   * 2 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2052/artifact/artifacts/PullRequestReport.html
