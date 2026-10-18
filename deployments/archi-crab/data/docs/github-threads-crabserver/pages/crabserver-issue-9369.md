# dmwm/CRABServer issue #9369: implemente automatic increase of time/memory when resubmitting

State: open
Opened: 2026-07-28T14:24:16Z
URL: https://github.com/dmwm/CRABServer/issues/9369

## Opening post (belforte, 2026-07-28T14:24:16Z)

@aspiringmind-code now in the master and in production allows for this, but we need to add the proper retry policies and adapt/remove the current code which exits with fatal error in
https://github.com/dmwm/CRABServer/blob/0a4d004e1d6d686e3496b62d62ca96061dd9c2cb/src/python/TaskWorker/Actions/RetryJob.py#L369
and
https://github.com/dmwm/CRABServer/blob/0a4d004e1d6d686e3496b62d62ca96061dd9c2cb/src/python/TaskWorker/Actions/RetryJob.py#L391
