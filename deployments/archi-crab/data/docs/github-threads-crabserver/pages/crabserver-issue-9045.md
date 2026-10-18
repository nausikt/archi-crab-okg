# dmwm/CRABServer issue #9045: status_cache.py fails to catch transition from unsubmitted or idle to running

State: closed
Opened: 2025-04-14T20:16:14Z
Closed: 2025-04-16T14:28:46Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9045

## Opening post (belforte, 2025-04-14T20:16:14Z)

these lines are wrong
https://github.com/dmwm/CRABServer/blob/9ac340864c34ce29acc0b732bd1410cd0e6de4ff/scripts/task_process/cache_status.py#L285-L289

the use of `setdefault` means that if job `State` was already set in a previous run of the script, it will not change until the DAG node reaches a different status like `5=complete`

There is no reason to use `setdefault` and indeed code around it does not !

## Comment (belforte, 2025-04-16T14:28:47Z)

closed via #9046
