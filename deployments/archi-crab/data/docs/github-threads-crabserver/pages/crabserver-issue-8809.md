# dmwm/CRABServer issue #8809: flexible pipeline does not work ?`

State: closed
Opened: 2024-11-22T17:24:14Z
Closed: 2025-01-20T11:37:51Z
URL: https://github.com/dmwm/CRABServer/issues/8809

## Opening post (belforte, 2024-11-22T17:24:14Z)

I tried this, after tagging a local clone of current `master`
```
TAG=v3.241122.1
git tag $TAG
git push gitlab $TAG -o ci.variable="SUBMIT_STATUS_TRACKING=t"
```
pipeline: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8572192

and this
```
TAG=v3.241122.1
git tag $TAG
git push gitlab $TAG -o ci.variable="SUBMIT_STATUS_TRACKING=t" -o ci.variable="SKIP_BUILD=t" -o ci.variable="SKIP_DEPLOY=t"
```
pipeline: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8572202

but in both cases the standard pipeline was run with un-desired build-deploy steps and the status tracking tasks were not submitted, nor looked for.

Can you please document how the new options work ? Best with new files in `cicd/trigger-ci/`

## Comment (aspiringmind-code, 2024-11-25T10:23:17Z)

@belforte You need to explicitly use true and not t.
```
git push gitlab $TAG -o ci.variable="SUBMIT_STATUS_TRACKING=true" -o ci.variable="SKIP_BUILD=true" -o ci.variable="SKIP_DEPLOY=true"
```
I used this to create the pipeline https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8584828
Please let me know if that resolves your issue. I will add it to cicd/trigger-ci Thanks!

## Comment (belforte, 2024-11-25T11:07:51Z)

I see. Will try when done with current emergency
I was mislead by the use of  `=t` in current scripts in cicd/trigget-ci
Hopefully you can find a way to have a consistent interface

## Comment (aspiringmind-code, 2024-11-25T11:21:13Z)

The ci-trigger scripts have been updated and explicit true is used everywhere now. See https://github.com/dmwm/CRABServer/pull/8812

## Comment (belforte, 2024-11-25T20:30:36Z)

I have not tested status tracking yet, but I noticed that even if I don't, the jobs are still submitted https://gitlab.cern.ch/crab3/CRABServer/-/jobs/46494960

I am still confused

## Comment (aspiringmind-code, 2024-11-26T09:03:20Z)

@belforte By default, the SUBMIT_STATUS_TRACKING is true. So if you don't specify anything, they will be submitted. You can turn it off by specifying it as false.

## Comment (belforte, 2024-11-26T09:23:34Z)

isn't it odd that by default sunmission is true but checking is false ? if there's no check, why submit ?

## Comment (aspiringmind-code, 2024-11-26T09:39:34Z)

Hmm...makes sense. I can turn the default to false.

## Comment (belforte, 2024-11-26T09:45:13Z)

IMHO there should be only one flag: to execute or not a given test, which controls both submission and checking.
