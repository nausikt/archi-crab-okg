# dmwm/CRABServer issue #7737: add crab_input quota to monitoring

State: closed
Opened: 2023-07-10T17:38:53Z
Closed: 2023-07-14T17:04:43Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7737

## Opening post (belforte, 2023-07-10T17:38:53Z)

change
- [x] https://github.com/dmwm/CRABServer/blob/v3.230705/src/script/Monitor/GenerateMONIT.py
- [ ] https://github.com/dmwm/CRABServer/blob/v3.230705/src/python/TaskWorker/Actions/Recurring/ReportRecallQuota.py

possibly rename the latter to be more generic and then change list of recurrent actions in puppet TW config
- [ ] https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/data/fqdns/crab-prod-tw01.cern.ch.yaml#L17

## Comment (belforte, 2023-07-12T16:07:07Z)

as a short term fix, I have added panels from Rucio dashbard to https://monit-grafana.cern.ch/d/CsnjLe6Mk/crab-overview?orgId=11

## Comment (belforte, 2023-07-14T13:19:14Z)

I can't understand those panels in RUcio dashboard and do not really trust them. Let's make sure I have some data I understand to look at !

## Comment (belforte, 2023-07-14T17:03:23Z)

GenerateMONIT.py is too fragile already and we need to change how it is run.
Let's simply add a data push to MONIT in the [Recurring action](https://github.com/dmwm/CRABServer/blob/v3.230705/src/python/TaskWorker/Actions/Recurring/ReportRecallQuota.py)

Done in https://github.com/belforte/CRABServer/commit/fe159fd2c09e0a1a06b5d836acf528dc4e5d8867

## Comment (belforte, 2023-07-14T17:04:27Z)

Also remove reporing of Rucio quotas in GenerateMONIT, since the ad-hoc JSON file is not there anymore
https://github.com/dmwm/CRABServer/pull/7760/commits/c5a9e57b6c2284ee8674598bdc14d65da7bbe734
