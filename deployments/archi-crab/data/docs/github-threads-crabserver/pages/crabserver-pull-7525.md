# dmwm/CRABServer pull request #7525: New params inputblocks for support running on datablocks

State: closed
Opened: 2023-02-07T12:25:48Z
Closed: 2023-02-10T14:58:55Z
Merged: 2023-02-10T14:58:55Z
URL: https://github.com/dmwm/CRABServer/pull/7525

## Opening post (novicecpp, 2023-02-07T12:25:48Z)

Fix https://github.com/dmwm/CRABServer/issues/7203

This PR adds new params inputblocks (Data.inputBlocks in client) to let users run jobs on specific blocks.
 Because the underlying code actually processes data by block, I only filter user-specific blocks when fetching at dbs/rucio step, and it works like a charm.

`inputblocks` accept full block name `/dataset#block_uuid` from client. Code in server side already use full block name.

Also, upload warning to remind users that they supply `Data.inputBlocks`.
```
Warning:                        Only blocks in "Data.inputBlocks" will be processed (1 blocks).
```

## Comment (cmsdmwmbot, 2023-02-07T12:30:33Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 34 warnings and errors that must be fixed
   * 12 warnings
   * 226 comments to review
 * Pycodestyle check: succeeded
   * 404 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1414/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-07T18:33:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 34 warnings and errors that must be fixed
   * 12 warnings
   * 226 comments to review
 * Pycodestyle check: succeeded
   * 404 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1415/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-08T17:33:03Z)

Ho @novicecpp , looks very good, thanks. I only ask that you move code improvements to RucioUtils to a different PR

## Comment (cmsdmwmbot, 2023-02-09T14:38:21Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 33 warnings and errors that must be fixed
   * 11 warnings
   * 212 comments to review
 * Pycodestyle check: succeeded
   * 332 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1416/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-10T13:53:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 35 warnings and errors that must be fixed
   * 11 warnings
   * 212 comments to review
 * Pycodestyle check: succeeded
   * 332 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1418/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-10T14:22:43Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 37 warnings and errors that must be fixed
   * 11 warnings
   * 212 comments to review
 * Pycodestyle check: succeeded
   * 332 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1419/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-10T14:30:27Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 32 warnings and errors that must be fixed
   * 11 warnings
   * 212 comments to review
 * Pycodestyle check: succeeded
   * 332 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1420/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-10T14:58:07Z)

thanks. Looks ready to go to me.

## Comment (novicecpp, 2023-02-10T14:59:04Z)

Thanks Stefano. 
Merging
