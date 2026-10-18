# dmwm/CRABClient issue #5399: remove dag nodes parsing from crab status

State: closed
Opened: 2025-06-25T15:39:27Z
Closed: 2025-10-31T08:41:48Z
Labels: enhancement, HighPrio, CleanUp
URL: https://github.com/dmwm/CRABClient/issues/5399

## Opening post (belforte, 2025-06-25T15:39:27Z)

the work is now done in the `cache_status.py` script and result available in the pickle file. 
Client should not have knowledge of the internals of DAG nodes.

ref: https://github.com/dmwm/CRABServer/issues/6875

## Comment (belforte, 2025-06-25T15:43:52Z)

Of course deleting of current code must be done after careful validation that what we get in the pickle file is sufficient and correct, or at least not worst.

## Comment (belforte, 2025-10-06T08:27:31Z)

@nausikt I think that cleanup is better done by me. No point for you to study code which is going to be removed
