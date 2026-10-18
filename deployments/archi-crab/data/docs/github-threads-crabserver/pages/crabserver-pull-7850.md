# dmwm/CRABServer pull request #7850: RUCIO_Transfers.py: fix pylint before merge to master

State: closed
Opened: 2023-08-22T17:16:25Z
Closed: 2023-08-23T15:09:18Z
Merged: 2023-08-23T15:09:18Z
URL: https://github.com/dmwm/CRABServer/pull/7850

## Opening post (novicecpp, 2023-08-22T17:16:25Z)

Ignore some warnings:

- W1203, line 44 in BuildDBSDataset.checkOrCreateContainer: Use lazy % formatting in logging functions 
  - Need to change pylint config instead (Stefano already mentioned this sometime ago.)
- C0103:  Module name "<module_name>" doesn't conform to '[A-Z,a-zA-Z0-9]+$' pattern
- R0903, line 17 in RunTransfer: Too few public methods (1/2)
- R0902, line 13 in Transfer: Too many instance attributes (17/7)

Also I did not try to correct pylint warning from `cmscp.py`,  `PostJob.py` (Will check it after warning from new files is solve at it later), and files in `src/test` directory.

There is pylint warning `R0402, line 8: Use 'from ASO.Rucio import config' instead` that I explicitly disable it in code. 
When change to `from..import`, object reference still point to old object instead the new one where I modified it in [ASO/Rucio/Main.py#L73](https://github.com/dmwm/CRABServer/blob/ed4915d91af1deb425212c2e363e656415e7a87f/src/python/ASO/Rucio/Main.py#L73), so it got `None` instead of object return from `ArgumentParser.parse_args()`. Maybe I misunderstand something but I will do it later.

## Comment (cmsdmwmbot, 2023-08-22T17:18:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1664/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-08-22T18:52:14Z)

pylint jenkins is broken when merge to non-master branch.

Logs: https://cmssdt.cern.ch/dmwm-jenkins/job/DMWM-CRABServer-PR-pylintpy3/407/console

```
...
error: pathspec 'rucio_transfers' did not match any file(s) known to git
...
...
fatal: ambiguous argument 'rucio_transfers..e980e624ffb0cb57e0881b8803410158370b7a12': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
...
```

Errors code are around here: https://gitlab.cern.ch/CMSDOCKS/dmwm/-/blob/80463d704594841b7913f841773619656449cc34/crab_staticanalysis/crab/pylintTest.sh#L26-33

## Comment (cmsdmwmbot, 2023-08-23T13:17:17Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1665/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-23T13:24:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1666/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-23T13:38:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 49 warnings and errors that must be fixed
   * 14 comments to review
 * Pycodestyle check: succeeded
   * 72 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1667/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-23T14:37:57Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 42 warnings and errors that must be fixed
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 72 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1668/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-23T14:50:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 42 warnings and errors that must be fixed
   * 11 comments to review
 * Pycodestyle check: succeeded
   * 72 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1669/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-23T15:00:13Z)

@novicecpp honestly I do not have the strength nor time to review this in detail. I trust you more than I trust me on these matters anyhow. Let's merge and see how it goes.

## Comment (novicecpp, 2023-08-23T15:09:02Z)

Thanks. It only fixes pylint complaints without changing any code logic.
The Main point is if we agree to mute some pylint complaints that I summarize in the PR description.
Indeed, we can have a chat about it later. No need to rush. I will add comment in https://github.com/dmwm/CRABServer/issues/7756.
