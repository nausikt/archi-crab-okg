# dmwm/CRABServer pull request #7862: Taperecall: allow to recall any data tier if size less than threshold

State: closed
Opened: 2023-09-01T15:20:13Z
Closed: 2023-09-05T09:18:12Z
Merged: 2023-09-05T09:18:12Z
URL: https://github.com/dmwm/CRABServer/pull/7862

## Opening post (novicecpp, 2023-09-01T15:20:13Z)

Fix https://github.com/dmwm/CRABServer/issues/7841

The current policy is (correct me if I am wrong):
1. Allow to recall any dataset with size less than threshold.
2. If recall dataset are in `*AOD*` tier allow recall any size.

This PR is special. Actually, the [first commit](https://github.com/dmwm/CRABServer/commit/e0dcafa7a88cbcdd066e5424f17b2c9e7919ba5a) is already do the job. But I want to show a small but valuable use case of unittest that helps me code with fewer mistakes and get faster feedback (no need to submit the tasks).

PS. Thanks to Stefano for refactoring tape recall condition (especially the part involve `usePartialDataset`). It is much more easier to change the code.

## Comment (cmsdmwmbot, 2023-09-01T15:23:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 14 comments to review
 * Pycodestyle check: succeeded
   * 67 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1686/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-04T18:09:30Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1687/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-09-04T18:13:02Z)

Changing the messages as Stefano suggested:

For input **block** larger than threshold (line 484):
```
Warning:                        Some blocks are on TAPE only and will not be processed.
                                The 'Data.inputBlocks' size is larger than the allowed size to issue automatic recall from TAPE (172.541TB/50TB).
                                If you need these blocks, contact Data Transfer team via https://its.cern.ch/jira/browse/CMSTRANSF
```
For input **dataset** larger than threshold (last else):
```
Warning:                        Some blocks are on TAPE only and will not be processed.
                                This dataset is too large for automatic recall from TAPE. If you can do with only a piece, use Data.inputBlocks configuration.
                                If you need the full dataset, contact Data Transfer team via https://its.cern.ch/jira/browse/CMSTRANSF
```

## Comment (belforte, 2023-09-05T08:27:45Z)

looks good, thanks !
