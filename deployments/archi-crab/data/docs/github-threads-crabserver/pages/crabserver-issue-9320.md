# dmwm/CRABServer issue #9320: Review heavy queries on cms_analysis_reqmgr

State: open
Opened: 2026-06-02T13:01:25Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9320

## Opening post (nausikt, 2026-06-02T13:01:25Z)

We got a report from the DB admin.

there are many inefficient queries that are scanning the whole table and may cause overall Oracle DB performance degradation.

See also [Grafana of other queries/endpoints](https://monit-grafana.cern.ch/goto/u31X8Vxvg?orgId=11) that taking > 100 ms.

## Comment (belforte, 2026-06-23T14:11:50Z)

Please remember to talk to Kate about the other queries which take multiple seconds to ask if something can be done.
