# dmwm/CRABServer issue #8235: Fix Grafana alert migrated from old instance

State: closed
Opened: 2024-02-14T11:23:01Z
Closed: 2024-08-23T15:35:16Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8235

## Opening post (novicecpp, 2024-02-14T11:23:01Z)

Grafana's alert messages from the new instance are [very long and difficult to read](https://mattermost.web.cern.ch/cms-o-and-c/pl/ka999dtcw3fu3q6s4wos9nz4mw). Some alerts are incorrect. 

- [x] (fixed) For example, [this alert](https://mattermost.web.cern.ch/cms-o-and-c/pl/thefws78rjbz58oi1t7nd9ofah) is fired because it matched preprod's metrics (using [this](https://community.grafana.com/t/lucene-query-not-working-as-expected/39314/2) suggestion)
- [ ] Also, check the panel if it migrate to new TimeSerie

And [old instances are still running and keep sending alerts](https://mattermost.web.cern.ch/cms-o-and-c/pl/14sm96fj8pd5djh44s4phg54ih), which makes the MM channel very cluttered.

## Comment (belforte, 2024-08-23T15:35:16Z)

DONE
