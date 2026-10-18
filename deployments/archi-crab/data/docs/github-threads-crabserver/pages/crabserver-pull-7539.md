# dmwm/CRABServer pull request #7539: Allow blocks taperecall for any Tier if inputblocks provided

State: closed
Opened: 2023-02-16T17:55:54Z
Closed: 2023-02-17T16:19:11Z
Merged: 2023-02-17T16:19:11Z
URL: https://github.com/dmwm/CRABServer/pull/7539

## Opening post (novicecpp, 2023-02-16T17:55:54Z)

Fix https://github.com/dmwm/CRABServer/issues/7528

I have changed what we agree in https://github.com/dmwm/CRABServer/issues/7528#issuecomment-1425955091,
from **Allow to recall blocks in the new list of dataTier (e.g. RAW, RECO)**,
to **Allow to recall any number of blocks if it not in `tiersToRecall`  as long as 1) `inputblocks` provided 2) not exceed the limit**.
(The limitation can config via `config.TaskWorker.maxTierToBlockRecallSizeTB`)

This way there is no need to maintain possible dataTier and it make if-else of taperecall's decision more simpler.

Also, simply remove [DBSDataDiscovery.py#L453-L460](https://github.com/dmwm/CRABServer/blob/9e822e562a3200c2eacebb5f93d66ca2b17d3583/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L453-L460) and let it fall through the if-else below.

## Comment (cmsdmwmbot, 2023-02-16T18:00:32Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 4 warnings
   * 67 comments to review
 * Pycodestyle check: succeeded
   * 77 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1427/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-16T18:09:20Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 4 warnings
   * 63 comments to review
 * Pycodestyle check: succeeded
   * 77 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1428/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-17T14:07:35Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 4 warnings
   * 60 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1430/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-17T14:09:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 4 warnings
   * 60 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1431/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-17T14:22:24Z)

I am done reviewing. Looks better and better :-)

## Comment (belforte, 2023-02-17T16:04:48Z)

feel free to merge

## Comment (cmsdmwmbot, 2023-02-17T16:06:08Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 4 warnings
   * 60 comments to review
 * Pycodestyle check: succeeded
   * 77 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1432/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-02-17T16:17:48Z)

Thanks Stefano.
You review/comment is faster than pylint jobs and my response :)
