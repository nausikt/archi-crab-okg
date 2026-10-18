# dmwm/CRABServer pull request #7649: RUCIO_Transfers.py: Add RegisterReplicas action and separate transfer container from publish container.

State: closed
Opened: 2023-05-30T12:42:30Z
Closed: 2023-06-19T08:14:36Z
Merged: 2023-06-19T08:14:36Z
URL: https://github.com/dmwm/CRABServer/pull/7649

## Opening post (novicecpp, 2023-05-30T12:42:30Z)

This PR replaces https://github.com/dmwm/CRABServer/pull/7637, which introduces a major change besides new `RegisterReplicas` action, separating the published and transfer containers.

I use the `outputdataset` field from `transfers.txt` as publish container name. Then, modify `outputdataset` to `/PrimaryDataset/DatasetName_TRANSFER.{MD5OfTaskName[:8]}/USER` and use it as a transfer container name.

For example, given `/GenericTTbar/tseethon-integrationtest-12/USER` a  publish container name, we will get `/GenericTTbar/tseethon-integrationtest-12_TRANSFER.3b1e780f/USER` as a transfer container name.

I also split `RegisterReplicas.register()` into two methods, `addFileToRucio()` to register files to Rucio, and `addReplicasToContainer()` to add newly registered replicas to datasets in the transfer container to let Rucio do transfers. It will be reuse in `MonitorLockStatus` action class later to register transfer completed replicas.

## Comment (cmsdmwmbot, 2023-05-30T12:45:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1532/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-06T06:56:36Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1534/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-06T12:55:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1535/artifact/artifacts/PullRequestReport.html
