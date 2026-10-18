# dmwm/CRABServer pull request #7587: RUCIO_Transfer refactoring: Boostrap refactoring and add building task's dataset

State: closed
Opened: 2023-04-12T13:22:50Z
Closed: 2023-05-12T13:46:51Z
Merged: 2023-05-12T13:46:51Z
URL: https://github.com/dmwm/CRABServer/pull/7587

## Opening post (novicecpp, 2023-04-12T13:22:50Z)

First PR of `RUCIO_Transfers.py` refactoring. 

- I have created new branch [rucio\_transfers\_refactoring\_origin](https://github.com/dmwm/CRABServer/tree/rucio_transfers_refactoring_origin), based on commit `a4209967` a week ago, to merge refactoring PR against it.
- Change `RUCIO_Transfers.py`  to simple entrypoint to `main()` in `src/python/ASO/Rucio/Main.py`
  - Move all code to OldRucioTransfer.py, for dev (me) to pair with the new code.
- Processing start at `RunTransfer.algorithm()`
- `main()` of  `RUCIO_Transfers.py`  split into 3 parts of Actions class.
  - `BuildTaskDataset` to build containter and dataset.
  - `RegisterReplicas` to add file replicas to dataset.
  - `MonitoringReplicas` to update status to database.
- I use [pytest](https://docs.pytest.org/en/7.2.x/) to write unit test and run test.
  - Quick docs how to run the test: https://cmscrab.docs.cern.ch/technical/crab-testing.html
  - Code still complex, duplicate, and hard to read. Still have no idea how to improve it.
  - Skip unit test in `Main.py` and `RunTransfer.py` because I have no idea how to test it.
  - In the next step of test, I will write integration/end-to-end test that interact with real server.

@belforte Please review.
@mapellidario Please, if you have any suggestion, feel free to comment. I am glad to hear it. 

EDITED: Note that I never test current code by running it manually. I will do it when start writing integration/end-to-end test.

## Comment (cmsdmwmbot, 2023-04-12T13:25:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1485/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-12T21:08:31Z)

It will take some time to review ! I had a quick look and my initial reaction is a concern that there are too many layers around the algorithm. Makes it difficult to understand what's going on. Are they really needed ? Of course if is possible that I simply got lost and will know better after I have spent some hours on this.

## Comment (novicecpp, 2023-04-13T12:01:44Z)

> my initial reaction is a concern that there are too many layers around the algorithm.

It is good to have separate classes/functions to separate concerns and focus on one thing at a time when we develop.

## Comment (novicecpp, 2023-04-13T12:03:37Z)

The new RUCIO_Transfer have 4 components:
- Main (`Main.py`, `RunTransfer.py`), to initialize everything we need.
- Transfer object (`Transfer.py`) replace `globs` class and pass to action class. It also response for read info from disk.
- Actions (`BulildTaskDataset.py` and more) to define what to do.
- And Utility files (`exception.py`, `config.py`)

## Comment (belforte, 2023-04-27T16:40:45Z)

@novicecpp I am not sure what we should do here. We reviewed and it looks good, but if we merge it will break current RUCIO_Transfers.py. Do you like to keep it open ? SHould I approve ?

## Comment (novicecpp, 2023-04-28T06:46:06Z)

Let's me push changes we agreed and then you can approve this PR. Maybe end of today or next Monday.
Anyway, I opened it against  new branch which based on master a month ago. So, it safe to merge.

## Comment (belforte, 2023-04-28T07:12:59Z)

in order to merge we must make sure not to override RUCIO_Transfers.py, not until new version is ready.

## Comment (cmsdmwmbot, 2023-05-02T06:59:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1510/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-05-02T07:24:13Z)

@belforte sorry for take it so long. PR is now ready to review.

Here are the changes list compare to previous comment ([see diff](https://github.com/novicecpp/CRABServer/compare/0082a15ef8e8fedfe844ac8344697506350daf85...novicecpp:CRABServer:9f95639b06ae7f7ca91dcd5da99989c7b2c9d61f)):
- Change `config.config` to `config.args` and add ref on how does it work.
- Remove `RucioTransferMain` class and move code to `main()` function.
- Replication rule at container level.
- Rename `BuildTaskDataset` to `BuildDBSDataset`.
- Add more method in `Transfer.py` object to read bookkeeping data from files.

Please ignore `test_BuildDBSDataset.py` for now, only rename from `test_BuildTaskDataset.py` to `test_BuildDBSDataset.py` without fixing code.

I need to override `RUCIO_Transfers.py` to test this PR in my local machine. So, I have created new branch in `dmwm/CRABServer` [rucio\_transfers\_refactoring\_origin](https://github.com/dmwm/CRABServer/tree/rucio_transfers_refactoring_origin) and open this PR against it. I will not merge to `master` until new version is ready.

## Comment (belforte, 2023-05-12T13:32:30Z)

Wa and myself reviewed together and looks very neat now. Thanks

## Comment (cmsdmwmbot, 2023-05-12T13:42:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1516/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-05-12T13:43:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1517/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-05-12T13:47:02Z)

Thanks Stefano.
