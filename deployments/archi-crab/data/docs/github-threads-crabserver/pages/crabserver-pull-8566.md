# dmwm/CRABServer pull request #8566: Small fixes for rucio publisher

State: closed
Opened: 2024-07-25T19:22:29Z
Closed: 2024-07-26T10:54:43Z
Merged: 2024-07-26T10:54:43Z
URL: https://github.com/dmwm/CRABServer/pull/8566

## Opening post (belforte, 2024-07-25T19:22:29Z)

this PR addresses a couple of bugs and a pylint complain found by pylint when running on PR https://github.com/dmwm/CRABServer/pull/8562

```text
Warnings from pylint by file and severity

    src/python/Publisher/Main.py
    src/python/Publisher/PublisherMasterRucio.py
        E1111, line 396 in Master.markAsFailed: Assigning result of a function call, where the function has no return
        E1123, line 396 in Master.markAsFailed: Unexpected keyword argument 'crabserver' in function call
        W1203, line 317 in Master.startSlave: Use lazy % formatting in logging functions
    src/python/Publisher/RunPublisher.py
    src/python/Publisher/TaskPublishRucio.py
        E1120, line 115 in publishInDBS3.publishOneBlockInDBS: No value for argument 'migLogDir' in function call
```

## Comment (belforte, 2024-07-25T19:22:55Z)

@novicecpp I did not squash commits because it may be easier to review one commit at a time

## Comment (cmsdmwmbot, 2024-07-25T19:28:22Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2068/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-07-26T10:44:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2070/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-26T10:49:49Z)

rebased, maybe there's a way to do w/o the force push... sorry for being clumsy

This spotted a typo in argument name (`crabserver` vs `crabServer`). THANKS THANK THANKS for suggestin to do this check

## Comment (cmsdmwmbot, 2024-07-26T10:50:15Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2071/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-07-26T10:51:38Z)

> rebased, maybe there's a way to do w/o the force push... sorry for being clumsy

No, rebase PR always ends up force-push.
