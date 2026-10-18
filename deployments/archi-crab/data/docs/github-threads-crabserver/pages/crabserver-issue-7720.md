# dmwm/CRABServer issue #7720: create grafana alert if DBSDataDiscover takes too long

State: closed
Opened: 2023-07-07T13:45:52Z
Closed: 2024-05-24T16:04:47Z
Labels: Priority: Medium, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7720

## Opening post (belforte, 2023-07-07T13:45:52Z)

we could have noticed earlier the recent "one DBS pod hung" problem by noticeing that all/most DBS queries were taking long time.
One simple way on our side is to look at DBSDataDiscovery:
![image](https://github.com/dmwm/CRABServer/assets/1837785/ad5938ac-b23c-4695-a643-01681202ad64)


FYI @novicecpp

## Comment (mapellidario, 2024-05-24T16:04:47Z)

I added an alert rule [1] from this panel [2]. It will send a message to mattermost if DBSDataDiscovery takes at least 200s every time for six hours hours, no data should not trigger an alert. 

I will close this issue

[1] https://monit-grafana.cern.ch/alerting/grafana/e700ea70-8d06-44c4-bf57-07a3229cf74b/view?returnTo=%2Fd%2FMNg7eZF4z%2Fcrab-alerts%3ForgId%3D11%26viewPanel%3D139%26editPanel%3D139%26showCategory%3DRepeat%2520options%26tab%3Dalert
[2] https://monit-grafana.cern.ch/goto/gs5at8PSg?orgId=11
