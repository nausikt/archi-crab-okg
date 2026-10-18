# dmwm/CRABServer issue #8971: TW v3.250227 does not set CRAB_Retry classAd

State: closed
Opened: 2025-03-10T15:37:49Z
Closed: 2025-03-10T16:32:40Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8971

## Opening post (belforte, 2025-03-10T15:37:49Z)

HAmmerCloud monitoring relies on CRAB_Retry, so it spotted a problem with canary TW which runs  https://github.com/dmwm/CRABServer/releases/tag/v3.250227.1

```console
belforte@vocms0106/~> condor_q -con 'jobuniverse==5&&jobstatus==2' -af crab_retry crab_taskworker|sort|uniq -c|sort -n|tail
     19 1 crab-prod-tw01
     27 18 crab-prod-tw01
     34 14 crab-prod-tw01
     46 17 crab-prod-tw01
     50 2 crab-prod-tw01
     59 16 crab-prod-tw01
     75 15 crab-prod-tw01
    292 3 crab-prod-tw01
   1472 0 crab-prod-tw01
   1912 undefined crab-prod-tw02
belforte@vocms0106/~>
```

## Comment (belforte, 2025-03-10T15:47:30Z)

a `MY.` is trivially missing here
https://github.com/dmwm/CRABServer/blob/3fbd21a2a1408eb9ac989dde77dee913f41a514e/src/python/TaskWorker/Actions/PreJob.py#L238
