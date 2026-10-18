# dmwm/CRABServer issue #8542: keep tmp directory in TW only for 6 hours

State: closed
Opened: 2024-07-05T08:33:27Z
Closed: 2024-07-05T08:36:42Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8542

## Opening post (belforte, 2024-07-05T08:33:27Z)

until a more fundamental solution to #7461 is put in place, let's reduce the time that tmp directories stick around for debugging

https://github.com/dmwm/CRABServer/blob/c56db97db0f6ca6e885ff11f95c680201c649971/src/python/TaskWorker/Actions/Recurring/RemovetmpDir.py#L13
