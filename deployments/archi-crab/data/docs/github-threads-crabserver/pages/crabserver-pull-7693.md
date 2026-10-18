# dmwm/CRABServer pull request #7693: RUCIO_Transfers.py: various fix

State: closed
Opened: 2023-06-29T08:29:27Z
Closed: 2023-07-05T10:35:52Z
URL: https://github.com/dmwm/CRABServer/pull/7693

## Opening post (novicecpp, 2023-06-29T08:29:27Z)

It is not just fix from Stefano comments but including all what I have in my current private branch which contains:
- Seperation between rucio replica/lock and metadata we passing around function called "fileDoc".
- Remove "skip monitoring lock for the files in the same run".
- Rename update status to rest server.
- Closing dataset when time has passed.
- Filter out logs transfers.
- Ensure to not create a new dataset when no new replica.

I disagree to move rest update outside RegisterReplicas and MonitorLockStatus class. It tight couple with the context of the action classes on which key of `fileDoc` is needed for the REST API.

## Comment (cmsdmwmbot, 2023-06-29T08:35:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1565/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-07-05T10:35:52Z)

Closing this due to too many changes in same PR.
Supersede by https://github.com/dmwm/CRABServer/pull/7716
