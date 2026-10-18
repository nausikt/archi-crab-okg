# dmwm/CRABServer pull request #7897: Fix PreDAG.py to always use user proxy for rucio client

State: closed
Opened: 2023-10-06T13:27:09Z
Closed: 2023-10-06T14:04:08Z
Merged: 2023-10-06T14:04:08Z
URL: https://github.com/dmwm/CRABServer/pull/7897

## Opening post (novicecpp, 2023-10-06T13:27:09Z)

Relate to https://github.com/dmwm/CRABServer/issues/7894

This PR fixes the bug when we alter TW config to use user cert here: https://github.com/dmwm/CRABServer/blob/412bd3a45c19d65a411d528dd9b96efaef16b1b4/src/python/TaskWorker/Actions/PreDAG.py#L204-L208
But, it gets override by `config.Services.Rucio_cert` in `TaskWorkerConfig.py` file in here:
https://github.com/dmwm/CRABServer/blob/412bd3a45c19d65a411d528dd9b96efaef16b1b4/src/python/RucioUtils.py#L27

## Comment (cmsdmwmbot, 2023-10-06T13:30:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 4 warnings
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 25 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1715/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-06T14:30:10Z)

not for now, but the change that you need to to to RucioUtils makes me think that we may not have found the correct way to organize those configuration params. Could go together with the attempt I did (for publisher_rucio so far) to separate also the REST parameters.
