# dmwm/CRABServer issue #7767: add time range to CrabServer UI MONIT pointer

State: closed
Opened: 2023-07-17T10:28:04Z
Closed: 2023-09-18T09:47:50Z
Labels: Type: Enhancement, Type: Support, Priority: High, Status: Available
URL: https://github.com/dmwm/CRABServer/issues/7767

## Opening post (belforte, 2023-07-17T10:28:04Z)

since the default is 30min, now it almost always fails to find the task as it builts URL like

https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=santocch&var-task=230714_100021:santocch_crab_singlemu-2017f

Need the same as in `crab status`

https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=santocch&var-task=230714_100021%3Asantocch_crab_singlemu-2017f&from=1689325221000&to=now

where from is in `msec` fom epoch, see
https://github.com/dmwm/CRABClient/blob/00d5e3ced6389fe328fe429eb41941a2a6a7f1d6/src/python/CRABClient/Commands/status.py#L460-L470

## Comment (belforte, 2023-09-14T08:32:05Z)

@mapellidario @novicecpp this requires changes to
https://github.com/dmwm/CRABServer/blob/a344356b0708b0a6b9f181eb34715252afa63a04/src/script/task_info.js#L583-L584

AFAIU: extract task submission time from part of taskname before `:`, convert in msec from epoch and add it to the URL.
But I do not know `js` (JavaScript ?) and would take me a while to learn how to manipulate strings and arithmetic here. Does  maybe one of you know this stuff already and could assign to himself and do ?
It always annoys me when I need to look at someones taks and hit this thing that I click on the button and the task info is partilally available at best. If then I change the data in grafana, it shows me all tasks submitted since then by that user and I need to find the right one :-(

## Comment (novicecpp, 2023-09-14T08:35:04Z)

The trick is move time range to 30 days. Always work for me.

I will do.

## Comment (belforte, 2023-09-14T08:40:54Z)

not all of the times for me. It may depend on whether the task has jobs submitted in last 30min so that it appears in the initial dashboard and can stick in the selection menu.

thanks !
