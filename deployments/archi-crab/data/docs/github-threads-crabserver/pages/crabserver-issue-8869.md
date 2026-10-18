# dmwm/CRABServer issue #8869: use input_args.json file in CMSRunAnalysis.py via --jobId arg

State: closed
Opened: 2025-01-08T11:43:50Z
Closed: 2025-01-20T14:54:56Z
URL: https://github.com/dmwm/CRABServer/issues/8869

## Opening post (belforte, 2025-01-08T11:43:50Z)

Get rid of the awful long arg list in Job.submit (ref. https://github.com/dmwm/CRABClient/issues/5288#issuecomment-2577345857)
`
Arguments = "-a $(CRAB_Archive) --sourceURL=$(CRAB_ISB) --jobNumber=$(CRAB_Id) --cmsswVersion=$(CRAB_JobSW) --scramArch=$(CRAB_JobArch) '--inputFile=$(inputFiles)' '--runAndLumis=$(runAndLumiMask)' --lheInputFiles=$(lheInputFiles) --firstEvent=$(firstEvent) --firstLumi=$(firstLumi) --lastEvent=$(lastEvent) --firstRun=$(firstRun) --seeding=$(seeding) --scriptExe=$(scriptExe) --eventsPerLumi=$(eventsPerLumi) --maxRuntime=$(maxRuntime) '--scriptArgs=$(scriptArgs)' -o $(CRAB_AdditionalOutputFiles)"
`
and make it possible to use instead simply `--jobId=$(CRAB_Id)`

Now every task has `input_args.json` in its spool dir, so add it to list of `transfer_input_files` in `Job.submit` and add the new arg to CMSRunAnalysis.py

This will also allow to simplify the `RunJobs.dag` file where all those env.vars. are defined
`
VARS Job1 count="1" runAndLumiMask="job_lumis_1.json" lheInputFiles="False" firstEvent="None" firstLumi="None" lastEvent="None" firstRun="None" maxRuntime="-60" eventsPerLumi="None" seeding="AutomaticSeeding" inputFiles="job_input_file_list_1.txt" scriptExe="None" scriptArgs="[]" +CRAB_localOutputFiles="\"kk.root=kk_1.root\"" +CRAB_DataBlock="\"/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM#3517e1b6-76e3-11e7-a0c8-02163e00d7b3\"" +CRAB_Destination="\"davs://eoscms.cern.ch:443/eos/cms/store/user/belforte/GenericTTbar/crab_20241216_165508/241218_101115/0000/log/cmsRun_1.log.tar.gz, davs://eoscms.cern.ch:443/eos/cms/store/user/belforte/GenericTTbar/crab_20241216_165508/241218_101115/0000/kk_1.root\""
`

Since everything is in `input_args.json` !

- [x] start by adding the new `jobId` arg so can test along current code
   - [x] modify CMSRunAnalysis.py and test with preparelocal
   - [x] modify Job.submit in DagmanCreator to transfer input_args.json (circa line 570) and replace args list with --jobId
- [ ] eventually remove old code and possibly rename `--jobId` to `--jobNumber`

## Comment (belforte, 2025-01-13T18:08:06Z)

harder than it looked. Can't have a single `input_args.json` since for automatic splitting each subdag will need different one. Can maybe keep adding ?

## Comment (belforte, 2025-01-15T20:47:33Z)

my branch https://github.com/belforte/CRABServer/tree/use-jobid-arg-for-CMSRunAnalysis-8869
now has something that I more or less like and works for "traditional" DAGs. Need to worry about automatic splitting subdags. I lean toward making one new input_args_X.json file for each, like done for the RunJobX.dag files
But have to be careful with the "common" Job.submit since subdags may start when the processing dag has not submitted all jobs yet, i.e. not all PreJobs have run and not all Job.N.submit have been created for it (or any other previous subdag).

One possibility is to insert the input_args.json in the PreJob picking the correct json file. But in order to keep CMSRunAnalysis scripts simple and for mind sanity it is better that file in the WN have constant names.

Back to ... add new jobs to same input_args.json as they are created by DagmanCreator

## Comment (belforte, 2025-01-16T00:00:28Z)

task which worked: https://cmsweb-test2.cern.ch/crabserver/ui/task/250115_234857%3Abelforte_crab_20250116_004851

## Comment (belforte, 2025-01-16T17:53:02Z)

making automatic splitting work is still tricky because of lots of old code which is not broken but likely useless. E.g. there are some arguments to CMSRunAnalysis like `CRAB_ISB=sourceURL` which are never used
But I prefer to make it work touching only DagmanCreator first, then cleanup.

## Comment (belforte, 2025-01-17T00:55:36Z)

first task with automatic splitting which submitted the processing DAG and completed successfully
https://cmsweb-test2.cern.ch/crabserver/ui/task/250117_002140%3Abelforte_crab_20250117_012136

## Comment (belforte, 2025-01-17T17:52:18Z)

rats... creation of tail dag gets stuck insite PreDag at
```text

[crabtw@vocms059 SPOOL_DIR]$ cat prejob_logs/predag.1.txt 
Fri, 17 Jan 2025 18:26:19 CET(+0100):INFO:PreDAG Pre-DAG started with output redirected to /data/srv/glidecondor/condor_local/spool/3940/0/cluster10053940.proc0.subproc0/prejob_logs/predag.1.txt
Fri, 17 Jan 2025 18:26:19 CET(+0100):INFO:PreDAG found 25 completed jobs
Fri, 17 Jan 2025 18:26:19 CET(+0100):INFO:PreDAG jobs remaining to process: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 3, 4, 5, 6, 7, 8, 9
Fri, 17 Jan 2025 18:26:19 CET(+0100):INFO:PreDAG jobs remaining to process: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 3, 4, 5, 6, 7, 8, 9
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG average throughput for 22 jobs: 5286.660909090909 evt/s
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG average eventsize for 22 jobs: 19.863636363636363 bytes
/usr/lib64/python3.9/tarfile.py:2268: RuntimeWarning: The default behavior of tarfile extraction has been changed to disallow common exploits (including CVE-2007-4559). By default, absolute/parent paths are disallowed and some mode bits are cleared. See https://access.redhat.com/articles/7004769 for more details.
  warnings.warn(
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG Adding lumis from failed job 9
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG Adding lumis from failed job 11
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG Adding lumis from failed job 13
Fri, 17 Jan 2025 18:26:29 CET(+0100):DEBUG:JobFactory About to load files by DAO
[crabtw@vocms059 SPOOL_DIR]$ 
```

i.e. inside Splitter

## Comment (belforte, 2025-01-19T17:44:23Z)

Big mistery, I even tried to kill the predag and the dag bootstrap, but now I find that log is completed, 3 tails had been submittedf and completed finely
https://cmsweb-test2.cern.ch/crabserver/ui/task/250117_123553%3Abelforte_crab_20250117_133547

`predag.1.txt` has
```text
Fri, 17 Jan 2025 18:26:19 CET(+0100):INFO:PreDAG Pre-DAG started with output redirected to /data/srv/glidecondor/condor_local/spool/3940/0/cluster10053940.proc0.subproc0/prejob_logs/predag.1.txt
Fri, 17 Jan 2025 18:26:19 CET(+0100):INFO:PreDAG found 25 completed jobs
Fri, 17 Jan 2025 18:26:19 CET(+0100):INFO:PreDAG jobs remaining to process: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 3, 4, 5, 6, 7, 8, 9
Fri, 17 Jan 2025 18:26:19 CET(+0100):INFO:PreDAG jobs remaining to process: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 3, 4, 5, 6, 7, 8, 9
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG average throughput for 22 jobs: 5286.660909090909 evt/s
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG average eventsize for 22 jobs: 19.863636363636363 bytes
/usr/lib64/python3.9/tarfile.py:2268: RuntimeWarning: The default behavior of tarfile extraction has been changed to disallow common exploits (including CVE-2007-4559). By default, absolute/parent paths are disallowed and some mode bits are cleared. See https://access.redhat.com/articles/7004769 for more details.
  warnings.warn(
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG Adding lumis from failed job 9
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG Adding lumis from failed job 11
Fri, 17 Jan 2025 18:26:20 CET(+0100):INFO:PreDAG Adding lumis from failed job 13
Fri, 17 Jan 2025 18:26:29 CET(+0100):DEBUG:JobFactory About to load files by DAO
Fri, 17 Jan 2025 19:16:36 CET(+0100):DEBUG:JobFactory About to commit 3 jobGroups
Fri, 17 Jan 2025 19:16:36 CET(+0100):DEBUG:JobFactory About to commit 1 jobs
Fri, 17 Jan 2025 19:16:36 CET(+0100):INFO:PreDAG Splitting results:
Fri, 17 Jan 2025 19:16:36 CET(+0100):INFO:PreDAG Created jobgroup with length 1
Fri, 17 Jan 2025 19:16:36 CET(+0100):INFO:PreDAG Created jobgroup with length 1
Fri, 17 Jan 2025 19:16:36 CET(+0100):INFO:PreDAG Created jobgroup with length 1
Fri, 17 Jan 2025 19:16:36 CET(+0100):INFO:RucioUtils Initializing native Rucio client
Fri, 17 Jan 2025 19:16:36 CET(+0100):DEBUG:RucioUtils Using cert [/data/srv/glidecondor/condor_local/spool/3940/0/cluster10053940.proc0.subproc0/c6ea75e904ebb26531217d954bd562c96db20c11]
 and key [/data/srv/glidecondor/condor_local/spool/3940/0/cluster10053940.proc0.subproc0/c6ea75e904ebb26531217d954bd562c96db20c11] for rucio client.
Fri, 17 Jan 2025 19:16:36 CET(+0100):INFO:RucioUtils Rucio server v.35.6.0 contacted
Fri, 17 Jan 2025 19:16:36 CET(+0100):INFO:RucioUtils Rucio client initialized for belforte in status ACTIVE
Fri, 17 Jan 2025 19:16:36 CET(+0100):DEBUG:DagmanCreator starting createSubdag, kwargs are:
Fri, 17 Jan 2025 19:16:36 CET(+0100):DEBUG:DagmanCreator {'task': {'tm_taskname': '250117_123553:belforte_crab_20250117_133547', 'tm_task_status': 'HOLDING', 'tm_task_command': 'SUBMIT', 'tm_start_time': 1737117379, 'tm_start_injection': '', 'tm_end_injection': '', 'tm_task_failure': None, 'tm_job_sw': 'CMSSW_13_3_0', 'tm_job_arch': 'el8_amd64_gcc12',
[....]
an AMAZINGLY LONG list of lumis !
[....] Until
Fri, 17 Jan 2025 19:16:37 CET(+0100):DEBUG:DagmanCreator Acquired lock on run and lumi tarball
Submitting job(s).
1 job(s) submitted to cluster 10053976.
WARNING: the line 'RemoveKillSig = SIGUSR1' was unused by condor_submit. Is it a typo?
WARNING: the line 'OnExitRemove = ( ExitSignal =?= 11 || (ExitCode =!= UNDEFINED && ExitCode >=0 && ExitCode <= 2))' was unused by condor_submit. Is it a typo?
WARNING: the line 'JobUniverse = 7' was unused by condor_submit. Is it a typo?

-----------------------------------------------------------------------
File for submitting this DAG to HTCondor           : RunJobs1.subdag.condor.sub
Log of DAGMan debugging messages                   : RunJobs1.subdag.dagman.out
Log of HTCondor library output                     : RunJobs1.subdag.lib.out
Log of HTCondor library error messages             : RunJobs1.subdag.lib.err
Log of the life of condor_dagman itself            : RunJobs1.subdag.dagman.log

-----------------------------------------------------------------------
Fri, 17 Jan 2025 19:16:42 CET(+0100):DEBUG:PreDAG PreDAG lock released
Ended TaskManagerBootstrap with code 0
[crabtw@vocms059 SPOOL_DIR]$ 

``

SO maybe it is all OK.
I will submit same task again and let it run overnight

## Comment (belforte, 2025-01-19T18:01:47Z)

new automatic splitting test with branch  https://github.com/belforte/CRABServer/tree/use-jobid-arg-for-CMSRunAnalysis-8869
task:
https://cmsweb-test2.cern.ch/crabserver/ui/task/250119_180101%3Abelforte_crab_20250119_190055

## Comment (belforte, 2025-01-20T08:00:42Z)

task ran finely, even if again spending almost 40 min on Splitting
```text
Sun, 19 Jan 2025 23:21:00 CET(+0100):DEBUG:JobFactory About to load files by DAO
Sun, 19 Jan 2025 23:58:29 CET(+0100):DEBUG:JobFactory About to commit 1 jobGroups
```

For peace of mind I am submitting same task to prod scheduler
https://cmsweb.cern.ch/crabserver/ui/task/250120_080014%3Abelforte_crab_20250120_090007

## Comment (belforte, 2025-01-20T14:53:40Z)

the task which ran in productions still spend an amazing amount of time in Splitter
```text
Mon, 20 Jan 2025 14:26:43 CET(+0100):DEBUG:JobFactory About to load files by DAO
Mon, 20 Jan 2025 15:21:53 CET(+0100):DEBUG:JobFactory About to commit 1 jobGroups
```
anyhow speeding up AutomaticSplittting is not a goal, nor likely possible nor useful.

So I conclude that new code is working as well as old one  and will merge #8883
