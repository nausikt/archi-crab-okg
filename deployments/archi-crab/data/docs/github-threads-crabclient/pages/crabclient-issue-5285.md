# dmwm/CRABClient issue #5285: deprecate resubmission of successful jobs

State: closed
Opened: 2024-01-10T16:35:30Z
Closed: 2025-06-23T13:40:17Z
Labels: Support, HighPrio, CleanUp
URL: https://github.com/dmwm/CRABClient/issues/5285

## Opening post (belforte, 2024-01-10T16:35:30Z)

given that it is tricky to support (only works in certain DAGMAN status) and there is no clear use case, and that it may cause more confusion than help, we agreed to simply remove the possibility and only allow resubmission of failed jobs.

See also #5273 

FYI @mapellidario
