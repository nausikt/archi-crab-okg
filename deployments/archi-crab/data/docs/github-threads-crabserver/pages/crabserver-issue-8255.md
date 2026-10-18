# dmwm/CRABServer issue #8255: Schedd instant load dashboard - no data in grafana

State: closed
Opened: 2024-02-20T14:54:54Z
Closed: 2024-04-12T11:37:29Z
Labels: Status: On Hold, Area: MONIT, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8255

## Opening post (mapellidario, 2024-02-20T14:54:54Z)

The following dashboard [1] is empty, despite the necessary documents appear to be in opensearch [2]. Unusual, I will have a look

[1] https://monit-grafana.cern.ch/d/byfWUEhZk/crab-schedds-instant-load?orgId=11&from=now-30d&to=now
[2] https://monit-opensearch-lt.cern.ch/dashboards/goto/31d6e610962e003ce8adc89217e18896

## Comment (mapellidario, 2024-02-20T15:11:36Z)

Data about duty cycle come from [3]. SI is aware that there is no data after 2024-02-01, they do not know the cause and are investigating.

Meanwhile, the panel about running dagmans in every schedd in a dashboard in playground [4] copied from [1] is ok. the plot thickens, I will need to ask nikodemas...


[3] `SI-condor` in grafana, `monit_prod_cms_raw_si_condor_*` index in https://monit-opensearch.cern.ch .
 https://monit-opensearch.cern.ch/dashboards/goto/6cf8ba87da4a7c3c982a7bb5fc9807f6

[4] https://monit-grafana.cern.ch/goto/cUzOvVTSg?orgId=11

## Comment (belforte, 2024-02-20T18:03:09Z)

sorry, I noticed a few days ago and pinged SI, but did not tell you.
https://mattermost.web.cern.ch/cms-o-and-c/pl/8g9zehm7upd8zx6cktdbszdg3r
But AFAICT running dagman panel is OK also in [1] (all in all it comes from CRAB monitoring i.e. our own reporting)
It is just the schedd's duty cycle which is missing.

## Comment (mapellidario, 2024-04-12T11:37:29Z)

fixed by si/monit
