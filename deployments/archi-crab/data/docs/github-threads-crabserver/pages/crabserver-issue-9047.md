# dmwm/CRABServer issue #9047: status_cache.py fails to deal with short running jobs

State: closed
Opened: 2025-04-15T09:58:05Z
Closed: 2025-04-16T12:30:46Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9047

## Opening post (belforte, 2025-04-15T09:58:05Z)

code sort of assumes that there is time to catch all statuses.
But if a job quickly fails twice with message to retry, in the code below the node `status` may fail to be sampled while in STATUS_SUBMITTED in the second attempt, so that `info['State']` will not be changed from `cooloff` when STATUS_POSTRUN is detected.

The point is that while a node is in POSTRUN, i.e. PostJob wating to run, we have no way to know if it is waiting because maxPost in the DAGMAN kicked in, or if it is waiting on the transfer to complete. And the only time we have jobs in cooloff now is when they are back to STATUS_READY or STATUS_PRERUN

Indeed inside STATUS_READY we should check on retry number to tell unsubmitted from cooloff, like done in PRERUN, instead of looking at what the node status was set to in previous iteration of the cache_status.py script (`info['State']) !

Many things can happen between one iteration and the next of the status caching script, it should never rely on previous value, if possible, but only on current information.


https://github.com/dmwm/CRABServer/blob/9ac340864c34ce29acc0b732bd1410cd0e6de4ff/scripts/task_process/cache_status.py#L275-L294
