# dmwm/CRABServer pull request #9291: Use python3 for wmc httpd

State: closed
Opened: 2026-04-07T13:35:33Z
Closed: 2026-04-07T14:01:13Z
Merged: 2026-04-07T14:01:13Z
URL: https://github.com/dmwm/CRABServer/pull/9291

## Opening post (belforte, 2026-04-07T13:35:33Z)

one instance was missing, making `./status.sh` fail inside crabserver pod

## Comment (belforte, 2026-04-07T13:36:13Z)

ouch ! looks like I need a proper rebase.

## Comment (cmsdmwmbot, 2026-04-07T13:38:54Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2779/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-07T13:39:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2780/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-04-07T14:01:09Z)

rebased. tested, and trivial enough that I am merging,  FYI @nausikt
