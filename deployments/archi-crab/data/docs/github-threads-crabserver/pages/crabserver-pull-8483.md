# dmwm/CRABServer pull request #8483: Triggering release pipeline via Github Actions

State: closed
Opened: 2024-06-10T11:52:11Z
Closed: 2024-06-11T10:27:08Z
URL: https://github.com/dmwm/CRABServer/pull/8483

## Opening post (novicecpp, 2024-06-10T11:52:11Z)

The last part for https://github.com/dmwm/CRABServer/issues/8401. This PR is adding 2 new pipelines:

1. Github Actions: Pipline to trigger another pipeline in [crab3/CRABServer](https://gitlab.cern.ch/crab3/CRABServer/)'s Gitlab-CI.

The pipeline only triggers when push "Publish release" button on [creating a new release's page](https://github.com/dmwm/CRABServer/releases/new).  The job trigger the Gitlab-CI pipeline by running the `curl` command to `https://gitlab.cern.ch/api/v4/projects/<project_id>/trigger/pipeline` endo. The API needs branch/tag to trigger and a token to authenticate. Full API documentation is on <https://docs.gitlab.com/ee/ci/triggers/>.

The token that is used here is "Trigger API token", created on Gitlab's `crab3/CRABServer`, in repository's CI/CD setting. 

The only variable we pass through the API is the name of the new tag, the `GITHUB_REF_NAME`.

2. Gitlab-CI: pipeline to pull new tags from GitHub to Gitlab

This pipeline only have single job `sync_release_from_github` doing 2 steps: one is to clone the new tag from `GITHUB_REF_NAME`, and then push it to `crab3/CRABServer`. When it pushed to `crab3/CRABServer`, the [release pipeline](https://github.com/dmwm/CRABServer/pull/8421) will be triggered.
The credential that is used to push there is the ssh-key attached to the `crabint1` account, so it will not expire as long as the `crabint1` account is still active. Note that `Developer` access is grant to `crabint1` in order to allow to push.

The interaction diagram between GitHub Action and Gitlab-CI is shown in the following image:


![trigger_from_gh drawio(1)](https://github.com/dmwm/CRABServer/assets/2346664/93524b70-64d0-4c63-a5e4-11271d3752d5)

## Comment (cmsdmwmbot, 2024-06-10T11:56:15Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2013/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-06-11T09:42:07Z)

great documentation, very clear. And I love the diagram.
Will look at code next

## Comment (mapellidario, 2024-06-11T09:51:49Z)

Thanks wa! 

Before I give you my final opinion and before I deep dive into google, i have naive question. It feels weird that we need to use ssh to fetch the tags from github and push them to gitlab. is it possible that we can achieve the same result with the gitlab feature "repository mirroring" [1]? 

[1] https://gitlab.cern.ch/help/user/project/repository/mirror/index

## Comment (novicecpp, 2024-06-11T10:26:17Z)

Thanks Dario. At the time I tried, some how the repo mirror does not trigger the pipeline. 
But now everything works.

Here is the release <https://github.com/dmwm/CRABServer/releases/tag/v3.240607.test1>
After repo sync (taking some time or can trigger sync manually in "Repository mirroring" setting), new pipeline was triggered <https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7546188>

## Comment (novicecpp, 2024-06-11T10:27:08Z)

Closing this PR then. Not need it anymore.

## Comment (belforte, 2024-06-11T12:54:56Z)

:astonished:

## Comment (mapellidario, 2024-06-11T14:17:26Z)

Uh, that was quick, thanks wa for having a look, sorry for changing your plans!
I did not want to discard your work, it is terrific as always, thanks for having the patience for always finding a working solution to every problem or question or desire we may have :)

## Comment (novicecpp, 2024-06-12T09:23:42Z)

I might revive this PR later because it is more reliable (in term of triggering time and traceability) than trigger from mirror sync.
