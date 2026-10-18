# dmwm/CRABServer issue #8338: remove calls to htcondor inside REST code

State: closed
Opened: 2024-04-15T21:45:04Z
Closed: 2024-06-24T15:07:00Z
Labels: Priority: High, Area: Code Cleanup, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8338

## Opening post (belforte, 2024-04-15T21:45:04Z)

we do not use them since almost ever. Nor want to.
If we ever wanted to talk to HTCondor from client, better do it via the TW. 

 - [x] remove htc calls from HTCondorDataWorkflow.py
 - [x] make sure that's the only place
 - [x] make the change backward compatible with current client
 - [x]  also remove htcondor from CRABRest container

- [x] Also remove possibility to do this in `crab status` https://github.com/dmwm/CRABClient/blob/0a267d70365e02621f2187bf09ccad791ac2e60d/src/python/CRABClient/Commands/status.py#L85-L88 At first sight that's the only API which would trigger a call to HTCondor inside the REST
   - [x] https://github.com/dmwm/CRABClient/issues/5316

## Comment (mapellidario, 2024-04-17T09:59:51Z)

Does this issue supersede #7782 ? Can we close that issue in favor of this one?

## Comment (belforte, 2024-04-17T11:18:40Z)

oopss... Thanks Dario, I did not rememeber that we have that already. It i exacly same thing.
Let's merge in this one. so adding 
- [ ] remove htcondor from CRABRest container

I do guess it is not worth to worry about old spec files anymore, will be enough to do for the Pypi part
