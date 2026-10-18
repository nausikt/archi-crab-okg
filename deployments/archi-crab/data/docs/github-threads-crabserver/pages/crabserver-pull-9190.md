# dmwm/CRABServer pull request #9190: Refresh input s3 cache while running PreDAG

State: closed
Opened: 2025-09-24T08:10:13Z
Closed: 2025-09-26T19:30:21Z
Merged: 2025-09-26T19:30:21Z
URL: https://github.com/dmwm/CRABServer/pull/9190

## Opening post (nausikt, 2025-09-24T08:10:13Z)

In response to https://github.com/dmwm/CRABClient/issues/5413.

when crab report fails in case of automatic splitting, cause by the missing of user's jobs lumis, input_file in S3.
```bash
File job_lumis_1.json not found in run_and_lumis.tar.gz
File job_input_file_list_1.txt not found in input_files.tar.gz
ERROR: KeyError: '1'
```

Actually *0*, parent dag idx, was properly uploaded to s3 cache during first boostrapping once but it just our parent dag (CRAB matter) reached to s3, Other ***1++*** parent_idx/job_ids were missing. (so called User specific jobs/DAG part).
```bash
[kphornsi@lxplus975 temp_krittin]$ tar -zxvf input_files.tar.gz
job_input_file_list_0-1.txt
job_input_file_list_0-2.txt
job_input_file_list_0-3.txt
job_input_file_list_0-4.txt
job_input_file_list_0-5.txt
```

Thus, we just have to refresh cache again once user's DAG was completely settled. 

And at the end of PreDAG (as you hint) also be a good timing. 
_______
Things might could be done better from my side:
1. me wrapping this refresh cache as function.
2. make it recursively pick ups important files, and update it in hierarchically manner? make it more generic refresh cache function.
3. wrapping as new TaskAction like Uploader, but this one aim to be more generic and reusable for people how want to refresh S3 cache keep things in SPOOL_DIR/WEB_DIR in sync. (every time we need checkpoint.)

All in all, I'm trying not to overdo it. so please let me hear your thoughts on these. @belforte

## Comment (cmsdmwmbot, 2025-09-24T08:12:44Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2633/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-09-24T08:38:15Z)

what about implementing the simple solution instead ?

## Comment (cmsdmwmbot, 2025-09-24T13:24:49Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2634/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-09-24T18:46:14Z)

HI @sinonkt 
with reference to this afternoon chat, let me "persist" here some pointers and a bit of clarification.
The handling of `run_and_lumis.tar.gz` and `input_files.tar.gz` is described in comments in DagmanCreator, please have a look and let me know if you find them obscure, wrong, or otherwise needing improvements:
https://github.com/dmwm/CRABServer/blob/cf85a3fd59282b9fcac9e7ffe41a0650444bb4d0/src/python/TaskWorker/Actions/DagmanCreator.py#L796-L837
https://github.com/dmwm/CRABServer/blob/cf85a3fd59282b9fcac9e7ffe41a0650444bb4d0/src/python/TaskWorker/Actions/DagmanCreator.py#L720-L728

In the same file there is a very terse explanation of why you could nevertheless find f `run_and_lumis.tar.gz`  in the SPOOL_DIR
https://github.com/dmwm/CRABServer/blob/cf85a3fd59282b9fcac9e7ffe41a0650444bb4d0/src/python/TaskWorker/Actions/DagmanCreator.py#L773-L775

The comment there is correct,  but insufficient. I could have extracted the file from the tarball in PostJob as well and keep SPOOL_DIR "more clean". I did not do that because PreDag is executed only a couple of times in the life of a task, but PostJob is potentially executed  thousands of times, I am afraid that adding tar/untar/zip/unzip in there adds too much I/O on SPOOL disk which is already stressed. And all in all there is surely no harm in keeping a few more files in SPOOL_DIR.

I wait to add comments in DagmanCreator for that, in case you have other suggestions or requests.

Kindly let me know

## Comment (nausikt, 2025-09-24T19:02:25Z)

> HI @sinonkt with reference to this afternoon chat, let me "persist" here some pointers and a bit of clarification. The handling of `run_and_lumis.tar.gz` and `input_files.tar.gz` is described in comments in DagmanCreator, please have a look and let me know if you find them obscure, wrong, or otherwise needing improvements:
> 
> https://github.com/dmwm/CRABServer/blob/cf85a3fd59282b9fcac9e7ffe41a0650444bb4d0/src/python/TaskWorker/Actions/DagmanCreator.py#L796-L837
> 
> 
> https://github.com/dmwm/CRABServer/blob/cf85a3fd59282b9fcac9e7ffe41a0650444bb4d0/src/python/TaskWorker/Actions/DagmanCreator.py#L720-L728
> 
> In the same file there is a very terse explanation of why you could nevertheless find f `run_and_lumis.tar.gz` in the SPOOL_DIR
> 
> https://github.com/dmwm/CRABServer/blob/cf85a3fd59282b9fcac9e7ffe41a0650444bb4d0/src/python/TaskWorker/Actions/DagmanCreator.py#L773-L775
> 
> The comment there is correct, but insufficient. I could have extracted the file from the tarball in PostJob as well and keep SPOOL_DIR "more clean". I did not do that because PreDag is executed only a couple of times in the life of a task, but PostJob is potentially executed thousands of times, I am afraid that adding tar/untar/zip/unzip in there adds too much I/O on SPOOL disk which is already stressed. And all in all there is surely no harm in keeping a few more files in SPOOL_DIR.
> 
> I wait to add comments in DagmanCreator for that, in case you have other suggestions or requests.
> 
> Kindly let me know

Thank you Stefano! I will have careful read there.

BTW, my job got into `rescheduled as tail jobs` status what does it means in this case? 

after i patch PR, both of my submitted tasks got into this status. Does it just natural expected behaviour of automatic splitting to launch multiple round of probes sometimes? or it's clear sign of something went wrong with this PR.

## Comment (belforte, 2025-09-24T19:10:14Z)

`rescheduled as tail` is a normal step, but should not last indefinitely

## Comment (nausikt, 2025-09-24T19:12:56Z)

I've digged into prejob_logs but there's no obvious clues at my first glances. 

it's not totally indefinitely yet, it just start their second round.

HELP url : https://cmsweb-test14.cern.ch/crabserver/ui/task/250924_173645%3Akphornsi_crab_ReportFailsWhenAutomaticSplittingTest14Fix6666Final

## Comment (belforte, 2025-09-24T19:23:07Z)

I looked up your latest task. It seems to suffer of confusion in out file handling. I am not sure why PostJob submits an ASO requests that fails in that [very odd way](https://cmsweb.cern.ch/scheddmon/069/kphornsi/250924_173645:kphornsi_crab_ReportFailsWhenAutomaticSplittingTest14Fix6666Final/postjob.1.0.txt), maybe is a problem related to execution site T1_PL_NCBJ ? but you should remove this line from your config
```
config.JobType.disableAutomaticOutputCollection = True
```
And make sure that things work with non-automatic splitting, for peace of mind.
I also suggest to use a white list like `T2_US*, T2_IT*, T2_DE*, T2_UK*, T2_FR_*, T2_ES*` to avoid marginal sites which may confuse the picture with their own failures.

## Comment (belforte, 2025-09-24T19:26:45Z)

see "ASO log" in https://cmsweb.cern.ch/scheddmon/069/kphornsi/250924_173645:kphornsi_crab_ReportFailsWhenAutomaticSplittingTest14Fix6666Final/SPOOL_DIR/task_process/transfers/transfer_inject.log

The tail job ran at CNAF and also failed in ASO step since the "source RSE" was T1_IT_CNAF which does not exists, should have been T1_IT_CNAF_Disk.

I have no idea what's going on !

## Comment (nausikt, 2025-09-24T19:28:25Z)

> I looked up your latest task. It seems to suffer of confusion in out file handling. I am not sure why PostJob submits an ASO requests that fails in that [very odd way](https://cmsweb.cern.ch/scheddmon/069/kphornsi/250924_173645:kphornsi_crab_ReportFailsWhenAutomaticSplittingTest14Fix6666Final/postjob.1.0.txt), maybe is a problem related to execution site T1_PL_NCBJ ? but you should remove this line from your config
> 
> ```
> config.JobType.disableAutomaticOutputCollection = True
> ```
> 
> And make sure that things work with non-automatic splitting, for peace of mind. I also suggest to use a white list like `T2_US*, T2_IT*, T2_DE*, T2_UK*, T2_FR_*, T2_ES*` to avoid marginal sites which may confuse the picture with their own failures.

Roger that Stefnao, That
```bash
config.JobType.maxMemoryMB = 5000
config.JobType.disableAutomaticOutputCollection = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 4

# also
config.Data.publication = True
config.Data.splitting = 'Automatic'
config.Data.ignoreLocality = False
```
I copied from user reported failed automatic splitting task, to imitate and reproduced this crab report failed case.

That's true, `T1_*` is there in whitelist, as part of my daily routine test task though.

## Comment (belforte, 2025-09-24T19:31:31Z)

OK. These lines in PostJob log explain

Wed, 24 Sep 2025 20:00:54 CEST(+0200):INFO:PostJob ====== Starting upload of logs archive file metadata.
Wed, 24 Sep 2025 20:00:54 CEST(+0200):WARNING:PostJob Temporary storage site for logs archive file not defined in job report. This is expected if there was no attempt to stage out the file into a temporary storage. Will use the executed site as the temporary storage site in the file metadata.

You have this extremely unusual configuration where you do not ask to transfer output, but ask to transfer logs. CRAB is not handling that correctly, the above fallback to `executed site as temporary storage site` (not my code FWIW) works for T2's and T3's, which have same name for execution site and disk, but fails for T1's.

Feel free to open a bug in GH.  But I am not sure we want to fix it.

## Comment (nausikt, 2025-09-24T19:33:26Z)

Okk, will fix my config instead and let you know.

## Comment (nausikt, 2025-09-24T19:34:07Z)

Thank you so much that's save me decades!

## Comment (belforte, 2025-09-24T19:36:38Z)

your white list is not bad
`config.Site.whitelist = ['T1_*', 'T2_US_*', 'T2_IT_*', 'T2_DE_*', 'T2_ES_*', 'T2_FR_*', 'T2_UK_*']`

but the combination of "executing at  T1" and "transfer logs but not output" triggered the bug.

You should also disable transfer of log files, it is a useless waste, I am sure you never read them from CERNBOX !
Simply remove
`config.General.transferLogs = True`
the default is False and is good.

## Comment (nausikt, 2025-09-24T19:40:06Z)

> your white list is not bad `config.Site.whitelist = ['T1_*', 'T2_US_*', 'T2_IT_*', 'T2_DE_*', 'T2_ES_*', 'T2_FR_*', 'T2_UK_*']`
> 
> but the combination of "executing at T1" and "transfer logs but not output" triggered the bug.
> 
> You should also disable transfer of log files, it is a useless waste, I am sure you never read them from CERNBOX ! Simply remove `config.General.transferLogs = True` the default is False and is good.

Got it, new non-Automatic splitting task with `TransferLogs=False`, `config.JobType.disableAutomaticOutputCollection=False` are on their way, expect simply completed. then switch to Automatic once again.

## Comment (belforte, 2025-09-24T19:40:56Z)

> I've digged into prejob_logs but there's no obvious clues at my first glances.

I guess you meant "predag".
It seems that predag worked finely. The problem is that all jobs are failing in the ASO step.
Probe jobs were OK because for those transfer of output AND log are forcefully disabled.

## Comment (belforte, 2025-09-24T19:44:55Z)

you can simply remove this line. The default is to parse the PSet and automatically find from it
the list of output files to retrieve (output.root in your case). The idea is that users can set this extra-config
to True in case their PSet descrived (also) files which they do not need, in which case an explicit list
of output file names must be supplied.
```
config.JobType.disableAutomaticOutputCollection=False
```

Better not to have in the config lines which you do not understand. And of course ask me if you are in doubt as to what they mean after having looked in https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

## Comment (nausikt, 2025-09-24T19:47:30Z)

> you can simply remove this line. The default is to parse the PSet and automatically find from it the list of output files to retrieve (output.root in your case). The idea is that users can set this extra-config to True in case their PSet descrived (also) files which they do not need, in which case an explicit list of output file names must be supplied.
> 
> ```
> config.JobType.disableAutomaticOutputCollection=False
> ```
> 
> Better not to have in the config lines which you do not understand. And of course ask me if you are in doubt as to what they mean after having looked in https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

My bad, sorry i should not put any flag in any task unless truly understood them.

Better consult twiki next time, Krittin learned his lesson!

## Comment (nausikt, 2025-09-25T13:48:13Z)

@belforte Ciao Stefano, 

I've work grounded up from non-Automatic-Splitting task first, it was completed well.
Then, i made very minor changed to the config as following to submit in automatic splitting mode. 
```python
config.Data.splitting = 'Automatic'
# config.JobType.maxJobRuntimeMin = 60
# config.Data.unitsPerJob = 1
# config.Data.totalUnits = 10
```

PreDag and first round probe jobs and their corresponding Pre/PostJobs were completed fine.
```
Thu, 25 Sep 2025 15:36:45 CEST(+0200):INFO:PreDAG Pre-DAG started with output redirected to /data/srv/glidecondor/condor_local/spool/7349/0/cluster1637349.proc0.subproc0/prejob_logs/predag.0.txt
Thu, 25 Sep 2025 15:36:45 CEST(+0200):INFO:PreDAG found 0 completed jobs
Thu, 25 Sep 2025 15:36:45 CEST(+0200):DEBUG:PreDAG PreDAG lock released
Ended TaskManagerBootstrap with code 4
```

It seems to me that it didn't starting the real jobs and get stuck indefinitely.
(*** some of my tasks took almost 4 hrs in Scheduler Status: "SUBMITTED" without clear sign of job failed / rescheduled)

Could you give me some hints or a typical working automatic splitting tasks configuration please?

Task URL: https://cmsweb-test14.cern.ch/crabserver/ui/task/250925_132459%3Akphornsi_crab_testAS

## Comment (nausikt, 2025-09-25T13:51:52Z)

Ohh my bad, jobs from dag.1 start popping up now. it possibly because my priority was low.

## Comment (belforte, 2025-09-25T14:26:33Z)

Can not be priority, you do not have that many jobs.  But keep in mind that cache is refreshed every 5 min and that it takes a few minutes for HTC to turn a job from Idle to Running even if there are CPU's available.

## Comment (nausikt, 2025-09-25T14:34:30Z)

I've tested on test14, [250925_132459:kphornsi_crab_testAS](https://cmsweb-test14.cern.ch/crabserver/ui/task/250925_132459%3Akphornsi_crab_testAS)

Since, job_lumis-{1++}, input_file_list-{1++} beyond probes job was properly included in S3 archive as expected now.
_____
[1] FWIW: our current code did some kind of *soft* overwritten to the archive via appending new entry, when we extracting `runtimefiles` again it will pick latest added entry (among same key/path). So our runtimefiles grow more than we expected like in this case `runtimefiles` size jumped from 1.6 MB to 2.2 MB. but i think it's tolerable in this case.  
```
[kphornsi@lxplus964 temp]$ tar -zxvf testAS.runtimefiles
CMSRunAnalysis.tar.gz
TaskManagerRun.tar.gz
RunJobs0.subdag
CMSRunAnalysis.tar.gz
```

## Comment (belforte, 2025-09-25T14:39:29Z)

Maybe we can adjust addFileToGzippedArchive to get rid of the duplicate ? If nothing else not to confuse poor dumb Stefano next times I do a `tar tf`

## Comment (nausikt, 2025-09-25T14:48:38Z)

`crab report` works as expected now. (** it took a bit too long for `transferring` to be done)
```
[kphornsi@lxplus964 crab_report_fails]$ crab report
Running crab status to fetch necessary information.
Rucio client intialized for account kphornsi
Will put report files in directory /tmp/crabStatusTracking/crab_testAS/results
Summary from successful jobs (i.e. in status 'finished'):
  Number of files processed: 46
  Number of events read: 993400
  Number of events written in EDM files: 993400
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Processed lumis written to processedLumis.json
Summary from output datasets in DBS:
  Number of events:
    /GenericTTbar/kphornsi-autotest-1758806696-94ba0e06145abd65ccb1d21786dc7e1d/USER: 0
  Files to process written to filesToProcess.json
  Files processed by successful jobs written to processedFiles.json
Additional report lumi files:
  Input dataset lumis (from DBS, at task submission time) written to inputDatasetLumis.json
  Lumis to process written to lumisToProcess.json
Log file is /tmp/crabStatusTracking/crab_testAS/crab.log
```

> Maybe we can adjust addFileToGzippedArchive to get rid of the duplicate ? If nothing else not to confuse poor dumb Stefano next times I do a `tar tf`

Acknowledge Stefano!, let me fix addFileToGzippedArchive here in this PR then, I used `tar tf` too but when comes to nested tar i haven't try it yet, will do. Thanks for pointed out!

## Comment (cmsdmwmbot, 2025-09-26T14:44:50Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2636/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-26T16:10:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 10 comments to review
 * Pycodestyle check: succeeded
   * 24 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2637/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-09-26T16:15:53Z)

I've fixed `addToGZippedTarfile`, now duplicated arcs will not be accumulated. they will be overwritten via rebuilding/cloning into the new tar gzip.

Also extensively tested and try to ensure robustness by let first arg be able to be provided as file paths. e.g. both of the following invocation should works just fine.
```
addToGZippedTarfile(['CMSRunAnalysis.tar.gz'], 'InputFiles.tar.gz')
addToGZippedTarfile(['./some/path/to/CMSRunAnalysis.tar.gz'], 'InputFiles.tar.gz')
```

[1] Before
```
(crab-py3) [kphornsi@lxplus948 python]$ tar tf InputFiles.tar.gz
CMSRunAnalysis.tar.gz
TaskManagerRun.tar.gz
RunJobs0.subdag
CMSRunAnalysis.tar.gz
```
[2] After 
```
(crab-py3) [kphornsi@lxplus948 python]$ tar tf InputFiles.tar.gz
TaskManagerRun.tar.gz
RunJobs0.subdag
CMSRunAnalysis.tar.gz
```
