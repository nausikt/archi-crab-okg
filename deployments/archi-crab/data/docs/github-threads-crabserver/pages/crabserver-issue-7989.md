# dmwm/CRABServer issue #7989: TW monitoring - differentiate submitfailed caused by crab system from user errors

State: closed
Opened: 2023-11-01T19:27:12Z
Closed: 2024-07-30T09:11:40Z
Labels: Type: Enhancement, Type: Support, Status: Done, Priority: High, Area: MONIT, Postmortem
URL: https://github.com/dmwm/CRABServer/issues/7989

## Opening post (mapellidario, 2023-11-01T19:27:12Z)

We receive an alert when the number of tasks that failed to be submitted in the last 2h is higher than a certain threshold.

However, tasks fail to be submitted both because of user errors (no quota at destination site, no dataset found in dbs, ...) and because of crab system (3000 running dagmans, crabserver rest could not contact oracle, ... ) or crab dependencies (rucio, ...) outages. This means that in order to monitor crab system availability, we receive false positives [1], which for example made us slow to respond to a recent rucio outage [1].

In order to improve our trust in our alerts, we would a new way of distinguishing tasks that are not submitted because of a system outage from the ones that are not submitted because of a problem with the user request.

Stefano proposed to introduce a new status `submitrefused`, which would have a different meaning from submitfailed :

- 1. `submitfailed` "crab system encountered a generic problem with task submission", which would indicate problems with crab itself or its dependencies
- 2. `submitrefused` "crab could not submit a task because of a problem in the user request"

I suggest that 

- we create a new sql query + function that sets a task to `submitrefused`
- compile a list of task submission failures that would make sense to identify as user-related problems
- check in the code where those failures are triggered and switch to the new function.

---

[1] https://codimd.web.cern.ch/G8BrXmKZQPyfoizEUOCmVQ#

## Comment (belforte, 2023-11-01T21:36:27Z)

No need for a new SQL/API. Code to set task status is already in
https://github.com/dmwm/CRABServer/blob/9cb5d51245477e0bfa68fd2fc14931a620f7df15/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L232-L246
As indicated in there, this is a good chance to move it to some common place, together with other methods which are now replicated here and there.

As to " code where those failures are triggered" we can surely do this a bit at a time starting from the most obnoxious things (stageoutcheck failure and inexisting dataset), the simplest way is probably to add a new Exception to be handled in 
https://github.com/dmwm/CRABServer/blob/9cb5d51245477e0bfa68fd2fc14931a620f7df15/src/python/TaskWorker/Worker.py#L97-L116

## Comment (belforte, 2024-07-23T14:33:58Z)

preliminary code in https://github.com/belforte/CRABServer/tree/add-submitrefused-7989 sets new SUBMITREFUSED status, but does not report reason in the Warnings.

## Comment (belforte, 2024-07-23T21:31:47Z)

<strike>* `uploadWarning()` must be called when the problem is detected before raising `SubmissionRefusedException`</strike>

I changed so that message is uploaded in Handlet.py. In the various places it will be enough to put
`raise SubmissionRefuseException(msg)`

## Comment (belforte, 2024-07-24T19:16:47Z)

WHen StageoutCheck fails, things work now when running using sequential worker (`start.sh -g -d`) but using slaves pool, child processes etc. via `start.sh -g` the task is set to SUBMITFAILED instead of SUBMITREFUSED

I need to understand this before I raise SubmissionRefusedException in other places.

## Comment (belforte, 2024-07-24T19:36:47Z)

FIxed. I need to catch the new Exception also in Worker.py

Now I'd like to put a better message:
```
belforte@lxplus801/TC3> crab status 
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240724_213454
Task name:			240724_193457:belforte_crab_20240724_213454
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITREFUSED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240724_193457%3Abelforte_crab_20240724_213454
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=240724_193457%3Abelforte_crab_20240724_213454&from=1721846097000&to=now
Warning:			CRAB3 refuses to send jobs to grid scheduler for 240724_193457:belforte_crab_20240724_213454. Error message: Permission denied. Can't submit task because write check at destination site fails. Please check that you have write access to destination site and that your quota is not exceeded, use crab checkwrite for more information.
				Copying 85 bytes file:///data/srv/TaskManager/240724193457belfortecrab20240724213454_crab3check.tmp => davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/belforte/240724193457belfortecrab20240724213454_crab3check.tmp
				event: [1721849714458] BOTH   GFAL2:CORE:COPY	LIST:ENTER	
				event: [1721849714458] BOTH   GFAL2:CORE:COPY	LIST:ITEM	file:///data/srv/TaskManager/240724193457belfortecrab20240724213454_crab3check.tmp => davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/belforte/240724193457belfortecrab20240724213454_crab3check.tmp
				event: [1721849714458] BOTH   GFAL2:CORE:COPY	LIST:EXIT	
				event: [1721849714458] BOTH   
				[... message truncated to the first 1000 chars ...]
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240724_213454/crab.log
belforte@lxplus801/TC3> 
```

## Comment (belforte, 2024-07-24T19:56:53Z)

not that it was any better "before"
```text
belforte@lxplus801/TC3> crab status -d ./crab_20240724_215456 
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240724_215456
Task name:			240724_195459:belforte_crab_20240724_215456
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-preprod-tw01
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb-testbed.cern.ch/crabserver/ui/task/240724_195459%3Abelforte_crab_20240724_215456
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=240724_195459%3Abelforte_crab_20240724_215456&from=1721847299000&to=now
Failure message from server:	CRAB3 refuses to send jobs to grid scheduler for 240724_195459:belforte_crab_20240724_215456. Error message: Permission denied. Can't submit task because write check at destination site fails. Please check that you have write access to destination site and that your quota is not exceeded, use crab checkwrite for more information.
				Copying 85 bytes file:///data/srv/TaskManager/240724195459belfortecrab20240724215456_crab3check.tmp => davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/belforte/240724195459belfortecrab20240724215456_crab3check.tmp
				event: [1721850919845] BOTH   GFAL2:CORE:COPY	LIST:ENTER	
				event: [1721850919845] BOTH   GFAL2:CORE:COPY	LIST:ITEM	file:///data/srv/TaskManager/240724195459belfortecrab20240724215456_crab3check.tmp => davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/belforte/240724195459belfortecrab20240724215456_crab3check.tmp
				event: [1721850919845] BOTH   GFAL2:CORE:COPY	LIST:EXIT	
				event: [1721850919845] BOTH   
				[... message truncated to the first 1000 chars ...]
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240724_215456/crab.log
belforte@lxplus801/TC3> 
```

## Comment (belforte, 2024-07-24T19:57:20Z)

let's say that this is a good time to improve

## Comment (belforte, 2024-07-24T20:30:44Z)

better now
```text
belforte@lxplus801/TC3> crab status 
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240724_222942
Task name:			240724_202944:belforte_crab_20240724_222942
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITREFUSED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240724_202944%3Abelforte_crab_20240724_222942
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=240724_202944%3Abelforte_crab_20240724_222942&from=1721849384000&to=now
Warning:			CRAB3 refuses to send jobs to grid scheduler for 240724_202944:belforte_crab_20240724_222942. Error message:
				Permission denied. Can't submit task because write check at destination site fails.
				Please check that you have write access to destination site
				 and that your quota is not exceeded
				 use crab checkwrite for more information.
				Copying 85 bytes file:///data/srv/TaskManager/240724202944belfortecrab20240724222942_crab3check.tmp => davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/belforte/240724202944belfortecrab20240724222942_crab3check.tmp
				gfal-copy error: 1 (Operation not permitted) - DESTINATION MAKE_PARENT HTTP 403 : Permission refused 
				
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240724_222942/crab.log
belforte@lxplus801/TC3> 
```

## Comment (belforte, 2024-07-25T08:45:23Z)

Now that basic is working, let's list places where to switch from SUBMITFAILED to SUBMITREFUSED
- [x] dataset not in DBS
- [x] more than 10K jobs
- [x] splitting did not produce any job
- [x] No locations found for dataset 
- [x] invalid LFN/Block name

## Comment (mapellidario, 2024-07-30T09:11:02Z)

I think we need to advertise this change in cmstalk before deploying. It is possible that some of our users parse the output of crab status after a submission and they grep for "submitfailed".

## Comment (belforte, 2024-07-30T09:30:18Z)

good point. Thanks @mapellidario
