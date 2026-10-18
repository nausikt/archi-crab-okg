# dmwm/CRABServer pull request #8275: Fix bug from PR#8254

State: closed
Opened: 2024-03-11T21:12:28Z
Closed: 2024-03-12T10:04:35Z
Merged: 2024-03-12T10:04:35Z
URL: https://github.com/dmwm/CRABServer/pull/8275

## Opening post (novicecpp, 2024-03-11T21:12:28Z)

1. Fix typo bug from file name changes.
2. Use PYTHONPATH directly instead of APP_PATH because it will break path when assign as prefix of COMMAND_DIR in [manage.sh#L20](https://github.com/dmwm/CRABServer/blob/22cb74aaf1f15d4d6eafd7701d06d9e71b9c8430/cicd/crabtaskworker_pypi/manage.sh#L20) in `./start.sh -g` mode.
3. Apply `set -euo pipefail` to all process control scripts to make it more robust.

## Comment (cmsdmwmbot, 2024-03-11T21:15:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1889/artifact/artifacts/PullRequestReport.html
