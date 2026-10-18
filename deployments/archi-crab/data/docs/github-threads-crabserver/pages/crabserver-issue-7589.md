# dmwm/CRABServer issue #7589: avoid tape recalls across Atlantic

State: closed
Opened: 2023-04-13T22:00:30Z
Closed: 2023-04-28T17:12:00Z
Labels: Status: Done, Priority: High, Area: zDATA RECALL
URL: https://github.com/dmwm/CRABServer/issues/7589

## Opening post (belforte, 2023-04-13T22:00:30Z)

self describing !

## Comment (belforte, 2023-04-14T08:22:26Z)

I think we can start simple:
* from FNAL tape go only to US and BR
* from other T1's  exclude US and BR

## Comment (belforte, 2023-04-27T16:46:12Z)

the fix in https://github.com/dmwm/CRABServer/commit/c817fcce91d8679e8c9d51f4ab3fa8d58e797480 does not work. Currently the list of locations has one entry per block. 
https://github.com/dmwm/CRABServer/blob/3d7cb32e23e1b3c0da6fd2f93c7f646f093509a5/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L455-L461
