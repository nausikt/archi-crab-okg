# dmwm/CRABServer issue #8815: CI pipeline cache/artifact confusion

State: closed
Opened: 2024-11-25T16:06:53Z
Closed: 2025-02-28T15:44:22Z
Labels: Type: Bug, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8815

## Opening post (belforte, 2024-11-25T16:06:53Z)

Something is wrong with our pipleine.
https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8586807 failed in the check status with
```
Reason is: Impossible to find task 241125_151251:crabint1_crab_transferOutputs in the database.
```
AFAICT the reason is that we had two pipelines running at same time, that one and https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8586977


That task was created in preprod by the second pipeline, but somehow the first pipeline (which worked with the test2 instance, i.e. dev DB) picked the list of task from the other pipeline and failed.

## Comment (belforte, 2024-11-25T21:58:05Z)

most likely same problem as #8755
