# dmwm/CRABServer issue #8264: Abandon storage.xml in favor of storage.json (Issue from WMCore upstream)

State: closed
Opened: 2024-02-28T11:18:20Z
Closed: 2024-04-29T22:27:09Z
URL: https://github.com/dmwm/CRABServer/issues/8264

## Opening post (novicecpp, 2024-02-28T11:18:20Z)

Blocked by [Abandon storage.xml in favor of storage.json for stage-in and stage-out](https://github.com/dmwm/WMCore/issues/11703). 
We will wait until the upstream issue is solved.

Comments move from meeting minutes:
- Wa will give this an initial round of check by building TW with their modified WMCore. Still an open issue in WMCore. Wait until they close this on their side.
- Good time to review cmscp.py and possibly refactor and simplify, hoping that the new implementation does not require (large) changes on our side to use it.

## Comment (novicecpp, 2024-03-28T14:23:25Z)

https://monit-grafana.cern.ch/goto/OEPl3mxIg?orgId=11

All sites are working fine with TW v3.240325 Stefano deployed on preprod. 
(Failed jobs are all exceed wall clock time (10mins).

![image](https://github.com/dmwm/CRABServer/assets/2346664/c7befe27-7666-4881-882b-ebae0ab40c55)

## Comment (novicecpp, 2024-03-28T14:24:26Z)

Keep issue open until new TW is on prod at least 1 week.

## Comment (belforte, 2024-04-03T20:11:36Z)

TW was put in production on Apr 2

## Comment (novicecpp, 2024-04-29T22:27:09Z)

Done
