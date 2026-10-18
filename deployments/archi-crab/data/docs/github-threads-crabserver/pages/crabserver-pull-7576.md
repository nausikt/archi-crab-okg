# dmwm/CRABServer pull request #7576: Allow incomplete blocks fix 7573

State: closed
Opened: 2023-03-29T23:14:03Z
Closed: 2023-04-02T18:50:01Z
Merged: 2023-04-02T18:50:01Z
URL: https://github.com/dmwm/CRABServer/pull/7576

## Opening post (belforte, 2023-03-29T23:14:03Z)

sligthly improved wrt discussion in chat: always use full replicas of blocks when available.
Note: I Have not a dataset with incomplete blocks at hand to test. Need to find or craft one.

## Comment (cmsdmwmbot, 2023-03-29T23:18:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 75 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1474/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-03-31T12:38:49Z)

while testing I found that current coding does not handle properly disk vs. tape. Will fix.

## Comment (belforte, 2023-03-31T17:31:20Z)

fixed and squashed commits

## Comment (belforte, 2023-03-31T17:35:21Z)

@novicecpp ready for review

## Comment (cmsdmwmbot, 2023-03-31T17:39:54Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1479/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-03-31T21:01:05Z)

I have a request and questions:
- Could you give me dataset name you use to test? I have strange feeling about how we decide if block is available on disk  in the partial block's era and need to crosscheck.
- What is rucio replicas **NOT** `AVAILABLE` state mean?
- If Rucio reaper delete the files, is replicas still there and change from `AVAILABLE` state to another OR replicas object get delete from database?

## Comment (belforte, 2023-04-02T18:27:57Z)

thanks @novicecpp 
good questions, I will address them in line below. If more is needed let's talk on MM or Zoom.
Of course there is not clear documentation in Rucio about those things !

1. Could you give me dataset name you use to test? I have strange feeling about how we decide if block is available on disk in the partial block's era and need to crosscheck.
   * I am afraid that exactly for that reason I do not have such dataset at hand, main problem is that details of what is on disk change. I tested by taking incomplete datasets via `if` in the code. Not ideal, I agree.

2. What is rucio replicas NOT AVAILABLE state mean?
   * if all files which belong to a dataset are AVAILABLE on that RSE, then the dataset replica status is AVAILABLE
      * I could not find a place in Rucio documentation where this is written. Diego told me this. And it matches my experience
   * NOT AVAILABLE can be any of the other possible replica states https://github.com/rucio/rucio/blob/ce39a0bf87105ff50fcc2a9ca5da69d187523f39/lib/rucio/db/sqla/constants.py#L107-L115 .
3. If Rucio reaper delete the files, is replicas still there and change from AVAILABLE state to another OR replicas object get delete from database?
   * We must not confuse file replica and dataset replica. Reaper deletes single files. When a file is deleted the dataset replica still exist on that RSE, but it lacks one file-replica, so it becomes not AVAILABLE. I **think** that it is done [here](https://github.com/rucio/rucio/blob/ce39a0bf87105ff50fcc2a9ca5da69d187523f39/lib/rucio/core/replica.py#L338-L345). If I read the code correctly the when a file replica is deleted, it also gets removed from DB. And again IIUC when a dataset replica has no more files is also removed, but I really do not have guts to fully understand https://github.com/rucio/rucio/blob/master/lib/rucio/core/replica.py and I hope it is not needed
