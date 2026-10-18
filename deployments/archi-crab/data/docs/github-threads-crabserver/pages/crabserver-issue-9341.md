# dmwm/CRABServer issue #9341: move EXIT_RETRY_POLICY to configuration

State: open
Opened: 2026-07-03T19:34:51Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9341

## Opening post (belforte, 2026-07-03T19:34:51Z)

Can replace this
https://github.com/dmwm/CRABServer/blob/7ae2e893a540c8044a108b0cd6a7f10b0e2cd690/src/python/TaskWorker/Actions/RetryJob.py#L22-L30
with a JSON file loaded via config and deployed via puppet.
So can exercise changes in policy w/o needing new build
