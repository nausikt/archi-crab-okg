# dmwm/CRABServer pull request #8101: Fix all possibly unbound in DBSDataDiscovery

State: closed
Opened: 2023-12-15T07:15:53Z
Closed: 2023-12-15T09:47:19Z
Merged: 2023-12-15T09:47:18Z
URL: https://github.com/dmwm/CRABServer/pull/8101

## Opening post (novicecpp, 2023-12-15T07:15:53Z)

Fix https://github.com/dmwm/CRABServer/issues/8100 and potential bugs that may cause `local variable referenced before assignment`. The "potential bugs" are reported by pyright as explained in https://github.com/dmwm/CRABServer/issues/8100#issuecomment-1857383835.

## Comment (cmsdmwmbot, 2023-12-15T07:18:43Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 62 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1787/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-12-15T07:20:33Z)

Tasks with the [HC dataset](https://cmsweb-test12.cern.ch/crabserver/ui/task/231215_070437%3Atseethon_crab_hc_1kj_test12_20231215_080432) and [User dataset](https://cmsweb-test12.cern.ch/crabserver/ui/task/231215_070503%3Atseethon_crab_user_dataset_user_test12_20231215_080500) can be submitted properly.

## Comment (belforte, 2023-12-15T09:41:33Z)

perfect, thanks. And sorry for the bug.

## Comment (belforte, 2023-12-15T09:41:45Z)

you can merge

## Comment (novicecpp, 2023-12-15T09:47:01Z)

Thanks.
