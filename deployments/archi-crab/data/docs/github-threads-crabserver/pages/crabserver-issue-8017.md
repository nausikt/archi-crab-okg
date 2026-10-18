# dmwm/CRABServer issue #8017: CI for update kube secrets from crab-secrets repo

State: closed
Opened: 2023-11-20T17:09:11Z
Closed: 2025-10-16T11:54:58Z
Labels: Area: CI/CD, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8017

## Opening post (novicecpp, 2023-11-20T17:09:11Z)

Today, I have updated the credentials of CRAB REST to the cmsweb secrets system, which needs to manually sync secrets from our source-of-truth (`crab-secrets`) to the cmsweb system.
This process is error-prone because I need to make sure I update the correct files, put the secrets in the correct place, and update the correct upstream systems.
Ultimately, it is time-consuming to both ensure it works properly and fix it if it does not.

The automatic CI step will help us relieve these kinds of issues. 

The CI steps should be:
- Figure it out if the commit changing kube secrets files. Providing envs to next step.
- Apply secrets to all envs from output of previous step
  - Something like:
    - reading filename/env from previous step.
    - Apply to template files
    - execute `kubectl apply`
  - Make prod as manually trigger step.
- Testing if it work for all envs from first step
  - Either check 5xx from grafana or execute the testsuite.
- Apply change to cmsweb secrets system (omit detail of this part, will discuss privately).

One of CI "wishlist's" in https://github.com/dmwm/CRABServer/issues/7958

## Comment (nausikt, 2025-08-12T10:12:19Z)

@belforte Ciao Stefano, this is not urgent na Stefano, please no worries, i wrote this just for record.

Here's detailed write-up of [MR4](https://gitlab.cern.ch/crab3/crab-secrets/-/merge_requests/4)

CI steps implemented:
1. **Validate Changes** - this acts as a safe-guard for pipeline triggering. Every times we create a merge request or push a commit directly, it will check and collect only the allowed changed secret files for further downstream CI Jobs otherwise it will early terminated the pipeline.
2. **Re-encrypt Secrets** - this step will decrypt the changed secrets from our CRAB SOPS + GPG  setup, then encrypts them into the CMSWEB SOPS+GPG protocol in as atomic operation as possible, Sensitive debugging output is suppressed here. it then returns a list of `reencrypted_secret_files` and their corresponding envs as Artifacts for the downstream jobs.
3. **Open merge request**: this step copies the re-encrypted secrets into central `services_config`, check out a new branch, commits, pushes the changes, and then opens a merge request via the API from the new `update-test14-testX...-secrets` (`source_branch`) to `test` branch to `services_config`.
4. **Check MR Status** - We poll the merge request every minute for up to 1 hr, checking for either the "merged" or "closed" status; otherwise, it's terminated. we are not polling for few days as originally planned, since that would waste the CI-runner resources for nothing, So 1hr is enough for a quick review and merge, otherwise we retry this job for another 1 hr checking.
5. **Deploy** - Since the affected environments already known from upstream jobs, here we check out latest `services_confg` on the `test` branch and deploy only to the affected environments.

This pipeline currently works only on the forked repos (`kphornsi/crab-secrets` -> `kphornsi/services_configs`). after i get the green lights from you guys, I will switch to the real repos/secrets/configs ones. Thanks!

## Comment (nausikt, 2025-08-12T10:26:02Z)

### Things left to do
- [ ] Activate in origin repos.
- [x] more Tests step? if things really works on all affected envs after deployed by either check 5xx from grafana.
- [x] [Optional] more refining around `scripts/deploy-secrets.sh crab crabserver`?. 
- [x] [Optional] make prod as manually trigger step. (Right now we discard prod)

## Comment (nausikt, 2025-10-16T11:54:59Z)

Eventually, we didn't activated it in origin repos though.

I have done complete PoC around this imperative CI/CD styles and its works fine on my fork.

1. make a commit `kphornsi/crab-secrets`
2. kubectl apply secret directly to each cluster env
3. open MR to `kphornsi/services_config`
4. waiting for MR merged, otherwise failed.
5. done syncing live with origin.

But we preferred update k8s-secret manually though, because its worth waiting a bit converging to inuitive new ArgoCD style or any secret CI/CD pipeline on `origin/services_config` sometimes in next year.

this way we not confusing ourself twice, and eventually treat `services_config` as **Single source of Truth** for k8s-secrets.
