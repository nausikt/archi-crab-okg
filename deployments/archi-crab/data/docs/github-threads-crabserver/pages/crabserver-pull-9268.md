# dmwm/CRABServer pull request #9268: Fix python2/3 compatibility for Status Tracking with different CMSSW versions

State: closed
Opened: 2026-01-26T15:46:15Z
Closed: 2026-01-26T16:28:36Z
Merged: 2026-01-26T16:28:36Z
URL: https://github.com/dmwm/CRABServer/pull/9268

## Opening post (aspiringmind-code, 2026-01-26T15:46:15Z)

Choose python3 or python2 depending on the CMSSW version and remove fstrings that only work with python3

## Comment (aspiringmind-code, 2026-01-26T15:47:37Z)

Fix #9213 
See [Pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13880174)

## Comment (cmsdmwmbot, 2026-01-26T15:48:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 13 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2725/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-01-26T16:09:45Z)

Code looks OK, even if as usual you bash is way too advanced for me (you can compare with
the poor-man way which I used in CRABClient/bin/crab !)

This solution differs from what I (possibly wrongly) stated in #9213, i.e. that problem was using EL7 CMSSW release in an EL9 container. I presume that you tested the fix an it works, so it would be good to state in the issue what exactly the problem was instead and what is the eventual solution, which IIUC is to use for StatusTracking.py the same CMSSW release which was used for submission and hence make it py2/3 compatible as we did for CRABClient.
If that's the case, please put a comment at the top of the script to remind us that we need to be py2 compatible is we ever want to do changes. And of the fact that not all crab commands work in e.g. CMSSW_7 (SL6). 

If you have a test pipeline which ran with the change (successfully ?), please point to it.

## Comment (belforte, 2026-01-26T16:10:29Z)

Anyhow I approved since the changes look good to me.

## Comment (aspiringmind-code, 2026-01-26T16:21:42Z)

Thanks for the review. Yes, you are right. I will add a comment on top of the script.

## Comment (cmsdmwmbot, 2026-01-26T16:28:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2726/artifact/artifacts/PullRequestReport.html
