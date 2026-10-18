# dmwm/CRABServer issue #9077: kill, not hold, DAGs when CRAB_TaskEndTime is reached

State: closed
Opened: 2025-05-16T14:58:58Z
Closed: 2025-05-26T14:18:54Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9077

## Opening post (belforte, 2025-05-16T14:58:58Z)

allows proper wrap-up of ASO-Rucio see
https://github.com/dmwm/CRABServer/issues/8429#issuecomment-2886278081

relevant code is
https://github.com/dmwm/CRABServer/blob/c64dc53f28f56a1022121b3680a757daf88f40ad/src/python/TaskWorker/Actions/DagmanSubmitter.py#L502-L509

easy enough to replace `PeriodicHold` with `PeriodicRemove` but should I also change `OnExitHold` or (better) remove it ?
Or is it useful for tasks where the dagman completes with some failed jobs and a Rescue file to be activated via a condor_release ?

Will start minimal and test
