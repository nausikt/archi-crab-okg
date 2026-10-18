# dmwm/CRABServer issue #7611: add quota used by tape_recall to Grafana

State: closed
Opened: 2023-04-20T14:43:37Z
Closed: 2023-04-21T12:44:50Z
Labels: Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7611

## Opening post (belforte, 2023-04-20T14:43:37Z)

- [x] create a recurring action in TW to get info from Rucio and put in log/TapeRecallQuota.json
- [x] modify GenerateMONIT.py to pick it from /data/container/TaskWorker/log and add to message sent
- [x] make panel in Grafana

## Comment (belforte, 2023-04-21T12:44:50Z)

Done and now in master branch
