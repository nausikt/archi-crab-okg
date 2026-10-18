# dmwm/CRABServer issue #9114: Disable publicatiion and warn users when input dataset is not VALID

State: closed
Opened: 2025-06-25T15:25:19Z
Closed: 2025-06-30T08:24:47Z
Labels: Type: Enhancement, Type: Support, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/9114

## Opening post (belforte, 2025-06-25T15:25:19Z)

as noted in https://cms-talk.web.cern.ch/t/publication-failure/40941/4 in this case publication fails becasue migration is only allowed for VALID datasets.

But getting errors during publication step is impossible to understand for users and make Publisher uselessly stuck.

Indeed problem came back again to support https://cms-talk.web.cern.ch/t/is-dbs-phys03-down/126157?u=belforte

## Comment (belforte, 2025-06-25T15:58:45Z)

as a start,  add a message in
https://github.com/dmwm/CRABServer/blob/c378484de98e554338cfc38b20a94a4498967a71/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L53-L58

## Comment (belforte, 2025-06-25T16:06:50Z)

then "it may be enough" to override `task['tm_publication']` in the `task` dictionary used inside Dagman*py, since the info is then passed to scheduler via the class ad `CRAB_Publish`. But in view of the fact that this is also used in ASO/Rucio and so on, better to exploit the new `edit API`and change  in the DB as well 
https://github.com/dmwm/CRABServer/blob/c378484de98e554338cfc38b20a94a4498967a71/src/python/CRABInterface/RESTTask.py#L494
