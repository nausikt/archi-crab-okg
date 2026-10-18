# dmwm/CRABServer issue #8677: Merge crab rest, log pipeline, and serviceaccount manifests together in single helm chart

State: closed
Opened: 2024-08-30T12:42:04Z
Closed: 2025-01-28T18:08:10Z
URL: https://github.com/dmwm/CRABServer/issues/8677

## Opening post (novicecpp, 2024-08-30T12:42:04Z)

I would like to commit the new serviceaccount for CI to [CMSKuberentes](https://github.com/dmwm/CMSKubernetes) but I do not know where to put it. Also, the crab's logstash manifests [is in different place](https://github.com/dmwm/CMSKubernetes/blob/master/kubernetes/cmsweb/monitoring/crab/logstash.conf).

After discuss with @arooshap, she suggested to put everything together in single helm chart, `helm/crabserver`, and use value flags to render specific resources groups.

We have 3 resource group:

- [crabserver](https://github.com/dmwm/CMSKubernetes/blob/master/helm/crabserver/templates/deployment.yaml) manifest for crab rest.
- log pipline, which have logstash and crab's filebeat.
- [new CI serviceaccount](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/variables.html#testbed-cluster) that need cluster admin permission. 

For example, the `values-testX.yaml` only for render `crabserver`-related manifests:
```
environment: "test"
enabled: true
image:
  tag: "pypi-test12-manual1"
```

To render log pipeline and CI serviceaccount (e.g., `values-admin.yaml`), the value file will look like this:
```
environment: "preprod"
enabled: false
logPipeline:
  enabled: true
ciServiceAccount:
  enabled: true
```

This will be easier for cluster admin to maintain all our services. 
And for us, we only need to focus on modifying the `crabserver` resourec group, e.g., adding a new canary deployment.

## Comment (novicecpp, 2024-08-30T12:53:03Z)

@belforte @aspiringmind-code I would like to hear your comment about a new `config` directory structure. 

- `config/{test,preprod,prod}/config.py` for rest config `config.py` (move from `crab-secrets/kuberentes`)
- `config/{test,preprod,prod}/logstash.conf` for logstash config

Here is the full directory structure:

```
[thanayut@localhost beautify]$ tree .
.
├── Chart.yaml
├── config
│   ├── preprod
│   │   ├── config.py
│   │   └── logstash
│   │       ├── logstash.conf
│   │       └── logstash.yml
│   └── test
│       ├── config.py
│       └── logstash
│           ├── logstash.conf
│           └── logstash.yml
├── deploy.sh
├── README.md
├── scripts
│   └── setup.sh
├── templates
│   ├── ci-serviceaccount-rbac.yaml
│   ├── ci-serviceaccount-secret.yaml
│   ├── ci-serviceaccount.yaml
│   ├── configMap.yaml
│   ├── deployment-canary.yaml
│   ├── deployment.yaml
│   ├── filebeat-configmap.yaml
│   ├── filebeat-daemonset.yaml
│   ├── _helpers.tpl
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── logstash-configmap.yaml
│   ├── logstash-deployment.yaml
│   ├── logstash-service.yaml
│   ├── serviceaccount.yaml
│   └── service.yaml
├── values-canary.yaml
├── values-genall.yaml
├── values-logpipeline.yaml
├── values-prod.yaml
├── values-test11.yaml
├── values-test12.yaml
├── values-test14.yaml
├── values-test2.yaml
├── values-testbed.yaml
└── values.yaml

8 directories, 38 files
```

What do you think?

## Comment (novicecpp, 2024-08-30T12:59:00Z)

You can view these files in my fork here: https://github.com/novicecpp/CMSKubernetes/tree/crab_canary/helm/crabserver

## Comment (belforte, 2024-08-30T13:55:53Z)

I like it

## Comment (novicecpp, 2024-10-31T16:21:00Z)

This is done, merge to CMSKubernetes, and documents.

## Comment (novicecpp, 2024-10-31T16:27:56Z)

Sorry. I need to keep this open because it does not deploy on production yet.

test (at least test12) and preprod are now use new helm chart.

## Comment (nausikt, 2025-01-27T10:36:52Z)

@novicecpp Hi Wa, We've activated the canary using your new Helm chart template and have learned a lot from it. Since all the the initiatives and work done came from you, Could you kindly do us the honor of closing this issue for us? Thanks!

## Comment (nausikt, 2025-01-28T18:08:10Z)

Closed by @novicecpp
