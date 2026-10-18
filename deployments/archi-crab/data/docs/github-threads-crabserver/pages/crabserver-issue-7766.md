# dmwm/CRABServer issue #7766: add Njob in task to Task Table

State: closed
Opened: 2023-07-17T10:19:25Z
Closed: 2025-04-11T13:50:20Z
Labels: Type: Enhancement, Type: Support, Status: Done, Status: Available
URL: https://github.com/dmwm/CRABServer/issues/7766

## Opening post (belforte, 2023-07-17T10:19:25Z)

It helps when looking at user jobs e.g. in the [UI](https://cmsweb.cern.ch/crabserver/u) to know how big was the task w/o going through remake+status or opening the (possibly large and slow) grafana page or the (possibly large and very slow) webdir
TW has the info after the splitting process, so can surely add easily

We do not have it for automatic splitting, can start by setting it to e.g. -1
if we want an integer there  (leave 0 for cases like splitter did not create any job).

For automatic splitting we'd need to add and edit it from preDag's as they run,
but maybe too much trouble

## Comment (novicecpp, 2023-07-18T10:20:51Z)

This is what I also want but I do not like the idea to store this data in oracle just for monitoring.
Can we do it the same way  we do with `cache_status()` in [task_proc_wrapper.sh](https://github.com/dmwm/CRABServer/blob/2365939e2777e4afa2077f2c6b485b899c1facde/scripts/task_process/task_proc_wrapper.sh#L7-L10), dump the simple json and let web UI to fetch this file and display?

## Comment (belforte, 2025-03-12T08:45:46Z)

doing now, since it may also be useful for task scheduling: knowing how big are current tasks for a given user
