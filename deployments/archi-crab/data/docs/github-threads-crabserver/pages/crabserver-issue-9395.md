# dmwm/CRABServer issue #9395: report IgnoreLocality to MONIT

State: closed
Opened: 2026-08-24T10:34:44Z
Closed: 2026-08-24T12:44:43Z
URL: https://github.com/dmwm/CRABServer/issues/9395

## Opening post (belforte, 2026-08-24T10:34:44Z)

we need to be able to easily see whether given jobs/tasks used IgnoreLocality or not, and to select based on that in OS/Grafana.

Will introduce a new classAd `CRAB_IgnoreLocality = True/False` to reflect the task table column `task['tm_ignore_locality']`

## Comment (belforte, 2026-08-24T12:44:43Z)

duplicate of #9390
