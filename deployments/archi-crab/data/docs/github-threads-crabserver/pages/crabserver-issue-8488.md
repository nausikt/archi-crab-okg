# dmwm/CRABServer issue #8488: cleanup TaskType names

State: closed
Opened: 2024-06-11T21:03:36Z
Closed: 2024-08-19T16:44:12Z
Labels: Status: Done, Priority: High, Area: Code Cleanup, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8488

## Opening post (belforte, 2024-06-11T21:03:36Z)

in the context of Modernize HTC calls
see https://github.com/dmwm/CRABServer/issues/8337#issuecomment-2161576067

- [x] rename TaskType ad to CRAB_DAGType
- [x] rename ROOT type to MAIN. So that dagman jobs will have CRAB_DagType in ["MAIN",  "PROCESSING", "TAIL"]. "normal" tasks will only have "MAIN". "automatic" will use "MAIN" for running probes, followed by "PROCESSING" and up to 3 "TAIL".
But I am still not happy here. ROOT is more descriptive for a DAG which can be either the full thing standalone or the probe step for automatic splitting. Maybe "BASE" ?
I will start with renaming the classAd, at least it will make it easier later  on to identify where it is used and possibly change the value.

**BEWARE these changes will not be backward compatible ! i.e. `crab kill` and `crab resubmit` will not work on tasks which have TaskType but not CRAB_DAGType.**
 - [x] add a backward-compatibility layer (to be remove after 2 months in production)

Note: ROOT is assigned in initial submission (so it i the same for everybody) in DagamSubmitter. Later on PreDag uses the stage name when it submits the various subdags. Stage name is set in DagmanCreator and used in PreDag and PreJob

List of possible values. Note that CRAB_DAGType is the classAd of a job !! Simply it takes a non trivial value when the job runs in the Scheduler universe to execut a DagMan

|kind of job | universe |CRAB_DAGType | stage name  |
|-|-|-|-|
| main Dagman w/o automatic splitting | scheduler (7) | BASE | conventional |
| main Dagman with automatic splitting | scheduler (7) | BASE  | probe |
| grid job | vanilla (5) | Job | not used |
| task_process | local (12) | undefined | not used |
| processing subDag | scheduler (7) | PROCESSING | processing |
| tail subDag | scheduler (7) |TAIL | tail |

Possible alternative names for ROOT:  MAIN , BASE



TaskType ad is defined in
https://github.com/dmwm/CRABServer/blob/3c826e3856dfb602150c817b4ddf6aa8e8e4ecf2/src/python/TaskWorker/Actions/DagmanSubmitter.py#L529
and
https://github.com/dmwm/CRABServer/blob/43208f8307874dab3d255415b62aa45c0cd1e32f/src/python/TaskWorker/Actions/DagmanCreator.py#L104

and in case of automatic splitting in
https://github.com/dmwm/CRABServer/blob/3c826e3856dfb602150c817b4ddf6aa8e8e4ecf2/src/python/TaskWorker/Actions/PreDAG.py#L338

the `stage` in PreDAG is passed as argument when PreDAG is called during Dag execution:
https://github.com/dmwm/CRABServer/blob/3c826e3856dfb602150c817b4ddf6aa8e8e4ecf2/src/python/TaskWorker/Actions/DagmanCreator.py#L56

and the code which managed the various DAGs creation is the somehow cryptic
https://github.com/dmwm/CRABServer/blob/3c826e3856dfb602150c817b4ddf6aa8e8e4ecf2/src/python/TaskWorker/Actions/DagmanCreator.py#L998-L1024

TaskType ad is also used in
https://github.com/dmwm/CRABServer/blob/43208f8307874dab3d255415b62aa45c0cd1e32f/scripts/task_process/task_proc_wrapper.sh#L73-L77

https://github.com/dmwm/CRABServer/blob/43208f8307874dab3d255415b62aa45c0cd1e32f/scripts/AdjustSites.py#L452

https://github.com/dmwm/CRABServer/blob/43208f8307874dab3d255415b62aa45c0cd1e32f/src/python/TaskWorker/Actions/DagmanResubmitter.py#L73

https://github.com/dmwm/CRABServer/blob/43208f8307874dab3d255415b62aa45c0cd1e32f/src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py#L153

https://github.com/dmwm/CRABServer/blob/43208f8307874dab3d255415b62aa45c0cd1e32f/src/python/TaskWorker/Actions/DagmanKiller.py#L63

https://github.com/dmwm/CRABServer/blob/43208f8307874dab3d255415b62aa45c0cd1e32f/src/python/TaskWorker/Actions/DagmanKiller.py#L75

## Comment (belforte, 2024-06-12T07:59:46Z)

do not put priority very high, since in the end it is quite some work, need to changes a lot of places, for "small" gain
