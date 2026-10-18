# dmwm/CRABServer issue #9188: Shift to ArgoCD + Helm PRs, update crabserver chart, hands pointers.

State: closed
Opened: 2025-09-17T17:00:20Z
Closed: 2026-06-02T13:36:53Z
Labels: Area: zK8s, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/9188

## Opening post (nausikt, 2025-09-17T17:00:20Z)

There's **2 PRs** here for **2 different concerns**, would like you guys @belforte @aspiringmind-code  to review.
- [x] First PR: [Refactored CRABServer helm chart for Argo CD monorepo-style and CI/CD](https://github.com/dmwm/CMSKubernetes/pull/1661) [1]
- [x] Second PR: `Do-not-merge`, example of pointer manifests, [crab-argocd-application-pointers-for-testx-preprod](https://github.com/dmwm/CMSKubernetes/compare/master...nausikt:CMSKubernetes:crab-argocd-application-pointers-for-testx-preprod) [2]

### Concern #1, Update CRABServer Chart
1. Re-organized, clean-up cross-cutting components (e.g. ingress, filebeat, logstash, ... etc) to eliminated risks of conflicts between apps & platform pointers.
2. Better how we handle deltas as `values-<env>`, their corresponding `default values` and also reduced obscured if-else-conditional such that overall our chart are more intuitive, required less devOperators's cognitive load to comprehend in future, and clearer layering / deltas. 
** There's too many *never* been used `values` that Wa's kindly try to accommodated devOps, clusterAdmin but with current direction its better been deprecated, keep it tidy,
** debugging things can moved to our own forked, workbench (crab-k8s-overlays).
** cluster-admin, log-pipeline should be deprecated (e.g.  better provisioning from centralized to avoids pointers conflicts, from both resources, ownership perspectives)
3. Support directly customize config.py via chart values, such that it easy for us to test configMap while we developing (we can edited `config.py` in `crab-k8s-overlays` repo right away).

This PR are quite straightforward and can be safely merged, since it got tested e2e via CI/CD pipeline, everything wired together and work well.

### Concern #2, Hands CRAB specific pointers to CMSWeb
***Rationales:*** We need to pointed to our dedicated hot values repo, `crab-k8s-overlays`. because we don't want our CI/CD, bots, or us to bug/flooding upstream repo with commits/PRs. (Other team like WMCore, pointed to Dario's forked, P&R also have private gitlab repo overall approach almost identical to us for their `unified` and they use mixtures of kustomize + helm, helm chart also lies in their private gitlab repo, neatly done by Hassan Ahmed)
** Our approach will always treat `dmwm/CMSKubernetes` as our **Single source of Truth** for manifest templating via helm chart, where any changes need PRs. Hot values changes will not bugging as PRs/commits at all, and totally be our control in `crab-k8s-overlays`.

CMSWeb expert will be requested by us to do at least 2 things.
1. Let `CMSWeb`'s argocd recognize our private gitlab repo, `crab-k8s-overlays` with `GITLAB_PROJECT_ACCESS_TOKEN`, name `cmsweb-argocd-crab-pointers` with `read_repository`, expired on `Sep 17, 2026`. that could retrieved [here](https://gitlab.cern.ch/crab3/crab-k8s-overlays/-/settings/access_tokens?page=1)
```
argocd repo add https://gitlab.cern.ch/crab3/crab-k8s-overlays.git \
  --username oauth2 \
  --password $GITLAB_PROJECT_ACCESS_TOKEN
```

2. Apply CRAB's [applicationset](https://github.com/dmwm/CMSKubernetes/compare/master...sinonkt:CMSKubernetes:crab-argocd-application-pointers-for-testx-preprod#diff-72f3e49ff5866630e60d3098873191ea1b1d1dbaebcbe90b6f2831fe2f942b9f). such that `testX`, `preprod` start deployed via `https://gitlab.cern.ch/crab3/crab-k8s-overlays.git`, and CI/CD starting working there too.
This step easiest to be done via `kubectl` below.
```
kubectl apply -n argocd -f argo/apps/crab/applicationset
```
BUT, some details need to be checked from CMSWEB side like do CMSWEB allowed us to do this on `preprod`? otherwise it should be commented out, also in this manifest have `project-crab` assigned to this manifest, kind of safety lock, pointer isolation that could be modified to fit `CMSWeb` context, practices.
```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: crab-svcs
  namespace: argocd
spec:
  generators:
    - list:
        elements:
          # ---------- test2 cluster ----------
          - { svc: crabserver, env: test, cluster: test2 }
          # ---------- test12 cluster ----------
          - { svc: crabserver, env: test, cluster: test12 }
          # ---------- test14 cluster ----------
          - { svc: crabserver, env: test, cluster: test14 }
          # ---------- preprod cluster ----------
          - { svc: crabserver, env: preprod, cluster: preprod }
  template:
    metadata:
      name: '{{svc}}-{{cluster}}'             # e.g., crabserver-test2
      labels:
        team: crab
        env: '{{env}}'
    spec:
      project: project-crab
      sources:
        - repoURL: https://gitlab.cern.ch/crab3/crab-k8s-overlays.git
          targetRevision: master
          path: vendor/helm/crabserver
          helm:
            valueFiles:
              - values.yaml
              - values-{{env}}.yaml
              - $hot/helm/crabserver/values-{{cluster}}.yaml
        - repoURL: https://gitlab.cern.ch/crab3/crab-k8s-overlays.git
          targetRevision: master
          ref: hot
      destination:
        name: cmsweb-{{cluster}}
        namespace: crab
      syncPolicy:
        automated: { prune: false, selfHeal: true }
        syncOptions: [ CreateNamespace=true ]

```

### Optional stuffs, better not pursuit now
[1] apply project, and parents pointer (app-of-apps, pointer-of-pointers) for crab namespace. so it automatically keep tracking of CRAB's `applicationset` above. ** that could be put to upstream repo for more transparency, tracking, version-control, easier to rollbacking/reverting...
```
kubectl apply -n argocd -f argo/projects/project-crab.yaml   # <---- resources isolation and safety lock.
kubectl apply -n argocd -f argo/apps/ns-crab.yaml                 # <---- pointer-of-pointers
```
[2] If `CRABServer` helm chart was serving on `helm chart registry` OR CMSWeb Multi-Tenant ArgoCD've been upgraded to `latest` version ArgoCD ApplicationSet Controller.  We can define our pointers with more effective `applicationset` schema and thus we no longer have to relied on `vendir` synchronization, this could be discussed in some of our meeting later. but at the moment, just 2 mandatory requested are sufficient.

## Comment (nausikt, 2025-10-27T15:27:18Z)

@belforte, let me write final groks details down here.

I've tested finalized Grok patterns on `prod` logs [1,2], they work well and will be as following. 

- [x] we will no longer extract pod_name from log file path for these 2 log types.
- [x] preserved future-proof optional ephemeral ports (mostly occurs in dev/test env.)
- [x] add ` - Podname=%{DATA:pod_name} Type=%{WORD:log_type}$` for both log types for pod_name availability.
- [x] rename attr from `total` -> `proc` to better represent its value.  

### Grok #1, main `crabhttpcall` (basic http, metrics) lines.
Grok,
```
\[%{NOTSPACE:timestamp_temp}\] %{DATA:backend} %{IPORHOST:clientip}(|:%{NUMBER}) "%{WORD:method} %{NOTSPACE:request} %{DATA:httpversion}" %{NUMBER:code:int} %{DATA} \[data: (-|%{NUMBER:bytes_sent:int}) in (-|%{NUMBER:bytes_received:int}) out (-|%{NUMBER:time_spent_ms:int}) us \] \[auth: %{DATA} "%{DATA:dn}".*\] \[ref: "%{DATA}.*" "%{DATA:client}" \] - Podname=%{DATA:pod_name} Type=%{WORD:log_type}$
```
[1] tested that they were matched identical lines to the prev grok one.
```bash
========== Processing: ./test/logs/canary.0.log ==========
========== Summary ==========
[OK] Total of 1677 lines were matched.
[FAIL] Total of 23739 lines were failed.
========== Preview, matched of ./test/logs/canary.0.log ==========
[OK] line 1: {'timestamp_temp': '16/Oct/2025:16:29:26', 'backend': 'crabserver-canary-5655cf459f-bmsmp', 'clientip': '188.185.89.202', 'method': 'PUT', 'request': '/crabserver/prod/fileusertransfers', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 2255, 'bytes_received': 36, 'time_spent_ms': 6436, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=__REDACTED__CN=__REDACTED__/CN=__REDACTED__', 'client': 'CRABSchedd/v3.250820', 'pod_name': 'crabserver-canary-5655cf459f-bmsmp', 'log_type': 'cherrypylog'}
========== Processing: ./test/logs/primary.0.log ==========
========== Summary ==========
[OK] Total of 771 lines were matched.
[FAIL] Total of 11526 lines were failed.
========== Preview, matched of ./test/logs/primary.0.log ==========
[OK] line 15: {'timestamp_temp': '16/Oct/2025:17:07:04', 'backend': 'crabserver-66d49b5bd-wd8gw', 'clientip': '188.185.101.116', 'method': 'PUT', 'request': '/crabserver/prod/filemetadata', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 2406, 'bytes_received': 66, 'time_spent_ms': 5013, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=__REDACTED__/CN=__REDACTED__/CN=__REDACTED__', 'client': 'CRABSchedd/v3.251002', 'pod_name': 'crabserver-66d49b5bd-wd8gw', 'log_type': 'cherrypylog'}
```

### Grok #2, around `crabrest` calls lines.
Grok:
```bash
%{TIMESTAMP_ISO8601:timestamp_temp}:%{NOTSPACE:trace_id}:%{NOTSPACE:log_level}:%{NOTSPACE}:MeasureTime:seconds - modulename=%{NOTSPACE:modulename} label='%{NOTSPACE:label}' tot=%{NUMBER:tot:float} proc=%{NUMBER:proc:float} thread=%{NUMBER:thread:float} - Podname=%{DATA:pod_name} Type=%{WORD:log_type}$
```
[2] tested that they were matched identical lines to the prev grok one.
```bash
========== Processing: ./test/logs/canary.0.log ==========
========== Summary ==========
[OK] Total of 2771 lines were matched.
[FAIL] Total of 22645 lines were failed.
========== Preview, matched of ./test/logs/canary.0.log ==========
[OK] line 12: {'timestamp_temp': '2025-10-16 16:29:26,637', 'trace_id': 'XDirpysjmBaQ', 'log_level': 'INFO', 'modulename': 'CRABInterface.RESTBaseAPI', 'label': 'RESTBaseAPI.execute', 'tot': 0.0003, 'proc': 0.0001, 'thread': 0.0001, 'pod_name': 'crabserver-canary-5655cf459f-bmsmp', 'log_type': 'crablog'}
========== Processing: ./test/logs/primary.0.log ==========
========== Summary ==========
[OK] Total of 1431 lines were matched.
[FAIL] Total of 10866 lines were failed.
========== Preview, matched of ./test/logs/primary.0.log ==========
[OK] line 9: {'timestamp_temp': '2025-10-16 17:07:04,253', 'trace_id': 'SQEsjzoLrwle', 'log_level': 'INFO', 'modulename': 'CRABInterface.RESTBaseAPI', 'label': 'RESTBaseAPI.execute', 'tot': 0.0004, 'proc': 0.0001, 'thread': 0.0001, 'pod_name': 'crabserver-66d49b5bd-wd8gw', 'log_type': 'crablog'}
```
_____

Other than that, the upstream PR, will also included CRAB helm chart configHash aware feature, thus ArgoCD will also automatically triggered relevant deployment rollout for us.

### To-Do list, deployment/daemonset <-> configmaps awareness:
- [x] crab-specific
- [x] filebeat, logstash

## Comment (nausikt, 2025-12-01T12:07:53Z)

Now, CRAB helm chart was merged in upstream CMSKubernetes master, https://github.com/dmwm/CMSKubernetes/pull/1661

I will proceeding to do PoC around Solution 5 (`branch-topology`) on my own forked repo https://github.com/nausikt/CMSKubernetes/

This way "things need to be done" will transparent to everyone, thus we can hand details instructions/checklist on how to properly impose branch-protection rulesets covered S5. we can even live with this S5 for a while on our end first, by allow me to use ArgoCD Control plane on `test12` -- pointing to --> just `test2,test12,test14`. 

OR we could also fall back to multi-repo S4 approaches (that already been done) to avoid risk of giving away write-access token for the whole repo.

## Comment (nausikt, 2026-03-09T15:29:29Z)

I've restored our ArgoCD deployments for **test2, test12, test14 and preprod** while respecting the more restricted permissions granted to the **crab-gitlab-ci** service account, safe from resources conflicts.
*P.S. Back then it could touch ConfigMap & DaemonSet but currently it cannot. also can't get/list most API groups. which make sense as the service account name implied for just CI-purpose only not CD.*
*P.S. But, we're fine to utilize **crab-gitlab-ci** for Gitlab pipeline configuring.*

So right now,  we are utilizing test12/14 ArgoCD Control plane, which used to be provisioned by CMSWEB operator, and **crab-gitlab-ci** service account for full-CI/CD-integration testing before switching. [1] 

## Remaining items (before full switching):
- [x] 1. live with this ArgoCD for a week till O&C Week, verifying protection-rules.
*I will reach out to Andrea in-person and may work on the same screen to do [2,3].* 
- [x] 2. configure `dmwm/CMSKubernetes` to have proper `protection-rules` to master.
- [x] 3. generate (write) PAT for CRAB's Gitlab CI on `dmwm/CMSKubernetes` side, installed deploy key.
*verifying by manually pushing/merging into crab branch.*
- [x] 4. https://github.com/dmwm/CRABServer/pull/9279
- [x] 5. switch [nausikt/CMSKubernetes#crab](https://github.com/nausikt/CMSKubernetes/tree/crab) to [dmwm/CMSKubernetes#crab](https://github.com/dmwm/CMSKubernetes/tree/crab) via PR.
*also hands our pointers to CMSWEB ArgoCD control plane, where CD permissions are right.*

[1] Now, *only* **Deployments** and **Services** were syncing during full e2e intregation testing.
```bash
❯ argocd app list
NAME                       CLUSTER         NAMESPACE  PROJECT       STATUS  HEALTH   SYNCPOLICY  CONDITIONS  REPO                                          PATH                   TARGET
argocd/crabserver-preprod  cmsweb-preprod  crab       project-crab  Synced  Healthy  Auto        <none>      https://github.com/nausikt/CMSKubernetes.git  helm/crabserver        crab
argocd/crabserver-test12   cmsweb-test12   crab       project-crab  Synced  Healthy  Auto        <none>      https://github.com/nausikt/CMSKubernetes.git  helm/crabserver        crab
argocd/crabserver-test14   cmsweb-test14   crab       project-crab  Synced  Healthy  Auto        <none>      https://github.com/nausikt/CMSKubernetes.git  helm/crabserver        crab
argocd/crabserver-test2    cmsweb-test2    crab       project-crab  Synced  Healthy  Auto        <none>      https://github.com/nausikt/CMSKubernetes.git  helm/crabserver        crab
argocd/ns-crab             in-cluster      argocd     project-ops   Synced  Healthy  Auto        <none>      https://github.com/nausikt/CMSKubernetes.git  argocd/argo/apps/crab  crab
```

## Comment (nausikt, 2026-03-18T10:01:36Z)

We need to configure/ensure `dmwm/CMSKubernetes` have Rulesets that not allow force push, PR-gated on every branches except `crab` there's 2 steps as follows:
*See also test and full [Protect Master ruleset in action at nausikt/CMSKubernetes](https://github.com/nausikt/CMSKubernetes/settings/rules/14008397)* [3]

## [1] Configure Rulesets
**Branch Target** 
*Includes Pattern*
- [x] `master`
- [ ] `*`
- [ ] Or explicitly allows crucial branches e.g. `releases/**/*`, `features/**/*`

*Excludes Pattern*
- [x] `crab` or `crabserver` (in upstream)

**Branch rules**
- [x] Restrict deletions
- [x] Require linear history
- [x] Require a pull request before merging (at least 1 reviewer)
- [x] Block force pushes


## [2] Deploy Keys
- [x] Krittin hands public key of ***crabserver-gitlab-ci***, ssh PKI `dmwm.cmskubernetes.crab-gitlab-ci.deploy`) to Andrea. 
- [x] Krittin has returned admin access to Andrea.

[3] when we got blocked and unblocked at `nausikt/CMSKubernetes#crab` branch. See also [pipeline test](https://gitlab.cern.ch/crab3/CRABServer/-/jobs/71619006)
*with expected `Changes must be made through a pull request.` msg.*
<img width="1286" height="863" alt="Image" src="https://github.com/user-attachments/assets/e41f1937-f1ed-42b6-8876-e1dd209eccaf" />

## Comment (nausikt, 2026-04-07T10:08:41Z)

We should change our deploy keys to use a more sophisticated algorithm than the current **id_ed25519** one. (Once added we may rarely changed, so better used some thing more secure)

Encrypt it in crab-secrets repo -> try CI/CD deploy with my forked once again -> then should be very mindful before made any rule-sets changes with temporary admin access on real upstream production CMSKubernetes.

## Comment (nausikt, 2026-04-10T12:37:56Z)

The newly re-generated deploy key with new knobs works well and has been tested on my `nausikt/CMSKubernetes`.

I think we quite confident with the branch rule-sets and deploy key approach. our gitlab CI can mess with only `crab` [1]

[1] we can't push/write to `master` or any other `branch` except `crab`.
<img width="994" height="432" alt="Image" src="https://github.com/user-attachments/assets/f2bbb4e3-440e-4785-9a55-31a843607479" />

## Comment (nausikt, 2026-04-10T13:23:31Z)

Its turned out, there's a lot of experimental branches in `upstream/CMSKubernetes`.
<img width="804" height="383" alt="Image" src="https://github.com/user-attachments/assets/c4e7f5e5-d6d4-49dd-946f-7a5b0cefc582" />

I've come to think that the most appropriate final approach, w/o blocking other, would be to just protect `master` from `us` (our deploy key) and allow us (`crabserver` branch) be able to force push in advance. Done.

## Comment (nausikt, 2026-04-10T14:03:12Z)

From https://github.com/dmwm/CRABServer/issues/9188#issuecomment-4024615388

We've done pretty much everything except the real switching at CMSWEB ArgoCD control plane.

*Here's the very last mile, to-do/check list!*
##  Last Mile, Check List:
- [x] 1. sync `dmwm/CMSKubernetes#crabserver` so that it is up to date and reflects the currently running tags/configs. https://github.com/dmwm/CMSKubernetes/pull/1694, Ticket: [CMSKUBERNETES-348](https://its.cern.ch/jira/browse/CMSKUBERNETES-348).
- [x] 2. after [1] merged, ask Aroosha/Que for another PR approval merging from `dmwm/CMSKubernetes` `master` -> `crabserver`
- [x] 3. turn-off `cmsweb-test12` local ArgoCD control plane that we use for testing.
- [x] 4. ask Aroosha/Que for `crabserver` activation in `non-prod` envs. 
*(targeting the `dmwm/CMSKubernetes#crabserver` branch.)*
- [x] 5. configure gitlab CI to switch from `nausikt/CMSKubernetes#crab` to `dmwm/CMSKubernetes#crabserver` along with the corresponding PKI key.
## For Production
- [x] 6. ask Aroosha/Que for `prod` activation point to `dmwm/CMSKubernetes#master` helm: announce a 30-mins intervention, switching and monitoring together. Bump Image [PR#1696](https://github.com/dmwm/CMSKubernetes/pull/1696) then [CMSKUBERNETES-362](https://its.cern.ch/jira/browse/CMSKUBERNETES-362)

## Comment (nausikt, 2026-06-01T11:15:42Z)

Update on [6], we created ticket [CMSKUBERNETES-362](https://its.cern.ch/jira/browse/CMSKUBERNETES-362), note that the switching is transparent to the users thus announcement is unnecessary.

## Comment (nausikt, 2026-06-02T13:36:53Z)

Thanks to Que & Aroosha! longstanding support & initiative, we're DONE with the shift!
