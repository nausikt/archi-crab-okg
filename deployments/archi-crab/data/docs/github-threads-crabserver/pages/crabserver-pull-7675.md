# dmwm/CRABServer pull request #7675: RUCIO_Transfers.py: add MonitorLockStatus action

State: closed
Opened: 2023-06-19T09:16:32Z
Closed: 2023-06-29T08:13:07Z
Merged: 2023-06-29T08:13:07Z
URL: https://github.com/dmwm/CRABServer/pull/7675

## Opening post (novicecpp, 2023-06-19T09:16:32Z)

Third actions of RUICO_Transfers.py scripts. Basically:
- If replicas is OK, add it to publish container, update status in transferdb to transfer done.
- Check if block is complete, update block information in rest for all files in the block
- bookkeepping replicas where block is completed, in local file(s)

2 things that need to improve (but I have no idea how):
- `checkBlockCompleteStatus` function name can be mislead. 
  - Not just check and return block complete list. It actually filter out the replicas in incomplete block.
- Closing dataset when 6 hours pass. 
  - If we close it, next iteration will create new dataset, then close in next 6 hours. We will have empty dataset.

## Comment (cmsdmwmbot, 2023-06-19T09:21:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1546/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-06-29T08:12:35Z)

As we agreed in private chat. I am merging this PR and open a new one to fix what Stefano comments.
