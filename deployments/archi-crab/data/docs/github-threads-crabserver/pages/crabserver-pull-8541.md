# dmwm/CRABServer pull request #8541: Use simple py script as the entrypoint of TW process

State: closed
Opened: 2024-07-04T10:41:29Z
Closed: 2024-07-09T10:43:30Z
Merged: 2024-07-09T10:43:30Z
URL: https://github.com/dmwm/CRABServer/pull/8541

## Opening post (novicecpp, 2024-07-04T10:41:29Z)

Fix https://github.com/dmwm/CRABServer/issues/8540

This PR introduce `crab-taskworker` file to act as binary of TW process, so when you run `./start.sh -g`, python will read `MasterWorker.py` from GH instead of installation path.

The PR also deprecates the `SequentialWorker.py` and replaces it with the new option `--pdb`, running sequential mode the same way `SequentialWorker.py` does.

## Comment (cmsdmwmbot, 2024-07-04T10:46:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 5 warnings
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 66 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2042/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-07-09T10:42:10Z)

Thanks Stefano. Merging...
