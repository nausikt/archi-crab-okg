# dmwm/CRABServer issue #9076: rm dagman jobs on `crab kill`

State: closed
Opened: 2025-05-16T14:56:31Z
Closed: 2025-05-22T08:56:52Z
URL: https://github.com/dmwm/CRABServer/issues/9076

## Opening post (belforte, 2025-05-16T14:56:31Z)

Since we deprecate resubmission (#9075) there is no point in holding them.
Also `node_state` file does not differentiate between running and held dagman making it difficult to tell what's going on in `cache_status.py` see 
* https://github.com/dmwm/CRABServer/issues/8429#issue-2313045233
* https://github.com/dmwm/CRABServer/issues/8429#issuecomment-2880611568
