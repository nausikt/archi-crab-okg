# dmwm/CRABServer issue #9138: change locking policy for MINIAOD*

State: closed
Opened: 2025-08-01T10:37:17Z
Closed: 2025-08-04T13:25:10Z
Labels: Type: Enhancement, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9138

## Opening post (belforte, 2025-08-01T10:37:17Z)

see https://its.cern.ch/jira/browse/CMSTRANSF-119

pasting relevant text below

CRAB already creates rules for datasets that are used as analysis input with copies=1 and 1 month lifetime

DM  would like CRAB to create  rules with copies=2 and 1 year lifetime for MINIAOD* datasets only.
They would like to have it as soon as possible.
CRAB can use the "keep_miniaod=True" as RSE expression and "dm_weight" as the weight

## Comment (belforte, 2025-08-01T10:38:52Z)

@aspiringmind-code do you want to give it a shot  ? Or do you prefer that I do it ?

## Comment (aspiringmind-code, 2025-08-01T12:01:38Z)

Yes, sure.

## Comment (belforte, 2025-08-01T12:07:28Z)

hopefully all that we need is to change
https://github.com/dmwm/CRABServer/blob/9aa518ddab0e87a19a968d8e32d7805bf5273c80/src/python/TaskWorker/Actions/RucioActions.py#L285-L288
introducing  something like
```python
if 'MINIAOD' in containerDid['name']:
   rseExpression='keep_miniaod=True'
   copies=2,
   weight=`dm_weight`,
   lifetime=3600*24*365
```
and of course change the signature for `createOrReuseRucioRule` and propagate args, When I coded initially I did not make it fully general. Another possibility is to do the change inside  `createOrReuseRucioRule`, where the actual call to Rucio client is done, but having to the `if MINIAOD*` in the `lockData` is more clear.
