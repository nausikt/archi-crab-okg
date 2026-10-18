# dmwm/CRABServer issue #9225: Implement configHash to automatically trigger rollouts of relevant deployments via ArgoCD + Helm

State: closed
Opened: 2025-10-27T16:09:28Z
Closed: 2025-10-28T15:30:57Z
Labels: Type: Enhancement, Priority: Medium, Area: zK8s, Area: CI/CD, Area: zDesired Feature
URL: https://github.com/dmwm/CRABServer/issues/9225

## Opening post (nausikt, 2025-10-27T16:09:28Z)

From time to time,

We occasionally end up in a situation where the ConfigMap has already been updated, but the deployment has not been explicitly rolled out yet.
P.S. And sometimes its might took so long to realize these, like in my case #9221.
P.S. thus, why one of `Kustomize`'s killing feature, is to automatically update/trigger roll out via suffixing the configmap name, as default feature.  

Since, we go with ArgoCD + Helm, we better make this process automated as well, aware of ConfigMap content changes, via helm templating for each components in our CRABServer helm Chart.

P.S. Should we better included this update into Final Helm Chart update PR now? [dmwm/CMSKubernetes#PR1661](https://github.com/dmwm/CMSKubernetes/pull/1661), or later as seperated PR.
P.S. Continuation of updated Finalized Groks, https://github.com/dmwm/CRABServer/issues/9188#issuecomment-3451888006

## Comment (nausikt, 2025-10-28T15:30:57Z)

I've implemented https://github.com/dmwm/CMSKubernetes/pull/1661/commits/ec3d59aebd02deea9acde57f7140ad4cea4b1caf, tested and deployed on `preprod` for `crabserver` and `filebeat`.

Now, we have podAnnotations.`configHash` for each corresponding deployment/daemonset, that will be aware of content changes for us. as you can see in the following example [1]

This way, new DevOperator just have to change the config content -> ArgoCD + helm will patched configHash -> rollouts restart for us.

P.S. k8s is sensitive to any changes inside pod `template` thus this minimal implementations are sufficient for automatic triggering rollouts restart.
P.S. IMO, we don't have to overdo by suffixing the configMap name, where hotswap configmap and audit traceability are necessity/concern or have higher priority than simplicity. current implmentation are much clearer to me to see config diffs.

***Other Important Notes***: 
1. I'ven't implmented this feature for `Logstash`, `crab-secrets` yet (e.g. CRABServerAuth.py)  Since, we're on an on-going process of moving toward ***global*** logstash, So, we have to keep in mind that `logstash` will need manual rolling-out restart for now.   
2. In case of crab-secrets, since its `*.sops` not included in upstream helm chart. So, ArgoCD + Helm can't hashing it during rendering time, can't patched configHash for any changes happens in `services_config`.  So, another occasion to remind ourself for manually rollout.

[1] 
<img width="1216" height="539" alt="Image" src="https://github.com/user-attachments/assets/1992fb13-f9ac-49a0-9425-a880ebd16a27" />
