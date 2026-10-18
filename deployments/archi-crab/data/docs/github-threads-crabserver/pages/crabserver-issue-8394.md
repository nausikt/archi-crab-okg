# dmwm/CRABServer issue #8394: change Task status in DB task table from SUBMITTED to COMPLETED or FAILED when DAG completes

State: closed
Opened: 2024-05-10T14:42:38Z
Closed: 2025-04-11T13:50:20Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8394

## Opening post (belforte, 2024-05-10T14:42:38Z)

basically we want to be able to count running DAG's per user in order to do some task scheduling #7485 

hmm.. maybe we can leave Task status alone and e.g. define later how and when exactly to call it FAILED but add a column with `Dagman Status` ?

In any case this should be one API call in cache_statup.py

Need to be able to also catch FAILED->SUBMITTED transition at crab resubmit time.

## Comment (belforte, 2024-05-10T14:44:33Z)

FYI @mapellidario , please comment as you see fit

## Comment (belforte, 2025-03-06T17:44:50Z)

Best seems a new status column, imitating what `crab status` does atm
```
Status on the CRAB server:	SUBMITTED
Status on the scheduler:	SUBMITTED
```
leave it to `crab status` to combine, but mosty move to the AP all the dag status parsing which now happens in https://github.com/dmwm/CRABClient/blob/5079df8a21cd6acd9768d257fb390551cada6e1d/src/python/CRABClient/Commands/status.py#L350-L411

DAG Status will be `RUNNING|COMPLETED|FAILED`

This leave current task status untouched so there is no danger of messing with NEW/SUBMITTED/RESUBMITTING etc.

## Comment (belforte, 2025-03-06T17:46:03Z)

OTOH understanding what `crab status` does here is way from easy. First time that I try. And I have forgotten how exactly `cache_status.py` works inside the job_wrapper.
