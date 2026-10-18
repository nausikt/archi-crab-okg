# dmwm/CRABServer pull request #8530: store also scope in tm_dbs_blockname. Quick fix for #8525

State: closed
Opened: 2024-06-26T20:47:35Z
Closed: 2024-06-27T11:19:51Z
Merged: 2024-06-27T11:19:51Z
URL: https://github.com/dmwm/CRABServer/pull/8530

## Opening post (belforte, 2024-06-26T20:47:35Z)

quick and dirty fix which appears to work by looking at FileTransfersDB  content in e.g. https://cmsweb-test2.cern.ch/crabserver/ui/task/240626_200922%3Abelforte_crab_rucio_transfers_20240626_220918
 and https://cmsweb-test2.cern.ch/crabserver/ui/task/240626_203056%3Abelforte_crab_rucio_transfers_group_20240626_223054

A more elegant solution is beyond what I can do now and would require to deepen my understanding of ASO/Rucio first see https://github.com/dmwm/CRABServer/issues/8525#issuecomment-2192593099

## Comment (cmsdmwmbot, 2024-06-26T20:50:41Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 27 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2035/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-06-27T11:19:51Z)

thanks Wa
