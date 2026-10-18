# dmwm/CRABServer issue #8385: disable publication when input dataset is not VALID

State: closed
Opened: 2024-05-08T16:11:26Z
Closed: 2026-04-08T13:49:22Z
Labels: Type: Enhancement, Type: Question, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/8385

## Opening post (belforte, 2024-05-08T16:11:26Z)

DBS server only migrates VALID datasets, it is annoying that users only
discover this when publication fail, and we need to inspect Publisher logs to tell.

OTOH, currentely we let DBS enforce which dataset to migrate and which not.
But lack any good way to communicate to users what happened.

Need to make a decision !

## Comment (belforte, 2026-04-08T13:49:23Z)

duplicate of #9114  - Fixed in #9115
