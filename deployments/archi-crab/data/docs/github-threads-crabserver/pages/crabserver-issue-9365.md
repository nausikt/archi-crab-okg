# dmwm/CRABServer issue #9365: track HOLDING states, all CRAB status values.

State: open
Opened: 2026-07-24T15:10:43Z
Labels: Area: MONIT
URL: https://github.com/dmwm/CRABServer/issues/9365

## Opening post (nausikt, 2026-07-24T15:10:43Z)

(no text)

## Comment (belforte, 2026-07-24T16:06:18Z)

the number of tasks in each status is sent to OpenSearch in https://github.com/dmwm/CRABServer/blob/master/src/script/Monitor/GenerateMONIT.py

At first sight it is a matter of extending this list
https://github.com/dmwm/CRABServer/blob/ea2f8c0bfa80ac2c0d9b2d2065f6f0130f9a39d7/src/script/Monitor/GenerateMONIT.py#L241-L242

But of course better have a closer look and test things.

Note whenever we build a new image it gets picked by monitor cron in crab-test-tw02 which feeds
https://monit-grafana.cern.ch/d/f72be185-5789-4015-933a-a29a6ed75514/crab-overview-test-monitoring?orgId=11&from=now-30d&to=now&timezone=browser&var-crabosindex=fe12b234-8cb7-434a-a8c5-0199ee28eb14&var-monit_source=crab-dev-tw02.cern.ch&var-productionSchedulers=$__all&var-schedd=$__all&refresh=1h

short url: https://monit-grafana.cern.ch/goto/bft39iiyc4w74e?orgId=11

see https://cmscrab.docs.cern.ch/crab-components/crab-monitoring/crab-crontabs.html for more on how code gets run by feeder for test and main dashboards
