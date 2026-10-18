# dmwm/CRABServer issue #9127: some of CCV_test_suite get stuck and keep failing on FileOpenError 8020

State: closed
Opened: 2025-07-08T13:33:41Z
Closed: 2025-07-08T14:44:04Z
URL: https://github.com/dmwm/CRABServer/issues/9127

## Opening post (nausikt, 2025-07-08T13:33:41Z)

Guys, don't know whether this is very common issue that some file might corrupted or failed sometimes due to inconsistent network/fs.
OR it could be related to our newly introduced site whitelist [#9120] in userInputFiles test case. @belforte any hints? Thanks!

```
[kphornsi@lxplus9116 CMSSW_13_0_2]$ crab status --instance=test14 --task=250708_105844:crabint1_crab_secondaryInputDataset
crab status requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_secondaryInputDataset/.requestcache not created, because it already exists.
Rucio client intialized for account kphornsi
CRAB project directory:         /eos/home-k/kphornsi/WORK/CMSSW_13_0_2/crab_secondaryInputDataset
Task name:                      250708_105844:crabint1_crab_secondaryInputDataset
Grid scheduler - Task Worker:   crab3@vocms059.cern.ch - crab-dev-tw05
Status on the CRAB server:      SUBMITTED
Task URL to use for HELP:       https://cmsweb-test14.cern.ch/crabserver/ui/task/250708_105844%3Acrabint1_crab_secondaryInputDataset
Dashboard monitoring URL:       https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=crabint1&var-task=250708_105844%3Acrabint1_crab_secondaryInputDataset&from=1751968724000&to=now
Status on the scheduler:        FAILED

Jobs status:                    failed                  100.0% (1/1)

No publication information (publication has been disabled in the CRAB configuration file)

Error Summary: (use crab status --verboseErrors for details about the errors)

1 jobs failed with exit code 8020
```
```
==== Execution FAILED at Tue Jul  8 13:11:31 2025 UTC ====
==== CMSSW JOB Execution completed at Tue Jul  8 13:11:31 2025 UTC ====
Application exit code: 5
==== Execution FINISHED at Tue Jul  8 13:11:31 2025 UTC ====
======== CMSSW OUTPUT STARTING ========
NOTICE: lines longer than 3000 characters will be truncated
== CMSSW: 08-Jul-2025 13:11:17 UTC  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root
== CMSSW: 08-Jul-2025 13:11:23 UTC  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root
== CMSSW: 08-Jul-2025 13:11:29 UTC  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root
== CMSSW: %MSG-w XrdAdaptorInternal:  AfterFile 08-Jul-2025 13:11:30 UTC pre-events
== CMSSW: Failed to open file at URL root://eoscms.cern.ch:1094//eos/cms/store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root?xrdcl.requuid=483da488-3252-4d07-9f79-bd85ba4eab54.
== CMSSW: %MSG
== CMSSW: %MSG-w XrdAdaptorInternal:  AfterFile 08-Jul-2025 13:11:30 UTC pre-events
== CMSSW: Failed to open file at URL root://eoscms.cern.ch:1094//eos/cms/store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root?tried=&xrdcl.requuid=c18203c1-60ba-4696-bdee-597dcace14cb.
== CMSSW: %MSG
== CMSSW: 08-Jul-2025 13:11:30 UTC  Initiating request to open file root://xrootd-cms.infn.it//store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root
== CMSSW: %MSG-w XrdAdaptorInternal:  AfterFile 08-Jul-2025 13:11:31 UTC pre-events
== CMSSW: Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root?tried=+1213xrootd-redic.pi.infn.it&xrdcl.requuid=8252276a-de38-4323-b9cb-fd7904b09504.
== CMSSW: %MSG
== CMSSW: %MSG-w XrdAdaptorInternal:  AfterFile 08-Jul-2025 13:11:31 UTC pre-events
== CMSSW: Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root?tried=+1213xrootd-redic.pi.infn.it,&xrdcl.requuid=4f638b06-f3e2-44bb-9418-579715dc511c.
== CMSSW: %MSG
== CMSSW: 08-Jul-2025 13:11:31 UTC  Closed file root://eoscms.cern.ch//eos/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root
== CMSSW: ----- Begin Fatal Exception 08-Jul-2025 13:11:31 UTC-----------------------
== CMSSW: An exception of category 'FileOpenError' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW:    [1] Constructing input source of type PoolSource
== CMSSW:    [2] Calling RootInputFileSequence::initTheFile()
== CMSSW:    [3] Calling StorageFactory::open()
== CMSSW:    [4] Calling XrdFile::open()
== CMSSW: Exception Message:
== CMSSW: Failed to open the file 'root://xrootd-cms.infn.it//store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root'
== CMSSW:    Additional Info:
== CMSSW:       [a] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://eoscms.cern.ch//eos/cms/store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root
== CMSSW:       [b] Input file root://xrootd-cms.infn.it//store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root could not be opened.
== CMSSW:       [c] XrdCl::File::Open(name='root://xrootd-cms.infn.it//store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] No servers are available to read the file.
== CMSSW: ' (errno=3011, code=400). No additional data servers were found.
== CMSSW:       [d] Last URL tried: root://cms-xrd-global.cern.ch:1094//store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root?tried=+1213xrootd-redic.pi.infn.it,&xrdcl.requuid=4f638b06-f3e2-44bb-9418-579715dc511c
== CMSSW:       [e] Problematic data server: cms-xrd-global.cern.ch:1094
== CMSSW:       [f] Disabled source: cms-xrd-global.cern.ch:1094
== CMSSW: ----- End Fatal Exception -------------------------------------------------
== CMSSW:
== CMSSW:         Scram Command Diagnostic:
== CMSSW:         Command : scramv1
== CMSSW:         Architecture: el8_amd64_gcc11
== CMSSW:         Executed: stdbuf -oL -eL cmsRun -j FrameworkJobReport.xml PSet.py > cmsRun-stdout.log.tmp 2>&1
== CMSSW:         Exit Status: 5
== CMSSW:         Stdout:
== CMSSW:         Stderr: None
======== CMSSW OUTPUT FINISHING ========
==== Report file creation STARTING at Tue Jul  8 13:11:31 2025 UTC ====
Sanitize FJR
```

## Comment (belforte, 2025-07-08T13:36:50Z)

😲

## Comment (belforte, 2025-07-08T13:38:06Z)

indeed that file is not on CERN EOS now. ~But I believe that I checked when modifying the CCV test and it was there... for sure the file name is unchanged since a long time.~
```
belforte@lxplus806/~> ls /eos/cms/store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root
ls: cannot access '/eos/cms/store/mc/HC/GenericTTbar/GEN-SIM-RAW/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/BA3911AE-F275-E711-9F5E-FA163EE0AE95.root': No such file or directory
belforte@lxplus806/~> 
```

## Comment (nausikt, 2025-07-08T13:44:31Z)

Would you recommend changing the dataset in our test cases, or should we specify a different site (whitelist) that retains this dataset, instead of T2_CH_CERN?

## Comment (belforte, 2025-07-08T13:45:47Z)

I got confused. That has nothing to do with `inputUserFiles`. The test which fails is `secondaryInputDataset`  which uses `/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/GEN-SIM-RAW` which clearly was removed from disk [1].

There are only 3 ways forward:
1: remove the test
2: ask DM to place the dataset on CERN disk again
3. modify the test so that it takes this error as a sign of success.... all in all it means that CRAB did try to read from the what was indicated as secondary dataset ! So the Configuration was properly processed !

[1]
```
crab checkdataset --dataset /GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/GEN-SIM-RAW
```

## Comment (belforte, 2025-07-08T13:49:19Z)

hmm.... if I read my code correctly, 3. should be implemented already !
https://github.com/dmwm/CRABServer/blob/646fbd7bcada83b0624ed05c16055340b4973f1e/test/makeTests.py#L380-L387

did the test fail really  ? what do you mean by "get stuck" ? Can you point to the pipeline ?

## Comment (nausikt, 2025-07-08T13:51:50Z)

Ohhhhh, forgive me, i understood now. Thanks for hints..., and utility command.

> hmm.... if I read my code correctly, 3. should be implemented already !
> 
> [CRABServer/test/makeTests.py](https://github.com/dmwm/CRABServer/blob/646fbd7bcada83b0624ed05c16055340b4973f1e/test/makeTests.py#L380-L387)
> 
> Lines 380 to 387 in [646fbd7](/dmwm/CRABServer/commit/646fbd7bcada83b0624ed05c16055340b4973f1e)
> 
>  validationScript = """ 
>  checkStatus ${taskName} COMPFAIL 
>  statusCode=$? 
>  ([ $statusCode -eq 0 ] || [ $statusCode -eq 2 ]) || exit 1 
>  crabCommand getlog "--short --jobids=1 --proxy=$PROXY" 
>  lookFor "Retrieved job_out.1.*.txt" commandLog.txt || echo "secondaryInputDataset: Retrieval failure job_out.1.*.txt" 
>  lookFor "request to open.*GenericTTbar/GEN-SIM-RAW" "${workDir}/results/job_out.1.*.txt" || echo "secondaryInputDataset: Retrieval failure" 
>  """ 
> did the test fail really ? what do you mean by "get stuck" ? Can you point to the pipeline ?

Here's problematic job: https://gitlab.cern.ch/crab3/CRABServer/-/jobs/58496758
and task name...
```
crab status --instance=test14 --task=250708_105844:crabint1_crab_secondaryInputDataset
```

## Comment (nausikt, 2025-07-08T13:53:30Z)

In jobs_log.txt it keep terminating with exitcode 84 util DAG Abort...

## Comment (nausikt, 2025-07-08T14:04:10Z)

> I got confused. That has nothing to do with `inputUserFiles`. The test which fails is `secondaryInputDataset` which uses `/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/GEN-SIM-RAW` which clearly was removed from disk [1].
> 
> There are only 3 ways forward: 1: remove the test 2: ask DM to place the dataset on CERN disk again 3. modify the test so that it takes this error as a sign of success.... all in all it means that CRAB did try to read from the what was indicated as secondary dataset ! So the Configuration was properly processed !
> 
> [1]
> 
> ```
> crab checkdataset --dataset /GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/GEN-SIM-RAW
> ```

Since [3] was already implemented, can we have option [4]? that we point to other dataset that likely longstanding on disk.

## Comment (belforte, 2025-07-08T14:22:09Z)

It will not help. Secondary dataset must be a parent of primary or we will get errors anyhow. Can't pick one at random. And btw the only dataset which is guaranteed to be there long term is the one for HC tests which we use as input in all our tests.

## Comment (belforte, 2025-07-08T14:23:06Z)

> In jobs_log.txt it keep terminating with exitcode 84 util DAG Abort...

? why not 8020  line in the crab status which you pasted at the beginning ?

## Comment (belforte, 2025-07-08T14:28:29Z)

I think that the test failed becasue task was not completed nor failed. Even if the script really stinks, it is damn difficult to tell what exactly makes it fail here. But I do not like that we check for status 7 seconds after "task bootstrapped"

```text
Task bootstrapped at 2025-07-08 13:02:39 UTC. 7 seconds ago
Status information will be available within a few minutes
Log file is /home/gitlab-runner/shell/builds/t3_ZsMk1N/0/crab3/CRABServer/workdir/CMSSW_13_0_2/src/crab_secondaryInputDataset/crab.log
+ '[' 0 -ne 0 ']'
+ local isSub=0
+ local isDone=0
+ local isFailed=0
+ grep -q 'Status on the scheduler:.*SUBMITTED' statusLog.txt
+ grep -q 'Status on the scheduler:.*COMPLETED' statusLog.txt
+ grep -q 'Status on the scheduler:.*FAILED' statusLog.txt
+ case $targetStatus in
+ '[' 0 -eq 1 ']'
+ '[' 0 -eq 0 ']'
+ '[' 0 -eq 0 ']'
+ exit 1
``

## Comment (belforte, 2025-07-08T14:29:01Z)

I am re-running the test.
And indeed it succeeded :-)
https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12393787

## Comment (nausikt, 2025-07-08T14:35:20Z)

> > In jobs_log.txt it keep terminating with exitcode 84 util DAG Abort...
> 
> ? why not 8020 line in the crab status which you pasted at the beginning ?

Forgive me, the origin of error is 8020, exit-code 84 is just HTCondor universe i guessed...
```
Job terminated of its own accord at 2025-07-08T13:11:53Z with exit-code 84.
```

## Comment (nausikt, 2025-07-08T14:44:04Z)

> I am re-running the test. And indeed it succeeded :-) https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12393787

Thanks for your investigation efforts!(during your retirement time😭), 
Things are transparent to me now and I think your efforts put and end to this issue. Thanks again...

**Some background before Today's chaos**:
I've shoot my own foot by flooding both manual & automatic (from pipeline) submitted tasks into my test14 before manually retry ***run_testsuite_{CV|CCV}***

## Comment (belforte, 2025-07-08T14:44:23Z)

food for thought:
`mod(8020, 256)=84`  ! 
or, equivalently: `8020 % 255 = 84`

255 = FF hex = 11111111 binary (8 bits)

HTCondor universe is a completely different thing

## Comment (belforte, 2025-07-08T14:51:30Z)

the reason for the intial job failure is that the test is not prepared for
```
Task bootstrapped at 2025-07-08 13:02:39 UTC. 7 seconds ago
Status information will be available within a few minutes
```
so it failed to find the lines it was looking for in `crab status` output because the output information was not there.

This test is executed by the pipeline 20 minutes after submission, so the above is really odd. I am not sure what you flooded, but if you filled your TW with tasks from many different origins, it may have failed to keep up.

If you do not want this to happen to you anymore, feel free to provide a patch for the test. But I think we should only worry if it happens under normal conditions, not in extreme cases.

## Comment (nausikt, 2025-07-08T14:59:59Z)

> food for thought: `mod(8020, 256)=84` ! or, equivalently: `8020 % 255 = 84`
> 
> 255 = FF hex = 11111111 binary (8 bits)
> 
> HTCondor universe is a completely different thing

Thanks for food, So, 8020 is decimal (base 10) but somehow it has to truncated to 8 bits to fit HTCondor protocol...


> the reason for the intial job failure is that the test is not prepared for
> 
> ```
> Task bootstrapped at 2025-07-08 13:02:39 UTC. 7 seconds ago
> Status information will be available within a few minutes
> ```
> 
> so it failed to find the lines it was looking for in `crab status` output because the output information was not there.
> 
> This test is executed by the pipeline 20 minutes after submission, so the above is really odd. I am not sure what you flooded, but if you filled your TW with tasks from many different origins, it may have failed to keep up.
> 
> If you do not want this to happen to you anymore, feel free to provide a patch for the test. But I think we should only worry if it happens under normal conditions, not in extreme cases.

I'll better aware of this odd behavior and also not to pushed to extreme cases that much...

## Comment (belforte, 2025-07-08T15:07:32Z)

truncating exit codes to 8-bit is standard Linux shell behavior. It is not an htcondor peculiarity

## Comment (nausikt, 2025-07-08T15:17:04Z)

Its extreme obvious now... Thanks, I was so stuck with local minima idea of it's HTCondor things... so embarrassing! but good for self-awareness.
