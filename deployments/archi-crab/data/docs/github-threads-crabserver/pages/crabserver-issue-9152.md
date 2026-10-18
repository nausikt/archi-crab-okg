# dmwm/CRABServer issue #9152: migrate to ArgoCD

State: closed
Opened: 2025-08-18T15:41:09Z
Closed: 2025-09-15T09:14:39Z
Labels: Area: zK8s, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/9152

## Opening post (nausikt, 2025-08-18T15:41:09Z)

Ciao @belforte @aspiringmind-code,

Guys, please, allow me to kick start ArgoCD migration via this following Draft below.

## Prelude

ArgoCD embraces declarative & GitOps principles: a single source of truth about infrastructure stored in Git, human/PR-gated reviews, operational transparency, built-in version control, and make it easier to maintain, roll back and forth, and fully own our deployment operations through commits and PRs—kind of *decommissioning* direct `kubectl` commands.
> Think of ArgoCD as a Puppet agent for Kubernetes—similar in how they have their own agent, polling for VM configs from repo but ArgoCD was tailored for K8s. 
(P.S. And of course! there's subtle differences!)

In our case, we already have such a monorepo (dmwm/CMSKubernetes).
But since this repo serves multiple teams, we must address some challenges unique to the shared ownership.

### Key Considerations & Challenges
1. **Shared Monorepo trade-offs**: great for common infra, and CMSWeb we **do have** *common ground*, but less ideal when teams need autonomy and frequent iteration.
2. **PR noise** : when to use PR-gated (human-reviewed) vs Bot-commits.
     > e.g. our CRAB team alone have 3 DevOps pushing test tags twice daily → ~144 PRs/month flooding github `dmwm/CMSKubernetes`, even if auto-merged.

### Proposed Solution
**In short  [P1]**:
1. **PR-gated:** for **preprod/prod** and the *base* of **dev/test** manifests remain in GitHub `dmwm/CMSKubernetes`.
2. **Bot-commits:** for *Hot* **dev/test** desired state (*patches/overlays*) moves to a kind of minimal sidecar repo. (e.g. possibly name **crab3/crab-iac** in GitLab).
     > This gives us autonomy for frequent updates. **where**
         1.) Still inherits and respects the base from CMSKubernetes.
         2.) Transparency preserved—most code still remains in the shared monorepo.
         We configure ArgoCD pointng to this, our *team-desired-state* repo, where Bot-commits update hot desired state (tags from crab3/CRABServer pipelines).
         ** P.S. other Possible sidecar repo names: **crab-dev-iac**, **crab-k8s-infra**, **crab-devtest-infra**, ...etc.

**Otherwise  [P2]**:
> *If sticking to mono repo is something we strongly wish to preserve.*

We would need to kindly ask CMSKubernetes maintainers to adopt **branch-based dev/test overlays** with **CODEOWNERS**, so our bot-commits could write directly into them.

## To-Do List
- [x] Deploy ArgoCD in test14.
- [x] Implement `kustomize` + `vendir` in gitlab `crab-iac` (sidecar) repo, re-organize things current overlays github `sinonkt/CMSKubernetes`.
 > ArgoCD + Helm is an alternative one, we could do extensive comparison later, **BUT** Since, kustomize are quite intuitive (*no* lots of templates, which a bit hard to comprehend, *IMO*) just plains k8s manifest yaml, have base/overlays concepts, patches on overlays fashions that are highly suitable for large multi-IaC projects that share common ground across team, and among each team envs as CMS. Thus why CMSWeb team choose kustomize approach as default.
- [x] Enable Bot-commits workflow in *test14*.
- [x] Integrate Bot-commits with current GitLab CI/CD (**crab3/CRABServer**).
- [x] Generalize overlays for *test2*, *test12*.
- [x] Team (Stefano, Vijay, Krittin) start using *test2*, *test12*, *test14*.
- [x] Apply *PR-gated* model in **preprod** (development work on fork **sinonkt/CMSKubernetes**).
- [ ] Add mandatory pipeline checks before merge (syntax, conformance, smoke tests, policy checks).
> In other words, anywhere/time before we merge, we MUST trigger manifests syntax validations & checking, like kube conformity, in prod, we also might/good-to have to verify against share policies and some smoke tests. 
** some pipelines have to be done on our side, some should be integrated to CMSKubernetes in general. **

- [ ] Adopt **CODEOWNERS** rules per overlay dir → enforce path-specific ownership.
- [x] Team starts living with *preprod* PR-gated, encounter defects → refine -> iterate.
- [ ] Simplify CRABServerAuth secrets (consider multi-env consolidation/generalization if possible).
> as Stefano mentioned in the meeting last week.

- [ ] Integrate ArgoCD Secrets handling (SOPS + GPG plugin first; later explore alternatives).
- [ ] Adopt new ArgoCD-based secrets handling in `test2`, `test12`, `test14` and `preprod`.
- [ ] Apply all **lessons learned** to `prod` and `canary`, Switching from **[P1]** to **[P2]** could be made here at this stage, we will discuss again later...

Edited:
Guys, Please, let me know your thoughts and feels free to comments along the way. I thought of making tutorials and walkthrough around these if you guys would like. This issue will be main Source of Truth for migrating ArgoCD. An input interface for gathering feedbacks, converging to our Team need/convention.

## Comment (nausikt, 2025-08-18T15:43:28Z)

2025 Goals in **Q3**, ArgoCD for our K8s applications in #8879

## Comment (belforte, 2025-08-18T16:06:07Z)

I added values for priority/days so that it shows in the [Workplan](https://github.com/orgs/dmwm/projects/14/views/8)
Feel free to change them

## Comment (nausikt, 2025-09-02T09:32:09Z)

@belforte @aspiringmind-code Hi, Guys, I've found workaround over current layout and its works now.
How do you guys feel about we start adopting to your test2, test12?

P.S. There shouldn’t be any noticeable difference when using core CI/CD pipelines.

## Comment (belforte, 2025-09-02T09:38:07Z)

can you indicate how it will work w/o the pipeline ? If I simply want to change what I am running in test2, which steps will be needed ? E.g. I may  want to change what I run in REST w/o changing TW. I can do the other way by using `runContainer.sh`.
Shall we start tomorrow's meeting 30min earlier and keep 30min at the end for a walk-through of the new procedure ?

## Comment (nausikt, 2025-09-02T09:40:32Z)

> can you indicate how it will work w/o the pipeline ? If I simply want to change what I am running in test2, which steps will be needed ? E.g. I may want to change what I run in REST w/o changing TW. I can do the other way by using `runContainer.sh`. Shall we start tomorrow's meeting 30min earlier and keep 30min at the end for a walk-through of the new procedure ?

Acknowledge your use case, Stefano. Yes, 30-mins earlier works for me.

## Comment (nausikt, 2025-09-04T10:24:09Z)

Hi @belforte, regarding configmap update.

The only action we need is:
1. commit updated config.py at base. [here](https://github.com/sinonkt/CMSKubernetes/commit/fa11e5c726d1ce47c5addf249aafa943a071e586)


Then, it will propagates to all `test/dev` (also `preprod`, `prod` when activated) clusters, with the same suffix hash (reflected versioning by content changed) as you can see below.

```
test2❯ k get configmap -n crab
NAME                    DATA   AGE
crabserver-75f547d48t   2      13m
```
```
test12❯ k get configmap -n crab
NAME                    DATA   AGE
crabserver-75f547d48t   2      13m
```
```
test14❯ k get configmap -n crab
NAME                    DATA   AGE
crabserver-75f547d48t   2      14m
```

## Comment (belforte, 2025-09-04T11:10:46Z)

OK. And we will still be able to have different config in different clusters for testing and incremental deployment, right ? Could this extend to different config for canary ?

By the way: we need to stop using your fork of CMSKubernetes.

## Comment (nausikt, 2025-09-04T11:13:55Z)

> OK. And we will still be able to have different config in different clusters for testing and incremental deployment, right ? Could this extend to different config for canary ?
> 
> By the way: we need to stop using your fork of CMSKubernetes.

Yes it could, it will be override patches for each overlays (including canary) with this same current setting, we have to added additional patches which could be done on either `crab3/crab-iac-overlays-sidecar` or `upstream/CMSKubernetes`.

## Comment (nausikt, 2025-09-04T11:15:22Z)

@belforte @aspiringmind-code

Guys, `test2`, `test12` also in argoCD hands now, with bot-committing a new deployment from our core CI/CD pipeline at side-car repo.

Overall, your development experiences should be the same.

**Except**
1. when you wish for manually bumping the image, or adding anything (that changes frequently) or very specific to your local dev env.
-> we can do it by update patched image in sidecar repo here: [crab3/crab-k8s-overlays](https://gitlab.cern.ch/crab3/crab-k8s-overlays)
2. when you would like to changes base's things e.g. configmap, deployment.
-> We can open PR to upstream dmwm/CMSKubernetes. (but during migration we will stick to my [forked repo]([https://github.com/dmwm/CMSKubernetes/compare/master...sinonkt:CMSKubernetes:migrate-to-argocd) just for now).

## Comment (belforte, 2025-09-04T11:29:45Z)

please take the time to start a new "instruction for ArgoCD" section for this in https://cmscrab.docs.cern.ch/crab-components/crab-rest/deploy.html which will of course evolve

## Comment (nausikt, 2025-09-04T15:27:09Z)

> please take the time to start a new "instruction for ArgoCD" section for this in https://cmscrab.docs.cern.ch/crab-components/crab-rest/deploy.html which will of course evolve

Acknowledge Stefano. Guys, i've renamed repo to `crab-k8s-overlays`, as you guys voted, e2e was tested on `test2`, `test12`, `test14`, they were welcoming new naming!

## Comment (nausikt, 2025-09-08T12:29:43Z)

Guys, `testX`, `preprod` is now fully managed by ArgoCD [1,2] and integrated with our core CI/CD pipeline via bot-commits as you can see [here](https://gitlab.cern.ch/crab3/crab-k8s-overlays/-/commits/master?ref_type=heads) in `crab-k8s-overlays`. 

There should be no noticeable impact to your development/releasing workflow. 

P.S. for pipeline testing results could be seen here by use cases: [normal](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12841421) | [stable-releasing](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12841502)
P.S. will proceeding to secret handling and `prod`, also `canary` on `prod`

[1]
<img width="668" height="718" alt="Image" src="https://github.com/user-attachments/assets/7bf16355-a7f0-4c94-8f52-98854056bc97" />

[2]
<img width="1175" height="262" alt="Image" src="https://github.com/user-attachments/assets/df6e7aaf-c69d-42d8-be6e-2c732c9f0ae1" />

## Comment (nausikt, 2025-09-09T12:28:51Z)

Guys, Due to the latest strong trends shifting towards `Argo+Helm` in upstream/CMSKubernetes, instead of `Kustomize-First` approach back then.

IMO, I love this latest CMSWeb vision a lot, in trading Kustomize readability for long-term operability. 

Now, `platform` things, e.g. cross-cutting, shared components got started to be helmified. 

Thus, `Helm` will likely be the one who layering env layouts via clean & clear values.yaml diffs act as deltas/patches in `kustomize` land, This also means current kustomize overlays layouts on upstream/CMSKubernetess will considered to be redundant and likely/better been deprecated. 
(** Since, majority of components both in `apps` land and `platform` land are already been helmified, including CRAB by Wa, all dmwm's svcs by Dario, ... etc.)

CRAB better converging to latest CMSWEB's vision for seamless integration by made `Helm`-compatible adaptation such that, CRAB flexible to also incorporate this unified deployment approach or `kustomize` & `helm` hybrid approach.

The `crab-k8s-overlays` are already agnostic to `Helm` or `Kustomize`-styles for addressing hot desired manifests use-cases where we would like low-PR-noises, autonomous workspace repo to do automation. Thus, drop-in replacement of new `helm` values and minor re-organizing overlays should be sufficient.

Which means our current `testX`, `preprod` `dev/releasing` workflow experience should remain the same.

### ArgoCD + Helm Adaptation To-Do List
- [x] clean-up e.g. ingress, ci-serviceaccount-*. (remove cross-cutting / cluster-admins things out of crab helm chart concerns, which likely been centrally provisioning & owned by CMSWEB core/platform team soon).
- [x] clean-up filebeat, logstash in our CRAB helm, we better use upstream/third-party/vendor helm registry (Strong use-cases for `helm`) which easier for ops to maintain/ugprade/evolving via community-driven chart rather than maintain our own manifests, unnecessary introducing more knobs (complexity) in CRABServer Helm Chart.
- [x] revise some aspect of CRAB Helm chart.
- [x] scatter CRABServer, Filebeat, Logstash's `values-X.yaml` diffs specific to each envs, adjusted to be appropriated to `crab-k8s-overlays` workspaces, friendly to devs.  
- [ ] adapt our ApplicationSet, to be flexible for pointing to new `ArgoCD+Helm`-style layering.
---------

After finished these list, I think we good to consult with Aroosha w/o bothering her much. Hopefully, we could help her at least putting a small CRAB's jigsaw in `apps` land and also/maybe our pointers into the whole picture that might good for her in progressing to start testing things in `apps` land on `testX` and `preprod`. 
(** She might already been overwhelmed by cross-cutting components a lot where much more intricates, concerns and criticalities than `apps` during these recent & upcoming weeks, so we better minimize our (my) annoyances more. ToT)

## Comment (belforte, 2025-09-09T13:19:55Z)

we try to swin in the same direction as the other fish in the river... If you love this, we will surely be happy as well.
As I don't understand nor helm nor kustomize, I can't comment on the To-Do list. I trust your judgement.

## Comment (belforte, 2025-09-09T15:40:27Z)

I asked Aroosha for an example, her it is:

I have an example from cmsweb-test11 cluster that Dario documented  https://cms-wmcore.docs.cern.ch/deployment/WMCore-in-kubernetes/#deploy-wmcore-services-with-argocd . So it is as simple as just specifying the values file in the ArgoCD file, the rest of the templating is done by Helm Charts. I deployed ArgoCD for Krittin in cmsweb-test14 so it should be very straight forward .

I had  quick look and it looks reasonably easy.

## Comment (nausikt, 2025-09-15T09:14:39Z)

> I asked Aroosha for an example, her it is:
> 
> I have an example from cmsweb-test11 cluster that Dario documented https://cms-wmcore.docs.cern.ch/deployment/WMCore-in-kubernetes/#deploy-wmcore-services-with-argocd . So it is as simple as just specifying the values file in the ArgoCD file, the rest of the templating is done by Helm Charts. I deployed ArgoCD for Krittin in cmsweb-test14 so it should be very straight forward .
> 
> I had quick look and it looks reasonably easy.

Thank you Stefano, now CRAB converged to CMSWeb & DMWM conventions on my forked, but we still left with last mile issue where we need to make it compatible with our CI/CD on some kind of `dev` branch of `shared` CMS  gitlab repo. I will open new issue dedicated to these.

The Secret handling need to have a lot more discussions and finalized by CMSWeb & DMWM team, we better waiting and converging later when things settled. I'm fine with manually update secret during this time.
