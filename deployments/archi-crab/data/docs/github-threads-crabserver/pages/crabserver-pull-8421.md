# dmwm/CRABServer pull request #8421: Release pipeline

State: closed
Opened: 2024-05-21T13:32:09Z
Closed: 2024-05-27T09:20:09Z
Merged: 2024-05-27T09:20:09Z
URL: https://github.com/dmwm/CRABServer/pull/8421

## Opening post (novicecpp, 2024-05-21T13:32:09Z)

Complete the https://github.com/dmwm/CRABServer/issues/8401

The release pipeline is based on [build-deploy-test](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/pipelines/build-deploy-test.html) pipeline but has 2 more stages:
- `prepare_release`: changing the version number in source files.
- `tagging_release`: tagging docker images with the release name.

The git tag name must match `v3\.[0-9]{6}.*` regex in order to trigger above jobs.
The final docker image tag, `RELEASE_NAME`, will be `v3.YYMMDD-stable` as we agreed in the issue.

This change also allow to do force release by pushing the git tag name same as above condition (the convention is `v3.YYMMDD__somestring`), provides `RELEASE_NAME=final-tag-name-including-stable` and `SKIP_DEPLOY=t` variable to CI.

## Comment (cmsdmwmbot, 2024-05-21T13:33:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1993/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-05-21T13:58:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1994/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-21T17:55:41Z)

I tried to look. But can't understand what the code does. Nor can I really understand the instructions. This is possibly too terse

>This change also allow to do force release by pushing the git tag name same as above condition (the convention is v3.YYMMDD__somestring), provides RELEASE_NAME=final-tag-name-including-stable and SKIP_DEPLOY=t variable to CI.

## Comment (novicecpp, 2024-05-22T11:22:25Z)

This will be long explanation. Please bear with me.

2 things we rely on: 
1. We use the pushing tag (`git push <remote> <tag>`) as the way to trigger the pipeline.
2. The release flow will be the same as we do now; go to the release page in GH and create a new release. From there, we use the tools to sync the release tag to Gitlab and trigger Gitlab CI.
  
(The second mechanism is still not yet finalized, but we can simulate it by simply **pushing** the tag with the same name as the release tag, directly to Gitlab to trigger the pipeline.)

"To trigger the pipeline" in this context means CI selecting the jobs in the `.gitlab-ci.yml` where the `rules` directive of the jobs are satisfied. Then, puts these jobs together and creates a pipeline to run. The rules for `if` directive is test against the CI variables defined each trigger. If the rule does not match, next rule will be evaluate. If no job matches the conditions, no pipeline will be run.

Reading the rule is a bit tricky here because Gitlab offered the yaml tag `!reference` as the way to reference the rule defined in hidden keys.

For example, job `get_env` at [L26-L27](https://github.com/dmwm/CRABServer/blob/068530f45109e7efcd78b1c1eafba3b624c9fe1b/.gitlab-ci.yml#L26-L27) define the rule as:

```yaml
get_env:
  rules:
    - !reference [.default_rules, default]
```

And the key `.default_rules` we define in here is:
```yaml
.default_rules:
  default:
    - if: $CI_COMMIT_TAG =~ /pypi-.*/
    - if: $CI_COMMIT_TAG =~ /v3\.[0-9]{6}.*/ 
```

Make `get_env` equivalent to:
```yaml
get_env:
  rules:
    - if: $CI_COMMIT_TAG =~ /pypi-.*/         
    - if: $CI_COMMIT_TAG =~ /v3\.[0-9]{6}.*/  
```

This rule means to run this job only when `$CI_COMMIT_TAG` matches the regex `pypi-.*`, OR `v3\.[0-9]{6}.*`. 

For `$CI_COMMIT_TAG`, this variable is only available when pushing the tag.

Here is the base "Build-Deploy-Test" pipeline which use the `.default_rules:default`:

![320979971-67321507-67ff-4d62-98a6-0ba484b21d3a](https://github.com/dmwm/CRABServer/assets/2346664/96f7500a-7863-4b4e-a841-b19f8e06c768)

Here is the "Release Pipeline" of this PR which some jobs only have `.default_rules:release` rules ([#7420156](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7420156)):

![Screenshot from 2024-05-22 11-29-00](https://github.com/dmwm/CRABServer/assets/2346664/1b474515-f8ec-4712-aed9-d1f0eb945a51)

In some cases, you want to run only some jobs, not all-or-none. One way you can do this is to let users provide some variables and add rules to explicitly not trigger the job. In our case, we want to skip the testing part to release the new image immediately. 

For example, `deploy_server` job:

```yaml
deploy_server:
  rules:
    - if: $SKIP_DEPLOY
      when: never
    - !reference [.default_rules, rules]
```

Which mean, if `$SKIP_DEPLOY` is exist, do not run the `deploy_server`. If not, checking next rule.

Here is the pipeline when `$SKIP_DEPLOY` is defined ([#7401218](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7401218)):

![Screenshot from 2024-05-22 13-24-32](https://github.com/dmwm/CRABServer/assets/2346664/0ba0aeb9-12e1-4242-86eb-3d90a5b9c36e)

You can supply any variable to the pipeline each for trigger, by providing the [push option](https://docs.gitlab.com/ee/user/project/push_options.html#push-options-for-gitlab-cicd) `ci.variables=VARIABLE_NAME=value` when pushing the tag.

The `$RELEASE_NAME` is generated from [parseEnv.sh](https://github.com/dmwm/CRABServer/blob/068530f45109e7efcd78b1c1eafba3b624c9fe1b/cicd/gitlab/parseEnv.sh#L23) in the [get\_env](https://github.com/dmwm/CRABServer/blob/068530f45109e7efcd78b1c1eafba3b624c9fe1b/.gitlab-ci.yml#L25) job which simply appends the `-stage` to `$CI_COMMIT_TAG`, and will be used to re-tag docker image later in the [release\_stable](https://github.com/dmwm/CRABServer/blob/068530f45109e7efcd78b1c1eafba3b624c9fe1b/.gitlab-ci.yml#L216) job. However, to trigger the pipeline from the same commit again, you need the different git tag. Different tag mean different release image tag too. So, `$RELEASE_NAME=tagname` allows you to override the final image tag to whatever you want. 

For example, push the tag with name `v3.YYMMDD__manual1`, and push variable `$RELEASE_NAME=v3.YYMMDD-stable` to have final docker image tag `v3.YYMMDD-stable`, and `SKIP_DEPLOY=t` to skip all testing steps.


(The code need some updates to make it more clear, will do it tomorrow).

## Comment (belforte, 2024-05-22T12:46:11Z)

hmm.. something like this ?
```
cd to my R/W clone of .... what's the gitlab repo name ?
(git clone ssh://git@gitlab.cern.ch:7999/crab3/CRABServer.git  ? )
git checkout master
git tag v3.240601__manual1
git push -o RELEASE_NAME=v3.240601-stable -o SKIP_DEPLOY=t 
```
forgive me, I never used `git` to create tags, always did it via the web i/i in github, i.e. direction on upstream.

I am sorry but I can't possibly try to review and understand the code. I am sticking with "have instructions which I can follow" and then will test those.

## Comment (novicecpp, 2024-05-23T04:38:47Z)

Ok. 

And Sorry for make explanation too long. The correct commands should be:
```
cd path/to/your/usual/forked/CRABServer
git remote add gitlab ssh://git@gitlab.cern.ch:7999/crab3/CRABServer.git 
git checkout master # make sure you build the release from master
git tag v3.240601__manual1
git push gitlab v3.240601__manual1 -o ci.variable="RELEASE_NAME=v3.240601-stable" -o ci.variable="SKIP_DEPLOY=t"
```

EDITED: fix `git push` command.

## Comment (novicecpp, 2024-05-23T04:58:36Z)

Hmm, look like it is easily to make a mistake when you forget to checkout master/v3.YYMMDD before tag.

Maybe trigger pipeline via Gitlab API is better, so you do not need to re-tag it. It is a bit inconvenient because you need separate credential (token API) in your machine instead using ssh/git mechanism to authenticate.

I will have a look later.

## Comment (cmsdmwmbot, 2024-05-23T06:26:39Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1996/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-05-23T06:44:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1997/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-23T08:37:22Z)

Do we need a client-side API with tokens etc ? Or could this be done on the gitlab web ui ?

Maybe it should be a multistep action ?
1. tag and push  v3.240601__manual1
2. wait for build and validation
3. push release name

btw, what's the bad side of forgetting to tag locally before pushing ? is that something that can be (easily) corrected in case ?

## Comment (novicecpp, 2024-05-27T09:19:19Z)

> btw, what's the bad side of forgetting to tag locally before pushing ? is that something that can be (easily) corrected in case ?

Let imagine when you are in hurry and you want to release master immediately. 
You go to your local CRABServer directory, current branch is not master because you are testing new multiprocess feature, let call `my-multiprocessor`, then you tag, and you push to gitlab. 
The tag you push is actually from latest commit of your branch `my-multiprocessor`, so pipeline build your commit instead of from `master`. 

This kind of situation I would like to avoid.

For how we trigger the pipeline to force release, push options is how I "hack" to force pipeline to run. I would like to start from "what should it be" first. But let talk about this in the issue.

## Comment (belforte, 2024-05-27T09:41:53Z)

thanks, now I understand
> Hmm, look like it is easily to make a mistake when you forget to checkout master/v3.YYMMDD before tag.

and  I agree with the concern
