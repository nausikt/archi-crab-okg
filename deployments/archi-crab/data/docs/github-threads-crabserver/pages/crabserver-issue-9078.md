# dmwm/CRABServer issue #9078: remove ASORucioTimeout

State: closed
Opened: 2025-05-16T15:06:52Z
Closed: 2025-05-26T14:18:54Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9078

## Opening post (belforte, 2025-05-16T15:06:52Z)

let PostJob run for as long as needed to give Rucio time to deal with stuck replicas, until `CRAB_TaskEndTime`
see https://github.com/dmwm/CRABServer/issues/8429#issuecomment-2871927499


**since jobs in transferring can not be resubmitted, do not stop PostJob after 7 days, let it run until Task is terminated/completed, i.e. Rucio eventually succeeds or task is killed or task reaches end of life**
