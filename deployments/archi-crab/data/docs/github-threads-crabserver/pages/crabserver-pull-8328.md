# dmwm/CRABServer pull request #8328: PoC CI pipeline on Gitlab to verify PyPI image

State: closed
Opened: 2024-04-09T19:38:18Z
Closed: 2024-04-18T13:30:26Z
Merged: 2024-04-18T13:30:26Z
URL: https://github.com/dmwm/CRABServer/pull/8328

## Opening post (novicecpp, 2024-04-09T19:38:18Z)

This PR is PoC of new CI systems on Gitlab. 
Please see explanation in https://github.com/dmwm/CRABServer/issues/8267#issuecomment-2045933223.

Final pipeline will look like this:
![Screenshot from 2024-04-08 14-53-58](https://github.com/dmwm/CRABServer/assets/2346664/67321507-67ff-4d62-98a6-0ba484b21d3a)

## Comment (cmsdmwmbot, 2024-04-09T19:43:32Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 8 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1933/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-04-11T20:12:06Z)

The pipeline is ready to review. 
@belforte @mapellidario if [the guide](https://github.com/dmwm/CRABServer/issues/8267#issuecomment-2045933223) is not enough for you and want another chat. Feel free to ping me.

## Comment (belforte, 2024-04-11T21:13:54Z)

sounds like I should hand over to you my highest priority issues, so I can put a couple of days on this !
Unfortunately at top of my list I have "troubles with publication in DBS" :-( or cleaning up use of HTCondor classAds

## Comment (belforte, 2024-04-14T17:03:38Z)

First of all, this is excellent documentation and very nice work.
Neat and terse, thank you ! Really professional.

Then, during previous chat I was focused on understanding "the spirit" now am trying to understand how it works, so have some questions due to my ignorance of those tools. Ideally we'd like to be in a situation where some can understand from the documentation enough to make changes.

* what is the purpose of `cicd/buildtools/Dockerfile` ?  I can't find where it is used
* with reference to the `build_docker` stage, where is `${CI_PROJECT_DIR}` defined ? And how does the GH code gets there ?
* I know nothing about kaniko, hopefully I can live for a while w/o it
* what does it do the line `  - !reference [.default_rules, rules]` in the `gitlab-ci.yml` ?
* what is `name: registry.cern.ch/cmscrab/buildtools` ? Something I am not familiar with becasue it is part of the pypi build which I have not digested ?
* IIUC gitlab runner (?) can do ssh into TW VM's as crab3 user. Via its public key. How can this bypass 2FA ? AFAICT we onnly have `cmsbuild` in TW's `.ssh/authorized_keys`


I have not looked at the test part yet, I think it will be easier, less dependent on tools I do not know.
A bit at a time...

## Comment (novicecpp, 2024-04-15T11:34:50Z)

Answering your questions:

> what is the purpose of `cicd/buildtools/Dockerfile` ?  I can't find where it is used

It is Dockerfile to build `registry.cern.ch/cmscrab/buildtools`, container we use in this CI (as seen in [line 25](https://github.com/dmwm/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/.gitlab-ci.yml#L25)).
I will add README.md and short script for building this image.

> with reference to the `build_docker` stage, where is `${CI_PROJECT_DIR}` defined ? And how does the GH code gets there ?

See https://docs.gitlab.com/ee/ci/variables/predefined_variables.html

All details about sync, setup variables, credentials, runner, still not ready yet. 
Especially sync, I still have no conclusion about it, either via custom script or webhook magic.
Currently, I push to gitlab directly when I want to run pipeline.

> I know nothing about kaniko, hopefully I can live for a while w/o it

It is tools to build docker container in userspace. I plan to convert to [CERN](https://gitlab.cern.ch/gitlabci-examples/build_docker_image/)'s template later then ask for help from CERN IT.
For now, please consult [upstream docs](https://github.com/GoogleContainerTools/kaniko) directly. 

> what does it do the line `  - !reference [.default_rules, rules]` in the `gitlab-ci.yml` ?

https://docs.gitlab.com/ee/ci/jobs/job_control.html#reuse-rules-in-different-jobs

I use it to apply the rules define in [.gitlab-ci.yml#L9-L11](https://github.com/dmwm/CRABServer/blob/acbef6d60cbaf9cccd291d9216576fbae756b15a/.gitlab-ci.yml#L9-L11), i.e., make all jobs run only when tag name is prefix with `pypi-`.

> what is `name: registry.cern.ch/cmscrab/buildtools` ? Something I am not familiar with becasue it is part of the pypi build which I have not digested ?

Image name of docker-runner to run in this job (see also the propose of `cicd/buildtools/Dockerfile` I answered above). 
You can choose any image you want for docker-runner, or use default one (setup in runner config) and install/pull/download later.

> IIUC gitlab runner (?) can do ssh into TW VM's as crab3 user. Via its public key. How can this bypass 2FA ? AFAICT we onnly have `cmsbuild` in TW's `.ssh/authorized_keys`

Whitelist the runner host, like we do with Jenkins's hosts, and I use different ssh key to access.

## Comment (cmsdmwmbot, 2024-04-15T11:39:37Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 8 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1945/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-04-15T14:36:58Z)

Thanks for answers Wa. Now that you made me have a 2nd look at buildtools, is there any special reason not to install K8s client  via `yum install kubernetes-client.x86_64` and CERN repository like in
```          
belforte@aiadm00/~> cat /etc/yum-puppet.repos.d/kubernetes9el-stable.repo 
[kubernetes9el-stable]
name=Kubernetes clients [stable]
baseurl=http://linuxsoft.cern.ch/internal/repos/kubernetes9el-stable/x86_64/os
enabled=1
gpgcheck=True
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-kojiv2
includepkgs=kubernetes-client helm
priority=20
```

## Comment (novicecpp, 2024-04-15T14:39:46Z)

Ah, I never know. 
Thanks! I will change it in next PR.

## Comment (novicecpp, 2024-04-15T16:15:29Z)

Thanks a lot Stefano for the questions and review!

## Comment (novicecpp, 2024-04-16T18:41:24Z)

Thanks for comments and questions, Dario.

> is it true that if a job at a certain stage fails, then all the jobs at following stages are skipped, even if we did not specify any needs: directive? This [seems](https://gitlab.cern.ch/tseethon/crabserver/-/pipelines/7174555) to be the case but i could not find it mentioned in the official docs. maybe you already have a pointer

Yes, by default. Sorry, I do not have a pointer for this nor fully understand `needs` (yet). But, this make sense as "if something break, you should not continue". 

> please add to your guide/document that the variables CMSCRAB_REGISTRY_URL, ... come from https://gitlab.cern.ch/tseethon/crabserver/-/settings/ci_cd . I know you wrote "setup of these variables is not included in this document", I know, but I am not interested now in what values I should set there, but at least tell me where they are from, thanks :)

I have written short sentence where we set those in Gitlab. I completely forgot this.

> I would change the structure of the Appendix 2. all that section is about manually running a pipeline. I would start it with the instructions on how to run a pipeline, then specify that when we do so from the webgui or from the api we can set some additional env variables to speed up the execution. Only at this point i would specify the meaning of MANUAL_CI_PIPELINE_ID, SUBMIT_STATUS_TRACKING, ...

The pipeline in this PR does not mean to trigger manually where we can choose variables freely like we do with the Jenkins (still in my plan, but not for now). You need it only when you what to test new CI code (mainly the `.gitlab-ci.yml`. 

Maybe I should not write "Usage:" sub-bullet too, it make the guide more confusing, expecting you know (or google) how to do instead. The intention here is simply "I use this vars to test this and that." 

I will rewrite this section when move `cms-crab-docs` as "How to run manually." and "How to debug CI.", separately. Thanks for guiding.

> I see that you added to the latest appending a mention to the git push options, but I do not see where they could be used in the scripts. are they a replacement for the variables mentioned in my comments above, for example CMSCRAB_REGISTRY_URL or SUBMIT_STATUS_TRACKING?

Yes. I really missed that. For now, you can see example in [tag\_and\_push\_option.sh](https://github.com/dmwm/CRABServer/blob/4612652af1fc9fb61fac7dbd06b3c3a171f4a963/cicd/gitlab/trigger-ci/tag_and_push_option.sh).

## Comment (cmsdmwmbot, 2024-04-16T18:44:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 8 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1946/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-16T18:46:01Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 8 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1947/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-04-18T13:30:12Z)

Thanks again @belforte @mapellidario.
Merging...
