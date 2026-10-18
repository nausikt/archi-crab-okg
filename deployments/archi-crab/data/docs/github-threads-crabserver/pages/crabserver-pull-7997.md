# dmwm/CRABServer pull request #7997: Multiple Publish Container

State: closed
Opened: 2023-11-07T17:34:27Z
Closed: 2023-11-27T17:26:54Z
Merged: 2023-11-27T17:26:54Z
URL: https://github.com/dmwm/CRABServer/pull/7997

## Opening post (novicecpp, 2023-11-07T17:34:27Z)

Fix https://github.com/dmwm/CRABServer/issues/7976

In summary, this PR is changed in following ASO code:
-  Add new column `tm_multipub_rule` to `TASKS` table.
- Construct `Transfer.multiPubContainers` attribute  to store all publish container names.
- Create container for all `Transfer.multiPubContainers` and store rule ids in `Transfer.multiPubRuleIDs` attribute.
- New `MonitorLockStatus.registerToMultiPubContainers()` method to register transferred success replicas to its own publish container.
And the code in REST:
  - New `multipubrulejson` args for `tasks/?subresource=addrucioasoinfo`

~~The new Publish Container names will have `__<filename>` append to container "name" section (see docstring in newly added method `registerToMutiPubContainers()` for more detail).~~

New Rucio Publish Container Scheme: https://github.com/dmwm/CRABServer/issues/7976#issuecomment-1819487757

And please ignore pytest.

## Comment (cmsdmwmbot, 2023-11-07T17:36:43Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 81 warnings and errors that must be fixed
   * 8 warnings
   * 169 comments to review
 * Pycodestyle check: succeeded
   * 401 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1752/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-09T11:46:44Z)

@novicecpp while looking at changes, I have to recap in my mind how everything works, since there are so many files and thins... I happened to notice that Transfers/readInfoFromRucio is empty (only comments). So I presume it is a placeholder for something still to be implemented ? Or something to cleanup ? Could you put some comments to explain ?

## Comment (novicecpp, 2023-11-09T12:28:27Z)

It is used to fetch some data/state from Rucio and save it in `Transfer` attribute for use in the entire application.
Not need it anymore. I will remove it later.

## Comment (novicecpp, 2023-11-09T20:55:17Z)

> but at the moment I do not find where the multiPubContainer are turned into proper DBS dataset names and where the proper ones get the info for DBS (block name/complete status) updated in transfersdb.

Ohhhhhhh. I completely forgot that the container name where EDM files live has changed, and most importantly, it breaks Publisher :man_facepalming:
I do not have solution yet. Let's me think about it for a day or two.

## Comment (belforte, 2023-11-09T21:08:18Z)

But we should have proper output dataset names already for those files, i.e. names which are good for DBS.
Well at this time I am not able to have a really educated opinion.

## Comment (cmsdmwmbot, 2023-11-22T09:38:35Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 89 warnings and errors that must be fixed
   * 10 warnings
   * 331 comments to review
 * Pycodestyle check: succeeded
   * 1018 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1762/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-11-22T10:05:47Z)

Thanks to suggestions from Stefano and the new Rucio Publish Container's naming scheme, I only need to change the naming and it is working out-of-the-box.

@belforte PR is working fine with Publisher (at least report from `crab status`), and ready to review again.

## Comment (cmsdmwmbot, 2023-11-22T10:06:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 89 warnings and errors that must be fixed
   * 10 warnings
   * 331 comments to review
 * Pycodestyle check: succeeded
   * 1018 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1763/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-22T10:24:38Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 86 warnings and errors that must be fixed
   * 10 warnings
   * 329 comments to review
 * Pycodestyle check: succeeded
   * 1019 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1764/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-22T10:32:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 85 warnings and errors that must be fixed
   * 10 warnings
   * 329 comments to review
 * Pycodestyle check: succeeded
   * 1018 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1765/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-27T17:20:36Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 85 warnings and errors that must be fixed
   * 10 warnings
   * 329 comments to review
 * Pycodestyle check: succeeded
   * 1021 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1772/artifact/artifacts/PullRequestReport.html
