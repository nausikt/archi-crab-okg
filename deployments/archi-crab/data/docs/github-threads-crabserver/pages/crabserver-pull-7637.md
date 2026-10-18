# dmwm/CRABServer pull request #7637: RUCIO_Transfers.py: Add RegisterReplicas action

State: closed
Opened: 2023-05-16T06:31:44Z
Closed: 2023-05-30T12:44:24Z
URL: https://github.com/dmwm/CRABServer/pull/7637

## Opening post (novicecpp, 2023-05-16T06:31:44Z)

The second PR of new RUCIO_Transfers.py scripts for `RegisterReplicas` action.
Note that I merged https://github.com/dmwm/CRABServer/pull/7636 and this PR is opened on top of that.

@belforte do you prefer to review it by yourself or do it together ?

## Comment (cmsdmwmbot, 2023-05-16T06:37:39Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1521/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-05-24T10:32:58Z)

@novicecpp I am having a first read myself. Maybe we go through it together later so I can explain my doubts, if needed. Thanks

## Comment (novicecpp, 2023-05-24T13:07:13Z)

Thanks Stefano. 
Actually, my private branch contain a lot of changes to `RegisterReplicas.py` and `Transfer.py` that I plan to take this down and open the new one.

Let me gather your comments, close this one, and open the new one later.

## Comment (belforte, 2023-05-24T14:28:35Z)

Sorry, has a 2h power cut. OK. Let me finish reading and then switch to new version.

## Comment (belforte, 2023-05-24T14:37:51Z)

everything looks good to me. Only the minor comment above.
Close at your convenience

## Comment (novicecpp, 2023-05-30T12:44:24Z)

Closing this in favor of new PR https://github.com/dmwm/CRABServer/pull/7649.
