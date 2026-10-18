# dmwm/CRABServer pull request #7996: WIP: Multiple Publish Container

State: closed
Opened: 2023-11-07T17:22:26Z
Closed: 2023-11-07T17:35:03Z
URL: https://github.com/dmwm/CRABServer/pull/7996

## Opening post (novicecpp, 2023-11-07T17:22:26Z)

Fix https://github.com/dmwm/CRABServer/issues/7976

In summary, this PR is changed in following code part:
-  Add new column `tm_multipub_rule`
- Construct `Transfer.multiPubContainers` to store all publish container names.
- Create container for all `Transfer.multiPubContainers` and store rule ids in `Transfer.multiPubRuleIDs`.
- New `MonitorLockStatus.registerToMutiPubContainers()` to register transferred success replicas to its own publish container.

Please ignore pytest for now.

## Comment (cmsdmwmbot, 2023-11-07T17:24:43Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 81 warnings and errors that must be fixed
   * 8 warnings
   * 169 comments to review
 * Pycodestyle check: succeeded
   * 401 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1751/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-11-07T17:35:03Z)

wrong branch.
