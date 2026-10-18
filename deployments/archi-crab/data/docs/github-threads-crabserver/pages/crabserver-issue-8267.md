# dmwm/CRABServer issue #8267: Pipeline for automatically test new pypi image

State: closed
Opened: 2024-02-29T15:27:53Z
Closed: 2024-06-24T11:17:27Z
Labels: Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8267

## Opening post (novicecpp, 2024-02-29T15:27:53Z)

Move from second part of https://github.com/dmwm/CRABServer/issues/8224

Requirements:

1. Automated everything, from code commits to reporting the test.
2. However, do not trigger build every time when committed.
    - In example, in feature branch, we do not want to deploy every time we push code there. Sometimes just want to save after finishing work.
    - Another example, test code is broken, it is a waste of time (and resources) to build it again.
3. Pipeline should deploy to proper environment.
    - We have 3 (private) dev environments. If Stefano's wants to test, it should pick the source from stefano's changes and run on dev/test2.


The fourth requirement is **to move CI to Gitlab** because:
- *Gitlab-CI is the platform I am familiar with.*
- Officially supported by CERN IT.
- Better practice than Jenkins (at least for the declarative part; everything is defined in `.gitlab-ci.yml`).
- I like the "Pipeline" concept.
    - You can use `CI_PIPELINE_ID` from the previous pipeline as a reference to get some cache/data. 
    - Retrying the failed jobs/pipeline is easy to do on the Web UI.   
    - Caching files between pipelines is easy to do. See [example](https://about.gitlab.com/blog/2022/09/12/a-visual-guide-to-gitlab-ci-caching/).
    - Dynamic pipeline generation, [see official docs](https://docs.gitlab.com/ee/ci/pipelines/downstream_pipelines.html#dynamic-child-pipelines).
- Runner (equivalent to Agent in Jenkins) is easy to deploy and manage. Basic executor (shell/docker/etc.) is ready to use in CERN Gitlab. 
- The practice in Gitlab is good enough to become an example to apply to another CI platform (not just Jenkins).

Of course, there are some limitations:
- Pipeline is bound to the repository. If we want multiple pipline, there are 2 workarounds:
    - Generate pipeline on the fly (Gitlab CI feature.)
    - Create a blank repo that contains only CI scripts.
- Job retry is limited to 3 times (enforced by CERN Gitlab admin), and we cannot do delay retry like we do in Jenkins (CheckTestResult job).
- You need to deploy Runner by yourself, at least to running Apptainer.
- Need some synchronization between Github and Gitlab.
- What about Github, like WMCore?
    - I personally never used it before, need to explore what is limitations and *cost*.

My grand plan is to use this CI as the pilot to build another CI on our wishlist in [#7958](https://github.com/dmwm/CRABServer/issues/7958).

## Comment (novicecpp, 2024-02-29T15:28:42Z)

Here is a technical overview. I split it into six parts:

- Flow (trigger & branch management)
- Pipeline
- Scripts
- Credentials
- Runner
- Synchronization between Github and Gitlab


**Flow**

This is the flow of CI I come up with:

- Dev push tags directly to their own forked CRABServer repository with a special format: `<cernusername>_<anytagname>`.
- We use `<cernusername>` deploy in the proper environment (dev/devtwo/devthree).
- Setup Github webhook to trigger Jenkins jobs to push tags to the Gitlab repo.
    - Point here is that we need to sync update code to Gitlab and trigger the pipeline to run.
    - See technical details in Synchronization between GitHub and Gitlab below.
- Pipeline started; use `<cernusername>` in the tag to determine which cluster needs to be deployed.
- The last pipeline stage will notify users of the results of the test suite.

**Pipeline**

Pipeline will have 4 stage: build -> deploy -> runtest -> checktest
- Build: Build docker image (currently use kaniko to build)
- Deploy: Deploy to Kubernetes cluster and VM (See *Credentials* section below on how we can authenticate with server).
- Runtest: Clone of [ExecuteTests-StatusTracking's jenkins job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/).
- CheckTest: Clone of [CheckTestResult's  jenkins job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/).

The details I will explain later when I have `.gitlab-ci.yml` files.

**Scripts**

The scripts are mostly taken from [testingScripts](https://github.com/dmwm/CRABServer/tree/master/test/container/testingScripts), plus some shell scripts we put in the Jenkins jobs. Modify it a bit to make it more suitable for the new CI.

These are the rules I enforce (to myself) while editing the scripts:
- Clone the CRABServer repo is done by the pre-job step; taking care by CI.
- When cloning WMCore or other repos or fetching files on the internet, the endpoint and version/hash should commit to the file inside the repo. Then read it at the build time to fetch it. With this and the above bullet, we can get rid of the step where we need to pass the arguments of the tag/branch manually.
- Make scripts more modular; do one job at a time. Most shell scripts in Jenkins jobs need to be fixed regarding this.
- Most importantly, scripts should be part of the repo. In case CI scripts need to be changed, we can commit changes together with the new feature code. CI always runs depending on the tag/branch that has the latest change. So fixing your own branch will not affect other people's branches (you have to reconcile with the master branch later, though).

**Credentials**

There are 4 credentials we need:
- [Build] `registry.cern.ch`: We can generate on harbor UI. 
- [Deploy] `ssh-key` to `crab-dev-tw` machine: One time generation, plus bypass 2fa in those machines.
- [Deploy] Kubernetes serviceaccount credential: to deploy CRAB REST. See ["Manually create an API token for a ServiceAccount"](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount).
- [Runtest/Checktest] CERN grid cert (`usercert.pem/userkey.pem`): We need the main cert in order to recreate the proxy. We can use one of our service accounts for this.

All credentials have now become `Variables` of `CI/CD` of gitlab repo. This is safe because:
- We do not allow (by default) forked repos to run the same CI resources and read the same variables.
- At least, only people who have gitlab access to this project (crab-operator + voc roles) can view pipelines and variables.

However, I need to verify this if I understand correctly.

**Runner**

`Runner` is equivalent to a Jenkins Agent, where it can spawn processes inside the machine.
`Executor` is the mode in which the Runner runs CI jobs.

We need 2 runners for each executor type:

1. Docker executor
Run jobs in a Docker container. For example, if we want to run kubectl, instead of installing it on the Runner machine, you only provide a custom Docker image, and the scripts (kubectl command) will run inside that container automatically.
This allows dev to have full control over the software needed in order to run CI jobs.

This executor is the same as `Kubernetes+executor` CERN IT (`Kubernetes+executor`, it is the same except running in container spawn inside kubernetes cluster).

2. Shell executor
Shell Executor is like running a shell natively on a machine. We need it to run `cmssw-el8`'s Apptainer (e.g., running `crab` command).
We use "Shell Executor," plus an extra wrapper, to run jobs inside Apptainer. 

I choose to maintain this runner myself in exchange for gaining control of node setup, but there is docker+machine executor provided by CERN that we can also use.

**Synchronization between Github and Gitlab**

Because our main repo is on Github. We push code to Github. But pushing the code on both platforms is a bit too much (or not?). It would be better if we push code to Github, then some automation synced the changes to Gitlab.

One limitation of Gitlab is that you cannot trigger pipelines from the autosync feature of Gitlab. We need to push to Gitlab manually in order to trigger the pipeline.

What I plan to do is:

- Setup Github webhook to trigger Jenkins jobs, like we have right now when we publish a new release in main repo.
    - Need to setup a webhook for each forked repo.
- In jenkins jobs, pull repo, fetch tag, push to Gitlab

An alternative way is to write a sync service that pulls Github every 30s and pushes to gitlab.

## Comment (novicecpp, 2024-04-09T19:41:25Z)

This is the guide for PR https://github.com/dmwm/CRABServer/pull/8328 

The pipeline does the build-deploy-test loop, where the "build" is building the new PyPI image and the "test" is executing the "status tracking" testsuite.

The CI contains 5 stages:

![Screenshot from 2024-04-08 14-53-58](https://github.com/dmwm/CRABServer/assets/2346664/67321507-67ff-4d62-98a6-0ba484b21d3a)

1. `prepare_env`: Prepare `.env` file for use across job in pipeline.
    The [parseEnv.sh](cicd/gitlab/parseEnv.sh) script parse the tag format `pypi-<env>-<name>` to get environment (see "Trigger" section below about triggering CI and tag format). Then, write appropriate environment variables to `.env`.
    `.env` is available for all jobs in the pipeline as pipeline artifacts (see [.gitlab-ci.yml#L30-33](https://github.com/novicecpp/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/.gitlab-ci.yml#L30-L33))
2. `build_docker`: Build container
    Build the containers from [cicd/crabserver_pypi](https://github.com/dmwm/CRABServer/tree/master/cicd/crabserver_pypi) and [cicd/crabtaskworker_pypi](https://github.com/dmwm/CRABServer/tree/master/cicd/crabserver_pypi) using kaniko. This kaniko is not different from [what CERN offer](https://gitlab.cern.ch/gitlabci-examples/build_docker_image/). It is just from the early days when I played with Gitlab-CI, it still works fine. We can migrate to CERN kaniko later.
3. `deploy`: Deploy REST and TaskWorker.
    - Deploy REST in K8s: Change the image to the image built by this pipeline, wait until the readiness test passes. This step does not apply the Helm template or any kube  manifests to reduce job complexity. Operators need to apply proper manifests before running the pipeline.
    - Deploy TW on the TW machine: use the script in Jenkins Job [CRABServer\_Deploy\_TW](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_Deploy_TW/configure) to deploy with `deployTW.sh` script.
4. `run_testsuite`: Submitting status tracking test suite.
    In general, `executeTests.sh` is the entrypoint of job to execute `taskSubmission.sh` inside appropriate cmssw container to run `crab` command. I have removed all Github bot code from scripts to simplify the code, plan to add back later. Please see `executeTests.sh` and  `taskSubmission.sh` source code in "Appendix 1" on how it works. 
5. `check_test_result`: check the test result submit by previous step.
   Same as step 4 `run_testsuite`, `executeStatusTracking.sh` is the entrypoint and `taskSubmission.sh` is real execution  which call `taskSubmission.py` later. The `executeStatusTracking.sh` is wrapped inside [retry.sh](https://github.com/novicecpp/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/cicd/gitlab/retry.sh) helper to emulate the retry machanism in Gitlab-CI (CERN gitlab retry is limit only 3 time).

#### Triggering

The pipeline is trigger only when push tag and the tag name should match regex `pypi-.*`. But, the legit tag we use in this pipeline is `^pypi-(devthree|preprod).*`, as defined in `VALIDATE_TAG` in [parseEnv.sh#L6](https://github.com/novicecpp/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/cicd/gitlab/parseEnv.sh#L6). I use this pattern to get environment name to create set of environment variables to use in deploy and test stages.

#### Helper scripts

1. [retry.sh](https://github.com/novicecpp/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/cicd/gitlab/retry.sh) is the retry wrapper which can replace by CI system when they have [deley retry](https://gitlab.com/gitlab-org/gitlab/-/issues/19231) feature like in the Jenkins. The script retry only callee script exit with code `4`, and controlled by `RETRY_MAX` (default: 10) and `RETRY_SLEEP_SECONDS` (default: 5mins). 
2. [credFile.sh](https://github.com/novicecpp/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/cicd/gitlab/credFile.sh) is for copy creds file from gitlab variable to working directory and change owner to CI user and mode to 0600. The script accept first arg as file path and print new absolute file path to stdout.

#### Variable (Credential)

(Note: setup these variables are not included in this document.)

We use CI variables (From WebUI, Setting -> CI/CD -> Variables) to set all secrets that are used in the jobs.

There are 6 CI variables that available for all job:

- `CMSCRAB_REGISTRY_URL`: CERN docker registry (Harbor) URL.
- `CMSCRAB_REGISTRY_USER`: Registry username.
- `CMSCRAB_REGISTRY_PASSWORD`: Registry password.
- `CRAB_TW_SSH_KEY`: ssh key to deploy on TW machine.
- `KUBECONFIG_FILE`: k8s client config, include credential to access k8s cluster.
- `X509_USER_PROXY`: Grid proxy certificate to use with `crab` command.

(Security) Attack surface: Only people who has access to crab3 group (cms-service-crab-operators) can access. (Need confirm) forked project cannot access variables nor project runners.

#### Practices

To make CI easy to debug later, I have enforce these rules while writing scripts:

1. With appropriate setup of cvmfs/voms/myproxy/container, all scripts must be able to run locally.
2. Always run script inside `$WORK_DIR` (default: `./workdir`, with some exception). This makes running the script on a local machine easy to clean up.
3. Following point 2, `$ROOT_DIR` is ALWAYS available when `$WORK_DIR` is defined, and always point to git root directory. This make script easy to call other script inside repo.
4. `$SCRIPT_DIR`, [one-liner to get script's location](https://stackoverflow.com/a/246128), is use when script want to call another script where it is the same level or sub directory. Use `$ROOT_DIR` instead when calling outside script's directory (e.g, use `${ROOT_DIR}/test/path-to/script.sh` instead of `../../test/path-to/another-script.sh`).
5. `set -euo pipefail` is a must. However, when source scripts in cvmfs we need to disable it because some scripts does not wrote with unbound variable or failure of pipe command in mind.

#### Run locally

I has separate scripts ([test\_executeTestsStatusTracking.sh](https://github.com/novicecpp/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/cicd/gitlab/st/test_executeTestsStatusTracking.sh), [test\_executeStatusTracking.sh](https://github.com/novicecpp/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/cicd/gitlab/st/test_executeStatusTracking.sh)) for test running CI job locally.

The content of script is clone from [.gitlab-ci.yml](https://github.com/novicecpp/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/.gitlab-ci.yml) file, simply to avoid call the scripts too many level. 

#### Appendix 1: Table of cloned scripts and its original

|                                                                                                                              |                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [deployTW.sh](https://github.com/novicecpp/CRABServer/blob/ci_gitlab_pypi/cicd/gitlab/deployTW.sh)                           | Jenkins Job [CRABServer_Deploy_TW](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_Deploy_TW/configure)                                                                                                      |
| [executeStatusTracking.sh](https://github.com/novicecpp/CRABServer/blob/ci_gitlab_pypi/cicd/gitlab/executeStatusTracking.sh) | Jenkins job [CRABServer_CheckTestResults](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/configure)                                                                                        |
| [executeTests.sh](https://github.com/novicecpp/CRABServer/blob/ci_gitlab_pypi/cicd/gitlab/executeTests.sh)                   | Jenkins job [CRABServer_ExecuteTests](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/configure)                                                                                                |
| [taskSubmission.sh](https://github.com/novicecpp/CRABServer/blob/ci_gitlab_pypi/cicd/gitlab/taskSubmission.sh)               | [test/container/testingScripts/taskSubmission.sh](https://github.com/dmwm/CRABServer/blob/5f3ab24a9f3544995d920610b84405d2d2b4dc3a/test/container/testingScripts/taskSubmission.sh)                             |
| [setupCRABClient.sh](https://github.com/novicecpp/CRABServer/blob/ci_gitlab_pypi/cicd/gitlab/setupCRABClient.sh)             | [test/container/testingScripts/setupCRABClient.sh](https://github.com/dmwm/CRABServer/blob/5f3ab24a9f3544995d920610b84405d2d2b4dc3a/test/container/testingScripts/setupCRABClient.sh)                           |
| [st/statusTracking.sh](https://github.com/novicecpp/CRABServer/blob/ci_gitlab_pypi/cicd/gitlab/st/statusTracking.sh)         | [test/container/testingScripts/TaskSubmissionStatusTracking.sh](https://github.com/dmwm/CRABServer/blob/5f3ab24a9f3544995d920610b84405d2d2b4dc3a/test/container/testingScripts/TaskSubmissionStatusTracking.sh) |
| [st/statusTracking.py](https://github.com/novicecpp/CRABServer/blob/ci_gitlab_pypi/cicd/gitlab/st/statusTracking.py)         | [test/container/testingScripts/statusTracking.py](https://github.com/dmwm/CRABServer/blob/5f3ab24a9f3544995d920610b84405d2d2b4dc3a/test/container/testingScripts/statusTracking.py)                             |

#### Appendix 2: CI Features for debugging

These feature are for debug CI only. To reduce time when waiting for docker build or tasks finish running.

1. If `MANUAL_CI_PIPELINE_ID` is specify, only `check_test_result` job is run. Simply to debug `executeStatusTracking.sh` and `retry.sh` scripts without submitting task again. 
    - This is possible by using [fallback cache key](https://docs.gitlab.com/ee/ci/caching/#use-a-fallback-cache-key). At [.gitlab-ci.yml#L159-L166](https://github.com/novicecpp/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/.gitlab-ci.yml#L159-L166), default is `$MANUAL_CI_PIPELINE_ID` then `$CI_PIPELINE_ID` then CI default to `submitted_tasks_TS_latest` where it same across all pipeline.
    - This is assume we run on specific branch/tag, not newly pushed tag.
    - Usage:
        - At WebUI menu -> Pipeline -> top right "Run pipeline" botton ([we can use API to trigger pipeline](https://docs.gitlab.com/ee/ci/triggers/), but later)
        - select branch/tag on `Run for branch name or tag` and paste `CI_PIPELINE_ID` from previous successfully submitted pipeline.
        - Hit "Run pipeline".
3. If `SUBMIT_STATUS_TRACKING` is non null, run `task_submission_status_tracking`  then
    - This is assume we run on specific branch/tag, not newly pushed tag. See usage in 1.    
4. If `$SKIP_BUILD`is not null, skip `build_docker` stage, to support manual provides tag name to deploy later.
5. If `$SKIP_DEPLOY`is not null, skip `deploy` stage (it should skip `build_docker` too, but later).

#### Appendix 3: Reference

- Getting start: https://docs.gitlab.com/ee/ci/pipelines/
- Job Artifact: https://docs.gitlab.com/ee/ci/jobs/job_artifacts.html
- Cache: https://about.gitlab.com/blog/2022/09/12/a-visual-guide-to-gitlab-ci-caching/
- Rules: https://docs.gitlab.com/ee/ci/jobs/job_control.html
- CI Variable: https://docs.gitlab.com/ee/ci/variables/predefined_variables.html
- Push Option: https://docs.gitlab.com/ee/user/project/push_options.html

## Comment (novicecpp, 2024-06-24T11:17:27Z)

This is done and the guide here is moved to [CRAB CI on Gitlab](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/index.html).
