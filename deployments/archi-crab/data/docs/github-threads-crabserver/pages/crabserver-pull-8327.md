# dmwm/CRABServer pull request #8327: Clean up cmsbot's Rucio storage space

State: closed
Opened: 2024-04-09T16:24:38Z
Closed: 2024-04-12T10:56:23Z
Merged: 2024-04-12T10:56:23Z
URL: https://github.com/dmwm/CRABServer/pull/8327

## Opening post (novicecpp, 2024-04-09T16:24:38Z)

Hardcode username and filter for now, will fix when we migrate to Gitlab-CI later.

Jenkins job config: https://cmssdt.cern.ch/dmwm-jenkins/job/tseethon_Run/configure
Succesfully run: https://cmssdt.cern.ch/dmwm-jenkins/job/tseethon_Run/11/console

## Comment (mapellidario, 2024-04-09T16:27:38Z)

Does it run on your environment if you use "env python3”? I would prefer to make clear that we really don't want to use py2 there :)

## Comment (cmsdmwmbot, 2024-04-09T16:28:25Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 warnings
   * 3 comments to review
 * Pycodestyle check: succeeded
   * 5 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1930/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-09T16:29:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 warnings
   * 3 comments to review
 * Pycodestyle check: succeeded
   * 5 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1931/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-04-09T16:30:13Z)

I confused with this morning issue and look at wrong column on `rucio list-account-usage`,  thought the rucio space is insufficient and tried to fix immediately.
However, it not the case, everything is fine. For 6 months, we use only 60/100GB :-)

Anyhow, it is better to have cleanup and the scripts is ready to use.

## Comment (novicecpp, 2024-04-09T16:31:29Z)

Sorry @mapellidario, I do not understand your question. What does `env python3` do?

## Comment (belforte, 2024-04-09T16:35:28Z)

this will fail on EL9
```
#!/usr/bin/env python
```
there is no `python` there. Of course it does not matter if you start it with `python3 filename.py`. But why the shebang then ?

Maybe this is what Dario meant above...

## Comment (belforte, 2024-04-09T16:42:39Z)

code looks good, but please add a coupe lines saying it in English what it does.
IIUC you remove all rules that are older than 4 days and refer to transfer containers or task containers which are not published in DBS.

At some point we will need to remove also published datasets though !

## Comment (cmsdmwmbot, 2024-04-09T18:39:28Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 1 warnings
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1932/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-04-09T18:44:29Z)

Update:

- Delete rules older than 30 days (after task's lifetime).
    - All testsuite tasks are now gone due to typo (14 -> 4). Sorry.
-  Comments.
- Dry run by default except execute from cleanup.sh script.
- Delete **ALL** rules, both transfer/publish container. [Line 37](https://github.com/dmwm/CRABServer/blob/dc2407fe452c5aa357721e7fc1dd47a2ffe5ac1c/cicd/rucio/cleanup.py#L37) is just failsafe to delete only rules created by CRAB.

## Comment (belforte, 2024-04-10T07:24:37Z)

looks good, I put two minor comments in code.
But I am still confused about the scope. It still looks to me that you only delete rules for transfer containers and not published dataset. There are also rules created by CRAB for final datasets which go to DBS (no `transfer` nor `Fake` in the name), no ?

Last note: why do you say that all test are gone ? Do you mean the rules, or the data ? I may be confused, but I thought we write to T2_CH_CERN which has lazy cleanup, not greedy. So data files will stick around also when rule is gone. Indeed we can consider using `--purge-replicas` (that's the CLI option, I do not have the python arg. at my fingertips).

## Comment (novicecpp, 2024-04-11T12:09:25Z)

> looks good, I put two minor comments in code. But I am still confused about the scope. It still looks to me that you only delete rules for transfer containers and not published dataset. There are also rules created by CRAB for final datasets which go to DBS (no `transfer` nor `Fake` in the name), no ?

There are 2 (or more) rules per tasks like you said. However, the second if 
https://github.com/dmwm/CRABServer/blob/dc2407fe452c5aa357721e7fc1dd47a2ffe5ac1c/cicd/rucio/cleanup.py#L37
is to "skip if the name does not contain ruciotransfers", no matter if it is a transfer rule or publish rule. This string is created by [test/statusTrackingTasks/rucio_transfers.py](https://github.com/dmwm/CRABServer/blob/5f3ab24a9f3544995d920610b84405d2d2b4dc3a/test/statusTrackingTasks/rucio_transfers.py) where the output container will be similar to `/GenericTTbar/tseethon-ruciotransfers-1712576902-94.../USER` AND `/GenericTTbar/tseethon-ruciotransfers-1712576902-94..._TRANSFER.f4ce12b2/USER` (link to [task](https://cmsweb-test12.cern.ch/crabserver/ui/task/240408_114824%3Atseethon_crab_rucio_transfers_20240408_134822)).

`FakePublish` is to match the task that `tm_publication` is false, like [test/statusTrackingTasks/rucio_transfers_manyedm_nopublication.py](https://github.com/dmwm/CRABServer/blob/5f3ab24a9f3544995d920610b84405d2d2b4dc3a/test/statusTrackingTasks/rucio_transfers_manyedm_nopublication.py).

## Comment (novicecpp, 2024-04-11T12:11:20Z)

> Last note: why do you say that all test are gone ? Do you mean the rules, or the data ? I may be confused, but I thought we write to T2_CH_CERN which has lazy cleanup, not greedy. So data files will stick around also when rule is gone. Indeed we can consider using --purge-replicas (that's the CLI option, I do not have the python arg. at my fingertips).

The rules and its files because I force `--purge-replicas` at [line 49](https://github.com/dmwm/CRABServer/blob/dc2407fe452c5aa357721e7fc1dd47a2ffe5ac1c/cicd/rucio/cleanup.py#L49-L49).

## Comment (belforte, 2024-04-11T12:15:40Z)

Thanks. I misread the `if` :-(  sorry for noise.

## Comment (cmsdmwmbot, 2024-04-11T12:33:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1934/artifact/artifacts/PullRequestReport.html
