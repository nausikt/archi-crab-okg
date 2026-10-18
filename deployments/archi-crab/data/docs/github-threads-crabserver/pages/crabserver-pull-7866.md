# dmwm/CRABServer pull request #7866: RUCIO_Transfers: Mark file as fail to transfer when add_replicas raise exception

State: closed
Opened: 2023-09-07T14:19:03Z
Closed: 2023-09-11T11:30:04Z
Merged: 2023-09-11T11:30:04Z
URL: https://github.com/dmwm/CRABServer/pull/7866

## Opening post (novicecpp, 2023-09-07T14:19:03Z)

Fix https://github.com/dmwm/CRABServer/issues/7865

Mark failed to transfer to FiletransferDB and let PostJob trigger the retry. It is safe because the file does not have DID in rucio yet.

## Comment (cmsdmwmbot, 2023-09-07T14:25:35Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 15 warnings and errors that must be fixed
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 32 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1688/artifact/artifacts/PullRequestReport.html
