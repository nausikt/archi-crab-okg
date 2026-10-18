# dmwm/CRABServer issue #9086: update clientValidation in gitlab pipeline

State: closed
Opened: 2025-05-21T14:25:54Z
Closed: 2025-07-14T11:58:29Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9086

## Opening post (belforte, 2025-05-21T14:25:54Z)

on August 2024  the testing of `crab recover`  was added to the old script used in Jenkins
https://github.com/dmwm/CRABServer/blob/master/test/container/testingScripts/clientValidation.sh
in https://github.com/dmwm/CRABServer/commit/a1e9ca08f0972cb8a4db48570e9fd0ee91fd79b2

but that is missing in the version which we use in gitlab
https://github.com/dmwm/CRABServer/blob/master/cicd/gitlab/clientValidation.sh

must make sure that nothing is lost and eventually remove old files/directories in `test/container` and replace with symlinks to gitlab versions, until a time where we decide that we will never run tests in Jenkins anymore

## Comment (aspiringmind-code, 2025-07-14T11:57:12Z)

[Tested](https://gitlab.cern.ch/crab3/CRABServer/-/jobs/58751272)
