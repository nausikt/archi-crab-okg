# dmwm/CRABServer issue #7590: extend lifetime of tape recall rules

State: closed
Opened: 2023-04-13T22:07:34Z
Closed: 2023-04-13T22:18:02Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7590

## Opening post (belforte, 2023-04-13T22:07:34Z)

in CRAB DevOps meeting today we agreed to:

- [x] make initial tape recall rule valid for 30 days . Done in https://github.com/dmwm/CRABServer/commit/bbd2caba3073c50f7acdb6f6fa0536be547a01bd
- [x] allow 30 days for tape recall to be complete (currently 14 days)
- [x] when recall is complete and task is released, update lifetime 30 days from now
