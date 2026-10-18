# dmwm/CRABServer issue #9374: reduce load on dagman start by lowting MaxPre

State: closed
Opened: 2026-08-01T16:36:52Z
Closed: 2026-08-01T16:52:12Z
Labels: Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/9374

## Opening post (belforte, 2026-08-01T16:36:52Z)

Our schedd's struggle to restart when fully loaded. One contribution is too much memory in python processes.
In particular when schedd restarts all dagman restart at same time, and try to submit. So can have hundreds of PreJob
scripts running at same time.
Currently we allow up to 20 PreJob to run concurrently in each Dagman. But over time we have been added things to
PreJob and they do not really complete very fast.
So as a mitigation we can lower MaxPre from 20 to 10 in

https://github.com/dmwm/CRABServer/blob/6e374190d0b47f1a193751bce8876654f834f1f9/scripts/dagman/dag_bootstrap_startup.sh#L282

MaxPost is already 10 and anyhow concurrenty of PostJob could be due to many jobs completing at same time, but it is not immediately affecting schedd restart.
