# dmwm/CRABServer pull request #9293: Add manual pipeline

State: closed
Opened: 2026-04-09T13:25:07Z
Closed: 2026-04-10T10:55:04Z
Merged: 2026-04-10T10:55:04Z
URL: https://github.com/dmwm/CRABServer/pull/9293

## Opening post (belforte, 2026-04-09T13:25:07Z)

This PR does not really add manual pipelines, which is  a [gitlab feature](https://docs.gitlab.com/ci/pipelines/#run-a-pipeline-manually), but simply makes it easy by pre-filling the new pipeline page with the variables which one may want to change.
When a pipeline is started manually, rather than via a push, there may not be a git tag in the format `pypi-testX-` , or one may want to run for an existing tag (e.g. `v3.yymmdd`). Therefore it is useful to have a way to  select manually the rest/tw/pub hosts. For that goal, this PR  introduces the `ENV_NAME` variable (see the new `parseEnv.sh`)

## Comment (cmsdmwmbot, 2026-04-09T13:29:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2781/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-04-09T13:29:48Z)

A possible enhancement is to use [inputs](https://docs.gitlab.com/ci/inputs/) to help the operator with a predefine set of variables for common use-cases (deploy a give tag, rerun tests on same tag as some failed pipeline), but atm it seems an overkill.

## Comment (belforte, 2026-04-09T14:04:28Z)

thanks @nausikt for super-fast feedback. Indeed it is a safe PR. I asked for review mostly to keep you informed

## Comment (belforte, 2026-04-10T08:54:51Z)

@aspiringmind-code would you like to review first, or may I merge ?

## Comment (aspiringmind-code, 2026-04-10T10:32:15Z)

@belforte Yes, reviewing in a bit.
