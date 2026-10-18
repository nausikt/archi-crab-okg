# dmwm/CRABServer issue #7782: Remove dependency on htcondor from HTCondorDataWorkflow.py

State: closed
Opened: 2023-07-20T16:50:52Z
Closed: 2024-04-17T13:14:27Z
Labels: Priority: Medium, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7782

## Opening post (mapellidario, 2023-07-20T16:50:52Z)

We are not using anymore the functions in HTCondorDataWorkflow.py that require talking directly to the schedulers.

However, maybe in the future we will find a good reason for talking to the schedds from crabserver, so we do not want to remove the rpm from py3-htcondor specfile from the crabserver image and we want to keep HTCondorDataWorkflow.py around in the current state (maybe freeze the file in its current forms in a copy with "old" appended at the end).

A good starting point would be https://github.com/dmwm/CRABServer/compare/master...mapellidario:20230717_py3htc10

## Comment (belforte, 2023-07-20T17:22:46Z)

we can remove htcondor from spec file unti needed, FWIW. I only worry about loosing code which we may not easily re-invent

## Comment (belforte, 2024-04-17T13:14:27Z)

item moved to #8338
