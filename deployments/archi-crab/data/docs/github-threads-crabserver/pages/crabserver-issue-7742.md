# dmwm/CRABServer issue #7742: find correct duplicate rule 

State: closed
Opened: 2023-07-11T22:34:47Z
Closed: 2023-07-12T12:55:16Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/7742

## Opening post (belforte, 2023-07-11T22:34:47Z)

this is wrong
https://github.com/dmwm/CRABServer/blob/2e36bc17d6ab4db1ce4588588877521425d3036b/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L669-L673

there can be multiple rules on CMS datasets, starting with `wmcore_output` locking data to tape. Need to loop on all rules and find the correct one which does really match our account.
Using wrong rule will make TapeRecallManager wrongly believe that all is OK and release task.

@novicecpp had reported same issue while working on RUCIO_Transfers, but I failed to make the connection :-(
