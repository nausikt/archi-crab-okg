# dmwm/CRABServer issue #9388: prevent users from accidentally lower memory/time limits

State: open
Opened: 2026-08-19T21:47:02Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9388

## Opening post (belforte, 2026-08-19T21:47:02Z)

We should refuse to decrease memory and time limit to less than indicated in the original config file (and stored in `tasks` table).

* we have seen at least one case where a user decresed max-mem by mistake creating an onslaught of jobs failing after hours of processing
* but we need to think hard if there is some situation where users have a good reason to do this and we are preventing them
