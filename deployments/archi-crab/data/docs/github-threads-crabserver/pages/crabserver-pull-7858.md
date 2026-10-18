# dmwm/CRABServer pull request #7858: Store Rucio ASO information to tasksDB

State: closed
Opened: 2023-08-29T19:58:46Z
Closed: 2023-08-30T18:45:11Z
Merged: 2023-08-30T18:45:11Z
URL: https://github.com/dmwm/CRABServer/pull/7858

## Opening post (novicecpp, 2023-08-29T19:58:46Z)

Adding 3 new columns to TasksDB to store Rucio ASO information with the new `subresource=addrucioasoinfo` to update 
- Transfer Container name (`tm_transfer_container`).
- Rucio's Rule ID of *Transfer Container* (`tm_transfer_rule`).
- Rucio's Rule ID of *Publish Container* (`tm_publish_rule`).

This information will upload to db only "once" in RUCIO_Transfers.py scripts (before bookkeeping rule id).

Example tasks: https://cmsweb-test12.cern.ch/crabserver/ui/task/230829_165108%3Atseethon_crab_rucio_transfers_publication_test12_20230829_185106

No need new API to get this data. Current client already fetch all column from Task table.

## Comment (cmsdmwmbot, 2023-08-29T20:02:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 48 warnings and errors that must be fixed
   * 6 warnings
   * 48 comments to review
 * Pycodestyle check: succeeded
   * 280 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1680/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-30T16:36:07Z)

depends what you mean with "leave in token world". Eventually X509 will not be supported at all and we may have user tokens, but not user proxies. Since tokens are "capability-based" one can imagine that jobs carry a token that says "the bearer can read from /store/data and can write in /store/temp/user".
If we could extent to "bearer can write in /store/user/rucio" a lot of possibilities would open up.

## Comment (cmsdmwmbot, 2023-08-30T18:44:25Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 48 warnings and errors that must be fixed
   * 6 warnings
   * 48 comments to review
 * Pycodestyle check: succeeded
   * 278 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1684/artifact/artifacts/PullRequestReport.html
