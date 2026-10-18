# dmwm/CRABServer issue #9206: reduce memory limit for 1 core jobs

State: closed
Opened: 2025-10-09T11:30:09Z
Closed: 2025-10-10T07:55:26Z
Labels: Type: Enhancement, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9206

## Opening post (belforte, 2025-10-09T11:30:09Z)

we have evidence that many user specify the maximul allowed (5GB) even if their jobs only use 1~2 GB or RAM.
Usual problem of "sticking, copied/pasted configuration".

US people pointed out that in there alone this leads to as many idle cores as a a full T2 !!!

We converged on the following approach:
 1) Reduce Max for 1 core from 5 to 3 GB in initial submission
 2) Allow user to ask more (up to 5) in crab resubmit
 3) Possibly, at a later time,  make 2) automatic

No changes for multicore.

This issue will track 1) and 2) if we decide to implement 3), will open a new ad-hoc one.

## Comment (mmascher, 2025-10-09T11:57:20Z)

Feel free to point people to https://cmssi.docs.cern.ch/policies/memory/ for explanations. I'll need to update it once this is done.

## Comment (belforte, 2025-10-09T12:07:29Z)

thanks Marco. Done.

## Comment (belforte, 2025-10-09T12:16:33Z)

with new code:

```console
belforte@lxplus806/TC3> crab status 
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20251009_141243
Task name:			251009_121246:belforte_crab_20251009_141243
Grid scheduler - Task Worker:	N/A yet - crab-dev-tw01
Status on the CRAB server:	SUBMITREFUSED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/251009_121246%3Abelforte_crab_20251009_141243
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=251009_121246%3Abelforte_crab_20251009_141243&from=1760008366000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_SGrid_Bristol']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			Task requests 4000 MB of memory, above the allowed maximum of 3000 for a 1 core(s) job.
				    Please see https://cmssi.docs.cern.ch/policies/memory/ 
				
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20251009_141243/crab.log
belforte@lxplus806/TC3> 
```

Still have to check  resubmission

## Comment (belforte, 2025-10-09T13:22:50Z)

If a user issues  a `crab resubmit --maxmemory=7000` (e.g.) I am going to set status `RESUBMITFAILED` so to
allow user to issue `crab resubmit --maxmemory=5000` (e.g.). While if I raised `sunmissionRefused` (like I do at initial submission) no further `resubmit` would be possible.

## Comment (belforte, 2025-10-09T13:23:47Z)

OK. Tested in crab-dev-tw01
