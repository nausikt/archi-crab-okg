# dmwm/CRABServer pull request #8529: Publisher rucio to check block completion 8491

State: closed
Opened: 2024-06-26T20:45:35Z
Closed: 2024-06-27T09:09:07Z
URL: https://github.com/dmwm/CRABServer/pull/8529

## Opening post (belforte, 2024-06-26T20:45:35Z)

quick and dirty fix which appears to work by looking at FileTransfersDB  content in e.g. https://cmsweb-test2.cern.ch/crabserver/ui/task/240626_200922%3Abelforte_crab_rucio_transfers_20240626_220918
 and https://cmsweb-test2.cern.ch/crabserver/ui/task/240626_203056%3Abelforte_crab_rucio_transfers_group_20240626_223054

A more elegant solution is beyond what I can do now and would require to deepen my understanding of ASO/Rucio first see https://github.com/dmwm/CRABServer/issues/8525#issuecomment-2192593099

## Comment (cmsdmwmbot, 2024-06-26T20:49:50Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2034/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-06-27T08:53:42Z)

Is it the same as https://github.com/dmwm/CRABServer/pull/8526, https://github.com/dmwm/CRABServer/commit/c65d8afad17ca85f613bd245df1302534e11c64e ?
Why does GH show this PR still diff with master?
Or do I misunderstand something?

## Comment (belforte, 2024-06-27T09:06:33Z)

oops... my bad. sorry. I know why I did this mistake
