# dmwm/CRABServer issue #7586: JobWrapper elapsed time computation is wrong

State: closed
Opened: 2023-04-12T08:09:45Z
Closed: 2023-04-19T11:34:26Z
Labels: Type: Bug, Priority: High, Area: JobWrapper
URL: https://github.com/dmwm/CRABServer/issues/7586

## Opening post (belforte, 2023-04-12T08:09:45Z)

example from one job stdout:
```
======== gWMS-CMSRunAnalysis.sh STARTING at Tue Apr 11 22:15:46 GMT 2023 on ng1052.vampire ========
[...]
======== gWMS-CMSRunAnalysis.sh FINISHING at Tue Apr 11 22:35:21 GMT 2023 on ng1052.vampire with (short) status 0 ========
Local time: Tue Apr 11 17:35:21 CDT 2023
Short exit status: 0
======== Figuring out long exit code of the job for condor_chirp at Tue Apr 11 22:35:21 GMT 2023========
==== Long exit code of the job is 0 ====
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
Job Running time in seconds:  10
Job runtime is less than 1 minute. Sleeping  50

```

## Comment (belforte, 2023-04-12T08:12:58Z)

@mapellidario I believe that this was correct at the time I introduced the final sleep time, but have no idea when it started to go wrong. It is not something that we usually look at.
Anyhow, since jobWrapper is in your hands now.. please have a look. I set priority high because it is not nice to add O(1 minute) of sleep time to good jobs !

## Comment (mapellidario, 2023-04-12T08:17:39Z)

Could you add a reference to the job log?

 I suspect that the pset-tweaking is not accounted for in the logic that decides whether to sleep for 1min

## Comment (belforte, 2023-04-12T08:24:14Z)

That was from last Jenkins run:
https://cmsweb.cern.ch:8443/scheddmon/0137/cmsbot/230411_221356:cmsbot_crab_Jenkins_CMSSW_13_0_X_2023-04-11-2300_el8_amd64_gcc11_2024/job_out.1.0.txt

But I had noticed this initially in a user job
https://cmsweb.cern.ch:8443/scheddmon/0197/mhuwiler/230411_123230:mhuwiler_crab_BtoDstarDsInclUpdated_firstprod_20230411_143217/job_out.1.0.txt
where anyhow application execution took ~15 mins
```
==== ScriptEXE Execution started at Tue Apr 11 12:54:39 2023 ====
==== ScriptEXE Execution completed at Tue Apr 11 13:08:18 2023 ====
```

## Comment (belforte, 2023-04-12T08:25:53Z)

same for the Jenkins job, the cmsRun step took 17 minutes ! We must have some stupid bug somewhere
