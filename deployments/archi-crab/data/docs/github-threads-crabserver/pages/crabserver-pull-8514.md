# dmwm/CRABServer pull request #8514: Fix various CIs 

State: closed
Opened: 2024-06-19T12:56:30Z
Closed: 2024-06-19T18:51:18Z
Merged: 2024-06-19T18:51:18Z
URL: https://github.com/dmwm/CRABServer/pull/8514

## Opening post (novicecpp, 2024-06-19T12:56:30Z)

1. Fix error in https://gitlab.cern.ch/crab3/CRABServer/-/jobs/40238792
    CI will not pull artifacts for a job if job does not specify "needs:" from job that created the artifact (I could not find the citation, but this is what I understand from working with Gitlab-CI).
2. Move `tag_monit_latest` job to `tagging_release` stage instead of same stage as build. Avoid blocking other stage if bug arise and it would be better to let it passing validation first. 
3. Fix force release, CI code is already there (Issue: https://github.com/dmwm/CRABServer/issues/8401) but 
    - Add `FORCE_RELEASE` variable to skip deploy and test, which is currently equivalent to `SKIP_DEPLOY` but more understandable.
    - Fix when we specify `RELEASE_NAME`, it will not suffix with `-stable`.
    - Fix in `set_version_name` job, default value of release name is the tag name.

## Comment (cmsdmwmbot, 2024-06-19T13:00:53Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2026/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-06-19T13:39:09Z)

Everything looks perfect, thanks for the in-person explanation, and for the promise of adding how to use these new features to our documentation :) you can merge this PR anytime :)

## Comment (belforte, 2024-06-19T13:41:13Z)

thanks Wa and Dario. I will not try to understand the details here. There's a limit at how much I can absorb.

## Comment (mapellidario, 2024-06-19T13:53:17Z)

> There's a limit at how much I can absorb.

I have to admit that I struggle to keep up with the implementation details, Wa's [qi](https://en.wikipedia.org/wiki/Qi) is getting too strong :) Nonetheless, I start to see how nice the result is, I really like interacting with gitlab and I promise and made wa promise that we will have a simple "how to use" guide. Once you start using it I am sure that you will enjoy play with it as well :)

## Comment (belforte, 2024-06-19T14:01:14Z)

oh I like it already. Simply can't read the YAML file and have an opinion !

## Comment (novicecpp, 2024-06-19T18:51:14Z)

Thanks Dario and Stefano for comments!
