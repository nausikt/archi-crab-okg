# dmwm/CRABServer issue #8307: Too many false potisive alerts on mattermost from grafana

State: closed
Opened: 2024-04-02T14:31:24Z
Closed: 2024-04-09T09:41:38Z
Labels: Area: MONIT, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8307

## Opening post (mapellidario, 2024-04-02T14:31:24Z)

We are receiving too many notifications on mattermost from grafana, for example [1].

From a quick googling session [2] it can be that we are making grafana query the data providers (prometheus, for example) too aggressively.

we have two options:

- [x] do not trigger an alert if a panel contains no data: should be simple to implement, will reduce false positives, but will likely miss some incidents.
- [x] reduce the frequency at which we check the value of a variable, 
    - [x] for example, we do not really need to evaluate every minute if any of our k8s pod has more than 50 open fds.

[1]

```plaintext
Value: [no value]
Labels:

    alertname = DatasourceError
    grafana_folder = CRAB Alerts Alerts - MNg7eZF4z
    rule_uid = ee1322c8-065d-4b14-a182-745da00317a7
    rulename = NUMBER OF RUNNING DAGMANS PER SCHEDD alert
```

[2] https://community.grafana.com/t/intermitent-alertname-datasourceerror/103872/6

## Comment (mapellidario, 2024-04-02T14:56:36Z)

So:

- [x] I reduced the evaluation time to 10min for every alert
- [x] I set "alert state if execution error or timeout" set "ok"  [1] 

result
- [x] all alerts in "CRAB Alerts Alerts - MNg7eZF4z" in [grafana](https://monit-grafana.cern.ch/alerting/list) are ok, not firing

let's see how the next week goes before marking this issue as solved.

--- 

[1]

![Screenshot_20240402_163907](https://github.com/dmwm/CRABServer/assets/16376695/c8a20955-34dd-410c-ba7e-3bc771b9c474)

## Comment (belforte, 2024-04-02T16:28:05Z)

why was this happening just now ?

## Comment (mapellidario, 2024-04-09T09:41:39Z)

> why was this happening just now ?

This is a mystery, it can be any combination of grafana, prometheus and opensearch changes. I think the situation improved and will close this issue. If the problem appears again I will open a new one
