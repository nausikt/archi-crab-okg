# dmwm/CRABServer issue #8197: job wrapper chirps exe exit code instead of cmscp one

State: closed
Opened: 2024-01-30T08:49:19Z
Closed: 2025-05-05T14:34:23Z
Labels: Type: Bug, Priority: High, Status: In Progress, Area: JobWrapper
URL: https://github.com/dmwm/CRABServer/issues/8197

## Opening post (belforte, 2024-01-30T08:49:19Z)

```
====== Mon Jan 29 22:28:24 2024: cmscp.py FINISHING (status 60302).

real	0m0.747s
user	0m0.523s
sys	0m0.128s
======== Stageout at Mon Jan 29 22:28:24 GMT 2024 FINISHING (short status 142) ========
======== gWMS-CMSRunAnalysis.sh FINISHING at Mon Jan 29 22:28:24 GMT 2024 on ccwcondor0489 with (short) status 142 ========
Local time: Mon Jan 29 23:28:24 CET 2024
Short exit status: 142
======== Figuring out long exit code of the job for condor_chirp at Mon Jan 29 22:28:24 GMT 2024========
==== Long exit code of the job is 0 ====
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
```

## Comment (belforte, 2024-08-23T10:01:03Z)

was maybe fixed ?

NO!

## Comment (belforte, 2025-04-29T19:34:23Z)

`chirp` is called in https://github.com/dmwm/CRABServer/blob/1d41fa3554c92583a3ad2c03036e74f9d24f83eb/scripts/gWMS-CMSRunAnalysis.sh#L77
where the exit code is picked from `jobReport.exitCode.txt` which is written in [CMSRunAnalysis.py](https://github.com/dmwm/CRABServer/blob/master/scripts/CMSRunAnalysis.py)

Since stageout is only called when exit code is 0
https://github.com/dmwm/CRABServer/blob/1d41fa3554c92583a3ad2c03036e74f9d24f83eb/scripts/gWMS-CMSRunAnalysis.sh#L243-L245

it should be safe to overwrite the content of  `jobReport.exitCode.txt` e.g. in
https://github.com/dmwm/CRABServer/blob/1d41fa3554c92583a3ad2c03036e74f9d24f83eb/scripts/gWMS-CMSRunAnalysis.sh#L272-L274
without touching the dreaded `cmscp.py`
