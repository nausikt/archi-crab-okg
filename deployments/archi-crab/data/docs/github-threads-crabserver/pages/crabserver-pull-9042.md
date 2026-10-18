# dmwm/CRABServer pull request #9042: Add info to tasks 03 25

State: closed
Opened: 2025-04-10T17:06:50Z
Closed: 2025-04-10T17:07:54Z
URL: https://github.com/dmwm/CRABServer/pull/9042

## Opening post (belforte, 2025-04-10T17:06:50Z)

this PR brings in 3 things

1. reports to DB Number of Jobs in DAG. Works also for automatic splitting.
2. reports to DB status of DAG. More work still needed for automatic splitting, but OK otherwise
3. runs new version of status_cache.py code which was in since years but never enabled. At the moment the new version is run "parassitically", output compared and mail sent to Stefano in case of difference.

I'd like to have this in Canary so I can make sure that 3. is OK (or fix) and to get examples of more complex automatic splitting jobs to finalize code

## Comment (belforte, 2025-04-10T17:07:54Z)

wrong branch :-(
