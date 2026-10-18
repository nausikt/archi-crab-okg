# dmwm/CRABServer issue #8958: reduce disk space consumption of tasks that use Rucio as ASO in CI Pipeline

State: closed
Opened: 2025-02-28T11:12:55Z
Closed: 2025-03-11T10:30:14Z
Labels: Area: Code Cleanup, Area: CI/CD, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8958

## Opening post (nausikt, 2025-02-28T11:12:55Z)

See also original issue: https://github.com/dmwm/CRABServer/issues/8887

From @belforte: disk for test ouptuts is filling up fast
abelforte@lxplus813/ruciotransfers-1740666881> rucio list-account-usage crabint1
+------------+-----------+------------+--------------+
| RSE        | USAGE     | LIMIT      | QUOTA LEFT   |
|------------+-----------+------------+--------------|
| T2_CH_CERN | 88.191 GB | 100.000 GB | 11.809 GB    |

hints from Stefano:
- [ ] try not to submit StatusTracking suite all of the times
- [ ] for *Rucio* tasks, reduce from 40 to 10 jobs.
- [ ] (original issue: https://github.com/dmwm/CRABServer/issues/8887) implement the automatic cleanup. Or even better, add something to the pipeline so that rules created by each task are given a 7d lifetime. Default is "no expiration" !

Please @aspiringmind-code helps me get this done, feels free to correct me along the way!

## Comment (belforte, 2025-02-28T11:22:09Z)

be aware of overlap with https://github.com/dmwm/CRABServer/issues/8887

## Comment (nausikt, 2025-02-28T11:23:44Z)

Closed, and working over there then.

## Comment (nausikt, 2025-02-28T11:34:55Z)

I've reopened and revised this issue to address non-overlaps action items properly.
- [ ] add something to the pipeline so that rules created by each task are given a 7d lifetime
- [ ] for Rucio tasks, reduce from 40 to 10 jobs.
- [ ] try not to submit StatusTracking suite all of the times

Notes: https://github.com/dmwm/CRABServer/blob/master/scripts/Utils/DeleteOldRules.py

## Comment (aspiringmind-code, 2025-02-28T12:15:33Z)

As for "try not to submit StatusTracking suite all the time" I can set its default value to false and when someone wants STATUS Tracking they will have to explicitly set it true.

## Comment (nausikt, 2025-02-28T13:13:52Z)

> As for "try not to submit StatusTracking suite all the time" I can set its default value to false and when someone wants STATUS Tracking they will have to explicitly set it true.

> As for "try not to submit StatusTracking suite all the time" I can set its default value to false and when someone wants STATUS Tracking they will have to explicitly set it true.

That's great! it works for me too!. Could you kindly open PR for the changing skip_TS's default value? or would you like me to included in my PR below. 
- [x] for Rucio tasks, reduce from 40 to 10 jobs.
- [x] try not to submit StatusTracking suite all of the times
- [ ] add something to the pipeline so that rules created by each task are given a 7d lifetime

## Comment (aspiringmind-code, 2025-02-28T16:04:08Z)

The default value set to false in [PR](https://github.com/dmwm/CRABServer/pull/8962)

## Comment (nausikt, 2025-03-11T10:33:52Z)

As we discussed in the last meeting, first 2 items are sufficient. the last item could be done gracefully later by  https://github.com/dmwm/CRABServer/issues/8887

## Comment (belforte, 2025-03-11T10:38:30Z)

OTOH, if we set a finite lifetime for rules in the pipeline, later cleanup via crontab does not need to run that often or may even be not needed at all.

## Comment (aspiringmind-code, 2025-03-11T13:17:16Z)

> OTOH, if we set a finite lifetime for rules in the pipeline, later cleanup via crontab does not need to run that often or may even be not needed at all.

It can be as simple as running a cleanup stage in the pipeline. See [here](https://github.com/dmwm/CRABServer/pull/8976)
