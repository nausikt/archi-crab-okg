# dmwm/CRABServer pull request #8553: [CI] fix SUBMIT_STATUS_TRACKING

State: closed
Opened: 2024-07-23T11:21:29Z
Closed: 2024-07-23T11:21:36Z
Merged: 2024-07-23T11:21:36Z
URL: https://github.com/dmwm/CRABServer/pull/8553

## Opening post (novicecpp, 2024-07-23T11:21:29Z)

If we provide `SUBMIT_STATUS_TRACKING` to CI, it still run all job. 
For example https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7806040

It should run `task_submission_status_tracking` and `check_test_result` only, as stated in design document https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/pipelines/build-deploy-test.html#run-testsuite

This PR fix that issue.
