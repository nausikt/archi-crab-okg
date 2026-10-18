# dmwm/CRABServer pull request #7541: RucioUtils.py:getWritePFN - fix bug in dealing with exception

State: closed
Opened: 2023-02-17T12:54:21Z
Closed: 2023-02-17T12:59:59Z
Merged: 2023-02-17T12:59:58Z
URL: https://github.com/dmwm/CRABServer/pull/7541

## Opening post (mapellidario, 2023-02-17T12:54:21Z)

Fixes #7540 

### status

tested:

- [x]  https://cmsweb-test11.cern.ch/crabserver/ui/task/230217_124810%3Admapelli_crab_20230217_134807

```plaintext
...
Failure message from server:    lfn2pfn resolution with Rucio failed for site: T2_CH_CERNBOX  LFN: /store/user/dmapelli/230217124810dmapellicrab20230217134807_crab3check.tmp with exception :
                                operation: third_party_copy_write, exception: RSE does not exist.
                                Details: RSE 'T2_CH_CERNBOX' cannot be found in vo 'def'
...
```

I think this is ready for merge, but I am open to comments and suggestions

### description

I save the string of the exception for every iteration of the loop, not only for the last one. It seems a bit more meaningful.

## Comment (cmsdmwmbot, 2023-02-17T12:57:27Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 1 warnings
   * 8 comments to review
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1429/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-17T12:58:32Z)

I like it, thanks Dario.

## Comment (mapellidario, 2023-02-17T12:59:48Z)

Good! Thanks Stefano, I will merge it :)
