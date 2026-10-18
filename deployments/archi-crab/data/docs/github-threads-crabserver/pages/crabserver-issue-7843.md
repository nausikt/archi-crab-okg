# dmwm/CRABServer issue #7843: crabserver rest - use helm charts to deploy it

State: closed
Opened: 2023-08-19T13:23:39Z
Closed: 2024-08-23T09:57:04Z
Labels: Priority: Medium, Status: In Progress, Area: CI/CD, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7843

## Opening post (mapellidario, 2023-08-19T13:23:39Z)

At the moment, we use kubernetes manifest files to deploy crabserver rest [1].

However, the CMSWEB team wants to migrate the deployment of the services to use helm charts [2].

Which actions are required from us?

- [x] test helm charts on a cmsweb-testN cluster. Dario did on cmsweb-test11 and everything seems ok so far.
- [x] write brief documentation on how to deploy and operate the crabserver via the `helm` cli, instead of plain `kubectl`. Dario can do this anytime.
- [x] test helm charts on preprod. Dario prefers to do this under Aroosha's supervision
- [x] can we avoid using `helm` cli? shall we look for an alternative of `imagebot`, so that we can deploy crabserver from a jenkins job? Shall we look into github actions? This is not compulsory, it would just be a "nice to have"
- [x] use helm charts on prod. We do not have a timescale so far.

---

[1] https://github.com/dmwm/CMSKubernetes/blob/master/kubernetes/cmsweb/services/crabserver.yaml
[2] https://github.com/dmwm/CMSKubernetes/tree/master/helm/crabserver

## Comment (belforte, 2024-02-28T11:17:06Z)

question now is:
 * how to deploy and track different versions in different clusters so that e.g. `helm list` or `helm history` are useful

We have:
 - chart version (used by GH atuomatic build tool to decide that a char has changed and rebuild)
 - appVersion inside chart (just informative for us)
 - image tag in the `values` file (indicates the tag of the docker container)

only the first 2 are shown by `helm list` and `helm history` . To see the deployed tag we need `kubectl get deployment`

## Comment (novicecpp, 2024-03-28T12:37:35Z)

Following the brief discussion before the end of the weekly meeting, here is my proposal for helm:

**Using helm as configuration template.**

That means, we use helm to generate manifests from templates only, similar to `helm template crabserver . -f values.yaml | kubectl apply -f -`.

We throw away the chart version and appVersion, but it can replace with,

- To track the version/history, do rollbacks, etc., we use git feature to revert changes and apply them again (`kubectl rollout` also should work).
- To see the live info using usual `kubectl`.
    

Why? Because for CD tools like ArgoCD never apply manifest as helm. It use helm to generate the manifests, apply them to k8s, and then track the objects directly.
For the user, when we move to ArgoCD, we will never use `helm install/upgrade` but learn how ArgoCD works instead.

Each environment has its own value file; the common values file is `values.yaml` and the values file for the environment is `values-<k8s-cluster-name>.yaml`.
Our crabserver in helm directory will look like this: 

```
crabserver/
├── Chart.yaml
├── templates
│   ├── ...
│   ├── deployment-deamonset.yaml
│   ├── deployment.yaml
│   ├── _helpers.tpl
│   └── ...
├── values-test12.yaml
├── values-test2.yaml
├── values-testbed.yaml
└── values.yaml
```

We apply helm with `helm template crabserver . -f values.yaml -f values-test12.yaml | kubectl apply -f -` (example for `test12`, rightmost `-f` has the highest precedence.)

About imagebot, as we know it does not compatible with helm. I propose to drop the imagebot and use serviceaccount credential to run kubectl/helm directly from CI jobs.

-------------------

So first step should be: make it work with manually apply for all environment. Then, we will make it work on Jenkins.

Here are the action items:
- [x] Ensure helm template crabserver . -f values.yaml | kubectl apply -f - is working in all environments.
- [x] Separate multiple environments into individual values files.
- [x] Set up crab's serviceaccount with a minimum rbac to access non-prod cluster.
- ~~[ ] Clone Deploy_TW and modify it to deploy the helm chart.~~

Note that my knowledge about helm is very limited. I never use it except to generate manifests from upstream charts.
If you have better practice or if there is a new helm feature that can benefit us, feel free to leave a comment.

## Comment (mapellidario, 2024-08-23T09:57:04Z)

This is done! :)
