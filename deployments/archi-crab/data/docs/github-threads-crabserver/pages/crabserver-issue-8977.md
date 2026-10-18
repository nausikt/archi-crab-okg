# dmwm/CRABServer issue #8977: refresh tnsnames.ora regarding CMSR Oracle service intervention

State: closed
Opened: 2025-03-11T17:17:23Z
Closed: 2025-03-14T14:08:19Z
URL: https://github.com/dmwm/CRABServer/issues/8977

## Opening post (nausikt, 2025-03-11T17:17:23Z)

To accomodate, Oracle Intervention.

Right now, *tnsnames.ora* was provisioned from `cmsweb` image as we can see [crabserver_pypi/Dockerfile#L23-L24](https://github.com/dmwm/CRABServer/blob/f42c47d75ee1a055e99294982477d5f8f8d2ad83/cicd/crabserver_pypi/Dockerfile#L23-L24). 

We've to either bumping `cmsweb` image to the latest one, `20250311` (Thanks! Aroosha!) which picking the new *tnsnames.ora* up for us.

OR we could go for separately mounted from k8s configmap by ourself like DBS does.
(which might make things less sensitive to the base image but also introduce more manual operation to keeps things up-to-date)

## Comment (nausikt, 2025-03-12T00:58:09Z)

Since, we still struggling with building new `cmsweb` image therefore we'll go for provisioning `tnsnames.ora` via configmap instead. Here is some deployment result that i've applied & tested in `prod` and `test12`.

*Before*: the `/etc/tnsnames.ora` was provisioned from `cmsweb` image since 27/04/2023.
```
> kubectl exec -it crabserver-845bd5b5bd-4z6zt -n crab -- cat /etc/tnsnames.ora
###
### CERN official tnsnames.ora file
...
##Generation date: Thursday, 27/04/2023 15:18
```

*After*: `tnsnames.ora` was updated by rolling out from new helm chart via `./deploy.sh prod` then `kubectl rollout restart deployment/crabserver -n crab` (explicitly rollout needed if we haven't changes image tag or any values related to deployment).
```
> kubectl exec -it crabserver-5f54555666-245bb -n crab -- cat /etc/tnsnames.ora
###
### CERN official tnsnames.ora file
...
##Generation date: Tuesday, 11/03/2025 11:04
```

## Comment (nausikt, 2025-03-12T08:40:49Z)

We've updated to the latest config one `##Generation date: Wednesday, 12/03/2025 06:10` this morning.

N.B. updating could be done atomically with `--dry-run` to generate yaml first then `kubectl apply -f -` (* not sure is it more safe than `delete then create` operation)
N.B. 2 rollout restart are necessary, since patching/swapping configmap alone doesn't refreshed `tnsnames.ora` inside running pod (as i've checking).
```
kubectl create configmap tnsnames-config -n crab --from-file=tnsnames.ora -o yaml --dry-run | kubectl apply -f -
kubectl rollout restart deployment/crabserver -n crab
```

## Comment (nausikt, 2025-03-14T14:08:19Z)

Noted about other solutions:
As Stefano pointed out vocms* might enable yum-cron? (May be not via puppet too) or any rhel package manager features that magically updates `tnsnames.ora` for everyone, specifically updating via `oracle-instantclient-tnsnames.ora` rpm package.

this also aligned with what i've seen in `tzero`'s [t0wmadatasvc](https://github.com/dmwm/CMSKubernetes/tree/master/docker/t0wmadatasvc) pod that also magically refreshed `tnsnames.ora` via rpm, without neither having to bumping pod to new release tag and rolling out new pod nor mounted new `tnsnames.ora` configmap from host.  (P.S. `tzero` configmap was extremly outdate)
