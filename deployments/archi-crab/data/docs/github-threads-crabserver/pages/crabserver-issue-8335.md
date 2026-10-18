# dmwm/CRABServer issue #8335: prevent users from creating MC files with too many lumis

State: closed
Opened: 2024-04-15T20:20:25Z
Closed: 2025-08-29T15:43:14Z
Labels: Type: Enhancement, Type: Support, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8335

## Opening post (belforte, 2024-04-15T20:20:25Z)

if user do not specify anything, the default is 100.
That's too much. We should to down to e.g. 5 and impose a max at 10.

I'd like to see realistic MG generation use cases that needs more, before raising the max.
We can have an option, but I fear that users will start cloning config. files with large values
w/o knowing what they are doing.

## Comment (belforte, 2025-08-29T15:43:14Z)

this was solved with https://github.com/dmwm/CRABClient/issues/5385
