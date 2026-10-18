# dmwm/CRABServer issue #8727: reorganize scripts directory, simplify creation of TW Tarballs

State: closed
Opened: 2024-09-30T16:28:45Z
Closed: 2025-08-25T10:26:19Z
Labels: Status: Done, Priority: High, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8727

## Opening post (belforte, 2024-09-30T16:28:45Z)

in current [scripts](https://github.com/dmwm/CRABServer/tree/master/scripts) directory we mix files uses for different purposes, which forces us to keep explicit lists of file names in [buildTWTarballs.sh](https://github.com/dmwm/CRABServer/blob/master/cicd/crabtaskworker_pypi/buildTWTarballs.sh)

Instead we can structure `scripts` so that there is a top directory for "things which need to go in the scheduler's SPOOL_DIR" and "things which need to go in the grid job directory"

That will simplify both tarball creations and use and will be safer against adding, renaming files.

See https://github.com/dmwm/CRABServer/issues/8699#issuecomment-2374495276

## Comment (belforte, 2024-09-30T16:31:10Z)

I paste here text from https://github.com/dmwm/CRABServer/issues/8699#issuecomment-2374495276 for convenience

add two subdirectories in CRABServer/scripts 
```text
scripts
├── dagman
│   └── task_process
└── job_wrapper
```
so that in https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/cicd/crabtaskworker_pypi/buildTWTarballs.sh#L76-L84

we only copy well named directories around, like done now for `task_process`

and also move expanding of job_wrapper tarball
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/scripts/CMSRunAnalysis.sh#L49

to the top wrapper script between these lines
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/scripts/gWMS-CMSRunAnalysis.sh#L225-L227

## Comment (belforte, 2024-09-30T16:40:12Z)

better do right after #6544 "while memory is fresh" so that I can capture all changes in a documentation #8728

## Comment (belforte, 2025-08-05T20:13:00Z)

my branch can submit and run a 1-job task now https://github.com/belforte/CRABServer/tree/reorganize-tw-tarballs

## Comment (belforte, 2025-08-06T12:32:06Z)

summary of changes:
* TW only creates two tar files: `TaskManagerRun.tar.gz` and `CMSRunAnalysis.tar.gz` . They contain "top level scripts" and all python dependencies in `WMCore.zip` and `CRAB3.zip`
* `setup.py` TaskWorker part has been modified not to reference "named files and directories" any more
* `CRAB3.zip` now contains all code in `src/python`
* files created by DagmanCreator and needed on the AP are added to tarballs
* list of input files to transfer in condor_submit is now down to bare minimum (one for AP, two for WN since we add user's sandbox)
* initial script in AP and WN expands tarballs, restoring current situation, so code runs as before
* a couple of files need to be extracted from tarballs in order to be used as command in `condor_submit`: `dag_bootstrap_startup.sh` for the AP is extracted by DagmanCreator, `gWMS-CMSRunAnalysis.sh` is extracted by `dag_bootstrap_startup.sh`

## Comment (belforte, 2025-08-06T12:39:43Z)

todo:
- [x] test Publisher
   - [x] schedd
   - [x] rucio
 - [ ] test with full tests in CI pipeline

## Comment (belforte, 2025-08-06T18:36:11Z)

found an issue: `crab report` tries to download `input_files.tar.gz` and `run_and_lumis.tar.gz` from WEB_DIR, but those are now inside `CMSRunAnalysis.tar.gz`
But this should not happen given https://github.com/dmwm/CRABClient/issues/5368

the problem is that `crab report` expects to find those  file at the  top level  in `InputFiles.tar.gz` not inside . But now 
```
[crabtw@vocms059 SPOOL_DIR]$ tar tf InputFiles.tar.gz
CMSRunAnalysis.tar.gz
TaskManagerRun.tar.gz
[crabtw@vocms059 SPOOL_DIR]$ 
```

Best  approach seems to modify `crab report` to expand those tarballs in the tmp directory where `InputFiles.tar.gz`is downloaded from S3.

Changes to `crab preparelocal` are also likely needed,so will have the usual 3 steps

1. change client to be forward compatible
2. change TaskWorket
3. cleanup client

addressed in https://github.com/dmwm/CRABClient/issues/5409 and step 3. will not be needed

## Comment (belforte, 2025-08-07T20:50:44Z)

Additionally automatic splitting fails with the following because DagmanCreator needs to update `input_args.json` with the arguments for the new jobs created by PreDAG

```
Wed, 06 Aug 2025 21:36:07 CEST(+0200):DEBUG:DagmanCreator Acquired lock on run and lumi tarball
Wed, 06 Aug 2025 21:36:07 CEST(+0200):DEBUG:DagmanCreator First iteration: creating run and lumi from scratch
Wed, 06 Aug 2025 21:36:07 CEST(+0200):DEBUG:DagmanCreator First iteration: creating inputfiles from scratch
Got a fatal exception: [Errno 2] No such file or directory: 'input_args.json'
Traceback (most recent call last):
  File "/usr/lib64/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib64/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/data/srv/glidecondor/condor_local/spool/5791/0/cluster10265791.proc0.subproc0/CRAB3.zip/TaskWorker/TaskManagerBootstrap.py", line 24, in <module>
  File "/data/srv/glidecondor/condor_local/spool/5791/0/cluster10265791.proc0.subproc0/CRAB3.zip/TaskWorker/TaskManagerBootstrap.py", line 18, in bootstrap
  File "/data/srv/glidecondor/condor_local/spool/5791/0/cluster10265791.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PreDAG.py", line 132, in execute
  File "/data/srv/glidecondor/condor_local/spool/5791/0/cluster10265791.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PreDAG.py", line 316, in executeInternal
  File "/data/srv/glidecondor/condor_local/spool/5791/0/cluster10265791.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/DagmanCreator.py", line 1102, in createSubdag
FileNotFoundError: [Errno 2] No such file or directory: 'input_args.json'
[crabtw@vocms059 prejob_logs]$ 
```

So I have two possibilities:
 1. ship input_args.json to the Job explicitly "at same level as CMSRunAnalysis.tar.gz 
 2. update it inside the CMSRunAnalysis.tar.gz tarball (a bit awkward: untar,, replace, tar again)
 
I will try 2. first, since is the cleanest

But need to take also of `run_and_lumis.tar.gz ` and `input_files.tar.gz` which both need new info when we create new jobs In this case the error happens in the job wrapper
```

==== Tweak PSet at Mon Aug 11 20:10:35 2025 UTC ====
Failed to get information from tarball run_and_lumis.tar.gz and file job_lumis_1.json. Error : "filename 'job_lumis_1.json' not found"
Failed to get information from tarball input_files.tar.gz and file job_input_file_list_1.txt. Error : "filename 'job_input_file_list_1.txt' not found"
```

## Comment (belforte, 2025-08-13T16:48:31Z)

my [branch](https://github.com/belforte/CRABServer/tree/reorganize-tw-tarballs) works (again) for normal tasks after heavy restructuring of DagmanCreator to deal with `run_and_lumis.tar.gz` and `input_files.tar.gz` in PreDag
Time to test again automatic splitting

## Comment (belforte, 2025-08-14T10:32:35Z)

almost works. It turns out that when using automatic splitting PostJon needs `runs_and_lumis.tar.gz` to know which lumis were meant to be processed so it can build list of lumis for tail stages.
```text
Thu, 14 Aug 2025 12:18:54 CEST(+0200):INFO:PostJob ====== Starting saving data for automatic splitting.
Thu, 14 Aug 2025 12:18:54 CEST(+0200):INFO:PostJob ====== Starting to parse the lumi file
Thu, 14 Aug 2025 12:18:54 CEST(+0200):ERROR:PostJob Failure during post-job execution.
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/3529/0/cluster10273529.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 1695, in execute
    retval, retmsg = self.execute_internal()
  File "/data/srv/glidecondor/condor_local/spool/3529/0/cluster10273529.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 2033, in execute_internal
    self.saveAutomaticSplittingData()
  File "/data/srv/glidecondor/condor_local/spool/3529/0/cluster10273529.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 1872, in saveAutomaticSplittingData
[...]
FileNotFoundError: [Errno 2] No such file or directory: 'run_and_lumis.tar.gz'
```

## Comment (belforte, 2025-08-15T09:46:48Z)

almost. I had missed these lines in PreDag which only come in to action for tail DAGs
https://github.com/dmwm/CRABServer/blob/ac6a37af7fa8fdedfbc9fbf0c1f424133bbc8927/src/python/TaskWorker/Actions/PreDAG.py#L365-L372

## Comment (belforte, 2025-08-15T20:02:28Z)

looks very promising now, tail jobs created and running

https://cmsweb-test2.cern.ch/crabserver/ui/task/250815_160213%3Abelforte_crab_20250815_180209

## Comment (belforte, 2025-08-16T13:44:39Z)

all OK

## Comment (belforte, 2025-08-16T13:51:36Z)

now.. should I extract `run_and_lumis.tar.gz` from JobWrapper tarball in dagaman_bootstrap_startup ? So that there is no need for changes in PostJob and PreDag ?
And maybe rename `CMSRunaAnalysis.tar.gz` to `JobWrapper.tar.gz` ?

## Comment (belforte, 2025-08-18T14:44:40Z)

expanding tarball in PreDag, which runs 3 times per task at most is OK. But PostJob runs thousands of times, esp. for automatic splitting. I think I better limit tar operations as much as possible. So will extract `run_and_lumis.tar.gz` in `dag_bootstrap_startup.sh`

## Comment (belforte, 2025-08-18T19:27:03Z)

Ouch. PreDag now adds more lumimask in ` run_and_lumis.tar.gz`, I can't keep using the one created in `dag_bootstrap_startup.sh`, need to keep in SPOOL_DIR the one which was last used in `condor_submit`.
