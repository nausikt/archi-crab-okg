# dmwm/CRABServer pull request #8653: Change CI variables name for triggering the pipelines

State: closed
Opened: 2024-08-26T16:40:48Z
Closed: 2024-08-27T11:32:58Z
Merged: 2024-08-27T11:32:58Z
URL: https://github.com/dmwm/CRABServer/pull/8653

## Opening post (novicecpp, 2024-08-26T16:40:48Z)

The trigger scripts also included.

## Comment (cmsdmwmbot, 2024-08-26T16:42:48Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2124/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-08-26T16:43:52Z)

Documentation is in https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/triggering.html#variables-in-rules

Any comment is welcome. I will merge this tomorrow.

## Comment (belforte, 2024-08-26T18:41:50Z)

maybe `FORCE_RELEASE` --> `ONLY_BUILD_RELEASE` there is no forcing there, simply the DEPLOY and TEST stage are skipped.

Now there is this (new?)  [Triggering](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/triggering.html#variables-in-rules) page under 'Gitlab' and another [Triggering](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/pipelines/build-deploy-test.html#triggering) under `Gitlab/pipelines/build-deploy-test`

I find that confusing and am not sure that text is consistent. In particular (as usual because I am thick as a brick) I am confused if release is triggered by creating v3.YYMMDD in GH or if a push of v3.YYMMDD-stable to GL is needed.

FInally, can you clarify
```
Non-release tag in Gitlab will be cleaned up later.
```
? Do you mean that there is an automatic process ? Or that someone may have/want to cleanup at some time ?

Thanks !!!!

## Comment (novicecpp, 2024-08-26T18:57:51Z)

> maybe FORCE_RELEASE --> ONLY_BUILD_RELEASE there is no forcing there, simply the DEPLOY and TEST stage are skipped.

Ok. I will change.

> Now there is this (new?) [Triggering](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/triggering.html#variables-in-rules) page under 'Gitlab' and another [Triggering](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/pipelines/build-deploy-test.html#triggering) under Gitlab/pipelines/build-deploy-test

I forgot to modify that sections. It should be removed or point to the new page.

> I find that confusing and am not sure that text is consistent. In particular (as usual because I am thick as a brick) I am confused if release is triggered by creating v3.YYMMDD in GH or if a push of v3.YYMMDD-stable to GL is needed.

Former. I will make it clearer.

> FInally, can you clarify
> Non-release tag in Gitlab will be cleaned up later.
> ? Do you mean that there is an automatic process ? Or that someone may have/want to cleanup at some time ?

More likely the latter. The message I want to convey here is "all tags in Gitlab are temporary and subjects to be removed later". 
We abuse git tag so much that I fear the side effect in the long term. It would be great if we clean it up regularly. But of course, it is not urgent or become any problem. I would rather leave all tags as is and add some notes to the docs.


Thanks for reading and comments!

## Comment (belforte, 2024-08-26T18:59:22Z)

thanks to you
:bowing_man:

## Comment (belforte, 2024-08-26T19:20:31Z)

> . I would rather leave all tags as is and add some notes to the docs.

yeah... once we know that we can delete all tags at any time, we are happy !

## Comment (cmsdmwmbot, 2024-08-27T10:16:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2125/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-27T10:17:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2126/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-08-27T11:32:53Z)

Fix.
