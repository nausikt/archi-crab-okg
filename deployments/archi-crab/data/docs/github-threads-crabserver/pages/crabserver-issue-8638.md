# dmwm/CRABServer issue #8638: CRAB Overview dashboard - requests panel is empty now

State: closed
Opened: 2024-08-21T10:34:01Z
Closed: 2024-12-12T10:13:11Z
Labels: Type: Bug, Priority: High, Status: Available, Area: MONIT
URL: https://github.com/dmwm/CRABServer/issues/8638

## Opening post (mapellidario, 2024-08-21T10:34:01Z)

Since the transition from apache to APS frontend, we need to adapt our "requests" panel [1] and dashboard [2] to use the new opensearch index used in the new frontend dashbaord [3]. 

The APS monitoring is currently broken, it is being followed up in [4], so i set the status if this issue "on hold".

---

[1] https://monit-grafana.cern.ch/goto/MJoiRjjSR?orgId=11
[2] https://monit-grafana.cern.ch/d/qUVV6S0Gk/crab-fe-timber-2b-pods?orgId=11
[3] https://monit-grafana.cern.ch/goto/8NsGRjCSg?orgId=11
[4] https://its.cern.ch/jira/browse/CMSMONIT-620

## Comment (belforte, 2024-08-28T15:49:34Z)

APS monitoring was fixed https://its.cern.ch/jira/browse/CMSMONIT-620?focusedId=6501107&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6501107

Removing HOLD

## Comment (novicecpp, 2024-08-28T15:55:42Z)

FYI, I have reverted [FE timber + pods](https://monit-grafana.cern.ch/d/qUVV6S0Gk/crab-fe-timber-2b-pods?orgId=11) to apache version today.

Here is backup of APS version: `/afs/cern.ch/user/t/tseethon/public/fetimber_pods_aps.json`

## Comment (belforte, 2024-12-12T10:13:11Z)

this was solved.
