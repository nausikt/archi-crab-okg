# dmwm/CRABServer issue #8693: automatic splitting produce input file list with duplicates

State: closed
Opened: 2024-09-05T09:07:04Z
Closed: 2024-09-12T16:47:14Z
Labels: Type: Bug, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8693

## Opening post (belforte, 2024-09-05T09:07:04Z)

reference: https://cms-talk.web.cern.ch/t/duplicate-events-in-mini-nano-process/47484

This [task](https://cmsweb.cern.ch/crabserver/ui/task/240829_122306%3Aalobanov_crab_TTtoLNu2Q)
resulted in same file being listed N times for tail jobs
e.g. from https://cmsweb.cern.ch:8443/scheddmon/0119/alobanov/240829_122306:alobanov_crab_TTtoLNu2Q/job_out.1-17.0.txt
file `/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/4e0a48d7-e6f6-42d9-9a13-b688da03dc19.root` is listed 47 times in `Set attribute process.source.fileNames to cms.untracked.vstring(`

The problem is not "just with tail jobs". already [Job 1](https://cmsweb.cern.ch:8443/scheddmon/0119/alobanov/240829_122306:alobanov_crab_TTtoLNu2Q/job_out.1.0.txt) had an amazing list of duplicates
![image](https://github.com/user-attachments/assets/d30589ad-fc49-485d-beac-5e2ade2a75e8)

## Comment (belforte, 2024-09-05T10:07:59Z)

hmm. preadag.0.txt already has
Thu, 29 Aug 2024 15:50:54 CEST(+0200):INFO:PreDAG average eventsize for 5 jobs: 3170.8 bytes
Thu, 29 Aug 2024 15:50:54 CEST(+0200):DEBUG:JobFactory About to load files by DAO
Thu, 29 Aug 2024 15:50:56 CEST(+0200):DEBUG:JobFactory About to commit 29 jobGroups
Thu, 29 Aug 2024 15:50:56 CEST(+0200):DEBUG:JobFactory About to commit 1 jobs
Thu, 29 Aug 2024 15:50:56 CEST(+0200):WARNING:Splitter The input dataset contains the following dupl
icated lumis dict_keys([(1, 4), (1, 11), (1, 669), (1, 703),....
and a very long list follows
then there's this message which I do not know what it means exactly

Thu, 29 Aug 2024 15:50:56 CEST(+0200):WARNING:TaskAction CRAB detected lumis split across files in t
he input dataset. Will apply the necessary corrections in the splitting algorithm. You can ignore th
is message.

that comes from
https://github.com/dmwm/CRABServer/blob/ce559a11ef02c447f909ee166b7d48f218eb021d/src/python/TaskWorker/Actions/Splitter.py#L92-L100

I do not know where "necessary corrections" will be applied

## Comment (belforte, 2024-09-05T10:17:22Z)

this is where possibly everything happens
https://github.com/dmwm/WMCore/blob/213189431a6aeae29781429eb0478e79e2de8664/src/python/WMCore/JobSplitting/LumiBased.py#L82-L105

indeed [predag.0.txt](https://cmsweb.cern.ch:8443/scheddmon/0119/alobanov/240829_122306:alobanov_crab_TTtoLNu2Q/SPOOL_DIR/prejob_logs/predag.0.txt) is full of messages like
Thu, 29 Aug 2024 15:50:55 CEST(+0200):WARNING:LumiBased Skipping runlumi pair (1, 703) as it was already been processed.Will add /store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/83387792-3d10-4bed-9acc-346be670f881.root to the input files of the job processing the lumi

## Comment (belforte, 2024-09-05T10:58:24Z)

hmm.. as I wrote in [cms-talk](https://cms-talk.web.cern.ch/t/duplicate-events-in-mini-nano-process/47484/8?u=belforte)

The problem does not seem related to automatic splitting and quite possibly originates from the fact that many (all?) lumis are duplicated in different file of the input dataset [1].
I have not done the test, but suspect that a simple “split by lumi” would have been resulted in similar duplication.

WMCore’s SplittingFactory expects a lumi to be present in one file only and when it detects it in multiple files, it assumes that it was an exceptional situation where it has been split and that those files contains independent sets of events which together make up the full lumi content

I do not fully understand how exactly this may end up with the same input file being list many tens of times to same job (once for every lumi ??). But can’t really try to understand all WMCore internals.

Since this is a SIM dataset, I imgaine that it was simply created in two steps, every time starting lumicout at 1. Run number is always 1 for SIM.

So that the current task may have actually processed only half (?) of the generated sample.

Given my limited understanding, and the fact that setting of lumi numbers in SIM is not a strictly controlled process, I suggest to process SIM in splitByFile mode.

Stefano

[1]

>>> import dbs.apis.dbsClient as dbsClient
>>> dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader'
>>> dbs = dbsClient.DbsApi(url=dbsUrl)
Password for /afs/cern.ch/user/b/belforte/.globus/userkey.pem: 
>>> dset='/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
>>> len(dbs.listFiles(dataset=dset, run_num=1, lumi_list=[10]))
2
>>> len(dbs.listFiles(dataset=dset, run_num=1, lumi_list=[1]))
2
>>> len(dbs.listFiles(dataset=dset, run_num=1, lumi_list=[700]))
2
>>>

## Comment (belforte, 2024-09-05T15:00:58Z)

I submitted a test task on same input dataset using LumiSplit
 https://cmsweb-testbed.cern.ch/crabserver/ui/task/240905_132511%3Abelforte_crab_20240905_152505
TW found the list of duplicated lumis and I have the same message 
```
Warning:			CRAB detected lumis split across files in the input dataset.
Will apply the necessary corrections in the splitting algorithm. You can ignore this message.
```
But I did not get the
```
WARNING:LumiBased Skipping runlumi pair (1, 703) as it was already been processed.
Will add ... to the input files of the job processing the lumi
```
and the list of input files in job stdout looks normal

It may depend on the number of requested lumis per job, I set it to 1000. Alas PreDag log does not say which value it picked

## Comment (belforte, 2024-09-05T16:11:34Z)

automatic splitting uses `EventAwareLumiBased` splitting. User task had 739 jobs in the processing stage, dataset has [89455475](https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset+dataset%3D%2FTTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8%2FRun3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2%2FMINIAODSIM) events

So I try EventAwareLumiBased with 100K events per job (rounded) https://cmsweb-testbed.cern.ch/crabserver/ui/task/240905_160708%3Abelforte_crab_20240905_180703

But again TW log indicates the duplicates lumis, but no msg of the kind ` Skipping runlumi pair (1, 703) as it was already been processed`

And job stdout does not indicate duplicate filenames.

## Comment (belforte, 2024-09-05T16:37:29Z)

I do not have the stamina nor the time now to dig into PreDag in debug mode and follow things up inside WMCore's splitting factory.

Last thing is to verify reproducibility using in crabConfig
```python
config.Data.inputDataset = '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
config.Data.splitting = 'Automatic'
config.Data.totalUnits = -1
config.Data.unitsPerJob = 200
```
in https://cmsweb-testbed.cern.ch/crabserver/ui/task/240905_163528%3Abelforte_crab_20240905_183524

## Comment (belforte, 2024-09-05T17:24:18Z)

indeed now PreDag0.txt looks "as bad as in Artur's task"
and although different in the details the situation in the `input_files.tar.gz` is similarly bad
``` 
cat job_input_file_list_170.txt|tr , '\n'|sort|uniq -c|sort -n|cut -c 1-80|tail
      3  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
      4  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
      4  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
      4  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
      5  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
      7  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
     10  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
     11  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
     12  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
     16  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythi
```

## Comment (belforte, 2024-09-05T17:24:50Z)

I have to defer more digging to some future time

## Comment (belforte, 2024-09-11T10:05:44Z)

increase priority, I better do it while I am fresh of "looking at it"

## Comment (belforte, 2024-09-12T15:34:54Z)

running [PreDag with pdb](https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3OperatorDebugging#To_run_the_preDag_on_the_schedd)  all the lines like

WARNING:LumiBased Skipping runlumi pair (1, 43499) as it was already been processed.
Will add /store/mc/.... 046ccf32-c3b9-4cf6-93ba-62f0afc8f0e5.root to the input files of the job processing the lumi

come from Line 67 here
https://github.com/dmwm/CRABServer/blob/ce559a11ef02c447f909ee166b7d48f218eb021d/src/python/TaskWorker/Actions/Splitter.py#L65-L68

## Comment (belforte, 2024-09-12T15:55:25Z)

As feared, following code inside WMCore/JobSplitting/EventAwareLumiBased.py is very painful.
In automatic splitting the PreDag runs the splitter/job factories with 68732 avgEventsPerJob.
I can also try to use that in a plain task with ` EventAwareLumiBased` splitting. 
https://cmsweb-testbed.cern.ch/crabserver/ui/task/240912_155659%3Abelforte_crab_20240912_175652

## Comment (belforte, 2024-09-12T16:47:03Z)

OK. At last I can reproduce the problem with plain `EventAwareLumiBased` and this in the crab config. file
```python
config.Data.inputDataset = '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 68732
```
the above task does not have the messages from Splitter about filed being added, maybe something to do with debug level, I will have to check. But there are the feared duplicates in many (not all) jobs input file list. Same as for automatic splitting.
Looking at content of various file  in input_files_tar.gz and counting number of files (words) in each, I get this for EALS = EventAwareLuminositySplit and AUTO=AutomaticSplit for two "representative" jobs
```
belforte@vocms059/belfo> cat EALS/job_input_file_list_131.txt|tr , '\n'|sort|uniq -c|sort -n|tail -5
     10  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2540000/992f1c67-0c10-42b0-a36d-c22ab5c6a46a.root"
     14  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2540000/d649b7e1-da1c-4b71-89c0-fc33d6b144ba.root"
     23  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/787551b2-92e6-4d22-a637-d628f3a5a27a.root"
     24  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/98541904-b447-4894-91cd-183a5efd47d9.root"
     26  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/ee22e8bd-bdfd-4451-b95d-380fef23cb00.root"
belforte@vocms059/belfo> cat AUTO/job_input_file_list_66.txt|tr , '\n'|sort |uniq -c|sort -n|tail -5
      1 ["/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/9dd0dd6a-b48d-445e-a219-ae6125660120.root"
      1  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/ba9a82a8-fba7-4654-b7d8-38e976444f71.root"
      2  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/2540000/162d6c8c-9b44-4f5f-bdfc-bf27cd7b9955.root"
      7  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/5503f76d-ea9b-42b6-99b3-a96295005b4d.root"
     59  "/store/mc/Run3Summer22MiniAODv4/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/15212077-46ed-46d2-ba43-1f5db6a04a7f.root"
belforte@vocms059/belfo> 
```

Not all jobs have those duplications, but clearly they are not specific of automatic splitting and come straight from WMCore's splitting.

Bottom line: the present of so many duplicated lumis in input creates a mess !

## Comment (belforte, 2024-09-12T16:47:14Z)

Bottom line: the present of so many duplicated lumis in input creates a mess !
