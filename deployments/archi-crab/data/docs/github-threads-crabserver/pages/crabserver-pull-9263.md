# dmwm/CRABServer pull request #9263: drop GIT_SSL_CAINFO, GIT_EXEC_PATH to use system git instead.

State: closed
Opened: 2026-01-19T09:15:26Z
Closed: 2026-01-19T11:25:11Z
Merged: 2026-01-19T11:25:11Z
URL: https://github.com/dmwm/CRABServer/pull/9263

## Opening post (nausikt, 2026-01-19T09:15:26Z)

Resolve #9262 

This will make release pipeline back in order for the next release, As i tested [here](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13795570).
P.S. *I atomically dropped obsolete git-related envs for just git clone cmd this way to minimize adverse effects.*

## Comment (cmsdmwmbot, 2026-01-19T09:19:41Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2719/artifact/artifacts/PullRequestReport.html
