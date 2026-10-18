# dmwm/CRABServer issue #8873: make sure that TW name decision sticks

State: closed
Opened: 2025-01-09T13:03:06Z
Closed: 2025-01-20T07:50:27Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/8873

## Opening post (belforte, 2025-01-09T13:03:06Z)

now that we have two TW's (primary and canary) we should avoid that a TW restarts overwrites the TW assignment of QUEUED tasks and any other "interference"

at the moment both primary and canary pick tasks QUEUED by either, set to NEW and then primary handles them again as new with a new decision if to assign to canary or not.

This makes for non-reproducible behavior and makes it difficult to debug.

Once the initial decision on which TW handles a task is taken, it should stay there.

## Comment (aspiringmind-code, 2025-01-20T07:50:27Z)

Resolved in https://github.com/dmwm/CRABServer/pull/8882
