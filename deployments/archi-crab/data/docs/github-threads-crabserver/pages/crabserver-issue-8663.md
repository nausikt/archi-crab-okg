# dmwm/CRABServer issue #8663: add an API (URL) to retrieve list of SUBMITREFUSED in last N minutes

State: closed
Opened: 2024-08-28T13:22:44Z
Closed: 2024-09-19T11:57:40Z
Labels: Type: Enhancement, Type: Support
URL: https://github.com/dmwm/CRABServer/issues/8663

## Opening post (belforte, 2024-08-28T13:22:44Z)

pretty much like
https://cmsweb.cern.ch/crabserver/prod/task?subresource=lastfailures&minutes=60
But for tasks in SUBMITREFUSED and instead of `tm_task_failure` print `tm_task_warnings` .
[example](https://cmsweb-testbed.cern.ch/crabserver/ui/task/240828_131912%3Abelforte_crab_20240828_151859) of such a task

hint:
* grep for `lastfailures` in repository source
