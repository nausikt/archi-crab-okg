# dmwm/CRABServer issue #9426: keep job in queue for some time after PostJob completes

State: closed
Opened: 2026-09-23T15:14:13Z
Closed: 2026-09-24T07:13:47Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9426

## Opening post (belforte, 2026-09-23T15:14:13Z)

I have found several removed jobs where classAds in MONIT are not what we expect from PostJob. As e.g. reported in #9398 

As a possible way to mitigate we can keep jobs in the queue for some time after PostJob ran to give time to the spider to pick up things. It should pick ads from history in case, but... better to be safe.

`LeaveJonInQueue` is initially set to 30 hours after job termination
https://github.com/dmwm/CRABServer/blob/be37a0af0873e3612a646c22ef0a4a3509bc1fd4/src/python/TaskWorker/Actions/DagmanCreator.py#L442-L445
which is OK with the 24h ASO timeout, but should be changed when using ASO-Rucio !!

Then  in PostJob
https://github.com/dmwm/CRABServer/blob/be37a0af0873e3612a646c22ef0a4a3509bc1fd4/src/python/TaskWorker/Actions/PostJob.py#L2983-L2984

Should change to stay in queue for e.g. 30 more minutes (spider runs every 12 min)
