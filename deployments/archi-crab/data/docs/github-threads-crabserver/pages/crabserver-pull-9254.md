# dmwm/CRABServer pull request #9254: bumped to WMCore 2.4.5.2 (wmfreeze), a py3.12 compliant version, synced its necessary deps.

State: closed
Opened: 2025-12-19T15:09:45Z
Closed: 2026-03-03T16:33:52Z
URL: https://github.com/dmwm/CRABServer/pull/9254

## Opening post (nausikt, 2025-12-19T15:09:45Z)

Resolve #9150

This PR make container buildable on py3.12 env. As we can see the succeed in lifting to py3.12 env, also put container into thoroughly tests in Draft PR #9251
*P.S. This PR was cherry-picked(s) of relevant commits from #9251*

## Comment (cmsdmwmbot, 2025-12-19T15:13:27Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2711/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-01-16T17:14:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2718/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-03-03T16:33:52Z)

I will close this PR, since it was cherry-picked into https://github.com/dmwm/CRABServer/pull/9265.
