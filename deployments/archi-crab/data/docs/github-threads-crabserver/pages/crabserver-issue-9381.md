# dmwm/CRABServer issue #9381: Storm of oracle connections problem caused by fds spike on CRABServer

State: open
Opened: 2026-08-10T11:51:37Z
URL: https://github.com/dmwm/CRABServer/issues/9381

## Opening post (nausikt, 2026-08-10T11:51:37Z)

Stefano reported that CRAB REST Server had a small storm of oracle connection problems and we got 5 min of timeout (HTTP 408). [1]

Nothing in common among 4 crashed pods they live in difference k8s nodes.[2,3] So it's not about hypervisor degradation issue. 
Indicate more a generic problem with our heavy query or an abusive submissions.

Need to investigate in detail since this start to be recurring and severe enough to cause time out.

[1]
<img width="738" height="1048" alt="Image" src="https://github.com/user-attachments/assets/04bca492-dbc6-4ab8-b799-d8b5c9b907ae" />

[2]
<img width="384" height="468" alt="Image" src="https://github.com/user-attachments/assets/abdc2218-3e50-446d-8995-ae8c146a23d2" />

[3]
```
crabserver-55fd4f78b8-5k5gs         1/1     Running     0              17d     10.100.192.239   cmsweb-k8s-prodsrv-zone-b-m4-2b2nguwnjv4w-node-3
crabserver-55fd4f78b8-cqbns         1/1     Running     0              17d     10.100.186.204   cmsweb-k8s-prodsrv-zone-b-m4-2b2nguwnjv4w-node-0   <none>
crabserver-55fd4f78b8-ph69f         1/1     Running     0              17d     10.100.186.195   cmsweb-k8s-prodsrv-zone-b-m4-2b2nguwnjv4w-node-0
crabserver-55fd4f78b8-pxqsp         1/1     Running     0              17d     10.100.82.61     cmsweb-k8s-prodsrv-zone-b-m4-2b2nguwnjv4w-node-1
```

## Comment (belforte, 2026-08-10T12:20:20Z)

Given that we already spent > 1y trying to understand and fix the root cause of those FileDescriptions/DBconnections surges.... I do not think that we have much hopes to find a better solution as long as the current probes restart the pods and revive the service.

Nor would it make sense to put a lot of work on this unless problems becomes much more serious. The only thing which comes to mind is to investigate if there's a way for K8s probes to kick-in and restart pods sooner. Current probes only acts when HTTP queries fail, detecting FD ramp may be better.
