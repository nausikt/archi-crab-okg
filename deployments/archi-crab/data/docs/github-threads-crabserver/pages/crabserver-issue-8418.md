# dmwm/CRABServer issue #8418: remove old "panda" columns from DB

State: closed
Opened: 2024-05-16T21:26:08Z
Closed: 2024-05-27T08:57:59Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8418

## Opening post (belforte, 2024-05-16T21:26:08Z)

our TaskDB table still contains the columns `panda_resubmitted_jobs` and `panda_jobset_id` even we do not use them since many many years and they have been removed from the code in 
https://github.com/dmwm/CRABServer/blob/master/src/python/Databases/TaskDB/Oracle/Create.py
and everywhere else.

Can we remove them from Oracle as well, for mind sanity if not for space ?
