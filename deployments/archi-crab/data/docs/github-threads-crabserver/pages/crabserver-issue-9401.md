# dmwm/CRABServer issue #9401: save dag_bootstrap.sh log and make it more robust

State: open
Opened: 2026-08-26T15:00:21Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9401

## Opening post (belforte, 2026-08-26T15:00:21Z)

following up on the analysis of #9399 , improve [dag_bootstrap.sh](https://github.com/dmwm/CRABServer/blob/master/scripts/dagman/dag_bootstrap.sh)
- [ ] when using ASO-Rucio make sure that the DEFERRING loop can not be exited with status 1
- [ ] save the script log, e.g. trim to needed part (w/o the env dump) and save in a file named  with id.retry, or timestamp, or add inside the Pre/PostJob.id.retry.txt log file
