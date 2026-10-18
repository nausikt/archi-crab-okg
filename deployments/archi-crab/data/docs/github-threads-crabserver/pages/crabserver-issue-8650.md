# dmwm/CRABServer issue #8650: Canary deployments - REST, TW, Publisher

State: closed
Opened: 2024-08-26T15:03:29Z
Closed: 2025-02-27T10:41:00Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8650

## Opening post (mapellidario, 2024-08-26T15:03:29Z)

## introduction

We have always dreamed about processing a small portion of production crab tasks with a new crab version.

We do not have a general solution, each crab system will need to be adapted in a very specific way.

### REST

This requires no change in the code, but requires some experience with k8s deployments. The idea is:

- create a new deployment in `dmwm/CMSKubernetes/helm/crabserver/templates`, call it `crabserver-canary`.
    - change only `metadata.name: crabserver-canary`, do **not** change for example `metadata.labels.app: crabserver` nor `spec.selector.matchLabels.app: crabserver`
- create a new values file `dmwm/CMSKubernetes/helm/crabserver/values-canary.yaml`
- change [deploy.sh](https://github.com/dmwm/CMSKubernetes/blob/master/helm/crabserver/deploy.sh)  to accept `canary` as an argument, you will need to edit the `cluster_map`.
    - otherwise simply use `helm template crabserver . -f values.yaml -f values-${1}.yaml | kubectl -n crab apply -f -`, but beware to be connected with the proper context (username+cluster)! 

### TaskWorker

This requires some change in the code, that have been outlined in https://github.com/dmwm/CRABServer/wiki/TaskWorker-Canary-Deployment

we decided that we run one TW per virtual machine, so that the hostname is enough to identify which TW process/container we are referring to.

### Publisher

This is not defined yet, but we have some ideas. The simplest one is

- run a publisher on every VM where we run TW
- make sure that a single publisher only select jobs that have been submitted by tasks processed by the TW running on the same VM
    - need to add tm_twname to filetransfersdb table or pick it up from task table using a join on taskname. In any case need to change the SQL which picks the files to work on.

## Comment (belforte, 2024-08-26T15:39:35Z)

I believe that we agreed that @novicecpp will do the K8s part together with @aspiringmind-code 

I am still un-decided if it is better to call it crabserver-canary or crabserver-qa

## Comment (belforte, 2024-08-26T15:40:24Z)

NOTE: it will be important to be able to tell (easily) the canary pod from the others in our monitoring, e.g. quickly tell where HTTP errors come from

## Comment (novicecpp, 2024-08-28T13:32:17Z)

![Screenshot from 2024-08-28 15-33-38](https://github.com/user-attachments/assets/7f0456c6-113e-4c12-a2d8-676d2e44551a)

Look promising.
https://monit-grafana.cern.ch/goto/3JXSKT3Ig?orgId=11

EDIT: new image to contains pod name.

## Comment (belforte, 2024-08-30T14:43:40Z)

better split off TW+Publisher to a different issue #8678

## Comment (novicecpp, 2024-09-13T11:12:28Z)

To-do:
- [x] Waiting https://github.com/dmwm/CRABServer/issues/8677 to close
- [x] Deploy https://github.com/dmwm/CMSKubernetes/pull/1545 on production
- [ ] Test it on production (same image tag) to verify dashboard.

## Comment (novicecpp, 2024-10-31T16:22:50Z)

~~Sorry. I need to keep this open because it does not deploy on production yet.~~

~~test (at least test12) and preprod are now use new helm chart.~~

## Comment (belforte, 2024-10-31T16:24:23Z)

@aspiringmind-code will do it :-)

## Comment (novicecpp, 2024-10-31T16:27:37Z)

Sorry, wrong issue.

This one I tested myself on my test12 and preprod, and it works.
But you may need to modify dashboard a bit to make it more easier to see metrics between `crabserver` and `crabserver-canary`.

## Comment (belforte, 2024-10-31T16:37:36Z)

I knew that it works, but AFAIK it is not deployed in production, not used, not monitored. We have not even deployed latest CRABServer tag there. Plenty of useful work to do !

## Comment (aspiringmind-code, 2024-11-21T10:59:27Z)

For Canary TW deployment, I envision changes made in commits [here](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/50bcf9c09de545602d5c376be9772fc9b4f55c04) and [here](https://github.com/aspiringmind-code/CRABServer/commit/1495c280201a5f21cc9888fb0763c2de382a420e) @belforte let me know if you agree with this approach. Thanks!

## Comment (belforte, 2024-11-21T11:09:57Z)

thanks @aspiringmind-code  changes to TW are not trivial, let's create an ad-hoc issue

## Comment (belforte, 2024-12-06T13:55:30Z)

time to look at REST #8859

## Comment (aspiringmind-code, 2025-02-27T10:41:00Z)

TW and REST done. Publisher decided not needed.
