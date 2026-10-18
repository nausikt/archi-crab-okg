# dmwm/CRABServer pull request #8001: fix #7948 also restrict partialDataset to disk data

State: closed
Opened: 2023-11-08T21:02:09Z
Closed: 2023-11-09T16:40:51Z
Merged: 2023-11-09T16:40:51Z
URL: https://github.com/dmwm/CRABServer/pull/8001

## Opening post (belforte, 2023-11-08T21:02:09Z)

There are three things in this PR

* fix for #7948
* some small pylint 
* I added line 312 in DBSDataDiscovery https://github.com/belforte/CRABServer/blob/e9e96fbc9beee5c2fea1d8cd0cfe8cae32da4e6f/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L312 which IMHO fixes a but. As it was there was the possibility that we try to process a block which is partially on tape, not very likely, but if it happens hard to understand. I have not tested, but I think that current code would have anyhow added tape sites to the location list, confusing, but not harmful if there's also disk, nobody would notice.

## Comment (cmsdmwmbot, 2023-11-08T21:04:38Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
 * Pycodestyle check: succeeded
   * 61 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1755/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-08T21:05:05Z)

this is now running on crab-dev-tw01. I guess we can also run some tests

## Comment (cmsdmwmbot, 2023-11-08T21:14:43Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 61 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1756/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-09T16:40:46Z)

thanks Wa
