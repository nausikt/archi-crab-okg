# dmwm/CRABServer issue #8872: keep tasks assignement to TW host when restarting

State: closed
Opened: 2025-01-09T13:02:34Z
Closed: 2025-02-13T20:41:01Z
URL: https://github.com/dmwm/CRABServer/issues/8872

## Opening post (belforte, 2025-01-09T13:02:34Z)

now that we have two TW's (primary and canary) we should avoid that a TW restarts overwrites the TW assignment of QUEUED tasks and any other "interference"

at the moment both primary and canary pick tasks QUEUED by either, set to NEW and then primary handles them again as new with a new decision if to assign to canary or not.

This makes for non-reproducible behavior and makes it difficult to debug.

Once the initial decision on which TW handles a task is taken, it should stay there.

## Comment (belforte, 2025-02-13T20:40:51Z)

duplicate of https://github.com/dmwm/CRABServer/issues/8873
