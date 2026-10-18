# dmwm/CRABServer issue #8938: output from automatic split probe jobs is not discarded

State: closed
Opened: 2025-02-19T16:12:44Z
Closed: 2025-02-27T13:08:30Z
Labels: Type: Bug, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8938

## Opening post (belforte, 2025-02-19T16:12:44Z)

see https://cmsweb.cern.ch/crabserver/ui/task/250217_154906%3Acerminar_crab_DoublePhoton_FlatPt-1To100_PU200

while transfer tab in there and `crab geteoutput --dump` only show processing and tail jobs, user showed me that the probe jobs output were also present in the destination directory.

One possibility is that this is due to direct stageout from WN in case the job ran at same site as destination.

It may even be that it has been like this since a while... need to check.

## Comment (belforte, 2025-02-19T16:18:48Z)

indeed from one probe job stdout
```text

======== Stageout at Mon Feb 17 16:17:02 GMT 2025 STARTING ========
====== Mon Feb 17 16:17:03 2025: cmscp.py STARTING.
The user has not specified to transfer the log files. No log files stageout (nor log files metadata upload) will be performed.
Stageout policy: local, remote
SRC site T2_CH_CERN has davs ? True. Has gsiftp ? False.
DST site T2_CH_CERN has davs ? True. Has gsiftp ? False.
====== Mon Feb 17 16:17:03 2025: Starting job report validation.
Job report seems ok (it has the expected structure).
Retrieved payload exit code ('jobExitCode') = 0 from job report.
Retrieved job wrapper exit code ('exitCode') = 0 from job report.
====== Mon Feb 17 16:17:03 2025: Finished job report validation (status 0).
Job execution site is the same as destination site. Changing stageout policy.
New stageout policy: remote, local
====== Mon Feb 17 16:17:03 2025: Starting to check if user output files exist.
Output file inputs140X.root exists.
====== Mon Feb 17 16:17:03 2025: Finished to check if user output files exist (status 0).
====== Mon Feb 17 16:17:03 2025: Starting to check if user output files are in job report.
Output file inputs140X.root found in job report.
====== Mon Feb 17 16:17:03 2025: Finished to check if user output files are in job report (status 0).
====== Mon Feb 17 16:17:03 2025: Starting initialization of stageout manager for local stageouts.
       -----> Stageout manager log start
INFO:root:StageOutMgr::__init__()
INFO:root:==== Stageout configuration start ====
INFO:root:
There are 1 stage out definitions.
INFO:root:
Stage out to : T2_CH_CERN using: gfal2

[...]

Copying 355941281 bytes file:///srv/inputs140X.root => davs://eoscms.cern.ch:443/eos/cms/store/group/cmst3/group/l1tr/cerminar/l1teg/fpinputs/DoublePhoton_FlatPt-1To100-gun/DoublePhoton_FlatPt-1To100_PU200_142Xv0/250217_154906/0000/inputs140X_0-1.root
```

## Comment (belforte, 2025-02-19T17:07:03Z)

` CRAB_localOutputFiles` is passed to the job via the `VARS` command in the DAG. Here's from Master branch

https://github.com/dmwm/CRABServer/blob/2283a7b9d4c342a78b16ec9ce4445abd9f236a9c/src/python/TaskWorker/Actions/DagmanCreator.py#L64

for the good task, the `RunJos.dag` file has this line
```
VARS Job0-1 My.CRAB_localOutputFiles="\"\""
```
full spec for one probe job node is
```text
JOB Job0-1 Job.0-1.submit
SCRIPT  PRE  Job0-1 dag_bootstrap.sh PREJOB $RETRY 0-1 250219_162741:belforte_crab_20250219_172737 crab-preprod-tw01.cern.ch probe
SCRIPT DEFER 4 1800 POST Job0-1 dag_bootstrap.sh POSTJOB $JOBID $RETURN $RETRY $MAX_RETRIES 250219_162741:belforte_crab_20250219_172737 0-1 /store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/crab_20250219_172737/250219_162741/0000 /store/user/belforte/GenericTTbar/crab_20250219_172737/250219_162741/0000 cmsRun_0-1.log.tar.gz probe 
#PRE_SKIP Job0-1 3
RETRY Job0-1 2 UNLESS-EXIT 2
VARS Job0-1 count="0-1"
# following 3 classAds could possibly be moved to Job.submit but as they are job-dependent
# would need to be done in the PreJob... doing it here is a bit ugly, but simpler
VARS Job0-1 My.CRAB_localOutputFiles="\"\""
VARS Job0-1 My.CRAB_DataBlock="\"/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM#35197562-76e3-11e7-a0c8-02163e00d7b3\""
VARS Job0-1 My.CRAB_Destination="\"davs://eoscms.cern.ch:443/eos/cms/store/user/belforte/GenericTTbar/crab_20250219_172737/250219_162741/0000/log/cmsRun_0-1.log.tar.gz\""
ABORT-DAG-ON Job0-1 3
```

## Comment (belforte, 2025-02-19T17:48:39Z)

But I find the same
```
VARS Job0-1 My.CRAB_localOutputFiles="\"\""
```
also when using crabtaskworker:v3.250215-stable which was the same TW used by the problematic task reported above.

I am waiting for those jobs to run (at CERN) to see what's in job stdout ads...

## Comment (belforte, 2025-02-19T20:27:02Z)

I need to make sure that I use a PSet which does produce output files :-(

## Comment (belforte, 2025-02-19T20:42:54Z)

I have initially focused on `CRAB_localOutputFiles` classAd. If it is empty if causes cmscp.py to do nothing. But it is set with the output file name in DAG file for both v3.250109 (current prod TW) and v3.250215 (used in the bad task in initial report).

But my jobs haven't run at CERN yet to see if local stageout was performed. pff...

## Comment (belforte, 2025-02-19T20:47:14Z)

one sure thing is that output transfer for probe jobs is disabled in PostJob, i.e. no ASO.

https://github.com/dmwm/CRABServer/blob/2283a7b9d4c342a78b16ec9ce4445abd9f236a9c/src/python/TaskWorker/Actions/PostJob.py#L2621-L2630

## Comment (belforte, 2025-02-19T21:07:13Z)

from a quick look at cmscp.py, the relevant classAd should be `CRAB_TransferOutputs`

things get interesting. Looking at how it is set in submit files for probes

* PRODUCTION
```console
belforte@vocms059/SPOOL_DIR> grep v3 TaskWorker/__init__.py 
__version__ = "v3.250109.patch1" #Automatically added during build process
belforte@vocms059/SPOOL_DIR> grep CRAB_TransferOutputs *0-*submit
Job.0-1.submit:+CRAB_TransferOutputs = 0
Job.0-2.submit:+CRAB_TransferOutputs = 0
Job.0-3.submit:+CRAB_TransferOutputs = 0
Job.0-4.submit:+CRAB_TransferOutputs = 0
Job.0-5.submit:+CRAB_TransferOutputs = 0
belforte@vocms059/SPOOL_DIR>
belforte@vocms059/SPOOL_DIR> grep CRAB_TransferOutputs Job.submit
belforte@vocms059/SPOOL_DIR> 
```

* NEW
```console
belforte@vocms0194/SPOOL_DIR> grep v3 TaskWorker/__init__.py 
__version__ = "v3.250215" #Automatically added during build process
belforte@vocms0194/SPOOL_DIR> grep CRAB_TransferOutputs *0-*submit
Job.0-1.submit:My.CRAB_TransferOutputs = 0
Job.0-1.submit:My.CRAB_TransferOutputs = 1
Job.0-2.submit:My.CRAB_TransferOutputs = 0
Job.0-2.submit:My.CRAB_TransferOutputs = 1
Job.0-3.submit:My.CRAB_TransferOutputs = 0
Job.0-3.submit:My.CRAB_TransferOutputs = 1
Job.0-4.submit:My.CRAB_TransferOutputs = 0
Job.0-4.submit:My.CRAB_TransferOutputs = 1
Job.0-5.submit:My.CRAB_TransferOutputs = 0
Job.0-5.submit:My.CRAB_TransferOutputs = 1
belforte@vocms0194/SPOOL_DIR> 
belforte@vocms0194/SPOOL_DIR> grep CRAB_TransferOutputs Job.submit
My.CRAB_TransferOutputs = 1
belforte@vocms0194/SPOOL_DIR> 
```

It seems that new code inserts `My.CRAB_TransferOutputs = 1` in the common Job.submit template while before it was left to PreJob 
https://github.com/dmwm/CRABServer/blob/2283a7b9d4c342a78b16ec9ce4445abd9f236a9c/src/python/TaskWorker/Actions/PreJob.py#L320-L321

## Comment (belforte, 2025-02-19T21:27:47Z)

bloody mess.

IIUC code before the "refactoring",  `CRAB_TransferOutputs` ad was not put in Job.submit by DagmanCreator, but passed and ad to the dag bootstrap by DagmanSubmitter to be later used in PreJob.

One clear goal  of the refactoring make explicit all such obscure information passing. I.e. I could move 
https://github.com/dmwm/CRABServer/blob/2283a7b9d4c342a78b16ec9ce4445abd9f236a9c/src/python/TaskWorker/Actions/DagmanCreator.py#L392
to after the Job.submit file was created, after this comment
https://github.com/dmwm/CRABServer/blob/2283a7b9d4c342a78b16ec9ce4445abd9f236a9c/src/python/TaskWorker/Actions/DagmanCreator.py#L1142-L1143

Another option could be to enforce that PreJob overrides existing ad in Job.submit by changing
https://github.com/dmwm/CRABServer/blob/2283a7b9d4c342a78b16ec9ce4445abd9f236a9c/src/python/TaskWorker/Actions/PreJob.py#L352-L354
so that `new_submit_text` is added after existing file, rather then the other way around. I have no idea why current code is like that.
But so far I have hesitated to change code w/o a full understanding, maybe there were reasons for current implementation ?

## Comment (belforte, 2025-02-19T22:04:32Z)

OK. I have submitte an auto-split task to v3.250215 with no sitewhitelist and indeed all jobs performed local stageout.
https://cmsweb-test2.cern.ch/crabserver/ui/task/250219_212948%3Abelforte_crab_20250219_222943

```console
belforte@lxplus802/TC3> crab status -d ./crab_20250219_222943  --long 
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250219_222943
Task name:			250219_212948:belforte_crab_20250219_222943
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01

[...]

 Job State        Most Recent Site        Runtime   Mem (MB)      CPU %    Retries   Restarts      Waste       Exit Code
 0-1 no output    T1_US_FNAL              0:23:37       1494         60          0          0    0:00:08               0
 0-2 no output    T1_FR_CCIN2P3           0:16:01       1196         90          0          0    0:00:08               0
 0-3 no output    T1_FR_CCIN2P3           0:16:12       1207         90          0          0    0:00:09               0
 0-4 no output    T1_FR_CCIN2P3           0:16:24       1444         86          0          0    0:00:09               0
 0-5 no output    T1_RU_JINR              0:18:35       1086         79          0          0    0:00:09               0
```


probe 0-1 ran at FNAL where local stage out failed and the file was indeed pushed to CERN
```console
belforte@lxplus802/~> ls /eos/cms/store/user/belforte/GenericTTbar/crab_20250219_222943/250219_212948/0000
kk_0-1.root
belforte@lxplus802/~> 
```

## Comment (belforte, 2025-02-19T22:18:10Z)

same task submitted to prod tw (v3.250109.patch1)
https://cmsweb.cern.ch/crabserver/ui/task/250219_220503%3Abelforte_crab_20250219_230459

indeed now
```console

belforte@vocms059/250219_220503:belforte_crab_20250219_230459> condor_q -con crab_reqname==\"250219_220503:belforte_crab_20250219_230459\" -af jobuniverse jobstatus CRAB_TransferOutputs
7 2 1
12 2 undefined
5 2 0
5 2 0
5 2 0
5 2 0
5 2 0
belforte@vocms059/250219_220503:belforte_crab_20250219_230459> 
```

## Comment (belforte, 2025-02-20T10:11:54Z)

* job log for probe jobs on  prod tw (v3.250109.patch1) https://cmsweb.cern.ch/scheddmon/059/belforte/250219_220503:belforte_crab_20250219_230459/job_out.0-1.0.txt
```text
[...]

== JOB AD: CRAB_TransferOutputs = 0

[...]

======== Stageout at Wed Feb 19 22:25:21 GMT 2025 STARTING ========
====== Wed Feb 19 22:25:22 2025: cmscp.py STARTING.
The user has not specified to transfer the log files. No log files stageout (nor log files metadata upload) will be performed.
The user has specified to not transfer the output files. No output files or logs stageout (nor output files metadata upload) will be performed.
Stageout wrapper has no work to do. Finishing here.
Setting stageout wrapper exit info to {'exit_code': 0, 'exit_acronym': 'OK', 'exit_msg': 'OK'}.
Cannot retrieve the job exit code from the job report (does None exist?).
====== Wed Feb 19 22:25:22 2025: cmscp.py FINISHING (status 0).

real	0m0.864s
user	0m0.425s
sys	0m0.171s
======== Stageout at Wed Feb 19 22:25:22 GMT 2025 FINISHING (short status 0) ========
======== gWMS-CMSRunAnalysis.sh FINISHING at Wed Feb 19 22:25:22 GMT 2025 on ccwcondor0678 with (short) status 0 ========
```

* probe job log for  v3.250215 https://cmsweb.cern.ch:8443/scheddmon/059/belforte/250219_212948:belforte_crab_20250219_222943/job_out.0-1.0.txt
```text
[...]

== JOB AD: CRAB_TransferOutputs = 1

[...]

======== Stageout at Wed Feb 19 21:47:58 GMT 2025 STARTING ========
====== Wed Feb 19 21:47:58 2025: cmscp.py STARTING.
The user has not specified to transfer the log files. No log files stageout (nor log files metadata upload) will be performed.
Stageout policy: local, remote
SRC site T1_US_FNAL has davs ? True. Has gsiftp ? False.
DST site T2_CH_CERN has davs ? True. Has gsiftp ? False.
====== Wed Feb 19 21:47:59 2025: Starting job report validation.
Job report seems ok (it has the expected structure).
Retrieved payload exit code ('jobExitCode') = 0 from job report.
Retrieved job wrapper exit code ('exitCode') = 0 from job report.
====== Wed Feb 19 21:47:59 2025: Finished job report validation (status 0).
====== Wed Feb 19 21:47:59 2025: Starting to check if user output files exist.
Output file kk.root exists.
====== Wed Feb 19 21:47:59 2025: Finished to check if user output files exist (status 0).
====== Wed Feb 19 21:47:59 2025: Starting to check if user output files are in job report.
Output file kk.root found in job report.
====== Wed Feb 19 21:47:59 2025: Finished to check if user output files are in job report (status 0).
====== Wed Feb 19 21:47:59 2025: Starting initialization of stageout manager for local stageouts.
```

CONCLUSION
**relevant classAd is indeed  `CRAB_TransferOutputs` which is not set to 0 for probe jobs in latest code**

## Comment (belforte, 2025-02-20T11:37:09Z)

OTOH.. since  `CRAB_TransferOutputs` is used in the Job Wrapper, why should it not be present in Job.submit ? PreJob is there exactly to customize it for each job and already has code to take care
https://github.com/dmwm/CRABServer/blob/2283a7b9d4c342a78b16ec9ce4445abd9f236a9c/src/python/TaskWorker/Actions/PreJob.py#L320

!!!!!!!!!!!!!

## Comment (belforte, 2025-02-20T12:07:46Z)

So I will go for

PreJob adds its stuff AFTER the common Job.submit template.  Reversing Line 354 here
https://github.com/dmwm/CRABServer/blob/2283a7b9d4c342a78b16ec9ce4445abd9f236a9c/src/python/TaskWorker/Actions/PreJob.py#L352-L354

## Comment (belforte, 2025-02-20T13:16:15Z)

rats. it did not work !
lines in Job.0-*.submit are in the expected order
```console
belforte@vocms059/cluster10126689.proc0.subproc0> grep CRAB_TransferOutputs *submit
Job.0-1.submit:My.CRAB_TransferOutputs = 1
Job.0-1.submit:My.CRAB_TransferOutputs = 0
Job.0-2.submit:My.CRAB_TransferOutputs = 1
Job.0-2.submit:My.CRAB_TransferOutputs = 0
Job.0-3.submit:My.CRAB_TransferOutputs = 1
Job.0-3.submit:My.CRAB_TransferOutputs = 0
Job.0-4.submit:My.CRAB_TransferOutputs = 1
Job.0-4.submit:My.CRAB_TransferOutputs = 0
Job.0-5.submit:My.CRAB_TransferOutputs = 1
Job.0-5.submit:My.CRAB_TransferOutputs = 0
Job.submit:My.CRAB_TransferOutputs = 1
belforte@vocms059/cluster10126689.proc0.subproc0> 
```
yet submitted jobs have the wrong value
```console
belforte@vocms059/cluster10126689.proc0.subproc0> condor_q -con crab_reqname==\"250220_123754:belforte_crab_20250220_133751\" -af CRAB_TransferOutputs 
1
undefined
1
1
1
1
1
belforte@vocms059/cluster10126689.proc0.subproc0> 
```

## Comment (belforte, 2025-02-20T13:28:22Z)

maybe lines added in JDL file after the `queue` statement are ignored ?
Yes, Sigh
```console
belforte@vocms059/SPOOL_DIR> condor_q -con crab_reqname==\"250220_123754:belforte_crab_20250220_133751\" -af DESIRED_SITES
undefined
undefined
undefined
undefined
undefined
undefined
undefined
belforte@vocms059/SPOOL_DIR> 
```

## Comment (belforte, 2025-02-20T13:32:37Z)

Need a bit more care in PreJob to make sure that `queue\n` stays as the last line.
I lean toward reading `Job.submit` into an `htcondor.Submit()` object, manipulate it, write it out as `Job.x.submit`
And avoid all that line manipulation.

I.e. I  will also take this chance to change `new_submit_text` into a `newJobSubmit` object and complete transition to modern HTC condor API also in PreJob.

## Comment (belforte, 2025-02-24T11:49:55Z)

After reformatting PreJob, now automatic splitting works and probe job stdout has
```
====== Sun Feb 23 16:38:14 2025: cmscp.py STARTING.
The user has not specified to transfer the log files. No log files stageout (nor log files metadata upload) will be performed.
The user has specified to not transfer the output files. No output files or logs stageout (nor output files metadata upload) will be performed.
Stageout wrapper has no work to do. Finishing here.
Setting stageout wrapper exit info to {'exit_code': 0, 'exit_acronym': 'OK', 'exit_msg': 'OK'}.
Cannot retrieve the job exit code from the job report (does None exist?).
====== Sun Feb 23 16:38:14 2025: cmscp.py FINISHING (status 0).
```

Need to do 
- [x] small cleanup in DagmanCreator: CRAB_Site*list should be `"site,site,site.."` not `'{"site", "site", "site",...}'` . Since those ads are simly for our diagnostics, not used anywhere, and so no need for the odd format. I.e. use same format as DESIRED_SITES
- [x] check for regression
   - [x] make some processing job fail to check tails  for automatic splitting
   - [x] check that new PreJob correctly propagates resubmission params
      - [x] jobids
      - [x]  whitelist
      - [x] blacklist   
      - [x] maxmemory
      - [x] maxjobruntime
      - [x] priority

## Comment (belforte, 2025-02-25T08:04:17Z)

CCV tests found a problem with `IgnoreLocality`
```text
Task name:			250225_001010:crabint1_crab_ignoreLocality
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/250225_001010%3Acrabint1_crab_ignoreLocality
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=crabint1&var-task=250225_001010%3Acrabint1_crab_ignoreLocality&from=1740438610000&to=now
Task bootstrapped at 2025-02-25 00:14:33 UTC. 1353 seconds ago
Task bootstrapped on schedd more than 22 minutes ago
```
PreJob failed with
```text
Tue, 25 Feb 2025 01:14:34 CET(+0100):ERROR:PreJob Can not submit since DESIRED_Sites list is empty
```
info in DB is OK

![Image](https://github.com/user-attachments/assets/38fcd381-00f4-4478-8f1a-ff1097cb3e8b)

## Comment (belforte, 2025-02-25T13:24:07Z)

above problem fixed with more "PreJob cleanup". Now pipeline is OK https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/10875440

## Comment (belforte, 2025-02-27T08:51:56Z)

I am reasonably hopeful that last commit is final now. Making a PR while pipeline runs
https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/10902770
