# dmwm/CRABServer issue #9441: JobWrapper fails to report error in initial bootstrap

State: open
Opened: 2026-10-13T09:30:30Z
Labels: Type: Bug, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9441

## Opening post (belforte, 2026-10-13T09:30:30Z)

see example below.
Then PostJob fails because job report could not be found, but we end with a job which is retried even if exit code was 0. Confusing !

```text
timeleft  : 133:07:37
uri       : voms-cms-auth.cern.ch:15000
======== PROXY INFORMATION FINISH at Wed Oct  7 07:07:52 GMT 2026 ========
======== TOKEN SETUP START at Wed Oct  7 07:07:52 GMT 2026 ========
======== TOKEN SETUP FINISH at Wed Oct  7 07:07:52 GMT 2026 ========
======== CMSRunAnalysis.sh at Wed Oct  7 07:07:52 GMT 2026 STARTING ========
======== CMSRunAnalysis.sh STARTING at Wed Oct  7 07:07:52 GMT 2026 ========
Local time : Wed Oct  7 09:07:52 CEST 2026
Current system : Linux hk2n1219.localdomain 5.14.0-570.140.1.el9_6.x86_64 #1 SMP PREEMPT_DYNAMIC Mon Sep 7 09:47:52 EDT 2026 x86_64 x86_64 x86_64 GNU/Linux
Current processor: model name	: AMD EPYC 9655 96-Core Processor
======== CMS environment load starting at Wed Oct  7 07:07:52 GMT 2026 ========
Error during job bootstrap: VO_CMS_SW_DIR, OSG_APP, CVMFS or /cvmfs were not found.
  Because of this, we can't load CMSSW. Not good.

real	0m0.015s
user	0m0.006s
sys	0m0.011s
CMSRunAnalysis.sh complete at Wed Oct  7 07:07:52 GMT 2026 with (short) exit status 251
======== CMSRunAnalysis.sh at Wed Oct  7 07:07:52 GMT 2026 FINISHING ========
======== User Application failed (exit code =  251) No stageout will be done
======== gWMS-CMSRunAnalysis.sh FINISHING at Wed Oct  7 07:07:52 GMT 2026 on hk2n1219.localdomain with (short) status 251 ========
Local time: Wed Oct  7 09:07:52 CEST 2026
Short exit status: 251
Application exit status: 0
======== Figuring out long exit code of the job for condor_chirp at Wed Oct  7 07:07:52 GMT 2026========
==== Failed to load the long exit code from jobReport.exitCode.txt. Falling back to short exit code ====
==== Short exit code of the job is 0 ====
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
======== Checking execution of user application (cmsRun or scriptExe) Wed Oct  7 07:07:52 GMT 2026========
the file cmsRun-stdout.log.tmp does **NOT** exist
the file cmsRun-stdout.log does **NOT** exist
======== Checking execution of cmsRun Wed Oct  7 07:07:52 GMT 2026========
the file FrameworkJobReport.xml does **NOT** exist
the file jobReport.json.24 exists
the file jobReport.exitCode.txt does **NOT** exist
======== Finished - Checking execution of user application Wed Oct  7 07:07:52 GMT 2026========
======== Figuring out long exit code of the job for condor_chirp at Wed Oct  7 07:07:52 GMT 2026========
==== Failed to load the long exit code from jobReport.exitCode.txt. Falling back to short exit code ====
==== Short exit code of the job is 0 ====
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
Job started:   1791356871 ,  Wed Oct 7 07:07:51 GMT 2026
Job finished:  1791356872 ,  Wed Oct 7 07:07:52 GMT 2026
Job Running time in seconds:  1
Job runtime is less than 1 minute. Sleeping  59
```

## Comment (belforte, 2026-10-14T10:44:55Z)

looks like this `if` is wrong
https://github.com/dmwm/CRABServer/blob/30286f7d5b215860e5b6da0edda0553b446d813d/scripts/job_wrapper/gWMS-CMSRunAnalysis.sh#L57-L60
Was introduced recently in https://github.com/dmwm/CRABServer/pull/9358
