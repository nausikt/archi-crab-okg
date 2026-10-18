# dmwm/CRABServer issue #9176: remove bannedOutDestination from TW

State: closed
Opened: 2025-09-04T21:25:59Z
Closed: 2025-09-22T10:07:24Z
Labels: Status: Done, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9176

## Opening post (belforte, 2025-09-04T21:25:59Z)

we never used it, and surely will not in the future.

I looks to me that this is not used anywhere and could simply be deleted

https://github.com/dmwm/CRABServer/blob/4f835ab370cfb4d969be4c1d244020ea177611ee/src/python/TaskWorker/Actions/SiteInfoResolver.py#L113-L122

 together with the relative test
https://github.com/dmwm/CRABServer/blob/4f835ab370cfb4d969be4c1d244020ea177611ee/src/python/TaskWorker/Actions/SiteInfoResolver.py#L155-L157

or am I confused ?

@sinonkt
