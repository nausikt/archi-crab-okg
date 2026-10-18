# dmwm/CRABServer issue #8504: monit - use pypi crabtaskworker docker image

State: closed
Opened: 2024-06-17T12:27:06Z
Closed: 2024-06-19T09:46:58Z
Labels: Area: MONIT, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8504

## Opening post (mapellidario, 2024-06-17T12:27:06Z)

Since we are quickly moving to images build from pypi, abandoning rpms, the docker images that we use for monitoring need to adapt as well.

Effectively, this means that the directories `monit-python` and `monit-taskworker` in https://github.com/dmwm/CRABServer/tree/master/cicd/build need to go.

I implemented the changes in an upcoming PR.
