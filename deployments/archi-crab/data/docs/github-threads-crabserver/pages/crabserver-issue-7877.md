# dmwm/CRABServer issue #7877: deploy updated `copycat` functionality

State: open
Opened: 2023-09-14T17:09:14Z
Labels: Priority: Low
URL: https://github.com/dmwm/CRABServer/issues/7877

## Opening post (belforte, 2023-09-14T17:09:14Z)

- [ ] current code which picks a user task (at random) and replays it e.g. to check stageout should be contributed to this repository and casted in such a way that it can be reused for other tests.
- [ ]  also make is a callable, so that new `crab recovery` can use it

## Comment (belforte, 2023-09-14T17:10:14Z)

@mapellidario FYI

## Comment (novicecpp, 2023-09-15T11:09:01Z)

> current code which picks a user task (at random)

My code is not that advance. The list of tasks is export from [Task GlobalView](https://monit-grafana.cern.ch/d/cmsTMGlobal/cms-tasks-monitoring-globalview?orgId=11) and do preprocessing using some heuristic rule (< 2000 jobs, <10% fail, etc.) before feed to cronjob.

Could you explain a bit on the last part `and replays it e.g. to check stageout should be contributed to this repository and casted in such a way that it can be reused for other tests`? 
Do you mean to persist the task somewhere (i.e. put in database or s3) and use it later?

## Comment (belforte, 2023-09-15T12:50:38Z)

I meant to persist the code ! Sorry for bad language,
your heuristic looks more advanced than "random" to me ! Anyhow that  part can surely be tuned on the need of the day,

## Comment (belforte, 2026-05-11T09:12:53Z)

I think we will live w/o this
