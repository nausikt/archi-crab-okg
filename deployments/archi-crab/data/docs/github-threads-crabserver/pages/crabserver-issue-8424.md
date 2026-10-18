# dmwm/CRABServer issue #8424: Remove WMArchive

State: closed
Opened: 2024-05-23T06:12:53Z
Closed: 2025-03-10T11:17:24Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8424

## Opening post (novicecpp, 2024-05-23T06:12:53Z)

We announced the deprecation WMArchive stats in [O&C weekly meeting on 24 April 2024](https://indico.cern.ch/event/1409162/).

It is time to remove the code.

## Comment (novicecpp, 2024-05-23T06:15:04Z)

@belforte Do we want to remove this code from PostJob? 
https://github.com/dmwm/CRABServer/blob/40a796ffe3d1c7b1b2cddf6a6e74c3b08e2b5a3a/src/python/TaskWorker/Actions/PostJob.py#L3086-L3156

 Or just improve the log to print warning instead of exception?

## Comment (belforte, 2025-03-06T12:23:52Z)

yes, remove
There are many other places where we should cleanup both in CRABServer repository and in puppet one
