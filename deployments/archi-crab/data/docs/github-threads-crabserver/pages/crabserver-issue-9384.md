# dmwm/CRABServer issue #9384: correct CRAB_JobCount  ad for automatic splitting

State: closed
Opened: 2026-08-13T09:26:58Z
Closed: 2026-08-19T14:19:39Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9384

## Opening post (belforte, 2026-08-13T09:26:58Z)

every job has a MY.CRAB_JobCount classAd which is meant to report the number of jobs in the task.
But since it is defined in DagmanCreator and passed to AP via the template JobSubmit object,
it represents the number of jobs created by TaskWorker,
so for automatic splitting is stuck to the number of probe jobs (5).
Need to update it for jobs submitted by automatic splitter sub-dags.

https://github.com/dmwm/CRABServer/blob/1cdeb6c7a7a9817f933cfafc2a018bc7a179c65b/src/python/TaskWorker/Actions/DagmanCreator.py#L381

That value is also added to dagman job classAd in DagmanSubmitter via
https://github.com/dmwm/CRABServer/blob/1cdeb6c7a7a9817f933cfafc2a018bc7a179c65b/src/python/TaskWorker/Actions/DagmanSubmitter.py#L28
https://github.com/dmwm/CRABServer/blob/1cdeb6c7a7a9817f933cfafc2a018bc7a179c65b/src/python/TaskWorker/Actions/DagmanSubmitter.py#L84

Besides being useful in order to decide whether to kill a job after too many ASO errors ( #9383 ) it will be generally good that each job carries the updated value of  number of jobs in task at the time the job was submitted.
