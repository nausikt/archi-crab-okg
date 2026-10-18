# dmwm/CRABServer issue #9405: primary TW should log tasknames assigned to canary

State: open
Opened: 2026-08-31T12:44:57Z
URL: https://github.com/dmwm/CRABServer/issues/9405

## Opening post (belforte, 2026-08-31T12:44:57Z)

currently MasterWorker simply logs this line with "canary-fraction probability"
https://github.com/dmwm/CRABServer/blob/2a9114fa346f4b3846443ce7f8f0ef652ea49298/src/python/TaskWorker/MasterWorker.py#L422

problems:
1. it is logged even if there was no task to be acted on
2. when some tasks are assigned to canary TW,  we should log their name to help debugging
