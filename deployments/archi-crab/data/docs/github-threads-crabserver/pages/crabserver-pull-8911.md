# dmwm/CRABServer pull request #8911: Protect CheckTapeRecall for rules by transfer_ops

State: closed
Opened: 2025-02-03T17:21:50Z
Closed: 2025-02-03T19:11:21Z
Merged: 2025-02-03T19:11:21Z
URL: https://github.com/dmwm/CRABServer/pull/8911

## Opening post (belforte, 2025-02-03T17:21:50Z)

(no text)

## Comment (cmsdmwmbot, 2025-02-03T17:26:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 25 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2368/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-02-03T17:27:53Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 25 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2369/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-02-03T17:32:46Z)

@aspiringmind-code this fixes current problem (tested), once merged we need to create a new container to use. I leave that to you and @sinonkt . Hopefully instructions in https://cmscrab.docs.cern.ch/crab-components/crab-monitoring/crab-crontabs.html works. If not, please fix them.
