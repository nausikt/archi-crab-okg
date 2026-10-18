# dmwm/CRABServer issue #8518: remove un-needed dependencies from crabtaskworker-pypi

State: closed
Opened: 2024-06-19T14:55:13Z
Closed: 2024-06-20T10:05:57Z
Labels: Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8518

## Opening post (belforte, 2024-06-19T14:55:13Z)

it currently takes O(10) min to build TW container in the pipeline.
I think it is because we still have a list of dependencies from "old rpm times" with all possible things used by all possible WMCore application in  https://github.com/dmwm/CRABServer/blob/master/cicd/crabtaskworker_pypi/requirements.txt 
Already https://github.com/dmwm/CRABServer/blob/master/cicd/crabserver_pypi/requirements.txt is much more trimmed.

## Comment (novicecpp, 2024-06-20T08:00:24Z)

Thanks Stefano. 
From what I saw in CI machine, most CPU is gone due to I/O wait. Reducing the deps will help cutting time by a lot.

## Comment (belforte, 2024-06-20T09:02:06Z)

yeah, I had been looking at pipeline log in realtime and noticed that all those pip install were taking a lot.
I built `pypi-test2-reducetwdep` with that and at least TW is built in same time as server. A lot of time goes in conda/gfal as you know. I guess the only way to cut time now is to create a base image with gfal and start from that. Not sure it is worth
