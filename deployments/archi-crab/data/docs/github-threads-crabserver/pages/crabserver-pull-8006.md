# dmwm/CRABServer pull request #8006: Fix getNativeRucioClientload load wrong config

State: closed
Opened: 2023-11-16T17:41:46Z
Closed: 2023-11-17T15:05:26Z
Merged: 2023-11-17T15:05:26Z
URL: https://github.com/dmwm/CRABServer/pull/8006

## Opening post (novicecpp, 2023-11-16T17:41:46Z)

Fix https://github.com/dmwm/CRABServer/pull/8006

Fix the `getNativeRucioClient()` to load correct config. Also change PreDag.py to assign user cert path to proper config attribute.

## Comment (cmsdmwmbot, 2023-11-16T17:46:13Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 4 warnings
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 24 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1759/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-16T17:49:11Z)

even if not now. It will be good to record a minimal explanation with this PR
Do IUC that in the code we had not switched to pick Rucio credential from the new `Services` section of the config ? :-(

## Comment (novicecpp, 2023-11-16T17:51:57Z)

In short, yes. 
I will add everything later.

## Comment (belforte, 2023-11-16T17:56:38Z)

no hurry. thanks for sorting this out.

## Comment (belforte, 2023-11-17T15:04:39Z)

good. Thanks
