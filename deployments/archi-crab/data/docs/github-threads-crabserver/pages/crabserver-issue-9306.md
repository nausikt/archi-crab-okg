# dmwm/CRABServer issue #9306: FRONTIER_ID env.var. is not set anymore in JobWrapper

State: closed
Opened: 2026-04-27T16:47:10Z
Closed: 2026-04-28T09:27:08Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9306

## Opening post (belforte, 2026-04-27T16:47:10Z)

change in https://github.com/dmwm/CRABServer/commit/367e5692451b821683af7404cece63eed280d6ce in Jam 2-25 broke the fix for #8366  which was done in August 2024 :-(

The problem is that I changed classAd name from `CRAB_ReqName` to `CRAB_Reqname` to make it consistent with the many places where it is used in HTC classAd manipulations and avoid confusion, but in the job wrapper we have case sensitive `grep` in the classAd dump file.

So the $FRONTIER_ID is now set to the useless `CRAB-` string, as Frontier support people just found out

```
Subject: 	CRAB's setting of FRONTIER_ID
Date: 	Mon, 27 Apr 2026 10:18:32 -0500
From: 	Dave Dykstra <dwd@cern.ch>
To: 	Stefano Belforte <stefano.belforte@cern.ch>
CC: 	Carl Vuosalo <carl.vuosalo@cern.ch>, Luis Simas <luis.simas@cern.ch>, Stephan Lammel <stephan.lammel@cern.ch>


Hi Stefano,

We're looking at the CMS CERN squid logs to try to understand some periods of unusually high bandwidth usage, and found that CRAB is no longer setting a useful value in $FRONTIER_ID in jobs that access frontier. The value in the log is always just "CRAB-" rather than some identifier that helps us figure out which set of jobs is doing any particular behavior. Do you have any insight into that, and can it be fixed?

Thanks,

Dave
```

All those `grep` should be case-insensitive, following the HTCondor feature that all classAd comparisons are case-insensitive.
