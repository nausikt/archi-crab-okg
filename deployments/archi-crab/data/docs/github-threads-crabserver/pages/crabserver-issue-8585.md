# dmwm/CRABServer issue #8585: avoid duplicated `queue` statement in dagman JDL

State: closed
Opened: 2024-08-02T20:14:29Z
Closed: 2024-08-03T21:28:18Z
Labels: Priority: High, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8585

## Opening post (belforte, 2024-08-02T20:14:29Z)

see
https://github.com/dmwm/CRABServer/issues/8272#issuecomment-2265870173

need to remove the extra `queue` at the bottom of `subdag.JDL` in

https://github.com/dmwm/CRABServer/blob/6b9d38ac9667d83246abef44fc3e9f9a8bec569b/src/python/TaskWorker/Actions/DagmanSubmitter.py#L520-L527

## Comment (belforte, 2024-08-03T21:20:24Z)

fix works
