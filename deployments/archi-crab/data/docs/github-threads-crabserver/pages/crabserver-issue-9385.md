# dmwm/CRABServer issue #9385: widen time window for TW getWork

State: closed
Opened: 2026-08-14T14:33:26Z
Closed: 2026-08-14T14:46:21Z
Labels: Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/9385

## Opening post (belforte, 2026-08-14T14:33:26Z)

We currently select tasks in HOLDING using "since 1 month" to avoid a full table scan, but we have evidence  of tasks leaking in HOLDING status.
It is not clear why it happens. In today's finding all tasks in HOLDING are from earlier than July 13 and are waiting on KILL command.

Maybe some edge effect when users send a kill to a task near its 30 days threshold.

We will start by enlarging the "getWork" window to 2 months in here
https://github.com/dmwm/CRABServer/blob/1cdeb6c7a7a9817f933cfafc2a018bc7a179c65b/src/python/TaskWorker/MasterWorker.py#L426-L442

by adding the `months` parameter to the GET query
